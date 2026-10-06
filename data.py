import sqlite3


class Database:

    def __init__(self) -> None:

        self.conn = sqlite3.connect("reminder-data.db")
        cursor = self.conn.cursor()

        cursor.execute(
            "CREATE TABLE IF NOT EXISTS reminders("
            "id INTEGER PRIMARY KEY AUTOINCREMENT,"
            "type TEXT NOT NULL,"
            "message TEXT NOT NULL,"
            "duration INTEGER NOT NULL)"
        )

        self.conn.commit()

    def add_reminder(self, reminder_type: str, message: str, duration: int):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO reminders (type, message, duration) VALUES (?, ?, ?)",
            (reminder_type, message, duration)
        )
        self.conn.commit()

        return cursor.lastrowid

    def get_reminders(self):
        cursor = self.conn.execute(
            "SELECT id, type, message, duration FROM reminders"
        )
        return cursor.fetchall()

    def delete_reminder(self, reminder_id: int):
        self.conn.execute(
            "DELETE FROM reminders WHERE id = ?",
            (reminder_id,)
        )
        self.conn.commit()