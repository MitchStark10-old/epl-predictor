#TODO: Import date
import sys
import re
sys.path.append('..')

from utilities.Date import Date

class Game:
    def __init__(self):
        self.date = ''
        self.homeTeamId = -1
        self.awayTeamId = -1
        self.homeTeamScore = -1
        self.awayTeamScore = -1
        self.predictedHomeTeamScore = -1
        self.predictedAwayTeamScore = -1
        self.espnGameId = -1
        self.competition = ''

    ###### Setters #######
    def setDate(self, date):
        #Format example: Wed, Oct 24
        print("Attempting to parse: " + date)
        initialDateString = str(date)
        matches = re.search("\w{3}, (\w{3}) (\d{1,2})", initialDateString)
        if matches is None:
            #Good old ESPN with some inconsistent software. Sometimes
            #the date returned is in the format Wed, 24 Oct
            matches = re.search("\w{3}, (\d{1,2}) (\w{3}", initialDateString)
            if matches is None:
                print("Error with date: " + date)
            else:
                month = matches[2]
                day = matches[1]
                year = Date.determineYear(month, day)
                self.date = str(year + "-" + month + "-" + day)
        else:
            month = matches[1]
            day = matches[2]
            year = Date.determineYear(month, day)
            self.date = str(year + "-" + month + "-" + day)
    
    def setHomeTeam(self, homeTeam):
        self.homeTeam = str(homeTeam)

    def setAwayTeam(self, awayTeam):
        self.awayTeam = str(awayTeam)

    def setHomeTeamScore(self, homeTeamScore):
        self.homeTeamScore = str(homeTeamScore)

    def setAwayTeamScore(self, awayTeamScore):
        self.awayTeamScore = str(awayTeamScore)

    def setPredictedHomeTeamScore(self, predictedHomeTeamScore):
        self.predictedHomeTeamScore = str(predictedHomeTeamScore)
    
    def setPredictedAwayTeamScore(self, predictedAwayTeamScore):
        self.predictedAwayTeamScore = str(predictedAwayTeamScore)

    def setEspnGameId(self, espnGameId):
        self.espnGameId = str(espnGameId)
    
    def setCompetition(self, competition):
        self.competition = str(competition)

    def setHomeTeamId(self, homeTeamId):
        self.homeTeamId = str(homeTeamId)

    def setAwayTeamId(self, awayTeamId):
        self.awayTeamId = str(awayTeamId)

    def setValueFromIndex(self, index, value):
        if index == 0:
            self.setDate(value.contents[0])
        elif index == 1:
            self.setHomeTeamId(value.contents[0]['href'].replace('/soccer/team/_/id/', ''))
            self.setHomeTeam(value.contents[0].contents[0])
        elif index == 2:
            #Score is in format: homeTeamGoals - awayTeamGoals
            scoreString = str(value.findAll("a")[1].contents[0])
            scoreArray = scoreString.split(" - ")
            self.setHomeTeamScore(scoreArray[0])
            self.setAwayTeamScore(scoreArray[1])
        elif index == 3:
            self.setAwayTeamId(value.contents[0]['href'].replace('/soccer/team/_/id/', ''))
            self.setAwayTeam(value.contents[0].contents[0])
        elif index == 4:
            gameHref = value.findAll("a", href=True)[0]['href']
            gameId = gameHref.replace('http://www.espnfc.com/match/_/gameId/', '')
            self.setEspnGameId(gameId)
        elif index == 5:
            self.setCompetition(value.contents[0])
        else:
            raise ValueError('Received unexpected value to set index for:', index, str(value))


    ####### Getters ######

    def getDate(self):
        return self.date   

    def getHomeTeam(self):
        return self.homeTeam

    def getAwayTeam(self):
        return self.awayTeam

    def getHomeTeamScore(self):
        return self.homeTeamScore

    def getAwayTeamScore(self):
        return self.awayTeamScore

    def getPredictedHomeTeamScore(self):
        return self.predictedHomeTeamScore
    
    def getPredictedAwayTeamScore(self):
        return self.predictedAwayTeamScore

    def getEspnGameId(self):
        return self.espnGameId

    def getCompetition(self):
        return self.competition

    def getHomeTeamId(self):
        return self.homeTeamId

    def getAwayTeamId(self):
        return self.awayTeamId

    def toString(self):
        return ("date: " + str(self.getDate())
        + "\nespnGameId: " + str(self.getEspnGameId())
        + "\nhomeTeam: " + str(self.getHomeTeam()) + " (" + str(self.getHomeTeamId()) + ")"
        + "\nawayTeam: " + str(self.getAwayTeam()) + " (" + str(self.getAwayTeamId()) + ")"
        + "\nactual score: " + str(self.getHomeTeamScore()) + "-" + str(self.getAwayTeamScore())
        + "\npredicted score: " + str(self.getPredictedHomeTeamScore()) + "-" + str(self.getPredictedAwayTeamScore())
        + "\ncompetition: " + str(self.getCompetition()))