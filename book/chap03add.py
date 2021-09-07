import ipywidgets

def ser(n=5):
    sum1 = 0
    for i in range(1,n+1):
        print(i)
        sum1 += i
    print(sum1)
    print(int(n*(n+1)/2))
    
ipywidgets.interact(ser,n=(1,10));
