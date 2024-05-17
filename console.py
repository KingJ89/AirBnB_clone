import cmd
import json

class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}

    @classmethod
    def from_dict(cls, data):
        return cls(data["id"], data["name"], data["email"])

    class StorageEngine:
        def __init__(self):
            self.data = {}

        def create(self, obj):
            self.data[obj.id] = obj

        def read(self, obj_id):
            return self.data.get(obj_id)

        def update(self, obj):
            if obj.id in self.data:
                self.data[obj.id] = obj

        def delete(self, obj_id):
            if obj_id in self.data:
                del self.data[obj_id]

class JSONFilePersistence:
    def __init__(self, filename):
        self.filename = filename

    def save(self, data):
        with open(self.filename, 'w') as f:
            json.dump(data, f, default=lambda obj: obj.to_dict(), indent=4)

    def load(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                return {int(k): User.from_dict(v) for k, v in data.items()}
            except FileNotFoundError:
                return {}

class Console(cmd.Cmd):
    intro = "Welcome to the ALX hbnb console project. Type ? to list commands."
    prompt = "HbnbJan$ "

    def __init__(self, storage, persistance):
        super().__init__()
        self.storage = storage
        self.persistance = persistance

    def do_create_user(self, args):
        """
        Create a new user. Usage: create_user <id> <name> <email>
        """
        try:
            id, name, email = args.split()
            user = User(int(id), name, email)
            self.storage.create(user)
            self.persistance.save(self.storage.data)
            print("User created successfully.Hello from Jan")
        except ValueError:
            print("Invalid arguments. Usage: create_user <id> <name> <email>")

        def do_read_user(self, args):
            """
            Read user details by ID. Usage: read_user <id>
            """
            try:
                id = int(args)
                user = self.storage.read(id)
                if user:
                    print(f"ID: {user.id}' Name: {user.name}, Email: {user.email}")
                else:
                    print("User not found.")
            except ValueError:
                print("Invalid arguments. Usage: read_user <id>")

    def do_update_user(self, args):
        """
        update existing user. Usage: update_user <id> <name> <email>
        """
        try:
            id, name, email = args.split()
            user = self.storage.read(int(id))
            if user:
                user.name = name
                user.email = email
                self.storage.update(user)
                self.persistance.save(self.storage.data)
                print("User updated successfully.")
            else:
                print("User not found.")
            except ValueError:
                print("Invalid arguments. Usage: update_user <id> <name> <email>")

        def do_delete_user(self, args):
            """
            Delete a user by ID. Usage: delete_user <id>
            """
            try:
                id = int(args)
                user = self.storage.read(id)
                if user:
                    self.storage.delete(id)
                    self.persistance.save(self.storage.data)
                    print("User deleted successfully.")
                else:
                    print("User not Found.")
            except ValueError:
                print("Invalid arguments. Usage: delete_user <id>")

        def do_quit(self, args):
            """
            quit console
            """
            return True

        if __name__ == "__main__":
            storage = StorageEngine()
            persistence = JSONFilePersistence("data.json")
            storage.data = persistence.load()
            console = Console(storage, persistence)
            console.prompt = "HbnbJan$ "
            console.cmdloop()
