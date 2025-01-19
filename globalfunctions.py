import pickle
import requests
import random
import time
from fake_useragent import UserAgent


def save_to_pickle(filename="output.pkl", obj=None):
    try:
        with open(filename, "wb") as file:
            pickle.dump(obj, file)
    except Exception as e:
        print(f"Error in save_to_pickle function, Error text: {e}")
def load_from_pickle(filename="output.pkl"):
    try:
        with open(filename, "rb") as file:
            return pickle.load(file, encoding="utf-8")
    except Exception as e:
        print(f"Error in load_from_pickle function, Error text: {e}")
        return 

def secure_request(url, method="GET", headers=None, payload=None, proxies=None, session=None):
    """
    Makes a secure and human-like request to the given URL.

    Args:
        url (str): The URL to make the request to.
        method (str): HTTP method (GET, POST, etc.). Defaults to GET.
        headers (dict): Custom headers for the request.
        payload (dict): Data to send with POST requests.
        proxies (dict): Proxy settings for the request.
        session (requests.Session): Optional session for maintaining cookies.

    Returns:
        Response object from the request.
    """
    # Use a session or create a new one
    session = session or requests.Session()

    # Generate a random User-Agent if not provided
    ua = UserAgent()
    headers = headers or {}
    headers['User-Agent'] = headers.get('User-Agent', ua.random)
    
    # Add other common headers to mimic browsers
    headers.setdefault('Accept-Language', 'en-US,en;q=0.9')
    headers.setdefault('Accept-Encoding', 'gzip, deflate, br')
    headers.setdefault('Referer', 'https://www.google.com/')

    # Add randomized delay to mimic human behavior
    time.sleep(random.uniform(1, 5))

    # Make the request
    try:
        if method.upper() == "GET":
            response = session.get(url, headers=headers, proxies=proxies)
        elif method.upper() == "POST":
            response = session.post(url, headers=headers, data=payload, proxies=proxies)
        else:
            raise ValueError("Unsupported HTTP method: " + method)

        # Return the response
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        return response

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None    
