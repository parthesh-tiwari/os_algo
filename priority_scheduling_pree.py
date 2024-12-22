def priorityScheduling(process_list):
    n = len(process_list)
    time = 0
    completed = 0
    gantt = []
    tat = [0] * n
    wt = [0] * n
    isCompleted = [False] * n
    remaining_time = [p[1] for p in process_list]

    while completed != n:
        idx = -1
        highest_priority = float('inf')

        for i in range(n):
            # process has arrived
            if (process_list[i][0] <= time and not isCompleted[i] and remaining_time[i] > 0):
                if highest_priority > process_list[i][2]:
                    highest_priority = process_list[i][2]
                    idx = i

        if (idx == -1):
            gantt.append('Idle')
            time += 1
            continue

        gantt.append(process_list[idx][3])
        time += 1
        remaining_time[idx] -= 1

        if remaining_time[idx] == 0:
            completed += 1
            isCompleted[idx] = True
            completion_time = time
            tat[idx] = completion_time - process_list[idx][0]
            wt[idx] = tat[idx] - process_list[idx][1]

        print("Gantt chart: ")
        print(" -> ".join(gantt))

        print("Process ID  |  Arrival Time  |  Burst Time  |  Priority  |  Turnaround Time  |  Waiting Time")

        for i in range(n):
            print(
                f"{process_list[i][3]}   {process_list[i][0]}  {process_list[i][1]}    {process_list[i][2]}   {tat[i]}   {wt[i]}")

        print(f"Average Turnaround Time: {sum(tat)/2:.2f}")
        print(f"Average Waiting Time: {sum(wt)/2:.2f}")


process_list = [[0, 6, 2, 'P1'], [2, 8, 1, 'P2'],
                [4, 7, 3, 'P3'], [6, 3, 2, 'P4']]

print("Input processes: ", process_list)
print("Solution")
priorityScheduling(process_list=process_list)
