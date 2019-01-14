
def dnaConversion():

  dna = input('Enter the DNA strand you want converted:')
  dna = dna.replace(' ', '').upper()

  rna = []

  for i in range(len(dna)):
    if dna[i] == 'G':
      rna.append('C')
    elif dna[i] == 'C':
      rna.append('G')
    elif dna[i] == 'A':
      rna.append('T')
    elif dna[i] == 'T':
      rna.append('A')

  rnaFinal = ''.join(rna)

  return (rnaFinal)


print(dnaConversion())
