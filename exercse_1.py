import numpy as np
x=np.array([0,1,0,3,4,5,0,7,8])

w=np.all(x>=0)
print(w)
#to count how many zeros are in an array
m=0
for c in x:
    if c==0:
        m+=1
print("there are " + str(m) + " numbers of zeros in this array")






# EOF