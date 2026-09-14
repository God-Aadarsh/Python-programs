questions = [("Whats used to print statement in python: "),
             ("What heavenly body is in the centre of solar system: "),
             ("What are you: ")]
options = [("A:print() B:helloworld() C:output() "), 
           ("A:earth B:sun C:moon"),
           ("A:GAY B:Hero C:Lesbian")]
answers= [("A"),("B"),("A")]
question_no = -1
correct_answer = 0
for question in questions:
    print(question)
    question_no += 1
    print(options[question_no])
    user_answer= (input("Enter the answer: ")).upper()
    if user_answer == answers[question_no]:
      print(f'Correct Answer! {answers[question_no]} is the correct answer..')
      correct_answer += 1
    else: 
      print(f'Incorrect Answer! {answers[question_no]} is the correct answer..')
    print("--------------------------")

total_score = ((correct_answer)/3) * 100
print("--------------------------")
print(f'Total Score: {total_score:.2f}% ')
print("--------------------------")


