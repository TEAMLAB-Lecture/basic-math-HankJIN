#######################
# Basic Math          #
#######################

"""
여기서 간단한 수학을 하는 프로그램을 만들것입니다. 
"""


def get_greatest(number_list):
    number_list.sort()
    greatest_number = number_list[-1]
    return greatest_number


def get_smallest(number_list):
    number_list.sort()
    smallest_number = number_list[0]
    return smallest_number


def get_mean(number_list):
    cnt = len(number_list)
    sum = 0
    for item in number_list :
        sum += item
    mean = sum/cnt
    return mean


def get_median(number_list):
    cnt = len(number_list)
    number_list.sort()
    if cnt%2==1:
        median = number_list[cnt//2]
    else :
        median = (number_list[cnt//2-1] + number_list[cnt//2])/2
    return median