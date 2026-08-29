def column_correct(soduku:list, column_no: int):
    new_list = []
    for row in soduku:
        new_list.append(row[column_no])

    seen = []
    for num in new_list:
        if num == 0:
            continue
        else:
            if num not in seen:
                seen.append(num)
            else:
                return False

    return True


    print
