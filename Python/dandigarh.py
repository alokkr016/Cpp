def reverse(a):
    l=len(a)
    c=0
    x=''
    if(l%2==0):
        l=int(l/2)
        str1 = a[0:l]
        str2 = a[l:]
    else:
        c=1
        l=int(l/2)
        x=a[int(l)]
        str1 = a[0:l]
        str2 = a[l+1:]
    st1=rev(str1)
    st2=rev(str2)
    if(c==0):
        return st1+st2
    else:
        return st1+x+st2

def rev(a):
    return a[::-1]
s=input("Enter a String")

sk=reverse(s)
print(sk)