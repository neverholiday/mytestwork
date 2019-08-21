#!/usr/bin/env python
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

def createOneColorDictionary( ):

    colorDict = {
        'H_max' : 0,
        'H_min' : 0,
        'S_max' : 0,
        'S_min' : 0,
        'V_max' : 0,
        'V_min' : 0
    }

    return colorDict

def createColorMultiColorDictionary( colorKeyList ):

    colorConfigDict = dict()

    for i,color in enumerate( colorKeyList ):
        
        colorDict = createOneColorDictionary()
        
        colorConfigDict[ color ] = colorDict
    
    return colorConfigDict

def createConfigObject( colorConfigDict ):

    config = ConfigObj( colorConfigDict )

    return config

def saveConfig( path, configInstance ):

    with open( path, 'w' ) as outputFile:

        configInstance.write( outputFile )
    



if __name__ == '__main__':
    
    colorKeyList = [ 'OrangeColorParameter', 'FieldGreenColorParameter', 'BlueColorParameter', 'YellowColorParameter', 'WhiteColorParameter', 'BlackColorParameter' ]

    colorConfig = createColorMultiColorDictionary( colorKeyList )

    config = createConfigObject( colorConfig )

    saveConfig( '/tmpfs/config.ini', config )