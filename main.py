from input import input


def get_digits(string):
    digits = ''
    for i in string:
        if i.isdigit(): digits += i
    return int(digits[0] + digits[-1])


def get_codes(codes):
    arr = list(map(get_digits, codes.split()))
    print(sum(arr))


if __name__ == '__main__':
    get_codes(input)
