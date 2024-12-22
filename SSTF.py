def sstf(seek, head):
    print("Order of access: \n")
    print(head, end=" -> ")

    total = 0

    while seek:
        closest = min(seek, key=lambda x: abs(x-head))
        print(closest, end=" -> ")
        total += abs(head - closest)
        head = closest
        seek.remove(closest)

    print("Total Seek time is: ", total)


seek = list(map(int, input("Enter the requests: ").split()))
head = int(input("Enter the desired head: "))

sstf(seek=seek, head=head)

# Here we find the closest from head and then add up the tota distance and then head is the closest value
