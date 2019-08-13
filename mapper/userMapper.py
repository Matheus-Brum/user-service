from api.models.userModel import UserModel


class UserMapper:

    def to_model(self, user_entity) -> UserModel:
        user_model: UserModel = UserModel()
        if user_entity:
            user_model.id = user_entity["Id"]
            user_model.username = user_entity["Username"]
            user_model.password = user_entity["Password"]
            user_model.salt = user_entity["Salt"]
        return user_model

    def to_entity(self):
        pass
