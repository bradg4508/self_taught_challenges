#1
tv = ["The Walking Dead",
         "Entourage",
         "The Sopranos",
         "The Vampire Diaries"]
for show in tv:
    print(show)


#2
for i in range(25,51):
    print(i)


#3
for n, show in enumerate(tv):
    print(show)
    print(n)


#4
i=0
nums = []
while i <=100:
    nums.append(i)
    i+=1

while True:
    response = input("Guess a number or enter \"q\" to quit: ")
    if response == "q":
        break
    try:
        response = int(response)
        if response in nums:
            print("You got it. That number is in the list.")
        else:
            print("Sorry, that number is not in the list.")
    except ValueError:
        print("You need to guess a number or enter \"q\" to quit: ")


#5
list1 = [8,19,148,4]
list2 = [9,1,33,83]
multilist = []

for i in list1:
    for j in list2:
        multilist.append(i*j)

print(multilist)
