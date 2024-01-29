from application.utilities.input_parser import input_parser
from application.libraries.Bot import Bot

bot = Bot()
text = "tolong buka aplikasi winrar lalu buka youtube"
actions = input_parser(text)

for action in actions:
    bot.run(**action)