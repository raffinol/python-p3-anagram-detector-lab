class Anagram:
    def __init__(self, word):
        self.word_letters = sorted([letter for letter in word])

    def match(self, list):
        match_list = []

        for word in list:
            if sorted([letter for letter in word]) == self.word_letters:
                match_list.append(word)

        return match_list
