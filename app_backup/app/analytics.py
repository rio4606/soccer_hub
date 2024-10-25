from collections import Counter

def team_performance_statistics(matches):
    """Анализирует результаты матчей команды и возвращает статистику"""
    wins = sum(1 for match in matches if match["result"] == "win")
    losses = sum(1 for match in matches if match["result"] == "loss")
    draws = sum(1 for match in matches if match["result"] == "draw")
    
    return {
        "wins": wins,
        "losses": losses,
        "draws": draws
    }


def top_scorers(players):
    """Возвращает список лучших бомбардиров"""
    scores = Counter({player["name"]: player["goals"] for player in players})
    return scores.most_common(5)
