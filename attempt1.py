import os
import pandas as pd
import matplotlib.pyplot as plt
import tabulate as tab

#get data from csv files
income_csv_dir = "./income_csv"
areas = {}
for filename in os.listdir(income_csv_dir):
    if filename.endswith(".csv"):
        area_name = os.path.splitext(filename)[0]
        area_data = pd.read_csv(os.path.join(income_csv_dir, filename))
        areas[area_name] = area_data


def csv_string_to_int(input):
    return int(input.replace("\xa0", "")) # <-- noe mac greier

# fra 2001 til 2019 (17?)
# gjennomsnit for decil 1 på alle områder per år
# gjennomsnit for decil 5 på alle områder per år
# gjennomsnit for decil 10 på alle områder per år

BOTTOM = "Bottom"
MIDDLE = "5th"
TOP = "Top"

years = areas["Yorkshire"]["Year3"].tolist() # all years are the same for all areas and same length

num_areas = len(areas)

result_df = pd.DataFrame(columns=["Year", "Bottom decile", "Middle decile", "Top decile"])

for year in range(len(years)):
    bottom_decile_sum = 0
    middle_decile_sum = 0
    top_decile_sum = 0
    for area_name, area_data in areas.items():
        #print(f"{area_name} | {area_data[BOTTOM][year]}")
        #print(tab.tabulate([[area_name, area_data[BOTTOM][year]]], tablefmt="grid"))
        bottom_decile_sum += csv_string_to_int(area_data[BOTTOM][year])
        middle_decile_sum += csv_string_to_int(area_data[MIDDLE][year])
        top_decile_sum += csv_string_to_int(area_data[TOP][year])
        #print(f"in area {area_name} for year {year}, bottom decile is {bottom_decile_sum}, middle decile is {middle_decile_sum}, top decile is {top_decile_sum}")
    
    bottom_avg_this_year = bottom_decile_sum / num_areas
    middle_avg_this_year = middle_decile_sum / num_areas
    top_avg_this_year = top_decile_sum / num_areas
    #print(f"area: bottom avg this year is {bottom_avg_this_year}, middle avg this year is {middle_avg_this_year}, top avg this year is {top_avg_this_year}")
    #year_cleaned = years[year].split('/')[0]
    
    result_df = result_df.append({"Year": years[year], "Bottom decile": bottom_avg_this_year, "Middle decile": middle_avg_this_year, "Top decile": top_avg_this_year}, ignore_index=True)

#hardcoded data for 2018-19
#data2018_19 = [5_473, 26_254, 119_902]
#result_df = result_df.append({"Year": "2018/19", "Bottom decile": data2018_19[0], "Middle decile": data2018_19[1], "Top decile": data2018_19[2]}, ignore_index=True)

#print(result_df)

#simple line chart visualisation
plt.figure(figsize=(10,6))

# Plot the lines
plt.plot(result_df["Year"], result_df["Bottom decile"], label="Bottom decile")
plt.plot(result_df["Year"], result_df["Middle decile"], label="Middle decile")
plt.plot(result_df["Year"], result_df["Top decile"], label="Top decile")

plt.xticks(rotation=45)

# Set the axis labels and title
plt.xlabel("Year")
plt.ylabel("Income")
plt.title("Income by Decile (based on avg of all areas)")

# Add a legend
plt.legend()

# Show the plot
plt.show()