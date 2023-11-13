import pandas as pd
from matplotlib import pyplot as plt

targetCategory = "Fish"

df = pd.read_csv("decile1_FoodCategory.csv", sep=";")
df2 = pd.read_csv("decile5_FoodCategory.csv", sep=";")
df3 = pd.read_csv("decile10_FoodCategory.csv", sep=";")

index = 1
for i in range(len(df["Food Category"])):
    if df["Food Category"][i] == targetCategory:
        index = i
 
x = df.keys()[2:21]
foodCategory = df["Food Category"][index]
units = df["Units"][index]
 
y = []
y2 = []
y3 = []
 
for key in x:
    #print(df3)
    print(key)
    y.append(df[key][index])
    y2.append(df2[key][index])
    y3.append(df3[key][index])

plt.title(foodCategory)
plt.xlabel("Year")
plt.ylabel(units)
plt.plot(x, y, color = "#31454A", label = "Decile 1")
plt.plot(x, y2, color = "#D3AD8D", label = "Decile 5")
plt.plot(x, y3, color = "#C6796C", label = "Decile 10")
plt.legend()
plt.show()