C0 = "0C"
Cf0 = "0D"
D0 = "0E"
Df0 = "0F"
E0 = "10"
F0 = "11"
Ff0 = "12"
G0 = "13"
Gf0 = "14"
A0 = "15"
Af0 = "16"
B0 = "17"
C1 = "18"
Cf1 = "19"
D1 = "1A"
Df1 = "1B"
E1 = "1C"
F1 = "1D"
Ff1 = "1E"
G1 = "1F"
Gf1 = "20"
A1 = "21"
Af1 = "22"
B1 = "23"
C2 = "24"
Cf2 = "25"
D2 = "26"
Df2 = "27"
E2 = "28"
F2 = "29"
Ff2 = "2A"
G2 = "2B"
Gf2 = "2C"
A2 = "2D"
Af2 = "2E"
B2 = "2F"
C3 = "30"
Cf3 = "31"
D3 = "32"
Df3 = "33"
E3 = "34"
F3 = "35"
Ff3 = "36"
G3 = "37"
Gf3 = "38"
A3 = "39"
Af3 = "3A"
B3 = "3B"
C4 = "3C"
Cf4 = "3D"
D4 = "3E"
Df4 = "3F"
E4 = "40"
F4 = "41"
Ff4 = "42"
G4 = "43"
Gf4 = "44"
A4 = "45"
Af4 = "46"
B4 = "47"
C5 = "48"
Cf5 = "49"
D5 = "4A"
Df5 = "4B"
E5 = "4C"
F5 = "4D"
Ff5 = "4E"
G5 = "4F"
Gf5 = "50"
A5 = "51"
Af5 = "52"
B5 = "53"
C6 = "54"
Cf6 = "55"
D6 = "56"
Df6 = "57"
E6 = "58"
F6 = "59"
Ff6 = "5A"
G6 = "5B"
Gf6 = "5C"
A6 = "5D"
Af6 = "5E"


class scale:
    def __init__(self, name, notes, octave):
        self.name = name
        self.notes = notes
        self.octave = octave


def majorise(root):

    Tnotes = []
    
    first = int(root, 16)  # Convert hexadecimal string to integer
    Tnotes.append(root) #adds the first note to the array
    latest = first #adds this to the 'latest added' variable
    
    
    for i in range(5):              # counts through 5 octaves
        for n in range(1, 8):       # counts through each note interval
            if n == 3 or n == 7:    # adds half-tone intervals
                Tnotes.append(hex(latest + 1)[2:].upper())
                latest = latest + 1
            else:                   # adds whole tone intervals
                Tnotes.append(hex(latest + 2)[2:].upper())
                latest = latest + 2

    return Tnotes

wholeOct = 7

majors = []

majors.append(scale("Cmaj", majorise(C0), wholeOct))
majors.append(scale("C#maj", majorise(Cf0), wholeOct))
majors.append(scale("Dmaj", majorise(D0), wholeOct))
majors.append(scale("D#maj", majorise(Df0), wholeOct))
majors.append(scale("Emaj", majorise(E0), wholeOct))
majors.append(scale("Fmaj", majorise(F0), wholeOct))
majors.append(scale("F#maj", majorise(Ff0), wholeOct))
majors.append(scale("Gmaj", majorise(G0), wholeOct))
majors.append(scale("G#maj", majorise(Gf0), wholeOct))
majors.append(scale("Amaj", majorise(A0), wholeOct))
majors.append(scale("A#maj", majorise(Af0), wholeOct))
majors.append(scale("Bmaj", majorise(B0), wholeOct))


def minorise(root):

    Tnotes = []
    
    first = int(root, 16)  # Convert hexadecimal string to integer
    Tnotes.append(root)
    latest = first
    
    
    for i in range(5):
        for n in range(1, 8):
            if n == 2 or n == 5:
                Tnotes.append(hex(latest + 1)[2:].upper())
                latest = latest + 1
            else:
                Tnotes.append(hex(latest + 2)[2:].upper())
                latest = latest + 2

    return Tnotes
    

minors = []

minors.append(scale("Cmin", minorise(C0), wholeOct))
minors.append(scale("C#min", minorise(Cf0), wholeOct))
minors.append(scale("Dmin", minorise(D0), wholeOct))
minors.append(scale("D#min", minorise(Df0), wholeOct))
minors.append(scale("Emin", minorise(E0), wholeOct))
minors.append(scale("Fmin", minorise(F0), wholeOct))
minors.append(scale("F#min", minorise(Ff0), wholeOct))
minors.append(scale("Gmin", minorise(G0), wholeOct))
minors.append(scale("G#min", minorise(Gf0), wholeOct))
minors.append(scale("Amin", minorise(A0), wholeOct))
minors.append(scale("A#min", minorise(Af0), wholeOct))
minors.append(scale("Bmin", minorise(B0), wholeOct))

#print(majors[0].name, majors[0].notes)
#print(minors[9].name, minors[9].notes)



def majblues(root):

    Tnotes = []
    
    first = int(root, 16)  # Convert hexadecimal string to integer
    Tnotes.append(root)
    latest = first
    
    
    for i in range(5):
        for n in range(1, 6):
            if n == 2 or n == 3:
                Tnotes.append(hex(latest + 1)[2:].upper())
                latest = latest + 1
            elif n == 4:
                Tnotes.append(hex(latest + 3)[2:].upper())
                latest = latest + 3
            else:
                Tnotes.append(hex(latest + 2)[2:].upper())
                latest = latest + 2

        Tnotes.append(hex(first + (i+1)*12)[2:].upper())

    return Tnotes

blueoct = 5

bluemajors = []

bluemajors.append(scale("Cmajb", majblues(C0), blueoct))
bluemajors.append(scale("C#majb", majblues(Cf0), blueoct))
bluemajors.append(scale("Dmajb", majblues(D0), blueoct))
bluemajors.append(scale("D#majb", majblues(Df0), blueoct))
bluemajors.append(scale("Emajb", majblues(E0), blueoct))
bluemajors.append(scale("Fmajb", majblues(F0), blueoct))
bluemajors.append(scale("F#majb", majblues(Ff0), blueoct))
bluemajors.append(scale("Gmajb", majblues(G0), blueoct))
bluemajors.append(scale("G#majb", majblues(Gf0), blueoct))
bluemajors.append(scale("Amajb", majblues(A0), blueoct))
bluemajors.append(scale("A#majb", majblues(Af0), blueoct))
bluemajors.append(scale("Bmajb", majblues(B0), blueoct))

#print(bluemajors[0].name, bluemajors[0].notes)

def minblues(root):

    Tnotes = []
    
    first = int(root, 16)  # Convert hexadecimal string to integer
    Tnotes.append(root)
    latest = first
    
    
    for i in range(5):
        for n in range(1, 6):
            if n == 3 or n == 4:
                Tnotes.append(hex(latest + 1)[2:].upper())
                latest = latest + 1
            elif n == 1 or n == 5:
                Tnotes.append(hex(latest + 3)[2:].upper())
                latest = latest + 3
            else:
                Tnotes.append(hex(latest + 2)[2:].upper())
                latest = latest + 2

        Tnotes.append(hex(first + (i+1)*12)[2:].upper())

    return Tnotes
    

blueminors = []

blueminors.append(scale("Cminb", minblues(C0), blueoct))
blueminors.append(scale("C#minb", minblues(Cf0), blueoct))
blueminors.append(scale("Dminb", minblues(D0), blueoct))
blueminors.append(scale("D#minb", minblues(Df0), blueoct))
blueminors.append(scale("Eminb", minblues(E0), blueoct))
blueminors.append(scale("Fminb", minblues(F0), blueoct))
blueminors.append(scale("F#minb", minblues(Ff0), blueoct))
blueminors.append(scale("Gminb", minblues(G0), blueoct))
blueminors.append(scale("G#minb", minblues(Gf0), blueoct))
blueminors.append(scale("Aminb", minblues(A0), blueoct))
blueminors.append(scale("A#minb", minblues(Af0), blueoct))
blueminors.append(scale("Bminb", minblues(B0), blueoct))

#print(blueminors[0].name, blueminors[0].notes)
