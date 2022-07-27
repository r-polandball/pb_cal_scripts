import datetime
import dateutil.parser

import pb_cal.accessor.imgur as imgur
import pb_cal.model.panel as panel

class Calendar:
    monthly_panels = None

    '''
    Inputs:
    year = number like "2020" representing the year depicted by the calendar
    daily_album_link = URL in the form of "https://imgur.com/a/<imgur_album_id>" - or None if not relevant
    monthly_album_link = URL in the form of "https://imgur.com/a/<imgur_album_id>" - or None if not relevant
    '''
    def __init__(self, year, daily_album_link, monthly_album_link):
        if isinstance(year, int) and year > 0:
            self.year = year
            self.__first_day = dateutil.parser.parse("January 1st, " + str(self.year))
        else:
            raise ValueError("Year must be a positive integer")

        if isinstance(daily_album_link, str):
            self.daily_album_id = daily_album_link.split('/')[-1]
        elif daily_album_link == None:
            self.daily_album_id = None
        else:
            # Well really it must be a valid URL but ngl this is already overkill for a simple little script
            raise ValueError("Daily album link must be a string")

        if isinstance(monthly_album_link, str):
            self.monthly_album_id = monthly_album_link.split('/')[-1]
        elif monthly_album_link == None:
            self.monthly_album_id =  None
        else:
            # Well really it must be a valid URL but ngl this is already overkill for a simple little script
            raise ValueError("Monthly album link must be a string")

        # Initialize panel data based on imgur data

        if self.daily_album_id:
            self.__fetch_daily_panels()
        else:
            print("You must enter the daily panel data for " + str(self.year) + " manually")

        if self.monthly_album_id:
            self.__fetch_monthly_panels()
        else:
            print("You must enter the monthly panel data for " + str(self.year) + " manually")


    '''
    Private method to fetch daily album data from Imgur, and store it as Day_Panel objects
    Assumes that each day is in chronological order in the Imgur data
    '''
    def __fetch_daily_panels(self):
        self.daily_panels = []

        # Get the raw daily album, which might contain irrelevant images (eg. monthly panels)
        daily_album_raw = imgur.get_album_images(self.daily_album_id)

        # Filter so we only get the daily images
        # We keep track of how many days we have seen so far so we know which date each panel depicts
        current_day = 0
        for image in daily_album_raw:
            if self.is_daily_panel(image):
                # Get which date the panel depicts
                current_date = self.__first_day + datetime.timedelta(days=current_day)

                # Store the current panel as a Day_Panel object
                day_panel = self.to_daily_panel(image, current_date)
                self.daily_panels.append(day_panel)

                # Increment which day we're on now
                current_day += 1

        # Sanity check
        # 366 is for leap years
        if not (current_day == 365 or current_day == 366):
            raise ValueError("Hmmm.... why are there " + str(current_day) + " day panels in this calendar?")
        return None


    '''
    Private method to fetch monthly album data from Imgur, and store it as Month_Panel objects
    Assumes each month is in chrological order (and the cover is the first image) in the Imgur data

    Optionally can pre-initialize monthly panels variable for albums that aren't stored in a typical way
    '''
    def __fetch_monthly_panels(self):
        if self.monthly_panels == None:
            self.monthly_panels = []

        # Get the raw monthly album, which might contain irrelevant images (eg. daily panels)
        monthly_album_raw = imgur.get_album_images(self.monthly_album_id)

        # Filter so we only get the monthly images
        current_month = len(self.monthly_panels)
        for image in monthly_album_raw:
            if self.is_monthly_panel(image):
                # Get which month the panel depicts
                current_month_name = panel.Month_Panel_Names(current_month)

                # Store the current month as a Month_Panel object
                month_panel = self.to_monthly_panel(image, current_month_name)
                self.monthly_panels.append(month_panel)

                # Increment which month we're on now
                current_month += 1

        # Sanity check
        # It's valid to have just a cover OR cover + 12 months
        if not (current_month == 1 or current_month == 13):
            raise ValueError("Hmmm.... why are there " + str(current_month) + " month panels in this calendar?")
        return None


    '''
    Given an Imgur_Image object, determine whether or not the panel depicts a Day or not
    MUST BE IMPLEMENTED BY DERIVED CLASSES FOR EACH YEAR (since every year stores this data differently)
    '''
    def is_daily_panel(self, imgur_image):
        return False


    '''
    Given an Imgur_Image object and a Datetime Date, return a Day_Panel
    Note that this does NOT check if the Imgur_Image is a daily panel - be sure to call __is_daily_panel before using this!
    MUST BE IMPLEMENTED BY DERIVED CLASSES FOR EACH YEAR (since every year stores this data differently)
    '''
    def to_daily_panel(self, imgur_image, datetime_date):
        return None


    '''
    Given an Imgur_Image object, determine whether or not the panel depicts a Month or not
    MUST BE IMPLEMENTED BY DERIVED CLASSES FOR EACH YEAR (since every year stores this data differently)
    '''
    def is_monthly_panel(self, imgur_image):
        return False


    '''
    Given an Imgur_Image object and a Monthly_Panel_Name, return a Month_Panel
    Note that this does NOT check if the Imgur_Image is a monthly panel - be sure to call __is_monthly_panel before using this!
    MUST BE IMPLEMENTED BY DERIVED CLASSES FOR EACH YEAR (since every year stores this data differently)
    '''
    def to_monthly_panel(self, imgur_image, monthly_panel_name):
        return None





