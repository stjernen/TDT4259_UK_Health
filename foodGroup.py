import pandas as pd
from matplotlib import pyplot as plt

targetGroups = ["Processed vegetables excluding processed potatoes", "Processed fruit and fruit products"]

df = pd.read_csv("./data/food_data/decile1_FoodGroup.csv", sep=";")
df2 = pd.read_csv("./data/food_data/decile5_FoodGroup.csv", sep=";")
df3 = pd.read_csv("./data/food_data/decile10_FoodGroup.csv", sep=";")

indexes = [-1, -1, -1]
for i in range(len(df["Food Group"])):
    for n in range(len(targetGroups)):
        if df["Food Group"][i] == targetGroups[n]:
            indexes[n] = i
 
x = df.keys()[2:21]
units = df["Units"][indexes[0]]
 
y = []
y2 = []
y3 = []
 
for key in x:
    tmpy = 0
    tmpy2 = 0
    tmpy3 = 0
    for i in range(len(targetGroups)):
        tmpy += df[key][indexes[i]]
        tmpy2 += df2[key][indexes[i]]
        tmpy3 += df3[key][indexes[i]]
    y.append(tmpy)
    y2.append(tmpy2)
    y3.append(tmpy3)

plt.title("Processed vegetables and fruit")
plt.xlabel("Year")
plt.ylabel(units)
plt.plot(x, y, color = "#31454A", label = "Decile 1")
plt.plot(x, y2, color = "#D3AD8D", label = "Decile 5")
plt.plot(x, y3, color = "#C6796C", label = "Decile 10")
plt.legend()
plt.show()