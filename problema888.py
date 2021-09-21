ora=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
t=[7,7,4,4,7,6,6,7,7,8,8,9,10,11,12,12,13,12,12,11,11,9,9,8,7]
print('Temperatura medie= ', round(sum(t)/24,1))
print('Maximul= ',max(t))
print('Minimul= ',min(t))
print('Ora(orele) la care s-a inregistrat temp. max.: ',ora[t.index(max(t))])
print('Ora(orele) la care s-a inregistrat temp. min.: ',ora[t.index(min(t))])