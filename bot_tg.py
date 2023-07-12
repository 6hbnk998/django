
# token = 'your token'
# bot = telebot.TeleBot(token)




# @bot.message_handler(commands=['start'])
# @bot.message_handler(commands=['test'])
# def start_message(message):
#     bot.send_message(message.chat.id, 'Привет, я помогу тебе решить, что писать {name of your friend} из {name} ))))) ')





#     markup = telebot.types.InlineKeyboardMarkup()
#     markup.add(telebot.types.InlineKeyboardButton(text='Пивка для рывка?', callback_data=3))
#     markup.add(telebot.types.InlineKeyboardButton(text='Is London the capital of Great Britain?', callback_data=4))
#     markup.add(telebot.types.InlineKeyboardButton(text='Смотрел обзор Бэда?', callback_data=5))
#     markup.add(telebot.types.InlineKeyboardButton(text='Вкусно и точка,или невкусно и запятая(', callback_data=6))
#     bot.send_message(message.chat.id, text="Какую именно цитату ты бы отпрвила?", reply_markup=markup)

# @bot.callback_query_handler(func=lambda call: True)
# def query_handler(call):

#     bot.answer_callback_query(callback_query_id=call.id, text='Отличный выбор, так и пиши')
#     answer = ''
#     if call.data == '3':
#         answer = 'Доступные варианты: Жигулевское, Козел темный, Козел светлый'
        
#     elif call.data == '4':
#         answer = 'Не очень... : {name of the article}}'
#     elif call.data == '5':
#         answer = 'Да, он смотрел, вот ссылка : {name of the article}}'
#     elif call.data == '6':
#         answer = 'Вкусно блин и точка нафиг'


#     bot.send_message(call.message.chat.id, answer)





# bot.polling(non_stop=True)
