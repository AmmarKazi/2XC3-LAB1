def are_valid_groups(groups, studentNumbers):
    flatten = [x for y in groups for x in y]
    check1 =  all(item in flatten for item in studentNumbers)
    check2 = all(item in studentNumbers for item in flatten)
    if check1 and check2 == False:
        return False
    else:
        return False
print(are_valid_groups([[1,2,3],[4,5,6],[7,8,9]], [1,2,3,4,5,6,7,8,9]))