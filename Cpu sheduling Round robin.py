def round_robin(bhanu, quantum):
    n = len(bhanu)
    completion_time = [0] * n
    current_time = 0
    while True:
        completed = True
        for i in range(n):
            if bhanu[i][1] > 0:
                completed = False
                if bhanu[i][1] > quantum:
                    current_time += quantum
                    bhanu[i][1] -= quantum
                else:
                    current_time += bhanu[i][1]
                    completion_time[i] = current_time
                    bhanu[i][1] = 0
        if completed:
            break
    for i in range(n):
        print("Process", bhanu[i][0], "completed at", completion_time[i])

bhanu = [["P1", 21], ["P2", 3], ["P3", 6], ["P4", 2]]

quantum = 5

round_robin(bhanu, quantum)
