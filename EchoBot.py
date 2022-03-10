import telebot


TOKEN = '5257423133:AAEnuhj3wwmPv8GwziUx-E7tvPNutFfPYXk'

bot = telebot.TeleBot(TOKEN)

keys = {
    'биткоин': 'BTC',
    'эфириум': 'ETH',
    'доллар': 'USD',
}

class ConvertionException(Exception):
    pass

# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(content_types=['voice', ])
def repeat(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'Ты божественный')
pass

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Welcome, {message.chat.username}")


@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n.join((text, key, ))'
        bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    quote, base, among = message.text.split(' ')
    r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
    total_base = json.loads(r.content)[leys[base]]
    text = f'Цена {amouunt} {quote} в {base} - {total_base}'
    bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)