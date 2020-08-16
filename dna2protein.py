#This code was part of my assignment in BIF510 Programming Fundamentals, Bioinformatics and Systems Biology Program, KMUTT, Thailand.
#Thanks to Hong Qin, because his video on Youtube I can fulfill my assignment :) However, I add some modifications here.
#This script only read the first start DNA codon (ATG) until the first stop codon (TGA, TAA, and TAG, that symbolized with *)
#Please use this script wisely.
#Enjoy!
	
protdict ={
    'TTT':' Phe','TTC':' Phe','TTA':' Leu','TTG':' Leu','CTT':' Leu','CTC':' Leu','CTG':' Leu','CTA':' Leu','ATT':' Ile',
    'ATC':' Ile','ATA':' Ile','ATG':' Met','GTT':' Val','GTC':' Val','GTA':' Val','GTG':' Val','TCT':' Ser','TCC':' Ser',
    'TCA':' Ser','TCG':' Ser','CCT':' Pro','CCC':' Pro','CCA':' Pro','CCG':' Pro','ACT':' Thr','ACC':' Thr','ACA':' Thr',
    'ACG':' Thr','GCT':' Ala','GCC':' Ala','GCA':' Ala','GCG':' Ala','TAT':' Tyr','TAC':' Tyr','TAA':' *','TAG':' *',
    'CAT':' His','CAC':' His','CAA':' Gln','CAG':' Gln','AAT':' Asn','AAC':' Asn','AAA':' Lys','AAG':' Lys','GAT':' Asp',
    'GAC':' Asp','GAA':' Glu','GAG':' Glu','TGT':' Cys','TGC':' Cys','TGA':' *','TGG':' Trp','CGT':' Arg','CGC':' Arg',
    'CGA':' Arg','CGG':' Arg','AGT':' Ser','AGC':' Ser','AGA':' Arg','AGG':' Arg','GGT':' Gly','GGC':' Gly','GGA':' Gly',
    'GGG':' Gly'
    } #First, make the dictionary as a container for all the possible codons

def dna2prot(ORF,protdict):                     #Making functions to read DNA sequence
    protein = ""                                #Container for translated sequence
    start = ORF.find("ATG")                     #Command to find start codon (ATG). If you wish, you can change it in RNA form. Dont forget to change the dictionary too.
    seqstart = ORF[start:]                      #Amino acid translation starts from here, when the first ATG is found                      
    if len(seqstart)%3 == 1:                    #All conditional commands are used to ensure the DNA sequence can be divided by 3. If there is modulus, then the one or two last character from sequence are not translated. 
        seqstart1 = seqstart[:-1]
        for d in range (0,len(seqstart1),3):    #Looping command to read the sequence from ATG until first stop codon, based on 3 character that will be translated to one amino acid
            codon = seqstart1[d:d + 3]          #Codon is equal to 3 character of DNA base
            protein += protdict[codon]          #Amino acid will be added as sequence can be translated except for stop codon
            if protdict[codon] == ' *':         #If stop codon is met, then the result will be directly printed and looping command stops
                break
            pass
    elif len(seqstart)%3 == 2:
        seqstart2 = seqstart[:-2]
        for e in range (0,len(seqstart2),3):
            codon = seqstart2[e:e + 3]
            protein += protdict[codon]
            if protdict[codon] == ' *':
                break
            pass
    if len(seqstart)%3 == 0:
        for c in range (0,len(seqstart),3):
            codon = seqstart[c:c + 3]
            protein += protdict[codon]
            if protdict[codon] == ' *':
                break
    return protein