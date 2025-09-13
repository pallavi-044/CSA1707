% --- Knowledge Base: Birds and flying ability ---
% Format: bird(Name, CanFly).

bird(sparrow, yes).
bird(penguin, no).
bird(crow, yes).
bird(ostrich, no).
bird(parrot, yes).
bird(kiwi, no).

% --- Rule to check if a bird can fly ---
can_fly(Bird) :-
    bird(Bird, yes).

cannot_fly(Bird) :-
    bird(Bird, no).
22nd
