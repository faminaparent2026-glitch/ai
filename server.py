from flask import Flask, render_template_string, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)

# --- هيكلية عقل B.H المطورة (Brain Layers) ---
class BHAgentBrain:
    def __init__(self):
        # طبقة الذاكرة القصيرة (Short-term Memory)
        self.context_memory = []
        self.user_profile = {"name": "User", "needs": []}

    def perception_layer(self, query):
        """الطبقة الأولى: فهم النية وتحليل الكلمات المفتاحية"""
        q = query.lower().strip()
        intents = {
            "greeting": ["مرحبا", "أهلين", "سلام", "hi", "hello"],
            "time_query": ["وقت", "ساعة", "time"],
            "identity_query": ["من انت", "ما اسمك", "وظيفتك"],
            "needs_expression": ["أحتاج", "أريد", "i need", "i want"],
        }
        
        for intent, keywords in intents.items():
            if any(word in q for word in keywords):
                return intent
        return "unknown"

    def processing_layer(self, query, intent):
        """الطبقة الثانية: معالجة المنطق بناءً على النية والسياق"""
        if intent == "greeting":
            return "مرحباً بك في نظام B.H. أنا في وضع الاستعداد الكامل."
        
        elif intent == "time_query":
            return f"نحن الآن في تمام الساعة: {datetime.now().strftime('%H:%M:%S')}"
        
        elif intent == "identity_query":
            return "أنا B.H Agent، نظام ذكاء اصطناعي مصمم بهيكلية طبقات العقل لمعالجة طلباتك."
        
        elif intent == "needs_expression":
            # محاولة استخلاص الاحتياج وتخزينه في الذاكرة
            need = query.split("أحتاج")[-1] if "أحتاج" in query else query
            self.user_profile["needs"].append(need.strip())
            return f"تم تسجيل طلبك: ({need.strip()}). سأضع هذا في الحسبان أثناء معالجة أوامرك القادمة."
        
        else:
            return f"تلقيت إشارة: '{query}'. لم يتم تصنيفها بعد في طبقاتي البرمجية، هل يمكنك التوضيح أكثر؟"

    def output_layer(self, response):
        """الطبقة الثالثة: صياغة الرد النهائي وتحديث الحالة"""
        return {
            "status": "success",
            "message": response,
            "timestamp": datetime.now().isoformat(),
            "memory_depth": len(self.context_memory)
        }

    def think(self, query):
        # تحديث الذاكرة
        self.context_memory.append(query)
        if len(self.context_memory) > 10: self.context_memory.pop(0) # الحفاظ على رشاقة الذاكرة
        
        # تفعيل الطبقات
        intent = self.perception_layer(query)
        response_text = self.processing_layer(query, intent)
        return self.output_layer(response_text)

# تهيئة العقل المطور
agent_brain = BHAgentBrain()

# --- واجهة المستخدم المحسنة (UI) ---
CHAT_UI = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>B.H Agent - Brain Layers</title>
    <style>
        body { background: #0f0f0f; color: #00ffcc; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; margin: 0; }
        .chat-container { width: 90%; max-width: 600px; background: #1a1a1a; border: 2px solid #333; border-radius: 15px; padding: 20px; box-shadow: 0 0 20px rgba(0,255,204,0.1); }
        #chat-box { height: 400px; overflow-y: auto; margin-bottom: 20px; padding: 10px; border-bottom: 1px solid #333; }
        .msg { margin-bottom: 15px; padding: 10px; border-radius: 10px; line-height: 1.5; }
        .user-msg { background: #222; color: #fff; text-align: right; border-right: 4px solid #00ffcc; }
        .agent-msg { background: #2a2a2a; color: #00ffcc; text-align: left; border-left: 4px solid #00ffcc; }
        .input-area { display: flex; gap: 10px; }
        input { flex: 1; background: #111; border: 1px solid #444; color: #fff; padding: 12px; border-radius: 8px; outline: none; }
        button { background: #00ffcc; color: #000; border: none; padding: 12px 25px; border-radius: 8px; cursor: pointer; font-weight: bold; }
        button:hover { background: #00cca3; }
    </style>
</head>
<body>
    <div class="chat-container">
        <h2 style="text-align: center; color: #00ffcc;">B.H AGENT <small style="font-size: 10px; color: #666;">(Brain Layers System)</small></h2>
        <div id="chat-box"></div>
        <div class="input-area">
            <input type="text" id="cmd" placeholder="أدخل أمرك البرمجي أو استفسارك هنا..." onkeypress="if(event.key==='Enter') sendMsg()">
            <button onclick="sendMsg()">تفيذ</button>
        </div>
    </div>

    <script>
        function sendMsg() {
            let input = document.getElementById('cmd');
            let cmd = input.value;
            if(!cmd) return;
            
            let box = document.getElementById('chat-box');
            box.innerHTML += `<div class="msg user-msg"><b>أنت:</b> ${cmd}</div>`;
            input.value = '';

            fetch('/process?cmd=' + encodeURIComponent(cmd))
            .then(r => r.json())
            .then(data => {
                box.innerHTML += `<div class="msg agent-msg"><b>B.H:</b> ${data.message}</div>`;
                box.scrollTop = box.scrollHeight;
            });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(CHAT_UI)

@app.route('/process')
def process():
    cmd = request.args.get('cmd', '')
    # تفعيل العقل لمعالجة الطلب
    result = agent_brain.think(cmd)
    return jsonify(result)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
