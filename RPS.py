import random

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)
    
    moves = ["R", "P", "S"]
    
    if not opponent_history:
        return random.choice(moves)
    
    n = 3
    if len(opponent_history) >= n:
        recent_pattern = ''.join(opponent_history[-n:])
        
        pattern_counts = {"R": 0, "P": 0, "S": 0}
        for i in range(len(opponent_history) - n):
            if ''.join(opponent_history[i:i+n]) == recent_pattern:
                next_move = opponent_history[i+n]
                pattern_counts[next_move] += 1
        
        predicted_move = max(pattern_counts, key=pattern_counts.get)
        
        if predicted_move == "R":
            return "P"
        elif predicted_move == "P":
            return "S"
        else:
            return "R"
    
    return random.choice(moves)