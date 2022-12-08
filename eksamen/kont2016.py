# Oppgave 2a
def load_bin(filename):
  binstring = ""
  try:
    with open(filename,'r') as f:
      for line in f:
        binstring+=line.strip()
  except:
    print("Error: Could not open file",filename)
  return binstring


# Oppgave 2b
def bin_to_dec(binary):
  decimal = 0
  bin_number = 1
  for i in range(len(binary)-1,-1,-1):
    if binary[i]=="1":
      decimal+= bin_number
    bin_number+=bin_number
  return decimal


# Oppgave 2c
def dec_to_char(dec):
  alfabet=" ,.ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"
  if (dec<len(alfabet) and dec>=0):
    return alfabet[dec]
  else:
    return""


# Oppgave 2d
def bin_to_txt(binstring):
  txt=""
  for i in range(0,len(binstring),5):
    dec = bin_to_dec(binstring[i:i+5])
    txt += dec_to_char(dec)
  return txt


# Oppgave 2e
def main():
  print("Binary-to-text converter")
  print("========================")
  b_file = input("Name of binaryfile to load from: ")
  b_string = load_bin(b_file)
  txt = bin_to_txt(b_string)
  t_file = input("Name of textfile to save to: ")
  try:
    with open(t_file,"w") as f:
      f.write(txt)
    print(b_file,"has been converted and saved to",t_file)
  except:
    print("Error: Could to write to file",t_file)


# Oppgave 3a
def sek_paa_benken(ant_paa_laget,ant_paa_banen,kamptid):
  ant_reserver=ant_paa_laget-ant_paa_banen
  kamptid_sek=kamptid*60
  sek_benken=(kamptid_sek/ant_paa_laget)*ant_reserver
  return round(sek_benken)

# Oppgave 3b
def minutt_sekund(sekunder):
  minutter=sekunder//60
  sekunder=sekunder%60
  m=str(minutter)
  if sekunder<10:
    s='0'+str(sekunder)
  else:
    s=str(sekunder)
  return m+':'+s

# Oppgave 3c
def les_inn_forfall():
  print('Skrivnavn,ellerkunENTER(tomtekst)foråavslutte.')
  navn=input('Spillersomharmeldtforfall:')
  forfall=[]
  while navn!='':
    forfall.append(navn)
    navn=input('Spillersomharmeldtforfall:')
  return forfall


# Oppgave 3d
def finn_tilgjengelige(alle,forfall):
  tilgj=[]+alle
  for navn in forfall:
    tilgj.remove(navn)
  return tilgj


# Oppgave 3e
import random 
def laginndeling(spillere,sp_per_lag):
  ant_lag=len(spillere)//sp_per_lag
  kopi=[]+spillere
  lagoppsett=[[]for l in range(ant_lag)]
  lag=0 
  while kopi!=[]:
    navn=random.choice(kopi)
    kopi.remove(navn)
    lagoppsett[lag].append(navn)
    lag=(lag+1)%ant_lag
  return lagoppsett


# Oppgave 3f
BARN=['Ada','Bo','Cindy','EmmaA.','EmmaB.','Henrik',
      'Ine','Jo','Kim','Lucas','My','Noor','Ola','Pia',
      'Quentin','Rashad','Sara','Tuva','Yngve']

def main():
  forfall=les_inn_forfall()
  spillere=finn_tilgjengelige(BARN,forfall)
  sp_per_lag=int(input('Spillereperlag:'))
  kamptid=int(input('Kamptid(minutter):'))
  lag=laginndeling(spillere,sp_per_lag)
  for i in range(len(lag)):
    print('Lag',i+1,':')
    print(lag[i])
    benk_tid=sek_paa_benken(len(lag[i]),sp_per_lag,kamptid)
    print('Tidpåbenkenperspiller:',minutt_sekund(benk_tid))
    print()
main()


# Oppgave 3g
def ny_fil(tekst='Pythonmyra',inn='kampoppsett.txt',ut='kampplan.txt'):
  innfil=open(inn)
  utfil=open(ut,'w')
  for linje in innfil:
    if tekst in linje:
      utfil.write(linje)
  utfil.close()
  innfil.close()
  return utfil