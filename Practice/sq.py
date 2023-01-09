# print([i**0.5 for i in range(1,16,2)])
names=["abreera bla","asa asdf","dfgd asd"]
# print([i[0]+"."+i.split(" ")[1] for i in names])
hel=lambda hey:[i[0]+"."+i.split(" ")[1] for i in names]
print(hel(names))