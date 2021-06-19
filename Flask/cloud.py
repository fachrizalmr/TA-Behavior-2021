plus = 0
count = 0
for i in range(24):
    counter = "elif jam == "
    for j in range(12):
        test = i
        if plus == 55:
            print(counter, test, "and menit >= ",
                  plus, " and menit <= ", 0, ":")
            plus = 0
            print("     now = ", count+1, "\n")
            count = count+1

        else:
            print(counter, test, "and menit >= ",
                  plus, " and menit <= ", plus+5, ":")
            plus = plus + 5
            print("     now = ", count+1, "\n")
            count = count+1
