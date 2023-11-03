from chatterbot import ChatBot
from chatterbot.trainers import WikiTrainer

chatbot = ChatBot('mybot')


wiki_trainer = WikiTrainer(chatbot)

wiki_trainer.train('D:\\work\\wiki.tsv')

print('Training Complete')