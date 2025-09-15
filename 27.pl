% --- Graph edges ---
edge(a,b). edge(a,c).
edge(b,d). edge(b,e).
edge(c,f). edge(e,g).

% --- BFS ---
bfs([[Goal|Path]|_], Goal, [Goal|Path]).
bfs([[Node|Path]|Rest], Goal, Sol) :-
    findall([X,Node|Path],
            (edge(Node,X), \+ member(X,[Node|Path])),
            Next),
    append(Rest, Next, Queue),
    bfs(Queue, Goal, Sol).

start_bfs(Start, Goal, Path) :-
    bfs([[Start]], Goal, RevPath),
    reverse(RevPath, Path).
