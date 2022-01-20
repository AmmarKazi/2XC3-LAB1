def are_valid_groups(groups, studentNumbers):
    
    flatGroups = [x for y in groups for x in y]
    
    check1 =  all(item in flatGroups for item in studentNumbers)
    check2 = all(item in studentNumbers for item in flatGroups)

    if check1 and check2 == True:
        return True
    else:
        return False

print(are_valid_groups([[1,2,3],[4,5,6],[7,8]], [1,2,3,4,5,6,7,8]))