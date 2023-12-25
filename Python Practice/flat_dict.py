def flat_dict(nested_dict):
    dictn={}
    for key,value in nested_dict.items():
        if isinstance(value,dict):
            dictn[key] = None
            for k in value:
                dictn[k] = value[k]
        else:
            dictn[key] = value

    return dictn

print(flat_dict({'a':{'b':1},'c':2}))