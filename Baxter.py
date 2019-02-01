#######
#10/01/2018
#######

import random
from collections import Counter

#dictionary mapping phonemes to Baxter and Manaster Ramer's (2000) Dolgopolsky classes
#'8' and '3' mark English dental fricatives


Alpha = {"p":'P', "b":'P', "f": 'P', "v": 'P',
         "m": 'M',
         "n": 'N', "N": 'N',
         "s":'S', "z": 'S',  "S": 'S',  "Z" : 'S',
         "c": 'K', "x": 'K', "k": 'K', "g": 'K', "C": 'K', "j": 'K',
         "t": 'T', "d": 'T', "T": 'T', "8": 'T', "D": 'T',
         "r": 'R', "l" : 'R', "L": 'R',
         "y": 'J',
         "o": 'O', "u": 'W', "3" : 'O', "h": 'O', "G": 'O',  "q": 'O', "a": 'O', "E": 'O', "e": 'O', "i": 'O', "$": 'O', "A": 'O',
         "w": 'W'}


#168-wordlists, first phoneme

#the symbol 'c' in Mongolian is encoding the affricate /ts/.
# 'z' is the alveolar fricative, 'Z' the postalveolar fricative, 'C' the postalveolar sibilant affricate
#vowel distinctions are not crucial for the purposes of the algorithm, therefore some vowel constrasts are missing

Mon = ["bo", "n", "x", "g", "d", "t", "it", "u", "o", "o",
          "x", "Z", "ba", "xn", "Sn", "e", "x", "x", "a", "z",
          "S", "n", "b", "m", "xo", "m", "o", "Z", "u", "n",
          "u", "x", "c", "on", "o", "a", "m", "c", "y", "o",
           "o", "be", "s", "o", "u", "t", "C", "n", "x", "a", #50
           "S", "x", "x", "x", "o", "g", "d", "g", "NA", "x",
           "n", "z", "u", "i", "x", "n", "b", "u", "a", "i",
          "ux", "sd", "m", "b", "u", "a", "nu", "a", "u", "bz",
           "a", "c", "xo", "x", "x", "m", "mu", "s", "n", "a",
           "i", "x", "s", "z", "e", "u", "o", "b", "S", "u", #100
           "u", "a", "t", "tC", "xS", "ub", "o", "t", "x", "NA",
           "nt", "x", "u", "x", "x", "n", "s", "o", "u", "b",
           "g", "n", "dt", "d", "C", "e", "t", "u", "m", "ot",
          "s", "c", "m", "u", "g", "u", "S", "z", "u", "u",
           "n", "S", "c", "x", "S", "o", "Z", "bd", "x", "d", #150
           "S", "x", "s", "m", "y", "bx", "S", "d", "x", "m",
           "g", "n", "x", "z", "o", "b", "z", "n"]

Man = ["g", "e", "j", "i", "d", "s", "a", "g", "ol", "jf",
          "u", "a", "f", "i", "n", "NA", "n", "j", "e", "n",
          "Cg", "i", "C", "m", "ub", "m", "bw", "t", "u", "a",
          "fd", "n", "i", "on", "f", "s", "y", "s", "g", "t",
          "u", "u", "u", "f", "f", "u", "S", "y", "o", "a", #50
         "w", "i", "x", "b", "t", "g", "a", "NA", "d", "m",
          "f", "n", "o", "j", "s", "C", "jf", "fe", "e", "i",
           "s", "d", "s", "g", "w", "go", "a", "b", "b", "a",
           "at", "t", "f", "d", "t", "w", "f", "e", "d", "y",
           "j", "d", "t", "i", "f", "t", "b", "j", "x", "m", #100
           "o", "m", "t", "a", "m", "x", "u", "t", "xs", "u",
          "e", "d", "e", "g", "ad", "S", "b", "u", "m", "a",
           "b", "ot", "mn", "NA", "w", "y", "n", "t", "t", "a",
            "e", "n", "j", "NA", "t", "f", "d", "j", "a", "f",
           "n", "s", "NA", "s", "d", "i", "a", "bx", "S", "j",  #150
          "i", "f", "s", "e", "n", "nl", "s", "m", "d", "m",
            "b", "u", "o", "t", "x", "i", "x", "g"]

Tur =  ["NA", "b", "i", "u", "d", "b", "b", "u", "g", "k",
           "a", "k", "k", "d", "i", "e", "k", "C", "NA", "b",
           "k", "ki", "b", "y", "k", "a", "o", "y", "NA", "y",
           "k", "k", "C", "o", "i", "d", "e", "k", "k", "y",
          "y", "b", "k", "t", "sk", "b", "k", "g", "b", "a", #50
            "d", "d", "t", "a", "d", "e", "k", "k", "b", "b",
            "as", "y", "i", "y", "i", "t", "k", "u", "s", "g",
           "g", "d", "b", "NA", "k", "k", "u", "y", "o", "s",
           "a", "v", "k", "y", "b", "NA", "k", "y", "u", "y",
           "g", "y", "o", "d", "d", "d", "v", "t", "e", "o", #50
           "y", "s", "C", "i", "a", "b", "d", "s", "s", "s",
          "o", "y", "a", "d", "S", "NA", "a", "y", "s", "y",
            "i", "g", "d", "t", "t", "k", "t", "b", "s", "g",
            "y", "k", "b", "d", "NA", "k", "y", "y", "d", "k",
            "y", "s", "ab", "sk", "g", "g", "y", "s", "s", "d", #150
           "y", "e", "i", "k", "C", "k", "d", "y", "NA", "NA",
            "d", "i", "k", "d", "y", "s", "s", "a"]

Eng = ["$", "w", "t", "8", "f", "f", "b", "l", "w", "8", "h",
          "s", "S", "n", "8", "m", "NA", "C", "NA", "f", "b",
          "d", "l", "s", "w", "t", "NA", "NA", "s", "l", "r",
          "b", "NA", "g",  "r", "s", "m", "b", "b", "f", "e",
         "h", "t", "f", "h", "h", "i", "a", "n", "m", "t", #50
          "t", "f", "f", "n", "h", "w", "b", "g", "n", "b",
          "h", "d", "i", "b", "s", "NA", "b", "b", "l", "s",
          "h", "n", "8", "s", "f", "s", "l", "d", "f", "h",
          "h", "k", "s", "s", "s", "d", "s", "f", "w", "k",
           "l", "s", "s", "t", "f", "g", "h", "s", "r", "w", #100
          "w", "p", "p", "8", "t", "s", "NA", "s", "s", "p",
          "f", "f", "f", "s", "s", "m", "s", "w",  "r", "r",
          "NA", "s", "s", "s", "s", "$", "k", "f", "s", "w",
          "s", "a", "s", "f", "A", "b", "r", "NA", "r", "g",
           "y", "w", "b", "n", "d", "y", "w", "k", "f", "n", #150
          "o", "g", "b", "r", "d", "s", "NA", "S", "d", "s",
           "w", "d", "k", "n", "r", "l", "n"]

Ita = ["a", "u", "d", "t", "k", "C", "g", "l", "l", "s",
          "p", "p", "k", "s", "s", "w", "p", "b", "a", "p",
          "C", "k", "p", "s", "v",  "a", "f", "f", "s", "f",
         "r", "k", "f", "e", "k", "p", "k", "s", "o", "g",
          "w", "k", "k", "p", "k", "t", "o", "o", "n", "b", #50
          "d", "l", "u", "p", "j", "m", "a", "p", "i", "k",
          "s", "k",  "b", "m", "m", "s", "v", "s", "r", "r",
          "v", "s", "s", "p", "a", "t", "d", "v", "m",  "k",
         "k", "k", "t", "f", "p", "g", "s", "n", "v", "k",
          "v", "j", "s", "s", "j", "k", "d", "t", "s", "s", #100
          "l", "a", "t", "s", "l", "l", "k", "k", "d", "k",
          "j", "g", "f", "j", "g", "s", "l", "s", "a", "p",
          "f", "l", "m", "s", "p", "s", "t", "n", "n", "C",
          "v", "n", "g", "f", "f", "C", "b", "s", "m", "r",
           "v", "j", "b", "n", "n", "j", "a", "k", "f", "p", #150
          "n", "v", "b", "k", "m", "s", "d", "r",  "a", "s",
         "l", "b", "as", "k", "v", "d", "s", "n"]

#the distinction between aspirated/non aspirated coronal is ignored, since it does not matter for Dolgopolski classes
Hin = ["d", "e", "d", "t", "C", "p", "b", "l", "C", "g",
          "b", "C", "NA", "NA", "p", "NA", "NA", "b", "NA", "m",
           "C", "k", "j", "s", "k", "p", "j", "p", "b", "p",
           "j", "C", "p", "g", "r", "t", "m", "NA", "h", "C",
          "a", "s", "p", "p",  "b", "s", "k", "a", "n", "m", #50
          "d", "j", "n", "p", "g", "h", "p", "p", "a", "NA",
           "p", "h", "p", "k", "k", "t", "u", "p", "s", "h",
          "d", "s", "j", "s", "s", "D", "s", "j", "NA", "l",
           "s", "m", "k", "b", "b", "k", "k", "t", "u",  "C",
         "a", "l", "b", "k", "m", "g", "d", "p", "g",  "m", #50
          "d", "p", "k", "d", "p", "b", "s", "g", "k", "g",
          "k", "t", "b", "j", "s", "s", "C", "t", "p", "v",
          "n", "j", "s", "NA", "p", "r", "d", "b", "d", "NA",
           "NA", "NA", "NA", "d", "a", "r", "j", "s", "p", "l",
          "h", "p", "NA", "k", "r", "d", "NA", "NA",  "t", "p", #150
         "n", "p", "a", "b", "s", "g", "s", "g", "t", "k",
           "C", "g", "s", "NA", "n", "d", "b","n"]




#take two words, return a distance according to Baxter and Manaster Ramer (2000)
def distance_pair(x, y):
    dist = []
    for symbol1 in x:
        for symbol2 in y:
            #add 1 if the two symbols do not match, otherwise 0
            if set(Alpha[symbol1]) & set(Alpha[symbol2]) == set():
                dist.append(1)
            else:
                dist.append(0)
    return sum(dist)/len(dist)

#calculate distance between two wordlists
def distance(lang1, lang2):
    dist = []
    for word1, word2 in zip(lang1, lang2):
        #skip in case of missing values
        if word1 != 'NA' and word2 != 'NA':
            dist.append(distance_pair(word1, word2))
    return sum(dist)/len(dist)

#given a distance value and a list of distances, calculate p-value
def pvalue(dist_value, dlist):
    for index, d in enumerate(dlist):
        if dist_value < d:
            return index/10000
    return 1.0

#run the Monte Carlo test
def Osw(Ling1,Ling2):
    dist_all=[]
    d = distance(Ling1,Ling2)
    for i in range(10000):
        #create a shuffled list
        Ling2_rand= Ling2[:]
        random.shuffle(Ling2_rand)
        dist_all.append(distance(Ling1,Ling2_rand))
    dist_all = sorted(dist_all)
    #optional print: the average of the randomized distances
    #print(sum(dist_all)/len(dist_all))
    #print the global distance of the two wordlists and its p-value after the Monte Carlo test
    print(round(d, 3), "p =", pvalue(d, dist_all))
    return pvalue(d,dist_all)

#experiment on loanwords, Section 8
def simulation(Ling, borrowings):
    #create two randomized list starting for the input list
    Ling_rand = Ling[:]
    random.shuffle(Ling_rand)
    Ling_rand2 = Ling[:]
    random.shuffle(Ling_rand2)
    p_values = []
    #integer variable needed to determine the saturation threshold. Initialize with any n > len(borrowings)
    threshold = 10
    #perform borrowing experiment by forcing different rates of lexical borrowing, as contained in the list 'borrowings'
    for value in borrowings:
        #create a new language, which is basically Ling_rand2 with some borrowing from Ling_rand
        Ling_contact = Ling_rand[:value] + Ling_rand2[value:]
        #run the Monte Carlo test between the new list and Ling_rand
        p_values.append(Osw(Ling_rand, Ling_contact))
    for index, value in enumerate(p_values):
        #explore the p-values and return the borrowing threshold that yields a positive p-value
        if value < 0.05:
            threshold = index
            break
        if index == 2 and value >= 0.05:
            threshold = 'none'
    print('#')
    return threshold


print('#####Table 3####')
Osw(Eng, Ita)
Osw(Eng, Hin)
Osw(Hin, Ita)
print('    ')

print('#####Table 4####')
Osw(Tur, Eng)
Osw(Tur, Ita)
Osw(Tur, Hin)
Osw(Mon, Eng)
Osw(Mon, Ita)
Osw(Mon, Hin)
Osw(Man, Eng)
Osw(Man, Ita)
Osw(Man, Hin)
print('    ')

print('#####Table 8####')
Osw(Tur,Man)
Osw(Tur,Mon)
Osw(Mon,Man)
print('    ')

'''
######This might take some time
print('#####Table 13####')
print('Simulation Turkish')
print(Counter([simulation(Tur, [0, 8, 17]) for num in range(50)]))
print('Simulation Mongolian')
print(Counter([simulation(Mon, [0, 8, 17]) for num in range(50)]))
print('Simulation Manchu')
print(Counter([simulation(Man, [0, 8, 17]) for num in range(50)]))
print('    ')
'''