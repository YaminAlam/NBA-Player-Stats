# NBA-Player-Stats
An examination into NBA player stats for the 2017-2018 season


## Data Sources
* [Player Salary](https://www.kaggle.com/koki25ando/salary)
* [Player Stats](https://www.kaggle.com/mcamli/nba17-18)
* [Player Measurements](https://www.kaggle.com/whitefero/nba-players-measurements-19472017)
* [MVP Voting](https://www.kaggle.com/danchyy/nba-mvp-votings-through-history)

##Pipeline
1. Download Data Files

2. Transformations 
  * Player Measurements (Yamin Alam)
    1. Load Data
    2. Filter to currently active players
    3. Filter Columns ('Player Full Name', 'Height (ft 1/2)', 'Height (inches 2/2)', 'Height (in cm)',
                'Wingspan (in cm)', 'Standing Reach (in cm)', 'Weight (in lb)', 'Body Fat (%)')
    4. Check and clear columns that have value of 0
    5. Create new height column that has more concise measurement
    6. Filter final dataset to include only the new height column and remove the old height columns, while including the other 
    previously filtered columns.
    7. Save file to csv
    
  * Player Stats (David Cimino) - et_plater_stats.py (NBA players from 2017-2018 season)
    1. Load csv file (664 records), (dataset from Kaggle.com)
    2. Remove duplicates (540 records)
    3. Clean up player name column (remove tags after "\")
    4. Filter columns ("id", "rank", "position", "age", "games", "minutes_played", "true_shooting_percentage", "block_percentage")
    5. Export stats (NBA_player_stats_final.csv)
  
  * Player Salary (Enock Descopin) load(NBA_season 17_18) 
     1- Load data from csv file, (450 records), ( dataset from Kaggle.com)
     2- Filter the headers and rename them.
     3- rename all the rows in the Name column.
     4- rename and save the csv file and upload it in github

  * MVP Voting (Tohibur Paiker)
     1. Load data from csv (mvp_votings.csv, 636 records), dataset from Kaggle.com
     2. Filter the data by "season", then filter the season for only 2017-18 season, came out to only 12 records.
     3. Chose relevant columns to MVP_votings: 'player', 'votes_first', 'points_won', 'points_max', 'award_share'.
     4. Cleaned up the column names: 'Player',	'Votes',	'Points_won',	'Max_points',	'Award_share'.
  
3. Load Data 
