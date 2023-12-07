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

total_powers = 0
for game_id, rolls in games.items():
    minimum_dice = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }
    for roll in rolls:
        for color, number in roll.items():
            if number > minimum_dice[color]:
                minimum_dice[color] = number
    power = minimum_dice['red'] * minimum_dice['green'] * minimum_dice['blue']
    total_powers += power
print(total_powers)
