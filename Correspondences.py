#######
#10/01/2018
#######


import random
from collections import Counter

#168-wordlists, first phoneme
#the symbol '-' encodes polymorphism as opposed to double articulation
#the symbol 'V' encodes vowels

Mon = ["b-V", "n", "x", "g", "d", "t", "V-t", "V", "V", "V",
          "x", "Z", "V-b", "n-V", "S-n", "V", "x", "x", "V", "z",
           "S", "n", "b", "m", "V-x", "m", "V", "Z", "V", "n",
           "V", "x", "c", "V-n", "V", "V", "m", "c", "y", "V",
          "V", "V-b", "s", "V", "V", "t", "C", "n", "x", "V", #50
          "S", "x", "x", "x", "V", "g", "d", "g", "NA", "x",
       "n", "z", "V", "V", "x", "n", "b", "V", "V", "V",
           "V-x", "s-d", "m", "b", "V", "V", "V-n", "V", "V", "b-z",
           "V", "c",  "V-h", "x", "x", "m", "m-V", "s", "n", "V",
           "V", "x", "s", "z", "V", "V", "V", "b", "S", "V", #100
            "V", "V",  "t", "t-C", "x-S", "V-b", "V", "t", "x", "NA",
           "n-t", "x", "V", "x", "x", "n", "s", "V", "V",  "b",
            "g", "n", "d-t", "d", "C", "V", "t", "V", "m", "V-t",
          "s", "c",  "m", "V", "g", "V", "S", "z",  "V", "V",
           "n", "S", "c", "x", "S", "V", "Z", "b-d", "x", "d", #150
          "S", "x", "s", "m", "y", "b-x", "S", "d",  "x", "m",
            "g", "n", "x", "z", "V", "b", "z", "n"]

Man = ["g", "V", "j", "V", "d", "s", "V", "g", "V-l", "j-f",
          "V", "V", "f", "V", "n", "NA", "n", "j", "V", "n",
          "g-C", "V", "C", "m", "V-b", "m", "b-w", "t", "V", "V",
           "f-d", "n", "V", "V-n", "f", "s", "y", "s", "g", "t",
           "V", "V", "V", "f", "f", "V", "S", "y", "V", "V", #50
          "w", "V", "x", "b", "t", "g", "V", "NA", "d", "m",
           "f", "n", "V", "j", "s", "C", "j-f", "f-V", "V", "V",
          "s", "d", "s", "g", "w", "g-V", "V", "b", "b", "V",
        "V-t", "t", "f", "d", "t", "w", "f", "V", "d",  "y",
         "j", "d", "t", "V", "f", "t", "b", "j", "x",  "m", #100
          "V", "m", "t", "V", "m", "x", "V", "t", "x-s",  "V",
          "V", "d", "V", "g", "V-d", "S", "b", "V", "m",  "V",
          "b", "V-t", "m-n", "NA", "w", "y", "n", "t", "t", "V",
          "V", "n", "j", "NA", "t", "f", "d", "j", "V", "f",
          "n", "s", "NA", "s", "d", "V", "V", "b-x", "S", "j", #150
           "V", "f", "s", "V", "n", "n-l", "s", "m",   "d", "m",
         "b", "V", "V", "t", "x", "V", "x", "g"]

Tur =  ["NA", "b", "V", "V", "d", "b", "b", "V", "g", "k",
           "V", "k", "k", "d", "V", "V", "k", "C", "NA", "b",
           "k", "k-V", "b", "y", "k", "V", "V", "y", "NA", "y",
            "k", "k", "C", "V",  "V", "d", "V", "k", "k", "y",
           "y", "b", "k", "t",  "k-s", "b", "k", "g", "b", "V",#50
           "d", "d", "t", "V",  "d", "V", "k", "k", "b", "b",
           "V-s", "y", "V", "y", "V", "t", "k", "V", "s", "g",
           "g", "d", "b", "NA", "k", "k", "V", "y", "V", "s",
           "V", "v", "k", "y", "b", "NA", "k", "y", "V", "y",
         "g", "y", "V", "d", "d", "d", "v", "t", "V", "V", #100
         "y", "s", "C", "V", "V", "b", "d", "s", "s", "s",
            "V", "y", "V", "d", "S", "NA", "V", "y", "s",  "y",
          "V", "g", "d", "t", "t", "k", "t", "b",  "s", "g",
           "y", "k", "b", "d", "NA", "k", "y", "y", "d", "k",
            "y", "s", "V-b", "k-s", "g", "g", "y", "s", "s", "d", #150
        "y", "V", "V", "k", "C", "k", "d", "y",   "NA", "NA",
          "d", "V", "k", "d", "y", "s", "s", "V"]

Eng = ["V", "w", "t", "8", "f", "f", "b", "l", "w", "8",
          "h", "s", "S", "n", "8", "m", "NA", "C", "NA", "f",
           "b", "d", "l", "s", "w",  "t", "NA", "NA", "s", "l",
         "r", "b", "NA", "g", "r", "s", "m", "b", "b", "f",
           "V", "h", "t", "f",  "h", "h", "V", "V", "n", "m", #50
          "t", "t", "f", "f",  "n", "h", "w", "b", "g", "n",
         "b", "h", "d", "V", "b", "s", "NA", "b", "b", "l",
          "s", "h", "n", "8", "s", "f", "s", "l", "d", "f",
           "h", "h", "k", "s", "s", "s", "d", "s", "f",  "w",
          "k", "l", "s", "s", "t", "f", "g", "h", "s",  "r", #100
         "w", "w", "p", "p", "8", "t", "s", "NA", "s", "s",
           "p", "f", "f", "f", "s", "s", "m", "s", "w",  "r",
          "r", "NA", "s", "s", "s", "s", "V", "k", "f", "s",
          "w", "s", "V", "s", "f", "V", "b", "r", "NA", "r",
        "g", "y", "w", "b", "n", "d", "y", "w", "k", "f", #150
          "n", "V", "g", "b", "r", "d", "s", "NA", "S", "d",
           "s", "w", "d", "k", "n", "r", "l", "n"]

Ita = ["V", "V", "d", "t", "k", "C", "g", "l", "l", "s",
          "p", "p", "k", "s", "s", "w", "p", "b", "V", "p",
           "V", "k", "p", "s", "v",  "V", "f", "f", "s", "f",
          "r", "k", "f", "V", "k", "p", "k", "s", "V", "g",
           "w", "k", "k", "p",  "k", "t", "V", "V", "n", "b", #50
          "d", "l", "V", "p",  "j", "m", "V", "p", "V", "k",
         "s", "k",  "b", "m", "m", "s", "v", "s", "r", "r",
          "v", "s", "s", "p", "V", "t", "d", "v", "m",  "k",
         "k", "k", "t", "f", "p", "g", "s", "n", "v", "k",
          "v", "j", "s", "s", "j", "k", "d", "t", "s", "s", #100
          "l", "V", "t", "s", "l", "l", "k", "k", "d",  "k",
          "j", "g", "f", "j", "g", "s", "l", "s", "V", "p",
          "f", "l", "m", "s", "p", "s", "t", "n",  "n", "C",
          "v", "n", "g", "f", "f", "C", "b", "s",  "m", "r",
          "v", "j", "b", "n", "n", "j", "V", "k", "f", "p", #150
           "n", "v", "b", "k", "m", "s", "d", "r", "V", "s",
           "l", "b", "V-s", "k", "v", "d", "s", "n"]

Hin = ["d", "V", "d", "t", "C", "p", "b", "l", "C", "g",
          "bh", "Ch", "NA", "NA", "p", "NA", "NA", "b", "NA", "m",
           "C", "k", "j", "s", "k", "p", "j", "ph", "b", "p",
          "j", "Ch", "ph", "gh", "r", "t", "m", "NA", "h", "C",
           "V", "s", "p", "p", "b", "s", "k", "V", "n", "m", #50
           "d", "j", "n", "p",  "gh", "h", "p", "p", "V", "NA",
          "p", "h",  "p", "kh", "k", "th", "V", "ph", "s", "h",
          "d", "s", "j", "s", "s", "D", "s", "j", "NA", "l",
          "s", "m", "k", "b", "bh", "kh", "kh", "t", "V", "C",
           "V", "l", "b", "kh", "m", "g", "d", "p", "gh", "m", #100
           "dh", "p", "kh", "dh", "ph", "b", "s", "g", "k",  "g",
          "kh", "t", "b", "j", "s", "s", "C", "t", "p", "v",
           "n", "jh", "s", "NA", "p", "r", "dh", "b", "dh", "NA",
           "NA", "NA", "NA", "dh", "V", "r", "j", "s", "p", "l",
           "h", "p", "NA", "k", "r", "d", "NA", "NA",  "Th", "p", #150
         "n", "p", "V", "b", "s", "g", "s", "g",  "t", "k",
          "C", "g", "s", "NA", "n", "d", "b", "n"]

#get a correspondence table
def corr(Ling1, Ling2):
    corr_table = Counter()
    for word1, word2 in zip(Ling1, Ling2):
        # skip in case of missing values
        if word1 == 'NA' or word2 == 'NA':
            continue
        for ph1 in word1.split('-'):
            for ph2 in word2.split('-'):
                corr_table[(ph1, ph2)] += 1
    #optional print: the total number of correspondences
    #print(sum(corr_table.values()))
    return corr_table

#get the phonemic distribution in the two languages
def distr(Ling1, Ling2):
    freq1 = []
    freq2 = []
    for letter1, letter2 in zip(Ling1, Ling2):
        if letter1 == 'NA' or letter2 == 'NA':
            continue
        freq1.extend(letter1.split('-'))
        freq2.extend(letter2.split('-'))
    return [{n: float(freq1.count(n)) for n in freq1}, {n: float(freq2.count(n)) for n in freq2}]

#calculate the binomial formula
def binomialCoeff(n, k):
    result = 1
    for i in range(1, k+1):
        result = result * (n-i+1) / i
    return result

#get the value of the variable 'h' given the four parameters of the hypergeometric formula
def hyper(words, freq1, freq2, corr):
    return binomialCoeff(freq2, corr) * binomialCoeff(words-freq2,freq1-corr) / binomialCoeff(words,freq1)

#detect all significant correspondences (.01 level) given two wordlists
def hyper_final(Ling1, Ling2):
    #calculate the global number of correspondences
    length = 0
    for letter1, letter2 in zip(Ling1, Ling2):
        if letter1 != 'NA' and letter2 != 'NA':
            length += len(letter1.split('-')) * len(letter2.split('-'))
    #get phonemic distributions
    dict_distr1, dict_distr2 = distr(Ling1, Ling2)
    #get correspondence table
    dict_corr = corr(Ling1, Ling2)
    print("Possible correspondences:" + str(len(dict_corr)))
    count=0
    #calculate the cumulative distribution
    for key in dict_corr.keys():
            cumulative = 1.0
            for i in range(dict_corr[key]):
                cumulative = cumulative - hyper(length, int(dict_distr1[key[0]]), int(dict_distr2[key[1]]), i)
            if cumulative < 0.01:
                print(str(key[0]) + ' ' + str(key[1]) + ' ' + str(dict_distr1[key[0]]) + ' ' + str(dict_distr2[key[1]]) + ' ' + str(dict_corr[key]) + ' ' + str(cumulative) + ' ' + str(cumulative*len(dict_corr)))
                count = count + 1
    print("Number of significant correspondences:" + str(count))

#count the number of significan correspondences (.01 level) given two wordlists
def hyper_final_count(Ling1, Ling2):
    length = 0
    for letter1, letter2 in zip(Ling1, Ling2):
        if letter1 != 'NA' and letter2 != 'NA':
            length += len(letter1.split('-')) * len(letter2.split('-'))
    dict_distr1, dict_distr2 = distr(Ling1,Ling2)
    dict_corr = corr(Ling1, Ling2)
    count=0
    for key in dict_corr.keys():
            cumulative = 1.0
            for i in range(dict_corr[key]):
                cumulative = cumulative - hyper(length, int(dict_distr1[key[0]]), int(dict_distr2[key[1]]), i)
            if cumulative < 0.01:
                count = count + 1
    return count

#perform the Monte Carlo experiment on two wordlists
def randomize(Ling1,Ling2):
    num_all = {}
    corr_number= hyper_final_count(Ling1,Ling2)
    for i in range(1000):
        Ling2_rand= random.sample(Ling2, len(Ling2))
        corr = hyper_final_count(Ling1, Ling2_rand)
        if corr not in num_all:
            num_all[corr] = 1
        elif corr in num_all:
            num_all[corr] += 1
    n = 1000
    for i in range(corr_number):
        if i in num_all.keys():
            n = n - num_all[i]
    return n/1000

#experiment on loanwords, Section 8
def simulation1(Ling, borrowings):
    #create two randomized list starting for the input list
    Ling_rand = random.sample(Ling, len(Ling))
    Ling_rand2 = random.sample(Ling, len(Ling))
    p_values = []
    #integer variable needed to determine the saturation threshold. Initialize with any n > len(borrowings)
    threshold = 10
    #perform borrowing experiment by forcing different rates of lexical borrowing, as contained in the list 'borrowings'
    for value in borrowings:
        #create a new language, which is basically Ling_rand2 with some borrowing from Ling_rand
        Ling_contact = Ling_rand[:value] + Ling_rand2[value:]
        #run the Monte Carlo test between the new list and Ling_rand
        p_values.append(randomize(Ling_rand, Ling_contact))
    for index, value in enumerate(p_values):
        #explore the p-values and return the borrowing threshold that yields a positive p-value
        if value < 0.05:
            threshold = index
            break
        if index == 2 and value >= 0.05:
            threshold = 'none'
    print('#')
    return threshold

#calculate Rsquare
def Rsquare(corr_table):
    return sum([(corr_table[key] - 1)**2 for key in corr_table])

#given a distance value and a list of distances, calculate p-value
def pvalue(dist_value, dlist):
    for index, d in enumerate(dlist):
        if dist_value > d:
            return index/10000
    return 1.0


#run the Monte Carlo test
def Kessler(Ling1,Ling2):
    dist_all=[]
    d = Rsquare(corr(Ling1,Ling2))
    for i in range(10000):
        Ling2_rand= random.sample(Ling2, len(Ling2))
        dist_all.append(Rsquare(corr(Ling1,Ling2_rand)))
    dist_all = sorted(dist_all, reverse=True)
    print(round(d, 3), "p =", pvalue(d, dist_all))
    return pvalue(d,dist_all)

#experiment on loanwords, Section 8
def simulation2(Ling, borrowings):
    #create two randomized list starting for the input list
    Ling_rand = random.sample(Ling, len(Ling))
    Ling_rand2 = random.sample(Ling, len(Ling))
    p_values = []
    #integer variable needed to determine the saturation threshold. Initialize with any n > len(borrowings)
    threshold = 10
    #perform borrowing experiment by forcing different rates of lexical borrowing, as contained in the list 'borrowings'
    for value in borrowings:
        #create a new language, which is basically Ling_rand2 with some borrowing from Ling_rand
        Ling_contact = Ling_rand[:value] + Ling_rand2[value:]
        #run the Monte Carlo test between the new list and Ling_rand
        p_values.append(Kessler(Ling_rand, Ling_contact))
    for index, value in enumerate(p_values):
        #explore the p-values and return the borrowing threshold that yields a positive p-value
        if value < 0.05:
            threshold = index
            break
        if index == 2 and value >= 0.05:
            threshold = index + 1
    print('#')
    return threshold


print('#####Table 5####')
Kessler(Eng,Ita)
Kessler(Eng,Hin)
Kessler(Hin,Ita)
print('    ')

'''
print('#####Table 5bis: not in the paper####')
Kessler(Eng,Tur)
Kessler(Ita,Tur)
Kessler(Hin,Tur)
Kessler(Eng,Mon)
Kessler(Ita,Mon)
Kessler(Hin,Mon)
Kessler(Eng,Man)
Kessler(Ita,Man)
Kessler(Hin,Man)
print(hyper_final(Tur, Eng))
print(hyper_final(Tur, Ita))
print(hyper_final(Tur, Hin))
print(hyper_final(Mon, Eng))
print(hyper_final(Mon, Ita))
print(hyper_final(Mon, Hin))
print(hyper_final(Man, Eng))
print(hyper_final(Man, Ita))
print(hyper_final(Man, Hin))
print(randomize(Tur, Eng))
print(randomize(Tur, Ita))
print(randomize(Tur, Hin))
print(randomize(Mon, Eng))
print(randomize(Mon, Ita))
print(randomize(Mon, Hin))
print(randomize(Man, Eng))
print(randomize(Man, Ita))
print(randomize(Man, Hin))
print('    ')
'''

print('#####Table 6####')
print(hyper_final(Eng, Ita))
print(hyper_final(Eng, Hin))
print(hyper_final(Ita, Hin))
print(randomize(Ita, Eng))
print(randomize(Hin, Eng))
print(randomize(Ita, Hin))
print('    ')


print('#####Table 9####')
Kessler(Tur,Man)
Kessler(Tur,Mon)
Kessler(Man,Mon)
print('    ')

print('#####Table 10- you need to uncomment a line in the function corr() to print the number of correlations####')
print(corr(Eng,Ita))
print(corr(Eng,Hin))
print(corr(Hin,Ita))
print(corr(Tur,Man))
print(corr(Tur,Mon))
print(corr(Man,Mon))
print('    ')

print('#####Table 12####')
print(hyper_final(Tur, Man))
print(hyper_final(Tur, Mon))
print(hyper_final(Man, Mon))
print(randomize(Tur, Man))
print(randomize(Tur, Mon))
print(randomize(Man, Mon))
print('    ')

'''
######This might take some time
print('#####Table 13####')
print('Simulation Turkish, Ringe')
print(Counter([simulation1(Tur, [0, 8, 17]) for num in range(50)]))
print('Simulation Turkish, RSquare')
print(Counter([simulation2(Tur, [0, 8, 17]) for num in range(50)]))
print('Simulation Mongolian, Ringe')
print(Counter([simulation1(Mon, [0, 8, 17]) for num in range(50)]))
print('Simulation Mongolian, RSquare')
print(Counter([simulation2(Mon, [0, 8, 17]) for num in range(50)]))
print('Simulation Manchu, Ringe')
print(Counter([simulation1(Man, [0, 8, 17]) for num in range(50)]))
print('Simulation Mongolian, RSquare')
print(Counter([simulation2(Man, [0, 8, 17]) for num in range(50)]))
print('    ')
'''

