scors = []

x = int(input("tedad daneshjoyan ra vared namaeid:"))
 
for i in range(x):
    y = float(input("nomarat ra vared namaeid :"))
    scors.append(y)

avrage = sum(scors)/x
max = max(scors)
min = min(scors)





print("avvrage :",avrage, "maximom :" , max , "minimom :" , min)