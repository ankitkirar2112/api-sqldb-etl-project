import requests as req

def fetch_carts(url):
    try:
        response = req.get(url)
        response.raise_for_status()
        if response.status_code==200:
            return response.json()
    # except req.HTTPError as htt_error:
    # except req.ConnectionError as cnn_err:
    # except req.Timeout as t:
    # except ValueError:
    except req.RequestException as e:
        print(f"Unexpected Error: {e}")


# url = 'https://fakestoreapi.com/carts'
# fetch_carts(url)