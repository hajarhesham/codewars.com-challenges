def my_languages(results):
    li = list()
    for key,value in sorted(results.items(),key=lambda x: x[1],reverse=True):
        if value >= 60:
            li.append(key)
    return li 
