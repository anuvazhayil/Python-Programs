class AtbashCipher(object):
  
  def __init__(self):
    self.plain = ''
    
  def atbash_cipher(self, cipher):
    for ch in cipher:
      if ch.isalpha():
        if ch.isupper():
          start = 65 
        if ch.islower():
          start = 97 

        cip_0_25_range = ord(ch)-start
        msg_0_25_range = 25 - cip_0_25_range
        msg_ascii = start + msg_0_25_range                 
        self.plain += chr(msg_ascii)
      
      else:
        self.plain += ch
      
    return self.plain
