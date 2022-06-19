
import math
from collections import deque

class Movie:

    def __init__(self):
        self.adjacent = []
        self.d = math.inf
        self.visited = False

def BFS(s):
    q = deque()
    s.visited = True
    s.d = -1
    q.append(s)
    while len(q):
        v = q.popleft()
        for neighbor in v.adjacent:
            if not neighbor.visited:
                neighbor.visited = True
                neighbor.d = v.d+1
                q.append(neighbor)

N, H, L = map(int,input().split())

#generate list of all movies
movies = []
for _ in range(N):
    movies.append(Movie())

#start node is connected to all horror movies
horror_movies = list(map(int,input().split()))
start_node = Movie()
#add horror movies to special starting node
for movie in horror_movies:
    start_node.adjacent.append(movies[movie])
    movies[movie].adjacent.append(start_node)

for line in range(L):
    movie1, movie2 = map(int,input().split())
    #add edge movie1-movie2 in movie1.adjacent and movie2.adjacent
    movies[movie1].adjacent.append(movies[movie2])
    movies[movie2].adjacent.append(movies[movie1])

#compute the distances to the starting node
# distance = score (aka how far the movie is from all horror movies)
BFS(start_node)

#linear search to find the best movie
max_score = 0
best_movie = 0
for i in range(N):
    if movies[i].d>max_score:
        max_score = movies[i].d
        best_movie = i

print(best_movie)














