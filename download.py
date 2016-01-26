import requests

def download_image(url, key):
    """Downloads an image from the internet.
    Args:
        url (str): the source url of the image
        key (str): authorisation key for the website
    Return:
        Shape file containing the image
    """
    r = requests.get(url, stream=True, auth=(key, ''))
    local_filename = in_file

    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()

    return local_filename

