import os
import subprocess
import sys
import logging
from flask import Flask, render_template_string, request

# --- المرحلة 1: تثبيت الأدوات ---
def install_requirements():
    required = ['flask']
    for package in required:
        try:
            __import__(package)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install_requirements()

# --- المرحلة 5: إعداد نظام السجلات ---
logging.basicConfig(filename='ai_system.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# --- المرحلة 2: واجهة المستخدم ---
app = Flask(__name__)

HTML_UI = """
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <style>
        body { background-color: #121212; color: #fff; font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        #app-box { width: 400px; height: 500px; border: 2px solid #333; border-radius: 15px; display: flex; flex-direction: column; background: #1e1e1e; overflow: hidden; }
        #chat-area { flex: 1; padding: 20px; overflow-y: auto; border-bottom: 1px solid #333; }
        #input-area { padding: 10px; display: flex; }
        input { flex: 1; background: #333; border: none; color: white; padding: 10px; border-radius: 5px; }
        button { background: #4caf50; border: none; color: white; padding: 10px; margin-left: 5px; border-radius: 5px; cursor: pointer; }
    </style>
</head>
<body>
    <div id="app-box">
        <div id="chat-area"><p>مرحباً، أنا نظامك الذكي B.H. كيف يمكنني مساعدتك؟</p></div>
        <div id="input-area">
            <input type="text" id="user-input" placeholder="اكتب أمرك هنا...">
            <button onclick="sendMessage()">إرسال</button>
        </div>
    </div>
    <script>
        function sendMessage() {
            let input = document.getElementById('user-input');
            let chat = document.getElementById('chat-area');
            chat.innerHTML += '<p style="text-align:right;">أنت: ' + input.value + '</p>';
            fetch('/process?cmd=' + input.value)
                .then(res => res.text())
                .then(data => {
                    chat.innerHTML += '<p>الوكيل: ' + data + '</p>';
                    input.value = '';
                });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_UI)

# --- المرحلة 3, 4, 5: معالجة الأوامر والسجلات ---
@app.route('/process')
def process():
    cmd = request.args.get('cmd', '').lower()
    logging.info(f"User command: {cmd}")
    
    if cmd == "status":
        return "النظام يعمل بكفاءة. أنا في المرحلة 5."
    elif cmd == "help":
        return "الأوامر المتاحة: status, help, list, logs"
    elif cmd == "list":
        return "الملفات: " + ", ".join(os.listdir('.'))
    elif cmd == "logs":
        if os.path.exists('ai_system.log'):
            with open('ai_system.log', 'r') as f:
                return "<br>".join(f.read().splitlines()[-5:])
        return "لا توجد سجلات بعد."
    else:
        return f"الوكيل: لم أفهم '{cmd}'."

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

