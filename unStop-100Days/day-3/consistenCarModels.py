# def carModels (allowed : str , models : list) -> list :
#     result = []
#     for each in models:
#         if all(i in allowed for i in each):
#             result.append(each)
        
#     return result

# print(carModels("emta", ["etmb", "e", "et", "eam", "mtb", "akm"]))
# print(carModels("abcdef", ["ad" ,"bd" , "aaab" ,"baa" ,"badab" ,"asd" , "e" ,"f"]))




def count_consistent_cars(components, n, models):
    print(models)
    result = []
    counter = 0
    for each in models:
        if all(i in components for i in each):
            result.append(each)
            counter += 1 

    print(result)
    return counter

if __name__ == '__main__':
    components = input().strip()
    n = int(input().strip())
    models = list(map(str, input().strip().split(" ")))
    result = count_consistent_cars(components, n, models)
    print(result)