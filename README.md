# Polandball Calendar Scripts

These scripts were created to fetch data from previous Polandball CAL projects. Specifically, it fetches:

**Individual daily panels**:

1. Date depicted by calendar panel
2. Event depicted for date
3. Author/creator
4. Direct imgur link to image

**Monthly view**:

1. Month depicted by banner
2. Author/creator of banner
3. Direct imgur link to image

**Calendar cover**:

1. Author/creator of cover
2. Direct imgur link to cover

PLEASE NOTE that you will need to manually enter the data for:

1. Monthly views in some years, as it wasn't worth adding Reddit API integration just for a small handful of data

All of the data for 2019, 2020, 2021, and 2022 is already in this repository, and you do NOT need to rerun the script to fetch that. However, it might be a decent test to rerun the script for these pre-filled years to ensure your local setup works as expected.

## How to run locally

First of all, note that you're probably not going to need to rerun the script for previous years, because it's not like the old data is going to change over time.

But, if you're intending to use these scripts for future CAL projects, you'll probably want to know how to run them to fetch any CAL panels that were generated between the last time this was run, and whenever you run these scripts.

So in *that* case, I recommend running locally for ome of the past years that this script is known to work for (2019, 2020, 2021, 2022)

I'm assuming you're running this on a UNIX-like system, like Linux, or the Ubuntu subsystem for Windows (which is what I used to develop all of this).

### Basic idea of how this works

This script uses the Imgur API to fetch the following data for each daily panel:

1. Event depicted
2. Author/creator
3. Direct link to image
4. The image itself

The actual image itself does not get stored, but it will be input to OpenCV + PyTesseract to automatically read the panel text and determine:

1. Date depicted by the panel

All of the info extracted from above, except for the image itself, will be saved as a `.csv` file (usable like a spreadsheet) in the `data` folder.

Then, for some years, you will be asked to enter the following data manually (it's not automated since there's not enough data to be worth automating):

1. Cover info
2. Monthly banner info

### Set up secrets

#### Create `.env` file to store local secrets

Copy the `.env_TEMPLATE` file to a new file named `.env`. Python will use this to determine values for local environment variables (including API keys).

(For your safety, the `.env` file is in the `.gitignore` so you don't accidentally publish it on Github.)

#### Generate API credentials for Imgur

Because this script fetches data from the Imgur API, you need to create an Imgur API key to use it:

1. Log in to Imgur (yes, you must have an Imgur account for this)
2. Go to the [Imgur API registration portal](https://api.imgur.com/oauth2/addclient)
3. Enter whatever application name you want - it'll show up in [your account settings](https://imgur.com/account/settings/apps) by this name later, so make it something sensible so you remember what this is
4. Choose "Anonymous usage without user authorization" - you don't need user logins for this script
5. Put some random URL in "Authorization callback URL" - this field isn't relevant for this project, but is required to register with Imgur; you can also change this later if you want

After this, Imgur will show you a `Client ID` and `Client Secret` - this is what you need to save.

#### Save API credentials

In the `.env` file you created:

1. Set the `IMGUR_CLIENT_ID` equal to the `Client ID` you just got from Imgur
2. Set the `IMGUR_CLIENT_SECRET` equal to the `Client Secret` you just got from Imgur

### Set up local environment

Now that your secrets are set up, you need to make sure you have all the dependencies you need.

```sh
# Set up resources for virtual python environment (so you don't override local package installations)
python3 -m venv ./venv

# Start running virtual environment
# To deactivate this later, simply type "deactivate"
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Run the code!

```sh
# This is assuming you are in the root directory of the repo - aka the same directory containing this README file
python3 src/fetch_cal_panels.py
```

### Oh noes! It failed!

If your test run on old data seems to have failed, first check that you:

1. Set up your local secrets correctly
    - if not, please re-read the "Set up local environment" section of this README
2. Are running within the Python virtual environment
    - if not, run `source venv/bin/activate` from the root directory of this repo (should be called `pb_cal_bot`)
3. Installed the requirements in your Python virtual environment
    - if not, run `pip install -r requirements.txt` from the root directory of this repo

If those seem to be set up properly, and you're getting some kind of error from Imgur, then, unfortunately, you'll probably need to [check the Imgur API documentation](https://apidocs.imgur.com/#intro) and read the code (oh, the horror) to see if the API has changed since the code was last updated. And make code changes accordingly.

## Updating the script for future years

There are a couple of assumptions made in the basic code itself:

1. We're using [the same 800 x 800px calendar panel template we've used since 2019](https://imgur.com/lVGwa1h) - and the bottom part of that contains text about what day is depicted
2. The calendar panels are hosted as an Imgur album
3. The Imgur API is the same as it was at the time the code was written
4. Each calendar imgur album has explanatory text about what event is depicted, and who made the panel

Supposing those are still true, then you'll need to do the following for future years:

1. Create a new derived class from `pb_cal.model.calendar` for your new year. Ideally create it in the folder `src/pb_cal/model/year`, and name it `cal_YEAR.py`
2. In this derived class, implement the following methods based on however you formatted the image descriptions in imgur for that cal year:
    - constructor - just call the parent `Calendar` class constructor with the correct arguments
    - `is_daily_panel`
    - `to_daily_panel`
    - `is_monthly_panel`
    - `to_monthly_panel`
3. Create an instance of your new class in `python3 src/fetch_cal_panels.py`, and invoke the `write_csv_files()` method on it, just as it is done with all the other years.

You can check out the other classes in `src/pb_cal/model/year` for example code.

## The posts we are fetching data from

- [2019 Polandball Calendar](https://www.reddit.com/r/polandball/comments/ab6mg7/polandball_calendar_2019/) - the first ever Polandball daily calendar, and brainchild of u/Eesti_Stronk!
    - [2019 Calendar day-by-day imgur album](https://imgur.com/a/N63szEQ) - note: it doesn't seem there was a monthly version with banners for this first calendar
- [2020 Polandball Calendar](https://www.reddit.com/r/polandball/comments/effs6h/the_polandball_calendar_2020/)
    - [2020 Calendar imgur album](https://imgur.com/a/4doXh10) - includes both monthly and daily views
    - [2020 Calendar monthly imgur album](https://imgur.com/a/E25rtS0)
- [2021 Polandball Calendar](https://www.reddit.com/r/polandball/comments/kjxz7b/the_official_polandball_2021_calendar/) - the last community project from u/Eesti_Stronk before he stepped down as mod.
    - [2021 Calendar day-by-day imgur album](https://imgur.com/a/d7xEONX)
    - Monthly version + banners available only on Reddit
- [2022 Polandball Calendar](https://www.reddit.com/r/polandball/comments/rth7ke/the_official_polandball_2022_calendar/) - the first and only calendar project run by u/Diictodom before he stepped down as mod.
    - [2022 Calendar day-by-day imgur album](https://imgur.com/a/m9dGNpP)
    - [2022 Calendar monthly imgur album](https://imgur.com/a/v0qkh2t)

