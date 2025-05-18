import time 
#approach : brute force 
def best_time_to_buy_andsell(prices : list) -> int:
    profit = 0
    start = time.time()
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            profit = max(profit, prices[j] - prices[i])
    end_time = time.time()
    print(f"runtime:{(end_time - start)*1000:.3f}")
    return profit


print(best_time_to_buy_andsell([10,1,5,6,7,1]))


