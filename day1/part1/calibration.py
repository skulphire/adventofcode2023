with open('input.txt', 'r') as f:
    lines = f.readlines()

sum_of_calibrations = 0

for line in lines:
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
    sum_of_calibrations += combined_int
print(sum_of_calibrations)

