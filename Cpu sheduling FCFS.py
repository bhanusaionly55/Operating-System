def FCFS(proccess):
    n = len(proccess);
    wt = 0;
    tat = 0;
    avg_wt = 0;
    avg_tat = 0;

    for i in range(n):
        if i ==0:
            wt = 0;
            tat = proccess[i][1];
        else:
            wt = wt + proccess[i-1][1];
            tat = wt + proccess[i][1];
        avg_wt = avg_wt + wt;
        avg_tat = avg_tat + tat;

    avg_wt = avg_wt/n;
    avg_tat = avg_tat/n;

    return avg_wt,avg_tat;

proccess = [(1,10),(2,5),(3,8)];

avg_wt,avg_tat = FCFS(proccess)
print("AVG WT: ",avg_wt);
print("AVG TAT: ",avg_tat);
