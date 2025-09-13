% --- Facts: planet(Name, OrderFromSun, Type, Diameter(km)) ---

planet(mercury, 1, terrestrial, 4879).
planet(venus,   2, terrestrial, 12104).
planet(earth,   3, terrestrial, 12742).
planet(mars,    4, terrestrial, 6779).
planet(jupiter, 5, gas_giant,   139820).
planet(saturn,  6, gas_giant,   116460).
planet(uranus,  7, ice_giant,   50724).
planet(neptune, 8, ice_giant,   49244).

% --- Rules ---

% closer_to_sun(P1, P2) :- P1 is closer to the sun than P2.
closer_to_sun(P1, P2) :-
    planet(P1, O1, _, _),
    planet(P2, O2, _, _),
    O1 < O2.

% bigger(P1, P2) :- P1 has larger diameter than P2.
bigger(P1, P2) :-
    planet(P1, _, _, D1),
    planet(P2, _, _, D2),
    D1 > D2.
20
