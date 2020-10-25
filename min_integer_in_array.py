# given a list of integers return the minimum 
# integer missing from the list
def solution(a):
    # you could use the original list
    # my reasoning for creating  set out
    # of the original list was to make the
    # search for the elements faster as a
    # set does not contain duplicates
    # for example given a=[1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,,2,2,2,2,2,2]
    # a set will only contain the elements {1,2}
    set_of_integers = set(a)
    set_max = max(set_of_integers)
    if set_max <= 0:
        return 1
    for i in range(set_max + 1):
        current_value = i + 1
        if current_value in set_of_integers:
            continue
        else:
            return current_value


assert solution([1, 2, 3]) == 4
assert solution([1, 1, 1]) == 2
assert solution([-1, -2, -3]) == 1
assert solution([0, 0, 0]) == 1
assert solution([-2,-1,1,2,3,4, 9, 10, 19]) == 5
assert solution([1, 2, 3, 4, 5, 6, 9, 10, 19]) == 7
print('Ok!')

