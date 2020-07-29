from collections import defaultdict
import sys
import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
# rel_path = 'timber_sample_input.txt'
rel_path = 'timber_input.txt'
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

def timber():
    N = int(in_file.readline())
    P = [list(map(int, in_file.readline().strip().split())) for _ in range(N)]
    #print(P)
    P.sort()
    lookup = defaultdict(lambda:defaultdict(int))
    result = 0
    for d, direction in ((1, lambda x:x), (-1, reversed)):
        for p, l in direction(P):
            lookup[d][p+d*l] = max(lookup[d][p+d*l], lookup[d][p]+l)
        for p, l in lookup[d].items():
            result = max(result, lookup[-d][p]+l)
    return result

t = int(in_file.readline())
for case in range(t):
    check_result = timber()
    if(case < t - 1):
          printf('Case #{}: {}'.format(case+1, check_result))
    else:
          printf('Case #{}: {}'.format(case+1, check_result), linebreak=False)
out_file.close()
