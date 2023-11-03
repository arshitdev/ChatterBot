from chatterbot import ChatBot

gbot = ChatBot('mybot',
                logic_adapters=[
                    {
                        'import_path': 'chatterbot.logic.BestMatch',
                        'default_response': 'I am sorry, but I do not understand.',
                        'maximum_similarity_threshold': 0.80
                    }
                ],
               read_only = True)

while True:
    uin = input('You: ')
    if uin.lower() in ('q', 'quit', 'exit'):
        break
    if uin.lower() in('bye', 'goodbye'):
        print('Babye')
        break
    try:
        gresponse = gbot.get_response(uin)
        print('Bot: ' + gresponse.text)
        print(gresponse.confidence)
    except:
        print('Error!')