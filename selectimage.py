import requests
import geojson
from download import download_image

def select_image(url, key, point, image_type, file_name):
    """Downloads an image matching the selected coordinates.
    Args:
        url (str): the source url of the image
        key (str): authorisation key for the website
        point(lst): Decimal coordinates of the point for which the map should be retrieved
        image_type (str): The type of image you want to open (visual or analytic)
    Result:
        Tif file containing the downloaded image
    """
    nw = point
    se = (point[0]+0.001, point[1]+0.001)
    ne = (se[0], nw[1])
    sw = (nw[0], se[1])
    poly = geojson.Polygon([[nw, ne, se, sw, nw]])
    intersects = geojson.dumps(poly)
    params = {"intersects": intersects,}
    r = requests.get(url, params=params, auth=(key, ''), stream = True)
    r.raise_for_status()
    data = r.json()
    scenes_data = data["features"]
    for scene in scenes_data:
        link = scene["properties"]["data"]["products"][image_type]["full"]
#        download_image(link, key)
    
    r = requests.get(link, stream=True, auth=(key, ''))
    if 'content-disposition' in r.headers:
        local_filename = file_name
#        r.headers['content-disposition'] \
#            .split("filename=")[-1].strip("'\"")
    else:
        local_filename = '.'.join(link.split('/')[-2:])

    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
    return local_filename