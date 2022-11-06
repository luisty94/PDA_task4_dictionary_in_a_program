def get_game_store_name(game_store):
    return game_store["name"]

def get_games_by_genre(game_store, genre):
    found_games = []
    games = game_store["games"]
    for game in games:
        if game["genre"] == genre:
            found_games.append(game)

    return found_games