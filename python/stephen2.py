maths=int(input("maths score"))
kisw=int(input("kisw score"))
english=int(input("english score"))
science=int(input("science score"))
socialstudies=int(input("socialstudies score"))
mean=(maths+kisw+english+science+socialstudies)/5
if (mean>=70 and mean<=100):
    print("Grade A")
if (mean>=60 and mean<70):
    print("Grade B")
if (mean>=50 and mean<60):
    print("Grade C")
if (mean>=40 and mean<50):
    print("Grade D")
if (mean>=0 and mean<40):
    print ("Fail")

