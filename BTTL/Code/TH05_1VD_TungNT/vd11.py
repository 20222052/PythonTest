import numpy as np
A = np.array([(5,7,2,9,10,15,2,9,2,17,28,16),(5,7,2,9,7,15,2,9,2,17,8,1),(5,7,2,9,10,15,2,9,2,17,28,1)],dtype=np.int16)
A2 = np.flip(A,0)
A2=np.flipud(A)
print('ma tran theo hang: \n',A2)