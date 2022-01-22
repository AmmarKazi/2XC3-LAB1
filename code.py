def are_valid_groups(groups, studentNumbers):
    nest = [i for group in groups for i in group]
    ans = all(student in nest for student in students)

    if ans:
        return True  
    else:
        return False
