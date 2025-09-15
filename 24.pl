% state(MonkeyPos, BoxPos, MonkeyOnBox?, HasBanana?)
% MonkeyPos, BoxPos = door | window | middle
% MonkeyOnBox? = floor | onbox
% HasBanana? = no | yes

initial(state(door, window, floor, no)).
goal(state(_, _, _, yes)).

% Actions
move(state(door, B, floor, no), state(middle, B, floor, no)) :-
    write('Monkey walks to middle'), nl.

move(state(window, B, floor, no), state(middle, B, floor, no)) :-
    write('Monkey walks to middle'), nl.

move(state(middle, window, floor, no), state(middle, middle, floor, no)) :-
    write('Monkey pushes box to middle'), nl.

move(state(middle, middle, floor, no), state(middle, middle, onbox, no)) :-
    write('Monkey climbs box'), nl.

move(state(middle, middle, onbox, no), state(middle, middle, onbox, yes)) :-
    write('Monkey grabs banana'), nl.

% Plan until goal
plan(S) :-
    goal(S),
    write('Done!'), !.

plan(S) :-
    move(S, S1),
    plan(S1).
