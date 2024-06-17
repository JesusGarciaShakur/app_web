# id_sale, userName_sale, product_name, sale_date, total_sale, direction, pieces
from .db import get_connection

mydb = get_connection()

class Sale:
    def __init__(self, id_sale='', userName_sale='', product_name='', sale_date='', total_sale='', direction='', pieces=''):
        self.id_sale = id_sale
        self.userName_sale = userName_sale
        self.product_name = product_name
        self.sale_date = sale_date
        self.total_sale = total_sale
        self.direction = direction
        self.pieces = pieces

    def save(self):
        with mydb.cursor() as cursor:
            sql = "INSERT INTO sales (userName_sale, product_name, sale_date, total_sale, direction, pieces) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (self.userName_sale, self.product_name, self.sale_date, self.total_sale, self.direction, self.pieces)
                        #revisar errores 
            print(f"SQL: {sql}")
            print(f"Values: {val}")
            cursor.execute(sql, val)
        mydb.commit()

    def update(self):
        with mydb.cursor() as cursor:
            sql = "UPDATE sales SET userName_sale = %s, product_name = %s, sale_date = %s, total_sale = %s, direction = %s, pieces = %s WHERE id_sale = %s"
            values = (self.userName_sale, self.product_name, self.sale_date, self.total_sale, self.direction, self.pieces)
            cursor.execute(sql, values)
            mydb.commit()
        return self.id_sale
    
    def delete(self):
        with mydb.cursor() as cursor:
            sql = f"DELETE FROM sales WHERE id_sale = { self.id_sale }"
            cursor.execute(sql)
            mydb.commit()
        return self.id_sale
    
    @staticmethod
    def get(id_sale):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT * FROM sales WHERE id_sale = { id_sale }"
            cursor.execute(sql)
            sale = cursor.fetchone()
            if sale:
                sale = Sale(id_sale=sale["id_sale"],
                            userName_sale=sale["userName_sale"],
                            product_name=sale["product_name"],
                            sale_date=sale["sale_date"],
                            total_sale=sale["total_sale"],
                            direction=sale["direction"],
                            pieces=sale["pieces"])
                return sale
            return None

    @staticmethod
    def __get__(id_sale):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT * FROM sales WHERE id_sale = { id_sale }"
            cursor.execute(sql)
            sale = cursor.fetchone()
            if sale:
                sale = Sale(id_sale=sale["id_sale"],
                            userName_sale=sale["userName_sale"],
                            product_name=sale["product_name"],
                            sale_date=sale["sale_date"],
                            total_sale=sale["total_sale"],
                            direction=sale["direction"],
                            pieces=sale["pieces"])
                return sale
            return None
        
    @staticmethod
    def get_all():
        sales = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM sales"
            cursor.execute(sql)
            result = cursor.fetchall()
            for sale in result:
                sales.append(Sale(id_sale=sale["id_sale"],
                                userName_sale=sale["userName_sale"],
                                product_name=sale["product_name"],
                                sale_date=sale["sale_date"],
                                total_sale=sale["total_sale"],
                                direction=sale["direction"],
                                pieces=sales["pieces"]))
                sales.append(sale)
        return sales
    
class Product:
    def __init__(self, id_product='', product_name='', product_price='', product_description='',product_image = ''):
        self.id_product = product_name
        self.product_name = product_name
        self.product_price = product_price
        self.product_description = product_description
        self.product_image = product_image

    @staticmethod
    def get_all():
        products = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM products"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                product = Product(product_name=row["product_name"],
                                product_price=row["product_price"],
                                product_description=row["product_description"],
                                product_image=row["product_image"])
                products.append(product)
        return products