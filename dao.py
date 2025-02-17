import sqlite3
from typing import List, Tuple, Optional

class UserDAO:
    def __init__(self, db_name: str = "database.db"):
        self.conn = sqlite3.connect(db_name1)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL
                )
                """
            )
    
    def add_user(self, name: str, email: str) -> None:
        with self.conn:
            self.conn.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    
    def get_user_by_id(self, user_id: int) -> Optional[Tuple[int, str, str]]:
        cursor = self.conn.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        return cursor.fetchone()
    
    def get_all_users(self) -> List[Tuple[int, str, str]]:
        cursor = self.conn.execute("SELECT * FROM users")
        return cursor.fetchall()
    
    def update_user(self, user_id: int, name: str, email: str) -> None:
        with self.conn:
            self.conn.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (name, email, user_id))
    
    def delete_user(self, user_id: int) -> None:
        with self.conn:
            self.conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
    
    def close(self):
        self.conn.close()

# Приклад використання
if __name__ == "__main__":
    dao = UserDAO()
    dao.add_user("John Doe", "john@example.com")
    dao.add_user("Jane Doe", "jane@example.com")
    
    users = dao.get_all_users()
    print("Users:", users)
    
    user = dao.get_user_by_id(1)
    print("User with ID 1:", user)
    
    dao.update_user(1, "John Smith", "john.smith@example.com")
    print("Updated User 1:", dao.get_user_by_id(1))
    
    dao.delete_user(2)
    print("Users after deletion:", dao.get_all_users())
    
    dao.close()
