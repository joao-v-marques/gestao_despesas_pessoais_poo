from models.expense import Expense, ExpenseModel

class ExpenseService:

    @staticmethod
    def get_all():
        expenses = ExpenseModel.get_all()

        return expenses
    
    @staticmethod
    def get_expense_id(expense_id):
        expense = ExpenseModel.get_by_id(expense_id)

        return expense

    @staticmethod
    def create(data):
        if data["value"] <= 0:
            raise ValueError("O valor deve ser maior que zero")
        
        expense = Expense(
            title=data["title"],
            value=data["value"],
            category=data["category"]
        )

        saved_expense = ExpenseModel.save(expense)
        return saved_expense
    
    def delete(expense_id):
        if not expense_id:
            raise Exception("ID Inválido")
        
        ExpenseModel.delete(expense_id)
        return "ok"