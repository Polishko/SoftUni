from collections import deque


jobs = deque(int(x) for x in input().split(", "))
target_idx = int(input())
job_collection = {}

for i in range(len(jobs)):
    job = jobs.popleft()
    job_collection[i] = job

sorted_jobs = sorted(job_collection.items(), key=lambda x: (x[1], x[0]))

total_cycles = 0
for item in sorted_jobs:
    total_cycles += item[1]
    if item[0] == target_idx:
        print(total_cycles)
        break
