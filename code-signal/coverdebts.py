def coverDebts(s, debts, interests):
    items = list(zip(interests, debts))
    items.sort(reverse=True)
    n = len(items)
    ans = 0
    for i in range(len(debts)):
        items[i] = list(items[i])
    while True:
        amount = s*0.1
        isEmpty = True
        for i in range(n):
            if items[i][1] > 0:
                isEmpty = False
                if items[i][1] > amount:
                    items[i][1] -= amount
                    ans += amount
                    break
                else:
                    amount -= items[i][1]
                    ans += items[i][1]
                    items[i][1] = 0
        if isEmpty:
            break
        else:
            for i in range(n):
                if items[i][1] > 0:
                    items[i][1] += items[i][1]*(items[i][0]*0.01) 
    return ans


def main():
    print(coverDebts(50, [2,2,5], [200, 100, 150]))

if __name__ == "__main__":
    main()
