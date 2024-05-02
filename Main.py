# C950 - Webinar-4 - Python Modules
# W-4_ChainingHashTable_zyBooks_Key-Value_CSV_Greedy_Dijkstra_Main.py
# Ref: zyBooks: Figure 7.8.2: Hash table using chaining.
# Ref: zyBooks: 3.3.1: MakeChange greedy algorithm.
# Ref: zyBooks: zyDE 6.12.1: Dijkstra's shortest path example.
# Ref: Graph Data Structure 4. Dijkstra’s Shortest Path Algorithm: https://www.youtube.com/watch?v=pVfj6mxhdMw
'''
Add this file to the project
BestMovies.csv:
-----------------------
ID, Name, Year, Price, City, State
1, "CITIZEN KANE", 1941, 25.00, Salt Lake City, Utah
2, "CASABLANCA", 1942, 25.00, Helena, Montana
3, "THE GODFATHER", 1972, 10.00, Santa Fe, New Mexico
4, "GONE WITH THE WIND", 1939, 10.00, Austin, Texas
5, "LAWRENCE OF ARABIA", 1962, 10.00, Lincoln, Nebraska
6, "THE WIZARD OF OZ", 1939, 10.00, Madison, Wisconsin
7, "THE GRADUATE", 1967, 5.00, New York, New York
8, "ON THE WATERFRONT", 1954, 5.00, Columbus, Ohio
9, "SCHINDLER'S LIST", 1993, 5.00, Raleigh, North Carolina
10, "SINGIN' IN THE RAIN", 1952, 5.00, Orlando, Florida
11, "STAR WARS", 1977, 1.00, Montgomery, Alabama
-----------------------
'''
# copy commented codes below and create these modules
from Hash import ChainingHashTable
from CSV import loadMovieData
from Greedy import greedyAlgorithmMinExpenses
from Dijkstra import Vertex, Graph, dijkstra_shortest_path, get_shortest_path, get_shortest_path_city


# Hash table instance
myHash = ChainingHashTable()

# Load movies to Hash Table
loadMovieData('BestMovies.csv', myHash)


def getMovieData():
    print("BestMovies from Hashtable:")
    # Fetch data from Hash Table
    for i in range(len(myHash.table) + 1):
        print("Movie: {}".format(myHash.search(i + 1)))  # 1 to 11 is sent to myHash.search()


getMovieData()
# Movie CSV Data import - END



print("\nGreedy Algorithm: Min Expenses => Max Profits")
greedyAlgorithmMinExpenses(102)  # $102.00 budget
greedyAlgorithmMinExpenses(94)  # $94.00 budget
greedyAlgorithmMinExpenses(71)  # $71.00 budget
greedyAlgorithmMinExpenses(200)  # $200.00 budget
# Greedy Algorithm - END


def dijkstraAlgorithmShorthestPath():
    # Dijkstra shortest path main
    # Program to find shortest paths from vertex A.
    g = Graph()

    # add Vertices
    vertex_1 = Vertex("1")  # 1, "CITIZEN KANE", 1941, 25.00, Salt Lake City, Utah
    g.add_vertex(vertex_1)
    vertex_2 = Vertex("2")  # 2, "CASABLANCA", 1942, 25.00, Helena, Montana
    g.add_vertex(vertex_2)
    vertex_3 = Vertex("3")  # 3, "THE GODFATHER", 1972, 10.00, Santa Fe, New Mexico
    g.add_vertex(vertex_3)
    vertex_4 = Vertex("4")  # 4, "GONE WITH THE WIND", 1939, 10.00, Austin, Texas
    g.add_vertex(vertex_4)
    vertex_5 = Vertex("5")  # 5, "LAWRENCE OF ARABIA", 1962, 10.00, Lincoln, Nebraska
    g.add_vertex(vertex_5)
    vertex_6 = Vertex("6")  # 6, "THE WIZARD OF OZ", 1939, 10.00, Madison, Wisconsin
    g.add_vertex(vertex_6)
    vertex_7 = Vertex("7")  # 7, "THE GRADUATE", 1967, 5.00, New York, New York
    g.add_vertex(vertex_7)
    vertex_8 = Vertex("8")  # 8, "ON THE WATERFRONT", 1954, 5.00, Columbus, Ohio
    g.add_vertex(vertex_8)
    vertex_9 = Vertex("9")  # 9, "SCHINDLER'S LIST", 1993, 5.00, Raleigh, North Carolina
    g.add_vertex(vertex_9)
    vertex_10 = Vertex("10")  # 10, "SINGIN' IN THE RAIN", 1952, 5.00, Orlando, Florida
    g.add_vertex(vertex_10)
    vertex_11 = Vertex("11")  # 11, "STAR WARS", 1977, 1.00, Montgomery, Alabama
    g.add_vertex(vertex_11)

    # add Edges
    g.add_undirected_edge(vertex_1, vertex_2, 484)  # 484 miles
    g.add_undirected_edge(vertex_1, vertex_3, 626)
    g.add_undirected_edge(vertex_2, vertex_6, 1306)
    g.add_undirected_edge(vertex_3, vertex_5, 774)
    g.add_undirected_edge(vertex_3, vertex_4, 687)
    g.add_undirected_edge(vertex_4, vertex_11, 797)
    g.add_undirected_edge(vertex_5, vertex_6, 482)
    g.add_undirected_edge(vertex_6, vertex_7, 936)
    g.add_undirected_edge(vertex_7, vertex_8, 535)
    g.add_undirected_edge(vertex_7, vertex_9, 504)
    g.add_undirected_edge(vertex_9, vertex_10, 594)
    g.add_undirected_edge(vertex_11, vertex_5, 970)
    g.add_undirected_edge(vertex_11, vertex_8, 664)
    g.add_undirected_edge(vertex_11, vertex_9, 567)
    g.add_undirected_edge(vertex_11, vertex_10, 453)

    # Run Dijkstra's algorithm first.
    dijkstra_shortest_path(g, vertex_1)

    # Get the vertices by the label for convenience; display shortest path for each vertex
    # from vertex_1.
    print("\nDijkstra shortest path:")
    for v in g.adjacency_list:
        if v.pred_vertex is None and v is not vertex_1:
            print("1 to %s ==> no path exists" % v.label)
        else:
            print("1 to %s ==> %s (total distance: %g)" % (v.label, get_shortest_path(vertex_1, v), v.distance))

    print("\nDijkstra shortest path with Cities:")
    for v in g.adjacency_list:
        myMovie = myHash.search(int(v.label))
        if v.pred_vertex is None and v is not vertex_1:
            print("Salt Lake City to %s ==> no path exists" % myMovie.city)
        else:
            print("Salt Lake City to %s ==> %s (total distance: %g)" % (
            myMovie.city, get_shortest_path_city(vertex_1, v, myHash), v.distance))


dijkstraAlgorithmShorthestPath()
# Dijkstra shortest path - END

# main - START
if __name__ == '__main__':
    print("\nWelcome to C950: Classic Movies: Hash Table, CSV Import, Greedy Algorithm, Dijkstra Algorithm")

    # loop until user is satisfied
    isExit = True
    while (isExit):
        print("\nOptions:")
        print("1. Get Movie Data")
        print("2. Run Greedy Algorithm with a Budget")
        print("3. Run Dijkstra Algorithm")
        print("4. Exit the Program")
        option = input("Chose an option (1,2,3 or 4): ")
        if option == "1":
            getMovieData()
        elif option == "2":
            budget = int(input("What is your budget (ex. 150)? "))
            greedyAlgorithmMinExpenses(budget)
        elif option == "3":
            dijkstraAlgorithmShorthestPath()
        elif option == "4":
            isExit = False
        else:
            print("Wrong option, please try again!")
            # main - END