import requests  as req
import json
import pandas as pd
from pathlib import Path
from src import config
# def authentication():
#     pass

def extract_data_api(url):
    try:
        response=req.get(url)
        response.raise_for_status()
        if response.status_code ==200:
            return response.json()
    except req.exceptions.HTTPError as htt_err:
        print(f"HTTP Error occured: {htt_err} | Status code: {response.status_code}")
    except req.exceptions.ConnectionError as cnn_err:
        print(f'Connection Error :Uable to connect to the API | ERROR: {cnn_err}')
    except req.exceptions.Timeout as t:
        print(f"Timeout Error : API took too long time to respond")
    except ValueError:
        print("Invalid JSON format receive from API .")
    except req.exceptions.RequestException as e:
        print(f"Unexpected Error: {e}")
    

# def save_to_json(data,path):
#     with open(f'{path}\product.json','w') as f:
#         for records in data:
#            line = json.dumps(records,indent=2)
#            f.write(line+'\n')

# def save_to_json_df(data):
#      df=  pd.DataFrame(data)
#      df.to_json('product_sample.json')
#      df.to_csv('product_data.csv')

    
url = 'https://fakestoreapi.com/products'
data = extract_data_api(url)
# save_to_json(data,config.DATA_DIR)
# save_to_json_df(data)

