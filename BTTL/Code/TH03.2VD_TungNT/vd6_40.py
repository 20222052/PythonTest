f1 = open('anh.txt','a+')
st=' this is new line....'
f1.write(st)
f1.close()
f = open('anh.txt','r')
print(f.read())