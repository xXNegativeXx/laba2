from flask import Flask

app = Flask(_name_)

@app.route('/')
def home():
    return 'It is working!'

def main():
    app.run(host='0.0.0.0', port=81)

if __name__=='__main__':
    main()
