% facts: disease has these symptoms
disease(flu,     [fever, cough, headache]).
disease(malaria, [fever, chills, sweating]).
disease(measles, [fever, cough, rash]).

% ask symptoms and match
diagnose(D) :-
    disease(D, Symptoms),
    check_all(Symptoms).

check_all([]).
check_all([S|Rest]) :-
    write('Does patient have '), write(S), write('? (yes/no) '),
    read(yes), 
    check_all(Rest).
