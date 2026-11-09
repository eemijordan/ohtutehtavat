import unittest
from statistics_service import StatisticsService
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_returns_existing_player(self):
        player = self.stats.search("Kurri")

        self.assertEqual(player.name, "Kurri")
        self.assertEqual(player.team, "EDM")

    def test_search_returns_none_if_player_not_found(self):
        self.assertIsNone(self.stats.search("Selanne"))

    def test_team_returns_players_of_given_team(self):
        players = self.stats.team("EDM")
        names = [player.name for player in players]

        self.assertEqual(names, ["Semenko", "Kurri", "Gretzky"])

    def test_team_returns_empty_list_for_unknown_team(self):
        self.assertEqual(self.stats.team("XXX"), [])

    def test_top_returns_players_in_points_order(self):
        top_players = self.stats.top(3)
        names = [player.name for player in top_players[:3]]

        self.assertEqual(names, ["Gretzky", "Lemieux", "Yzerman"])