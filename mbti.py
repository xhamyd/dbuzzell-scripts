from collections import namedtuple

LETTERS = [("E", "I"),  # Extroverted, Introverted
           ("N", "S"),  # iNtuition, Sensing
           ("F", "T"),  # Feeling, Thinking
           ("J", "P")]  # Judging, Perceiving

AXES = {
    # Judging functions: "Feeling", "Thinking"
    "J": ("F", "T"),
    # Perceiving functions: "iNtuition", "Sensing"
    "P": ("N", "S")
}


def validate_letters(letters):
    if not isinstance(letters, str) or not letters.isupper() or len(letters) != len(LETTERS):
        return False

    for i, letter in enumerate(letters):
        valid_letters = LETTERS[i]
        if letter not in valid_letters:
            return False
    return True


def validate_types(types):
    if not types or len(types) != len(LETTERS):
        return False

    for function_type in types:
        if not isinstance(function_type, str) or len(function_type) != 2:
            return False
        first_letter, second_letter = function_type
        function_letters = (letter for row in LETTERS[1:3] for letter in row)
        if not first_letter.isupper() or first_letter not in function_letters:
            return False
        if not second_letter.islower() or second_letter.upper() not in LETTERS[0]:
            return False
    return True


def get_opposite(letter):
    a_letter, b_letter = next((row for row in LETTERS if letter in row), None)
    return a_letter if letter == b_letter else b_letter


def convert_letters_to_types(letters):
    assert validate_letters(letters), f"Invalid MBTI Letters: {letters}"

    # With the middle letter, find which on is on the extroverted axis
    if letters[1] in AXES[letters[3]]:
        extroverted_letter, introverted_letter = letters[1], letters[2]
    else:
        extroverted_letter, introverted_letter = letters[2], letters[1]

    # Based on "*-verted" letter, determine first and second function
    if letters[0] == "E":
        first_function, second_function = extroverted_letter, introverted_letter
    else:
        first_function, second_function = introverted_letter, extroverted_letter

    # Fill in the remaining information
    first_verted = letters[0].lower()
    second_verted = get_opposite(letters[0]).lower()
    third_letter, fourth_letter = get_opposite(second_function), get_opposite(first_function)

    types = (f"{first_function}{first_verted}",
             f"{second_function}{second_verted}",
             f"{third_letter}{first_verted}",
             f"{fourth_letter}{second_verted}")
    assert validate_types(types), f"Invalid MBTI types: {types}"
    return types


def convert_types_to_letters(types):
    assert validate_types(types), f"Invalid MBTI types: {types}"
    top_letters = types[0][0], types[1][0]

    first_letter = types[0][1].upper()
    second_letter = top_letters[0] if top_letters[0] in LETTERS[1] else top_letters[1]
    third_letter = top_letters[0] if top_letters[0] in LETTERS[2] else top_letters[1]
    extroverted_letter = top_letters[0] if first_letter == "E" else top_letters[1]
    fourth_letter = next((axis for axis in AXES.keys() if extroverted_letter in AXES[axis]), None)

    letters = f"{first_letter}{second_letter}{third_letter}{fourth_letter}"
    assert validate_letters(letters), f"Invalid MBTI Letters: {letters}"
    return letters


def test_mbti():
    Testcase = namedtuple("Testcase", "letters types")
    testcases = [Testcase("ISTP", ('Ti', 'Se', 'Ni', 'Fe')),
                 Testcase("INTP", ('Ti', 'Ne', 'Si', 'Fe'))]
    test_result = True
    for tc in testcases:
        converted_type = convert_letters_to_types(tc.letters)
        converted_letters = convert_types_to_letters(tc.types)
        if converted_type != tc.types:
            test_result = False
            print(f"{tc.letters} -> {converted_type} instead of {tc.types}")
        if converted_letters != tc.letters:
            test_result = False
            print(f"{tc.types} -> {converted_letters} instead of {tc.letters}")
    return test_result


assert(test_mbti())
