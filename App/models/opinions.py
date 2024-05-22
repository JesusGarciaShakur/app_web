#id_opinion, username_opinion, id_product, rating_product, comment_opinion, date_opinion
from .db import get_connection

mydb = get_connection()

class Opinion:
    def __init__(self, id_opinion='', username_opinion='', id_product='', rating_product='', comment_opinion='', date_opinion=''):
        self.id_opinion = id_opinion
        self.username_opinion = username_opinion
        self.id_product = id_product
        self.rating_product = rating_product
        self.comment_opinion = comment_opinion
        self.date_opinion = date_opinion

    def save(self):
        with mydb.cursor() as cursor:
            sql = "INSERT INTO opinions (username_opinion, id_product, rating_product, comment_opinion, date_opinion) VALUES (%s, %s, %s, %s, %s)"
            values = (self.username_opinion, self.id_product, self.rating_product, self.comment_opinion, self.date_opinion)
            print(f"SQL: {sql}")
            print(f"Values: {values}")
            cursor.execute(sql, values)
        mydb.commit()

    def update(self):
        with mydb.cursor() as cursor:
            sql = "UPDATE opinions SET username_opinion = %s, id_product = %s, rating_product = %s, comment_opinion = %s, date_opinion = %s WHERE id_opinion = %s"
            values = (self.username_opinion, self.id_product, self.rating_product, self.comment_opinion, self.date_opinion)
            cursor.execute(sql, values)
            mydb.commit()
        return self.id_opinion

    def delete(self):
        with mydb.cursor() as cursor:
            sql = f"DELETE FROM opinions WHERE id_opinion = { self.id_opinion }"
            cursor.execute(sql)
            mydb.commit()
        return self.id_opinion
        
    @staticmethod
    def get(id_opinion):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT * FROM opinions WHERE id_opinion = { id_opinion }"
            cursor.execute(sql)
            opinion = cursor.fetchone()
            if opinion:
                opinion = Opinion(id_opinion=opinion["id_opinion"],
                                username_opinion=opinion["username_opinion"],
                                id_product=opinion["id_product"],
                                rating_product=opinion["rating_product"],
                                comment_opinion=opinion["comment_opinion"],
                                date_opinion=opinion["date_opinion"])
                return opinion
            return None
        
    @staticmethod
    def __get__(id_opinion):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT * FROM opinions WHERE id_opinion = { id_opinion }"
            cursor.execute(sql)
            opinion = cursor.fetchone()
            if opinion:
                opinion = Opinion(id_opinion=opinion["id_opinion"],
                                username_opinion=opinion["username_opinion"],
                                id_product=opinion["id_product"],
                                rating_product=opinion["rating_product"],
                                comment_opinion=opinion["comment_opinion"],
                                date_opinion=opinion["date_opinion"])
                return opinion
            return None
        
    @staticmethod
    def get_all():
        opinions = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM opinions"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                opinion = Opinion(id_opinion=row["id_opinion"],
                                username_opinion=row["username_opinion"],
                                id_product=row["id_product"],
                                rating_product=row["rating_product"],
                                comment_opinion=row["comment_opinion"],
                                date_opinion=row["date_opinion"])
                opinions.append(opinion)
        return opinions
    
class Product:
    def __init__(self, id_product, product_name, product_price, product_description):
        self.id_product = id_product
        self.product_name = product_name
        self.product_price = product_price
        self.product_description = product_description

    @staticmethod
    def get_all():
        products = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM products"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                product= Product(id_product=row["id_product"],
                                    product_name=row["product_name"],
                                    product_price=row["product_price"],
                                    product_description=row["product_description"])
                products.append(product)
            return products