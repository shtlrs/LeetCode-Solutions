from string import digits


class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.lstrip()

        if not s:
            return 0

        if s[0] in ["+", "-"]:
            sign = s[0]
            s = s[1:]
        else:
            sign = "+"

        if not s:
            return 0

        n = len(s)
        for index, char in enumerate(s):
            if char not in digits:
                n = index
                break

        if s[0] not in digits:
            return 0

        s = s[: n]

        number = int(f"{sign}{s}")
        if number > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif number < - 2 ** 31:
            return - 2 ** 31
        else:
            return int(number)
