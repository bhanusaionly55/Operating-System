def priority_scheduling(bhanu):
    bhanu.sort(key=lambda x: x[2])
    completion_time = 0
    for process in bhanu:
        completion_time += process[1]
        print("Process", process[0], "with priority", process[2], "completed at", completion_time)

bhanu = [("P1", 6, 2), ("P2", 8, 1), ("P3", 7, 3), ("P4", 3, 4)]

priority_scheduling(bhanu)
