
from system.core.model import Model

class Note(Model):
    def __init__(self):
        super(Note, self).__init__()
    def get_all(self):
        return self.db.query_db("SELECT id, title, description FROM notes")
    def create_new(self, info):
        query = "INSERT INTO notes (title, description, created_at, updated_at) VAlUES (%s, %s, now(), now())"
        data = [info["title"], info["description"]]
        return self.db.query_db(query, data)
    def delete_note(self, id):
        query = "DELETE FROM notes WHERE id = %s"
        data = [id]
        return self.db.query_db(query, data)
    def update_note(self, info):
        query = "UPDATE notes SET description = %s WHERE id = %s"
        data = [info["description"], info["id"]]
        return self.db.query_db(query, data)
