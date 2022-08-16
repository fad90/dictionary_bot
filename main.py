import telebot
import requests

bot = telebot.TeleBot('5336455020:AAGQWCpyNcvGbPLNlM_ks5bAtGfVMPmKzCc')

urlAuthenticate = 'https://developers.lingvolive.com/api/v1.1/authenticate'
apiKey = 'OGVmNzk4NjYtMjBhNC00OTkxLWIyMTUtYjBlZThhYWQzNzNkOjViYTBjN2MxNmVkZjQ1OTZhN2EzMjEwZGE0ZmQ5OWRm'
headersAuthenticate = {"Authorization": f"Basic {apiKey}"}
bearerToken = requests.post(urlAuthenticate, headers=headersAuthenticate).text


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Привет, гость!. Напиши мне что-нибудь')


@bot.message_handler()
def handle_text(message):
    if message.text:
        try:
            wordForTranslate = message.text
            srcLang = '1033'
            dstLang = '1049'
            url = f"https://developers.lingvolive.com/api/v1/Minicard?text={wordForTranslate}&srcLang={srcLang}&dstLang={dstLang}"
            headers = {"Authorization": f"Bearer {bearerToken}"}
            response = requests.get(url, headers=headers)
            translatedWord = response.json()["Translation"]["Translation"]
            bot.send_message(message.chat.id, 'Перевод: ' + translatedWord)
        except Exception as ex:
            bot.send_message(message.chat.id, "I can't find the translation")


bot.polling(none_stop=True)
