def hanoiKuleleri(kaynak,temp,hedef,n):
    if (n == 0):
        return
    
    hanoiKuleleri(kaynak, hedef, temp, n - 1)
    print(f"\n{n} disk ({kaynak} -> {hedef})")
    hanoiKuleleri(temp, kaynak, hedef, n - 1)
    


n = int(input("Number of Disks \n"))
hanoiKuleleri('a', 'b', 'c', n);
print("\n\n")



