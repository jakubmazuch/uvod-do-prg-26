from math import sqrt, acos, pi


def delka_vektoru(x):
    return sqrt(sum(vi**2 for vi in x))


u = [5, 2, 3]
v = [4, 2, 1]

# vektorový součin
vektorovySoucin = [u[1]*v[2] - v[1]*u[2], 
                   u[2]*v[0]-u[0]*v[2], 
                   u[0]*v[1]-u[1]*v[0]
                   ]
print(vektorovySoucin)

#skalární součin
skalarniSoucin = u[0]*v[0]+u[1]*v[1]+u[2]*v[2]
print(skalarniSoucin)

#délka w
print(delka_vektoru(vektorovySoucin))

#uhel mezi vektory
uhel = acos(skalarniSoucin/(delka_vektoru(u)*delka_vektoru(v)))
print(uhel, "rad", )
print(uhel*(180/pi), "°")