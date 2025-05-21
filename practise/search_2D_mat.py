import time 
from abhishek import *
def seach_in_2d_mat(mat : list, target : int) -> bool:
    start_time = time.time()
    for i in range(len(mat)):
        each = mat[i]
        if target >= each[0] and target  <= each[-1]:
            if target in each:
                end_time = time.time()
                print(runtime(start_time, end_time))
                print(f"found at -> {i},{each.index(target)}")
                return True 
    end_time = time.time() 
    print(runtime(start_time, end_time))
    return False 
    

print(seach_in_2d_mat([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 11 ))
print(seach_in_2d_mat([[  1,  2,  3,  4,  5,  6,  7,  8,  9, 10],
 [ 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
 [ 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
 [ 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
 [ 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
 [ 51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
 [ 61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
 [ 71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
 [ 81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
 [ 91, 92, 93, 94, 95, 96, 97, 98, 99,100]], 15))

