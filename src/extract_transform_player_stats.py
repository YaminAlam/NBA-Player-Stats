import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd



csv_file = '../Raw Data/player_measurements.csv'
player_measure = pd.read_csv(csv_file)

#filter the year end to 2018 as this seems to signify players that played the 2017-2018 season
current_players = player_measure[player_measure['Year End']==2018]

#chosing select columns to upload
clean_current_players = current_players[['Player Full Name', 'Height (ft 1/2)', 'Height (inches 2/2)', 'Height (in cm)',\
                'Wingspan (in cm)', 'Standing Reach (in cm)', 'Weight (in lb)', 'Body Fat (%)'] ].\
                dropna(axis = 0, how = 'any').\
                rename(columns={'Height (ft 1/2)':'Height(ft)','Height (inches 2/2)':'Height(in)',\
                                'Height (in cm)': 'Height(cm)', 'Wingspan (in cm)': 'Wingspan(cm)',\
                                'Standing Reach (in cm)':'Standing_Reach(cm)','Weight (in lb)':'Weight(lb)',\
                                'Body Fat (%)': 'Body_Fat(%)'}).\
                set_index('Player Full Name').copy()

#cleaning the zero value rows
player_stats_rough = clean_current_players.drop(clean_current_players[clean_current_players["Standing_Reach(cm)"]==0].\
                                          index, axis=0).copy()

#creating a more readable height stat
player_stats_rough["Height_full(in)"]=12*player_stats_rough["Height(ft)"] + player_stats_rough["Height(in)"]

#adding height stat in
player_stats_final = player_stats_rough[['Height_full(in)', 'Wingspan(cm)', 'Standing_Reach(cm)','Weight(lb)',\
                                         'Body_Fat(%)']].copy()

#creating parquet file
review_table = pa.Table.from_pandas(player_stats_final)
pq.write_table(review_table, '../input/player_stats.parquet')