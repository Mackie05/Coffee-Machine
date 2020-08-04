atom_count = int(input())
reduced_count = int(input())
half_life = 0
hl_periods = 0
while atom_count >= reduced_count:
    atom_count /= 2
    hl_periods += 12

print(hl_periods)
