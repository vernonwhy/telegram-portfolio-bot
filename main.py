from config import get_config_value
import request_service
import telegram_bot

account = get_config_value('ACCOUNT')
telegram_api_key = get_config_value('TELEGRAM_API_KEY')

def main():
    telegram_bot.start_bot(account)
    
    
if __name__ == '__main__':
    main()