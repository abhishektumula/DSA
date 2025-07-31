#https://unstop.com/code/challenge-assessment/250196?moduleId=372

#task is to find the youngest one who receives gifts from everynone but doesnt give any..

# def youngerChild(members , giftsExchanged, exchanges : list) -> int :
#     gave = set()
#     received_from = {}

#     for giver, receiver in exchanges:
#         gave.add(giver)

#         if not receiver in received_from.items():
#             received_from[receiver] = set()

#         received_from[receiver].add(gave)

#     for i in range(1, members + 1):
#         if i not in gave and len(received_from.get(i, set())) == members - 1:
#             return i 

#     return -1 

def youngerChild(members , giftsExchanged, exchanges : list) -> int :
    gave = set()
    received_from = {}

    for giver, receiver in exchanges:
        gave.add(giver)

        if not receiver in received_from.items():
            received_from[receiver] = set()

        received_from[receiver].add(gave)

    for i in range(1, members + 1):
        if i not in gave and len(received_from.get(i, set())) == members - 1:
            return i 

    return -1 


from collections  import defaultdict 
def youngChildren (membres, giftsExchanged, exchanges : list) -> int :
    gave = set()
    exc = defaultdict(set)
    for giver, taker in exchanges:
        gave.add(giver)
        if taker  not in exc:
            exc[taker] = set() 
        exc[taker].add(giver)

    for i in range(1, membres + 1):
        if i not in gave and len(exc.get(i, set(0))) == membres - 1:
            return i 
        
    return - 1




