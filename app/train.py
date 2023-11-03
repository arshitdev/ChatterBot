from chatterbot import ChatBot
from chatterbot.trainers import WikiTrainer

chatbot = ChatBot('mybot')


wiki_trainer = WikiTrainer(chatbot)

# train on english corpus data
# english.tsv and wiki.tsv files are in app folder
# wiki_trainer.train('D:\\work\\english.tsv')


wiki_trainer.train('D:\\work\\wiki.tsv')

print('Training Complete')