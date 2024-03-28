fav_comp=['Sanrio','Mattel','logitech','moeflavor','dollskill','care bears']

#a
for e in range(len(fav_comp)):
    print(fav_comp[e])

#b
for e in range(len(fav_comp)):
    print(f"{e}. {fav_comp[e]}")

del fav_comp[1:2]
fav_comp.append('hoyoverse')
fav_comp.append('valve')
fav_comp.append('umbrella corp.')

print(fav_comp)


