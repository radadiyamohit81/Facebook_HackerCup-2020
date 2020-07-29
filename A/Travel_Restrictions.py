import sys

def left2right_path(i, j):
    return [k for k in range(i, j+1)]

def right2left_path(i, j):
    return [k for k in reversed(range(j, i+1))]

def restriction(flight_path):
    def country_res(k):
        in_res = incoming[k-1]
        out_res = outgoing[k-1]
        return in_res + out_res
    temp = [country_res(k) for k in flight_path]
    temp = ''.join(temp)
    temp = temp[1:-1]
    if len(temp) < 1:
        return 'Y'
    else:
        return temp

def path(i, j):
    if i < j:
        return left2right_path(i, j)
    elif i > j:
        return right2left_path(i, j)
    else:
        return [i]

class Flight():
    def __init__(self, country_num, incoming, outgoing):
        super().__init__()
        self.country_num = country_num
        self.incoming = incoming
        self.outgoing = outgoing    

if __name__ == "__main__":
    
    in_file = open('travel_restrictions_input.txt', 'r')

    flight_num = int(in_file.readline())

    flight_list = []
    for f in range(0, flight_num):
        country_num = int(in_file.readline())
        incoming = in_file.readline()
        outgoing = in_file.readline()
        flight_obj = Flight(country_num, incoming, outgoing)
        flight_list.append(flight_obj)

    out_file = open('travel_restrictions_output.txt', 'w')

    for f in range(0, flight_num):
        out_file.write('Case #{}:\n'.format(f+1))
        country_num = flight_list[f].country_num
        incoming = flight_list[f].incoming
        outgoing = flight_list[f].outgoing
        for i in range(1, country_num + 1):
            for j in range(1, country_num+1):
                restrict = restriction(path(i, j))
                check = 'N' if 'N' in restrict else 'Y'
                out_file.write(check)
            if f == flight_num - 1 and i == country_num and j == country_num:
                continue
            else:
                out_file.write('\n')
    
    out_file.close()
