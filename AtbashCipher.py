from trie import trieDictionary as dictionary

class atbashCipher(object):

    def __init__(self):
        self.plain = ''

    def atbash_cipher(self, cipher):
        for ch in cipher:
            # Performs decryption for alpha values
            if ch.isalpha():
                if ch.isupper():
                    start = 65
                if ch.islower():
                    start = 97

                cip_0_25_range = ord(ch)-start
                msg_0_25_range = 25 - cip_0_25_range
                msg_ascii = start + msg_0_25_range
                self.plain += chr(msg_ascii)
            # Non-alpha values
            else:
                self.plain += ch

        plain_words = self.plain.split()
        if len(plain_words) > 7:
            plaintext_sets = plain_words[0:7]
        else:
            plaintext_sets = plain_words[:]

        result = trie_obj.word_check(plaintext_sets)

        # Returns True or False
        # True, if the encryption used was Atbash
        # False, if some other encryption mechanism is used for creating the cipher text
        return result

trie_obj = dictionary()
