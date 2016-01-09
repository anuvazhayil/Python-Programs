from trie import trieDictionary as dictionary
import base64
import binascii

class base64Decoding(object):
    def __init__(self):
        self.decoded = ''

    def is_base64(self,encoded):
        try:
            self.decoded = base64.decodestring(encoded)
            plain_words = self.decoded.split()
            if len(plain_words) > 7:
                plaintext_sets = plain_words[0:7]
            else:
                plaintext_sets = plain_words[:]

            result = trie_obj.word_check(plaintext_sets)

            # Returns True or False
            # True, if the encryption used was base64
            # False, if some other encryption mechanism is used for creating the cipher text
            return result

        except binascii.Error:
            return False

trie_obj = dictionary()
