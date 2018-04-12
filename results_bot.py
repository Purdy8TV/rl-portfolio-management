import telepot

# Required API Keys and Lists

# Telegram bot API - https://core.telegram.org/bots
bot_api = 'YOURBOTAPI'

# Telegram group chat ID
# https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id
chat_id = 'YOURCHATID'


class ResultsBot():

    def __init__(self, bot_api, chat_id):
        self.bot_api = bot_api
        self.chat_id = chat_id

    def init_bot(self):
        myBot = telepot.Bot(self.bot_api)
        return myBot

    def training_finished(self):
        myBot = self.init_bot()
        myBot.sendMessage(self.chat_id, 'Training Finished')
        myBot.sendPhoto(self.chat_id, photo=open('training_fig.png', 'rb'))

    def testing_finished(self):
        myBot = self.init_bot()
        myBot.sendMessage(self.chat_id, 'Testing Finished')
        myBot.sendPhoto(self.chat_id, photo=open('test_pandp.png', 'rb'))
        myBot.sendPhoto(self.chat_id, photo=open('test_weights.png', 'rb'))
        myBot.sendPhoto(self.chat_id, photo=open('test_costs.png', 'rb'))

    def best_comparison(self):
        myBot = self.init_bot()
        myBot.sendPhoto(self.chat_id, photo=open('best_fig.png', 'rb'))


thisBot = ResultsBot(bot_api, chat_id)
