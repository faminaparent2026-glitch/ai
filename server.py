from flask import Flask

app = Flask(__name__)

# هذا هو "الملف الواحد" الذي يحتوي على الواجهة (HTML) والسيرفر (Python)
@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>سيرفر B.H الصفرِي</title>
    </head>
    <body style="background: black; color: green; text-align: center; padding-top: 50px;">
        <h1>نظام B.H يعمل بنجاح</h1>
        <p>لا استهلاك، لا ملفات إضافية، سرعة مطلقة.</p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run()

