from random import choice
import re

"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    def __init__(self, filepath, stop_words = None) -> None:
        self.filepath = filepath
        self.wordlist = []
        temp = self.read_file()
        self.wordlist = temp
        print(f'{len(self.wordlist)} words read')
    

    def read_file(self):
        """This method tries to open the filepath passed into the
        instance and, if successful, populates a list of words stored
        on the instance. Finally, it lets the user know how many words
        are in the file."""
        try:
            with open(self.filepath) as f:
                new_list = [word.replace('\n', '').strip() for word in f.readlines()]

            return new_list

        except FileNotFoundError as f:
            print('You have provided an incorrect file path; please try again.')
            raise
    

    def random(self, words = None):
        """This method used the choice method from the
        random module to return a random word from self.wordlist
        when called."""
        return choice(words or self.wordlist)


class SpecialWordFinder(WordFinder):
    def __init__(self, filepath) -> None:
        self.wordlist = []
        self.filepath = filepath
        self.make_special_list()

    def make_special_list(self):
        self.wordlist = super().read_file()
        stop_words = re.findall(r'#\s?[A-Za-z]+\n?', " ".join(self.wordlist), re.I)
        self.wordlist = [word for word in self.wordlist if\
            word not in stop_words and word != '']
        print(f'{len(self.wordlist)} words read.')


my_words = WordFinder('words.txt')
print(my_words.random())

special_words = SpecialWordFinder('special.txt')
print(special_words.random())

