outcome_score = {
    'X': {
        'A': 3,
        'B': 0,
        'C': 6
    },
    'Y': {
        'A': 6,
        'B': 3,
        'C': 0
    },
    'Z': {
        'A': 0,
        'B': 6,
        'C': 3
    }
}
move_score = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

losing_move = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}

winning_move = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}

draw_move = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

outcome_strategy = {
    'X': losing_move,
    'Y': draw_move,
    'Z': winning_move
}


def strategy_score():
    total_score = 0
    with open('inputs/day2.txt') as sf:
        for line in sf.readlines():
            op_move, my_move = line.strip().split()
            total_score += move_score[my_move] + outcome_score[my_move][op_move]
    return total_score


def win_los_strategy_score():
    total_score = 0
    with open('inputs/day2.txt') as sf:
        for line in sf.readlines():
            op_move, outcome = line.strip().split()
            my_move = outcome_strategy[outcome][op_move]
            total_score += move_score[my_move] + outcome_score[my_move][op_move]
    return total_score


print('part 1', strategy_score())
print('part 2', win_los_strategy_score())
