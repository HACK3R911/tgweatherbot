#Import data weater -->  https://github.com/csparpa/pyowm
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

#Import tgbot ---------> https://github.com/eternnoir/pyTelegramBotAPI
import telebot

#DATA OF WEATHER
owm = OWM('d8e5d826179ac55f338c655baf10f41a')
mgr = owm.weather_manager

#BOT
bot = telebot.TeleBot("5028475011:AAGcBd-PkgstgFRiggSwKD2f1s80FfBoNi8")

@bot.message_handler(content_types=['text'])
def send_echo(message):

	observation = mgr.weather_at_place(message.text)
    w = observation.weather

    temp = w.temperature('celsius')["temp"]

    #REPLY FROM BOT
    answer = "Now in the city of " + message.text  + str(w.detailed_status) + "\n"
    answer += "Tempeture now in city " + str(temp) + "\n\n"

        if temp < 10:
        answer += "Now is very cold, wear warm jacket!"
    elif temp < 20:
        answer += "Now is cold, dress warmly."
    else:
        answer += "Outside is heat, you can wear anything."

        bot.send_message(message.chat.id, answer)

bot.infinity_polling()
