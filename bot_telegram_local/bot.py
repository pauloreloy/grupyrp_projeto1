import os
import json
import telebot
import requests
from detectFace import detectFace

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['analisar', 'Analisar'])
def analisar(message):
    ans = "Por gentileza, envie a foto que deseja analisar..."
    sent_msg = bot.send_message(message.chat.id, ans, parse_mode="Markdown")
    bot.register_next_step_handler(message, analisarFoto)

@bot.message_handler(content_types=['photo'])
def analisarFoto(message):
    bot.send_message(message.chat.id, "Aguarde. Foto em análise...")
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)
    try:
        result = detectFace(downloaded_file)
        result = json.loads(result)
        totalfaces = result['result']['totalfaces']
        totalsmiling = result['result']['smiling']
        msg = f"Total de Pessoas: {totalfaces}\nTotal Sorrindo: {totalsmiling}"
        bot.send_message(message.chat.id, msg, parse_mode="Markdown")
    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, "Erro ao analisar a foto.", parse_mode="Markdown")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.send_message(message.chat.id, "Função não reconhecida.")


bot.infinity_polling()
