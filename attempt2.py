import os
import pandas as pd
import matplotlib.pyplot as plt
import tabulate as tab

result_df = pd.DataFrame(columns=["Year", "Bottom decile", "Middle decile", "Top decile"])

# excel ark hentet fra:
# https://www.ons.gov.uk/peoplepopulationandcommunity/personalandhouseholdfinances/incomeandwealth/datasets/theeffectsoftaxesandbenefitsonhouseholdincomefinancialyearending2014

excel_dir = "./income_excel_sheets"
sheets = {}
for filename in os.listdir(excel_dir):
    
    if filename.endswith(".xlsx") or filename.endswith(".xls"):
        sheet_name = os.path.splitext(filename)[0]
        sheet_data = None
        
        # selvfølgelig er det ikke samme ark hvert år, takk UK gov
        filesWith14 = ['2003to2004','2005to2006','2008to2009', '2009to2010', '2010to2011', '2011to2012', '2012to2013', '2013to2014']
        filesWith2a = ['2014to2015', '2015to2016', '2016to2017', '2017to2018', '2018to2019']
        filesWith2b = ['2019to2020', '2020to2021', '2021to2022']
        
        isTable2b = sheet_name in filesWith2b

        BOTTOM = 1 if not isTable2b else 2
        MIDDLE = 5 if not isTable2b else 6
        TOP =    10 if not isTable2b else 11

        sheet_with_deciles = None

        if sheet_name == '2005to2006': sheet_with_deciles = 'Table14' # UK gov typo
        elif sheet_name in filesWith14: sheet_with_deciles = 'Table 14'
        elif sheet_name in filesWith2a: sheet_with_deciles = 'Table 2a'
        elif sheet_name in filesWith2b: sheet_with_deciles = 'Table 2b'
        else: print("error: " + sheet_name)
        
        try:
            sheet_data = pd.read_excel(os.path.join(excel_dir, filename), sheet_name = sheet_with_deciles)
        except Exception as e:
            print(e)
            print(f"error reading sheet {sheet_with_deciles} in file {sheet_name}")
            continue

        row_index = (sheet_data.iloc[:, 0] == 'Gross income').idxmax()
        final_income = sheet_data.iloc[row_index]
        sheet_year = sheet_name.replace('to', '/')
        result_df = result_df.append({"Year": sheet_year, "Bottom decile": final_income[BOTTOM], "Middle decile": final_income[MIDDLE], "Top decile": final_income[TOP]}, ignore_index=True)

#print(result_df)


#simple line chart visualisation
plt.figure(figsize=(10,7))

# Plot the lines
plt.plot(result_df["Year"], result_df["Top decile"], color='#C6796C', label="Top decile")
plt.plot(result_df["Year"], result_df["Middle decile"], color='#D3AD8D', label="Middle decile")
plt.plot(result_df["Year"], result_df["Bottom decile"], color='#31454A', label="Bottom decile")

plt.xticks(rotation=45)

# Set the axis labels and title
plt.xlabel("Year")
plt.ylabel("Income")
plt.title("Gross income by Decile")

# Add a legend
plt.legend()

# Show the plot
#plt.show()

# Save the plot
#plt.savefig("gross_income_by_decile.png", dpi=300)

# save the data as a csv
result_df.to_csv('gross_income_by_decile.csv')