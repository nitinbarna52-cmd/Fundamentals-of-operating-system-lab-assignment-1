'''
Task 1  Process Class & Input

You need to create a Process class with:

PID (Process ID)
AT (Arrival Time)
BT (Burst Time)
'''
class Process:
    def __init__(self, pid, at, bt):
        self.pid = pid
        self.at = at
        self.bt = bt
        self.ct = 0
        self.tat = 0
        self.wt = 0

# Input
processes = []
n = int(input("Enter number of processes: "))

for i in range(n):
    pid = input("Enter Process ID: ")
    at = int(input("Enter Arrival Time: "))
    bt = int(input("Enter Burst Time: "))
    processes.append(Process(pid, at, bt))

# Display Table
print("\nPID\tAT\tBT")
for p in processes:
    print(p.pid, "\t", p.at, "\t", p.bt)

    '''
   Task 2 - FCFS Scheduling
Logic:
Sort by Arrival Time
CT = Previous CT + BT
TAT = CT - AT
WT = TAT - BT 
    '''
    def fcfs(processes):
         processes.sort(key=lambda x: x.at)
    time = 0

   

    for p in processes:
        if time < p.at:
            time = p.at  # CPU Idle
        time += p.bt
        p.ct = time
        p.tat = p.ct - p.at
        p.wt = p.tat - p.bt

    print("\nFCFS Scheduling")
    print("PID\tAT\tBT\tCT\tTAT\tWT")
    for p in processes:
        print(p.pid, "\t", p.at, "\t", p.bt, "\t", p.ct, "\t", p.tat, "\t", p.wt)
'''
Task 3 - SJF Scheduling (Non-Preemptive)
'''
def sjf(processes):
    completed = []
    time = 0
    processes.sort(key=lambda x: x.at)

    while processes:
        ready = [p for p in processes if p.at <= time]
        if not ready:
            time += 1
            continue

        ready.sort(key=lambda x: x.bt)
        p = ready[0]
        processes.remove(p)

        time += p.bt
        p.ct = time
        p.tat = p.ct - p.at
        p.wt = p.tat - p.bt
        completed.append(p)

    print("\nSJF Scheduling")
    print("PID\tAT\tBT\tCT\tTAT\tWT")
    for p in completed:
        print(p.pid, "\t", p.at, "\t", p.bt, "\t", p.ct, "\t", p.tat, "\t", p.wt)
'''
 Task 5 - Performance Analysis
Formula:
Average WT = Total WT / Number of Processes
Average TAT = Total TAT / Number of Processes
'''
def avg_times(processes):
    total_wt = sum(p.wt for p in processes)
    total_tat = sum(p.tat for p in processes)
    n = len(processes)

    print("\nAverage Waiting Time =", total_wt/n)
    print("Average Turnaround Time =", total_tat/n)

