#MIT FINAL EXAM
#Problem 3

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    d_inv = {}
    for k, v in d.iteritems():
        d_inv[v] = d_inv.get(v, [])
        d_inv[v].append(k)
        d_inv[v] = sorted(d_inv[v])
    return d_inv
            