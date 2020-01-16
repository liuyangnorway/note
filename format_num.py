def str_float(x):
    import re
    x0=x
    x=re.findall(r"\d+\.?\d*",x)
    
    if len(x)==0:
        x=np.nan
    elif len(x)==1:
        x=float(x[0])
    else:
        print('x should one number',x)
        return x0
    return x
    

def num_format(x,n=9,k=4,f='f'):
    """
    n is the total width of the field being printed, lefted-padded by spaces.
    k is the number of digits after the decimal point.
    f is 'f' - Fixed point, 'e' - Exponent notation
    """
    if x==0:
        b=' {:>'+'{}'.format(n)+'.0f}'
    else:
        b=' {:>'+'{}'.format(n)+'.{}{}'.format(k,f)+'}'
    sx=b.format(x)
    return sx
