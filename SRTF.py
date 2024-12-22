def srtf(process_list):
    n = len(process_list)
    time = 0
    completed = 0
    gantt = []
    wt = [0] * n
    tat = [0] * n
    remaining_bt = [p[1] for p in process_list]

    while completed != n:
        idx = -1
        min_bt = float('inf')

        # Find the process with the shortest remaining time that has arrived
        for i in range(n):
            if process_list[i][0] <= time and remaining_bt[i] > 0:
                if remaining_bt[i] < min_bt or (remaining_bt[i] == min_bt and idx == -1):
                    min_bt = remaining_bt[i]
                    idx = i

        if idx == -1:
            gantt.append("Idle")
            time += 1
            continue

        gantt.append(process_list[idx][2])
        time += 1
        remaining_bt[idx] -= 1

        if remaining_bt[idx] == 0:
            completed += 1
            ct = time
            tat[idx] = ct - process_list[idx][0]
            wt[idx] = tat[idx] - process_list[idx][1]

    print("\nGantt Chart:")
    print(" | ".join(str(p) for p in gantt))

    print("\nProcess ID | Arrival Time | Burst Time | Turnaround Time | Waiting Time")
    for i in range(n):
        print(
            f"   {process_list[i][2]}\t\t{process_list[i][0]}\t\t{process_list[i][1]}\t\t{tat[i]}\t\t{wt[i]}"
        )

    print(f"\nAverage Turnaround Time: {sum(tat) / n:.2f}")
    print(f"Average Waiting Time: {sum(wt) / n:.2f}")


# Test
process_list = [[0, 6, 'P1'], [2, 8, 'P2'], [4, 7, 'P3'], [6, 3, 'P4']]
print("Input Process List:", process_list)
print("\nSolution:\n")
srtf(process_list)


process_list = [[0, 6, 'P1'], [2, 8, 'P2'], [4, 7, 'P3'], [6, 3, 'P4']]
print("Input Process List:", process_list)
print("\nSolution:\n")
srtf(process_list)


# In Process list, [0] refers Arrival time and [1] refers to the turnaroun time and [2] refers to the procss id
