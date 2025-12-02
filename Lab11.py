import os
import matplotlib.pyplot as plt

submissions = os.listdir("data/submissions")

def main():
    print("1. Student grade")
    print("2. Assignment statistics")
    print("3. Assignment graph")

    inp = int(input("Enter your selection: "))

    if inp == 1:
        total_score = 0
        name = input("Enter your name: ")
        l = open("data/students.txt", "r")
        id = ""
        for line in l:
            if name in line:
                id = line[0:3]

        l.close()
        if id == "":
            print("Student not found")
            return

        a = open("data/assignments.txt", "r")

        assignment_ids = []
        max_scores = []

        for line in a:
            new_line = line.rstrip('\n')
            if len(new_line) == 4 or len(new_line) == 5:
                try:
                    int(new_line)
                    assignment_ids.append(new_line)
                except ValueError: pass

            if len(new_line) == 2 or len(new_line) == 3:
                try:
                    int(new_line)
                    max_scores.append(new_line)
                except ValueError: pass
        a.close()
        for i in range(len(assignment_ids)):
            for submission in submissions:
                sub = open(f"data/submissions/{submission}", "r")
                stud_id, assign_id, score = sub.readline().rstrip('\n').split('|')
                if id in stud_id and assignment_ids[i] in assign_id:
                    total_score += int(score) / 100.0 * int(max_scores[i])

                sub.close()
        total_score /= 10
        print(f"{round(total_score)}%")

    if inp == 2:
        assign_name = input("What is the assignment name: ")
        a = open("data/assignments.txt", "r")

        assign_id = "-1"
        last = False
        for line in a:
            if last:
                assign_id = line.rstrip('\n')
                last = False
            if assign_name == line.rstrip('\n'):
                last = True
        a.close()

        if assign_name == "-1":
            print("Assignment not found")
            return

        max = 0
        min = 100
        scores = []
        for submission in submissions:
            sub = open(f"data/submissions/{submission}", "r")
            stud_id, assn_id, score = sub.readline().rstrip('\n').split('|')
            if assign_id == assn_id:
                student_score = int(score)
                scores.append(student_score)

                max = student_score if student_score > max else max
                min = student_score if student_score < min else min

            sub.close()

        avg = sum(scores) / len(scores)

        print(f"Min: {min}%")
        print(f"Avg: {round(avg)}%")
        print(f"Max: {max}%")
    if inp == 3:
        assign_name = input("What is the assignment name: ")
        a = open("data/assignments.txt", "r")

        assign_id = "-1"
        last = False
        for line in a:
            if last:
                assign_id = line.rstrip('\n')
                last = False
            if assign_name == line.rstrip('\n'):
                last = True
        a.close()

        if assign_name == "-1":
            print("Assignment not found")
            return

        scores = []
        for submission in submissions:
            sub = open(f"data/submissions/{submission}", "r")
            stud_id, assn_id, score = sub.readline().rstrip('\n').split('|')
            if assign_id == assn_id:
                student_score = int(score)
                scores.append(student_score)

        plt.hist(scores, bins=[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70,75, 80, 85, 90, 95, 100])
        plt.show()


if __name__ == '__main__':
    main()