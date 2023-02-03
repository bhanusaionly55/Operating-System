def deadlock(processes, avail, maxm, allot):

    need = []
    for i in range(processes):
        n = [maxm[i][j] - allot[i][j] for j in range(len(avail))]
        need.append(n)

    finish = [False] * processes

    safe_seq = [0] * processes

    work = [0] * len(avail)
    for i in range(len(avail)):
        work[i] = avail[i]

    count = 0
    while count < processes:
        found = False
        for p in range(processes):
            if (not finish[p]) and all(need[p][i] <= work[i] for i in range(len(work))):
                for i in range(len(work)):
                    work[i] += allot[p][i]

                safe_seq[count] = p
                count += 1
                finish[p] = True
                found = True

        if not found:
            return False, []

    return True, safe_seq

processes = 5
avail = [3, 3, 2]
maxm = [[7, 5, 3], [3, 3, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
allot = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]

is_safe, seq = deadlock(processes, avail, maxm, allot)
if is_safe:
    print("System is in a safe state.\n Safe sequence:", seq)
else:
    print("System is in an unsafe state.")
