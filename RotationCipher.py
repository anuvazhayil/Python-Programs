import detectEnglish

class RotationCipher(object):

    def __init__(self):
        ##Initialise the plane text to be empty
        self.plain = ''

    def brute_force(self):
        ##Check
        return detectEnglish.isEnglish(self.plain)

    def rot_cipher(self, cipher):
        ##Decipher the text with all 25 possible keys
        ##for rot in range(26):
        rot = 3
            ##self.plain = ''
            for elem in cipher:

                if elem.isalpha():

                    if elem.isupper():
                        if ord(elem) + rot > 90:
                            self.plain += chr(ord(elem) + rot - 26)
                        else:
                            self.plain += chr(ord(elem) + rot)

                    if elem.islower():
                        if ord(elem) + rot > 122:
                            self.plain += chr(ord(elem) + rot - 26)
                        else:
                            self.plain += chr(ord(elem) + rot)

                else:
                    self.plain += elem

            ##self.brute_force();
        return self.plain

cip = RotationCipher()
print cip.rot_cipher('DEDQGRQ')
