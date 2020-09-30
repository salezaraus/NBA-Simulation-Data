"""
Created on Wed May  6 17:36:22 2020

@author: Christopher Salazar

This script creates a csv output for the total stats for all games prior to 
the NBA finals and creates csv for summary stats to be used in simulation
"""

# Import Libraries
import pandas as pd 
import numpy as np

########################################################
### DEFINE FUCNTIONS 
########################################################


# Renames CSV game files so that we could easily iterate thorugh all games 
def GameRename(Series,Game,textfile): 
    text = list(textfile)
    text[1] = str(Series)
    text[4] = str(Game)

    return "".join(text)

# Converts formatted MM:SS minutes played into a minutes float
def MPConversion(MP): 
    Time = float(MP.split(':')[0]) + float(MP.split(':')[1])/60
    
    return(Time)

# This function inputs a csv file for a nba game and returns a dictionary of
# Team Statistics per game.
def TeamStats(BasicStats):
        
    # Team Stats
    TmMP = float(BasicStats.loc[len(BasicStats.index)-1,'MP'])
    TmFGA = float(BasicStats.loc[len(BasicStats.index)-1,'FGA'])
    TmFTA = float(BasicStats.loc[len(BasicStats.index)-1,'FTA'])
    TmORB = float(BasicStats.loc[len(BasicStats.index)-1,'ORB'])
    TmDRB = float(BasicStats.loc[len(BasicStats.index)-1,'DRB'])
    TmTOV = float(BasicStats.loc[len(BasicStats.index)-1,'TOV'])
    
    Stats = {'TmMP': TmMP, 'TmFGA': TmFGA, 'TmFTA': TmFTA, 'TmORB': TmORB, 
             'TmDRB': TmDRB, 'TmTOV': TmTOV}
   
    
    return(Stats)

# Function uses dataframe input for games and player string to extract 
# data stats for player     
def PlayerStats(BasicStats, Player): 
    
    # Change Index to Player names 
    df = BasicStats.set_index('Starters')
    
    try: 
        RawMP = df.loc[Player, 'MP']
        MP = MPConversion(RawMP)    
    except: 
        MP = 0.0;
        
    try: 
        FGM = float(df.loc[Player, 'FG'])        
    except: 
        FGM = 0.0;
        
    try: 
        FGA = float(df.loc[Player, 'FGA'])        
    except: 
        FGA = 0.0;   
        
    try: 
        ThreeFGM = float(df.loc[Player, '3P'])        
    except: 
        ThreeFGM = 0.0;    
        
    try: 
        ThreeFGA = float(df.loc[Player, '3PA'])        
    except: 
        ThreeFGA = 0.0;
        
    try: 
        FTM = float(df.loc[Player, 'FT'])      
    except: 
        FTM = 0.0;
        
    try: 
        FTA = float(df.loc[Player, 'FTA'])       
    except: 
        FTA = 0.0;
        
    try: 
        ORB = float(df.loc[Player, 'ORB'])       
    except: 
        ORB = 0.0;
        
    try: 
        DRB = float(df.loc[Player, 'DRB'])       
    except: 
        DRB = 0.0;
        
    try: 
        TOV = float(df.loc[Player, 'TOV'])        
    except: 
        TOV = 0.0;
        
    try: 
        PF = float(df.loc[Player, 'PF'])        
    except: 
        PF = 0.0;
        
        
    PlayerStatsDict = {'MP': MP, 'FG': FGM, 'FGA': FGA, '3P': ThreeFGM, 
                  '3PA':ThreeFGA, 'FT': FTM, 'FTA':FTA, 'ORB':ORB, 
                  'DRB':DRB, 'TOV':TOV, 'PF': PF}
        
    return(PlayerStatsDict)
    
    
# Renames Series files so that we can cycle through all Series
def SeriesRename(Series,textfile): 
    text = list(textfile)
    text[1] = str(Series)

    return "".join(text)


# Function uses dataframe input for games and player string to extract 
# data stats for player     
def USGStats(BasicStats, Player): 
    
    # Change Index to Player names 
    df = BasicStats.set_index('Player')
    
    try: 
        G = float(df.loc[Player, 'G'])        
    except: 
        G = 0.0;
        
    try: 
        USG = float(df.loc[Player, 'USG%'])        
    except: 
        USG = 0.0;
        
    try: 
        DRBper = float(df.loc[Player, 'DRB%'])        
    except: 
        DRBper = 0.0;
        
    try: 
        ORBper = float(df.loc[Player, 'ORB%'])        
    except: 
        ORBper = 0.0;
        
    try: 
        ORtg = float(df.loc[Player, 'ORtg'])        
    except: 
        ORtg = 0.0;
        
    try: 
        DRtg = float(df.loc[Player, 'DRtg'])        
    except: 
        DRtg = 0.0;
    
        
    USGStatsDict = {'G': G, 'USG%': USG, 'DRB%': DRBper, 'ORB%':ORBper, 
                    'ORtg': ORtg, 'DRtg': DRtg}
    
    return(USGStatsDict)
    
    
#######################
### Script 
#######################
    
    
## Create Totals Stats Data Frame         
Stats = ['MP','FG','FGA','3P','3PA','FT','FTA','FT%','ORB',
 'DRB','TRB','AST','STL','BLK','TOV','PF','PTS']  

## Players in Series 
PlayerNames = ['LeBron James',
 'Kyrie Irving',
 'J.R. Smith',
 'Kevin Love',
 'Tristan Thompson',
 'Richard Jefferson',
 'Iman Shumpert',
 'Channing Frye',
 'Matthew Dellavedova',
 'Timofey Mozgov',
 'Mo Williams',
 'James Jones',
 'Dahntay Jones',
 'Jordan McRae']

TotalStats = pd.DataFrame(np.zeros((len(PlayerNames), len(Stats))),
                        index = PlayerNames, columns = Stats)


# Basic format of data files 
BasicStatsGame = "SX_GX_Basic.txt"    

GamesperSeries = [4,4,6] 

# Calculate Individual Player Stats (Total)

for Series in range(len(GamesperSeries)): 
    for Game in range(GamesperSeries[Series]): 
        
         # Rename Text Files for each game 
        BasicStatsGame = GameRename(Series+1,Game+1,BasicStatsGame)
        
        # Create DataFrame
        BasicStats = pd.read_csv(BasicStatsGame) 
        
        # Iterate through each player in the game 
        for player in range(len(BasicStats.index)-1):
            
            #Store each player state in dictionary 
            PlayerStat = PlayerStats(BasicStats,BasicStats['Starters'][player])
            
            # Update Total Minutes 
            TotalStats.loc[BasicStats['Starters'][player],
                           'MP'] = TotalStats.loc[BasicStats['Starters'][player],
                           'MP'] + PlayerStat['MP']
            
            # Update Total FG Made
            TotalStats.loc[BasicStats['Starters'][player],
                           'FG'] = TotalStats.loc[BasicStats['Starters'][player],
                           'FG'] + PlayerStat['FG']
            
            # Update Total FG Attempted
            TotalStats.loc[BasicStats['Starters'][player],
                           'FGA'] = TotalStats.loc[BasicStats['Starters'][player],
                           'FGA'] + PlayerStat['FGA']
            
            # Update Total 3FG Made
            TotalStats.loc[BasicStats['Starters'][player],
                           '3P'] = TotalStats.loc[BasicStats['Starters'][player],
                           '3P'] + PlayerStat['3P']
            
            # Update Total 3FG Attempted
            TotalStats.loc[BasicStats['Starters'][player],
                           '3PA'] = TotalStats.loc[BasicStats['Starters'][player],
                           '3PA'] + PlayerStat['3PA']
            
            # Update Total FT Made
            TotalStats.loc[BasicStats['Starters'][player],
                           'FT'] = TotalStats.loc[BasicStats['Starters'][player],
                           'FT'] + PlayerStat['FT']
            
            # Update Total FT Attempted
            TotalStats.loc[BasicStats['Starters'][player],
                           'FTA'] = TotalStats.loc[BasicStats['Starters'][player],
                           'FTA'] + PlayerStat['FTA']
            
            # Update Total ORB
            TotalStats.loc[BasicStats['Starters'][player],
                           'ORB'] = TotalStats.loc[BasicStats['Starters'][player],
                           'ORB'] + PlayerStat['ORB']
            
            # Update Total DRB
            TotalStats.loc[BasicStats['Starters'][player],
                           'DRB'] = TotalStats.loc[BasicStats['Starters'][player],
                           'DRB'] + PlayerStat['DRB']
            
            # Update Total TOV
            TotalStats.loc[BasicStats['Starters'][player],
                           'TOV'] = TotalStats.loc[BasicStats['Starters'][player],
                           'TOV'] + PlayerStat['TOV']
            
            # Update Total PF
            TotalStats.loc[BasicStats['Starters'][player],
                           'PF'] = TotalStats.loc[BasicStats['Starters'][player],
                           'PF'] + PlayerStat['PF']
            
 
# Calculate Team Stats per game  

## Create Totals Stats Data Frame         
Stats = ['MP', 'FGA','FTA','ORB','DRB','TOV']  

TotalTeam = pd.DataFrame(np.zeros((1, len(Stats))), columns = Stats)            
            
                        
for Series in range(len(GamesperSeries)): 
    for Game in range(GamesperSeries[Series]): 
        
         # Rename Text Files for each game 
        BasicStatsGame = GameRename(Series+1,Game+1,BasicStatsGame)
        
        # Create DataFrame
        BasicStats = pd.read_csv(BasicStatsGame)
        
        GameStats = TeamStats(BasicStats)
        
        TotalTeam['MP'] = TotalTeam['MP'] + GameStats['TmMP']
        TotalTeam['FGA'] = TotalTeam['FGA']+ GameStats['TmFGA']
        TotalTeam['FTA'] = TotalTeam['FTA']+ GameStats['TmFTA']
        TotalTeam['ORB'] = TotalTeam['ORB']+ GameStats['TmORB']
        TotalTeam['DRB'] = TotalTeam['DRB']+ GameStats['TmDRB']
        TotalTeam['TOV'] = TotalTeam['TOV']+ GameStats['TmTOV']
        
# Calculate usage rate by weighted average for each series
# Create temporary data frame 
        
## Create Totals Stats Data Frame         
Stats = ['G', 'GP*USG', 'GP*DRB%', 'GP*ORB%', 'GP*ORtg', 'GP*DRtg']  

USGTable = pd.DataFrame(np.zeros(( len(PlayerNames),len(Stats))), 
                         index= PlayerNames,columns = Stats) 

        
# Basic format of series csv files 
BasicStatsGame = "SX_Sum_Adv.txt"        

## THis is to calculate weightted stats 
for Series in range(3): 
    
    # Rename Text Files for each game 
    BasicStatsGame = SeriesRename(Series+1,BasicStatsGame)
     
    # Reads the game csv file 
    BasicStats = pd.read_csv(BasicStatsGame) 
    
    for player in range(len(BasicStats.index)-1):
        
        #Store each player state in dictionary 
        USGStat = USGStats(BasicStats,BasicStats['Player'][player])
        
        USGTable.loc[BasicStats['Player'][player],
                           'G'] = USGTable.loc[BasicStats['Player'][player],
                           'G'] + USGStat['G']
        
        USGTable.loc[BasicStats['Player'][player],
                           'GP*USG'] = USGTable.loc[BasicStats['Player'][player],
                           'GP*USG'] + USGStat['G']*USGStat['USG%']
        
        USGTable.loc[BasicStats['Player'][player],
                           'GP*DRB%'] = USGTable.loc[BasicStats['Player'][player],
                           'GP*DRB%'] + USGStat['G']*USGStat['DRB%']
        
        USGTable.loc[BasicStats['Player'][player],
                           'GP*ORB%'] = USGTable.loc[BasicStats['Player'][player],
                           'GP*ORB%'] + USGStat['G']*USGStat['ORB%']
        
        USGTable.loc[BasicStats['Player'][player],
                           'GP*ORtg'] = USGTable.loc[BasicStats['Player'][player],
                           'GP*ORtg'] + USGStat['G']*USGStat['ORtg']
        
        USGTable.loc[BasicStats['Player'][player],
                           'GP*DRtg'] = USGTable.loc[BasicStats['Player'][player],
                           'GP*DRtg'] + USGStat['G']*USGStat['DRtg']

        
# Create Total Stats Data Frame
# Concatenate 
TotalStats = pd.concat([TotalStats,USGTable], axis=1)
     
# Calcuate 2PT %           
TotalStats['2pt%'] = (TotalStats['FG']-TotalStats['3P'])/(TotalStats['FGA']
                -TotalStats['3PA'])

# Calcuate 3PT % 
TotalStats['3pt%'] = TotalStats['3P']/TotalStats['3PA'] 

# Calcualte 3PT Rate                         
TotalStats['3ptRate'] = TotalStats['3PA']/TotalStats['FGA']

# Calculate Usage Rate 
TotalStats['USG%'] = TotalStats['GP*USG']/TotalStats['G']/100  

# Calculate DRB Rate 
TotalStats['DRB%'] = TotalStats['GP*DRB%']/TotalStats['G']/100  

# Calculate ORB Rate 
TotalStats['ORB%'] = TotalStats['GP*ORB%']/TotalStats['G']/100      

# Calcualte Turnover rate 
TotalStats['TOV Rate'] = TotalStats['TOV'] /(TotalStats['FGA'] 
            + 0.44 * TotalStats['FTA'] + TotalStats['TOV']) 

# Calculate Free Throw Rate 
TotalStats['FT Rate'] = TotalStats['FTA']/TotalStats['FGA'] 

# Calculate ORtg Rate 
TotalStats['ORtg'] = TotalStats['GP*ORtg']/TotalStats['G']

# Calculate DRtg Rate 
TotalStats['DRtg'] = TotalStats['GP*DRtg']/TotalStats['G'] 

# Calcualte PF per game 
TotalStats['PFGame'] = TotalStats['PF']/TotalStats['G']

TotalStats['FT%'] = TotalStats['FT']/TotalStats['FTA']


Starters = [1,1,1,1,1,0,0,0,0,0,0,0,0,0]

TotalStats['Starters'] = Starters

del TotalStats['GP*USG']
del TotalStats['GP*DRB%']
del TotalStats['GP*ORB%']
del TotalStats['GP*ORtg']
del TotalStats['GP*DRtg']

TotalStats.to_csv('CLE_stats.csv', index = True)
            
            
            
            
            
            
    
        
        
