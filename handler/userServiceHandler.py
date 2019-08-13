from flask_restful import Resource
from flask import jsonify, abort, make_response, request
from uuid import uuid4
from api.models.userModel import UserModel
from database.userDAO import UserDAO
from mapper.userMapper import UserMapper
from validators.commonValidator import CommonValidator
from validators.userModelValidator import UserModelValidator


class Users(Resource):

    def __init__(self):
        self.userDAO: UserDAO = UserDAO()
        self.user_mapper: UserMapper = UserMapper()

    def get(self):
        if request.args.get('username'):
            username = request.args.get('username')
            user_entity = self.userDAO.retrieve_user_by_username(username)
            if user_entity:
                return make_response(jsonify(self.user_mapper.to_model(user_entity).serialize()), 200)
            abort(404)
        else:
            return [self.user_mapper.to_model(user_entity).serialize()
                    for user_entity in self.userDAO.retrieve_users()]

    def post(self):
        new_user: UserModel = UserModel()
        new_user.id = str(uuid4())
        new_user.username = request.json['username']
        new_user.password = request.json['password']
        new_user.salt = str(uuid4().hex)
        if UserModelValidator.validate_user_model(new_user):
            is_user_added: bool = self.userDAO.add_user(new_user)
            if is_user_added:
                return make_response(jsonify(new_user.serialize()), 201)
            print('unexpected error occurred.')
            abort(500)
        print('invalid user model.')
        abort(400)


class User(Resource):

    def __init__(self):
        self.userDAO: UserDAO = UserDAO()
        self.user_mapper: UserMapper = UserMapper()

    def get(self, user_id: str):
        if not CommonValidator.is_none(user_id) and CommonValidator.validate_id(user_id):
            user_entity = self.userDAO.retrieve_user(user_id)
            if user_entity:
                return make_response(jsonify(self.user_mapper.to_model(user_entity).serialize()), 200)
            print('no user found.')
            abort(404)
        print('invalid user id.')
        abort(400)

    def delete(self, user_id: str):
        if not CommonValidator.is_none(user_id) and CommonValidator.validate_id(user_id):
            user_entity = self.userDAO.retrieve_user(user_id)
            if user_entity:
                is_user_removed: bool = self.userDAO.remove_user(user_id)
                if is_user_removed:
                    return make_response(jsonify(self.user_mapper.to_model(user_entity).serialize()), 200)
                print('unexpected error occurred.')
                abort(500)
            print('no user found.')
            abort(404)
        print('invalid user id.')
        abort(400)

    def put(self, user_id: str):
        print('invalid user id or user model.')
        abort(400)
        pass
