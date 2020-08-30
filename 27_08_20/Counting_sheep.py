#Consider an array/list of sheep where some sheep may be missing from their place.
# We need a function that counts the number of sheep
# present in the array (true means present).  Variant I like : return array_of_sheep.count(True)

def count_sheeps(sheep):
    count=0
    for next in sheep:
        if next:
            count+=1
        else : continue
    return  count

array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  None,  True ,
          False, False, True,  True]

print(f"There are {count_sheeps(array1)} sheeps in total")
#print(count_sheeps(array1), 17, "There are 17 sheeps in total, not %s" % count_sheeps(array1))