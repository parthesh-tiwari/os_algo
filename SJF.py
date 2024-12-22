# Shortest Job Fir

def sjf(process_list):
    completed = 0
    n = len(process_list)
    wt = [0] * n
    tat = [0] * n
    time = 0
    gantt = []
    is_completed = [False] * n

    while completed != n:
        idx = -1
        min_bt = float("inf")

        for i in range(n):
            if process_list[i][0] <= time and not is_completed[i]:
                if process_list[i][1] < min_bt:
                    min_bt = process_list[i][1]
                    idx = i

        if idx == -1:
            time += 1
            gantt.append("Idle")
            continue

        gantt.append(process_list[idx][2])
        time += process_list[idx][1]
        completed += 1
        is_completed[idx] = True

        ct = time
        tat[idx] = ct - process_list[idx][0]
        wt[idx] = tat[idx] - process_list[idx][1]

    print("\n Gantt Chart")
    print(" -> ".join(gantt))

    print(f"\n Process ID | Arrival Time | Burst Time | Turnaround Time | Waiting Time")

    for i in range(n):
        print(
            f"\n {process_list[i][2]}    {process_list[i][0]}     {process_list[i][1]}    {tat[i]}    {wt[i]}  ")

    print(f"Average turnaround time: {sum(tat) / n: .2f}")
    print(f"Average waiting time: {sum(wt) / n: .2f}")


process_list = [[0, 6, 'P1'], [2, 8, 'P2'], [4, 7, 'P3'], [6, 3, 'P4']]
print("\n Input Process", process_list)
print("\n Solution: ")
sjf(process_list)
