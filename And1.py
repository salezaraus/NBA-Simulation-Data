# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 16:08:49 2020

This code web scrapes basketball reference for all games for any teams to 
find their play by play data and start extracting information from such 
as fouls and and1 frequency

@author: salez
"""

import requests
from bs4 import BeautifulSoup 
import pandas as pd 
import numpy as np
import re

## Create Totals Stats Data Frame         
And1Stats = ['Sht Fouls Drawn', 'And1_2pt', 'And1_3pt'] 

## Players in Series 
PlayerNames_Play = ['LeBron James',
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

PlayerNames_Reg = ['LeBron James',
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

# Create data frame to store data 
TotalStats_Play = pd.DataFrame(np.zeros((len(PlayerNames_Play), len(And1Stats))),
                        index = PlayerNames_Play, columns = And1Stats)

TotalStats_Reg = pd.DataFrame(np.zeros((len(PlayerNames_Reg), len(And1Stats))),
                        index = PlayerNames_Reg, columns = And1Stats)

# Compares abbreviated name to full name. For example, AbbName = 'L. James' 
# returns True if FullName = 'LeBron James', False otherwise
def PlyNameComp(AbbName, FullName):
    if (AbbName.split()[0][0] == FullName[0] and AbbName.split()[1] ==
        FullName.split()[1]): 
        return True
    else: 
        return False

# Function loops through all game urls in game_links and stores them in 
# Pandas dataframe 'TotalStats' to calculate all and1 stats
def And1(game_links, TotalStats, PlayerNames):     
    for game in game_links:
        
        # Read in each game data 
        source = requests.get(game)
        soup = BeautifulSoup(source.text)
        
        table_dat = soup.find('div', class_= 'overthrow table_container')
        
        Row_data = table_dat.find_all('tr')
        
        for i in range(len(Row_data)):
            ClePlyFouled = False
            # search if shooting foul occured
            if re.search('Shooting foul',Row_data[i].getText()):                
                PlayerFouled = re.findall('drawn by ([a-zA-Z\u00C0-\u00D6\u00D8-\u00f6\u00f8-\u00ff. ]+)', 
                                          Row_data[i].getText())[0]
                               
                # Check if player fouled is from Cleveland
                for player in PlayerNames: 
                    if PlyNameComp(PlayerFouled, player):
                        TotalStats.loc[player]['Sht Fouls Drawn'] += 1
                        ClePlyFouled = True
                        break
                        
                # If Cleveland player fouled, check if they make an and1
                if ClePlyFouled: 
                    if re.search((PlayerFouled +' makes 2-pt'),Row_data[i-1].getText()): 
                        TotalStats.loc[player]['And1_2pt'] += 1
                    elif re.search((PlayerFouled + ' makes 3-pt'),Row_data[i-1].getText()): 
                        TotalStats.loc[player]['And1_3pt'] += 1
    return(TotalStats)

# Start from scheduled basketball games for Cleveland
CLE_sched = 'https://www.basketball-reference.com/teams/CLE/2016_games.html'

# Play by Play URL prefix
link_prefix = 'https://www.basketball-reference.com/boxscores/pbp/'

source = requests.get(CLE_sched)
soup = BeautifulSoup(source.text)

# Find Playoff games 
playoffs = soup.find('div', id = 'all_games_playoffs')
play_dat = playoffs.find('div', class_ = 'overthrow table_container')


play_game_links = []

# Find all links for playoff games
for game in play_dat.findAll('td', {"data-stat" : "box_score_text"}):
    link = link_prefix + game.a.get('href').split('/')[2]
    play_game_links.append(link)
    
# Only consider playoff games excluding finals
Ply_no_finals = play_game_links[0:14]    

# Find Regular season games 
regular = soup.find('div', id = 'all_games')
reg_dat = regular.find('div', class_ = 'overthrow table_container')

reg_game_links = []

# Find all links for playoff games
for game in reg_dat.findAll('td', {"data-stat" : "box_score_text"}):
    link = link_prefix + game.a.get('href').split('/')[2]
    reg_game_links.append(link)
                    
################
   
And1_Play = And1(Ply_no_finals, TotalStats_Play, PlayerNames_Play)
And1_Reg = And1(reg_game_links, TotalStats_Reg, PlayerNames_Reg)
    

    

          
                    
            
            
        
    
    


    

