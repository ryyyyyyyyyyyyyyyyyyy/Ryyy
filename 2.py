def max_profits(profits):
    if not profits:
        return 0
    if len(profits) == 1:
        return profits[0]

    # 初始化前两个位置的最大收益
    prev2 = profits[0]
    prev1 = max(profits[0], profits[1])

    # 从第三个位置开始遍历
    for i in range(2, len(profits)):
        # 计算当前最大收益
        curr = max(prev1, prev2 + profits[i])
        # 更新
        prev2 = prev1
        prev1 = curr

    return prev1


# 测试输入
profits = [2, 7,9, 3, 1]
result = max_profits(profits)
print(result)

profits = [3,5,4,1]
result = max_profits(profits)
print(result)

#时间复杂度：O（n）