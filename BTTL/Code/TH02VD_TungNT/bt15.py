list_a = [5,7,3,8]
list_b = [7,3,8,5,7]
list_ab = list_a + list_b
print('list moi:', list_ab)
print(list_ab,'co so phan tu la:', len(list_ab))
bol_0 = 0 in list_ab
print('phan tu 0 co thuoc list_ab?', bol_0)
bol_8 = 8 in list_ab
print('phan tu 8 co thuoc list_ab?', bol_8)
print('danh sach ban dau: \n', list_ab)
list_ab.append(10)
print('danh sach them vao cuoi: \n', list_ab)
list_ab.insert(1,100)
print('danh sachs them vao vi tri thu 2: \n',list_ab)
list_ab.pop()
print('danh sach xoa phan tu cuoi: \n', list_ab)
del list_ab[1]
print('danh sach xoa phan tu o vi tri so 2: \n', list_ab)
print('so 8 xuat hien: ',list_ab.count(8))
print('so 0 xuat hien: ',list_ab.count(0))