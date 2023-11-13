import os
import pandas as pd
import matplotlib.pyplot as plt
import tabulate as tab

#get data from csv files
income_csv_dir = "./data/income_csv"
areas = {}
for filename in os.listdir(income_csv_dir):
    if filename.endswith(".csv"):
        area_name = os.path.splitext(filename)[0]
        area_data = pd.read_csv(os.path.join(income_csv_dir, filename))
        areas[area_name] = area_data


def csv_string_to_int(input):
    return int(input.replace("\xa0", "")) # <-- mac ting

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
        bottom_decile_sum += csv_string_to_int(area_data[BOTTOM][year])
        middle_decile_sum += csv_string_to_int(area_data[MIDDLE][year])
        top_decile_sum += csv_string_to_int(area_data[TOP][year])
    
    bottom_avg_this_year = bottom_decile_sum / num_areas
    middle_avg_this_year = middle_decile_sum / num_areas
    top_avg_this_year = top_decile_sum / num_areas
    
    result_df = result_df.append({"Year": years[year], "Bottom decile": bottom_avg_this_year, "Middle decile": middle_avg_this_year, "Top decile": top_avg_this_year}, ignore_index=True)

# line chart visualisation
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