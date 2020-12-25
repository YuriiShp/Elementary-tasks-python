"""
Palindromes

Проверить является ли число или его часть палиндромом. Например,
число 1234437 не является палиндромом, но является палиндромом его
часть 3443. Числа меньшие, чем 10 палиндромом не считать.
"""


def main():
    """Module extracts palindromes from the number

    Input:
    positive real number

    Output:
    palindromes or 0 if palindromes were not found
    """

    raw_input = input('Enter positive real number: ')

    result = None
    if is_valid(raw_input):
        data = convert(raw_input)
        result = extract_palindromes(data)

        print_out(result)

    return result

def is_valid(var: str) -> bool:
    """Function checks user input

    Keyword arguments:
    var -- input string

    Return:
    boolean value
    """

    if not var:
        print(main.__doc__)
        return False

    var = var.strip()

    try:
        int(var)
    except ValueError:
        print('ERROR: invalid input!')
        return False

    if int(var) < 0:
        print('ERROR: invalid input!')
        return False

    return True

def convert(var: str) -> str:
    """Function just strips spaces from the input string"""

    return var.strip()

def extract_palindromes(var: str) -> list:
    """Function extracts palindromes from the number

    Keyword arguments:
    var -- input number in string format
    Return:
    list of numbers in string format
    """

    input_as_list = list(var)
    result = []

    # Inintial loop conditions
    left_side = [input_as_list.pop(0)]
    right_side = input_as_list
    mid = None
    mode = 'ODD'

    while True:

        # Here we move through the number splitting it by the two parts
        # (left and right) on each iteration chars from right part move
        # to the left
        if mode == 'EVEN':
            left_side.insert(0, mid)
            mid = None
            mode = 'ODD'
        else:
            if len(right_side) > 1:
                mid = right_side.pop(0)
                mode = 'EVEN'
            else:
                break

        # Here we compare two parts for symmetric ellements
        len_left = len(left_side)
        len_right = len(right_side)

        number_of_iterations = len_left \
                                if len_left <= len_right \
                                else len_right

        count = 0
        for i in range(number_of_iterations):
            if left_side[i] != right_side[i]:
                break
            count += 1

        # And joining them together if symmetry was found
        if count:
            mid = mid if mid else ''
            palindrome = ''.join(left_side[:count][::-1]) \
                         + mid \
                         + ''.join(right_side[:count])
            result.append(palindrome)

    return result

def print_out(var: str) -> None:
    """Function printin out the result"""

    print('Palindromes: ', end='')

    if not var:
        print(0)
    else:
        for i in var:
            print(i, end=', ')

if __name__ == '__main__':
    main()
