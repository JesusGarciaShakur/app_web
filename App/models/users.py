#models/users.py
from .db import get_connection
from werkzeug.security import generate_password_hash, check_password_hash

mydb = get_connection()

class User:
    def __init__(self, id_user='', id_type='', user_username='', user_name='', 
                user_lastname='', user_email='', user_password='', user_direction='', user_phoneNumber=''):
        self.id_user = id_user
        self.id_type = id_type
        self.user_username = user_username
        self.user_name = user_name
        self.user_lastname = user_lastname
        self.user_email = user_email
        self.user_password = user_password
        self.user_direction = user_direction
        self.user_phoneNumber = user_phoneNumber

    def save(self):
            with mydb.cursor() as cursor:
                self.user_password = generate_password_hash(self.user_password)
                sql = "INSERT INTO users (id_type, user_username, user_name, user_lastname, user_email, user_password, user_direction, user_phoneNumber) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                values = (self.id_type, self.user_username, self.user_name, self.user_lastname, self.user_email, self.user_password, self.user_direction, self.user_phoneNumber)
                cursor.execute(sql, values)
            mydb.commit() 

    def update(self):
        with mydb.cursor() as cursor:
            sql = "UPDATE users SET user_username=%s, user_name=%s, user_lastname=%s, user_email=%s, user_direction=%s, user_phoneNumber=%s WHERE id_user = %s"
            val = (self.user_username, self.user_name, self.user_lastname, self.user_email, self.user_direction, self.user_phoneNumber)
            cursor.execute(sql, val)
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
                            user_phoneNumber=user["user_phoneNumber"])
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
                            user_phoneNumber=user["user_phoneNumber"])
                return user
            return None
        
    @staticmethod
    def get_all():
        users = []  #Declara la lista vacía antes del bucle
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM vista_usuarios"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                user = User(
                    id_user=row["id_user"],
                    Id_type=row["id_type"],
                    User_username=row["user_username"],
                    User_name=row["user_name"],
                    User_lastname=row["user_lastname"],
                    User_email=row["user_email"],
                    User_password=row["user_password"],
                    User_direction=row["user_direction"],
                    User_phoneNumber=row["user_phoneNumber"]
                )
                users.append(user)  #Agrega el objeto usar a la lista
        return users

    @staticmethod
    def check_username(user_username):
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT id_user FROM users WHERE user_username = %s"
            cursor.execute(sql, (user_username,))
            result = cursor.fetchone()  # Consumir el resultado del cursor
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
        # Esta función comprueba si la contraseña proporcionada coincide con la contraseña almacenada en el objeto del usuario
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