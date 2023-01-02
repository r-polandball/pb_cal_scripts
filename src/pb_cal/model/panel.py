import datetime
from enum import Enum

class Day_Panel:

    '''
    Inputs:
    - date - a datetime timestamp of the date depicted
    - description - a string describing the event depicted
    - creators - list, reddit username(s) of the panel creator(s) (without "u/")
    - image_url - string, imgur URL of the actual panel image
    - reference_lnk - (only required for CAL 2023) string, URL to any website, describes what the event is
    - long_description - (optional) string, a long blob of text describing the panel
    '''
    def __init__(self, date, description, creators, image_url, reference_link=None, long_description=None):
        if isinstance(date, datetime.date):
            self.date = date
        else:
            raise ValueError("date must be a valid datetime.date object")

        if isinstance(description, str):
            self.description = description
        else:
            raise ValueError("description must be a valid string")

        if isinstance(creators, list) and not usernames_have_u_slash(creators):
            self.creators = creators
        else:
            raise ValueError("creator must be a valid string")

        if isinstance(image_url, str):
            self.image_url = image_url
        else:
            # Techcnically we only checked if it's a valid string, not a valid URL
            # Buuuut again, this is already overkill for such a simple and stupid script...
            raise ValueError("image_url must be a valid URL")

        if isinstance(reference_link, str) or reference_link == None:
            self.reference_link = reference_link
        else:
            # Techcnically we only checked if it's a valid string, not a valid URL
            # Buuuut again, this is already overkill for such a simple and stupid script...
            raise ValueError("reference_link must be a valid URL")

        if isinstance(long_description, str) or long_description == None:
            self.long_description = long_description
        else:
            raise ValueError("long_description must be a valid string")

        return None


    def to_dict(self):
        return {
            "date": self.date,
            "description": self.description,
            "creator(s)": ';'.join(self.creators),
            "image_url": self.image_url,
            "reference_link": self.reference_link,
            "long_description": self.long_description,
        }


class Month_Panel:

    '''
    Inputs:
    - month_panel_name - one of the values from the Month_Panel_Names enum
    - description - an optional string describing the monthly panel. can be None if omitted
    - creators - list, reddit username(s) of the panel creator(s) (without "u/")
    - image_url - string, imgur URL of the actual panel image
    '''
    def __init__(self, month_panel_name, description, creators, image_url):
        self.month_panel_name = month_panel_name
        self.description = description
        self.creators = creators
        self.image_url = image_url
        return None

    def to_dict(self):
        return {
            "month": self.month_panel_name.name,
            "description": self.description,
            "creator(s)": ';'.join(self.creators),
            "image_url": self.image_url
        }



'''
List of panels to be included in the monthly view spreadsheet.
Note the inclusion of the cover here.
Also note that order of listing does matter, as enums are iterable!
'''
class Month_Panel_Names(Enum):
    COVER = 0
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12



'''
utility functions for checking usernames
'''

def usernames_have_u_slash(usernames):
    for username in usernames:
        if username_has_u_slash(username):
            return True
    return False

def username_has_u_slash(username):
    return len(username.split("u/")) > 1


'''
utility function for removing "u/" from usernames
'''
def strip_u_slash(username):
    return username.split("u/")[-1]

