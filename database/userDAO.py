import pymysql
from api.models.userModel import UserModel
import hashlib
from config.userServiceConfig import UserServiceConfiguration


class UserDAO:

    def __init__(self):
        self.connection: pymysql.Connection = None
        self.user_service_configuration: UserServiceConfiguration = UserServiceConfiguration()

    def create_connection(self) -> pymysql.Connection:
        try:
            if not self.connection:
                self.connection = pymysql.connect(host=self.user_service_configuration.instance.HOST,
                                                  user=self.user_service_configuration.instance.USER,
                                                  password=self.user_service_configuration.instance.PASSWORD,
                                                  db=self.user_service_configuration.instance.DB,
                                                  charset=self.user_service_configuration.instance.CHARSET,
                                                  cursorclass=pymysql.cursors.DictCursor)
            return self.connection
        except pymysql.MySQLError as err:
            print("user service create_connection error : ")
            print(err)
            return None

    def retrieve_users(self):
        try:
            cursor = self.create_connection().cursor()
            cursor.execute("SELECT * "
                           "FROM user")
            result = cursor.fetchall()
            return result
        except pymysql.MySQLError as err:
            print("user service retrieve_users error : ")
            print(err)
            return None

    def add_user(self, user_model: UserModel) -> bool:
        try:
            user_hashed_password: str = hashlib.sha512(str(user_model.password + user_model.salt).encode('utf-8')).hexdigest()
            cursor = self.create_connection().cursor()
            cursor.execute("INSERT INTO user (Id, Username, Password, Salt)"
                           "VALUES(%s,%s,%s, %s)", (user_model.id, user_model.username, user_hashed_password, user_model.salt))
            self.connection.commit()
            return True
        except pymysql.MySQLError as err:
            print("user service add_user error : ")
            print(err)
            return False

    def retrieve_user(self, user_id: str):
        try:
            cursor = self.create_connection().cursor()
            cursor.execute("SELECT * "
                           "FROM user "
                           "WHERE Id = %s", (user_id,))
            result = cursor.fetchone()
            return result
        except pymysql.MySQLError as err:
            print("user service retrieve_user error : ")
            print(err)
            return None

    def remove_user(self, user_id: str) -> bool:
        try:
            cursor = self.create_connection().cursor()
            cursor.execute("DELETE FROM user "
                           "WHERE Id = %s", (user_id,))
            self.connection.commit()
            return True
        except pymysql.MySQLError as err:
            print("user service remove_user error : ")
            print(err)
            return False

    def retrieve_user_by_username(self, username: str):
        try:
            cursor = self.create_connection().cursor()
            cursor.execute("SELECT * "
                           "FROM user "
                           "WHERE Username = %s", (username,))
            result = cursor.fetchone()
            return result
        except pymysql.MySQLError as err:
            print("user service retrieve_user_by_username error : ")
            print(err)
            return None
