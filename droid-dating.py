droids = [
  {'name': 'BB-8', 'fav_jedi': 'Rey'},
  {'name': 'R2-D2', 'fav_jedi': 'Luke Skywalker'},
  {'name': 'C-3PO', 'fav_jedi': 'Luke Skywalker'},
  {'name': 'JJ-T0R', 'fav_jedi': 'Rey'}
]

'''{'name': 'JJ-T0R', 'fav_jedi': 'Rey'}'''

matches = [(a,b) for i,a in enumerate(droids) for b in droids[i+1:]]

scores = ['Great' if a['fav_jedi'] == b['fav_jedi'] else 'Miserable' for a,b in matches]

# print(*zip(matches, scores))
print(['{[name]} + {[name]} = {}'.format(*m, s) for m,s in zip(matches,scores)])

'''
OUTPUT:
['BB-8 + R2-D2 = Miserable', 'BB-8 + C-3PO = Miserable', 
'BB-8 + JJ-T0R = Great', 'R2-D2 + C-3PO = Great', 
'R2-D2 + JJ-T0R = Miserable', 'C-3PO + JJ-T0R = Miserable']
'''

'''
for i, a in enumerate(droids):
  for b in droids[i+1]:
    matches.append((a,b))

for i in range(len(droids)):
  for j in range(i+1, len(droids)):
    matches.append((droids[i], droids[j]))
'''

'''
#Parameter unwrapping
def foo(a, b, c, d=0):
  return a + b + c + d


args = [1, 2, 3]
kwargs = {
  'd': 6
}
print(foo(*args, **kwargs))
'''