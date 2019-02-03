class TeamDao:

    addTeamInsert = ("INSERT INTO Team "
                    "(EspnId, TeamName, Place, Points, Wins, Ties, Losses, GamesPlayed, GoalsFor, GoalsAgainst) "
                    "VALUES (%(espnId)s, %(name)s, %(place)s, %(points)s, %(wins)s, %(ties)s, %(losses)s, %(gamesPlayed)s, %(goalsFor)s, %(goalsAgainst)s)")

    updateTeamQuery = ("UPDATE Team "
                        "SET TeamName = %(name)s, Place = %(place)s, Points = %(points)s, Wins = %(wins)s, Ties = %(ties)s, "
                            "Losses = %(losses)s, GamesPlayed = %(gamesPlayed)s, GoalsFor = %(goalsFor)s, GoalsAgainst = %(goalsAgainst)s "
                        "WHERE EspnId = %(espnId)s")

    existingTeamQuery = ("SELECT COUNT(*) FROM Team WHERE EspnId = %(espnId)s")

    def insertNewTeam(team, databaseConnector):
        dbConnection = databaseConnector.retrieveDbConnection()
        cursor = dbConnection.cursor()
        print("Running Insert New Team: ")
        print(team.__dict__)
        print ("--------------------")
        cursor.execute(TeamDao.addTeamInsert, team.__dict__)
        dbConnection.commit()
        cursor.close()

    def updateTeam(team, databaseConnector):
        dbConnection = databaseConnector.retrieveDbConnection()
        cursor = dbConnection.cursor()
        print("Running Update Team")
        print(team.__dict__)
        print("--------------------")
        try:
            cursor.execute(TeamDao.updateTeamQuery, team.__dict__)
            dbConnection.commit()
        except:
            print("ERROR---------------------")
            print(cursor.statement)
            print("---------------------------")
            raise
        cursor.close()

    def checkIfTeamExists(team, databaseConnector):
        dbConnection = databaseConnector.retrieveDbConnection()
        cursor = dbConnection.cursor()
        print("Checking if team: " + team.getEspnId() + " exists")
        cursor.execute(TeamDao.existingTeamQuery, team.__dict__)
        teamCount = cursor.fetchone()[0]
        print("Teams with id: " + str(team.getEspnId()) + ": " + str(teamCount))
        return teamCount > 0
