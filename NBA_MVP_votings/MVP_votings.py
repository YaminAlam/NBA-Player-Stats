import warnings
warnings.filterwarnings('ignore')

#Dependencies
import pandas as pd

#load csv
file = "Resources/mvp_votings.csv"
df_mvp = pd.read_csv(file)
df_mvp.head(10)

df_mvp.columns

mvp_points = df_mvp[df_mvp["season"] == "2017-18"][["player","votes_first", "points_won", "points_max", "award_share"]].copy()

mvp_points.rename(columns={"player":"Player", "votes_first":"Votes", "points_won":"Points_won","points_max":"Max_points",
                           "award_share":"Award_share"})