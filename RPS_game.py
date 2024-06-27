import random

def play(player1, player2, num_games, verbose=False):
    p1_score = 0
    p2_score = 0
    p1_prev_play = ""
    p2_prev_play = ""
    
    for _ in range(num_games):
        p1_play = player1(p2_prev_play)
        p2_play = player2(p1_prev_play)
        
        if p1_play == "R":
            if p2_play == "S":
                p1_score += 1
            elif p2_play == "P":
                p2_score += 1
        elif p1_play == "P":
            if p2_play == "R":
                p1_score += 1
            elif p2_play == "S":
                p2_score += 1
        elif p1_play == "S":
            if p2_play == "P":
                p1_score += 1
            elif p2_play == "R":
                p2_score += 1
        
        p1_prev_play = p1_play
        p2_prev_play = p2_play
        
        if verbose:
            print(f"Player 1: {p1_play}, Player 2: {p2_play}, Score: {p1_score}-{p2_score}")
    
    return p1_score, p2_score

def quincy(prev_play, opponent_history=[]):
    return "P"

def mrugesh(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)
    
    return "R"

def kris(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)
    
    return "S"

def abbey(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)
    
    return random.choice(["R", "P", "S"])
