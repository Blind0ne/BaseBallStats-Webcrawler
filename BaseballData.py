import pandas as pd
import time
from urllib import request


# All Baseballteams in the American League!

Team = ['bal',
        'bos',
        'nyy',
        'tor',
        'chw',
        'cle',
        'det',
        'kan',
        'min',
        'laa',
        'oak',
        'sea',
        'tex',
        'hou',
        'was',
        'nym',
        'phi',
        'mia',
        'atl',
        'pit',
        'stl',
        'mil',
        'chc',
        'cin',
        'lad',
        'sdg',
        'sfo',
        'col',
        'ari']


def main():

    # Global timers
    global start_time
    global end_time

    start_time = time.time()        # Times the duration of the scraping!
    full_data = get_league()
    full_save = 'FullBaseBall.csv'  
    print(full_save)
    full_data.to_csv(full_save)     # Saves the data to csv-File

    # Just some timer calculation
    end_time = time.time()
    delta_seconds = end_time - start_time
    delta_minutes = delta_seconds / 60
    if delta_seconds <= 60:
        print("--- %s seconds ---" % delta_seconds)
    else:
        print("--- %s minutes ---" % delta_minutes)


def get_players(id):
    ''' Gets information on each Player! '''

    url = 'http://sports.yahoo.com/mlb/players/' + str(id) + '/'
    response = request.urlopen(url)
    player_page = str(response.read())
    sleeper = 0.05 #There are 42 sleepers in the function
    df = pd.DataFrame(columns=['Team',
                               'ID',
                               'Batting_Games',
                               'At_Bats',
                               'Batting_Runs',
                               'Batting_Hits',
                               'Doubles',
                               'Triples',
                               'Batting_Home_Runs',
                               'Runs_Batted_In',
                               'Batting_Bases_On_Balls',
                               'Batting_Strike_Outs',
                               'Stolen_Bases',
                               'Caught_Stealing',
                               'Batting_Average',
                               'On_Base_Percentage',
                               'Slugging_Percentage',
                               'On_Base_Plus_Slugging',
                               'Pitching_Games',
                               'Pitching_Games_Started',
                               'Wins',
                               'Losses',
                               'Saves',
                               'Blown_Saves',
                               'Holds',
                               'Complete_Games',
                               'Shutouts',
                               'Innings_Pitched',
                               'Pitching_Hits',
                               'Pitching_Runs',
                               'Earned_Runs',
                               'Pitching_Home_Runs',
                               'Pitching_Bases_On_Balls',
                               'Pitching_Strikeouts',
                               'Earned_Runs_Average',
                               'Walks_Plus_Hits_Per_Inning_Pitched',
                               'Batting_Average_Against',
                               'Fielding_Games',
                               'Position',
                               'Fielding_Games_Started',
                               'Innings',
                               'Putouts',
                               'Total_Chance',
                               'Assists',
                               'Errors',
                               'Double_Plays',
                               'Fielding'
                               ])

    # TOTALS

    # BATTING ----------------------------------------------------------------------------------------------------------
    try:
        Batting_Games = player_page.split('<td class="mlb-stat-type-1 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        At_Bats = player_page.split('<td class="mlb-stat-type-2 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Batting_Runs = player_page.split('<td class="mlb-stat-type-3 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Batting_Hits = player_page.split('<td class="mlb-stat-type-4 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Doubles = player_page.split('<td class="mlb-stat-type-5 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Triples = player_page.split('<td class="mlb-stat-type-6 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Batting_Home_Runs = player_page.split('<td class="mlb-stat-type-7 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Runs_Batted_In = player_page.split('<td class="mlb-stat-type-8 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Batting_Bases_On_Balls = player_page.split('<td class="mlb-stat-type-14 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Batting_Strike_Outs = player_page.split('<td class="mlb-stat-type-17 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Stolen_Bases = player_page.split('<td class="mlb-stat-type-12 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Caught_Stealing = player_page.split('<td class="mlb-stat-type-13 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Batting_Average = player_page.split('<td class="mlb-stat-type-23 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        On_Base_Percentage = player_page.split('<td class="mlb-stat-type-24 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Slugging_Percentage = player_page.split('<td class="mlb-stat-type-25 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        On_Base_Plus_Slugging = player_page.split('<td class="mlb-stat-type-26 stat-total')[1].split('</td>')[0].split('>')[1]
    except:
        Batting_Games = 0
        At_Bats = 0
        Batting_Runs = 0
        Batting_Hits = 0
        Doubles = 0
        Triples = 0
        Batting_Home_Runs = 0
        Runs_Batted_In = 0
        Batting_Bases_On_Balls = 0
        Batting_Strike_Outs = 0
        Stolen_Bases = 0
        Caught_Stealing = 0
        Batting_Average = 0
        On_Base_Percentage = 0
        Slugging_Percentage = 0
        On_Base_Plus_Slugging = 0



    '''
    print('----------BATTING-------------')
    print('G', Batting_Games)
    print('AB', At_Bats)
    print('R', Batting_Runs)
    print('H', Batting_Hits)
    print('2B', Doubles)
    print('3B', Triples)
    print('HR', Batting_Home_Runs)
    print('RBI', Runs_Batted_In)
    print('BB', Batting_Bases_On_Balls)
    print('K', Batting_Strike_Outs)
    print('SB', Stolen_Bases)
    print('CS', Caught_Stealing)
    print('AVG', Batting_Average)
    print('OBP', On_Base_Percentage)
    print('SLG', Slugging_Percentage)
    print('OPS', On_Base_Plus_Slugging)
    print('--------------------------------')
    '''

    # PITCHING ---------------------------------------------------------------------------------------------------------
    try:
        Pitching_Games = player_page.split('<td class="mlb-stat-type-103 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Pitching_Games_Started = player_page.split('<td class="mlb-stat-type-104 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Wins = player_page.split('<td class="mlb-stat-type-101 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Losses = player_page.split('<td class="mlb-stat-type-102 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Saves = player_page.split('<td class="mlb-stat-type-107 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Blown_Saves = player_page.split('<td class="mlb-stat-type-147 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Holds = player_page.split('<td class="mlb-stat-type-136 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Complete_Games = player_page.split('<td class="mlb-stat-type-105 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Shutouts = player_page.split('<td class="mlb-stat-type-106 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Innings_Pitched = player_page.split('<td class="mlb-stat-type-139 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Pitching_Hits = player_page.split('<td class="mlb-stat-type-111 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Pitching_Runs = player_page.split('<td class="mlb-stat-type-113 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Earned_Runs = player_page.split('<td class="mlb-stat-type-114 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Pitching_Home_Runs = player_page.split('<td class="mlb-stat-type-115 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Pitching_Bases_On_Balls = player_page.split('<td class="mlb-stat-type-118 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Pitching_Strikeouts = player_page.split('<td class="mlb-stat-type-121 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Earned_Runs_Average = player_page.split('<td class="mlb-stat-type-140 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Walks_Plus_Hits_Per_Inning_Pitched = player_page.split('<td class="mlb-stat-type-141 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Batting_Average_Against = player_page.split('<td class="mlb-stat-type-142 stat-total')[1].split('</td>')[0].split('>')[1]
    except:
        Pitching_Games = 0
        Pitching_Games_Started = 0
        Wins = 0
        Losses = 0
        Saves = 0
        Blown_Saves = 0
        Holds = 0
        Complete_Games = 0
        Shutouts = 0
        Innings_Pitched = 0
        Pitching_Hits = 0
        Pitching_Runs = 0
        Earned_Runs= 0
        Pitching_Home_Runs = 0
        Pitching_Bases_On_Balls = 0
        Pitching_Strikeouts = 0
        Earned_Runs_Average = 0
        Walks_Plus_Hits_Per_Inning_Pitched = 0
        Batting_Average_Against = 0


    '''
    print('--------PITCHING------------')
    print('G', Pitching_Games)
    print('GS', Pitching_Games_Started)
    print('W', Wins)
    print('L', Losses)
    print('SV', Saves)
    print('BS', Blown_Saves)
    print('HLD', Holds)
    print('CG', Complete_Games)
    print('SHO', Shutouts)
    print('IP', Innings_Pitched)
    print('H', Pitching_Hits)
    print('R', Pitching_Runs)
    print('ER', Earned_Runs)
    print('HR', Pitching_Home_Runs)
    print('BB', Pitching_Bases_On_Balls)
    print('K', Pitching_Strikeouts)
    print('ERA', Earned_Runs_Average)
    print('WHIP', Walks_Plus_Hits_Per_Inning_Pitched)
    print('BAA', Batting_Average_Against)
    print('--------------------------------')
    '''


    # FIELDING ---------------------------------------------------------------------------------------------------------
    try:
        Fielding_Games = player_page.split('<td class="mlb-stat-type-201 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Position = player_page.split('<td class="mlb-stat-type-219 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Fielding_Games_Started = player_page.split('<td class="mlb-stat-type-212 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Innings = player_page.split('<td class="mlb-stat-type-217 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Putouts = player_page.split('<td class="mlb-stat-type-204 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Total_Chance = player_page.split('<td class="mlb-stat-type-213 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Assists = player_page.split('<td class="mlb-stat-type-205 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Errors = player_page.split('<td class="mlb-stat-type-206 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Double_Plays = player_page.split('<td class="mlb-stat-type-207 stat-total')[1].split('</td>')[0].split('>')[1]
        time.sleep(sleeper)
        Fielding = player_page.split('<td class="mlb-stat-type-218 stat-total')[1].split('</td>')[0].split('>')[1]
    except:
        Fielding_Games = 0
        Position = 'N/A'
        Fielding_Games_Started = 0
        Innings = 0
        Putouts = 0
        Total_Chance = 0
        Assists = 0
        Errors = 0
        Double_Plays = 0
        Fielding = 0


    '''
    print('----------Fielding-----------')
    print('G', Fielding_Games)
    print('GS', Position)
    print('W', Fielding_Games_Started)
    print('L', Innings)
    print('SV', Putouts)
    print('BS', Total_Chance)
    print('HLD', Assists)
    print('CG', Errors)
    print('SHO', Double_Plays)
    print('IP', Fielding)
    print('--------------------------------')
    '''

    df = df.append({'Team': tname,
                    'ID': round(int(id)),
                    'Batting_Games': Batting_Games,
                    'At_Bats': At_Bats,
                    'Batting_Runs': Batting_Runs,
                    'Batting_Hits': Batting_Hits,
                    'Doubles': Doubles,
                    'Triples': Triples,
                    'Batting_Home_Runs': Batting_Home_Runs,
                    'Runs_Batted_In': Runs_Batted_In,
                    'Batting_Bases_On_Balls': Batting_Bases_On_Balls,
                    'Batting_Strike_Outs': Batting_Strike_Outs,
                    'Stolen_Bases': Stolen_Bases,
                    'Caught_Stealing': Caught_Stealing,
                    'Batting_Average': Batting_Average,
                    'On_Base_Percentage': On_Base_Percentage,
                    'Slugging_Percentage': Slugging_Percentage,
                    'On_Base_Plus_Slugging': On_Base_Plus_Slugging,
                    'Pitching_Games': Pitching_Games,
                    'Pitching_Games_Started': Pitching_Games_Started,
                    'Wins': Wins,
                    'Losses': Losses,
                    'Saves': Saves,
                    'Blown_Saves': Blown_Saves,
                    'Holds': Holds,
                    'Complete_Games': Complete_Games,
                    'Shutouts': Shutouts,
                    'Innings_Pitched': Innings_Pitched,
                    'Pitching_Hits': Pitching_Hits,
                    'Pitching_Runs': Pitching_Runs,
                    'Earned_Runs': Earned_Runs,
                    'Pitching_Home_Runs': Pitching_Home_Runs,
                    'Pitching_Bases_On_Balls': Pitching_Bases_On_Balls,
                    'Pitching_Strikeouts': Pitching_Strikeouts,
                    'Earned_Runs_Average': Earned_Runs_Average,
                    'Walks_Plus_Hits_Per_Inning_Pitched': Walks_Plus_Hits_Per_Inning_Pitched,
                    'Batting_Average_Against': Batting_Average_Against,
                    'Fielding_Games': Fielding_Games,
                    'Position': Position,
                    'Fielding_Games_Started': Fielding_Games_Started,
                    'Innings': Innings,
                    'Putouts': Putouts,
                    'Total_Chance': Total_Chance,
                    'Assists': Assists,
                    'Errors': Errors,
                    'Double_Plays': Double_Plays,
                    'Fielding': Fielding,
                    }, ignore_index=True)

    return df


def get_team(team):    
    ''' Gets the information on the team! '''

    global counter
    counter = 0
    delta_split = 'class="athlete" scope="row"><a href="/mlb/players/'
    url = 'http://sports.yahoo.com/mlb/teams/' + team + '/stats/'
    response = request.urlopen(url)
    team_page = str(response.read())
    ID = team_page.split(delta_split)[1].split('/"')[0]
    DaFr = get_players(ID)
    while True:
        try:
            ID = team_page.split(delta_split + ID)[1].split(delta_split)[1].split('/"')[0]
            players = get_players(ID)
            DaFr = DaFr.append(players, ignore_index=True)
            counter += 1
            print('Player', counter)
        except:
            return DaFr


def get_league():
    ''' Gets the information on the whole league!'''

    global tname

    tname = 'tam'
    print('-----------')
    print('Team:', tname, '|')
    print('-----------')
    data = get_team(tname)

    for each_team in Team:
        tname = each_team

        print('-----------')
        print('Team:', tname, '|')
        print('-----------')

        append_data = get_team(tname)
        data = data.append(append_data, ignore_index=True)

        save = 'BaseBall.csv'
        data.to_csv(save)

    return data


if __name__ == '__main__':
    main()
