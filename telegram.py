import telebot
import openai

telegram_key = '1133484080:AAF9JyWhco4eZJvFPSg1GrWT1ilpzjpF0xM'
gpt_key ='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'


bot = telebot.TeleBot(telegram_key)

openai.api_key = gpt_key

@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id,'Привет я твой Chat GPT')


@bot.message_handler(content_types=['text'])
def main(message):
    response = openai.Completion.create(
       
        engine='gpt-3.5-turbo-0613',
        prompt=message.text,
        max_tokens=10,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=15
    )
    if response and response.choices:
        reply =  response.choices[0].text.strip()
    else:
        reply = 'oh..'

    bot.send_message(message.chat.id, reply)


bot.polling(none_stop=True)