import pandas as pd

east_midlands = pd.read_csv("East Midlands.csv")
eastern = pd.read_csv("Eastern.csv")
london = pd.read_csv("London.csv")
north_east = pd.read_csv("North East.csv")
north_west = pd.read_csv("North West.csv")
northern_ireland = pd.read_csv("Northern Ireland.csv")
scotland = pd.read_csv("Scotland.csv")
south_east = pd.read_csv("South East.csv")
wales = pd.read_csv("Wales.csv")
west_midlands = pd.read_csv("West Midlands.csv")
yorkshire = pd.read_csv("Yorkshire.csv")

list = [east_midlands, eastern, london, north_east, north_west, northern_ireland, scotland, south_east, wales, west_midlands, yorkshire]

for area in list:
    bottom = area["Bottom"]
    middle = area["5th"]
    top = area["Top"]
    
    for year in years:
        print(year)

#resultData.to_csv('result.csv')