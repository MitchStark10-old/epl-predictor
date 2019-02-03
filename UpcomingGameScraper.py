#Allow model package imports
import sys
sys.path.append('..')

#Imports
import urllib.request as urllib2
from bs4 import BeautifulSoup
from model.Game import Game
from dao.GameDao import GameDao

def retrieveUpcomingGame(espnId, databaseConnector):
    response = urllib2.urlopen('http://www.espn.com/soccer/team/fixtures/_/id/' + str(espnId) + '/league/ENG.1')
    baseHtml = response.read()
    soup = BeautifulSoup(baseHtml, 'html.parser')
    firstUpcomingGame = soup.find("tr", {"class": "Table2__tr Table2__tr--sm Table2__even"})
    dataList = firstUpcomingGame.findAll("td", {"class": "Table2__td"})

    newGame = Game()
    for index, value in enumerate(dataList):
        if index == 0:
            newGame.setDate(value.contents[0].contents[0])
        elif index == 1:
            newGame.setHomeTeam(value.contents[0].contents[0].contents[0])
            newGame.setHomeTeamId(value.contents[0].contents[0]['href'].replace('/soccer/team/_/id/', ''))
        elif index == 3:
            newGame.setAwayTeam(value.contents[0].contents[0].contents[0])
            newGame.setAwayTeamId(value.contents[0].contents[0]['href'].replace('/soccer/team/_/id/', ''))
        elif index == 4:
            newGame.setEspnGameId(value.contents[0]['href'].replace('http://www.espnfc.com/match/_/gameId/', ''))
        elif index == 5:
            newGame.setCompetition(value.contents[0].contents[0])
    print(newGame.toString())

    if not GameDao.checkIfGameExists(newGame, databaseConnector):
        GameDao.insertNewGame(newGame, databaseConnector)
        print("\n\n\n")


