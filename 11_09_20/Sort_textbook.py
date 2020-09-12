#HELP! Jason can't find his textbook! It is two days before the test date,
# and Jason's textbooks are all out of order!
# Help him sort a list (ArrayList in java) full of textbooks by subject, so he can study before the test.
#The sorting should NOT be case sensitive
def sorter(textbooks):
    #Cramming before a test can't be that bad?
    return sorted(textbooks, key = str.lower)


print(sorter(['Algebra', 'History', 'Geometry', 'English']))     #'Does not sort strings'
print(sorter(['Algebra', 'history', 'Geometry', 'english']))     #'Does not handle capitalization'
print(sorter(['Alg#bra', '$istory', 'Geom^try', '**english']))   #'Does not handle symbols'
