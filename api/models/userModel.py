class UserModel:

    def __init__(self):
        self.id: str = None
        self.username: str = None
        self.password: str = None
        self.salt: str = None

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "salt": self.salt
        }
