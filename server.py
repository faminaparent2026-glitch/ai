from flask import Flask, render_template_string, request, jsonify
from datetime import datetime

app = Flask(__name__)

# --- الطبقة المنطقية (دمجنا العقل هنا ليعمل الملف بشكل مستقل) ---
class BHAgent:
    def process_query(self, query: str) -> dict:
        q = query.lower()
        if "مرحبا" in q or "أهلين" in q:
            return {"response": {"message": "مرحباً، أنا نظام B.H، كيف يمكنني مساعدتك اليوم؟"}}
        elif "time" in q or "وقت" in q:
            return {"response": {"message": f"الوقت الحالي هو: {datetime.now().strftime('%H:%M:%S')}"}}
        else:
            return {"response": {"message": "لم أفهم الأمر، جرب كلمة 'وقت' أو 'مرحبا'."}}

agent = BHAgent()

# --- واجهة المستخدم ---
CHAT_UI = """
<!DOCTYPE html>
<html lang="ar">
<body style="background:#121212; color:#fff; font-family:sans-serif; text-align:center;">
    <h1>B.H Agent Interface</h1>
    <div id="chat-box" style="border:1px solid #333; width:80%; margin:auto; height:300px; overflow-y:scroll; padding:10px;"></div>
    <br>
    <input type="text" id="cmd" placeholder="اكتب أمرك هنا..." style="width:60%; padding:10px;">
    <button onclick="sendMsg()" style="padding:10px;">إرسال</button>
    <script>
        function sendMsg() {
            let cmd = document.getElementById('cmd').value;
            fetch('/process?cmd=' + cmd)
            .then(r => r.json())
            .then(data => {
                let box = document.getElementById('chat-box');
                box.innerHTML += '<p>أنت: ' + cmd + '</p>';
                box.innerHTML += '<p style="color:cyan;">B.H: ' + data.response.message + '</p>';
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
    app.run(host='0.0.0.0', port=10000)

