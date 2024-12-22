def cscan(seek, head, direction):
    seek += [0, 199]
    seek.sort()
    total = 0

    left = [x for x in seek if x <= head]
    right = [x for x in seek if x > head]

    if direction.lower()[0] == 'l':
        sequence = left[::-1] + right[::-1]
    elif direction.lower()[0] == 'r':
        sequence = right + left
    else:
        print("Wrong direction: ")
        return

    print(head, end=" -> ")
    for req in sequence:
        total = abs(req - head)
        head = req
        print(head, end=" -> ")

    print(f"The total seek time is: {total}")


seek = list(map(int, input("Enter the requests: ").split()))
head = int(input("Enter the desired head position: "))
direction = input("Enter the direction(L/R): ")

cscan(seek=seek, head=head, direction=direction)
