Workload assumptions:
1. Each job runs for the same amount of time.
2. All jobs arrive at the same time.
3. All jobs only use the CPU (i.e., they perform no I/O).
4. The run-time of each job is known.

# Performance and fairness
Performance metric: Turnaround time
- The time at which the job completes minus the time at which the job arrived in the system    $T_{\text{turnaround}}=T_{\text{completion}}-T_{\text{arrival}}$
Another metric is fairness:
- Performance and fairness are often at odds in scheduling.

# Algorithms
## First In First Out
First Come, First Served (FCFS)
- Very simple and easy to implement
Example:
- A arrived just before B which arrived just before C.
- Each job runs for 10 seconds.
$\operatorname{avg}\ T_{\text{turnaround}}=\frac{10+20+30}{3}=20sec$

### Why is FIFO not that great?
If job A takes 100 seconds, the average turnaround time will be much higher.
$\operatorname{avg}\ T_{\text{turnaround}}=\frac{100+110+120}{3}=110sec$

## Shortest Job First
Example:
- A arrived just before B which arrived just before C.
- A runs for 100 seconds, B and C run for 10 each.
$\operatorname{avg}\ T_{\text{turnaround}}=\frac{10+20+120}{3}=50sec$

SJF is **NOT** a pre-emptive algorithm (the process cannot be interrupted)

### Why is SJF not that great?
If job A arrives before B and C (say, $T=10$), the average turnaround time will be much higher.
$\operatorname{avg}\ T_{\text{turnaround}}=\frac{100+(110-10)+(120-10)}{3}=103+\frac13sec$

## STCF