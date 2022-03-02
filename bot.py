import telebot

token = ""

bot = telebot.TeleBot(token)

db = open("test.txt", "r")
joined_users = set()
for line in db:
    joined_users.add(line.strip())
db.close()


@bot.message_handler(commands=['start'])
def welcome(message):
    global db
    if not str(message.chat.id) in joined_users:
        db = open("test.txt", "a")
        db.write(str(message.chat.id) + "\n")
        joined_users.add(message.chat.id)
        bot.send_message(message.chat.id, "example 1")


# get the text after the "send_secret_message" command and send it
# can be deleted
@bot.message_handler(commands=['send_secret_message'])
def secret_msg(message):
    for user in joined_users:
        bot.send_message(user, message.text[message.text.find(' '):])


# send text "example 2" in real time
@bot.message_handler(commands=['send'])
def msg(message):
    for user in joined_users:
        bot.send_message(user, "example 2")
        # img = open('11.jpg', 'rb')
        # bot.send_photo(message.chat.id, img)


bot.polling(none_stop=True)
