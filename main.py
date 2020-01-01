import config
import telebot
import requests
from telebot import types
from bs4 import BeautifulSoup as BS
r = requests.get('https://sinoptik.ua')
html = BS(r.content, 'html.parser')
bot = telebot.TeleBot(telebot.token)

for city in html.select('#header'):
    cur_city = city.select('.cityName .isMain')[0].text
    currentRegion = city.select('.currentRegion')[0].text
    print (cur_city + '- ' + currentRegion)

for el in html.select('#content'):
    time = el.select('.today-time')[0].text
    t_min = el.select('.temperature .min')[0].text
    t_max = el.select('.temperature .max')[0].text
    text = el.select('.wDescription .description')[0].text
    text2 = el.select('.oDescription .description')[0].text
    voshod_zakat = el.select('.lSide .infoDaylight')[0].text
    
    print (time + '\n\n' + cur_city + '- ' + currentRegion + '\n\n' + t_min + ', ' + 
    t_max + ', ' + '\n\n' + voshod_zakat + '\n\n' + text + '\n\n' + text2)

@bot.message_handler(commands=['start', 'help'])
def main(message):
    bot.send_message(message.chat.id, 
    time + '\n\n' + cur_city + '- ' + currentRegion + '\n\n' + t_min + ', ' + 
    t_max + ', ' + '\n\n' + voshod_zakat + '\n\n' + text + '\n\n' + text2)
    
if __name__ == '__name__':
    bot.polling(none_stop=True)
#
#
bot.polling()
