#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

choice = ["a", "b", "c", "d", "e"]

print("Welcome to the shopping list app!")

shopping_list = []

choice = raw_input("Enter your choice [a|b|c|d|e]:")

def startOver():
    startOver = raw_input("Do you wish to choose another letter option? ")
    if startOver == "yes":
        print(choice)

while choice.lower() != "e":
    print("Please choose your action from the following list:")
    print("a. Add an item to the list")
    print("b. Remove an item from the list")
    print("c. Check to see if an item is on the list")
    print("d. Show all items on the list")
    print("e. exit")


    if (choice == "a"):
        addItem = raw_input("What item do you want add? ")
        shopping_list.append(addItem)
        print("item added!")
        print(shopping_list)


    if (choice == "b"):
        removeItem = raw_input("What item do you wanna remove? ")
        shopping_list.remove(removeItem)
        print("item removed")
        print(shopping_list)


    if (choice == "c"):
        checkItem = raw_input("What item do you want to check on the list? ")
        print("item checked")
        print(shopping_list)


    if (choice == "d"):
        showItem = raw_input("Show all items on the list? ")
        print("showing all items")
        print(shopping_list)


    if (choice == "e"):
        exit = raw_input("Do you want to exit?")
        print("exit")
        break

    choice = raw_input("Enter your choice [a|b|c|d|e]:")


    # Your code below! Handle the cases when the user chooses a, b, c, d, or e
