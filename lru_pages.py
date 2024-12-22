def lru(pages,size):
    frames=[None]*size
    hit=0
    miss=0
    ptr=0
    for page in pages :
        print(page,end=" -> ")
        if page in frames:
            hit+=1
            ptr = ((frames.index(page)+1)%size)
            print(frames,end=" ")
            print("hit")
            
        else:
            miss+=1
            if None in frames :
                idx=frames.index(None)
                frames[idx]=page
                ptr=int(ptr+1)%size
            else:
                frames[ptr]=page
            print(frames,end=" ")
            print("miss")
    print("Miss are : ",miss)
    print("\nhit are : ",hit)
    
size=int(input("Enter number of frames : "))
pages=list(map(int,input("Enter pages : ").split()))

lru(pages,size)