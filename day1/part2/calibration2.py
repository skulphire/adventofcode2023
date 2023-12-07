with open('input.txt', 'r') as f:
    lines = f.readlines()

sum_of_calibrations = 0

valid_words = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

for line in lines:
    old_line = line
    num1 = 0
    num2 = 0
    for key in valid_words.keys():
        line = line.replace(key, key + str(valid_words[key]) + key)
    numbers_in_line = []
    for char in line:
        if char.isnumeric():
            numbers_in_line.append(int(char))
    num1 = numbers_in_line[0]
    if len(numbers_in_line) > 1:
        num2 = numbers_in_line[len(numbers_in_line) - 1]
    else:
        num2 = num1

    string_total = str(num1) + str(num2)
    combined_int = int(string_total)
    print(combined_int, old_line, line)
    sum_of_calibrations += combined_int
print(sum_of_calibrations)
