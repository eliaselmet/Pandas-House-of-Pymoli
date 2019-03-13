#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), '..\NUCHI201902DATA1\Homework\04-Pandas\Instructions\HeroesOfPymoli'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# ### Heroes Of Pymoli Data Analysis
# * Of the 1163 active players, the vast majority are male (84%). There also exists, a smaller, but notable proportion of female players (14%).
# 
# * Our peak age demographic falls between 20-24 (44.8%) with secondary groups falling between 15-19 (18.60%) and 25-29 (13.4%).  
# -----
#%% [markdown]
# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

#%%
# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)
purchase_data.head()

#%% [markdown]
# ## Player Count
#%% [markdown]
# * Display the total number of players
# 

#%%
player_count = purchase_data["SN"].unique()
len(player_count)

#%% [markdown]
# ## Purchasing Analysis (Total)
#%% [markdown]
# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

#%%
unique_items = purchase_data["Item Name"].unique()
unique_items_count = len(unique_items)
average_price = round(purchase_data["Price"].mean(),2)
number_purchases = len(purchase_data["Purchase ID"])
total_revenue = purchase_data["Price"].sum()

purchasing_analysis = {"Unique Items": unique_items_count, 
                       "Average Price": average_price, 
                       "Number of Purchases": number_purchases, 
                       "Total Revenue":total_revenue}


pd.DataFrame([purchasing_analysis])

#%% [markdown]
# ## Gender Demographics
#%% [markdown]
# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

#%%
purchases_unique = purchase_data.drop_duplicates(["Gender", "SN"])

count = purchases_unique["Gender"].value_counts()
percentage = round(100*count/len(player_count),2)

gender_summary = pd.DataFrame({"Total Count": count, "Percentage": percentage})

gender_summary

#%% [markdown]
# 
# ## Purchasing Analysis (Gender)
#%% [markdown]
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

#%%
purchase_by_gender = purchase_data.groupby(["Gender"])
total_by_gender = purchase_by_gender["Price"].sum()
purchase_count = purchase_data["Gender"].value_counts()
avg_purchase = round(total_by_gender / purchase_count,2)
avg_purchase_per_person = round(total_by_gender/count,2)

purchase_summary_gender = pd.DataFrame({"Purchase Count": purchase_count,
                                        "Avg Purchase Price": avg_purchase, 
                                        "Avg Purchase Total Per Person": avg_purchase_per_person,
                                        "Total Purchase Value": total_by_gender})

purchase_summary_gender

#%% [markdown]
# ## Age Demographics
#%% [markdown]
# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

#%%
bins = [0,9,14,19,24,29,34,39,100]

bin_labels = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

purchases_unique["Age Bin"] = pd.cut(purchases_unique["Age"],bins, labels = bin_labels)

bin_counts = purchases_unique["Age Bin"].value_counts()
bin_percent = round(bin_counts/ len(player_count),2)

age_demographics = pd.DataFrame({"Bin Count": bin_counts, 
                                "Percent": bin_percent})

age_demographics
#purchase_data.groupby(["Age Bin"])

#purchase_data.head()

#%% [markdown]
# ## Purchasing Analysis (Age)
#%% [markdown]
# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

#%%
purchase_count = purchase_data["Age Bin"].value_counts()

unique_purchases_by_bin = purchases_unique["Age Bin"].value_counts()

total_purchase_value = round(purchases_by_bin["Price"].sum(),2)

avg_purchase_price = round(total_purchase_value/purchase_count,2)

avg_total_purchase_person = round(total_purchase_value / unique_purchases_by_bin,2)

purchase_analysis_age = pd.DataFrame({"Purchase Count": purchase_count, "Average Purchase Price": avg_purchase_price,"Total Purchase Value": total_purchase_value,"Avg Total Purchase Per Person": avg_total_purchase_person})

purchase_analysis_age

#%% [markdown]
# ## Top Spenders
#%% [markdown]
# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

#%%
total_purchases = purchase_data["SN"].value_counts()

purchase_by_sn = purchase_data.groupby(["SN"])

purchase_sum = purchase_by_sn["Price"].sum()

avg_purchase = purchase_sum/total_purchases

top_spenders = pd.DataFrame({"Purchase Count": total_purchases,
                            "Avg Purchase Price": avg_purchase,
                            "Total Purchase Value": purchase_sum})

top_spenders = top_spenders.sort_values('Total Purchase Value', ascending=False)
top_spenders['Avg Purchase Price'] = top_spenders['Avg Purchase Price'].map("${:,.2f}".format)
top_spenders['Total Purchase Value'] = top_spenders['Total Purchase Value'].map("${:,.2f}".format)   
    
top_spenders.head()

#%% [markdown]
# ## Most Popular Items
#%% [markdown]
# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

#%%
#purchase_count = purchase_data["Item Name"].value_counts()

groupby_item_id = purchase_data.groupby(["Item Name","Item ID"])

purchase_count = groupby_item_id["Price"].count()
item_sum = groupby_item_id["Price"].sum()
item_price = groupby_item_id["Price"].mean()

popular_items = pd.DataFrame({"Purchase Sum": item_sum, "Item Price": item_price,
                            "Purchase Count": purchase_count})


popular_items = popular_items.sort_values('Purchase Count', ascending=False)
popular_items['Purchase Sum'] = popular_items['Purchase Sum'].map("${:,.2f}".format)
popular_items['Item Price'] = popular_items['Item Price'].map("${:,.2f}".format)

popular_items.head()

#%% [markdown]
# ## Most Profitable Items
#%% [markdown]
# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

#%%
groupby_item_id = purchase_data.groupby(["Item Name","Item ID"])

purchase_count = groupby_item_id["Price"].count()
item_sum = groupby_item_id["Price"].sum()
item_price = groupby_item_id["Price"].mean()

popular_items = pd.DataFrame({"Purchase Sum": item_sum, "Item Price": item_price,
                            "Purchase Count": purchase_count})


popular_items = popular_items.sort_values('Purchase Sum', ascending=False)
popular_items['Purchase Sum'] = popular_items['Purchase Sum'].map("${:,.2f}".format)
popular_items['Item Price'] = popular_items['Item Price'].map("${:,.2f}".format)

popular_items.head()


