from collections import Counter
import sys
import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
# rel_path = 'alchemy_sample_input.txt'
rel_path = 'alchemy_input.txt'
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
            
def alchemy():
    N = in_file.readline()
    #print(N)
    count = Counter(in_file.readline().replace("\n", "").strip())
    c = "NY"[int(abs(count['A']-count['B']) == 1)]
    return c

t = int(in_file.readline())

for case in range(t):
    check_result = alchemy()
    if(case < t - 1):
          printf('Case #{}: {}'.format(case+1, check_result))
    else:
          printf('Case #{}: {}'.format(case+1, check_result), linebreak=False)
out_file.close()
    
