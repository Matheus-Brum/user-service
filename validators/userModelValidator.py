from validators.commonValidator import CommonValidator
from api.models.userModel import UserModel


class UserModelValidator:

    @staticmethod
    def validate_user_model(user_model: UserModel) -> bool:
        return not CommonValidator.is_none(user_model) and not CommonValidator.is_empty(user_model) and \
                not CommonValidator.is_none(user_model.id) and not CommonValidator.is_none(user_model.username) and \
                not CommonValidator.is_none(user_model.password) and not CommonValidator.is_empty(user_model.id) and \
                not CommonValidator.is_empty(user_model.username) and not CommonValidator.is_empty(user_model.password) and \
                CommonValidator.validate_id(user_model.id) and CommonValidator.validate_string(user_model.username, 12, 50) and \
                CommonValidator.validate_string(user_model.password, 12, 128)
