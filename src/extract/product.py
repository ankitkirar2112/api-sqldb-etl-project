import requests  as req
import logging 

# Create the logger
logger = logging.getLogger('product_extract')
logger.setLevel(logging.DEBUG)

# Create Handler
handler = logging.FileHandler('extract.log')
format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(format)
logger.addHandler(handler)


def extract_data_api(url):
    logger.info("Product data extraction step started")
    logger.info(f"API URL : {url}")

    try:
        logger.info("Hitting the API...")
        response=req.get(url)
        logger.debug(f"API response with Status Code : {response.status_code}")

        # Warning for unexpected status code
        if response.status_code !=200:
            logger.warning(f"Unexpected status code received: {response.status_code}")
        
        # Raise the Error
        response.raise_for_status()
        data = response.json()

        if not isinstance(data,list):
            logger.warning("API did not return a list . Data Structure may be different")

        if response.status_code ==200:
            logger.debug(f"Extrected {len(data)} records from Product API ")
            return data
        
    except req.exceptions.HTTPError as htt_err:
        logger.error(f"HTTP Error occured: {htt_err} | Status code: {response.status_code}")
        logger.exception(htt_err)
    except req.exceptions.ConnectionError as cnn_err:
        logger.error(f"Connection Error :Uable to connect to the API | ERROR")
        logger.exception(cnn_err)
    except req.exceptions.Timeout as t:
        logger.error(f"Timeout Error : API took too long time to respond")
        logger.exception(t)
    except ValueError:
        logger.error("Invalid JSON format receive from API .")
        logger.exception(ValueError)
    except req.exceptions.RequestException as e:
        logger.error(f"Unexpected Error: {e}")
        logger.exception(e)
    finally:
        logger.info("Product data extraction step finished")
    return []

    


