'''
This module fetches an Imgur album and returns a list of Panels (pb_cal.model.panel)

Read the Imgur API docs here: https://apidocs.imgur.com/
'''

import dotenv
import json
import os
import requests
import string as s

import pb_cal.accessor.dto as dto


# =====
# Publicly accessible methods
# =====

'''
For an Imgur album linked at https://imgur.com/a/<album_hash>, fetch the list of images + their metadata from the Imgur API
Returns a Python list of Image DTO objects from the DTO package
'''
def get_album_images(album_hash):
    raw_data = _get_imgur_album_images(album_hash)
    images = []
    for datum in raw_data:
        image = dto.Imgur_Image(datum["description"], datum["link"])
        images.append(image)
    return images


# =====
# Load environment variables (to get the API keys)
# =====

dotenv.load_dotenv()

_IMGUR_CLIENT_ID = os.getenv('IMGUR_CLIENT_ID')
_IMGUR_CLIENT_SECRET = os.getenv('IMGUR_CLIENT_SECRET')


# =====
# API endpoint setup
# =====

_IMGUR_GET_ALBUM_ENDPOINT = s.Template("https://api.imgur.com/3/album/$album_hash")

_IMGUR_UNAUTHED_HEADERS = {
    'Authorization': 'Client-ID ' + _IMGUR_CLIENT_ID
}


# =====
# Helper functions
# (Not intended for access outside of this package)
# =====

'''
For an Imgur album linked at https://imgur.com/a/<album_hash>, fetch album data from the Imgur API
Returns the full JSON response object as a Python dictionary
'''
def _get_imgur_album(album_hash):
    album_endpoint = _IMGUR_GET_ALBUM_ENDPOINT.substitute(album_hash = album_hash)
    response = requests.get(album_endpoint, headers=_IMGUR_UNAUTHED_HEADERS)
    if response.status_code != 200:
        raise ValueError("Imgur response status code: " + response.status_code)
    return json.loads(response.text)

'''
For an Imgur album linked at https://imgur.com/a/<album_hash>, fetch the list of images + their metadata from the Imgur API
Returns a Python list of image data (stored as dictionaries based on the Imgur API JSON response object)
'''
def _get_imgur_album_images(album_hash):
    return _get_imgur_album(album_hash)["data"]["images"]
