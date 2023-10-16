import os
import pandas as pd

income_csv_dir = "./income_csv"
areas = {}
for filename in os.listdir(income_csv_dir):
    if filename.endswith(".csv"):
        area_name = os.path.splitext(filename)[0]
        area_data = pd.read_csv(os.path.join(income_csv_dir, filename))
        areas[area_name] = area_data


def csv_string_to_int(input):
    return int(input.replace("\xa0", "")) # <-- noe mac greier

avg_df_list = []


#get a list of all the years


# 1 dataframe med total gjennomsnitt for alle områder per år

# fra 2001 til 2019
# gjennomsnit for decil 1 på alle områder per år
# gjennomsnit for decil 5 på alle områder per år
# gjennomsnit for decil 10 på alle områder per år

bottom_df = pd.DataFrame(columns=["Year", "Bottom decile"])
total_df = pd.DataFrame(columns=["Year", "Bottom decile", "Middle decile", "Top decile"])

years = areas["Yorkshire"]["Year3"].tolist() # all years are the same for all areas and same length

for year in range(years):
    bottom_decile_sum = 0
    middle_decile_sum = 0
    top_decile_sum = 0
    for area_name, area_data in areas.items():
        bottom_decile_sum += csv_string_to_int(area_data["Bottom"][year])
        middle_decile_sum += csv_string_to_int(area_data["Middle"][year])
        top_decile_sum += csv_string_to_int(area_data["Top"][year])



#if(area_name == "Yorkshire"): print(area_data["Bottom"])
#area_data["Bottom"] = area_data["Bottom"].apply(csv_string_to_int)
