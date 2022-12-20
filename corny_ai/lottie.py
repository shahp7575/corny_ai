import requests

def load_lottieurl(url: str):
    # https://github.com/tylerjrichards/streamlit_goodreads_app/blob/master/books.py
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_book = load_lottieurl('https://assets8.lottiefiles.com/packages/lf20_6kbjigp3.json')