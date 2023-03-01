grade = {'A+': 90, 'A' : 80, 'A-' : 70, 'B+' : 65, 'B' : 60, 'C+' : 55, 'C' : 50, 'D' : 45, 'E' : 40, 'G' : 0}
req_client1 = "subject "
req_client2 = " : mark: "
req_client3 = " : grade: "


def _subject_count():
    subject_count = 0
    request_client = input("number of examination subjects: ")
    subject_count = int(request_client)
    return subject_count


def _subject_mark(s_count):
    subject_mark = []
    for i in range(0, s_count):
        x = input(req_client1 + str(i+1) + req_client2)
        subject_mark.append(int(x))
    return subject_mark
 

def _subject_grade(s_mark):
    subject_grade = []
    for i in s_mark:
        for j in grade:
            if i >= grade[j]:
                subject_grade.append(j)
                break;
    return subject_grade


def _overall_grade(s_grade):
    print(s_grade)


def _overall_mark_count(s_count, s_mark):
    x = 0
    y = s_count * 100
    for i in s_mark:
        x += i
    print("overall mark:", x, "/", y)
    return x


def _overall_percentage_result(s_count, omark_count):
    x = s_count * 100
    y = (omark_count/s_count)
    print("overall result percentage:", str(y) + "%")
    return y


def _failure_standard_review(opercent_result):
    x = "failure standard review:"
    if opercent_result > grade["E"]:
        print(x, "PASSED")
    else:
        print(x, "FAILED")


def _average_grade():
    pass


def _result():
    _sc = _subject_count()
    _sm = _subject_mark(_sc)
    _sg = _subject_grade(_sm)
    print("EXAM RESULT:")
    for i in range(0, _sc):
        print(req_client1 + str(i+1) + req_client2 + str(_sm[i]) + req_client3 + str(_sg[i]))
    _overall_grade(_sg)
    _omc = _overall_mark_count(_sc, _sm)
    _opr = _overall_percentage_result(_sc, _omc)
    _failure_standard_review(_opr)
    # update idea: add gpa result


def main():
    _result()


main()
