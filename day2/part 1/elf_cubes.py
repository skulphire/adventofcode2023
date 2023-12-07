with open('input.txt') as f:
    lines = f.readlines()

rolls = {
    'red': 0,
    'green': 0,
    'blue': 0,
}


def format_data():
    games = {}
    game_count = 1
    for line in lines:
        line = line.strip()
        game = line.split(':')
        raw_rolls = game[1].split(';')
        game_rolls = []
        for roll in raw_rolls:
            dice = roll.split(',')
            new_roll = rolls.copy()
            for d in dice:
                color = d.split(' ')[2]
                number = d.split(' ')[1]
                new_roll[color] = int(number)
            game_rolls.append(new_roll)
        games[game_count] = game_rolls
        game_count += 1

    return games


games = format_data()


def check_dice_max(roll):
    if roll['red'] > 12:
        return False
    if roll['green'] > 13:
        return False
    if roll['blue'] > 14:
        return False
    return True


total_ids = 0
for game_id, rolls in games.items():
    possible_count = 0
    for roll in rolls:
        if check_dice_max(roll):
            possible_count += 1
    if possible_count == len(rolls):
        total_ids += game_id
        print(game_id, rolls)
print(total_ids)
