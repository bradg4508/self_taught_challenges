#1
word = "Camus"
print(word[0])
print(word[1])
print(word[2])
print(word[3])
print(word[4])


#2
responseone = input("Enter something that you wrote: ")
responsetwo = input("Enter where you sent it: ")

statement = "Yesterday I wrote a {}. I sent it to {}!".format(responseone,responsetwo)

print(statement)


#3
sentence = "aldous Huxley was born in 1894."
capsent = sentence.capitalize()
print(capsent)


#4
quest = "Where now? Who now? When now?"
splitq = quest.split("?")
splitq.pop()
splitq[1] = splitq[1].strip()
splitq[2] = splitq[2].strip()
print(splitq)


#5
sentlist = ["The",
             "fox",
             "jumped",
             "over",
             "the",
             "fence"
             "."]

newsent = " ".join(sentlist)
newsent = newsent[:-1] + "."
print(newsent)


#6
ssent = "A screaming comes across the sky."
newssent = ssent.replace("s", "$")
print(newssent)


#7
firstm = "Hemingway".index("m")
print(firstm)


#8
quote1 = "\"Drink up,\" said Ford, \"You've got three pints to get through.\""
quote2 = "\"I forgot,\" Lennie said softly. \"I tried not to forget. Honest to God I did, George.\""
quote3 = "\"Yes,\" I said, \"I have a reason,\" and added very softly, \"My God.\""

print(quote1)
print(quote2)
print(quote3)


#9
threeword = "three"
concatadd = threeword + threeword + threeword
concatmulti = threeword * 3

print(concatadd)
print(concatmulti)


#10
longsent = "It was a bright cold day in April, and the clocks were striking thirteen."
slicesent = longsent[:33]
print(slicesent)
