# -*- coding: utf-8 -*-


from collections import OrderedDict
import numpy as np
import spacy
from spacy.lang.en.stop_words import STOP_WORDS


nlp = spacy.load('en_core_web_sm')


################################ Intention detection words #####################################################################

intros = ['robot', 'please', 'could you please', 'robot please', 'robot could you please', 'can you', 'robot can you',  'could you', 'robot could you']

tasks_go = ['go', 'put', 'navigate', 'proceed', 'move', 'advance', 'travel', 'drive', 'come', 'go near', 'walk']

# 'put' inicialmente era uma terefa take

tasks_take = ['take','grasp', 'pick up', 'pick', 'bring','bring me', 'give','deliver','get','place']

tasks_find = ['find', 'look', 'locate']

tasks_answer = ['answer']

tasks_tell = ['tell', 'tell me', 'say']

tasks_guide = ['guide']

tasks_introduce = ['introduce']

tasks_leave = ['leave']

all_tasks = tasks_go + tasks_take + tasks_find + tasks_answer + tasks_tell + tasks_introduce


class TextRank4Keyword():
    """Extract keywords from text"""
    
    def __init__(self):
        self.d = 0.85 # damping coefficient, usually is .85
        self.min_diff = 1e-5 # convergence threshold
        self.steps = 10 # iteration steps
        self.node_weight = None # save keywords and its weight

    
    def set_stopwords(self, stopwords):  
        """Set stop words"""
        for word in STOP_WORDS.union(set(stopwords)):
            lexeme = nlp.vocab[word]
            lexeme.is_stop = True
    
    def sentence_segment(self, doc, candidate_pos, lower):
        """Store those words only in cadidate_pos"""
        sentences = []
        for sent in doc.sents:
            selected_words = []
            for token in sent:
                # Store words only with cadidate POS tag
                if token.pos_ in candidate_pos and token.is_stop is False:
                    if lower is True:
                        selected_words.append(token.text.lower())
                    else:
                        selected_words.append(token.text)
            sentences.append(selected_words)
        return sentences
        
    def get_vocab(self, sentences):
        """Get all tokens"""
        vocab = OrderedDict()
        i = 0
        for sentence in sentences:
            for word in sentence:
                if word not in vocab:
                    vocab[word] = i
                    i += 1
        return vocab
    
    def get_token_pairs(self, window_size, sentences):
        """Build token_pairs from windows in sentences"""
        token_pairs = list()
        for sentence in sentences:
            for i, word in enumerate(sentence):
                for j in range(i+1, i+window_size):
                    if j >= len(sentence):
                        break
                    pair = (word, sentence[j])
                    if pair not in token_pairs:
                        token_pairs.append(pair)
        return token_pairs
        
    def symmetrize(self, a):
        return a + a.T - np.diag(a.diagonal())
    
    def get_matrix(self, vocab, token_pairs):
        """Get normalized matrix"""
        # Build matrix
        vocab_size = len(vocab)
        g = np.zeros((vocab_size, vocab_size), dtype='float')
        for word1, word2 in token_pairs:
            i, j = vocab[word1], vocab[word2]
            g[i][j] = 1
            
        # Get Symmeric matrix
        g = self.symmetrize(g)
        
        # Normalize matrix by column
        norm = np.sum(g, axis=0)
        g_norm = np.divide(g, norm, where=norm!=0) # this is ignore the 0 element in norm
        
        return g_norm

    
    def get_keywords(self, number=10):
        """Print top number keywords"""
        keyword = []
        node_weight = OrderedDict(sorted(self.node_weight.items(), key=lambda t: t[1], reverse=True))
        for i, (key, value) in enumerate(node_weight.items()):
            # print(key + ' - ' + str(value))
            keyword.append(key)
            if i > number:
                break
        return keyword
        
        
    def analyze(self, text, 
                candidate_pos=['NOUN', 'PROPN'], 
                window_size=4, lower=False, stopwords=list()):
        """Main function to analyze text"""
        
        # Set stop words
        self.set_stopwords(stopwords)
        
        # Pare text by spaCy
        doc = nlp(text)
        
        # Filter sentences
        sentences = self.sentence_segment(doc, candidate_pos, lower) # list of list of words
        
        # Build vocabulary
        vocab = self.get_vocab(sentences)
        
        # Get token_pairs from windows
        token_pairs = self.get_token_pairs(window_size, sentences)
        
        # Get normalized matrix
        g = self.get_matrix(vocab, token_pairs)
        
        # Initionlization for weight(pagerank value)
        pr = np.array([1] * len(vocab))
        
        # Iteration
        previous_pr = 0
        for epoch in range(self.steps):
            pr = (1-self.d) + self.d * np.dot(g, pr)
            if abs(previous_pr - sum(pr))  < self.min_diff:
                break
            else:
                previous_pr = sum(pr)

        # Get weight for each node
        node_weight = dict()
        for word, index in vocab.items():
            node_weight[word] = pr[index]
        
        self.node_weight = node_weight


def divide_sentence_in_phrases(sentence):
    a = ''
    sentence = sentence.split()

    for k, i in enumerate(sentence):
        if i in all_tasks and k != 0:
            for j in all_tasks:
                if i == j:
                    a += ',' + i
        else:
            a += ' '+i

    return a.replace(' ,',',').replace(', and',',').replace('and ', ',').replace(',,', ',').replace(' and,',',').replace('.','').split(',')


def intention_detection(instruction):
    original_word = ''
    intention = ''
    for word in instruction:
        original_word = word
        # print(word)
        
        if word in tasks_go:
            # print('Intention: GO\n')
            intention = 'GO'
            break
        elif word in tasks_take:
            # print('Intention: TAKE\n')
            intention = 'TAKE'
            break
        elif word in tasks_find:
            # print('Intention: FIND\n')
            intention = 'FIND'
            break
        elif word in tasks_answer:
            # print('Intention: ANSWER\n')  
            intention = 'ANSWER'
            break
        elif word in tasks_tell:
            # print('Intention: TELL\n')
            intention = 'TELL'
            break
        elif word in tasks_introduce:
            # print('Intention: INTRODUCE\n')
            intention = 'INTRODUCE'
            break
        elif word in tasks_guide:
            # print('Intention: INTRODUCE\n')
            intention = 'GUIDE'
            break
        elif word in tasks_leave:
            # print('Intention: TELL\n')
            intention = 'LEAVE'
            break
        else:
            if(instruction[-1] == word):
                # print('No Intention Detected')
                intention = 'No_intention'
        if intention == 'No_intention':
            original_word = ''
        else:
            original_word = word
    
    return intention, original_word


def slot_filling(frase):
    tr4w = TextRank4Keyword()
    tr4w.analyze(frase, candidate_pos = ['NOUN', 'PROPN'], window_size=5, lower=False)
    slot = tr4w.get_keywords(10)

    return slot



##############################################################################################
#############################     MAIN CODE     ##############################################
#############################################################################################

# stt = "Move to the bookshelf, find a person, and introduce yourself, Move to the side table, grasp the 7up and bring it to the couch table and kitchen is beautiful"

# stt = 'Move to the side table, grasp the 7up and bring it to the couch table'

# stt = 'Move to the side table grasp the Marmelade and bring it to me.  '

# stt = "Move to the bench, grasp the Fanta and put it in the trash bin"

stt = 'Move to the stove, grasp the Apple juice and put it in the trash bin.'


###############################################################33

phrase = divide_sentence_in_phrases(stt)

#######################################################################33
all_content = []
simple_words = ['the', 'to', 'and', 'a']

for k, inst in enumerate(phrase):
    
    frase_nlp = []

    print('\nInstrução: ', inst)
    instruction = inst.lower().split()
    
############### Intention detection  ############
   
    intention = intention_detection(instruction)

    print('Intention Detection:', intention)
    
    try:
        instruction.remove(intention[1])
        frase_nlp.append(intention[0])
    except:
        print('Nada para remover e adicionar')

# Remove as simple_words ['the', 'to', 'and', 'a']

    for i, j in enumerate(simple_words):
        if j in instruction:
            instruction.remove(j)

################### Slot Filling ##############
    slot = slot_filling(str(instruction))
    try:
        for i in slot:
            instruction.remove(i)
            print(i, ' removed')
    except:
        print('Nada pra remover - slot filling')

    # print('Slot Filling: ',slot)

############# Ate aqui eh o basico #######################




############ PARTE DAS GAMBIARRAS   ################
    # faz referencia ao objeto anterior

    # if 'it' in instruction:
    #     try:
    #         slot = slot_antigo + slot
    #     except: 
    #         print("slot = slot antigo + slot")
    # else:
    #     slot_antigo = slot
    
# pega o 'me' da frase

    if 'me' in instruction:
        try:
            slot.append('me')
        except: 
            print("adicionando o 'me'")

    print('Slot Filling: ',slot)

    print('Resto: ',str(instruction))

# tratando o problema do 'side board'
    if len(instruction) != 0:
        slot_resto = slot_filling(str(instruction))
        print("Slot_resto: ",slot_resto)
        slot.append(slot_resto)
# colocando naquele esquema de lista de listas, matrix...

    for s in slot:
        frase_nlp.append(s)       
    
    all_content.append(frase_nlp)


print('\n', all_content)

