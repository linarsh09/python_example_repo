#10
#Task_1/2(II попытка)
1.
slovo_1 = input().lower()
slovo_2 = input().lower()

if len(slovo_1) != len(slovo_2):
    print("не анаграммы")
else:
    anagramm = True

    for char in slovo_1: 
        if slovo_1.count(char) != slovo_2.count(char):
            anagramm = False
            break
            
    if anagramm:
        print("анаграммы")
    else:
        print("НЕ АНАГРАММЫ")



2.
def funkcyia(k, n):
    if k > n:
        return 0
    part = 1 / ((2 * k + 1) * (2 * k + 1))
    return part + funkcyia (k + 1, n)
n = int(input("Пж n введите: "))
result_of_sum = funkcyia (1, n)
print(result_of_sum)