import pb_cal.model.calendar as calendar
import pb_cal.model.panel as panel

# Reddit post: https://www.reddit.com/r/polandball/comments/kjxz7b/the_official_polandball_2021_calendar/
class Cal_2021(calendar.Calendar):

    def __init__(self):
        # Call Calendar class constructor
        super().__init__(
            2021,
            # Daily album
            "https://imgur.com/a/d7xEONX",
            # Monthly album
            None
        )

    '''
    Given an Imgur_Image object, determine whether or not the panel depicts a Day or not
    '''
    def is_daily_panel(self, imgur_image):
        # Everything in this album except the cover is a daily panel
        return len(imgur_image.caption.split('\n')) > 1 and (not "The /r/Polandball 2021 Daily Calendar" in imgur_image.caption)


    '''
    Given an Imgur_Image object and a Datetime Date, return a Day_Panel
    Note that this does NOT check if the Imgur_Image is a daily panel - be sure to call __is_daily_panel before using this!
    '''
    def to_daily_panel(self, imgur_image, datetime_date):
        # Get the part before "By" and then replace all whitespace (such as newlines) with a single space
        description = imgur_image.caption.split("Created by ")[0].strip()
        description = ' '.join(description.split())

        # Get the creator or list of creators (some have multiple creators)
        creator_text = imgur_image.caption.split("Created by ")[-1].strip()
        creator_list = creator_text.split(',')
        for i in range(0, len(creator_list)):
            creator_list[i] = creator_list[i].split("u/")[-1]

        return panel.Day_Panel(datetime_date, description, creator_list, imgur_image.image_link)


    '''
    Given an Imgur_Image object, determine whether or not the panel depicts a Month or not
    '''
    def is_monthly_panel(self, imgur_image):
        # There is no monthly album for this year - it's on the reddit post
        return False


    '''
    Given an Imgur_Image object and a Monthly_Panel_Name, return a Month_Panel
    Note that this does NOT check if the Imgur_Image is a monthly panel - be sure to call __is_monthly_panel before using this!
    '''
    def to_monthly_panel(self, imgur_image, monthly_panel_name):
        # There is no monthly album for this year - it's on the reddit post
        return None
