from flask import Flask, render_template_string, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)

# --- العقل (B.H Agent) - الملف بالكامل ---
class BHAgent:
    def __init__(self):
        self.memory = []

    def process_query(self, query: str) -> dict:
        q = query.lower()
        # هنا المنطق الخاص بك - تم إبقاؤه كما هو
        if "مرحبا" in q or "أهلين" in q:
            response = "مرحباً! أنا نظام B.H، كيف يمكنني مساعدتك؟"
        elif "time" in q or "وقت" in q:
            response = f"الوقت الحالي هو: {datetime.now().strftime('%H:%M:%S')}"
        else:
            response = f"فهمت طلبك: '{query}'. أنا ما زلت أتعلم، جرب سؤالاً آخر."
        
        self.memory.append({"query": query, "response": response})
        return {"message": response}

# تهيئة العقل
agent = BHAgent()

# --- واجهة المستخدم (UI) ---
CHAT_UI = """
<!DOCTYPE html>
<html lang="ar">
<body style="background:#121212; color:#fff; font-family:sans-serif; text-align:center;">
    <h1>B.H Agent System</h1>
    <div id="chat-box" style="border:1px solid #333; width:80%; margin:auto; height:300px; overflow-y:scroll; padding:10px; text-align:left;"></div>
    <br>
    <input type="text" id="cmd" placeholder="اكتب أمرك هنا..." style="width:60%; padding:10px; border-radius:5px;">
    <button onclick="sendMsg()" style="padding:10px; cursor:pointer;">إرسال</button>
    <script>
        function sendMsg() {
            let cmd = document.getElementById('cmd').value;
            fetch('/process?cmd=' + cmd)
            .then(r => r.json())
            .then(data => {
                let box = document.getElementById('chat-box');
                box.innerHTML += '<p><b>أنت:</b> ' + cmd + '</p>';
                box.innerHTML += '<p style="color:cyan;"><b>B.H:</b> ' + data.message + '</p>';
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
    return jsonify(agent.process_query(cmd))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

