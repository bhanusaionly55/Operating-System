class Process:
    def __init__(self, pid, burst_time, priority):
        self.pid = pid
        self.burst_time = burst_time
        self.priority = priority

def schedule(processes):
    processes = sorted(processes, key=lambda x: x.priority)
    current_time = 0
    waiting_time = 0
    for process in processes:
        current_time += process.burst_time
        waiting_time += current_time - process.burst_time
    return waiting_time / len(processes)

if __name__ == "__main__":
    processes = [Process(1, 6, 2), 
                 Process(2, 5, 0), 
                 Process(3, 8, 1)]
    average_waiting_time = schedule(processes)
    print("Average Waiting Time:", average_waiting_time)
