def find_highscore(data, n):
    high_score = 0
    data = sorted(data,reverse=True)
    for i in range(len(data)):
        if data[i] > data[i+1]:
            high_score = data[i + 1]
            break
    return high_score

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split(" "))
    arr = list(arr)
    print(find_highscore(arr,n))