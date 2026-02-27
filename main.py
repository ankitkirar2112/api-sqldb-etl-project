from src.extract import product, users, carts
from src.load import data_load


# Read the product and load into db
product_data = product.extract_data_api('https://fakestoreapi.com/products')
data_load.insert_raw_data(product_data,'products')   

# Read the user data and load into db
users_data = users.fetch_users('https://fakestoreapi.com/users')
data_load.insert_raw_data(users_data,'users')

# Read the user data and load into db
carts_data = carts.fetch_carts('https://fakestoreapi.com/carts')
data_load.insert_raw_data(carts_data,'carts')
