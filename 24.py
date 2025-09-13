% simple diet facts

good_food(diabetes, vegetables).
good_food(diabetes, lean_meat).
good_food(hypertension, fruits).
good_food(hypertension, low_salt_food).

bad_food(diabetes, sweets).
bad_food(diabetes, sugar_drinks).
bad_food(hypertension, salty_snacks).
bad_food(hypertension, high_fat_food).

% rule to suggest diet by asking user for disease

suggest_diet :-
    write('Enter your disease (diabetes or hypertension): '), nl,
    read(Disease),
    % ensure Disease is valid
    (   (Disease = diabetes ; Disease = hypertension)
    ->  % collect good and bad foods
        findall(G, good_food(Disease, G), GoodList),
        findall(B, bad_food(Disease, B), BadList),
        write('Foods you should eat: '), write(GoodList), nl,
        write('Foods to avoid: '), write(BadList), nl
    ;   write('Sorry, unknown disease.'), nl
    ).
