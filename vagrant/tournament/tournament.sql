-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- Drop the database if it already exists - otherwise create and connect to the database
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;

\c tournament;

-- Create tables in the database
CREATE TABLE players (id SERIAL primary key,
                      name TEXT);

CREATE TABLE matches (id SERIAL primary key,
                      winner INTEGER REFERENCES players (id),
                      loser INTEGER REFERENCES players (id));

-- Create a standings view for the Swiss-system tournament

CREATE VIEW standings AS
SELECT players.id, players.name, count(matches.winner) as wins,
  count(matches.winner) + count(matches2.loser) as total_matches
FROM players
LEFT JOIN matches on players.id = matches.winner
LEFT JOIN matches as matches2 on players.id = matches2.loser
GROUP BY players.id, players.name
ORDER BY wins DESC;
