class TeamGame:
    def __init__(self, teamId, gameId):
        self.espnTeamId = str(teamId)
        self.espnGameId = str(gameId)
        self.possessionPercent = "-1"
        self.shots = "-1"
        self.shotsOnTarget = "-1"
        self.yellowCards = "-1"
        self.redCards = "-1"
        self.fouls = "-1"
        self.offsides = "-1"
        self.corners = "-1"
        self.saves = "-1"


    # Getters ################
    def getEspnTeamId(self):
        return self.espnTeamId

    def getEspnGameId(self):
        return self.espnGameId

    def getPossessionPercent(self):
        return self.possessionPercent

    def getShots(self):
        return self.shots

    def getShotsOnTarget(self):
        return self.shotsOnTarget

    def getYellowCards(self):
        return self.yellowCards

    def getRedCards(self):
        return self.redCards

    def getFouls(self):
        return self.fouls

    def getOffsides(self):
        return self.offsides
    
    def getCorners(self):
        return self.corners

    def getSaves(self):
        return self.saves

    # Setters #################
    def setPossessionPercent(self, possessionPercent):
        self.possessionPercent = str(possessionPercent)

    def setShots(self, shots):
        self.shots = str(shots)
    
    def setShotsOnTarget(self, shotsOnTarget):
        self.shotsOnTarget = str(shotsOnTarget)

    def setYellowCards(self, yellowCards):
        self.yellowCards = str(yellowCards)

    def setRedCards(self, redCards):
        self.redCards = str(redCards)

    def setFouls(self, fouls):
        self.fouls = str(fouls)

    def setOffsides(self, offsides):
        self.offsides = str(offsides)

    def setCorners(self, corners):
        self.corners = str(corners)

    def setSaves(self, saves):
        self.saves = str(saves)

    def toString(self):
        return ("team id: " + self.getEspnTeamId()
        + "\npossession percent: " + self.getPossessionPercent()
        + "\nshots: " + self.getShots()
        + "\nshots on target: " + self.getShotsOnTarget()
        + "\nyellow cards: " + self.getYellowCards()
        + "\nred cards: " + self.getRedCards()
        + "\nfouls: " + self.getFouls()
        + "\noffsides: " + self.getOffsides()
        + "\ncorners: " + self.getCorners()
        + "\nsaves: " + self.getSaves())