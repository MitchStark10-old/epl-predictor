class Team: 

    def __init__(self):
        self.name = ''
        self.place = -1
        self.points = -1
        self.wins = -1
        self.ties = -1
        self.losses = -1
        self.gamesPlayed = -1
        self.goalsFor = -1
        self.goalsAgainst = -1
        self.goalDifferential = -1
        self.espnId = -1

    def setName(self, name):
        self.name = str(name)

    def setPlace(self, place):
        self.place = str(place)

    def setPoints(self, points):
        self.points = str(points)
    
    def setWins(self, wins):
        self.wins = str(wins)

    def setTies(self, ties):
        self.ties = str(ties)

    def setLosses(self, losses):
        self.losses = str(losses)
    
    def setGamesPlayed(self, gamesPlayed):
        self.gamesPlayed = str(gamesPlayed)

    def setGoalsFor(self, goalsFor):
        self.goalsFor = str(goalsFor)

    def setGoalsAgainst(self, goalsAgainst):
        self.goalsAgainst = str(goalsAgainst)

    def setGoalDifferential(self, goalDifferential):
        self.goalDifferential = str(goalDifferential.replace("+",""))

    def setEspnId(self, espnId):
        self.espnId = str(espnId)

    def getName(self):
        return self.name

    def getPlace(self):
        return self.place
    
    def getPoints(self):
        return self.points

    def getWins(self):
        return self.wins

    def getTies(self):
        return self.ties

    def getLosses(self):
        return self.losses

    def getGamesPlayed(self):
        return self.gamesPlayed

    def getGoalsFor(self):
        return self.goalsFor

    def getGoalsAgainst(self):
        return self.goalsAgainst

    def getGoalDifferential(self):
        return self.goalDifferential

    def getEspnId(self):
        return self.espnId

    #This sets a field based on the given index within the ESPN Table
    #Table located at: http://www.espn.com/soccer/table/_/league/eng.1
    #Indexes start at GP going until P
    def setValueFromIndex(self, index, value):
        if index == 0:
            self.setGamesPlayed(value)
        elif index == 1:
            self.setWins(value)
        elif index == 2:
            self.setTies(value)
        elif index == 3:
            self.setLosses(value)
        elif index == 4:
            self.setGoalsFor(value)
        elif index == 5:
            self.setGoalsAgainst(value)
        elif index == 6:
            self.setGoalDifferential(value)
        elif index == 7:
            self.setPoints(value)
        else:
            raise ValueError('Received unexpected value to set index for:', index)

    def toString(self):
        return str("Team: " + self.getName()
        + "\nplace: " + self.getPlace()
        + "\nwins: " + self.getWins()
        + "\nties: " + self.getTies()
        + "\nlosses: " + self.getLosses()
        + "\ngoalsFor: " + self.getGoalsFor()
        + "\ngoalsAgainst: " + self.getGoalsAgainst()
        + "\ngoalDifferential: " + self.getGoalDifferential()
        + "\npoints: " + self.getPoints()
        + "\nespnId: " + self.getEspnId()
        + "\n------------------------------")