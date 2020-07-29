from collections import deque
import sys
import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
# rel_path = 'running_on_fumes_chapter_1_input_sample.txt'
rel_path = 'running_on_fumes_chapter_1_input.txt'
abs_file_path = os.path.join(script_dir, rel_path)
in_file = open(abs_file_path, 'r')

out_file_check = True
rel_path = rel_path.replace('_input', '_output')
abs_file_path = os.path.join(script_dir, rel_path)
out_file = open(abs_file_path, 'w')

def printf(s, linebreak = True):
    #print(s) 
    if out_file_check:
        if linebreak:
            out_file.write(s + '\n')
        else:
            out_file.write(s)

def running_on_fumes_chapter_1():
    N, M = map(int, in_file.readline().strip().split())
    C = [int(in_file.readline()) for _ in range(N)]
    dq = deque([(0, 0)])
    for i in range(1, len(C)):
        count = 0
        if dq and i-dq[0][0] > M:
            count += 1
            dq.popleft()
        if not dq:
            return -1
        if not C[i]:
            continue
        #print(dq[0][1],C[i])
        d = dq[0][1] + C[i]
        while dq and dq[-1][1] >= d:
            dq.pop()
        dq.append((i, d))   
    return dq[0][1]

t = int(in_file.readline())
for case in range(t):
    check_result = running_on_fumes_chapter_1()
    if(case < t - 1):
          printf('Case #{}: {}'.format(case+1, check_result))
    else:
          printf('Case #{}: {}'.format(case+1, check_result), linebreak=False)
out_file.close()

