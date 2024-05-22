from .db import get_connection

mydb = get_connection()

class Comment:
    def __init__(self, id_comment='', content_comment='', email_comment='', date_comment='', nameUser_comment=''):
        self.id_comment = id_comment
        self.content_comment = content_comment
        self.email_comment = email_comment
        self.date_comment = date_comment
        self.nameUser_comment = nameUser_comment

    def save(self):
            with mydb.cursor() as cursor:
                sql = "INSERT INTO comments (content_comment, email_comment, date_comment, nameUser_comment) VALUES (%s, %s, %s, %s)"
                values = (self.content_comment, self.email_comment, self.date_comment, self.nameUser_comment)
                cursor.execute(sql, values)
            mydb.commit()

    def update(self):
        with mydb.cursor() as cursor:
            sql = "UPDATE comments SET content_comment = %s, email_comment = %s, date_comment = %s, nameUser_comment = %s WHERE id_comment = %s"
            values = (self.content_comment, self.email_comment, self.date_comment, self.nameUser_comment)
            cursor.execute(sql, values)
            mydb.commit()
        return self.id_comment
    
    def delete(self):
        with mydb.cursor() as cursor:
            sql = f"DELETE FROM comments WHERE id_comment = { self.id_comment }"
            cursor.execute(sql)
            mydb.commit()
        return self.id_comment
    
    @staticmethod
    def get(id_comment):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT * FROM comments WHERE id_comment = { id_comment }"
            cursor.execute(sql)
            comment = cursor.fetchone()
            if comment:
                comment = Comment(id_comment=comment["id_comment"],
                                content_comment=comment["content_comment"],
                                email_comment=comment["email_comment"],
                                date_comment=comment["date_comment"],
                                nameUser_comment=comment["nameUser_comment"])
                return comment
            return None
        

    @staticmethod
    def __get__(id_user):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT * FROM comments WHERE id_user = { id_user }"
            cursor.execute(sql)
            comments = cursor.fetchall()
            if comments:
                comments = [Comment(id_comment=comment["id_comment"],
                                content_comment=comment["content_comment"],
                                email_comment=comment["email_comment"],
                                date_comment=comment["date_comment"],
                                nameUser_comment=comment["nameUser_comment"]) for comment in comments]
                return comments
            return None
        

    @staticmethod
    def get_all():
        comments = [] #Declara una lista vacía antes del bucle
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM comments"
            cursor.execute(sql)
            comments = cursor.fetchall()
        if comments:
                comments = [Comment(id_comment=comment["id_comment"],
                                content_comment=comment["content_comment"],
                                email_comment=comment["email_comment"],
                                date_comment=comment["date_comment"],
                                nameUser_comment=comment["nameUser_comment"]) for comment in comments]
                return comments
        return None
