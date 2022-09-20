print ('hello world!')

greetings = ['hi', 'hello', 'hiya', 'hola earthlings' ]
print(greetings[3])


foodfav = {
    'mexican' : 'Carnitas',
    'chinese' : 'Fried rice',
    'greek' : 'Gyro'
}
print(foodfav['mexican'])


earthlings = [
    {
        "height in ft" : 5,
        "weight" : 220,
        "state" : "KY",
        "current loc": (38.2259, 85.7686),
        "weather" : "Summer" },
    {
        "height in ft" : 3,
        "weight" : 80,
        "state" : "NY",
        "current loc": (38.2259, 85.7686),
        "weather" : "Fall" }
]

print( earthlings[1]["current loc"])
