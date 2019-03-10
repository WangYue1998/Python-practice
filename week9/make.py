# Python program using dictionaries.
# Poorly documented so you have to trace an execution to learn what it does.

def m(filename):
    r = {}
    f = open(filename, 'r')
     
    for l in f:
        ll = l.strip().split(',')
        if ll[0]:
            p = ll[0]
            pl = [int(n) for n in ll[1:]]
        
            if p not in r:
                r[p] = []
            
            r[p] += pl
        
    f.close()
    return r

ds = m('initData.txt')

print( ds['Pam'] )

print( 'Hal:', ds['Hal'] )

print( 'Jane:', ds['Jane'] )

