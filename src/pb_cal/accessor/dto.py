'''
Data Transfer Objects (DTOs) for the sake of transferring data within this script package
Basically we want this so that there's a level of abstraction between internal data representation and the Imgur API
That means we only have to make changes in one place if the Imgur API ever changes its signature
'''

class Imgur_Image:

    '''
    Takes in:
    - caption - a string representing the caption for the image in Imgur
    - link - a link to the actual image. Should be a url in the form "https://i.imgur.com/<imgur image ID>.<filetype>"
    '''
    def __init__(self, caption, image_link):
        self.caption = caption
        self.image_link = image_link
