from flask import Flask
from models import db
from routes import criar_contas

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:usbw@localhost:3306/financeiro'

db.init_app(app)

# Comando que criará as tabelas no banco de dados
# Se Deus quiser vai dar certo, pra mim deu pelo menos
with app.app_context():
    db.create_all()

# Passo as rotas para o meu app
criar_contas(app)

if __name__ == "__main__":
    app.run()
