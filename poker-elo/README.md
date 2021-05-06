# Proposed Poker Elo Calculation

## Goal

Points reflect skill, not just grinding

Points only reflect skill after playing for a few games

Skill reflects how a player would do in real life poker tournaments

## Start

Every player starts the season with 100 points

Each game has a buy-in equal to 10% of the player's current points

## Point Distribution

The player who finishes first recieves all his points back, plus 1/2 of everyone who finished below him's points; The player who finishes second recieves 1/2 of his points back, plus 1/4 of everyone who finished below him's points; and so on...

Formula 

`P = B + 2^R * E`

Where

P: points a player recives

B: the player's initial buy-in

R: the player's placement in the game

E: the total points of every one else who finished below the player

## Demo

Will build later
