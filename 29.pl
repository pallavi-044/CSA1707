% facts
employee(alice, sales).
employee(bob, tech).
employee(carol, manager).

% rules
access(X, report) :- employee(X, sales).
access(X, server) :- employee(X, tech).
approve(X) :- employee(X, manager).
