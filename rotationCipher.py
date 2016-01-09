from trie import trieDictionary as dictionary

class rotationCipher(object):

    def __init__(self):
        self.plain = ''

    # Rotation cipher for all 25 keys
    def rot_cipher(self, cipher):
        for rot in range(1,26):
            for elem in cipher:
                # Performs decryption for alpha values
                if elem.isalpha():

                    # For uppercase alphabets
                    if elem.isupper():
                        if ord(elem) - rot < 65:
                            self.plain += chr(ord(elem) - rot + 26)
                        else:
                            self.plain += chr(ord(elem) - rot)

                    # For lowercase alphabets
                    if elem.islower():
                        if ord(elem) - rot < 97:
                            self.plain += chr(ord(elem) - rot + 26)
                        else:
                            self.plain += chr(ord(elem) - rot)
                # Non-alpha values
                else:
                    self.plain += elem

            # Checks the correctness of the key used, by comparing the first few words
            # of the decrypted plain text with the existing english words dictionary
            plain_words = self.plain.split()
            if len(plain_words) > 7:
                plaintext_sets = plain_words[0:7]
            else:
                plaintext_sets = plain_words[:]

            result = trie_obj.word_check(plaintext_sets)
            if result == True:
                return True

            # Reset the value of plain string
            self.plain = ""

        # Returns True or False
        # True, if the encryption used was Rotation
        # False, if some other encryption mechanism is used for creating the cipher text
        return False

trie_obj = dictionary()
