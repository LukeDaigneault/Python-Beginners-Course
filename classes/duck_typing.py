from abc import ABC, abstractmethod


class TextBox:
    def draw(self):
        print("TextBox")


class DropDownList:
    def draw(self):
        print("DropDownList")

# duck typing Abstract class not needed. But its good practise to have it.


def draw(controls):
    for control in controls:
        control.draw()
