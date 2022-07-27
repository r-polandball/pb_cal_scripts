import pb_cal.model.calendar as calendar
import pb_cal.model.panel as panel

# Reddit post: https://www.reddit.com/r/polandball/comments/effs6h/the_polandball_calendar_2020/
class Cal_2020(calendar.Calendar):

    def __init__(self):
        # Pre-fill Cover panel in monthly panels because it's not part of the monthly album for this year
        cover_panel = panel.Month_Panel(
            panel.Month_Panel_Names.COVER,
            "Cover",
            ["Watmaln"],
            "https://i.imgur.com/WluPgue.png"
        )
        self.monthly_panels = [cover_panel]

        # Call Calendar class constructor
        super().__init__(
            2020,
            # Daily album
            "https://imgur.com/a/4doXh10",
            # Monthly album
            "https://imgur.com/a/E25rtS0"
        )

    '''
    Given an Imgur_Image object, determine whether or not the panel depicts a Day or not
    '''
    def is_daily_panel(self, imgur_image):
        # Everything in this album except the cover is a daily panel
        return len(imgur_image.caption.split('\n')) > 1


    '''
    Given an Imgur_Image object and a Datetime Date, return a Day_Panel
    Note that this does NOT check if the Imgur_Image is a daily panel - be sure to call __is_daily_panel before using this!
    '''
    def to_daily_panel(self, imgur_image, datetime_date):
        # Get the part before "By" and then replace all whitespace (such as newlines) with a single space
        description = imgur_image.caption.split("By")[0].strip()
        description = ' '.join(description.split())

        # Get the creator or list of creators (some have multiple creators)
        creator_text = imgur_image.caption.split("By")[-1].strip()
        creator_list = creator_text.split(',')
        for i in range(0, len(creator_list)):
            creator_list[i] = creator_list[i].split("u/")[-1]

        return panel.Day_Panel(datetime_date, description, creator_list, imgur_image.image_link)


    '''
    Given an Imgur_Image object, determine whether or not the panel depicts a Month or not
    '''
    def is_monthly_panel(self, imgur_image):
        # Everything in this album is a monthly panel
        return True


    '''
    Given an Imgur_Image object and a Monthly_Panel_Name, return a Month_Panel
    Note that this does NOT check if the Imgur_Image is a monthly panel - be sure to call __is_monthly_panel before using this!
    '''
    def to_monthly_panel(self, imgur_image, monthly_panel_name):
        # Get the part before "created by" and then replace all whitespace (such as newlines) with a single space
        description = imgur_image.caption.split(" by")[0].strip()
        description = ' '.join(description.split())

        # Get the creator or list of creators (some have multiple creators)
        creator_text = imgur_image.caption.split(" by")[-1].strip()
        creator_list = creator_text.split(',')
        for i in range(0, len(creator_list)):
            creator_list[i] = creator_list[i].split("u/")[-1]

        return panel.Month_Panel(monthly_panel_name, description, creator_list, imgur_image.image_link)
