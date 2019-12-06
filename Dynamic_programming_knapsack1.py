# knapsack problem1: Define a package with capacity C, there are N items with weight[i] and values[i].
# How to maximize the value of the knapsack?
# Dynamic programming, time complexity : O(C*N), space complexity: O(N)

Capacity=15
Weight=[5,4,7,2,6]
Value=[12,3,10,3,6]
DP=[[0 for _ in range(Capacity)] for _ in range(len(Weight)+1)]

#Do not forget to set inital state... size(DP)=(N+1)*C
for i in range(len(Weight)):
    for j in range(Capacity):
        if Weight[i]<=j:
            DP[i+1][j]=max(DP[i][j],DP[i][j-Weight[i]]+Value[i])
        else:
            DP[i+1][j]=DP[i][j]

print(DP[-1][-1])
