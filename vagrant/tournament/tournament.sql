-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
CREATE DATABASE tournament;

\c tournament;

CREATE TABLE players (id SERIAL primary key,
                      name TEXT);

CREATE TABLE matches (id SERIAL primary key,
                      winner INTEGER REFERENCES players (id),
                      loser INTEGER REFERENCES players (id));

CREATE VIEW standings AS
SELECT players.id, players.name, count(matches.winner) as wins,
  count(matches.winner) + count(matches2.loser) as total_matches
FROM players
LEFT JOIN matches on players.id = matches.winner
LEFT JOIN matches as matches2 on players.id = matches2.loser
GROUP BY players.id, players.name
ORDER BY wins DESC;
