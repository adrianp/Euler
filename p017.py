import sys

from euler_util import toDigits


def main(*args, **kwargs):
    # some predefined numbers we need to get going
    # 1000 is in there because I am lazy
    numbers = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
               7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven",
               12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
               16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
               20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
               60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety",
               1000: "onethousand"}

    letters = 0

    for i in range(1, 1001):
        new = ""

        if i in numbers.keys():
            letters += len(numbers[i])
        else:
            digits = toDigits(i)
            magnitude = len(digits)
            if magnitude == 2:
                new = numbers[digits[0] * 10] + numbers[digits[1]]
                # we can reuse the 2-digit numbers when writting
                # the 3-digits ones
                numbers[i] = new
                letters += len(new)
            elif magnitude == 3:
                # note that we do not insert spaces
                new = numbers[digits[0]] + "hundred"
                if digits[1] != 0 or digits[2] != 0:
                    new += "and" + numbers[digits[1] * 10 + digits[2]]
                letters += len(new)

    print letters
    return 0

if __name__ == "__main__":
    sys.exit(main())
