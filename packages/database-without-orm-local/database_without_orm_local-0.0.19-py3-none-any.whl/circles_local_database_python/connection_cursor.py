class DatabaseCursor:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = None

    def connect(self):
        if self.cursor is None:
            self.cursor = self.connection.cursor()

    def execute(self, query):
        self.connect()  # Ensure the cursor is connected before executing
        self.cursor.execute(query)

    def fetchall(self):
        self.connect()  # Ensure the cursor is connected before fetching all
        return self.cursor.fetchall()

    def fetchone(self):
        self.connect()  # Ensure the cursor is connected before fetching one
        return self.cursor.fetchone()

    def close(self):
        if self.cursor is not None:
            self.cursor.close()
            self.cursor = None
.3