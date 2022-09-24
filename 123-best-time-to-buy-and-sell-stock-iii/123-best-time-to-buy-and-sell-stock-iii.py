class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)

        # cache = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n+1)]
        prev = [[0 for _ in range(3)] for _ in range(2)]
        
        
        for idx in range(n-1, -1, -1):
            curr = [[0 for _ in range(3)] for _ in range(2)]
            for lastBought in [True, False]:
                for totalSales in range(2):
                    if not lastBought:
                        buy = -prices[idx] + prev[True][totalSales]
                        notBuy = prev[False][totalSales]

                        curr[lastBought][totalSales] = max(buy, notBuy) 

                    elif lastBought:
                        curr[lastBought][totalSales] = max(
                            prices[idx] + prev[False][totalSales+1],
                            prev[lastBought][totalSales])

            prev = curr.copy()

        
        return prev[False][0]
                    
                    
                    
        
#         def solve(idx, lastBought, totalSales):

#             if idx >= n: return 0
#             if totalSales >= 2: return 0
#             if cache[idx][lastBought][totalSales] != -1: return cache[idx][lastBought][totalSales]

#             if not lastBought:
#                 buy = -prices[idx] + solve(idx+1, True, totalSales)
#                 notBuy = solve(idx+1, False, totalSales)
                
#                 cache[idx][lastBought][totalSales] = max(buy, notBuy)
#                 return cache[idx][lastBought][totalSales] 
            
#             elif lastBought:
#                 cache[idx][lastBought][totalSales] = max(
#                     prices[idx] + solve(idx+1, False, totalSales + 1),
#                     solve(idx+1, lastBought, totalSales)
#                 )
#                 return cache[idx][lastBought][totalSales]

#             return float('-inf')
        
#         return solve(0, False, 0)