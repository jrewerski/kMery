from operator import itemgetter

file0 = open("Wynik.txt", "w+")

text1='''atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccacaacctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgaccacggaaagatgatcaagagaggatgatttcttggccatatcgcaatgaatacttgtgacttgtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggattacgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttaggatagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaattgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccgattgaagatcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtttccttaaccctctattttttacggaagaatgatcaagctgctgctcttgatcatcgtttc'''

def PATTERNCOUNT(Text, Pattern):
    assert Text != ""
    assert Pattern != ""
    count = 0
    for i in range(len(Text) - len(Pattern)+1):
        if Text[i:i + len(Pattern)] == Pattern:
            count = count + 1
    #wyszukuje ilosc meru w danej sekwencji DNA
    assert count > 0
    assert count < len(Text)
    return count

def frequent_mers(text, k):
    assert text != ""
    assert k > 1
    assert k < len(text)
    frequent_mer = []
    slownik = {} 
    # slownik bedzie zawieral wszystkie mery i ich liczbe w sekwencji 
    for i in range(len(text) - k + 1):
        pattern = text[i:(i+k)]  # wybiera wszystkie mery
        slownik[pattern] = PATTERNCOUNT(text, pattern)
        # zlicza ilosc dnaego meru w sekwencji i podstawia pod klucz
        # ktory jest tym merem 
        assert slownik != ""
    print(slownik)
    MaxCount = max(slownik.items(), key=itemgetter(1))[1]  
    assert MaxCount > 0
    
    # Pobranie najwiekszej wartosci z slownika dzieje sie po wartosciach kluczy
    for a, b in slownik.items():  # wyszukuje klucz z najwieksza wartoscia
        if MaxCount == b:
            frequent_mer.append(a) # dodaje klucz do listy
            assert frequent_mer != "", "Blad, ktorys k mer musi sie pojawic jak najczestszy"
    return frequent_mer


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

assert frequent_mers(text1, 2) == ['tt'], "blad napisania fukcji"
