from .db import get_connection

mydb = get_connection()

class Type:
    def __init__(self, id_type='', type_name=''):
        self.id_type = id_type
        self.type_name = type_name

    def save(self):
        with mydb.cursor as cursor:
            sql = "INSERT INTO type (type_name) VALUES (%s)"
            val = (self.type_name,)
            cursor.execute(sql, val)
        mydb.commit()
        
    def update(self):
        with mydb.cursor as cursor:
            sql = "UPDATE type SET type_name = %s WHERE id_type = %s"
            val = (self.type_name, self.id_type)
            cursor.execute(sql, val)
            mydb.commit()
        return self.id_type
    
    def delete(self):
        with mydb.cursor as cursor:
            sql = f"DELETE FROM type WHERE id_type = { self.id_type }"
            cursor.execute(sql)
            mydb.commit()
        return self.id_type
    
    @staticmethod
    def get(id_type):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT * FROM type WHERE id_type = { id_type }"
            cursor.execute(sql)
            type = cursor.fetchone()
            if type:
                type = Type(id_type=type["id_type"],
                            type_name=type["type_name"])
                return type
            return None
    
    @staticmethod
    def __get__(id_type):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT * FROM type WHERE id_type = { id_type }"
            cursor.execute(sql)
            type = cursor.fetchone()
            if type:
                type = Type(id_type=type["id_type"],
                            type_name=type["type_name"])
                return type
            return None

    @staticmethod
    def get_all():
        types = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM type"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                type = Type(id_type=row["id_type"],
                            type_name=row["type_name"])
                types.append(type)
        return types