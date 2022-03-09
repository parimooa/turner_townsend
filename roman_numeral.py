roman_to_number_mapping = {"I": 1, "V": 5, "X": 10, "C": 100, "M": 1000}


def roman_to_number(roman):
    numeric = 0
    try:
        for r in roman:
            numeric += roman_to_number_mapping[r]
        return numeric
    except KeyError:
        print(f"Invalid Roman numeral: {r}")



if __name__ == "__main__":
    print("Input Roman numeral")
    input_data=input()
    print(roman_to_number(input_data))
