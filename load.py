from tendl import tendl

xs_dir = 'z'

projectile_protons = 1
projectile_neutrons = 0
target_protons = 26
target_nucleons = 56

d = tendl.read(xs_dir, projectile_protons, projectile_neutrons, target_protons, target_nucleons)
#print(d.keys())


r = tendl.read_reactions(xs_dir, projectile_protons, projectile_neutrons, target_protons, target_nucleons)
#print(r)

r = tendl.read_reactions_list(xs_dir, projectile_protons, projectile_neutrons, target_protons, target_nucleons)
print(r)


residual_protons = 27
residual_nucleons = 57

xs = tendl.read_xs(xs_dir, projectile_protons, projectile_neutrons, target_protons, target_nucleons, residual_protons, residual_nucleons)
print(xs)
