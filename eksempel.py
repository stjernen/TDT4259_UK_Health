import pandas as pd
from matplotlib import pyplot as plt

targetCategory = "Fresh and processed fruit and vegetables, including potatoes"

df = pd.read_csv("test_decile1.csv", sep=";")
index = 1
for i in range(len(df["Food Category"])):
    if df["Food Category"][i] == targetCategory:
        index = i
 
x = df.keys()[6:24]
foodCategory = df["Food Category"][index]
units = df["Units"][index]
 
y = []
 
for key in x:
    y.append(df[key][index])
 
plt.title(foodCategory)
plt.xlabel("Year")
plt.ylabel(units)
plt.plot(x, y)
plt.show()
