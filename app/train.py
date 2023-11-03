from chatterbot import ChatBot
from chatterbot.trainers import WikiTrainer

chatbot = ChatBot('mybot')


wiki_trainer = WikiTrainer(chatbot)

# train on english corpus data
# wiki_trainer.train('D:\\work\\english.tsv')


wiki_trainer.train('D:\\work\\wiki.tsv')

print('Training Complete')