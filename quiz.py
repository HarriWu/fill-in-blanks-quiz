list_questions=["Three days was simply not a(n) ---- amount of time to complete such a lot of work","You don't need to be a(n) ---- see what the problem here is","Make sure you read all the ---- carefully before setting up the device","There are special schools for students with ---- disorders","Seeing that some of their ---- have one, children ask their parents for a mobile phone at a very early age","When the space probe landed on Mars, the first thing it did was to take a(n) ---- from the Martian soil","The students gel a monthly ---- which usually consists of writing a report","Half of the courses in our department were ----. There were a variety of courses to choose from","Children need to be taught to learn ---- at primary school, otherwise they can't get anywhere in their school life","In most countries, schools have two ----, or semesters, while in others there can be up to six"]
list_answers=["acceptable","genius","instructions","mental","peers","specimen","assignment","optional","independently","terms"]
def pick_a_level():#Asks user to pick the level of difficulty for the quiz and returns the level of difficulty
    level=int(input("Type 1 for easy, 2 for medium, and 3 for hard: "))
    return level
print("Fill in the blanks represented by ---- with the words in this word bank {terms|independently|optional|assignment|specimen|peers|mental|instructions|genius|acceptable}")
level=pick_a_level()
user_chances=int(input("Put in how many chances you want to solve this quiz: "))
if level==1:
    number_of_questions=4
if level==2:
    number_of_questions=7
if level==3:
    number_of_questions=10
question=0
chances=0
while True:
    if question==number_of_questions:
        break
    if chances==user_chances:
        break
    print(list_questions[question])
    user_answer=input("Put in Answer here:")
    if user_answer==list_answers[question]:
        print(list_answers[question]+" is correct")
        question+=1
    else:
        print("Please Try Again")
        chances+=1