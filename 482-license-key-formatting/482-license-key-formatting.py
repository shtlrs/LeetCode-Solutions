class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        dash = "-"
        n = 0
        for char in s:
            if char != dash:
                n += 1
        s = "".join(s.upper().strip().split(dash))
        first_sub_string_len = n % k
        new_s = []
        if first_sub_string_len:
            new_s = [s[: first_sub_string_len]]
        s = s[first_sub_string_len: ]
        start = 0
        for ix, char in enumerate(s):
            if ((ix + 1) % k ) == 0:
                new_s.append(s[start: ix + 1])
                start = ix + 1

        print(new_s)
        return dash.join(new_s)