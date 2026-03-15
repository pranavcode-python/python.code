atts=1
pranv=119
userguess=int(input("guess the number:"))     
while userguess != pranv:
      print("wrong,try again")
      userguess=int(input("guess the number:"))
      atts=atts+1

print(f"correct guess{userguess}")
print(atts)

    
