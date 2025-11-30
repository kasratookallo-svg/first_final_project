# Supermarket Application
# Made by Kasra Tookallo
# 2025 the year
# 11/28/2025

import re
from datetime import date, datetime
import pickle

product_list = []

#--------------------------------------------------------------------------------------------------
# First approach : Class
class Product :
    def __init__(self, id , name, brand , quantity ,  price ,expire_date):
        self.product_id = id
        self.name = name
        self.brand = brand
        self.quantity = quantity
        self.price = price
        self.expire_date = datetime.strptime(expire_date, "%Y-%m-%d").date()

    # Method_function
    def is_valid(self):
        if not (type(self.product_id ) == int and self.product_id > 0):
            raise NameError("Invalid product ID")

        if not re.match(r"^[a-zA-Z\s]{3,30}$", self.name):
            raise NameError("Invalid name!")

        if not re.match(r"^[a-zA-Z\s]{3,30}$", self.brand):
            raise NameError("Invalid brand!")

        if not (type(self.quantity) == int and self.quantity > 0):
            raise NameError("Invalid quantity!")

        if not (type(self.price) == float and self.price > 0):
            raise NameError("Invalid price!")

        if not self.expire_date >= datetime.today().date():
            raise NameError("Invalid expiration date!")

        return True

    # Representation
    def __repr__(self):
        return print(f"Each Product Info ====>> ID Num : {self.product_id:10} ---> Name :{self.name:10}, Brand :{self.brand:10}, Quantity :{self.quantity:5}, Price :{self.price:5}, Exp.Date :{self.expire_date}")

    def to_tuple(self):
        return tuple((self.product_id, self.name, self.brand, self.quantity, self.price, self.expire_date))

#-----------------------------------------------------------------------------------------------
# Second appproach : Function_handling

def name_validator(name):
    if re.match(r"^[a-zA-Z\s]{2,20}$", name):
        return name
    else:
        raise ValueError("Name must be a string")

def brand_validator(brand):
    if re.match(r"^[a-zA-Z\s]{2,20}$", brand):
        return brand
    else:
        raise ValueError("Brand must be a string")

def price_validator(price):
    if type(price) == float and price > 0:
        return price
    else:
        raise ValueError("Price must be a positive number")

def quantity_validator(quantity):
    if type(quantity) == int and quantity > 0:
        return quantity
    else:
        raise ValueError("Quantity must be a positive number")

def expire_validator(expire_date):
    if type(expire_date) != date and expire_date >= date.today():
        raise ValueError("Expiration date must be YYYY-MM-DD.")

def creat_products_and_validate(id ,name , brand , quantity , price , expiration_date):
    #id_validator(id_number)
    name_validator(name)
    brand_validator(brand)
    quantity_validator(quantity)
    price_validator(price)
    # تبدیل تاریخ از رشته به تاریخ
    expire_date = datetime.strptime(expiration_date, "%Y-%m-%d").date()
    expire_validator(expire_date)

    product = {
        "id_number": id,
        "name": name,
        "brand": brand,
        "quantity": quantity,
        "price": price,
        "expire_date": expire_date
    }
    return product

#------------------------------------------------------------------------------------------------

def calculate_total(product_list):
    # If there is no product available show this message
    if not product_list:
        raise ValueError("No Products", "There are no products saved.")


    total = 0

    for product in product_list:
        total = total + product["quantity"] * product["price"]
    return total

def save_to_file(product_list):
    file = open("supermarket_app.dat", "wb")
    pickle.dump(product_list, file)
    file.close()

# ---------------------------------------------------------------------------------------------------
                                        # Encapsulation
# def get_product_name(self):
#   return self.product_name

# def get_product_id(self):
#   return self.product_id

# def get_product_brand(self):
#   return self.product_brand

# def get_product_quantity(self):
#   return self.product_price

# def set_product_name(self, product_name):
#  if not re.match(r"^[a-zA-Z\s]{3,30}$",self.product_name):
#     raise NameError("Product Name must be letter and space !!!!")
# self.__product_name = product_name

# def set_product_brand(self, product_brand):
#  if not re.match(r"^[a-zA-Z\s]{3,30}$",self.product_brand):
#     raise NameError("Product Brand must be letter and space !!!!")
# self.__product_brand = product_brand

# def set_product_quantity(self, product_quantity):
#  if not (type(self.product_quantity) == int and self.product_quantity > 0):
#     raise NameError("Product Quantity Error!!!!")
# self.__product_quantity = product_quantity

# def set_product_price(self, product_price):
#  if not (type(self.product_price) == int and self.product_price > 0):
#     raise NameError("Product Price Error!!!!")
# self.__product_price = product_price

# product_name = property(get_product_name, set_product_name)
# product_brand = property(get_product_brand, set_product_brand)
# product_quantity = property(get_product_quantity, set_product_quantity)
# product_price = property(get_product_price, set_product_price)
# --------------------------------------------------------------------------------------------------------

