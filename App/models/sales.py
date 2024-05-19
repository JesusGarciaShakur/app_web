# id_sale, id_user, id_product, sale_date, total_sale
from .db import get_connection

mydb = get_connection()

class Sale:
    def __init__(self, id_sale, id_user, id_product, sale_date, total_sale):
        self.id_sale = id_sale
        self.id_user = id_user
        self.id_product = id_product
        self.sale_date = sale_date
        self.total_sale = total_sale

    def save(self):
        with mydb.cursor() as cursor:
            sql = "INSERT INTO sales (id_user, id_product, sale_date, total_sale) VALUES (%s, %s, %s, %s)"
            val = (self.id_user, self.id_product, self.sale_date, self.total_sale)
            cursor.execute(sql, val)
        mydb.commit()

    def update(self):
        with mydb.cursor() as cursor:
            sql = "UPDATE sales SET id_user = %s, id_product = %s, sale_date = %s, total_sale = %s WHERE id_sale = %s"
            values = (self.id_user, self.id_product, self.sale_date, self.total_sale)
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
                            id_user=sale["id_user"],
                            id_product=sale["id_product"],
                            sale_date=sale["sale_date"],
                            total_sale=sale["total_sale"])
                return sale
            return None