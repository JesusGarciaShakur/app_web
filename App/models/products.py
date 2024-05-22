#id_product, product_name, product_price, product_description
from .db import get_connection

mydb = get_connection()

class Product:
    def __init__(self, id_product, product_name, product_price, product_description):
        self.id_product = id_product
        self.product_name = product_name
        self.product_price = product_price
        self.product_description = product_description

    def save(self):
        with mydb.cursor() as cursor:
            sql = "INSERT INTO products (product_name, product_price, product_description) VALUES (%s, %s, %s)"
            values = (self.product_name, self.product_price, self.product_description)
            cursor.execute(sql, values)
        mydb.commit()

    def update(self):
        with mydb.cursor() as cursor:
            sql = "UPDATE products SET product_name = %s, product_price = %s, product_description = %s WHERE id_product = %s"
            values = (self.product_name, self.product_price, self.product_description)
            cursor.execute(sql, values)
            mydb.commit()
        return self.id_product

    def delete(self):
        with mydb.cursor() as cursor:
            sql = f"DELETE FROM products WHERE id_product = { self.id_product }"
            cursor.execute(sql)
            mydb.commit()
        return self.id_product

    @staticmethod
    def get(id_product):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT * FROM products WHERE id_product = { id_product }"
            cursor.execute(sql)
            product = cursor.fetchone()
            if product:
                product = Product(id_product=product["id_product"],
                                product_name=product["product_name"],
                                product_price=product["product_price"],
                                product_description=product["product_description"])
                return product
            return None
    
    @staticmethod
    def get_all():
        products = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM products"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                product = Product(id_product=row["id_product"],
                                product_name=row["product_name"],
                                product_price=row["product_price"],
                                product_description=row["product_description"])
                products.append(product)
        return products 