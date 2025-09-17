% Define vowels
vowel(a).
vowel(e).
vowel(i).
vowel(o).
vowel(u).

% Base case: empty list has 0 vowels
count_vowels([], 0).

% If Head is a vowel, count +1
count_vowels([H|T], N) :-
    vowel(H),
    count_vowels(T, N1),
    N is N1 + 1.

% If Head is not a vowel, skip
count_vowels([_|T], N) :-
    count_vowels(T, N).
% Define vowels
vowel(a).
vowel(e).
vowel(i).
vowel(o).
vowel(u).

% Base case: empty list has 0 vowels
count_vowels([], 0).

% If Head is a vowel, count +1
count_vowels([H|T], N) :-
    vowel(H),
    count_vowels(T, N1),
    N is N1 + 1.

% If Head is not a vowel, skip
count_vowels([_|T], N) :-
    count_vowels(T, N).
