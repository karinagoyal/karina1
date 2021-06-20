def display(s):
    d={}
    for i in s:
        c=s.count(i)
        d[i]=c
    v=sorted(d.values(),reverse=True)
    v1=[]
    for i in v:
        if i not in v1:
            v1.append(i)
    for i in v1:
        for x in d:
            if d[x]==i:
                print(x,d[x],sep=' = ')
    
        
            
s=input("Enter String : ")
display(s)
