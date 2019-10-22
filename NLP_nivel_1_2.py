# -*- coding: utf-8 -*-

####################################################
########### IMPORTS ################################
####################################################
# from nltk.corpus import wordnet   #Para WORD_NOT_DETECTED

# KEYWORD EXTRACTION
# pip install monkeylearn
# from monkeylearn import MonkeyLearn
# ml = MonkeyLearn('2bb8c0268784df3103759bdc07ef33b87161fe9c')

# response = ml.classifiers.list(page=2, per_page=5, order_by=['-is_public', 'name'])
# print(response.body)

import rospy
from std_msgs.msg import ByteMultiArray
from std_msgs.msg import String



#################################################
############### SPEECH TO TEXT ##################
#################################################
 
 # Frase que o STT vai retornar

# stt = "Move to the bookshelf, find a person, and introduce yourself, move to the sidetable, grasp the Seven up and bring it to the couch table."






#################################################
######## COISAS QUE TEM NA COMPETIÇÃO ###########
#################################################


simple_words = ['the', 'to', 'and', 'a']


objects_a = ['kleenex', 'whiteboard cleaner', 'cup', 'snack', 'cereals bar', 'cookie', 'book', 'pen', 'notebook', 'laptop', 'tablet', 'charger',
            'pencil', 'peanut', 'biscuit', 'candy', 'chocolate bar', 'chewing gum', 'chocolate egg', 'chocolate tablet', 'donuts', 'cake', 'pie',
            'peach', 'strawberry', 'blueberry', 'blackberry', 'burger', 'lemon', 'lemon', 'banana', 'watermelon', 'pepper', 'pear', 'pizza',
            'yogurt', 'drink', 'beer', 'coke', 'sprite', 'sake', 'toothpaste', 'cream', 'lotion', 'dryer', 'comb', 'towel', 'shampoo', 'soap',
            'cloth', 'sponge', 'toothbrush', 'container', 'glass', 'can', 'bottle', 'fork', 'knife', 'bowl',
            'tray', 'plate', 'newspaper', 'magazine']

objects_an = ['almond', 'onion', 'orange', 'apple']

objects_the = ['cookies', 'almonds', 'book', 'pen', 'notebook', 'laptop', 'tablet', 'charger', 'pencil', 'chips', 'senbei', 'pringles',
            'peanuts', 'biscuits', 'crackers', 'candies', 'chocolate bar', 'manju', 'mints', 'chewing gums', 'chocolate egg', 'chocolate tablet',
            'donuts', 'cake', 'pie', 'food', 'peach', 'strawberries', 'grapes', 'blueberries', 'blackberries', 'salt', 'sugar', 'bread', 'cheese',
            'ham', 'burger', 'lemon', 'onion', 'lemons', 'apples', 'onions', 'orange', 'oranges', 'peaches', 'banana', 'bananas', 'noodles',
            'apple', 'paprika', 'watermelon', 'sushi', 'pepper', 'pear', 'pizza', 'yogurt', 'drink', 'milk', 'juice', 'coffee', 'hot chocolate',
            'whisky', 'rum', 'vodka', 'cider', 'lemonade', 'tea', 'water', 'beer', 'coke', 'sprite', 'wine', 'sake', 'toiletries', 'toothpaste',
            'cream', 'lotion', 'dryer', 'comb', 'towel', 'shampoo', 'soap', 'cloth', 'sponge', 'toilet paper', 'toothbrush', 'container', 'containers',
            'glass', 'can', 'bottle', 'fork', 'knife', 'bowl', 'tray', 'plate', 'newspaper', 'magazine', 'rice','kleenex', 'whiteboard cleaner', 'cup',
             'fresh', 'discs', 'chicken', 'tomato', 'sauce', 'dresser', 'cleaning', 'stuff']

objects_some = ['snacks', 'cookies', 'almonds', 'books', 'pens', 'chips', 'pringles', 'magazines', 'newspapers', 'peanuts', 'biscuits',
            'crackers', 'candies', 'mints', 'chewing gums', 'donuts', 'cake', 'pie', 'food', 'strawberries', 'grapes', 'blueberries',
            'blackberries', 'salt', 'sugar', 'bread', 'cheese', 'ham', 'lemons', 'apples', 'onions', 'oranges', 'peaches', 'bananas',
            'noodles', 'paprika', 'watermelon', 'sushi', 'pepper', 'pizza', 'yogurt', 'drink', 'milk', 'juice', 'coffee', 'hot chocolate',
            'whisky', 'rum', 'vodka', 'cider', 'lemonade', 'tea', 'water', 'beer', 'coke', 'sprite', 'wine', 'sake', 'toilet paper',
            'containers', 'glasses', 'cans', 'bottles', 'forks', 'knives', 'bowls', 'trays', 'plates', 'lemon', 'rice', 'cups', 'fanta']

objects_a_piece_of = ['apple', 'lemon', 'cake', 'pie', 'bread', 'cheese', 'ham', 'watermelon', 'sushi', 'pizza']

objects_a_cup_of = ['juice', 'rice', 'milk', 'coffee', 'hot chocolate', 'cider', 'lemonade', 'tea', 'water', 'beer']

objects_a_can_of = ['juice', 'kleenex', 'red bull', 'cider', 'iced tea', 'beer', 'coke', 'sprite', '7up']

objects_a_glass_of = ['milk', 'juice', 'coffee', 'hot chocolate', 'whisky', 'rum', 'vodka', 'cider', 'lemonade', 'tea', 'water', 'beer',
                    'coke', 'sprite', 'wine', 'sake']

objects_a_bottle_of = ['kleenex', 'milk', 'juice', 'whisky', 'rum', 'vodka', 'cider', 'lemonade',
                    'iced tea', 'water', 'beer', 'coke', 'sprite', 'wine','sake']

objects = list(set(objects_a + objects_the + objects_some + objects_an + objects_a_piece_of + objects_a_cup_of + objects_a_can_of + objects_a_bottle_of + objects_a_glass_of))
# ================================================================================================================
# locations
# ================================================================================================================
locations_on = ['nightstand', 'bookshelf', 'coffee','table', 'side', 'side', 'kitchen', 'cabinet',
                'tv stand', 'sofa', 'couch', 'bedroom','chair', 'kitchen', 'living','room', 'table', 'center','table',
                'drawer', 'desk', 'cupboard', 'side','shelf', 'bookcase', 'dining','table', 'fridge', 'counter',
                'cabinet', 'table', 'bedchamber', 'chair', 'dryer', 'oven', 'rocking chair', 'stove', 'television', 'bed', 'dressing table',
                'bench', 'futon', 'beanbag', 'stool', 'sideboard', 'washing machine', 'dishwasher', 'dinner']

locations_in = ['wardrobe', 'nightstand', 'bookshelf', 'dining room', 'bedroom', 'closet', 'living','room', 'bar', 'office',
                'drawer', 'kitchen', 'cupboard', 'side',' shelf', 'refrigerator', 'corridor', 'cabinet', 'bathroom', 'toilet', 'hall', 'hallway',
                'master','bedroom', 'dormitory','room', 'bedchamber', 'cellar', 'den', 'garage', 'playroom', 'porch', 'staircase', 'sunroom', 'music','room',
                'prayer',  'room', 'utility', 'shed', 'basement', 'workshop', 'ballroom', 'box', 'conservatory', 'drawing',
                'games room', 'larder', 'library', 'parlour', 'guestroom', 'crib', 'shower']

locations_at = ['wardrobe', 'nightstand', 'bookshelf', 'coffee table', 'side table', 'kitchen table', 'kitchen cabinet',
                'bed', 'bedside', 'closet', 'tv', 'stand', 'sofa', 'couch', 'bedroom chair', 'kitchen chair',
                'living room table', 'center table', 'bar', 'drawer', 'desk', 'cupboard', 'sink', 'side shelf',
                'bookcase', 'dining table', 'refrigerator', 'counter', 'door', 'cabinet', 'table', 'master bedroom', 'dormitory room',
                'bedchamber', 'chair', 'dryer', 'entrance', 'garden', 'oven', 'rocking chair', 'room', 'stove', 'television', 'washer',
                'cellar', 'den', 'laundry', 'pantry', 'patio', 'balcony', 'lamp', 'window', 'lawn', 'cloakroom', 'telephone', 'dressing table',
                'bench', 'futon', 'radiator', 'washing machine', 'dishwasher']

locations = list(set(locations_at+locations_in+locations_on + ['exit', 'apartment', 'trash', 'bin']))

# ================================================================================================================
# names
# ================================================================================================================
names_female = ['hanna', 'barbara', 'samantha', 'erika', 'sophie', 'jackie', 'skyler', 'jane', 'olivia', 'emily', 'amelia', 'lily',
                'grace', 'ella', 'scarlett', 'isabelle', 'charlotte', 'daisy', 'sienna', 'chloe', 'alice', 'lucy', 'florence', 'rosie',
                'amelie', 'eleanor', 'emilia', 'amber', 'ivy', 'brooke', 'summer', 'emma', 'rose', 'martha', 'faith', 'amy', 'katie',
                'madison', 'sarah', 'zoe', 'paige', 'mia', 'emily', 'sophia', 'abigail', 'isabella', 'ava']

names_male = ['ken', 'erik', 'samuel', 'skyler', 'brian', 'thomas', 'edward', 'michael', 'charlie', 'alex', 'john', 'james', 'oscar',
            'peter', 'oliver', 'jack', 'harry', 'henry', 'jacob', 'thomas', 'william', 'will', 'joshua', 'josh', 'noah', 'ethan', 'joseph',
            'samuel', 'daniel', 'max', 'logan', 'isaac', 'dylan', 'freddie', 'tyler', 'harrison', 'adam', 'theo', 'arthur', 'toby', 'luke',
            'lewis', 'matthew', 'harvey', 'ryan', 'tommy', 'michael', 'nathan', 'blake', 'charles', 'connor', 'jamie', 'elliot', 'louis',
            'aaron', 'evan', 'seth', 'liam', 'mason', 'alexander', 'madison']

names = list(set(names_male+names_female+ ['person', 'yourself', 'me']))

# ================================================================================================================
# what to tell
# ================================================================================================================
what_to_tell_about = ['name', 'nationality', 'eye color', 'hair color', 'surname', 'middle name', 'gender', 'pose', 'age', 'job', 'shirt color',
                     'height', 'mood']

what_to_tell_to = ["your teams affiliation", "your teams country", "your teams name", 'the day of the month','what day is today', 'what day is tomorrow', 'the time',
                    'the weather', 'that i am coming', 'to wait a moment', 'to come here', 'what time is it', 'a joke', 'something about yourself',
                    'the name of the person']

# ================================================================================================================
# intros
# ================================================================================================================
intros = ['robot', 'please', 'could you please', 'robot please', 'robot could you please', 'can you', 'robot can you',  'could you', 'robot could you']

tasks_go = ['go', 'navigate', 'proceed', 'move', 'advance', 'travel', 'drive', 'come', 'go near', 'walk']

tasks_take = ['take','grasp', 'pick up', 'pick', 'bring','bring me', 'give','put','deliver','get','place']

tasks_find = ['find', 'look', 'locate']

tasks_answer = ['answer']

tasks_tell = ['tell', 'tell me', 'say']

tasks_guide = ['guide']

tasks_introduce = ['introduce']

tasks_leave = ['leave']

all_tasks = tasks_go + tasks_take + tasks_find + tasks_answer + tasks_tell + tasks_introduce







###################################################################################
########################## Fazer para frases nivel 2 do GPSR ######################
###################################################################################

##### Wikipedia search
# import wikipedia
# wikipedia.summary("Facebook", sentences=1)

# frase =  "Bring me some Drink from a shelf"

# LOCATIONS
list_synonymous_some = ['some', 'any', 'few']
list_seating = ['bench']
list_table = ['hallway','side','table', 'kitchen', 'dinner', 'couch']
list_utensil=['bar']
list_shelf=['kitchen','counter', 'dresser', 'sideboard', 'bookshelf', 'pantry', 'cabinet']
list_appliance=['stove']

all_locations = list(set(list_seating + list_table + list_utensil+list_shelf+list_appliance + locations))


# CATEGORIES
list_Cleaning_stuff = ['deodorant', 'tooth', 'paste', 'cleaner', 'fresh','discs', 'sponge']
list_Drink = ['fanta','Beer can','coke', '7up', 'energy','drink', 'orange', 'juice', 'milk', 'apple','juice']
list_food = ['tomato', 'sauce','peanut','butter','chicken','marmelade','veggie','noodles', 'garlic', 'sauce']
list_Snack = ['chocolate', 'cookies', 'drops', 'crackers']

all_obj_categories = list(set(list_Cleaning_stuff + list_Drink + list_food + list_Snack + objects))







#######################################################
##########      PHRASE DIVIDER      ###################
#######################################################

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




########################################################
##########      INTENTION DETECTION     ################
########################################################



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






###########################################################################
#########################   SLOT FILLING   ################################
###########################################################################

def slot_filling(instruction):
    loc = []
    obj = []
    name = []
    dic = False
    obj_ant = False

    for word in instruction:
        if word in all_locations:
            loc.append(word)
            if len(loc) == 0:
            	dic = True
            # print(word)
        if word in all_obj_categories:
            obj.append(word)
            if len(obj) == 0:
            	dic = True
            # print(word)
        if word in names:
            name.append(word)
            if len(name) == 0:
            	dic = True
            # print(word)
        if word == 'it':  ######### objeto está instanciado na frase anterior
        	obj_ant = True
        
        if len(loc + obj + name) == 0:
        	dic = True

    return loc, obj, name, dic, obj_ant







###########################################################################
#########################   WORD NOT DETECTED   ###########################
###########################################################################

def word_not_detected(word_not_detected):

	syns = wordnet.synsets(word_not_detected)[0:1] 
	
	# print("\nSynonimous: ", syns, "\n")
	
	for i in enumerate(syns):
		print("WORD: ",syns[i[0]].lemmas()[0].name()) 
		print("DEFINITION: ", syns[i[0]].definition()) 
		print("EXAMPLE: ",syns[i[0]].examples())
		print("\n")








############################################################################
###########################     Funcao de tratamento - ROS   ###############
############################################################################

# def tratamento(msg): # toda vez que publicarem neste topico, esta funcão ira rodar
# 	data_valid = msg.data



############################################################################
###########################     MAIN    ####################################
############################################################################

class nlp_ros:
    
    def __init__(self, intention, lugar, objeto, name):
        self.intention = intention
        self.lugar = lugar
        self.objeto = objeto
        self.name = name
        self.string = String()
    
    def publish(self):
        self.pub = rospy.Publisher('chatter', String, queue_size=10)
        rospy.init_node('talker', anonymous=True)
        self.rate = rospy.Rate(1) # 1hz
        self.string = 'Intention:' + intention + ''
        while not rospy.is_shutdown():
            pub.publish()
            rate.sleep()
    



# rospy.init_node('Saida_NLP', anonymous=False)

# sub.data  = []
# sub = rospy.Subscriber('Entrada_NLP', str, tratamento)
# pub = rospy.Publisher('Saida_NLP', str, queue_size = 1)
# posso utilizar
# str, byte_multi_array, objeto



################################################################
##############     NLP -- MAIN CODE      #######################
################################################################

# stt = "Move to the bookshelf, find a person, and introduce yourself, Move to the side table, grasp the 7up and bring it to the couch table and kitchen is beautiful"

# stt = 'Move to the side table, grasp the 7up and bring it to the couch table'

# stt = "Move to the bench, grasp the Fanta and put it in the trash bin"

stt = 'Move to the side table, grasp the Marmelade and bring it to me.   '


phrase = divide_sentence_in_phrases(stt)

objeto_anterior = []
 
# Para cada frase na sentença...
for k, instruction in enumerate(phrase):
    print('Instrução: ',instruction, '\n')
    instruction = instruction.lower().split()
    intention = intention_detection(instruction) 
    print('Intention: ',intention, '\n')
    try:
    	instruction.remove(intention[1])
    except:
    	print('Nada para remover')
    # Tirando as simples words da frase
    for i, j in enumerate(simple_words):
    	if j in instruction:
    		instruction.remove(j)

    # SLOT FILLING FUNCTION
    slot = slot_filling(instruction)

    local = slot[0]
    objeto = slot[1]
    name = slot[2]
    dic = slot[3]
    obj_ant = slot[4]
    # print("Objeto Anterior: ", obj_ant, '\n')
    
    if obj_ant == True:
    	objeto = objeto_anterior
    	instruction.remove('it')

    else:
    	objeto_anterior = objeto
   
    
    all_str = local+objeto+name

    #Tirando as palavras slot-filing detectadas da frase
    for i, j in enumerate(all_str):
    	if j in instruction:
    		instruction.remove(j)
    
    ##################################
    ######### NIVEL 2: GPSR ##########
    ##################################
    
    if 'some' in instruction:
        instruction.remove('some')
        if objeto == 'drink':
            objeto = 'objeto do tipo que estiver lá' 
        
        elif objeto == 'cleaning':
            objeto = 'objeto do tipo que estiver lá'
        
        elif objeto == 'food':
            objeto = 'objeto do tipo que estiver lá'

        elif objeto == 'snack':
            objeto  = 'objeto do tipo que estiver lá'


    for i, k in enumerate(instruction):
        if 'from' == k:
            instruction.remove('from')
            try:
                local = instruction[i+1]
            except:
                print("Argumento do level 1")
    
    
    print('Slot Filling: LOCAL:', local, "OBJETO:", objeto, "NAME", name,'\n')
    
    msg = nlp_ros(intention, local, objeto, name)






    # print("NIVEL 2: Objeto:",objeto, "Local:", local)
    


    # Função 'word_not_detected' é ativada quando nao encontra o objeto ou lugar
    # Ela tem a função de procurar o significado e sinonimos da mesma
    # Ainda não esta corretamente aplicável ao código! 
    # Falta alguns ajustes

    # if dic == True:
    # 	for i, j in enumerate(instruction):
    # 		word_not_detected(j)
    
    print('Resto da frase: ', instruction)
    print(40*"##", '\n')



