import os

dirFile = os.listdir('C:/Users/user/anaconda3')

print(dirFile)
print("***"*100)
print(len(dirFile))


for x in os.listdir('C:/Users/user/anaconda3'):
        if x.endswith('exe'):
                print(x)
