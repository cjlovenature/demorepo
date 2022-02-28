def sameJson(json1,json2):
    keys1 = set(json1.keys())
    keys2 = set(json2.keys())
    if keys1 != keys2:
        return False
    else:
        flag = True
        for key in keys1:
            if type(json1[key])!= type(json2[key]):
                flag = False
                break 
        return flag
  