% towers_of_hanoi(N, Source, Target, Auxiliary).
% Move N disks from Source to Target using Auxiliary.

towers_of_hanoi(1, From, To, _) :-
    write('Move disk from '), write(From),
    write(' to '), write(To), nl.

towers_of_hanoi(N, From, To, Aux) :-
    N > 1,
    M is N - 1,
    towers_of_hanoi(M, From, Aux, To),
    towers_of_hanoi(1, From, To, _),
    towers_of_hanoi(M, Aux, To, From).
