#TODO: Call Upcoming Game Scraper, get all upcoming games
#TODO: Generate classes for each stat classes


#Allow model package imports
import sys
import re
sys.path.append('..')

#imports
import urllib.request as urllib2
from bs4 import BeautifulSoup
from model.Team import Team
import UpcomingGameScraper
from dao.TeamDao import TeamDao
from utilities.DatabaseConnection import DatabaseConnection

#Setup beautiful soup
response = urllib2.urlopen('http://www.espn.com/soccer/table/_/league/eng.1')
baseHtml = response.read()
soup = BeautifulSoup(baseHtml, 'html.parser')

teams = []

#Get list of standing rows
teamNameList = soup.findAll("td", {"class": "Table2__td"})

#Database connection
databaseConnector = DatabaseConnection()

for teamName in teamNameList:
	abbreviation = teamName.find("abbr")
	if (abbreviation is not None):
		href = teamName.find("a", href=True)['href']
		newTeam = Team()
		newTeam.setName(abbreviation['title'])
		newTeam.setEspnId(href.replace('/soccer/team/_/id/', ''))
		teams.append(newTeam)
		if not TeamDao.checkIfTeamExists(newTeam, databaseConnector):
			TeamDao.insertNewTeam(newTeam, databaseConnector)

mainTable = soup.findAll("tbody", {"class": "Table2__tbody"})[1]
statsRowList = mainTable.findAll("tr", {"class": re.compile(".*Table2__tr Table2__tr--sm Table2__even")})

for teamIndex, statsRow in enumerate(statsRowList):
		statsList = statsRow.findAll("td", {"class": "Table2__td"})
		for index, stat in enumerate(statsList):
				teams[teamIndex].setValueFromIndex(index, stat.contents[0].contents[0])
		teams[teamIndex].setPlace(teamIndex + 1)

print("here-------------------")
for index, team in enumerate(teams):
	if index == 0:
		print(team.toString())
		print('--------------------')
		UpcomingGameScraper.retrieveUpcomingGame(team.getEspnId(), databaseConnector)
		#TODO: Only add to database when ready
		# if not GameDao.checkIfGameExists(newGame, databaseConnector):
		#         GameDao.insertNewGame(newGame, databaseConnector)
		#         print("\n\n\n")