from configobj import ConfigObj
import operator

config = ConfigObj('../test_team.ini')
result =  config["Result"]
team_list = config["Team"]

team_table = {}
for team in team_list:
    team_table[team] = 0

def check_score(teamA,teamB):
    if(teamA == teamB):
        return (1,1)
    else:
        if(teamA > teamB):
            return (3,0)
        elif (teamA < teamB):
            return (0,3)




if __name__ == '__main__':
    
    for team_home in team_list:
        for team_away in team_list:
            if(not(team_home is team_away)):
                # print team_home + " vs " + team_away + "score : " + result[team_home][team_away]
                score1 = team_table[team_home]
                score2 = team_table[team_away]
                
                score_team_home = int(result[team_home][team_away].split("-")[0])
                score_team_away = int(result[team_home][team_away].split("-")[1])

                score_temp_home,score_temp_away = check_score(score_team_home,score_team_away)
                score1 = score1 + score_temp_home
                score2 = score2 + score_temp_away

                # print type(score1)

                team_table[team_home] = score1
                team_table[team_away] = score2
    
    team_table_sorted = sorted(team_table.items(),key=operator.itemgetter(1))    
    
    
    for i in list(reversed(range(4))):
        print "Team : " + team_table_sorted[i][0] + " : " + str(team_table_sorted[i][1])