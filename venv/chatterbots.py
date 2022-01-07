from chatterbot import ChatBot
from chatterbot.trainers import ChaterBotCorpusTrainer

chatbot = ChatBot('My_ChatBot')

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english.greetings" , "chatterbot.corpus.english.conversations")
response = chatbot.get_response('What is your Number?')
print(response)

response = chatbot.get_response('How are you doing')
print(response)
