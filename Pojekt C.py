file0 = open("Wynik.txt", "w+")
import operator
text1  = """atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccacaacctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgacca cggaaagatgatcaagagaggatgatttcttggccatatcgcaatgaatacttgtgacttgtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggattacgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttagga tagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaattgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccgattgaagatcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtt tccttaaccctctattttttacggaagaatgatcaagctgctgctcttgatcatcgtttc"""


def frequent_mers(text, k):

    frequent_mer = []
    slownik = {} # slownik z wszystkimi merami i ich liczbą
    for i in range(len(text) - k + 1):
        pattern = text[i:(i+k)]  # wybiera wszystkie mery
        slownik[pattern] = text.count(pattern)  
        # zlicza ilosc dnaego meru w sekwencji. 
        # PatternCount jest mniej wydajne od funkcji .count
    print(slownik)
    MaxCount = max(slownik.items(), key=operator.itemgetter(1))[0]
    # funkcja max znajduje najwieksza wartosc klucza
    for a, b in slownik.items():  # wyszukuje klucz z najwieksza wartoscia
        if MaxCount == b:
            frequent_mer.append(a) # dodaje klucz do listy
    return MaxCount


for k in range(2, 13):
    k1 = frequent_mers(text1, k)
    print(k1)
    file0.writelines("Najczęściej występujący k-mer: \n")
    file0.writelines([str(k1), "\n"])
file0.writelines("""Przy długim k - merze, prawdopodobieństwo położenia
takich sekwencji niedaleko siebie jest bardzo mało prawdopodone w losowo 
wygenerowanym DNA. Przy merze równym lub większym 12 nukleotydów znalezie
-nie powtarzajacego się np 12 - meru, ozacza, że dany framgent DNA może
 pełnić istotną funkcję biologiczną i powinno się go zbadać innymi metodami""")
   
file0.close()
