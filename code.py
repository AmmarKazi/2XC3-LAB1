def are_valid_groups(groups, studentNumbers):
<<<<<<< HEAD
    flatten = [x for y in groups for x in y]
    check1 =  all(item in flatten for item in studentNumbers)
    check2 = all(item in studentNumbers for item in flatten)
    if check1 and check2 != True:
        return True
    else:
=======
    flatgroups = [element for sublist in groups for element in sublist]
    check =  all(item in flatgroups for item in studentNumbers)
    check2 =  all(item in studentNumbers for item in flatgroups)
    if (check is True and check2 is True):
        return True  
    else :
>>>>>>> b6b7a6298508d6ad45a757e3381db4ca250740f0
        return False
print(are_valid_groups([[1,2,3],[4,5,6],[7,8,9]], [1,2,3,4,5,6,7,8,9]))