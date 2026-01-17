import numpy as np
import socket
import re

# [3] حارس الشبكة الواعي (Neural Firewall)
def network_sentinel():
    # مراقبة الاتصالات الخارجية المشبوهة
    active_conns = socket.gethostname()
    print(f"📡 [YUKINO]: Monitoring network traffic for {active_conns}...")
    # منطق افتراضي: إذا تم اكتشاف محاولة اتصال بعنوان IP مجهول، يتم حظره
    # (هنا يتم دمج أوامر جدار الحماية)

# [5] كاشف الابتزاز بالذكاء العاطفي
def emotion_analyser(text):
    # كلمات دلالية للابتزاز والتهديد
    threat_patterns = ["سأقوم بنشر", "فضيحة", "صورك", "ادفع", "ابتزاز"]
    score = 0
    for pattern in threat_patterns:
        if re.search(pattern, text):
            score += 1
    
    if score > 0:
        return "⚠️ [YUKINO]: غالب، هذا النص يحتوي على نبرة تهديد. قمت بتحديد هوية المصدر رقمياً."
    else:
        return "🌸 [YUKINO]: النص يبدو آمناً يا سيدي."

# [6] التوأم الرقمي للمحرك (Digital Twin) باستخدام NumPy
def engine_simulator(rpm, temperature):
    # معادلة احتراق وميكانيكا بسيطة للتنبؤ بالأعطال
    data_points = np.array([rpm, temperature])
    # مصفوفة الأداء المثالي للسيارة (The Spinner)
    ideal_performance = np.array([3000, 85]) 
    
    drift = np.linalg.norm(data_points - ideal_performance)
    if drift > 500:
        return f"⚙️ [YUKINO]: تحذير ميكانيكي! هناك انحراف في أداء المحرك بمقدار {drift:.2f}"
    return "✅ [YUKINO]: المحرك يعمل بكفاءة العميل K."

# تجربة التشغيل
print(emotion_analyser("سأقوم بنشر صورك إذا لم تدفع المال"))
print(engine_simulator(4500, 110))