with open("input.txt") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]
hands = {}
ranks = {}
for line in lines:
    hand = line.split(" ")[0]
    bid = line.split(" ")[1]
    hands[hand] = int(bid)
    ranks[hand] = 0

cards = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 1,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


def cards_to_numbers(hand):
    numbers = []
    for card in hand:
        numbers.append(cards[card])
    return numbers


def is_five_of_a_kind(hand):
    numbers = cards_to_numbers(hand)
    unique_numbers = set(numbers)
    if 1 in unique_numbers:
        unique_numbers.remove(1)
        if len(unique_numbers) == 0:
            return True
    if len(unique_numbers) == 1:
        return True
    return False


def is_four_of_a_kind(hand):
    numbers = cards_to_numbers(hand)
    unique_numbers = set(numbers)
    if 1 in unique_numbers:
        unique_numbers.remove(1)
    if len(unique_numbers) == 2:
        for number in unique_numbers:
            total_cards = numbers.count(number)
            if total_cards == 4:
                return True
            else:
                jokers = numbers.count(1)
                if total_cards + jokers == 4:
                    return True
    return False


def is_full_house(hand):
    numbers = cards_to_numbers(hand)
    unique_numbers = set(numbers)
    if 1 in unique_numbers:
        unique_numbers.remove(1)
    if len(unique_numbers) == 2:
        return True
    return False


def is_three_of_a_kind(hand):
    numbers = cards_to_numbers(hand)
    unique_numbers = set(numbers)
    if len(unique_numbers) >= 2:
        for number in unique_numbers:
            if numbers.count(number) == 3:
                return True
            else:
                jokers = numbers.count(1)
                if numbers.count(number) + jokers == 3:
                    return True
    return False


def is_two_pairs(hand):
    numbers = cards_to_numbers(hand)
    unique_numbers = set(numbers)
    if 1 in unique_numbers:
        unique_numbers.remove(1)
    pairs = 0
    if len(unique_numbers) == 3:
        for number in unique_numbers:
            if numbers.count(number) == 2:
                pairs += 1
            else:
                jokers = numbers.count(1)
                if numbers.count(number) + jokers == 2:
                    pairs += 1
        if pairs >= 2:
            return True
    return False


def is_one_pair(hand):
    numbers = cards_to_numbers(hand)
    unique_numbers = set(numbers)
    for number in unique_numbers:
        if numbers.count(number) == 2:
            return True
        else:
            jokers = numbers.count(1)
            if numbers.count(number) + jokers == 2:
                return True
    return False


def is_high_card(hand):
    numbers = cards_to_numbers(hand)
    unique_numbers = set(numbers)
    if len(unique_numbers) == 5:
        return True
    return False


def score_hands():
    scores = {
        7: [],
        6: [],
        5: [],
        4: [],
        3: [],
        2: [],
        1: []
    }
    arbitary_scores = {}
    for hand in hands:
        if is_five_of_a_kind(hand):
            scores[7].append(hand)
            arbitary_scores[hand] = 7000
        elif is_four_of_a_kind(hand):
            scores[6].append(hand)
            arbitary_scores[hand] = 6000
        elif is_full_house(hand):
            scores[5].append(hand)
            arbitary_scores[hand] = 5000
        elif is_three_of_a_kind(hand):
            scores[4].append(hand)
            arbitary_scores[hand] = 4000
        elif is_two_pairs(hand):
            print(hand)
            scores[3].append(hand)
            arbitary_scores[hand] = 3000
        elif is_one_pair(hand):
            scores[2].append(hand)
            arbitary_scores[hand] = 2000
        elif is_high_card(hand):
            scores[1].append(hand)
            arbitary_scores[hand] = 1000

    for score, scored_hands in scores.items():
        for h in scored_hands:
            selected_hand = cards_to_numbers(h)
            for h2 in scored_hands:
                current_hand = cards_to_numbers(h2)
                for i in range(5):
                    if selected_hand[i] > current_hand[i]:
                        arbitary_scores[h] += 1
                        break
                    elif selected_hand[i] < current_hand[i]:
                        arbitary_scores[h] -= 1
                        break
                    else:
                        continue

    sorted_scores = sorted(arbitary_scores.items(),
                           key=lambda kv: kv[1], reverse=True)
    print(sorted_scores)
    return sorted_scores


def rank_hands():
    scores = score_hands()
    rank = len(hands)
    for score in scores:
        ranks[score[0]] = rank
        rank -= 1

    sorted_ranks = sorted(ranks.items(), key=lambda kv: kv[1])
    return dict(sorted_ranks)


def get_total_winnings():
    total_winnings = 0
    ranks = rank_hands()
    for hand in hands:
        # print(hand, ranks[hand])
        total_winnings += hands[hand] * ranks[hand]
    return total_winnings


winnings = get_total_winnings()
print()
print(winnings)





