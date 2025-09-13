% student(Name, SubCode).
student(asha, cs101).
student(ravi, cs101).
student(priya, cs102).

% teacher(Name, SubCode).
teacher(rao, cs101).
teacher(leela, cs102).

% subject(SubCode, SubjectName).
subject(cs101, 'Programming').
subject(cs102, 'Data Structures').

% Which teacher teaches a student?
teacher_of_student(Student, Teacher) :-
    student(Student, Sub),
    teacher(Teacher, Sub).

% Which subject a student studies?
subject_of_student(Student, Subject) :-
    student(Student, Sub),
    subject(Sub, Subject).
