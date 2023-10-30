from flask import request, jsonify
from models import Conta, Usuario, db

def criar_contas(app):
    #READ
    @app.route('/contas', methods=['GET'])
    def listar():
        contas = Conta.query.all()
        lista = [{'id':conta.id,'descricao':conta.descricao,
                  'valor':conta.valor, 'tipo':conta.tipo}
                 for conta in contas]
        return lista
    #READ
    @app.route('/contas/<id>',methods=['GET'])
    def buscar_por_id(id):
        conta = Conta.query.get(id)
        return {'descricao':conta.descricao,'valor':conta.valor, 'tipo':conta.tipo}
    #CREATE
    @app.route('/contas', methods=['POST'])
    def adicionar():
        data = request.get_json()
        conta = Conta(descricao=data['descricao'],valor=data['valor'], tipo=data['tipo'])
        db.session.add(conta)
        db.session.commit()
        return {'id':conta.id, 'descricao':conta.descricao}
    #UPDATE
    @app.route('/contas/update/<id>', methods=['PUT'])
    def editar(id):
        data = request.get_json()
        conta = Conta.query.get(id)
        conta.descricao = data['descricao']
        conta.valor = data['valor']
        conta.tipo = data['tipo']
        db.session.commit()
        return {'message': 'Registro editado com sucesso.'}
    # DELETE
    @app.route('/contas/delete/<id>', methods=['DELETE'])
    def excluir(id):
        conta = Conta.query.get(id)
        db.session.delete(conta)
        db.session.commit()
        return {'message': 'Registro excluido com sucesso.'}

