#Given an array of integers.
# Return an array, where the first element is the count of positives numbers
#  and the second element is sum of negative numbers.
# If the input array is empty or null, return an empty array.

def count_positives_sum_negatives(arr):

    count_positives = 0
    sum_negatives = 0
    if not arr:
        return []
    for next in arr:
        if next > 0 :
            count_positives+= 1
        elif next < 0 :
            sum_negatives+= next
    return [count_positives,sum_negatives]


#print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))   #[10,-65]
print(count_positives_sum_negatives([])) #[]
print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14])) #,[8,-50]
print(count_positives_sum_negatives([-1])) #[]


#Another Variant
#if not arr: return arr
#    return [sum(1 for x in arr if x > 0), sum(x for x in arr if x < 0)]