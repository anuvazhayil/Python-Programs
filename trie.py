from pytrie import SortedStringTrie as trie

class trieDictionary(object):

    def __init__(self):
        with open('dictionary.txt', 'r') as infile:
            data = infile.read()
        #Creating a list of existing english words
        self.words = data.splitlines()

    #Initialising trie with a list of english words
    def init_trie(self,trie_tree):
        count = 0
        for i in self.words:
            trie_tree.__setitem__(i,count)
            count += 1

    #Checks the existence of the word and calculates the score of the given text
    # which determines the correctness of the decryption module
    def word_check(self,text):
        score = 0
        for elem in text:
            if trie_tree.__contains__(elem.upper()):
                score += 1
        if (len(text) == 1 or len(text) == 0) and score == 0:
            return False
        else:
            if score >= int(0.5*len(text)):
                return True
            else:
                return False

trie_tree = trie()
trie_obj = trieDictionary()
trie_obj.init_trie(trie_tree)
