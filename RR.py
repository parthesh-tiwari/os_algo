def rr(process_list, time_quantum):
    n = len(process_list)
    completed = 0
    time = 0
    wt = [0] * n
    tat = [0] * n
    gantt = []
    remaining_bt = [p[1] for p in process_list]
    is_completed = [False] * n
    last_process = -1

    while completed != n:
        idx = -1

        for i in range(n):
            if process_list[i][0] <= time and remaining_bt[i] > 0 and not is_completed[i]:
                # Move to the next process cyclically
                last_process = (last_process + 1) % n
            if process_list[last_process][0] <= time and remaining_bt[last_process] > 0:
                idx = last_process
                break

        if (idx == -1):
            gantt.append("Idle")
            time += 1
            continue

        gantt.append(process_list[idx][2])
        time += min(time_quantum, remaining_bt[idx])
        remaining_bt[idx] -= min(time_quantum, remaining_bt[idx])

        if (remaining_bt[idx] == 0):
            completed += 1
            completion_time = time
            tat[idx] = completion_time - process_list[idx][0]
            wt[idx] = completion_time - tat[idx]

    print("\n Gantt Chart:")
    print(" -> ".join(gantt))

    print("\nProcess ID | Arrival Time | Burst Time | Turnaround Time | Waiting Time")
    for i in range(n):
        print(
            f"   {process_list[i][2]}\t\t{process_list[i][0]}\t\t{process_list[i][1]}\t\t{tat[i]}\t\t{wt[i]}"
        )

    print(f"\nAverage Turnaround Time: {sum(tat) / n:.2f}")
    print(f"Average Waiting Time: {sum(wt) / n:.2f}")


process_list = [[0, 6, 'P1'], [2, 8, 'P2'], [4, 7, 'P3'], [6, 3, 'P4']]
time_quantum = 2

print("\n Process List: ", process_list)
print("\n Solution: ")
rr(process_list=process_list, time_quantum=time_quantum)
