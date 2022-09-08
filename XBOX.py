import time
import os

joke = ["Yo mama", "is so stupied", "she got tickets to", ".", ".", "."]
counter = 0
total_joke = len(joke)
print(total_joke)
def xbox():
    global counter
    while counter < total_joke:
        print(joke[counter])
        time.sleep(.1)
        counter = counter + 1
    counter = 0
    xbox()
xbox()

print(" -------     -------     -----------       ----------     -------     ------- ")
print(" \      \   /      /     |         |      /          \    \      \   /      / ")
print("  \      \ /      /      |         |     /    ----    \    \      \ /      /  ")
print("   \             /       |        /     /    /    \    \    \             /   ")
print("    \           /        |       /      |   |      |   |     \           /    ")
print("    /           \        |       \      |   |      |   |     /           \    ")
print("   /             \       |        \     \    \    /    /    /             \   ")
print("  /      / \      \      |         |     \    ----    /    /      / \      \  ")
print(" /      /   \      \     |         |      \          /    /      /   \      \ ")
print(" -------     -------     -----------       ----------     -------     ------- ")
