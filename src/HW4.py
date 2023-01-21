# Task 1
# Տրված է թվաբանական պրոգրեսիայի առաջին և երկրորդ անդամները։ Տրված n֊ի համար, վերադարձնել այդ պրոգրեսիայի n֊րդ անդամը։

def progression(a1, a2, n):
    d = a2 - a1
    a_n = a1 + (n - 1) * d
    return f"a[{n}]={a_n}"

# Task 2
# CodeMaster-ը նոր է վերադարձել գնումներից։ Նա սկանավորեց իր գնած ապրանքների չեկը և ստացված շարանը տվեց
# Ratiorg֊ին՝ պարզելու գնված ապրանքների ընդհանուր թիվը: Քանի որ Ratiorg-ը բոտ է, նա անպայման պատրաստվում է
# այն ավտոմատացնել, ուստի նրան անհրաժեշտ է ծրագիր, որը կամփոփի բոլոր թվերը, որոնք հայտնվում են տվյալ մուտքագրում:
# Օգնեք Ratiorg-ին՝ գրելով ֆունկցիա, որը վերադարձնում է տվյալ inputString-ում հայտնված թվերի գումարը։


def ratiorg(a):
    total = 0
    b = a.split(" ")
    for i in range(len(b)):
        if b[i].isnumeric():
            total += int(b[i])
    return total

# Task 3
# Մուտքագրեք երեք ամբողջ թիվ: Տպեք «Տեսակավորված» բառը, եթե թվերը նշված են աճող կամ նվազող հերթականությամբ,
# իսկ «Չտեսակավորված» հակառակ դեպքում:


def is_sorted(a, b, c):
    if (a < b and b < c) or (a > b and b > c):
        print("Sorted")
    else:
        print("Unsorted")

# TASK 4
# Գրել ֆունկցիա, որը տրված բնական թվի համար կստուգի, արդյոք այն կատարյալ թիվ է, թե ոչ։
# Հ․Գ Թիվը կոչվում է կատարյալ, եթե այն հավասար է իր բաժանարարների գումարին։


def is_perfect(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    if total == n:
        return True
    return False

# TASK 5
# Գրել ծրագիր, որը տրված թվային արժեքներով ցուցակի համար, կհաշվի նրա էլեմենտների գումարը։


def sum_of_elements(list1):
    total = 0
    for item in list1:
        total += item
    return total

# TASK 6
# Գրել ֆունկցիա, որը տրված թվային արժեքներով ցուցակի համար, կվերադարձնի այդ ցուցակի ամենամեծ էլեմենտը։


def max_list(list1):
    max_element = list1[0]
    for item in list1:
        if max_element < item:
            max_element = item
    return max_element

# TASK 7
# Գրել ֆունկցիա, որը տրված ցուցակից կջնջի տրված արժեքին հավասար բոլոր էլեմենտները։


def delete(list1, value):
    return [i for i in list1 if i != value]

# TASK 8
# Գրեք ֆունկցիա որը կվերադարձնի տրված թվային արժեքներով ցուցակի բոլոր էլեմենտների արտադրյալը։


def product_of_elements(list1):
    product = 1
    for i in list1:
        product *= i
    return product

# TASK 9
# Գրեք ֆունկցիա՝ տողը հակադարձելու համար, եթե դրա երկարությունը 4-ի բազմապատիկ է։


def reverse(str1):
    if len(str1) % 4 == 0:
        return str1[::-1]

# TASK 10
# Գրեք ֆունկցիա՝ որը տրված բնական n թվի համար վերադարձնում է Ֆիբոնաչիի n-րդ անդամը։
# Խնդիրը լուծել և ռեկուրսիվ, և իտերատիվ մեթոդներով։


def fib_recursive(n):
    if n <= 0:
        return "Invalid number"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n):
    f_1 = 0
    f_2 = 1
    if n <= 0:
        return "Invalid number"
    elif n == 1:
        return f_1
    elif n == 2:
        return f_2

    for i in range(1, n):
        f_1, f_2 = f_2, f_1 + f_2
    return f_1

# TASK 11
# Գրել ֆունկցիա, որը տրված 2 բնական թվերի համար կվերադարձնի նրանց ամենափոքր ընդհանուր բազմապատիկը։


def least_common_multiple(a, b):
    if a > b:
        largest = a
    else:
        largest = b
    while True:
        if (largest % a == 0) and (largest % b == 0):
            result = largest
            break
        largest += 1
    return result

# TASK 12
# Գրեք python ծրագիր՝ նշված թվի հաջորդ ամենափոքր պալինդրոմը գտնելու համար: Օրինակ 119-ի համար հաջորդ պալինդրոմը 121 է


def is_palindrome(num):
    str1 = str(num)
    if str1 == str1[::-1]:
        return True
    return False


def next_palindrome(num):
    while True:
        if is_palindrome(num):
            return num
        num = num + 1

# TASK 13
# Ռոբոտը կանգնած է ուղղանկյուն ցանցի վրա և ներկայումս գտնվում է կետում (X0, Y0): Կոորդինատները ամբողջ թիվ են։
# Այն ստանում է N հեռակառավարման հրամաններ: Յուրաքանչյուր հրաման մեկն է՝ վեր, վար, ձախ, աջ: Ճիշտ հրաման
# ստանալուց հետո ռոբոտը մեկ միավոր է տեղափոխում տվյալ ուղղությամբ։ Եթե ռոբոտը սխալ հրաման է ստանում,
# նա պարզապես անտեսում է այն: Որտե՞ղ է գտնվելու ռոբոտը բոլոր հրամաններին հետևելուց հետո:
# Ուշադրություն: աջը՝ x0+1, ձախը՝ x0-1, վերևը՝ y0+1, ներքևը՝ y0-1։


def position(moves):
    x_0, y_0 = 0, 0
    for i in range(len(moves)):
        if moves[i] == 'R':
            x_0 += 1
        elif moves[i] == 'L':
            x_0 -= 1
        elif moves[i] == 'U':
            y_0 += 1
        elif moves[i] == 'D':
            y_0 -= 1
    return x_0, y_0

# TASK 14
# Ստուգեք, արդյոք 2 ցուցակները 1-քայլ ցիկլիկ են:
# Օրինակ
# Ցուցակ1 = [1,2,3,4,5,6]
# Ցուցակ2 = [6,1,2,3,4,5]
# Վերադարձել True


def is_one_step_cycle(list1, list2):
    list1.extend(list1)
    for i in range(len(list1)):
        if list2 == list1[i:i + len(list2)]:
            return True
    return False

# TASK 15
# Գրել ծրագիր, որը ստանւմ է թիվ, գտեք առավելագույն թիվը, որը կարող եք ստանալ՝
# ջնջելով տվյալ թվի ուղիղ մեկ թվանշանը:


def delete_digit(num):
    str1 = str(num)
    min_index = 0
    for i in range(1, len(str1)):
        if(int(str1[i])) < int(str1[min_index]):
            min_index = i
    return int(str1[:min_index] + str1[min_index + 1:])

# TASK 16
# Գրեք ֆուկցիա որը ստանում է tuple տիպի օբյեկտ և վերադարձնում նոր tuple բաղկացած միայն առաջին tuple֊ի թվերից։t


def numbers(tuple1):
    tuple2 = ()
    for i in tuple1:
        if isinstance(i, (int, float)):
            tuple2 += (i,)
    return tuple2

# TASK 17
# Գրեք Python ֆուկցիա որը ստանում է tuple և ցանկացաց տիպի օբյեկտ և ավելացնում է ստացած արժեքը tuple մեջ։


def add_object(tuple1, a):
    return tuple1 + (a,)

# TASK 18
# Գրեք Python ֆուկցիա որը ստանում է tuple դարձնում է string։ Tuple֊ի էլեմենտները ստրինգում
# պետք է բաժանված լինեն ‘-’ նշանով։


def tuple_string(tuple1):
    str1 = str(tuple1[0])
    for i in range(1, len(tuple1)):
        str1 += "-" + str(tuple1[i])
    return str1

# TASK 19
# Գրեք Python ֆուկցիա որը ստանում է list և պետքա գտնել նրա երկարությունը առանց len() ֆունկցիա֊ի օգտագորձմամբ։


def list_len(list1):
    count = 0
    for i in list1:
        count += 1
    return count

# TASK 20
# Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky
# if the sum of the first half of the digits is equal to the sum of the second half.
# Given a ticket number n, determine if it's lucky or not. Not using: string, list, tuple, set types.


def number_of_digits(n):
    count = 0
    while n != 0:
        n = n // 10
        count += 1
    return count


def is_lucky(n):
    count = 0
    half = number_of_digits(n) / 2
    n1 = n // (10 ** half)
    sum1 = 0
    sum2 = 0
    while count < half:
        sum1 += n % 10
        sum2 += n1 % 10
        n = n // 10
        n1 = n1 // 10
        count += 1
    if sum1 == sum2:
        return True
    return False

# TASK 21
# Euler function is return a count of numbers not greater than N, which are mutually simple with N.


def greatest_common_divisor(a, b):
    result = 0
    if a > b:
        smallest = b
    else:
        smallest = a
    for i in range(1, smallest + 1):
        if (a % i == 0) and (b % i == 0):
            result = i
    return result


def euler(n):
    count = 0
    for i in range(1, n):
        if greatest_common_divisor(i, n) == 1:
            count += 1
    return count

# TASK 22 *
# You are given a 0-indexed string array words, where words[i] consists of lowercase English letters.
# In one operation, select any index i such that 0 &lt; i &lt; words.length and words[i - 1] and words[i] are anagrams,
# and delete words[i] from words. Keep performing this operation as long as you can select an index that satisfies
# the conditions. Return words after performing all operations. It can be shown that selecting the indices for
# each operation in any arbitrary order will lead to the same result. An Anagram is a word or phrase formed by
# rearranging the letters of a different word or phrase using all the original letters exactly once.


def anagram(words):
    i = 0
    while i < len(words):
        if sorted(words[i]) == sorted(words[i - 1]):
            del words[i]
        else:
            i += 1
    return words

# TASK 23 *
# You are given an array of strings names, and an array heights that consists of distinct positive integers.
# Both arrays are of length n. For each index i, names[i] and heights[i] denote the name and height of the ith person.
# Return names sorted in descending order by the people's heights.


def sorted_names(names, heights):
    for i in range(1, len(names)):
        if heights[i] > heights[i - 1]:
            temp1 = heights[i]
            heights[i] = heights[i - 1]
            heights[i - 1] = temp1
            temp2 = names[i]
            names[i] = names[i - 1]
            names[i - 1] = temp2
    return names

# TASK 24 *
# In a special ranking system, each voter gives a rank from highest to lowest to all teams participating in the
# competition. The ordering of teams is decided by who received the most position-one votes. If two or more teams
# tie in the first position, we consider the second position to resolve the conflict, if they tie again, we continue
# this process until the ties are resolved. If two or more teams are still tied after considering all positions,
# we rank them alphabetically based on their team letter.
# You are given an array of strings votes which is the votes of all voters in the ranking systems. Sort all teams
# according to the ranking system described above. Return a string of all teams sorted by the ranking system.
