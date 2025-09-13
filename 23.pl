% --- FACTS ---

% Male members
male(john).
male(mike).
male(paul).
male(raj).
male(aryan).

% Female members
female(linda).
female(susan).
female(anna).
female(rekha).

% Parent relationships
parent(john, mike).
parent(linda, mike).

parent(john, susan).
parent(linda, susan).

parent(mike, paul).
parent(anna, paul).

parent(mike, aryan).
parent(anna, aryan).

parent(susan, raj).
parent(raj, rekha).

% --- RULES ---

% Father rule
father(X, Y) :- 
    male(X), parent(X, Y).

% Mother rule
mother(X, Y) :- 
    female(X), parent(X, Y).

% Sibling rule
sibling(X, Y) :-
    parent(Z, X), parent(Z, Y),
    X \= Y.

% Brother rule
brother(X, Y) :-
    sibling(X, Y), male(X).

% Sister rule
sister(X, Y) :-
    sibling(X, Y), female(X).

% Grandparent rule
grandparent(X, Y) :-
    parent(X, Z), parent(Z, Y).

% Grandfather rule
grandfather(X, Y) :-
    grandparent(X, Y), male(X).

% Grandmother rule
grandmother(X, Y) :-
    grandparent(X, Y), female(X).

% Uncle rule
uncle(X, Y) :-
    brother(X, Z), parent(Z, Y).

% Aunt rule
aunt(X, Y) :-
    sister(X, Z), parent(Z, Y).
