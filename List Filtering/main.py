def filter_list(l):
    filtered_array = []
    for i in l: 
        if type(i) is int: #filter
            filtered_array.append(i);
    
    return filtered_array
