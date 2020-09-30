# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 19:52:28 2020

This script web scrapes from basketball-reference.com to obtain lineup data from 
Play-by-Play data 

@author: salez
"""

import requests
from bs4 import BeautifulSoup 
import pandas as pd 
import numpy as np
import re

## Players in Series 
PlayerNames_Play = ['LeBron James',
 'Kyrie Irving',
 'J.R. Smith',
 'Kevin Love',
 'Tristan Thompson',
 'Richard Jefferson',
 'Iman Shumpert',
 'Channing Frye',
 'Matthew Dellavedova']

# Convert Player name to abbreviated names 
NamesAbv = []
for player in PlayerNames_Play:
    NamesAbv.append(player[0] + '. ' + player.split()[1])
    

# Indicator if players are in or on bench
Starters = [1,1,1,1,1,0,0,0,0]

# Each quarter is split into thirds
features = ['Name','Q11', 'Q12', 'Q13',
            'Q21', 'Q22', 'Q23', 
            'Q31', 'Q32', 'Q33', 
            'Q41', 'Q42', 'Q43']

# Create data frame to store player lineup data
Lineup_Play = pd.DataFrame(np.zeros((len(PlayerNames_Play), len(features))),
                         columns = features)

# Game link to analyze 
game_links = ['https://www.basketball-reference.com/boxscores/pbp/201605080ATL.html']

# Compare quarters to make sure 5 players are on floor
def SubsComp(Qrt1,Qrt2): 
    Qrt = [sum(x) for x in zip(Qrt1, Qrt2)]
    return Qrt
        
    
def CheckSubs(Row_data, StartQ, EndQ, NamesAbv, Quarter, PrevQrt): 
    ''' This function goes through each row from the play-by-play data 
    and checks which players are in the game and which players are 
    being subbed out''' 
    
    # Check if in quarter 1 
    if Quarter ==  1: 
        # First Quarter
        Qx2 = [0]*len(NamesAbv)
        Qx3 = [0]*len(NamesAbv)
        
    
        for i in range(StartQ, EndQ):
            # search for players entering games
            if re.search('enters the game for',Row_data[i].getText()):
                
                if re.findall('enters the game for ([a-zA-Z. ]+)', 
                             Row_data[i].getText())[0] in NamesAbv: 
                
                    PlayerOut = re.findall('enters the game for ([a-zA-Z. ]+)', 
                                                  Row_data[i].getText())[0]
                    PlayerIn = re.findall('([a-zA-Z. ]+) enters', 
                                                  Row_data[i].getText())[0]
                    
                    print(Row_data[i].getText())
                    print(Row_data[i].find('td').getText())
                    print(PlayerOut, PlayerIn, '\n')
                    
                    MinuteTime = int(Row_data[i].find('td').getText().split(':')[0])
                    
                    if MinuteTime >= 6:
                        Qx2[NamesAbv.index(PlayerIn)] = 1
                        Qx2[NamesAbv.index(PlayerOut)] = -1
                        
                    elif MinuteTime >= 2 and MinuteTime < 6: 
                        Qx3[NamesAbv.index(PlayerIn)] = 1
                        Qx3[NamesAbv.index(PlayerOut)] = -1
                  
                        
        Qx2 = SubsComp(PrevQrt,Qx2)
        Qx3 = SubsComp(Qx2, Qx3)
        
        return Qx2, Qx3
    
    elif Quarter == 2:
        # Second Quarter
        Qx2 = [0]*len(NamesAbv)
        Qx3 = [0]*len(NamesAbv)
        
        for i in range(StartQ, EndQ):
            if re.search('enters the game for',Row_data[i].getText()):
                
                if re.findall('enters the game for ([a-zA-Z. ]+)', 
                             Row_data[i].getText())[0] in NamesAbv: 
                
                    PlayerOut = re.findall('enters the game for ([a-zA-Z. ]+)', 
                                                  Row_data[i].getText())[0]
                    PlayerIn = re.findall('([a-zA-Z. ]+) enters', 
                                                  Row_data[i].getText())[0]
                    
                    print(Row_data[i].getText())
                    print(Row_data[i].find('td').getText())
                    print(PlayerOut, PlayerIn, '\n')
                    
                    MinuteTime = int(Row_data[i].find('td').getText().split(':')[0])
                    
                    if MinuteTime >= 6:
                        Qx2[NamesAbv.index(PlayerIn)] = 1
                        Qx2[NamesAbv.index(PlayerOut)] = -1
                        
                    elif MinuteTime >= 2 and MinuteTime < 6: 
                        Qx3[NamesAbv.index(PlayerIn)] = 1
                        Qx3[NamesAbv.index(PlayerOut)] = -1
                        
        Qx2 = SubsComp(PrevQrt,Qx2)
        Qx3 = SubsComp(Qx2, Qx3)
        
        return Qx2, Qx3
    
    elif Quarter == 3:
        # Third Quarter
        Qx2 = [0]*len(NamesAbv)
        Qx3 = [0]*len(NamesAbv)
        
        for i in range(StartQ, EndQ):
            if re.search('enters the game for',Row_data[i].getText()):
                
                if re.findall('enters the game for ([a-zA-Z. ]+)', 
                             Row_data[i].getText())[0] in NamesAbv: 
                
                    PlayerOut = re.findall('enters the game for ([a-zA-Z. ]+)', 
                                                  Row_data[i].getText())[0]
                    PlayerIn = re.findall('([a-zA-Z. ]+) enters', 
                                                  Row_data[i].getText())[0]
                    
                    print(Row_data[i].getText())
                    print(Row_data[i].find('td').getText())
                    print(PlayerOut, PlayerIn, '\n')
                    
                    MinuteTime = int(Row_data[i].find('td').getText().split(':')[0])
                    
                    if MinuteTime >= 6:
                        Qx2[NamesAbv.index(PlayerIn)] = 1
                        Qx2[NamesAbv.index(PlayerOut)] = -1
                        
                    elif MinuteTime >= 2 and MinuteTime < 6: 
                        Qx3[NamesAbv.index(PlayerIn)] = 1
                        Qx3[NamesAbv.index(PlayerOut)] = -1
                        
        Qx2 = SubsComp(PrevQrt,Qx2)
        Qx3 = SubsComp(Qx2, Qx3)
        
        return Qx2, Qx3
    
    elif Quarter == 4:
        # Third Quarter
        Qx2 = [0]*len(NamesAbv)
        Qx3 = [0]*len(NamesAbv)
        
        for i in range(StartQ, EndQ):
            if re.search('enters the game for',Row_data[i].getText()):
                
                if re.findall('enters the game for ([a-zA-Z. ]+)', 
                             Row_data[i].getText())[0] in NamesAbv: 
                
                    PlayerOut = re.findall('enters the game for ([a-zA-Z. ]+)', 
                                                  Row_data[i].getText())[0]
                    PlayerIn = re.findall('([a-zA-Z. ]+) enters', 
                                                  Row_data[i].getText())[0]
                    
                    print(Row_data[i].getText())
                    print(Row_data[i].find('td').getText())
                    print(PlayerOut, PlayerIn, '\n')
                    
                    MinuteTime = int(Row_data[i].find('td').getText().split(':')[0])
                    
                    if MinuteTime >= 6:
                        Qx2[NamesAbv.index(PlayerIn)] = 1
                        Qx2[NamesAbv.index(PlayerOut)] = -1
                        
                    elif MinuteTime >= 2 and MinuteTime < 6: 
                        Qx3[NamesAbv.index(PlayerIn)] = 1
                        Qx3[NamesAbv.index(PlayerOut)] = -1
                        
        Qx2 = SubsComp(PrevQrt,Qx2)
        Qx3 = SubsComp(Qx2, Qx3)
        
        return Qx2, Qx3
    

# Loop through game link and compile lineup dataframe  

for game in game_links:
    
    # Read in each game data 
    source = requests.get(game)
    soup = BeautifulSoup(source.text)
    
    table_dat = soup.find('div', class_= 'overthrow table_container')
        
    Row_data = table_dat.find_all('tr')
    
    for i in range(len(Row_data)):
        if re.search('Start of 1st quarter',Row_data[i].getText()):
            Start1st = i
            print(Start1st)
        elif re.search('Start of 2nd quarter',Row_data[i].getText()):
            Start2nd = i
            print(Start2nd)
        elif re.search('Start of 3rd quarter',Row_data[i].getText()):
            Start3rd = i
            print(Start3rd)
        elif re.search('Start of 4th quarter',Row_data[i].getText()):
            Start4th = i
            print(Start4th)
            
    # Manually make the starters start the 3rd quarter 
    Q11 = Starters
    
    #First quarter
    Q12, Q13 = CheckSubs(Row_data, Start1st, Start2nd, NamesAbv, 1, Starters)
    
    # Manually put in lineup for start of second quarter
    Q21 = [0,1,0,0,0,1,1,1,1]
    
    #Second quarter
    Q22, Q23 = CheckSubs(Row_data, Start2nd, Start3rd, NamesAbv, 2, Q21)
    
    # Manually make the starters start the 3rd quarter 
    Q31 = Starters
    
    #Third quarter
    Q32, Q33 = CheckSubs(Row_data, Start3rd, Start4th, NamesAbv, 3, Q31)
    
    # Manually input lineup for Start of 4th quarter
    Q41 = [0,1,0,0,1,0,1,1,1]
    
    #4th quarter
    Q42, Q43 = CheckSubs(Row_data, Start4th, len(Row_data), NamesAbv, 4, Q41)
    
    ColList = [PlayerNames_Play, 
                    Q11, Q12, Q13, 
                    Q21, Q22, Q23, 
                    Q31, Q32, Q33, 
                    Q41, Q42, Q43]
    
    for i in range(len(ColList)): 
        Lineup_Play[Lineup_Play.columns[i]] = ColList[i]

Lineup_Play.to_csv('CleLine.csv', index = False)
    
    

                    
                    
                
                 
                
        
            
        



