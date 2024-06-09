#models/users.py
from .db import get_connection
from werkzeug.security import generate_password_hash, check_password_hash

mydb = get_connection()

class User:
    def __init__(self, id_user='', id_type='', user_username='', user_name='', 
                user_lastname='', user_email='', user_password='', user_direction='', user_phoneNumber='', user_image=''):
        self.id_user = id_user
        self.id_type = id_type
        self.user_username = user_username
        self.user_name = user_name
        self.user_lastname = user_lastname
        self.user_email = user_email
        self.user_password = user_password
        self.user_direction = user_direction
        self.user_phoneNumber = user_phoneNumber
        self.user_image = user_image

    def save(self):
        with mydb.cursor() as cursor:
            self.user_password = generate_password_hash(self.user_password)
            sql = "INSERT INTO users (id_type, user_username, user_name, user_lastname, user_email, user_password, user_direction, user_phoneNumber, user_image) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (self.id_type, self.user_username, self.user_name, self.user_lastname, self.user_email, self.user_password, self.user_direction, self.user_phoneNumber, self.user_image)
            cursor.execute(sql, values)
        mydb.commit() 

    def update(self):
        with mydb.cursor() as cursor:
            self.user_password = generate_password_hash(self.user_password)
            sql = "UPDATE users SET id_type=%s, user_username=%s, user_name=%s, user_lastname=%s, user_email=%s, user_password=%s, user_direction=%s, user_phoneNumber=%s, user_image=%s WHERE id_user = %s"
            values = (self.id_type, self.user_username, self.user_name, self.user_lastname, self.user_email, self.user_password, self.user_direction, self.user_phoneNumber, self.user_image, self.id_user)
            #revisar errores 
            # print(f"SQL: {sql}")
            # print(f"Values: {values}")
            cursor.execute(sql, values)
            mydb.commit()
        return self.id_user 

    def delete(self):
        with mydb.cursor() as cursor:
            sql = f"DELETE FROM users WHERE id_user = { self.id_user }"
            cursor.execute(sql)
            mydb.commit()
        return self.id_user

    @staticmethod
    def get(id_user):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT * FROM users WHERE id_user = { id_user }"
            cursor.execute(sql)
            user = cursor.fetchone()
            if user:
                user = User(id_user=user["id_user"],
                            id_type=user["id_type"],
                            user_username=user["user_username"],
                            user_name=user["user_name"],
                            user_lastname=user["user_lastname"],
                            user_email=user["user_email"],
                            user_password=user["user_password"],
                            user_direction=user["user_direction"],
                            user_phoneNumber=user["user_phoneNumber"],
                            user_image=user["user_image"])
                return user
            return None

    @staticmethod
    def __get__(id_user):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT * FROM users WHERE id_user = { id_user }"
            cursor.execute(sql)
            user = cursor.fetchone()
            if user:
                user = User(id_user=user["id_user"],
                            id_type=user["id_type"],
                            user_username=user["user_username"],
                            user_name=user["user_name"],
                            user_lastname=user["user_lastname"],
                            user_email=user["user_email"],
                            user_password=user["user_password"],
                            user_direction=user["user_direction"],
                            user_phoneNumber=user["user_phoneNumber"],
                            user_image=user["user_image"])
                return user
            return None
        
    @staticmethod
    def get_all():
        users = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM vista_usuarios"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                user = User(
                    id_user=row["id de usuario"],
                    id_type=row["tipo de usuario"],
                    user_username=row["nombre de usuario"],
                    user_name=row["nombre"],
                    user_lastname=row["apellido"],
                    user_email=row["correo electronico"],
                    user_direction=row["direccion"],
                    user_phoneNumber=row["numero de telefono"]
                )
                users.append(user)
        return users

    @staticmethod
    def check_username(user_username):
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT id_user FROM users WHERE user_username = %s"
            cursor.execute(sql, (user_username,))
            result = cursor.fetchone()
            return result is not None

    @staticmethod
    def check_email(user_email):
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT id_user FROM users WHERE user_email = %s"
            cursor.execute(sql, (user_email,))
            result = cursor.fetchone()
            return result is not None

    @staticmethod
    def check_password(user_password):
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT id_user FROM users WHERE user_password = %s"
            cursor.execute(sql, (user_password,))
            result = cursor.fetchone()
            return result is not None

    @staticmethod
    def check_password_hash(user_password):
        return check_password_hash(self.user_password, user_password) # type: ignore

    @staticmethod
    def get_by_password(user_username, user_password):
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT id_user, user_username, user_password FROM users WHERE user_username = %s"
            val = (user_username,)
            cursor.execute(sql, val)
            user = cursor.fetchone()
            print(user)
            if user != None:
                if check_password_hash(user["user_password"], user_password):
                    return User.__get__(user["id_user"])
            return None

class Type:
    def __init__(self, id_type='', type_name=''):
        self.id_type = id_type
        self.type_name = type_name
    
    @staticmethod
    def get_all():
        types = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM type"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                type= Type(id_type=row["id_type"], type_name=row["type_name"])
                types.append(type)
        return types