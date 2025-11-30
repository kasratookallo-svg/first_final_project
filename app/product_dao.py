import sqlite3

class ProductDataAccess:
    def save(self, product):
        with sqlite3.connect("supermarket_app_backup.db") as connection:
            cursor = connection.cursor()
            cursor.execute(
                "insert into products (id,name,brand,quantity,price,expiration_date) values(?,?,?,?,?,?)",
                [product.id,product.name,product.brand,product.quantity,product.price,product.expiration_date])
            connection.commit()

    def edit(self,product):
        with sqlite3.connect("supermarket_app_backup.db") as connection:
            cursor = connection.cursor()
            cursor.execute("update products set name=?,brand=?,quantity=?,price=? , expiration_date=? ,where id=?",
                           [product.name,product.brand,product.quantity,product.price,product.expiration_date,product.id])
            connection.commit()

    def remove(self,product_id):
        with sqlite3.connect("supermarket_app_backup.db") as connection:
            cursor = connection.cursor()
            cursor.execute("delete from products where id=?",[product_id])
            connection.commit()

    def find_all(self):
        with sqlite3.connect("supermarket_app_backup.db") as connection:
            cursor = connection.cursor()
            cursor.execute("select * from products order by name")
            return cursor.fetchall()
