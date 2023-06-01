                        # Kaun Banega Crorepati(KBC)
import random
list1 = ["What is capital of Punjab", "What 3*4*8*7*7*7*7 is?" , "What is synonym of bad?"]
qindex = random.randint(0, len(list1)-1)
question = list1[qindex]
print(question)


def answers():
    if qindex == 0:
        list2 = ["(a) Chandigarh" ,"(b) Delhi" , "(c) Jaipur" , "(d) None of these"]
        print(list2)
        a = input("Enter answer:")
        if a == "(a) Chandigarh" and a in list2:
            print("Your answer is", a, "you won Rs.10,000")
        else:
            print("Wrong answer, you have to go home with no money.")  
    elif qindex == 1:
        list3 = ["(a) 200000" , "(b) 230496" , "(c) 678950" , "(d) 123231" ]
        print(list3)
        b = input("Enter answer:")
        if b == "(b) 230496" and b in list3 :
            print("Correct answer", b, "you won Rs.20,000")
        else:
            print("Wrong answer, go home with Rs.10,000")
        
    elif qindex == 2:
        list4 = ["(a) good", "(b) worse", "(c) cool", "(d) best"]
        print(list4)
        c = input("Enter answer:")
        if c == "(a) good" and c in list4:
            print("Correct answer", c, "you won 50,000")
        else:
            print("wrong answer, go home back with Rs.20,000.") 
answers()


