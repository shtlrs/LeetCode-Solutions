def replace_vowels(string: str):
    letters_to_replace = ('a', 'e', 'i', 'o', 'u')
    for letter in letters_to_replace:
        string = string.replace(letter, "~")
    return string

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:

        answer_list = []

        d1 = {}
        d2 = {}
        d3 = {}

        for query in queries:
            d1[query] = ""
            d2[query.lower()] = ""
            d3[replace_vowels(query.lower())] = ""

        for word in reversed(wordlist):
            d1[word] = word
            d2[word.lower()] = word
            d3[replace_vowels(word.lower())] = word

        for query in queries:
            if d1[query] == query:
                answer_list.append(query)
                continue

            if d2[query.lower()] != "":
                answer_list.append(d2[query.lower()])
                continue

            if d3[replace_vowels(query.lower())] != "":
                answer_list.append(d3[replace_vowels(query.lower())])
                continue

            answer_list.append("")

        return answer_list
                
