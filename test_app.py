from app import random_fruit


def test_random_fruit():
    test_fruit = random_fruit()[0]
    fruits = ["apple", "cherry", "orange"]
    assert test_fruit in fruits

def test_one_fruit():
    assert len(random_fruit())==1



