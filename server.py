import os
import subprocess
import sys
from flask import Flask, request, render_template_string

# --- المرحلة 1: تثبيت الأدوات ---
def install_requirements():
    required = ['flask']
    for package in required:
        try:
            __import__(package)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install_requirements()

# --- المرحلة 2: واجهة المحادثة (الواجهة المربعة) ---
app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>B.H AI Agent</title>
    <style>
        body { background-color: #121212; color: white; font-family: sans-serif; display: flex; justify-content: center; padding: 20px; }
        #chatbox { width: 500px; border: 1px solid #333; padding: 20px; border-radius: 10px; background: #1e1e1e; }
        input { width: 80%; padding: 10px; }
        button { padding: 10px; }
    </style>
</head>
<body>
    <div id="chatbox">
        <h3>B.H AI Agent (المرحلة 1-2)</h3>
        <div id="log"></div>
        <input type="text" id="userInput" placeholder="اكتب أمراً هنا...">
        <button onclick="send()">إرسال</button>
    </div>
    <script>
        function send() {
            let text = document.getElementById('userInput').value;
            fetch('/chat?q=' + text)
                .then(res => res.text())
                .then(data => {
                    document.getElementById('log').innerHTML += '<p>أنت: ' + text + '</p><p>الوكيل: ' + data + '</p>';
                });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/chat')
def chat():
    user_query = request.args.get('q', '')
    # هنا سيتم لاحقاً ربط نظام الذكاء الاصطناعي (المرحلة 11-15)
    return f"تم استقبال طلبك: {user_query}. أنا قيد التطوير للمرحلة القادمة."

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

