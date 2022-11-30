'''Binery Search'''

def binerySearch(_list, search_item):
    low = 0
    high = len(_list) - 1
    search_result = False
    
    while low <= high and search_result != True:
        mid = (low + high) // 2
        guess = _list[middle]
        
        if guess == search_item:
            search_result = True
            return search_result
        
        if guess > search_item:
            high = mid - 1
        
        else:
            low = mid + 1
        
    return search_result
