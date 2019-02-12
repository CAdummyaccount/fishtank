print ("please enter length")
L=input()
print ("please enter width")
W=input()
print ("please enter height")
H=input()



litres=round((int(L)*int(W)*int(H)/276)*4.454)
print (str(litres) + " Litres")
ideal_C = 425
ideal_M = 1350
ideal_Al = 8.5

print ("Ammonia")
A=int(input())
if A>0:
    print ("-Perform a water change-")
if A==0: print ("-All Well-")

print ("NitrItes")
nI=int(input())    
if nI>0:  
    print ("-Perform a water change-")
if nI==0: print ("-All Well-")

print ("NitrAtes")
nA=int(input())
if nA>20:  
    print ("-Perform a water change-")
if nA in range (0,21):
    print ("-All Well-")

print ("Phosphate")
P=float(input())
if P>0.03:  
   print ("-Perform a water change-")
if P>0 and P<0.029: print ("-All Well-")

print ("Calcium")
C=int(input())
if C>430:
    print ("-Perform a water change-")
elif C<420:
    diff_C = ideal_C - C
    print ("-Dose Calcium- (needs {})".format(diff_C))
    print ("Dose " + str(round(0.0074*litres*diff_C)) + " ml's")
else:
    print ("-All Well-")


print ("Magnesium")
M=int(input())
if M>1360:  
   print ("-Perform a water change-")
elif C<1340:
    diff_M = ideal_M - M
    print ("-Dose Magnesium- (needs {})".format(diff_M))
    print ("Dose " + str(round(0.017*litres*diff_M)) + " ml's")
else:
    print ("-All Well-")

print ("Alkalinity")
Al=float(input())
if Al>9.5:
    print ("-Perform a water change-")
elif Al<8:
    diff_Al = ideal_Al - Al
    print ("-Dose Alkalinity- (needs {})".format(diff_Al))
    print ("Dose " + str(round(0.38*litres*diff_Al)) + "ml's")
else:
    print ("-All Well-")