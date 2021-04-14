d_imp = 30
c_imp = 20


land_mass = 150
booster_mass = 43

# d_imp*launch_mass = c_imp*land_mass
# d_imp*(ejected_mass + land_mass) = c_imp*(land_mass)
variable_mass = (d_imp/c_imp)*(land_mass) - booster_mass - land_mass

ejected_mass = booster_mass + variable_mass

launch_mass = land_mass + ejected_mass


print(launch_mass) 

print(land_mass) 

print(variable_mass)