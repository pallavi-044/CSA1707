% --- Facts ---
employee(alice, sales).
employee(bob, tech).
employee(carol, manager).

% --- Rules ---
access(X, report) :- employee(X, sales).
access(X, server) :- employee(X, tech).
approve(X) :- employee(X, manager).
