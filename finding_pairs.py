def get_unique_pairs(int_list,pair_sum):
    stop_index = len(int_list)
    unique_pairs_set = set()
    for cur_index in range(stop_index):
        num_1 = int_list[cur_index]
        num_2 = pair_sum - num_1
        remaining_list = int_list[cur_index + 1:]
        if num_2 in remaining_list:
            pair = (num_1 , num_2)
            pair = tuple(sorted(pair))
            unique_pairs_set.add(pair)
    return unique_pairs_set
            
            
def convert_str_ti_int (str_num_list):
    new_list= []
    for item in (str_num_list):
        num_list = int(item)
        new_list.append(num_list)
    return new_list
        
        
str_num_list = input().split(",")
pair_sum = int(input())
int_list = convert_str_ti_int(str_num_list)
unique_pairs =  get_unique_pairs(int_list,pair_sum)
for pair in unique_pairs:
    print(pair)

