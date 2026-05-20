from flask import Blueprint, request, jsonify
from services.expense_services import ExpenseService

bp_expenses = Blueprint("bp_expenses", __name__)

# função para buscar por todas as depesas cadastradas no sistema
@bp_expenses.route("/expenses", methods=['GET'])
def get_expeses():
    try:
        expenses = ExpenseService.get_all()

        return expenses
    except Exception as e:
        return jsonify({
            "message": str(e)
        })
    
@bp_expenses.route("/expenses/<int:id>", methods=['GET'])
def get_expense(expense_id):
    try:
        expense = ExpenseService.get_expense_id(expense_id)

        return expense
    except Exception as e:
        return jsonify({
            "message": str(e)
        })
        

# função para cadastrar nova despesa
@bp_expenses.route("/expenses", methods=['POST'])
def create_expense():
    try:
        # precisa ter title, value e category para cadastrar
        data = request.get_json()

        ExpenseService.create(data)
        return jsonify({
            "message": "Usuário inserido com sucesso!"
        }), 200
    except Exception as e:
        return jsonify({
            "message": str(e)
        })