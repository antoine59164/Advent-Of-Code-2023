# Vendredi 01/12/2023 Part 1
def exo1() -> int :
    result = 0
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    f = open("adventofcode.com_2023_day_1_input.txt", "r")
    for l in f:
        numbersInLine = []
        for w in l:
            if w in numbers:
                numbersInLine.append(w)
        joinNumber = numbersInLine[0] + numbersInLine[-1]
        result += int(joinNumber)
    return result


# Vendredi 01/12/2023 Part 2
def string_to_digit(texte):
    stringNumberToDigit = {
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

    texte_lower = texte.lower()

    if texte_lower in stringNumberToDigit:
        return stringNumberToDigit[texte_lower]
    else:
        return "Le texte ne correspond pas à un chiffre entre 1 et 9 en anglais."


print(string_to_digit('two'))
