def fifo(pages, size):
    frame = [None] * size
    head = 0
    miss = 0
    hit = 0

    for page in pages:
        print(page, end=': \t')
        if (page in frame):
            hit += 1
            print("\t hit \n")
        else:
            miss += 1
            frame[head] = page
            head = int((head+1) % size)
            print("\t miss \n")

    print("\nMisses are: ", miss)
    print("\n Hits: ", hit)


pages = list(map(int, input("Enter the page sizes: ").split()))
size = int(input("Enter the frame size: "))

fifo(pages=pages, size=size)
