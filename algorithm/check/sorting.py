# Sequence sort checker
def is_sorted(data: list):
    """
    Checks whether sequence has ascending sorting
    :param data: list sequence
    :return:
    """
    sort_status = False
    if len(data) <= 1:
        sort_status = True
        return data
    elif len(data) > 1 and sort_status is False:
        scope = len(data) - 1
        for n in range(scope - 1):
            if data[scope] > data[scope - 1]:
                scope -= 1
                sort_status = True
            else:
                sort_status = False
                break
        if scope == 1 and sort_status is True:
            print('Data is sorted')
            return data
        else:
            print('Data is not sorted')
            return data


