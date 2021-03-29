l=int(input("Enter No Of Testcases :"))
Print("AS=AISLE SEAT  MS=MIDDLE SEAT  WS:WINDOW SEAT")
for i in range(l):
    n=int(input("Enter Your seat Number :"))
    a={1:"12",2:"11",3:"10",4:"9",5:"8",6:"7",7:"6",8:"5",9:"4",10:"3",11:"2",12:"1"}
    b={1:"WS",2:"MS",3:"AS",4:"AS",5:"MS",6:"WS",7:"WS",8:"MS",9:"AS",10:"AS",11:"MS",12:"WS"}
    c=0
    k=[]
    while(n>=12 or n<=12):
        if n>12:
            n=n-12
            c+=1
        if n<=12:
            e=int(a[n])
            d=(c*12)+e
            k.append(d)
            k.append((b[n]))
            break
    for h in k:
        print(h,end=" ")
    print()
        
        
