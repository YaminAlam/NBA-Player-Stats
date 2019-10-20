#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sqlalchemy import create_engine


# In[2]:


stats_file = "Raw Data/nba_player_stats.csv"
stats_df = pd.read_csv(stats_file)
stats_df.head()


# In[3]:


stats_df["Player"] = stats_df["Player"].map(lambda name: name.split("\\")[0])
stats_df.head()


# In[4]:


# Create a filtered dataframe from specific columns
top_stats = ["Rk", "Player", "Pos", "Age", "G", "MP", "TS%", "BLK%"]
stats_transformed = stats_df[top_stats].copy()

# Rename the column headers
stats_transformed = stats_transformed.rename(columns={"Rk": "rank",
                                                      "Player": "id",
                                                      "Pos": "position",
                                                      "Age": "age",
                                                      "G": "games",
                                                      "MP": "minutes played",
                                                      "PER": "player efficiency rating",
                                                      "TS%": "true shooting percentange",
                                                      "BLK%": "block percentage"})

# Clean the data by dropping duplicates and setting the index
stats_transformed.drop_duplicates("id", inplace=True)
stats_transformed.set_index("id", inplace=True)

stats_transformed.head()


# In[31]:


stats_transformed.to_csv("NBA_player_stats_final.csv")


# In[5]:


stats_transformed.count()


# In[ ]:




