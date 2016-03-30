bbs = '01110011001000000110111001101111001000000010000001101001001000000111001101101110001000000110010100100000001000000110100000100000001000000110010100100000011100100010000000100000011100000110110100100000011011110010000001100011'

octets = []
for i in range(0, len(bbs), 8):
  octets.append(bbs[i:i+8])

chrs = [chr(int(octet, 2)) for octet in octets]

chrs = [c for c in chrs if c!= ' ']

message = ''.join(reversed(chrs))
print(message)
'''
^^same as^^
octects = list(map(lambda i: bbs[i:i+8], range(0, len(bbs), 8)))

ORRRR
octects = [bbs[i:i+8] for i in range(0,len(bbs),8)]
- this is a list comprehension
  - brackets '[]' indicate we're making a new list
  - bbs[i:i+8] is an expression
  - 'for' defines an iterator that we use for our new list


'''
