:- dynamic post/4.   % Allow dynamic insertion of posts

% ---------- HTML Generators ----------
title_tag(Stream, Title) :-
    format(Stream, '<title>~w</title>~n', [Title]).

heading_tag(Stream, Text) :-
    format(Stream, '<h1>~w</h1>~n', [Text]).

paragraph_tag(Stream, Text) :-
    format(Stream, '<p>~w</p>~n', [Text]).

anchor_tag(Stream, URL, Text) :-
    format(Stream, '<a href="~w">~w</a>~n', [URL, Text]).

video_tag(Stream, VideoFile) :-
    format(Stream, '<video width="640" height="360" controls>~n', []),
    format(Stream, '<source src="~w" type="video/mp4">~n', [VideoFile]),
    format(Stream, 'Your browser does not support the video tag.~n</video>~n', []).

% ---------- Add a new blog post ----------
add_post(Title, URL, Excerpt, VideoFile) :-
    assertz(post(Title, URL, Excerpt, VideoFile)).

% ---------- Rule to display blog post ----------
show_post(Stream, Title, URL, Excerpt, VideoFile) :-
    heading_tag(Stream, Title),
    paragraph_tag(Stream, Excerpt),
    anchor_tag(Stream, URL, 'Read more'),
    video_tag(Stream, VideoFile),
    format(Stream, '<hr>~n', []).

% ---------- Rule to generate full blog file ----------
generate_blog :-
    open('blog.html', write, Stream),
    format(Stream, '<!DOCTYPE html>~n<html>~n<head>~n', []),
    title_tag(Stream, 'My Prolog Blog'),
    format(Stream, '</head>~n<body>~n', []),

    forall(post(Title, URL, Excerpt, VideoFile),
          show_post(Stream, Title, URL, Excerpt, VideoFile)),

    format(Stream, '</body>~n</html>', []),
    close(Stream).
