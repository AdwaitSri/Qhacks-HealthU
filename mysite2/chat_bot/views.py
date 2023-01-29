from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse
import json
import os


data = json.loads(open('nf.json', 'r',encoding="utf8").read())
train = []
for k, row in enumerate(data):
    train.append(row['question'])
    train.append(row['answer'])
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
chatbot = ChatBot("QA",logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        }
    ])
trainer1 = ListTrainer(chatbot)
trainer1.train(train)
a = True
print("Hi there! How can I help?")
while a==True:
    request=input('You:')
    if request=="quit":
        break
    response = chatbot.get_response(request)
    print("HealthU: ", response)
        

# from django.shortcuts import render
# from django.shortcuts import redirect
# from django.contrib import messages
# from django.http import HttpResponse
# import json
# import os

# def index(request):
#     if request.method=='POST':
#         data = json.loads(open('nf.json', 'r').read())
#         train = []
#         for k, row in enumerate(data):
#             train.append(row['question'])
#             train.append(row['answer'])
#         from chatterbot import ChatBot
#         from chatterbot.trainers import ListTrainer
#         chatbot = ChatBot("QA",logic_adapters=[
#                 {
#                     'import_path': 'chatterbot.logic.BestMatch',
#                     'default_response': 'I am sorry, but I do not understand.',
#                     'maximum_similarity_threshold': 0.70
#                 }
#             ])
#         trainer1 = ListTrainer(chatbot)
#         trainer1.train(train[:10])
#         a = True
#         while a==True:
#             query=request.POST('query')
#             query=str(query)
#             if query=="quit":
#                 break
#             # response = chatbot.get_response(query)
#             # print("Bot: ", response)
#             # detail={'response':response}    
#         return render(request,'/index.html')













# Create your views here.
# from chatterbot import ChatBot  # to import chatterbot to python
# from chatterbot.trainers import ListTrainer
# chatbot = ChatBot("CoronaBot")  # "_name_" is the name of the chatbot


# conversation = [
#     "hello"
#     "Hi, how are you doing?",
#     "great",
#     "Glad to hear! How's your health?",
#     "not bad",
#     "Hope you are following the COVID guidelines for your area :)",
#     "yes I am",
#     "Did you try the N95 mask?",
#     "no",
#     "It's great and filters both the smallest and largest particles using charged fabric networks",
#     "thanks",
#     "Welcome! And *hint*: Do not wash your N95 mask with detergents or chemicals as it removes the static charge",
#     "alright",
#     "Also, regular soap water is more effective than sanitizers",
#     "I see",
#     "Try installing the aarogya setu app, it tracks potential corona carriers around your area using surveys",
#     "ok",
#     "Thank you",
#     "welcome"
# ]

# trainer = ListTrainer(chatbot)

# trainer.train(conversation)

# while True:
#     request = input('You: ')
#     response = chatbot.get_response(request)
#     print('CoronaBot:', response)











# Create your views here.
# from chatterbot import ChatBot  # to import chatterbot to python
# from chatterbot.trainers import ListTrainer
# chatbot = ChatBot("CoronaBot")  # "_name_" is the name of the chatbot


# conversation = [
#     "hello"
#     "Hi, how are you doing?",
#     "great",
#     "Glad to hear! How's your health?",
#     "not bad",
#     "Hope you are following the COVID guidelines for your area :)",
#     "yes I am",
#     "Did you try the N95 mask?",
#     "no",
#     "It's great and filters both the smallest and largest particles using charged fabric networks",
#     "thanks",
#     "Welcome! And *hint*: Do not wash your N95 mask with detergents or chemicals as it removes the static charge",
#     "alright",
#     "Also, regular soap water is more effective than sanitizers",
#     "I see",
#     "Try installing the aarogya setu app, it tracks potential corona carriers around your area using surveys",
#     "ok",
#     "Thank you",
#     "welcome"
# ]

# trainer = ListTrainer(chatbot)

# trainer.train(conversation)

# while True:
#     request = input('You: ')
#     response = chatbot.get_response(request)
#     print('CoronaBot:', response)