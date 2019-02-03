class TeamGameDao:

    addTeamGameInsert = ("INSERT INTO TeamGame "
                        "(EspnTeamId, EspnGameId, PossessionPercent, Shots, ShotsOnTarget, YellowCards, RedCards, Fouls, Offsides, Corners, Saves) "
                        "VALUES (%(espnTeamId)s, %(espnGameId)s, %(possessionPercent)s, %(shots)s, %(shotsOnTarget)s, %(yellowCards)s, %(redCards)s, %(fouls)s, %(offsides)s, %(corners)s, %(saves)s)")

    existingTeamGameQuery = ("SELECT COUNT(*) "
                            "FROM TeamGame "
                            "WHERE EspnTeamId = %(espnTeamId)s "
                                "AND EspnGameId = %(espnGameId)s")

    def insertTeamGame(teamGame, databaseConnector):
        dbConnection = databaseConnector.retrieveDbConnection()
        cursor = dbConnection.cursor()
        print("Running Insert New Team Game: " )
        print(teamGame.__dict__)
        print("--------------------")
        try:
            cursor.execute(TeamGameDao.addTeamGameInsert, teamGame.__dict__)
            dbConnection.commit()
        except:
            print("ERROR-------------------")
            print(cursor.statement)
            print("-----------------------")
            raise
        cursor.close()
    
    def checkIfTeamGameExists(teamGame, databaseConnector):
        dbConnection = databaseConnector.retrieveDbConnection()
        cursor = dbConnection.cursor()
        print("Checking if teamGame exists: " + teamGame.getEspnTeamId() + " - " + teamGame.getEspnGameId())
        cursor.execute(TeamGameDao.existingTeamGameQuery, teamGame.__dict__)
        teamGameCount = cursor.fetchone()[0]
        print("TeamGames found: " + str(teamGameCount))
        return teamGameCount > 0