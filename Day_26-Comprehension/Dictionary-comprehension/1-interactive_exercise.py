sentence = "What is the Airspeed velocity of an Unladen Swallow?"

list=sentence.split()
result={word:len(word) for word in list}
print(result)