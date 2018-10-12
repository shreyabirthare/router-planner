<<<<<<< HEAD
from helpers import load_map_40
=======
from helpers import load_map
>>>>>>> e0d9b27e8eb41682a5c06d70a37e2c1ef2776067

MAP_40_ANSWERS = [
    (5, 34, [5, 16, 37, 12, 34]),
    (5, 5,  [5]),
<<<<<<< HEAD
    (8, 24, [8, 14, 16, 37, 12, 17, 10, 24])
]

def test(shortest_path_function):
    map_40 = load_map_40()
    correct = 0
    for start, goal, answer_path in MAP_40_ANSWERS:
        path = shortest_path_function(map_40, start, goal).path
=======
    (8, 24, [8, 30, 16, 37, 12, 17, 10, 24])
]

def test(shortest_path_function):
    map_40 = load_map('map-40.pickle')
    correct = 0
    for start, goal, answer_path in MAP_40_ANSWERS:
        path = shortest_path_function(map_40, start, goal)
>>>>>>> e0d9b27e8eb41682a5c06d70a37e2c1ef2776067
        if path == answer_path:
            correct += 1
        else:
            print("For start:", start, 
                  "Goal:     ", goal,
                  "Your path:", path,
                  "Correct:  ", answer_path)
    if correct == len(MAP_40_ANSWERS):
        print("All tests pass! Congratulations!")
    else:
        print("You passed", correct, "/", len(MAP_40_ANSWERS), "test cases")
    