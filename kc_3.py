#!/usr/bin/env python
# coding: utf-8

# In[101]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Get Indices of total farm output, data from 1948 - 2019
    df = pd.read_csv("Indices_of_farm_output.csv")
    print()
    print()
    get_egg_difference(df)
    print()
    print()
    get_eggs_average(df)
    print()
    print()
    get_eggs_total(df)
    print()
    print()
    print()
    get_total(df)
    print()
    print()
    side_by_side_plots()
    #get_total(df)

def get_eggs_total(df):
    # Get Indices of total egg output, data from 1948 - 2019
    poultry_eggs = df[(df["Attribute"] == "Livestock and products output: Poultry and eggs")]
    #avg_value = round(df.Value.mean(),0)
    print(poultry_eggs)
    print()
    plt.xlabel('Yearly change', size=16)
    plt.ylabel('Farm output value', size=16)
    plt.title(f'The avg. egg production 1948 - 2019 is: {avg_value}', size=18)
    #print(f"The average value of egg production from 1948 - 2019 is: {avg_value}")
    sns.scatterplot(x=total_Agri_Out['Year'],
            y=total_Agri_Out['Value'])
    return plt.show()

def get_eggs_average(df):
    poultry_eggs = df[(df["Attribute"] == "Livestock and products output: Poultry and eggs")]
    avg_value = round(df.Value.mean(),0)
    return print(f"The average value of egg production from 1948 - 2019 is: {avg_value}")

def get_egg_difference(df):
    poultry_eggs = df[(df["Attribute"] == "Livestock and products output: Poultry and eggs")]
    poultry_eggs = poultry_eggs.reset_index(drop=True)
    #select_start = df.loc[df['Year'] == '1948']
    #select_end = df.loc[df['Year'] == '2019']
    onerow = poultry_eggs[poultry_eggs['Year'] == '1948']
    beg = poultry_eggs.iloc[0]
    end = poultry_eggs.iloc[70]
    data = (beg, end )
    
    df_year = pd.DataFrame(data)
    df_year = df_year.reset_index(drop=True)
    #Add new column with difference
    df_year['ProdDiff'] = df_year['Value'].diff()
    
    return print(df_year)

def get_total(df):
    df.head()
    print(df)

    sns.scatterplot(x=df['Year'],
                    y=df['Value'])
    return plt.show

def side_by_side_plots():
    # Create figure and multiple plots
    fig, axes = plt.subplots(nrows=1, ncols=2)

    # Auto adjust
    plt.tight_layout()

    # Display
    return plt.show()
    
main()


# In[ ]:





# In[ ]:




