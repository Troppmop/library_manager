class User:
    def __init__(self, name:str, user_id:int):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []
    def __str__(self):
        borrowed_string = ""

        for book in self.borrowed_books:
            borrowed_string += "\t"+ book + "\n"
        return f"Name: {self.name} | ID: {self.user_id} | Borrowed Books: \n{borrowed_string}"