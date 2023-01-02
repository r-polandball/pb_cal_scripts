import pb_cal.model.calendar as calendar
import pb_cal.model.panel as panel

class Cal_2023(calendar.Calendar):

    def __init__(self):
        # Call Calendar class constructor
        super().__init__(
            2023,
            # Daily album
            "https://imgur.com/a/RNvmVL1",
            # Monthly album
            "https://imgur.com/a/Y5381L2"
        )

    '''
    Given an Imgur_Image object, determine whether or not the panel depicts a Day or not
    '''
    def is_daily_panel(self, imgur_image):
        # Everything in this album except the cover is a daily panel
        return not "Persistence of Calendar" in imgur_image.caption


    '''
    Given an Imgur_Image object and a Datetime Date, return a Day_Panel
    Note that this does NOT check if the Imgur_Image is a daily panel - be sure to call __is_daily_panel before using this!
    '''
    def to_daily_panel(self, imgur_image, datetime_date):
        # Get the part after "Title: " and before "\n"
        description = imgur_image.caption.split("Title: ")[1]
        description = description.split("\n")[0]

        # Get the creator or list of creators (some have multiple creators)
        creator_text = imgur_image.caption.split("Creator: ")[1]
        creator_text = creator_text.split("\n")[0]
        creator_list = creator_text.split(' and ')
        for i in range(0, len(creator_list)):
            creator_list[i] = creator_list[i].split("u/")[-1]

        # Get the reference link
        reference_link = imgur_image.caption.split("Reference: ")[1]
        reference_link = reference_link.split("\n")[0]

        # Get the long description
        long_description = imgur_image.caption.split("Description:")[1].strip()

        return panel.Day_Panel(datetime_date, description, creator_list, imgur_image.image_link, reference_link, long_description)


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
        description = imgur_image.caption.split("Creator: ")[0]
        description = description.split("\n")[0]
        description = ' '.join(description.split())

        # Get the creator or list of creators (some have multiple creators)
        creator_text = imgur_image.caption.split("Creator: ")[1]
        creator_text = creator_text.split("\n")[0]
        creator_list = creator_text.split(' and ')
        for i in range(0, len(creator_list)):
            creator_list[i] = creator_list[i].split("u/")[-1]

        return panel.Month_Panel(monthly_panel_name, description, creator_list, imgur_image.image_link)
