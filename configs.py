from models.expense import ExpenseModel
from routes.render_pages.home import bp_home
from routes.expense import bp_expenses

def config_all(app):
    config_bp(app)
    create_tables()

def config_bp(app):
    app.register_blueprint(bp_home)
    app.register_blueprint(bp_expenses)

def create_tables():
    try:
        ExpenseModel.create_table()
        print("TABELAS CRIADAS COM SUCESSO!")
    except Exception as e:
        print(f"ERRO AO TENTAR CRIAR TABELAS: {str(e)}")