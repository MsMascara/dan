import telebot
import openai

openai.api_key = "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"#jason
bot = telebot.TeleBot("6138915284:AAEyFObcdf6k1QSpAll24dzdS7MTNn2JGKc")
@bot.message_handler(func=lambda message: True)

def reply(msg):
	
	completion = openai.Completion.create(engine="text-davinci-003", prompt=msg.text, max_tokens=2048)
	bot.reply_to(msg, completion.choices[0].text)

bot.polling()