from product_dao import ProductDataAccess
from product_model import creat_products_and_validate
from product_view import *


class ProductController:

    @staticmethod
    def save(id, name, brand, quantity, price, expiraion_date):
        try:
            product = creat_products_and_validate(id,
                                                  name,
                                                  brand,
                                                  quantity,
                                                  price,
                                                  expiration_date)
            product_da = ProductDataAccess()
            product_da.save(product)
            return True, "Product successfully saved."
        except Exception as e:
            return False, f"Saving Error: {e}"

    @staticmethod
    def edit(id, name, brand, quantity, price, expiraion_date):
        try:
            product = creat_products_and_validate(id,
                                                  name,
                                                  brand,
                                                  quantity,
                                                  price,
                                                  expiration_date
                                                  )
            product_da = ProductDataAccess()
            product_da.save(product)
            return True, "Product successfully Edited."
        except Exception as e:
            return False, f"Edition Error: {e}"

    @staticmethod
    def remove(product_id):
        try:
            product_da = creat_products_and_validate()
            product_da.remove(product_id)
            return True, "Product successfully removed from Database."
        except Exception as e:
            return False, f"Removing Error: {e}"

    @staticmethod
    def find_all():
        try:
            product_da = ProductDataAccess()
            return True, product_da.find_all()
        except Exception as e:
            return False, f"Finding Error: {e}"