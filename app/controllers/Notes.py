
from system.core.controller import *

class Notes(Controller):
    def __init__(self, action):
        super(Notes, self).__init__(action)
        self.load_model("Note")

    def index(self):
        notes = self.models["Note"].get_all()
        return self.load_view('index.html', notes=notes)
    def index_json(self):
        notes = self.models["Note"].get_all()
        return jsonify(notes=notes)
    def create(self):
        info = {
            "title": request.form["title"],
            "description": request.form["description"]
        }
        self.models["Note"].create_new(info)
        return redirect("/notes/get_all")
        
    def delete(self, id):
        self.models["Note"].delete_note(id)
        return redirect("/notes/get_all")
    def update(self, id):
        info = {
            "id": id,
            "description": request.form["note_update"]
        }
        self.models["Note"].update_note(info)
        return redirect("/notes/get_all")
        
    def get_all(self):
        notes = self.models["Note"].get_all()
        return self.load_view("partial.html", notes=notes)


