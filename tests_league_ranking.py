import unittest
from league_ranking import calculate_league_ranking

class TestLeagueRanking(unittest.TestCase):
    def test_sample_input(self):
        input_lines = [
            "Lions 3, Snakes 3",
            "Tarantulas 1, FC Awesome 0",
            "Lions 1, FC Awesome 1",
            "Tarantulas 3, Snakes 1",
            "Lions 4, Grouches 0",
        ]
        expected_output = (
            "1. Tarantulas, 6 pts\n"
            "2. Lions, 5 pts\n"
            "3. FC Awesome, 1 pt\n"
            "3. Snakes, 1 pt\n"
            "5. Grouches, 0 pts"
        )
        self.assertEqual(calculate_league_ranking(input_lines), expected_output)

    def test_all_draws(self):
        input_lines = [
            "Team A 1, Team B 1",
            "Team C 2, Team D 2",
            "Team C 2, Team D 2",
            "Team C 2, Team D 2",
            "Team C 2, Team D 2",
        ]
        expected_output = (
            "1. Team A, 1 pt\n"
            "1. Team B, 1 pt\n"
            "1. Team C, 1 pt\n"
            "1. Team D, 1 pt"
        )
        self.assertEqual(calculate_league_ranking(input_lines), expected_output)

    def test_single_game(self):
        input_lines = [
            "Team X 3, Team Y 0",
        ]
        expected_output = (
            "1. Team X, 3 pts\n"
            "2. Team Y, 0 pts"
        )
        self.assertEqual(calculate_league_ranking(input_lines), expected_output)

    def test_empty_input(self):
        input_lines = []
        expected_output = ""
        self.assertEqual(calculate_league_ranking(input_lines), expected_output)

if __name__ == "__main__":
    unittest.main()
