#######
#10/01/2018
#######



import random
from collections import Counter

#dictionary mapping phonemes to Kessler and Lehtonen's (2006) scores.
#the symbol '*' is encoded to mark double articulation as opposed to polymorphism
#'w' is split into two symbols, 'w' and 'W', as to account for the double articulation of /w/
#'8' and '3' mark English dental fricatives

Alpha = {"p":0.0, "b":0.0, "m": 0.0, "f": 0.0, "v": 0.0,
         "s":4.0, "t": 4.0, "T": 4.0, "d": 4.0, "D": 4.0, "n": 4.0, "z": 4.0, "Z": 4.0, "l" : 4.0, "S": 4.0, "i": 4.0, "c": 4.0, "E": 4.0, "e": 4.0, "r": 4.0, "R": 4.0, "3": 4.0, "8": 4.0,
         "y": 6.0,
         "x": 9.0, "k": 9.0, "g": 9.0, "a": 9.0, "N": 9.0,
         "h": 10.0, "G": 10.0, "q": 10.0,
          "o": 9.0, "u": 9.0,
         "C": 4.0, "j": 4.0,
         "w": 0.0,
         "W": 9.0,
         "*": 1000.0}



#168-wordlists, first consonant

#the symbol 'c' in Mongolian is encoding the affricate /ts/.
# 'z' is the alveolar fricative, 'Z' the postalveolar fricative, 'C' the postalveolar sibilant affricate

Mon = ["br", "n", "x", "g", "d", "t", "xt", "r", "r", "t",
          "x", "Z", "bx", "xn", "Sn", "r", "x", "x", "m", "z",
           "S", "n", "b", "m", "xt", "m", "y", "Z", "r", "n",
           "gn", "x", "c", "vn", "l", "r", "m", "c", "y", "x",
            "n", "bv", "s", "d", "s", "t", "C", "n", "x", "m",  #50
           "S", "x", "x", "x", "v", "g", "d", "g", "NA", "x",
           "n", "z", "x", "d", "x", "n", "b", "l", "m", "n",
           "zx", "sd", "m", "b", "n", "y", "n", "m", "x", "bz",
          "v", "c", "gx", "x", "x", "m", "mx", "s", "n", "l",
          "r", "x", "s", "z", "r", "n", "g", "b", "S", "r",   #100
          "g", "r", "t", "tC", "xS", "yb", "y", "t", "x", "NA",
           "nt", "x", "r", "x", "x", "n", "s", "d", "s", "b",
          "g", "n", "dt", "d", "C", "l", "t", "l", "m", "gt",
           "s", "c", "m", "t", "g", "n", "S", "z", "l", "l",
          "n", "S", "c", "x", "S", "d", "Z", "bd", "x",  "d", #150
           "S", "x", "s", "m", "y", "bx", "S", "d", "x", "m",
           "g", "n", "x", "z", "y", "b", "z", "n"]

Man = ["g", "m", "j", "l", "d", "s", "m", "g", "nl", "jf",
          "j", "j", "f", "s", "n", "NA", "n", "j", "r", "n",
         "Cg", "n", "C", "m", "bm", "m", "bWw", "t", "s", "b",
          "fd", "n", "l", "rn", "f", "s", "y", "s", "g", "t",
          "m", "x", "n", "f", "f", "j", "S", "y", "f", "N",  #50
          "*Ww", "l", "x", "b", "t", "g", "s", "NA", "d", "m",
          "f", "n", "m", "j", "s", "C", "jf", "fd", "r", "n",
          "s", "d", "s", "g", "*Ww", "gl", "m", "b", "b", "f",
           "bt", "t", "f", "d", "t", "*Ww", "f", "b", "d", "y",
          "j", "d", "t", "l", "f", "t", "b", "j", "x", "m", #100
          "b", "m", "t", "n", "m", "x", "f", "t", "xs", "C",
          "f", "d", "y", "g", "bd", "S", "b", "s", "m", "g",
          "b", "mt", "mn", "NA", "*Ww", "y", "n", "t", "t", "b",
          "d", "n", "j", "NA", "t", "f", "d", "j", "l", "f",
          "n", "s", "NA", "s", "d", "n", "n", "bx", "S", "j", #150
          "C", "f", "s", "x", "n", "nl", "s", "m", "d", "m",
          "b", "s", "l", "t", "x", "C", "x", "g"]

Tur =  ["NA", "b", "k", "C", "d", "b", "b", "z", "g", "k",
           "*Ww", "k", "k", "d", "n", "r", "k", "C", "NA", "b",
           "k", "tk", "b", "y", "k", "*Ww", "r", "y", "NA", "y",
            "k", "k", "C", "t", "p", "d", "t", "k", "k", "y",
           "y", "b", "k", "t" "sk", "b", "k", "g", "b", "*Ww", #50
           "d", "d", "t", "y", "d", "l", "k", "k", "b", "b",
           "rs", "y", "C", "y", "s", "t", "k", "f", "s", "g",
           "g", "d", "b", "NA", "k", "k", "y", "y", "l", "s",
           "v", "v", "k", "y", "b", "NA", "k", "y", "C", "y",
           "g", "y", "t", "d", "d", "d", "v", "t", "z",  "v", #100
          "y", "s", "C", "t", "t", "b", "d", "s", "s", "s",
            "y", "y", "k", "d", "S", "NA", "y", "y", "s", "y",
           "r", "g", "d", "t", "t", "k", "t", "b", "s", "g",
           "y", "k", "b", "d", "NA", "k", "y", "y", "d", "k",
           "y", "s", "kb", "sk", "g", "g", "y", "s", "s", "d",#150
           "y", "s", "y", "k", "C", "k", "d", "y", "NA", "NA",
           "d", "s", "k", "d", "y", "s", "s", "d"]

Eng = ["8", "*Ww", "t", "3", "f", "f", "b", "l", "*Ww", "3",
          "h", "s", "S", "n", "3", "m", "NA", "C", "NA", "f",
          "b", "d", "l", "s", "*Ww", "t", "NA", "NA", "s", "l",
          "r", "b", "NA", "g", "r", "s", "m", "b", "b", "f",
          "g", "h", "t", "f", "h", "h", "r", "a", "n", "m", #50
          "t", "t", "f", "f", "n", "h", "*Ww", "b", "g", "n",
          "b", "h", "d", "t", "b", "s", "NA", "b", "b", "l",
          "s", "h", "n", "3", "s", "f", "s", "l", "d",  "f",
          "h", "h", "k", "s", "s", "s", "d", "s", "f", "*Ww",
          "k", "l", "s", "s", "t", "f", "g", "h", "s", "r", #100
          "*Ww", "*Ww", "p", "p", "3", "t", "s", "NA", "s",  "s",
          "p", "f", "f", "f", "s", "s", "m", "s", "*Ww", "r",
          "r", "NA", "s", "s", "s", "s", "r", "k", "f", "s",
          "*Ww", "s", "s", "s", "f", "S", "b", "r", "NA", "r",
          "g", "y", "*Ww", "b", "n", "d", "y", "*Ww", "k", "f", #150
          "n", "l", "g", "b", "r", "d", "s", "NA", "S", "d",
          "s", "*Ww", "d", "k", "n", "r", "l", "n"]

#the symbol 'j' in Italian is encoding the postalveolar affricate
Ita = ["l", "n", "d", "t", "k", "C", "g", "l", "l", "s",
          "p", "p", "k", "s", "s", "*Ww", "p", "b", "n", "p",
          "C", "k", "p", "s", "v", "l", "f", "f", "s", "f",
          "r", "k", "f", "r", "k", "p", "k", "s", "s", "g",
           "*Ww", "k", "k", "p",  "k", "t", "r", "k", "n", "b", #50
         "d", "l", "n", "p", "j", "m", "l", "p", "n", "k",
          "s", "k", "b", "m", "m", "s", "v", "s", "r", "r",
          "v", "s", "s", "p", "n", "t", "d", "v", "m",  "k",
         "k", "k", "t", "f", "p", "g", "s", "n", "v",  "k",
         "v", "j", "s", "s", "j", "k", "d", "t", "s", "s", #100
          "l", "S", "t", "s", "l", "l", "k", "k", "d", "k",
          "j", "g", "f", "j", "g", "s", "l", "s", "k",  "p",
         "f", "l", "m", "s", "p", "s", "t", "n", "n", "C",
           "v", "n", "g", "f", "f", "C", "b", "s", "m", "r",
          "v", "j", "b", "n", "n", "j", "n", "k", "f", "p", #150
          "n", "v", "b", "k", "m", "s", "d", "r", "gf", "s",
           "l", "b", "Ss", "k", "v", "d", "s", "n"]
          
Hin = ["d", "k", "d", "t", "C", "p", "b", "l", "C", "g",
          "*bh", "*Ch", "NA", "NA", "p", "NA", "NA", "b", "NA", "m",
          "C", "k", "j", "s", "k", "p", "j", "*ph", "b", "p",
          "j", "*Ch", "*ph", "*gh",  "r", "t", "m", "NA", "h", "C",
         "n", "s", "p", "p", "b", "s", "k", "k", "n", "m", #50
          "d", "j", "n", "p", "*gh", "h", "p", "p", "n", "NA",
          "p", "h", "p", "*kh", "k", "*th", "l", "*ph", "s", "h",
          "d", "s", "j", "s", "s", "D", "s", "j", "NA", "l",
          "S", "m", "k", "b", "*bh", "*kh", "*kh", "t", "R", "C",
         "n", "l", "b", "*kh", "m", "g", "d", "p", "*gh",  "m", #100
         "*dh", "p", "*kh", "*dh", "*ph", "b", "s", "g", "k", "g",
        "*kh", "t", "b", "j", "s", "s", "C", "t", "p",  "v",
         "n", "*jh", "s", "NA", "p", "r", "dh", "b", "*dh", "NA",
          "NA", "NA", "NA", "*dh", "g", "r", "j", "s", "p", "l",
          "h", "p", "NA", "k", "r", "d", "NA", "NA", "*Th", "p", #150
          "n", "p", "*Ch", "b", "s", "g", "s", "g",  "t", "k",
         "C", "g", "s", "NA", "n", "d", "b", "n"]


          
#take two words, return a distance according to Kessler and Lehtonen (2006)
def distance_pair(word1, word2):
    dist = []
    for symbol1 in word1:
        for symbol2 in word2:
            if symbol1 != symbol2:
                #distance + 0.5 if the symbols are different
                dist.append(abs(Alpha[symbol1] - Alpha[symbol2]) + 0.5)
            else:
                dist.append(0)
    #if there is co-articulation, pick the lowest distance
    if '*' in word1 or '*' in word2:
        return min(dist)
    #if there is no coarticulation, pick the average distance of the letters
    else:
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
    Ling_rand2 = Ling[:]
    random.shuffle(Ling_rand)
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




print('#####Table 1####')
Osw(Eng, Ita)
Osw(Eng, Hin)
Osw(Hin, Ita)
print('    ')

print('#####Table 2####')
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


print('#####Table 7####')
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