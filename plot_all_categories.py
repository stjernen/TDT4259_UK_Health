import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("./data/food_data/decile1_fixed.csv", sep=";")
df2 = pd.read_csv("./data/food_data/decile5_fixed.csv", sep=";")
df3 = pd.read_csv("./data/food_data/decile10_fixed.csv", sep=";")

all_categories_not_null = df["Food Category"][df["Food Category"].notnull()].tolist()

for category in all_categories_not_null:
    targetCategory = category

    index = 1
    for i in range(len(df["Food Category"])):
        if df["Food Category"][i] == targetCategory:
            index = i

    x = df.keys()[2:24]
    foodCategory = df["Food Category"][index]
    units = df["Units"][index]
    
    y = []
    y2 = []
    y3 = []
    
    for key in x:
        y.append(df[key][index])
        y2.append(df2[key][index])
        y3.append(df3[key][index])
    
    plt.figure()
    plt.title(foodCategory)
    plt.xlabel("Year")
    plt.ylabel(units)
    plt.plot(x, y, color='#31454A', label = "Decile 1")
    plt.plot(x, y2, color='#D3AD8D', label = "Decile 5")
    plt.plot(x, y3, color='#C6796C', label = "Decile 10")
    plt.legend()
    plt.savefig(f"./plots/foodplots/{foodCategory}.png", dpi=300)
    print(f"saved plot for {foodCategory}")
    #plt.show()
    plt.close()

print("done")