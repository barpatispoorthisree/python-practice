var = int(input())
num_list = [(10, 20, 30), (1, 2), (5, 10, 15, 45)]
num_list[0] = num_list[0][:-1] +(var,)
num_list[1] = num_list[1][:-1] +(var,)
num_list[2] = num_list[2][:-1] +(var,)

print(num_list)
