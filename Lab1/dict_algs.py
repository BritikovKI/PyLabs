def elderChild(arrOfDicts):
    newArr=[]
    for elem in arrOfDicts:
        for child in elem["children"]:
            if(child["age"]>18):
                newArr.append(elem["name"])
                break
    return(newArr)

ivan = {"name":"ivan","age":34,"children":
    [{"name":"Vasja","age":12,}, {"name":"Petja","age":10, }],
}

darja = {"name":"darja","age":41,"children":
    [{"name":"Kirill","age":21,}, {"name":"Pavel","age":15, }],
}





emps=[ivan,darja];

print(elderChild(emps))