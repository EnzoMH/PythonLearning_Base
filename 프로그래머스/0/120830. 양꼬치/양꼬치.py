def solution(n, k):    
    price_food = n * 12000		#1
    
    if n >= 10:					#2
        price_drink = (k - n // 10) * 2000	#3 
    else :
        price_drink = k * 2000		#4
    
    answer = price_food + price_drink	#5
    return answer

# def solution(n, k):
#     service = n//10
#     drink = max(0, k-service)
#     return (12000*n)+(2000*drink)

# def solution(n, k):
#     return 12000 * n + 2000 * (k - n // 10)