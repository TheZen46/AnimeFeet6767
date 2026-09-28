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
$\operatorname{avg}\ T_{\text{turnaround}}=\frac{100+(110-10)+(120-10)}{3}=103.\overline3sec$

## STCF
Also knows as **Pre-emptive Shortest Job First (PSJF)**
Add pre-emption to SJF (processes can now be interrupted)
A new job enters the system:
- Determine of the remaining jobs and new job
- Schedule the job which has the lest time left

Example:
- A arrives at t=0 and needs to run for 100 seconds.
- B and C arrive at t=10 and each need to run for 10 seconds
$\operatorname{avg}\ T_{\text{turnaround}}=\frac{100+(20-10)+(30-10)}{3}=50sec$

# Response time
The time from when the job arrives to the first time it is scheduled    $T_{\text{response}}=T_{\text{firstrun}}-T_{\text{arrival}}$
STCF and related disciplines are not particularly good for response time.

How can we build a  scheduler that is **sensitive** to response time?

# Round Robin
Time slicing Scheduling
- Run a job for a time slice and then switch to the next job in the run queue until the jobs are finished.
	Time slice is sometimes called a scheduling quantum.
- It repeatedly does so until the jobs are finished.
- The length of a time slice must be a multiple of the timer-interrupt period.

RR is fair, but performs poorly on metrics such as turnaround time

Short time-slices:
- Better response time
- The cost of context switching will dominate overall performance.
Long time-slices:
- Amortize the cost of switching
- Worse response time