class RotationCipher(object):
  
  def __init__(self):
    
    self.plain = ''
    
  def rot_cipher(self, rot, cipher):
    
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

    return self.plain

