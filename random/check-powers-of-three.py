def checkPowersOfThree(n: int) -> bool:
    def backtrack(c, visited, powers, n):
        print(c)
        if c == n:
                return True
        for i in range(len(powers)):
            if not visited[i]:
                visited[i] = True
                backtrack(c + powers[i], visited, powers, n)
                visited[i] = False
                return False
        powers = []
        for i in range(16):
            powers.append(3**i)
        visited = [False]*16
        return backtrack(0, visited, powers, n)


def main():
    print(checkPowersOfThree(12))


if __name__ == "__main__":
    main()
