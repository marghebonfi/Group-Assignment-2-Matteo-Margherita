import time
def main():
    questions=["1) My program for X failed the testing and gave error Y. The last change I made was Z, can you help take a look?",
    "2)My program must perform task X. Its time complexity should be as small as possible. Each data structure has its own advantage, Y is faster for W meanwhile Z is faster for V. Which data structure should I use? Data structure Y or data structure Z?",
    "3)Usually, a code has to be as efficient as possible, but at the same time it should readable and maintainable. How do we find the right balance between readability and time efficiency?",
    "4)It’s important to have a code which satisfies the client, and so it should work in all scenarios. How to write meaningful unit tests to test the functionality and efficiency of the code?",
    "5)How should the code be structured for it to be as readable and maintainable as possible? When should we create a different function because the other one is too large becoming incomprehensible?",
    "6) What is the difference in programming with software engineer and without?",
    "7) What are the key rules to develop the best software?",
    "8) How will software engineering help in solving more complex problems?",
    "9) Can software engineer help improve already existing software?",
    "10) How to make the best architectural design decision? "]
    answers=["First of you all you have to check the error messages. The error messages consist of two parts, the error message and the stack trace. The error message is what’s wrong- good error messages are helpful and tell you what you should do. The stack-trace/tracebacks on the other hand is where it’s wrong. So it’s important to understand the error message as it allows us to identify immediately the whereabouts and the reason of the encountered problems.",
             "Since the program is commissioned by the client, then the programmer must first understand what the objective and the feature is needed most, according to his needs then we know if we have to put more weight  whether on W or on V, after all this process of careful analysis of the conceptualized problem we can start design the optimal algorithm and data structure for it.",
             "We can use a citation by Abelson & Sussman: Programs must be written for people to read, and only incidentally for machines to execute, which means in general It’s more important that a program can be easily understood than for it to be as efficient as possible, since nowadays thanks to the hardware resources we have, performance ceased to be a major limiting fact. Efficiency of the program becomes important only when the performance may become a major issue for the normal functioning of the code, however overall simplicity, readability is still more important, since performance optimized code is more complex, harder to read and maintain, and surely more bug-prone than the simplest working solution",
             "For unit testing, we can follow 2 types of approaches: Test driven where first you do the tests and then the code, and vice versa code first, test second. Instead of writing code, then writing test.  Write code then look at what you think the code should be doing. Think about all the intended uses of it and then write a test for each case. Writing tests is usually faster but more involved than the coding itself. The tests should test the intention. Thinking about the intentions most of the time you wind up finding corner cases which you didn’t consider beforehand.",
             "When it comes to making readable and maintainable code, there are many rules. First, it’s important to have comments and a nitid documentation, while it’s important to have comments, at the same time you must be careful to avoid obvious comment which sometimes can do more harm than good. Second, it’s important to follow a consistent style of indentation, naming scheme and whenever it’s possible group few lines of code which are similar (for example codes to load the templates). Worth mentioning is also the DRY principle which stands for Don’t Repeat Yourself, it follows the principle: automate repetitive task, so the same piece of code should not be repeated over and over again. Avoid deep nesting as it makes the hard to read and follow and therefore should also limit the line length. Last not for importance is the name of variables, they shouldn’t be letters but have a meaning which can be understood right away by others programmer. It’s important to never create a function which is too large, as it becomes difficult to follow the logical reasoning behind it and to maintain, most of the time it can be divided in smaller pieces which are more readable and maintainable.",
             "The biggest difference is the a generic programmer will just focus on a single stage of the project while a software engineer will overview the entire project from head to toe.",
             "The most important rule to develop a good software are: clarity, a program will probably be read by your collegues as well and not just you so it's really important it's easy to read for everyone; usign coding standard: for every language there are standards that need to be used to make the code easy to read; using libraries: there are plenty of excellent libraries for every language, so it would just be a waste of time not to use them.",
             "The best way to solve complex problem with software engineering is to divide them into smaller ones. Another way is often used is trying to explain the problem to someone who is not working in the field and therefore would not understand technical terms, this will help create a clear image of the problem in your mind",
             "A software engineer job is basically to understand problems and try to solve them in the most efficent way using technology, nowadays there are a lot of existing software that were developed years ago and that could be improved with the help of software engineering",
             "Architectural design is a creative process where you design a system organization that will satisfy the functional and non-functional requirements of a system. Because it is a creative process, the activities within the process depend on the type of system being developed, the background and experience of the system architect, and the specific requirements for the system. It is therefore useful to think of architectural design as a series of decisions to be made rather than a sequence of activities. During the architectural design process, system architects have to make a number of structural decisions that profoundly affect the system and its development process. "]
    wrongAnswers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    quit=False
    while(not quit):
        correct=0
        wrong_answers=[0,0,0,0,0,0,0,0,0,0]
        start=time.time()
        for i in range(10):
            answer=input(f"{questions[i]}\n")
            if len(answer)==0 or answer!=answers[i] :
                wrong_answers[i]=1
            else:
                correct+=1
        end=time.time()
        print(f"Right answers: {correct}")
        print(f"Time: {end-start}")
        for i in range(10):
            if wrong_answers[i]==1:
                print(f"Right answer for question {i+1}:\n{answers[i]}")
        choice=input("Continue or quit(enter the word or 1 for continue and 0 for quit)").upper()
        if choice==0 or choice =="QUIT" or len(choice)==0:
            quit=True

main()



if __name__ == '__main__':
    main
