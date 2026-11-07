from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Delifrost App is running!"

if __name__ == '__main__':
    app'0.0.0.0', port=5000)"
            
