from flask import Flask
from configs import config_all

def run_server():
    app = Flask(__name__)
    
    config_all(app)

    app.run(debug=True)

if __name__ == '__main__':
    run_server()