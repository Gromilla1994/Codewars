# Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the two
#  arrays have the "same" elements, with the same multiplicities (the multiplicity of a member is the
#  number of times it appears). "Same" means, here, that the elements in b are the elements in a squared,
#  regardless of the order.

def comp(array1: list, array2: list):
    if array1 == None or array2 == None:
        return False

    new_arr = [i**2 for i in array1]

    for i in range(len(array2)):
        the_same = False
        for j in range(len(array1)):
            if new_arr[j] == array2[i] and new_arr.count(new_arr[j]) == array2.count(array2[i]):
                the_same = True

        if not(the_same):
            return False

    return True


a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

print(comp(a1, a2))
