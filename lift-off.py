pilots = [
  {'name': 'Luke Skywalker', 'ship_id': 0},
  {'name': 'Darth Vader', 'ship_id': 1},
]
ships = [
  {'id': 1, 'model': 'TIE Advanced x1'},
  {'id': 0, 'model': 'T-65B X-wing'},
]

pilot_ships = [(p,s) for p in pilots for s in ships if p['ship_id'] == s['id']]

print(['{[name]} -> {[model]}'.format(p,s) for p,s in pilot_ships])

# ['Luke Skywalker → T-65B X-wing', 'Darth Vader → TIE Advanced x1']