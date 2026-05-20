from database.connectDB import get_db_connection, dict_fetchall, dict_fetchone

class Expense:
    # construtor da classe Expense
    def __init__(self, title, value, category, date=None, id=None):
        self.id = id
        self.title = title
        self.value = value
        self.category = category
        self.date = date


class ExpenseModel:
    # função para criar a tabela do modelo, apenas se não existir
    @staticmethod
    def create_table():
        conn = None
        try:
            conn, cursor = get_db_connection()

            sql_query = """
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    value REAL NOT NULL,
                    category TEXT NOT NULL,
                    date TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
            """
            cursor.execute(sql_query)
            conn.commit()

            return True 
        except Exception as e:
            raise Exception(str(e))
        finally:
            if conn:
                conn.close()

    # função que retorna todas as despesas cadastradas no sistema
    @staticmethod
    def get_all():
        conn = None
        try:
            conn, cursor = get_db_connection()

            sql_query = "SELECT * FROM expenses"
            cursor.execute(sql_query)

            expenses = dict_fetchall(cursor)

            return expenses
        except Exception as e:
            raise Exception(str(e))
        finally:
            if conn:
                conn.close()
    
    # função para buscar a despesa cadastrada no sistema com base no ID
    def get_by_id(expense_id):
        conn = None
        try:
            conn, cursor = get_db_connection()

            sql_query = "SELECT * FROM expenses WHERE id = ?"
            values = (expense_id,)

            cursor.execute(sql_query, values)
            expense = dict_fetchone(cursor)

            return expense
        except Exception as e:
            raise Exception(str(e))
        finally:
            if conn:
                conn.close()

    # função para inserir a despesa no banco de dados
    @staticmethod
    def save(expense):
        conn = None
        try:
            conn, cursor = get_db_connection()

            sql_query = """
                INSERT INTO expenses (title, value, category)
                VALUES (?, ?, ?)
            """
            values = (expense.title, expense.value, expense.category)

            cursor.execute(sql_query, values)
            conn.commit()

            expense.id =  cursor.lastrowid
            return expense
        except Exception as e:
            raise Exception(str(e))
        finally:
            if conn:
                conn.close()

    def delete(expense_id):
        conn = None
        try:
            conn, cursor = get_db_connection()

            sql_query = "DELETE FROM expenses WHERE id = ?"
            values = (expense_id,)

            cursor.execute(sql_query, values)
            conn.commit()

            return "ok"
        except Exception as e:
            raise Exception(str(e))
        finally:
            if conn:
                conn.close()