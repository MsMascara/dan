import telebot
import openai
import os

# Configuración del bot de Telegram
TOKEN = "6138915284:AAEyFObcdf6k1QSpAll24dzdS7MTNn2JGKc"
bot = telebot.TeleBot(TOKEN)

# Configuración de OpenAI
openai.api_key = "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"

# Manejador de comando "/start"
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, '¡Hola! ¿En qué puedo ayudarte?')

# Manejador de mensaje de texto
@bot.message_handler(func=lambda message: True)
def generate_text(message):
    # Obtenemos el texto del mensaje enviado por el usuario
    user_text = message.text

    # Utilizamos OpenAI para generar una respuesta
    prompt = f"{user_text}"
    response = openai.Completion.create(
        engine="davinci", prompt=prompt, temperature=1, max_tokens=2048
    )
    bot.reply_to(message, response.choices[0].text)

# Ejecutar el bot
bot.polling()
'''
-------------------------------------------------------------------
-------------------------------------------------------------------

import telebot
import openai

openai.api_key = "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"
bot = telebot.TeleBot("6138915284:AAEyFObcdf6k1QSpAll24dzdS7MTNn2JGKc")

comversation = ""
question = ""
i=1
while(i!= 0):
	question = input("Usuario: ")
	comversation += "\nUsuario: " + question + "\nAI:"
	response = openai.Completion.create(
		engine="davinci",
		prompt=comversation,
		temperatur=0.9,
		max_tokens=150,
		top_p=1,
		frecuency_penalty=0,
		precence_penalty=0.6,
		stop=["\n", "Usuario:","AI:"]
	)
	anwer = response.chices[0].text.sprip()
	comversation += anwer
	
@bot.message_handler(question=lambda message:True)

def enviar(message):
	
	bot.reply_to(message, anwer)


bot.polling()

'''
'''
------------------------------------------------------------------
------------------------------------------------------------------
@bot.message_handler(commands=["hola", "start"])
@bot.message_handler(func=lambda message:True)

def mensaje(message):
	bot.reply_to(message, message.text)
	
'''
