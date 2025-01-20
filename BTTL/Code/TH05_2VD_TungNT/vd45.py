import numpy as np
A =np.array([(3,-1,-2),
             (3,2,-3),
             (1,0,2)])
trace_A = A.trace()
print('Trace of Matrix A:',trace_A)
trace_A = A.diagonal().sum()
print('Trace of Matrix A:',trace_A)