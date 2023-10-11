from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysql://root:usbw@localhost:3306/financeiro'

if __name__ == "__main__":
    app.run()
