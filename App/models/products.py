#id_product, product_name, product_price, product_description
from .db import get_connection

mydb = get_connection()

class Product:
    def __init__(self, id_product='', product_name='', product_price='', product_description='',product_image = ''):
        self.id_product = id_product
        self.product_name = product_name
        self.product_price = product_price
        self.product_description = product_description
        self.product_image = product_image

    def save(self):
        with mydb.cursor() as cursor:
            sql = "INSERT INTO products (product_name, product_price, product_description, product_image) VALUES (%s,%s,%s,%s)"
            values = (self.product_name, self.product_price, self.product_description, self.product_image)
            cursor.execute(sql, values)
        mydb.commit()

    def update(self):
        with mydb.cursor() as cursor:
            sql = "UPDATE products SET product_name = %s, product_price = %s, product_description = %s, product_image = %s WHERE id_product = %s"
            values = (self.product_name, self.product_price, self.product_description, self.product_image, self.id_product)
            #revisar errores 
            #print(f"SQL: {sql}")
            #print(f"Values: {values}")
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
                                product_description=product["product_description"],
                                product_image=product["product_image"])
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
                                product_description=row["product_description"],
                                product_image=row["product_image"])
                products.append(product)
        return products 
    
    @staticmethod
    def get_paginated_products(page, per_page):
        offset = (page - 1) * per_page
        products = []

        with mydb.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT COUNT(*) FROM products")
            total = cursor.fetchone()["COUNT(*)"]

            cursor.execute("SELECT * FROM products ORDER BY `id_product` DESC LIMIT %s OFFSET %s", (per_page, offset))
            result = cursor.fetchall()
            for row in result:
                product = Product(id_product=row["id_product"],
                                product_name=row["product_name"],
                                product_price=row["product_price"],
                                product_description=row["product_description"],
                                product_image=row["product_image"])
                products.append(product)
            return products, total
        
    
    @staticmethod
    def search(query, page, per_page):
        offset = (page -1) * per_page
        sales = []
        search_query = f"%{query}%"

        with mydb.cursor(dictionary=True) as cursor:
            cursor.execute("""
                SELECT COUNT(*) FROM products 
                WHERE product_name LIKE %s OR product_price LIKE %s OR product_description LIKE %s
            """, (search_query, search_query, search_query))
            total = cursor.fetchone()['COUNT(*)']

            cursor.execute("""
                SELECT * FROM products 
                WHERE product_name LIKE %s OR product_price LIKE %s OR product_description LIKE %s
                ORDER BY `id_product` DESC LIMIT %s OFFSET %s
            """, (search_query, search_query, search_query, per_page, offset))
            result = cursor.fetchall()
            for row in result:
                product = Product(id_product=row["id_product"],
                                product_name=row["product_name"],
                                product_price=row["product_price"],
                                product_description=row["product_description"],
                                product_image=row["product_image"])
                sales.append(product)
            return sales, total