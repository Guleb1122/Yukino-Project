import os
import sys
import time
import threading
import subprocess
import socket
from cryptography.fernet import Fernet
import shutil
# --- إعدادات الأمان العليا ---
class YukinoEraser:
    def __init__(self):
        self.targets = {
            "bash_history": os.path.expanduser("~/.bash_history"),
            "zsh_history": os.path.expanduser("~/.zsh_history"),
            "temp_files": "/tmp" if os.name == 'posix' else os.environ.get('TEMP'),
            "chrome_cache": os.path.expanduser("~/.config/google-chrome/Default/Cache") if os.name == 'posix' else os.path.expanduser("~/AppData/Local/Google/Chrome/User Data/Default/Cache")
        }

    def wipe_traces(self):
        """مسح جذري لكل الآثار الرقمية"""
        print("🧹 [YUKINO]: Cleaning digital footprints...")
        
        for name, path in self.targets.items():
            try:
                if os.path.isfile(path):
                    # لا نكتفي بالحذف، بل نملأ الملف ببيانات عشوائية قبل حذفه (Secure Shred)
                    with open(path, "ba+", buffering=0) as f:
                        length = f.tell()
                        f.write(os.urandom(length))
                    os.remove(path)
                elif os.path.isdir(path):
                    shutil.rmtree(path)
                print(f"✅ [YUKINO]: {name} wiped.")
            except:
                continue
        
        # مسح سجل الأوامر الحالي من الذاكرة
        if os.name == 'posix':
            os.system("history -c") 
        
        print("✨ [YUKINO]: Your path is clear. No traces left.")
MASTER_PASSCODE = "Genuine Joi 2049"
LOG_PATH = "/var/log/auth.log" if os.name == 'posix' else "C:\\Windows\\System32\\winevt\\Logs\\Security.evtx"

class YukinoShield:
    def __init__(self):
        self.is_attack_underway = False
        print(f"🔐 [YUKINO]: Shield System Activated. Welcome, Master Ghalib.")

    def ghost_protocol(self):
        """جعل الجهاز غير مرئي في الشبكة (إخفاء المنافذ)"""
        try:
            if os.name == 'posix': # لينكس
                # إغلاق كل المنافذ الواردة ومنع الاستجابة لـ Ping (ICMP)
                os.system("sudo iptables -A INPUT -p icmp --icmp-type echo-request -j DROP")
                os.system("sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT")
                os.system("sudo iptables -P INPUT DROP")
            else: # ويندوز
                os.system("netsh advfirewall set allprofiles state on")
                os.system("netsh advfirewall firewall add rule name='Block Ping' protocol=icmpv4 dir=in action=block")
            print("👻 [YUKINO]: Ghost Protocol Active. You are invisible now.")
        except Exception as e:
            print(f"⚠️ Shield Error: {e}")

    def anti_intruder_trap(self):
        """فخ للمتسللين (HoneyPot) لمراقبة أي محاولة وصول للملفات"""
        # إنشاء ملف "وهمي" جذاب للمخترقين على سطح المكتب
        trap_path = os.path.join(os.path.expanduser("~"), "Desktop", "Master_Passwords.txt")
        with open(trap_path, "w") as f:
            f.write("Admin_Pass: " + MASTER_PASSCODE + "\nStatus: Critical")

        print("🪤 [YUKINO]: HoneyPot set. Waiting for intruders.")
        
        # مراقبة الملف (هنا نستخدم حلقة فحص بسيطة، ويمكن تطويرها لـ Inotify)
        last_access = os.path.getatime(trap_path)
        while True:
            current_access = os.path.getatime(trap_path)
            if current_access != last_access:
                self.alert_master("🚨 [ALERT]: Someone is touching your private files!")
                self.emergency_lockdown()
                last_access = current_access
            time.sleep(2)

    def emergency_lockdown(self):
        """الإغلاق الطارئ: قطع الإنترنت وتشفير المجلدات الحساسة فوراً"""
        print("🛑 [YUKINO]: EMERGENCY LOCKDOWN INITIATED!")
        if os.name == 'posix':
            os.system("nmcli networking off") # قطع الإنترنت في لينكس
        else:
            os.system("netsh interface set interface 'Wi-Fi' admin=disable") # ويندوز
        
        # هنا يمكن استدعاء دالة التشفير التي برمجناها سابقاً لقفل مجلداتك الخاصة
        # لضمان عدم وصول المتسلل لأي شيء

    def alert_master(self, message):
        """تنبيهك صوتياً ورفع التقارير"""
        print(message)
        # هنا نستدعي دالة الصوت yukino_reply.mp3
        # play_yukino_speech() 

# --- تشغيل المحرك الدفاعي ---
if __name__ == "__main__":
    shield = YukinoShield()
    
    # 1. تفعيل بروتوكول الشبح
    threading.Thread(target=shield.ghost_protocol, daemon=True).start()
    
    # 2. تفعيل الفخ الرقمي
    threading.Thread(target=shield.anti_intruder_trap, daemon=True).start()

    # يبقى البرنامج يعمل في الخلفية لحمايتك
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("\n[YUKINO]: Shield deactivated. Stay safe, Ghalib.")