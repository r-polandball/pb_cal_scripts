import pandas

from pb_cal.model.year.cal_2019 import *
from pb_cal.model.year.cal_2020 import *
from pb_cal.model.year.cal_2021 import *
from pb_cal.model.year.cal_2022 import *



# Utility functions


def write_csv_files(cal):
    if cal.daily_panels:
        daily_panels = to_dataframe(cal.daily_panels)
        daily_panels.to_csv('./data/' + str(cal.year) + '_daily.csv', index=False)

    if cal.monthly_panels:
        monthly_panels = to_dataframe(cal.monthly_panels)
        monthly_panels.to_csv('./data/' + str(cal.year) + '_monthly.csv', index=False)


def to_dataframe(panel_list):
    panel_dicts = []
    for panel in panel_list:
        panel_dicts.append(panel.to_dict())

    return pandas.DataFrame(panel_dicts)




# Actual main execution of fetching cal data
if __name__ == "__main__":

    cal_2019 = Cal_2019()
    write_csv_files(cal_2019)

    cal_2020 = Cal_2020()
    write_csv_files(cal_2020)

    cal_2021 = Cal_2021()
    write_csv_files(cal_2021)

    cal_2022 = Cal_2022()
    write_csv_files(cal_2022)
