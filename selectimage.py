import requests
import geojson
from download import download_image

def select_image(url, key, nw, se, image_type):
    """Downloads an image matching the selected coordinates.
    Args:
        url (str): the source url of the image
        key (str): authorisation key for the website
        nw (lst): Decimal coordinates of the North-West corner
        se (lst): Decimal coordinates of the South_East corner
        image_type (str): The type of image you want to open (visual or analytic)
    Result:
        Tif file containing the downloaded image
    """
    ne = (se[0], nw[1])
    sw = (nw[0], se[1])
    poly = geojson.Polygon([[nw, ne, se, sw, nw]])
    intersects = geojson.dumps(poly)
    params = {"intersects": intersects,}
    r = requests.get(url, params=params, auth=(key, ''))
    r.raise_for_status()
    data = r.json()
    scenes_data = data["features"]
    for scene in scenes_data:
        link = scene["properties"]["data"]["products"][image_type]["full"]
#        download_image(link, key)
    
    r = requests.get(link, stream=True, auth=(key, ''))
    if 'content-disposition' in r.headers:
        local_filename = r.headers['content-disposition'] \
            .split("filename=")[-1].strip("'\"")
    else:
        local_filename = '.'.join(link.split('/')[-2:])

    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
    return local_filename