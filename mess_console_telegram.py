
import requests

# Замените 'YOUR_BOT_TOKEN' на ваш токен бота Telegram
bot_token = '5910001413:AAHPJArd-innwC9TmAIbMvioQIK5eqRcTMc'
#
# Получение последнего обновления
response = requests.get(f'https://api.telegram.org/bot{bot_token}/getUpdates')
data = response.json()
print(response.json)
# Извлечение последнего сообщения
if data['result']:

    last_update = data['result'][-1]
    last_message = last_update.get('message')

    if last_message:
        text = last_message.get('text')
        print(text)  # Вывод текста последнего сообщения
    else:
        print('Последнее обновление не содержит сообщения')
else:
    print('Нет сообщений')                                                                                                       
