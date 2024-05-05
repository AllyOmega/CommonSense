import math

# 1:

# basketball_players = [
#     {"first_name": "Jill", "last_name": "Huang", "team": "Gators"},
#     {"first_name": "Janko", "last_name": "Barton", "team": "Sharks"},
#     {"first_name": "Wanda", "last_name": "Vakulskas", "team": "Sharks"},
#     {"first_name": "Jill", "last_name": "Moloney", "team": "Gators"},
#     {"first_name": "Luuk", "last_name": "Watkins", "team": "Gators"}
# ]

# football_players = [
#     {"first_name": "Hanzla", "last_name": "Radosti", "team": "32ers"},
#     {"first_name": "Tina", "last_name": "Watkins", "team": "Barleycorns"},
#     {"first_name": "Alex", "last_name": "Patel", "team": "32ers"},
#     {"first_name": "Jill", "last_name": "Huang", "team": "Barleycorns"},
#     {"first_name": "Wanda", "last_name": "Vakulskas", "team": "Barleycorns"}
# ]

# def find_multiple_sports(basketball_players, football_players):
    
#     res = []

#     football_dict = {}

#     for football_player in football_players:

#         football_dict[football_player['first_name']] = football_player['last_name']


#     for basketball_player in basketball_players:

#         if football_dict.get(basketball_player['first_name']) == basketball_player['last_name']:
#             res.append(f"{basketball_player['first_name']} {basketball_player['last_name']}")

    
#     return res


# print(find_multiple_sports(basketball_players, football_players))


# 2:

# def missing_number(num_arr):

#     num_dict = {}

#     for num in num_arr:
#         num_dict[num] = True
    
#     for num in range(len(num_arr) + 1):

#         if not num_dict.get(num):
#             return num
    
#better solution:

# def missing_number(num_arr):

#     full_sum = 0

#     for num in range(1, len(num_arr) + 1):
#         full_sum += num

#     cur_sum = 0

#     for num in num_arr:
#         cur_sum += num

#     return full_sum - cur_sum



# print(missing_number([2, 3, 0, 6, 1, 5]))




# 3:

# def greatest_profit(predicted_prices):

#     max_profit = 0

#     current_min = math.inf

#     for current_price in predicted_prices:

#         current_min = min(current_min, current_price)

#         max_profit = max(max_profit, current_price - current_min)
        


#     return max_profit

# print(greatest_profit([10, 7, 5, 8, 11, 2, 6]))


#4:

# def highest_product(num_arr):

#     max_num1, max_num2 = float('-inf'), float('-inf')
#     min_num1, min_num2 = float('inf'), float('inf')


#     for num in num_arr:
#         if num > max_num1:
#             max_num2 = max_num1
#             max_num1 = num
#         elif num > max_num2:
#             max_num2 = num
        
#         if num < min_num1:
#             min_num2 = min_num1
#             min_num1 = num
#         elif num < min_num2:
#             min_num2 = num
            
    
#     pos_prod = max_num1 * max_num2
    
#     neg_prod = min_num1 * min_num2
    
#     return max(pos_prod, neg_prod)
        
                   
# print(highest_product([5, -10, -6, 9, 4]))

#5

# def sort_temps(temperatures):

#     res = []

#     temp_dict = {}

#     for temp in temperatures:
#         temp_dict[temp] = temp_dict.get(temp, 0) + 1
    
#     for temp in range(970, 991):
#         temp /= 10
#         if temp_dict.get(temp):
#             for _ in range(temp_dict[temp]):
#                 res.append(temp)
    
#     return res

# print(sort_temps([98.6, 98.0, 97.1, 99.0, 98.9, 97.8, 98.5, 98.2, 98.0, 97.1]))


def longest_sequence(num_arr):

    res = 0

    num_dict = {}

    for num in num_arr:

        num_dict[num] = True

    for num in num_dict:
        cur_num = num
        cur_res = 0

        if not num_dict.get(cur_num - 1):
            while num_dict.get(cur_num):
                cur_res += 1

                cur_num += 1
            
            res = max(res, cur_res)
        
    return res

print(longest_sequence([19, 13, 15, 12, 18, 14, 17, 11]))

