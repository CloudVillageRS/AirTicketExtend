'''
pygame版，现已停止开发
'''
import json
import sys
import random
from typing import List, Optional
import time
import pygame

pygame.init()

A = ord("A")
B = ord("B")
C = ord("C")
D = ord("D")

R = random.randint(1, 100)

def toInt(s) -> Optional[int]:
    if len(s) == 0:
        return None
    for char in s:
        if not(ord("0") <= ord(char) <= ord("9")):
            return None
    return int(s)

class Backpack(object):
    def __init__(self, store, game: "Game"):
        self.game = game
        self.max = 10
        if "items" in store:
            self.items = store["items"]
            self.loveca = store["loveca"]
        else:
            self.items = []
            self.loveca = 0
    def add(self, item: int):
        self.items.append(item)
        if len(self.items) > self.max:
            print(f"背包已满，选择一样东西（1-{self.max + 1}）移除或使用", end="")
            ipt = input(f"输入1到{self.max + 1}之间的整数")
            while not(toInt(ipt) and 1 <= toInt(ipt) <= self.max + 1):
                ipt = input("输入错误，请重试")
            else:
                self.remove(toInt(ipt))

    def remove(self, item: int):
        self.items.remove(item)
    def show(self) -> List[str]:
        lst = list()
        for eachid in self.items:
            lst.append(self.game.data["items"][eachid])
        return lst
    def has(self, item):
        return item in self.items


class EventProcessor(object):
    def __init__(self, game: "Game"):
        self.game = game
    




class Game(object):
    def __init__(self) -> None:
        self.load()
        self.backpack = Backpack(self.store, self)
        self.experience = []
        self.processor = EventProcessor(self)
        self.screen = pygame.display.set_mode((800, 600))
        self.textarea = pygame.Surface((500, 300))
        self.clock = pygame.time.Clock()
        self.FPS = 30
        self.font = pygame.font.SysFont("方正粗黑宋简体", 20)
    def load(self) -> None:
        with open("data.json", "r", encoding="utf-8") as data_file:
            self.data: dict = json.load(data_file)
        try:
            with open("store.json", "r", encoding="utf-8") as store_file:
                self.store: dict = json.load(store_file)
                self.health: int = self.store["health"]
                self.attack: int = self.store["attack"]
                self.defence: int = self.store["defence"]
                self.progress: int = self.store["progress"]
        except IOError:
            self.store = {}
            self.health = 240
            self.attack = 15
            self.defence = 0
            self.progress = 0
    NORMAL = 0
    CROSS = 1
    BATTLE = 2
    def run(self):
        while True:
            self.loop()

    def exp(self, id: int):
        self.experience.append(id)
        story: dict = self.data["story"][str(id)]
        if "message" in story:
            self.story(story)
        elif "try_item" in story:
            if self.backpack.has(story["try_item"]):
                self.story(story["done"])
            else:
                self.story(story["fail"])

    def loop(self):
        
        pygame.display.update()
        self.clock.tick(self.FPS)

    def judge(self, condition):
        if type(condition) is int:
            if condition in self.experience:
                return True
        elif type(condition) is str:
            if condition[0] == "r":
                if R == int(condition[1:]):
                    return True
        return False

    def view_status(self):
        print("你有", self.backpack.show())
    
    def story(self, story):
        if type(story["message"]) is not list:
            raise TypeError("Story.message must be a list")
        for each in story["message"]:
            if type(each) is list:
                msg = each[0]
                condition = each[1]
                if not self.judge(condition):
                    continue
            elif type(each) is str:
                msg = each

            if msg[-1] == "/":
                print(msg[:-1])
            elif msg[0] == "/":
                self.execute(msg[1:])
            else:
                if input(msg) == "Z":
                    self.view_status()
        if "get_item" in story:
            self.backpack.add(story["get_item"])
            print(self.data["items"][story["get_item"]]["name"] + "已加入您的背包！按Z可查看背包")
        if "remove_item" in story:
            self.backpack.remove(story["remove_item"])
        if "choice" in story:
            i = 0
            for each in story["choice"]:
                if type(each) is list:
                    if self.judge(each[1]):
                        print(chr(A + i) + each[0], end="")
                elif type(each) is str:
                    print(chr(A + i) + each, end="")
                else:
                    raise TypeError("choice must be list or string")
                i += 1
            ipt = input()
            while len(ipt) != 1 or not (0 <= ord(ipt) - A < i):
                ipt = input("NND，为什么不选？不选，我就炸死你！")
            else:
                self.exp(story["to"][ord(ipt) - A])
        else:
            self.exp(story["to"])

    def execute(self, execution):
        tokens = execution.split(" ")
        if tokens[0] == "sleep":
            time.sleep(float(tokens[1]))

    def print(self, text):
        pass

if __name__ == "__main__":
    Game().run()
