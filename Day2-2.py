s="1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,2,9,19,23,2,13,23,27,1,6,27,31,2,6,31,35,2,13,35,39,1,39,10,43,2,43,13,47,1,9,47,51,1,51,13,55,1,55,13,59,2,59,13,63,1,63,6,67,2,6,67,71,1,5,71,75,2,6,75,79,1,5,79,83,2,83,6,87,1,5,87,91,1,6,91,95,2,95,6,99,1,5,99,103,1,6,103,107,1,107,2,111,1,111,5,0,99,2,14,0,0"
# Replaced s[0] with 12 and s[2] with 2 as said in the question
s = list(map(int, s.split(',')))
for a in range(99):
        z=list(i for i in s)
        z[1]=a
        for b in range(99):
                z[2]=b
                for i in range(0, len(z), 4):
                        if z[i] == 99: break
                        try:
                                if z[i] == 1: z[s[i+3]] = z[z[i+1]] + z[z[i+2]]
                        except: pass
                        try:
                                if z[i] == 2: z[z[i+3]] = z[z[i+1]] * z[z[i+2]]
                        except: pass
                        
                if z[0] == 19690720:
                        print(100*a+b)
                        break
