from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'It is working!'

def main():
    app.run(host='0.0.0.0', port=801)

if __name__=='__main__':
    main()
