# CSV.py
# Movie CSV Data import - START
import csv

class Movie:
    def __init__(self, ID, name, year, price, city, state, status):
        self.ID = ID
        self.name = name
        self.year = year
        self.price = price
        self.city = city
        self.state = state
        self.status = status

    def __str__(self):  # overwite print(Movie) otherwise it will print object reference
        return "%s, %s, %s, %s, %s, %s, %s" % (
        self.ID, self.name, self.year, self.price, self.city, self.state, self.status)


def loadMovieData(fileName, myHash):
    with open(fileName) as bestMovies:
        movieData = csv.reader(bestMovies, delimiter=',')
        next(movieData)  # skip header
        for movie in movieData:
            mID = int(movie[0])
            mName = movie[1]
            mYear = movie[2]
            mPrice = movie[3]
            mCity = movie[4]
            mState = movie[5]
            mStatus = "Loaded"

            # movie object
            m = Movie(mID, mName, mYear, mPrice, mCity, mState, mStatus)
            # print(m)

            # insert it into the hash table
            myHash.insert(mID, m)


# ---------------------------------------------------------
'''
# Hash table instance 
myHash = ChainingHashTable()

# Load movies to Hash Table
loadMovieData('BestMovies.csv', myHash)

def getMovieData():
    print("BestMovies from Hashtable:")
    # Fetch data from Hash Table
    for i in range(len(myHash.table)+1): 
        print("Movie: {}".format(myHash.search(i+1))) # 1 to 11 is sent to myHash.search()

getMovieData()
# Movie CSV Data import - END
'''