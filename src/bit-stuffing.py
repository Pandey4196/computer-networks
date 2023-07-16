def bitStuffing(N, arr):
    brr = [0 for _ in range(30)]
    k = 0
    i = 0
    j = 0
    while (i < N):
        if (arr[i] == 1):
            count = 1
            brr[j] = arr[i]
            k = i + 1
            while True:
                if not (k < N and arr[k] == 1 and count < 5):
                    break
                j += 1
                brr[j] = arr[k]
                count += 1
                if (count == 5):
                    j += 1
                    brr[j] = 0
                i = k
                k += 1
        else:
            brr[j] = arr[i]
        i += 1
        j += 1
    print("The bit-stuffed binary message is: ",end="")
    for i in range(0, j):
        print(brr[i], end="")


if __name__ == "__main__":
    x = input("Enter the binary message: ")
    n = len(x)
    Arr = []
    for i in x:
        Arr.append(int(i))
    bitStuffing(n, Arr)
