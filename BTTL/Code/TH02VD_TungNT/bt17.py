a = 10
b = a
b = 5
print('gia tri cua bien a:', a)
print('gia tri cua bien b:', b)
ds_a = [4,7,3,5]
ds_b = ds_a
ds_b[1] = 10
print('gia tri cua bien a:', ds_a)
print('gia tri cua bien b:', ds_b)
ds_a = [4,7,3,5]
ds_b = ds_a.copy()
ds_b[1] = 10
print('gia tri cua bien a:', ds_a)
print('gia tri cua bien b:', ds_b)