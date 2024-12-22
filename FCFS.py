def fcfs(process_list):
    n = len(process_list)
    gantt = []
    tat = [0] * n
    wt = [0] * n
    isCompleted = [False] * n
    completed = 0
    time = 0

    while completed != n:
        idx = -1

        for i in range(n):
            if process_list[i][0] <= time and not isCompleted[i]:
                idx = i
                break

        if idx == -1:
            gantt.append("Idle")
            time += 1
            continue

        gantt.append(process_list[idx][2])
        time += process_list[idx][1]
        completed += 1
        isCompleted[idx] = True
        completion_time = time
        tat[idx] = completion_time - process_list[idx][0]
        wt[idx] = tat[idx] - process_list[idx][1]

        print(" -> ".join(gantt))
        print(
            f"\nProcess Id  |  Arrival Time  |  Burst Time  |  Turnaround Time | Burst Time")

        for i in range(n):
            print(
                f"{process_list[i][2]}   {process_list[i][0]}   {process_list[i][1]}   {wt[i]}   {tat[i]}")

        print(f"\n  AverageTurnaround time: {sum(tat) / 2:.2f}")
        print(f"\n  Average Waiting Time: {sum(wt) / 2:.2f}")


process_list = [[0, 6, 'P1'], [2, 8, 'P2'], [4, 7, 'P3'], [6, 3, 'P4']]
print("Input Process List:", process_list)
print("\nSolution:\n")
fcfs(process_list)
