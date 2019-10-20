# import the library
import pandas as pd
In [75]:
# read the csv file
Salary_data_df = pd.read_csv(r'C:\Users\ENOCK DESCOPIN\Desktop\NBA-Player-Stats\Raw Data\NBA_season1718_salary.csv')
In [76]:
#open the CSV file
Salary_data_df.head()
Out[76]:
Unnamed: 0	Player	Tm	season17_18
0	1	Stephen Curry	GSW	34682550.0
1	2	LeBron James	CLE	33285709.0
2	3	Paul Millsap	DEN	31269231.0
3	4	Gordon Hayward	BOS	29727900.0
4	5	Blake Griffin	DET	29512900.0
In [77]:
# Rename some columns
Clean_data_df = Salary_data_df.columns = ['Unnamed','Players','Team','Salary17_18_$']
In [80]:
Salary_data_df.head()
Out[80]:
Unnamed	Players	Team	Salary17_18_$
0	1	Stephen Curry	GSW	34682550.0
1	2	LeBron James	CLE	33285709.0
2	3	Paul Millsap	DEN	31269231.0
3	4	Gordon Hayward	BOS	29727900.0
4	5	Blake Griffin	DET	29512900.0
In [92]:
Clean_data_df.To_csv('NBA_salary.csv', index=False)