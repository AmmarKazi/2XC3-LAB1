def are_valid_groups(groups, studentNumbers):
    flatgroups = [element for sublist in groups for element in sublist]
    check =  all(item in flatgroups for item in studentNumbers)
    check2 =  all(item in studentNumbers for item in flatgroups)
    if (check is True and check2 is True):
        return True  
    else :
        return False

print(are_valid_groups([[1,2,3],[4,5,6],[7,8,9]], [1,2,3,4,5,6,7,8,9]))

