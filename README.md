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
    a. Load csv file (664 records), (dataset from Kaggle.com)
    b. Remove duplicates (540 records)
    c. Clean up player name column
    d. Filter columns ("id", "rank", "position", "age", "games", "minutes_played", "true_shooting_percentage", "block_percentage")
    e. Export stats (NBA_player_stats_final.csv)

  * Player Measurements

  * MVP Voting
  
3. Load Data 
