import unittest
from src.game_store import *

class TestGameStore(unittest.TestCase):
    def setUp(self):
        self.customers = [
            {
                "name": "Luis",
                "games": [],
                "cash": 150
            },
            {
                "name": "Marina",
                "games": [],
                "cash": 200
            },
            {
                "name": "WillyRex",
                "games": [],
                "cash": 175
            }
        ]

        self.games_in_store = {
            "games": [
                {
                    "name": "Palo",
                    "genre": "shooter",
                    "quality": "new",
                    "price": 75
                },
                {
                    "name": "NINFA",
                    "genre": "sports",
                    "quality": "2nd hand",
                    "price": 30
                },
                {
                    "name": "Heart Calibur",
                    "genre": "fight",
                    "quality": "new",
                    "price": 50
                },
                {
                    "name": "Call of Holydays",
                    "genre": "shooter",
                    "quality": "2d hand",
                    "price": 50
                },
        
            ],
            "admin": {
                "total_cash": 1000,
                "games_sold": 0,
            },
            "name": "GGameOver"
        }

    def test_game_store_name(self):
        name = get_game_store_name(self.games_in_store)
        self.assertEqual("GGameOver", name)
    
    def test_all_games_by_genre__found(self):
        games = get_games_by_genre(self.games_in_store, "shooter")
        self.assertEqual(2, len(games))
