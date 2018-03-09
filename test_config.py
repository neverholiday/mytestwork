from configobj import ConfigObj

def createConfig(path,team):
    config = ConfigObj()
    config.filename = path
    config['Result'] = {}
    config['Result'][team[0]] = {team[1]:"2-0",team[2]:"2-3",team[3]:"4-2"}
    config['Result'][team[1]] = {team[0]:"2-3",team[2]:"1-0",team[3]:"8-0"}
    config['Result'][team[2]] = {team[0]:"2-0",team[1]:"2-3",team[3]:"4-2"}
    config['Result'][team[3]] = {team[0]:"2-3",team[1]:"1-0",team[2]:"8-0"}
    config.write()



if __name__ == '__main__':
    config = ConfigObj('test_team.ini')
    print config["Result"]["Denmark"]