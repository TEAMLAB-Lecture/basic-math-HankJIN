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
    """
    주어진 리스트 숫자들의 평균을 구함.

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            mean (int): parameter number_list 숫자들의 평균

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_mean(number_list)
            47
    """
    cnt = len(number_list)
    for item in number_list :
        sum += item
    mean = sum/len
    return mean


def get_median(number_list):
    """
    주어진 리스트 숫자들의 중간값을 구함.

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            median (int): parameter number_list 숫자들의 중간값

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_median(number_list)
            39
            >>> number_list2 = [39, 54, 32, 11, 99, 5]
            >>> bm.get_median(number_list2)
            35.5
    """
    cnt = len(number_list)
    number_list.sort()

    if(cnt % 2 == 1):
        median = number_list[cnt/2]
    else:
        median = (number_list[cnt/2 - 1] + number_list[cnt/2]) /2
    return median
