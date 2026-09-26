quiz_list = [
    "Python Basics",
    "SQL Basics",
    "General Knowledge"
]

question_list = [

    [
        "Python Basics",
        "Which keyword is used to create a function?",
        "func",
        "def",
        "function",
        "create",
        "2"
    ],

    [
        "Python Basics",
        "Which data type stores multiple values in order?",
        "List",
        "Integer",
        "Boolean",
        "Float",
        "1"
    ],

    [
        "Python Basics",
        "What is the output of 10 + 5?",
        "10",
        "15",
        "20",
        "5",
        "2"
    ],

    [
        "SQL Basics",
        "Which command is used to retrieve data?",
        "INSERT",
        "DELETE",
        "SELECT",
        "UPDATE",
        "3"
    ],

    [
        "SQL Basics",
        "Which command is used to add a new row?",
        "INSERT",
        "SELECT",
        "UPDATE",
        "DROP",
        "1"
    ],

    [
        "SQL Basics",
        "Which clause is used to filter records?",
        "ORDER BY",
        "WHERE",
        "GROUP BY",
        "JOIN",
        "2"
    ],

    [
        "General Knowledge",
        "What is the capital of India?",
        "Mumbai",
        "Delhi",
        "Chennai",
        "Kolkata",
        "2"
    ],

    [
        "General Knowledge",
        "How many days are there in a week?",
        "5",
        "6",
        "7",
        "8",
        "3"
    ],

    [
        "General Knowledge",
        "Which planet is known as the Red Planet?",
        "Earth",
        "Mars",
        "Jupiter",
        "Venus",
        "2"
    ]
]

score_list = []

def add_quiz():

    quiz_name = input("Enter quiz name: ")

    quiz_list.append(quiz_name)

    print("Quiz added successfully!")


def add_question():

    if len(quiz_list) == 0:

        print("First add a quiz.")

    else:

        print("\nAvailable Quizzes:")

        for i in range(len(quiz_list)):
            print(i + 1, ".", quiz_list[i])

        quiz_number = int(input("Select quiz number: "))

        quiz_name = quiz_list[quiz_number - 1]

        question = input("Enter question: ")

        option1 = input("Enter option 1: ")
        option2 = input("Enter option 2: ")
        option3 = input("Enter option 3: ")
        option4 = input("Enter option 4: ")

        answer = input("Enter correct answer (1-4): ")

        data = [
            quiz_name,
            question,
            option1,
            option2,
            option3,
            option4,
            answer
        ]

        question_list.append(data)

        print("Question added successfully!")


def modify_question():

    if len(question_list) == 0:

        print("No questions available.")

    else:

        print("\nQuestions:")

        for i in range(len(question_list)):
            print(i + 1, ".", question_list[i][1])

        number = int(input("Enter question number: "))

        new_question = input("Enter new question: ")

        question_list[number - 1][1] = new_question

        print("Question modified successfully!")


def delete_question():

    if len(question_list) == 0:

        print("No questions available.")

    else:

        print("\nQuestions:")

        for i in range(len(question_list)):
            print(i + 1, ".", question_list[i][1])

        number = int(input("Enter question number: "))

        question_list.pop(number - 1)

        print("Question deleted successfully!")


def delete_quiz():

    if len(quiz_list) == 0:

        print("No quizzes available.")

    else:

        print("\nAvailable Quizzes:")

        for i in range(len(quiz_list)):
            print(i + 1, ".", quiz_list[i])

        number = int(input("Enter quiz number: "))

        quiz_name = quiz_list[number - 1]

        quiz_list.pop(number - 1)

        i = 0

        while i < len(question_list):

            if question_list[i][0] == quiz_name:

                question_list.pop(i)

            else:

                i = i + 1

        print("Quiz deleted successfully!")


def view_quizzes():

    if len(quiz_list) == 0:

        print("No quizzes available.")

    else:

        print("\n========== AVAILABLE QUIZZES ==========")

        for i in range(len(quiz_list)):
            print(i + 1, ".", quiz_list[i])

def admin_menu():

    while True:

        print("\n========== ADMIN SECTION ==========")

        print("1. Add Quiz")
        print("2. Add Question")
        print("3. Modify Question")
        print("4. Delete Question")
        print("5. Delete Quiz")
        print("6. View Quizzes")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            add_quiz()

        elif choice == "2":

            add_question()

        elif choice == "3":

            modify_question()

        elif choice == "4":

            delete_question()

        elif choice == "5":

            delete_quiz()

        elif choice == "6":

            view_quizzes()

        elif choice == "7":

            print("Returning to main menu...")
            break

        else:

            print("Invalid choice!")


def view_student_quizzes():

    view_quizzes()


def start_quiz():

    if len(quiz_list) == 0:

        print("No quizzes available.")

    else:

        print("\nAvailable Quizzes:")

        for i in range(len(quiz_list)):
            print(i + 1, ".", quiz_list[i])

        quiz_number = int(input("Select quiz number: "))

        selected_quiz = quiz_list[quiz_number - 1]

        print("\nStarting Quiz:", selected_quiz)

        score = 0

        for i in range(len(question_list)):

            if question_list[i][0] == selected_quiz:

                print("\nQuestion:", question_list[i][1])

                print("1.", question_list[i][2])
                print("2.", question_list[i][3])
                print("3.", question_list[i][4])
                print("4.", question_list[i][5])

                answer = input("Enter your answer: ")

                if answer == question_list[i][6]:

                    score = score + 1

                    print("Correct!")

                else:

                    print("Wrong!")


        score_list.append(score)

        print("\nQuiz Completed!")
        print("Your Score:", score)


def answer_questions():

    if len(question_list) == 0:

        print("No questions available.")

    else:

        print("\nQuestions:")

        for i in range(len(question_list)):

            print(i + 1, ".", question_list[i][1])

        print("Answer questions using option numbers.")


def submit_quiz():

    print("Quiz submitted successfully!")


def view_score():

    if len(score_list) == 0:

        print("No score available.")

    else:

        print("\n========== SCORES ==========")

        for i in range(len(score_list)):

            print(
                "Quiz",
                i + 1,
                "Score:",
                score_list[i]
            )

def student_menu():

    while True:

        print("\n========== STUDENT SECTION ==========")

        print("1. View Available Quizzes")
        print("2. Start Quiz")
        print("3. Answer Questions")
        print("4. Submit Quiz")
        print("5. View Score")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            view_student_quizzes()

        elif choice == "2":

            start_quiz()

        elif choice == "3":

            answer_questions()

        elif choice == "4":

            submit_quiz()

        elif choice == "5":

            view_score()

        elif choice == "6":

            print("Returning to main menu...")
            break

        else:

            print("Invalid choice!")


while True:

    print("\n================================")
    print("       QUIZ MANAGEMENT SYSTEM")
    print("================================")

    print("1. ADMIN")
    print("2. STUDENT")
    print("3. EXIT")

    role = input("Select Role: ")

    if role == "1":

        admin_menu()

    elif role == "2":

        student_menu()

    elif role == "3":

        print("Thank you for using Quiz Management System!")
        break

    else:

        print("Invalid role!")
