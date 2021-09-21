z=["L","Ma","Mi","J","Vi","S","D"]
s=[]
for i in range(0,len(z)):
    x=input("salariul: {} ".format(z[i]))
    s.append(int(x))
print("Salariul in fiecare zi: {}".format(s))
print(sum(s))
print(round(sum(s)/7,2))
print(max(s))
vMax=[]
vMin=[]
for i in range(0,len(z)):
    if s[i]==max(s):
        vMax.append(z[i])
print(vMax)
for i in range(0,len(z)):
    if s[i]==min(s):
        vMin.append(z[i])
print(vMin)