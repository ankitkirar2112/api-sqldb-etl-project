from src.extract import product, users, carts
from src.load import data_load

product_data = product.extract_data_api('https://fakestoreapi.com/products')
data_load.load_to_db(product_data,'products')   

users_data = users.fetch_users('https://fakestoreapi.com/users')
data_load.load_to_db(users_data,'users')

carts_data = carts.fetch_carts('https://fakestoreapi.com/carts')
data_load.load_to_db(carts_data,'carts')
