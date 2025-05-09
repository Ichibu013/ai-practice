import spacy
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

myBot = ChatBot(
    name = 'PyBot',
    logic_adapter = ['chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch']
)

ListTrainer = ListTrainer(myBot)
corpurs_trainer = ChatterBotCorpusTrainer(myBot)

small_talk = [
    'hi',
    'hello',
    'how are you?',
    'i am good',
    'that is good to hear',
    'thank you',
    'you are welcome',
    'what is your name?',
    'i am PyBot',
    'what are you?',
    'i am a computer program',
    'what can you do?',
    'i can give information'
]

math_talk1 = [
    'pythagoreas therom'
    'In a right angle triangle, hypothenuse square in sum of base square and perpendicular square',
    'a^2 = b^2 + c^2'
]

math_talk2 = [
    'law of cosine',
    'c**2 = a**2 + b**2 - 2ab'
]

ListTrainer.train(small_talk)
ListTrainer.train(math_talk1)
ListTrainer.train(math_talk2)

corpurs_trainer.train('chatterbot.corpus.english')

print('Bot is ready to talk!! Type "exit" to leave')

while True:
    user_input = input('You : ')
    if user_input.lower() == 'exit':
        print('Exiting!!')
        break
    response = myBot.get_response(user_input)
    print('Bot : ', response)