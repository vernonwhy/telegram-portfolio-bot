import telebot
import request_service
from config import get_config_value

bot = None
account = None

def start_bot(accountId):
    telegram_api_token = get_config_value('TELEGRAM_API_KEY')
    bot = telebot.TeleBot(telegram_api_token)
    account = accountId
    
    @bot.message_handler(commands=['start'])
    def send_hello(message):
        bot.send_message(message.chat.id, 'Starting bot!')  
    
    @bot.message_handler(commands=['health'])
    def send_health(message):
        health = request_service.get_health_value(account)
        bot.send_message(message.chat.id, 'Your health value: ' + str(health))
  
    bot.polling()
    

