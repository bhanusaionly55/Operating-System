def sjf(bhanu):
    bhanu.sort(key=lambda x: x[1])
    completion_time = 0
    for bhanu in bhanu:
        completion_time += bhanu[1]
        print("Process: ", bhanu[0], "completed Time: ", completion_time)

bhanu = [("P1", 6), ("P2", 10), ("P3", 7), ("P4", 5)]

sjf(bhanu)
