import telebot
from telebot import *
import random
TOKEN = "TOKEN QO'yamiz"

bot = telebot.TeleBot(TOKEN)

@bot.messge_handler(commands = ['Start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
	item1 = types.KeyboardButton("Maktab darsliklari")
	item2 = types.KeyboardButton("Badiiy kitoblar")
	item3 = types.KeyboardButton("Bot dasturchisi")
	

	markup.add(item1, item2, item3)

	bot.send_message(message.chat.id, "Salom, {0.first_name}! 36-maktab darsliklari botiga xush kelibsiz!".format(message.from_user), reply_markup = markup)

@bor.messge_handler(content_types = ['text'])
def bot_message(message):
	if message.chat.type == 'private':
		if message.text == 'Maktab darsliklari':
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
			button1 =types.ReplyKeyboardMarkup("1-sinf")
			button2 =types.ReplyKeyboardMarkup("2-sinf")
			button3 =types.ReplyKeyboardMarkup("3-sinf")
			button4 =types.ReplyKeyboardMarkup("4-sinf")
			button5 =types.ReplyKeyboardMarkup("5-sinf")
			button6 =types.ReplyKeyboardMarkup("6-sinf")
			button7 =types.ReplyKeyboardMarkup("7-sinf")
			button8 =types.ReplyKeyboardMarkup("8-sinf")
			button9 =types.ReplyKeyboardMarkup("9-sinf")
			button10 =types.ReplyKeyboardMarkup("10-sinf")
			button11 =types.ReplyKeyboardMarkup("11-sinf")
			back =types.ReplyKeyboardMarkup("<-- ORQAGA")
			markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11)
			bot.send_message(message.chat.id, "Maktab darsliklari tanlandi!")

		elif message.text == "1-sinf":
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
			item1 = types.KeyboardButton('1-sinf Tarbiya')
			item2 = types.KeyboardButton("1-sinf Matematika")
			item3 = types.KeyboardButton("1-sinf Alifbe")
			item4 = types.KeyboardButton("1-sinf Yozuv daftari")
			item5 = types.KeyboardButton("1-sinf Matematika daftari")
			item6 = types.KeyboardButton("1-sinf Ona tili")
			item7 = types.KeyboardButton("1-sinf Tabiiy fan")
			item8 = types.KeyboardButton("1-sinf Ingliz tili")
			item9 = types.KeyboardButton("1-sinf Tasviriy san'at")
			item10 = types.KeyboardButton("1-sinf Texnologiya")
			item11 = types.KeyboardButton("1-sinf Jismoniy Tarbiya")
			back = types.KeyboardButton("<-- Orqaga")
			markup.add(item1, item2,item3,item4, item5, item6, item7, item8, item9, item10,item11, back)

			bot.send_message(message.chat.id, '1-sinf darsliklari tanlandi.', reply_markup = markup)

		elif message.text == "2-sinf":
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
			item1 = types.KeyboardButton('2-sinf Tarbiya')
			item2 = types.KeyboardButton("2-sinf Matematika")
			item3 = types.KeyboardButton("2-sinf O'qish")
			item4 = types.KeyboardButton("2-sinf Rus tili")
			item5 = types.KeyboardButton("2-sinf Matematika daftari")
			item6 = types.KeyboardButton("2-sinf Ona tili")
			item7 = types.KeyboardButton("2-sinf Tabiiy fan")
			item8 = types.KeyboardButton("2-sinf Ingliz tili")
			item9 = types.KeyboardButton("2-sinf Tasviriy san'at")
			item10 = types.KeyboardButton("2-sinf Texnologiya")
			item11 = types.KeyboardButton("2-sinf Jismoniy Tarbiya")
			back = types.KeyboardButton("<-- Orqaga")
			markup.add(item1, item2,item3,item4, item5, item6, item7, item8, item9, item10,item11, back)

			bot.send_message(message.chat.id, '2-sinf darsliklari tanlandi.', reply_markup = markup)

		elif message.text == "3-sinf":
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
			item1 = types.KeyboardButton('3-sinf Tarbiya')
			item2 = types.KeyboardButton("3-sinf Matematika")
			item3 = types.KeyboardButton("3-sinf O'qish")
			item4 = types.KeyboardButton("3-sinf Yozuv daftari")
			item5 = types.KeyboardButton("3-sinf Matematika daftari")
			item6 = types.KeyboardButton("3-sinf Ona tili")
			item7 = types.KeyboardButton("3-sinf Tabiiy fan")
			item8 = types.KeyboardButton("3-sinf Ingliz tili")
			item9 = types.KeyboardButton("3-sinf Tasviriy san'at")
			item10 = types.KeyboardButton("3-sinf Texnologiya")
			item11 = types.KeyboardButton("3-sinf Jismoniy Tarbiya")
			back = types.KeyboardButton("<-- Orqaga")
			markup.add(item1, item2,item3,item4, item5, item6, item7, item8, item9, item10,item11, back)

			bot.send_message(message.chat.id, '3-sinf darsliklari tanlandi.', reply_markup = markup)

		elif message.text == "4-sinf":
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
			item1 = types.KeyboardButton('4-sinf Tarbiya')
			item2 = types.KeyboardButton("4-sinf Matematika")
			item3 = types.KeyboardButton("4-sinf Alifbe")
			item4 = types.KeyboardButton("4-sinf Yozuv daftari")
			item5 = types.KeyboardButton("4-sinf Matematika daftari")
			item6 = types.KeyboardButton("4-sinf Ona tili")
			item7 = types.KeyboardButton("4-sinf Tabiiy fan")
			item8 = types.KeyboardButton("4-sinf Ingliz tili")
			item9 = types.KeyboardButton("4-sinf Tasviriy san'at")
			item10 = types.KeyboardButton("4-sinf Texnologiya")
			item11 = types.KeyboardButton("4-sinf Jismoniy Tarbiya")
			back = types.KeyboardButton("<-- Orqaga")
			markup.add(item1, item2,item3,item4, item5, item6, item7, item8, item9, item10,item11, back)

			bot.send_message(message.chat.id, '4-sinf darsliklari tanlandi.', reply_markup = markup)

		elif message.text == "5-sinf":
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
			item1 = types.KeyboardButton('5-sinf Tarbiya')
			item2 = types.KeyboardButton("5-sinf Matematika")
			item3 = types.KeyboardButton("5-sinf Alifbe")
			item4 = types.KeyboardButton("5-sinf Yozuv daftari")
			item5 = types.KeyboardButton("5-sinf Matematika daftari")
			item6 = types.KeyboardButton("5-sinf Ona tili")
			item7 = types.KeyboardButton("5-sinf Tabiiy fan")
			item8 = types.KeyboardButton("5-sinf Ingliz tili")
			item9 = types.KeyboardButton("5-sinf Tasviriy san'at")
			item10 = types.KeyboardButton("5-sinf Texnologiya")
			item11 = types.KeyboardButton("5-sinf Jismoniy Tarbiya")
			back = types.KeyboardButton("<-- Orqaga")
			markup.add(item1, item2,item3,item4, item5, item6, item7, item8, item9, item10,item11, back)

			bot.send_message(message.chat.id, '5-sinf darsliklari tanlandi.', reply_markup = markup)

		elif message.text == "6-sinf":
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
			item1 = types.KeyboardButton('6-sinf Tarbiya')
			item2 = types.KeyboardButton("6-sinf Matematika")
			item3 = types.KeyboardButton("6-sinf Adabiyot")
			item4 = types.KeyboardButton("6-sinf Fizika")
			item5 = types.KeyboardButton("6-sinf Geografiya")
			item6 = types.KeyboardButton("6-sinf Ona tili")
			item7 = types.KeyboardButton("6-sinf Biologiya")
			item8 = types.KeyboardButton("6-sinf Ingliz tili")
			item9 = types.KeyboardButton("6-sinf Tasviriy san'at")
			item10 = types.KeyboardButton("6-sinf Texnologiya")
			item11 = types.KeyboardButton("6-sinf Jismoniy Tarbiya")
			item12 = types.KeyboardButton("6-sinf Informatika")
			back = types.KeyboardButton("<-- Orqaga")
			markup.add(item1, item2,item3,item4, item5, item6, item7, item8, item9, item10,item11,item12, back)

			bot.send_message(message.chat.id, '6-sinf darsliklari tanlandi.', reply_markup = markup)

		elif message.text == "7-sinf":
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
			item1 = types.KeyboardButton('7-sinf Tarbiya')
			item2 = types.KeyboardButton("7-sinf Matematika")
			item3 = types.KeyboardButton("7-sinf Alifbe")
			item4 = types.KeyboardButton("7-sinf Yozuv daftari")
			item5 = types.KeyboardButton("7-sinf Matematika daftari")
			item6 = types.KeyboardButton("7-sinf Ona tili")
			item7 = types.KeyboardButton("7-sinf Tabiiy fan")
			item8 = types.KeyboardButton("7-sinf Ingliz tili")
			item9 = types.KeyboardButton("7-sinf Tasviriy san'at")
			item10 = types.KeyboardButton("7-sinf Texnologiya")
			item11 = types.KeyboardButton("7-sinf Jismoniy Tarbiya")
			back = types.KeyboardButton("<-- Orqaga")
			markup.add(item1, item2,item3,item4, item5, item6, item7, item8, item9, item10,item11, back)

			bot.send_message(message.chat.id, '7-sinf darsliklari tanlandi.', reply_markup = markup)

		elif message.text == "8-sinf":
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
			item1 = types.KeyboardButton('8-sinf Tarbiya')
			item2 = types.KeyboardButton("8-sinf Algebra")
			item3 = types.KeyboardButton("8-sinf Adabiyot")
			item4 = types.KeyboardButton("8-sinf Ona tili")
			item5 = types.KeyboardButton("8-sinf Kimyo")
			item6 = types.KeyboardButton("8-sinf Informatika")
			item7 = types.KeyboardButton("8-sinf Biologiya")
			item8 = types.KeyboardButton("8-sinf Ingliz tili")
			item9 = types.KeyboardButton("8-sinf DHA")
			item10 = types.KeyboardButton("8-sinf Texnologiya")
			item11 = types.KeyboardButton("8-sinf Jismoniy Tarbiya")
			back = types.KeyboardButton("<-- Orqaga")
			markup.add(item1, item2,item3,item4, item5, item6, item7, item8, item9, item10,item11, back)

			bot.send_message(message.chat.id, '8-sinf darsliklari tanlandi.', reply_markup = markup)

		elif message.text == "9-sinf":
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
			item1 = types.KeyboardButton('9-sinf Tarbiya')
			item2 = types.KeyboardButton("9-sinf Matematika")
			item3 = types.KeyboardButton("9-sinf Alifbe")
			item4 = types.KeyboardButton("9-sinf Yozuv daftari")
			item5 = types.KeyboardButton("9-sinf Matematika daftari")
			item6 = types.KeyboardButton("9-sinf Ona tili")
			item7 = types.KeyboardButton("9-sinf Tabiiy fan")
			item8 = types.KeyboardButton("9-sinf Ingliz tili")
			item9 = types.KeyboardButton("9-sinf Tasviriy san'at")
			item10 = types.KeyboardButton("9-sinf Texnologiya")
			item11 = types.KeyboardButton("9-sinf Jismoniy Tarbiya")
			back = types.KeyboardButton("<-- Orqaga")
			markup.add(item1, item2,item3,item4, item5, item6, item7, item8, item9, item10,item11, back)

			bot.send_message(message.chat.id, '9-sinf darsliklari tanlandi.', reply_markup = markup)

		elif message.text == "1-sinf":
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
			item1 = types.KeyboardButton('10-sinf Tarbiya')
			item2 = types.KeyboardButton("10-sinf Matematika")
			item3 = types.KeyboardButton("10-sinf Alifbe")
			item4 = types.KeyboardButton("10-sinf Yozuv daftari")
			item5 = types.KeyboardButton("10-sinf Matematika daftari")
			item6 = types.KeyboardButton("10-sinf Ona tili")
			item7 = types.KeyboardButton("10-sinf Tabiiy fan")
			item8 = types.KeyboardButton("10-sinf Ingliz tili")
			item9 = types.KeyboardButton("10-sinf Tasviriy san'at")
			item10 = types.KeyboardButton("10-sinf Texnologiya")
			item11 = types.KeyboardButton("10-sinf Jismoniy Tarbiya")
			back = types.KeyboardButton("<-- Orqaga")
			markup.add(item1, item2,item3,item4, item5, item6, item7, item8, item9, item10,item11, back)

			bot.send_message(message.chat.id, '10-sinf darsliklari tanlandi.', reply_markup = markup)



		elif message.text == "11-sinf":
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
			item1 = types.KeyboardButton('11-sinf Tarbiya')
			item2 = types.KeyboardButton("11-sinf Matematika")
			item3 = types.KeyboardButton("11-sinf Alifbe")
			item4 = types.KeyboardButton("11-sinf Yozuv daftari")
			item5 = types.KeyboardButton("11-sinf Matematika daftari")
			item6 = types.KeyboardButton("11-sinf Ona tili")
			item7 = types.KeyboardButton("11-sinf Tabiiy fan")
			item8 = types.KeyboardButton("11-sinf Ingliz tili")
			item9 = types.KeyboardButton("11-sinf Tasviriy san'at")
			item10 = types.KeyboardButton("11-sinf Texnologiya")
			item11 = types.KeyboardButton("11-sinf Jismoniy Tarbiya")
			back = types.KeyboardButton("<-- Orqaga")
			markup.add(item1, item2,item3,item4, item5, item6, item7, item8, item9, item10,item11, back)

			bot.send_message(message.chat.id, '11-sinf darsliklari tanlandi.', reply_markup = markup)

		elif message.text =="<-- Orqaga":
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
			item1 = types.KeyboardButton("Maktab darsliklari")
			item2 = types.KeyboardButton("Badiiy kitoblar")
			item3 = types.KeyboardButton("Bot dasturchisi")
	

			markup.add(item1, item2, item3)

			bot.send_message(message.chat.id, "Orqaga tanlandi!", reply_markup = markup)

		elif message.text=="Badiiy kitoblar":
			markup = types.ReplyKeyboardMarkup(reply_markup = True)
			button1 = types.KeyboardButton("Sariq devni minib")
			button2 = types.KeyboardButton("Ikki eshik orasi")
			button3 = types.KeyboardButton("Alpomish")
			button4 = types.KeyboardButton("Shaytanat")
			button5 = types.KeyboardButton("Choliqushi")
			button6 = types.KeyboardButton("Kecha va kunduz")
			button7 = types.KeyboardButton("Oq kema")
			button8 = types.KeyboardButton("Xamsa")
			button9 = types.KeyboardButton("Shum bola")
			button10 = types.KeyboardButton("Sariq devning o'limi")
			button11 = types.KeyboardButton("Quyonlar saltanati")
			button12 = types.KeyboardButton("Mungli ko'zlar")
			button13 = types.KeyboardButton("Navoiy romani")
			button14 = types.KeyboardButton("O'tkan kunlar")
			button15 = types.KeyboardButton("Mehrobdan Chayon")
			back = types.KeyboardButton("<-- Orqaga")

			markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, button13, button14, button15,back)
			bot.send_message(message.chat.id, "Badiiy kitoblar tanlandi!", reply_markup = markup)

		elif message.text == "Xamsa":
			button1 = types.KeyboardButton("1-doston")
			button2 = types.KeyboardButton("2-doston")
			button3 = types.KeyboardButton("3-doston")
			button4 = types.KeyboardButton("4-doston")
			button5 = types.KeyboardButton("5-doston")
			back = types.KeyboardButton("<-- Orqaga")

			markup.add(button1, button2, button3, button4, button5, back)

			bot.send_message(message.chat.id, "Xamsa tanlandi!", reply_markup = markup)


		elif message.text == 'Bot dasturchisi':
			button_1 = types.KeyboardButton("1-Bot dasturchisi")
			button_2 = types.KeyboardButton("2-Bot dasturchisi")
			back = types.KeyboardButton("<-- Orqaga")

			markup.add(button_1, button_2, back)
			bot.send_message(message.chat.id, "Bot dasturchisi paneli tanland!")

		elif message.text =="1-Bot dasturchisi":
			bot.send_message(message.chat.id, "Birinchi Bot dasturchisi:\nhttps://t.me/Firdavs_Programmer")
			bot.send_message(message.chat.id, "Birinchi Bot dasturchisi tanlandi!", reply_markup = markup)

		elif message.text == "2-Bot dasturchisi":
			bot.send_message(message.chat.id, "Ikkinchi Bot dasturchisi: \nhttps://t.me/Firdavs_Programmer1")
			bot.send_message(message.chat.id, "ikkinchi Bot dasturchisi tanlandi!", reply_markup = markup)

		elif message.text == "1-sinf Tarbiya":
			bot.send_document(document="", caption="")

		elif message.text == "1-sinf Matematika":
			bot.send_document(document="", caption="")
			"""
			item1 = types.KeyboardButton('1-sinf Tarbiya')
			item2 = types.KeyboardButton("1-sinf Matematika")
			item3 = types.KeyboardButton("1-sinf Alifbe")
			item4 = types.KeyboardButton("1-sinf Yozuv daftari")
			item5 = types.KeyboardButton("1-sinf Matematika daftari")
			item6 = types.KeyboardButton("1-sinf Ona tili")
			item7 = types.KeyboardButton("1-sinf Tabiiy fan")
			item8 = types.KeyboardButton("1-sinf Ingliz tili")
			item9 = types.KeyboardButton("1-sinf Tasviriy san'at")
			item10 = types.KeyboardButton("1-sinf Texnologiya")
			item11 = types.KeyboardButton("1-sinf Jismoniy Tarbiya")
			"""
		elif message.text =="1-sinf Alifbe":
			bot.send_document(document="", caption="")

		elif message.text =="1-sinf Yozuv daftari":
			bot.send_document(document="", caption="")

		elif message.text == "1-sinf Matematika daftari":
			bot.send_document(document="", caption="")

		elif message.text =="1-sinf Ona tili":
			bot.send_document(document="", caption="")

		elif message.text =='1-sinf Tabiiy fan':
			bot.send_document(document="", caption="")

		elif message.text =="1-sinf Ingliz tili"
			bot.send_document(document="", caption="")

		elif message.text =="1-sinf Tasviriy san'at"
			bot.send_document(document="", caption="")


		elif message.text =="1-sinf Texnologiya"
			bot.send_document(document="", caption="")

		elif message.text =="1-sinf Jismoniy Tarbiya"
			bot.send_document(document="", caption="")
"""
item1 = types.KeyboardButton('2-sinf Tarbiya')
			item2 = types.KeyboardButton("2-sinf Matematika")
			item3 = types.KeyboardButton("2-sinf O'qish")
			item4 = types.KeyboardButton("2-sinf Rus tili")
			item5 = types.KeyboardButton("2-sinf Matematika daftari")
			item6 = types.KeyboardButton("2-sinf Ona tili")
			item7 = types.KeyboardButton("2-sinf Tabiiy fan")
			item8 = types.KeyboardButton("2-sinf Ingliz tili")
			item9 = types.KeyboardButton("2-sinf Tasviriy san'at")
			item10 = types.KeyboardButton("2-sinf Texnologiya")
			item11 = types.KeyboardButton("2-sinf Jismoniy Tarbiya")
"""
		elif message.text =="2-sinf Matematika"
			bot.send_document(document="", caption="")

		elif message.text =="2-sinf O'qish"
			bot.send_document(document="", caption="")

		elif message.text =="2-sinf Rus tili"
			bot.send_document(document="", caption="")

		elif message.text =="2-sinf Matematika daftari"
			bot.send_document(document="", caption="")

		elif message.text =="2-sinf Ona tili"
			bot.send_document(document="", caption="")

		elif message.text =="2-sinf Tabiiy fan"
			bot.send_document(document="", caption="")

		elif message.text =="2-sinf Ingliz tili"
			bot.send_document(document="", caption="")

		elif message.text =="2-sinf Tasviriy san'at"
			bot.send_document(document="", caption="")

		elif message.text =="2-sinf Texnologiya"
			bot.send_document(document="", caption="")

		elif message.text =="2-sinf Jismoniy Tarbiya"
			bot.send_document(document="", caption="")

"""
item1 = types.KeyboardButton('3-sinf Tarbiya')
			item2 = types.KeyboardButton("3-sinf Matematika")
			item3 = types.KeyboardButton("3-sinf O'qish")
			item4 = types.KeyboardButton("3-sinf Yozuv daftari")
			item5 = types.KeyboardButton("3-sinf Matematika daftari")
			item6 = types.KeyboardButton("3-sinf Ona tili")
			item7 = types.KeyboardButton("3-sinf Tabiiy fan")
			item8 = types.KeyboardButton("3-sinf Ingliz tili")
			item9 = types.KeyboardButton("3-sinf Tasviriy san'at")
			item10 = types.KeyboardButton("3-sinf Texnologiya")
			item11 = types.KeyboardButton("3-sinf Jismoniy Tarbiya")
"""

		elif message.text =="3-sinf Tarbiya"
			bot.send_document(document="", caption="")

		elif message.text =="3-sinf Matematika"
			bot.send_document(document="", caption="")

		elif message.text =="3-sinf O'qish"
			bot.send_document(document="", caption="")

		elif message.text =="3-sinf Yozuv daftari"
			bot.send_document(document="", caption="")

		elif message.text =="3-sinf Matematika daftari"
			bot.send_document(document="", caption="")

		elif message.text =="3-sinf Ona tili"
			bot.send_document(document="", caption="")

		elif message.text =="3-sinf Tabiiy fan"
			bot.send_document(document="", caption="")

		elif message.text =="3-sinf Ingliz tili"
			bot.send_document(document="", caption="")

		elif message.text =="3-sinf Tasviriy san'at"
			bot.send_document(document="", caption="")

		elif message.text =="3-sinf Texnologiya"
			bot.send_document(document="", caption="")

		elif message.text =="3-sinf Jismoniy Tarbiya"
			bot.send_document(document="", caption="")

"""
item1 = types.KeyboardButton('4-sinf Tarbiya')
			item2 = types.KeyboardButton("4-sinf Matematika")
			item3 = types.KeyboardButton("4-sinf Alifbe")
			item4 = types.KeyboardButton("4-sinf Yozuv daftari")
			item5 = types.KeyboardButton("4-sinf Matematika daftari")
			item6 = types.KeyboardButton("4-sinf Ona tili")
			item7 = types.KeyboardButton("4-sinf Tabiiy fan")
			item8 = types.KeyboardButton("4-sinf Ingliz tili")
			item9 = types.KeyboardButton("4-sinf Tasviriy san'at")
			item10 = types.KeyboardButton("4-sinf Texnologiya")
			item11 = types.KeyboardButton("4-sinf Jismoniy Tarbiya")
"""

		elif message.text =="4-sinf Tarbiya"
			bot.send_document(document="", caption="")

		elif message.text =="4-sinf Matematika"
			bot.send_document(document="", caption="")


		elif message.text =="4-sinf Alifbe"
			bot.send_document(document="", caption="")

		elif message.text =="4-sinf Yozuv daftari"
			bot.send_document(document="", caption="")

		elif message.text =="4-sinf Matematika daftari"
			bot.send_document(document="", caption="")

		elif message.text =="4-sinf Ona tili"
			bot.send_document(document="", caption="")

		elif message.text =="4-sinf Tabiiy fan"
			bot.send_document(document="", caption="")

		elif message.text =="4-sinf Ingliz tili"
			bot.send_document(document="", caption="")

		elif message.text =="4-sinf Tasviriy san'at"
			bot.send_document(document="", caption="")

		elif message.text =="4-sinf Texnologiya"
			bot.send_document(document="", caption="")

		elif message.text =="4-sinf Jismoniy Tarbiya"
			bot.send_document(document="", caption="")
		"""
		item1 = types.KeyboardButton('5-sinf Tarbiya')
			item2 = types.KeyboardButton("5-sinf Matematika")
			item3 = types.KeyboardButton("5-sinf Alifbe")
			item4 = types.KeyboardButton("5-sinf Yozuv daftari")
			item5 = types.KeyboardButton("5-sinf Matematika daftari")
			item6 = types.KeyboardButton("5-sinf Ona tili")
			item7 = types.KeyboardButton("5-sinf Tabiiy fan")
			item8 = types.KeyboardButton("5-sinf Ingliz tili")
			item9 = types.KeyboardButton("5-sinf Tasviriy san'at")
			item10 = types.KeyboardButton("5-sinf Texnologiya")
			item11 = types.KeyboardButton("5-sinf Jismoniy Tarbiya")
		"""

		elif message.text =="5-sinf Tarbiya"
			bot.send_document(document="", caption="")

		elif message.text =="5-sinf Matematika"
			bot.send_document(document="", caption="")

		elif message.text =="5-sinf Alifbe"
			bot.send_document(document="", caption="")

		elif message.text =="5-sinf Yozuv daftari"
			bot.send_document(document="", caption="")

		elif message.text =="5-sinf Matematika daftari"
			bot.send_document(document="", caption="")


		elif message.text =="5-sinf Ona til"
			bot.send_document(document="", caption="")


		elif message.text =="5-sinf Tabiiy fan"
			bot.send_document(document="", caption="")

		elif message.text =="5-sinf Ingliz tili"
			bot.send_document(document="", caption="")


		elif message.text =="5-sinf Tasviriy san'at"
			bot.send_document(document="", caption="")

		elif message.text =="5-sinf Texnologiya"
			bot.send_document(document="", caption="")

		elif message.text =="5-sinf Jismoniy Tarbiya"
			bot.send_document(document="", caption="")

		"""
		
		"""

		elif message.text ==""
			bot.send_document(document="", caption="")

		elif message.text ==""
			bot.send_document(document="", caption="")

		elif message.text ==""
			bot.send_document(document="", caption="")

		elif message.text ==""
			bot.send_document(document="", caption="")


		elif message.text ==""
			bot.send_document(document="", caption="")

		elif message.text ==""
			bot.send_document(document="", caption="")

		elif message.text ==""
			bot.send_document(document="", caption="")

		elif message.text ==""
			bot.send_document(document="", caption="")

		elif message.text ==""
			bot.send_document(document="", caption="")

		elif message.text ==""
			bot.send_document(document="", caption="")

		elif message.text ==""
			bot.send_document(document="", caption="")

		elif message.text ==""
			bot.send_document(document="", caption="")

		elif message.text ==""
			bot.send_document(document="", caption="")

		elif message.text ==""
			bot.send_document(document="", caption="")

		elif message.text ==""
			bot.send_document(document="", caption="")

		elif message.text ==""
			bot.send_document(document="", caption="")

		elif message.text ==""
			bot.send_document(document="", caption="")

		elif message.text ==""
			bot.send_document(document="", caption="")

		elif message.text ==""
			bot.send_document(document="", caption="")

		elif message.text ==""
			bot.send_document(document="", caption="")

		elif message.text ==""
			bot.send_document(document="", caption="")

		elif message.text ==""
			bot.send_document(document="", caption="")

		elif message.text ==""
			bot.send_document(document="", caption="")

		elif message.text ==""
			bot.send_document(document="", caption="")

		elif message.text ==""
			bot.send_document(document="", caption="")

		elif message.text ==""
			bot.send_document(document="", caption="")

		elif message.text ==""
			bot.send_document(document="", caption="")

		elif message.text ==""
			bot.send_document(document="", caption="")

		elif message.text ==""
			bot.send_document(document="", caption="")

			

@bot.messge_handler(commands = ['admin'])
def admin(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
	item1 = types.KeyboardButton("Python dasturlash tili")
	item2 = types.KeyboardButton("Firdavsbek Yorkulov")
	item3 = types.KeyboardButton("Admin")
	item4 = types.KeyboardButton("KeyboardButton")
	item5 = types.KeyboardButton("InlineKeyboardButton")
	back = types.KeyboardButton("<-- Orqaga")

	markup.add(item1, item2, item3, item4, item5, back)

	bot.send_message(message.chat.id, "Salom, {0.first_name}! Firdavsbek Yorkulovning shaxsiy paneliga xush kelibsiz!!!".format(message.from_user), reply_markup = markup)
	



bot.polling(none_stop = True)