#! /usr/bin/python3
import os

os.environ["dog"] = "man's best friend"
os.environ["favorite_color"] = "blue"
os.environ["best_cuisine"] = "italian"

dog = input("what is a dog")
favorite_color = input("what's your favorite color?")
best_cuisine = input("what's your favorite cuisine?")


print(dog)
print(favorite_color)
print(best_cuisine)
