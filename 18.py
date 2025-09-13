% --- Knowledge Base: Person facts with Name and DOB ---
% Format: person(Name, dob(Day, Month, Year)).

person('Alice', dob(12, may, 2000)).
person('Bob', dob(25, december, 1998)).
person('Charlie', dob(5, july, 2002)).
person('Deeksha', dob(13, september, 2003)).

% --- Rules to query the database ---

% Find DOB of a person
get_dob(Name, DOB) :-
    person(Name, DOB).

% Find who is born on a particular date
born_on(Day, Month, Year, Name) :-
    person(Name, dob(Day, Month, Year)).

% Find all people born in a given month
born_in_month(Month, Name) :-
    person(Name, dob(_, Month, _)).
