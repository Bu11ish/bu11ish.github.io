import math
import random

from pprint import pprint

INF = float('inf')


def get_win_probability(skill_difference):
    """Estimate the outcome of a heads-up confrontation between two players.

    In this model, one point of skill difference roughly converts to a 1% edge,
    up to a maximum of 30% edge.

    Examples:
    - Same skills -> 50% win chance
    - Skill 102 vs Skill 100 -> 52% win chance
    - Skill 500 vs Skill 3800 -> 20% win chance (the minimum)
    """
    return (math.atan(skill_difference / 20) * 0.6 / math.pi) + 0.5


class Player:
    def __init__(self, player_id, skill=None):
        self.id = player_id
        self.skill = skill if skill is not None else player_id
        self.elo = 100

    def __hash__(self):
        return self.id

    def __repr__(self):
        return f'<Player #{self.id} ELO:{round(self.elo, 2)}>'


class Tournament:
    def __init__(self, players):
        if not players:
            raise ValueError('Tournament must have at least 1 player')

        self.chip_count = {player: 100 for player in players}
        self.prize_pool = 0
        self.multiplier = 2 ** len(players)

    def run(self):
        while len(self.chip_count) > 1:
            self.play_hand()

        winner, _ = self.chip_count.popitem()
        self.bust(winner)

    def bust(self, player):
        """Update player ELO and tournament prize pool on elimination."""
        self.chip_count.pop(player, None)

        buy_in = player.elo * 0.1
        player.elo += ((self.prize_pool + 2 * buy_in) / self.multiplier) - buy_in
        self.prize_pool += buy_in
        self.multiplier //= 2

    def play_hand(self):
        """Pick two random players and make them bet a random number of chips."""
        player1, player2 = random.sample(list(self.chip_count), 2)
        p1_win_prob = get_win_probability(player1.skill - player2.skill)
        winner, loser = (
            (player1, player2) if random.random() < p1_win_prob
            else (player2, player1)
        )

        bet_size = random.randint(1, 100)
        bet_size = min(bet_size, self.chip_count[player1], self.chip_count[player2])

        self.chip_count[winner] += bet_size

        if self.chip_count[loser] <= bet_size:
            self.bust(loser)
        else:
            self.chip_count[loser] -= bet_size


class Season:
    def __init__(self, nb_players=20):
        self.players = [Player(player_id) for player_id in range(nb_players)]
        self.nb_tournaments_played = 0

    def run(self):
        for _ in range(20000):
            self.run_tournament()

        # Check stability
        for _ in range(5):
            for _ in range(200):
                self.run_tournament()

            print(f'After {self.nb_tournaments_played} tournaments:')
            pprint(self.get_leaderboard())
            print()

    def get_leaderboard(self):
        return sorted(self.players, key=lambda p: p.elo, reverse=True)

    def run_tournament(self):
        """Pick players at random and match them."""
        nb_players = random.randint(4, 8)
        players = random.sample(self.players, nb_players)

        Tournament(players).run()
        self.nb_tournaments_played += 1


if __name__ == '__main__':
    season = Season()
    season.run()
    players = season.players[:6]
