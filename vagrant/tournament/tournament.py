#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def simpleTransaction(query):
    conn = connect()
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    conn.close()


def simpleInsert(query, arg):
    conn = connect()
    c = conn.cursor()
    c.execute(query, (arg,))
    conn.commit()
    conn.close()


def multipleInsert(query, arg1, arg2):
    conn = connect()
    c = conn.cursor()
    c.execute(query, (arg1, arg2,))
    conn.commit()
    conn.close()


def singleResultQuery(query):
    conn = connect()
    c = conn.cursor()
    c.execute(query)
    result = c.fetchone()
    c.close()
    conn.close()
    return result[0]


def multipleResultQuery(query):
    conn = connect()
    c = conn.cursor()
    c.execute(query)
    result = c.fetchall()
    c.close()
    conn.close()
    return result


def deleteMatches():
    """Remove all the match records from the database."""
    simpleTransaction("TRUNCATE matches CASCADE;")


def deletePlayers():
    """Remove all the player records from the database."""
    simpleTransaction("TRUNCATE players CASCADE;")


def countPlayers():
    """Returns the number of players currently registered."""
    return singleResultQuery("SELECT count(*) FROM players;")


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    return simpleInsert(("INSERT INTO players (name) VALUES (%s);"), name)

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    return multipleResultQuery("SELECT * from standings;")


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    return multipleInsert("INSERT INTO matches (winner, loser) VALUES (%s, %s);", winner, loser)


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = multipleResultQuery("SELECT id, name from standings;")

    """Determining the matches to be played according to players' rankings in the standings view.
    Iterating through the standings view 2 players at a time and returning their information."""

    pairs = []
    total_players = len(standings)
    for i in range(0, total_players, 2):
        pairs.append(standings[i] + standings[i+1])
    return pairs
