def prioritySchedulingNonPreemptive(process_list):
    n = len(process_list)
    time = 0
    completed = 0
    wt = [0] * n
    tat = [0] * n
    gantt = []
    is_completed = [False] * n

    while completed != n:
        idx = -1
        highest_priority = float('inf')

        for i in range(n):
            if process_list[i][0] <= time and not is_completed[i]:
                if process_list[i][2] < highest_priority:
                    highest_priority = process_list[i][2]
                    idx = i

        if (idx == -1):
            gantt.append('Idle')
            time += 1
            continue

        gantt.append(process_list[idx][3])
        time += process_list[idx][1]
        completed += 1
        is_completed[idx] = True
        ct = time
        tat[idx] = ct - process_list[idx][0]
        wt[idx] = tat[idx] - process_list[idx][1]

        print(" -> ".join(gantt))

        print("\nProcess ID  | Arrival Time  | Burst Time  |  Priority  |  Turnaround Time | Waiting Time")

        for i in range(n):
            print(
                f"\n{process_list[i][3]}   {process_list[i][0]}   {process_list[i][1]}   {process_list[i][2]}   {tat[i]}   {wt[i]}")

        print(f"\n Average Turnaround Time: {sum(tat) / n:.2f}")
        print(f"\n Average Waiting Time: {sum(wt) / n:.2f}")


process_list = [[0, 6, 2, 'P1'], [2, 8, 1, 'P2'],
                [4, 7, 3, 'P3'], [6, 3, 2, 'P4']]

print("Input processes: ", process_list)
print("Solution")

prioritySchedulingNonPreemptive(process_list=process_list)
