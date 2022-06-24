import pandas as pd
import seaborn as sns

#data = pd.read_csv("40165.csv")
df = pd.read_csv("D:\\_MyPython\\Indices_of_farm_output.csv")

total_Agri_Out = df[(df["Attribute"] == "Total agricultural output")]
#print(df)
print(total_Agri_Out)

sns.scatterplot(x=total_Agri_Out['Year'],
                y=total_Agri_Out['Value'])