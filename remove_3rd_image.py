import os

for a,b,c in os.walk(''):  # specify the path to the directory which contains images.
    for i in c:
        st = i.split('_')
        if st[1].startswith('3'):
            os.remove(a+'/'+i)
