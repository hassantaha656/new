import telebot

# استبدل TOKEN_HERE بـ Token البوت الخاص بك
bot = telebot.TeleBot('7202922124:AAFxTuU0s6LaAtfV6ZSiuDwYyJ0LqwTSURw')

@bot.message_handler(content_types=['document'])
def handle_doc(message):
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)   


    with open("received_file.pdf", 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, "تم حفظ الملف بنجاح")

bot.polling()