def fcfs(seek, head):
    total = 0
    for req in seek:
        total += abs(head-req)
        print(req, end=" -> ")

    print("\nTotal seek time is: ", total)


seek = list(map(int, input("Enter the requests: ").split()))
head = int(input("Enter the desired head position: "))

fcfs(seek=seek, head=head)
