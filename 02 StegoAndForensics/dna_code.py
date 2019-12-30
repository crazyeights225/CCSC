#crazyeights225
#CONVERT DNA TRIPLES TO ENGLISH
#Input: DNA triples without spaces
dnac={'AAA': 'a',
      'AAC': 'b', 
      'AAG': 'c',
      'AAT': 'd',
      'ACA': 'e',
      'ACC': 'f',
      'ACG': 'g',
      'ACT': 'h',
      'AGA': 'i',
      'AGC': 'j',
      'AGG': 'k',
      'AGT': 'l',
      'ATA': 'm',
      'ATC': 'n',
      'ATG': 'o',
      'ATT': 'p',
      'CAA': 'q',
      'CAC': 'r',
      'CAG': 's',
      'CAT': 't',
      'CCA': 'u',
      'CGC': 'v',
      'CCG': 'w',
      'CCT': 'x',
      'CGA': 'y',
      'CGC': 'z',
      'CGG': 'A',
      'CGT': 'B',
      'CTA': 'C',
      'CTC': 'D',
      'CTG': 'E',
      'CTT': 'F',
      'GAA': 'G',
      'GAC': 'H',
      'GAG': 'I',
      'GAT': 'J',
      'GCA': 'K',
      'GCC': 'L',
      'GCG': 'M',
      'GCT': 'N',
      'GGA': 'O',
      'GGC': 'P',
      'GGG': 'Q',
      'GGT': 'R',
      'GTA': 'S',
      'GTC': 'T',
      'GTG': 'U',
      'GTT': 'V',
      'TAA': 'W',
      'TAC': 'X',
      'TAG': 'Y',
      'TAT': 'Z',
      'TCA': '1',
      'TCC': '2',
      'TCG': '3',
      'TCT': '4',
      'TGA': '5',
      'TGC': '6',
      'TGG': '7',
      'TGT': '8',
      'TTA': '9',
      'TTC': '0',
      'TTG': ' ',
      'TTT': '.'};

def get_input():
	code=raw_input("Enter dna triples:")
        return code


def dna_code_to_english(code):
	plain=''
	for i in range(0, len(code), 3):
		plain+=dnac[code[i:i+3]]
	return plain

code=get_input()
plain=dna_code_to_english(code)
print("Output:")
print(plain)


