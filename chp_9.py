#1
with open("st.txt", "r") as f:
    print(f.read())


#2
answer = input("What is your favorite color? ")

with open("fav_color.txt", "w") as f:
    f.write(answer)


#3
import csv

movies = [["Top Gun", "Risky Business", "Minority Report"],
          ["Titanic", "The Revenant", "Inception"],
          ["Training Day", "Man on Fire", "Flight"]]

with open("movies.csv", "w") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=",")
    for movie_list in movies:
        spamwriter.writerow(movie_list)
