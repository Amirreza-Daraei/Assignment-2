time = []

h = int (input("saat ra vared namaeid:"))
m = int (input("daghighe ra vared namaeid:"))
s = int (input("saniye ra vared namaeid:"))

time.append(h*3600)
time.append(m*60)
time.append(s)

convert = sum(time)

print("sum of second is :" , convert)