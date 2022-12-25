'''
游玩：将data.json与此文件置于同一目录下，运行本文件



这是原版模块化。
开发一定要结合data.jsonc来看！！
'''
import json
import sys
import random
from typing import List, Optional, Union, Dict
import time
import os

Condition = Union[int, str]


A = ord("A")
B = ord("B")
C = ord("C")
D = ord("D")

LOVECA = 2 

R = random.randint(1, 100)

def to_int(s) -> Optional[int]:
    "字符串转整形，失败返回None而非报错。不支持负数"
    if len(s) == 0:
        return None
    for char in s:
        if not(ord("0") <= ord(char) <= ord("9")):
            return None
    return int(s)

def typeof(val):
    return type(val).__name__


class Achievements(object):
    '''
    单实例类，用于获取和追加成就。
    '''
    file = "./achievement.json"
    def __init__(self, game: "Game") -> None:
        self.data: List[dict] = game.data["achievement"]
    def add(self, id: int):
        d = self.get()
        if id in d:
            return
        d.append(id)
        print(f"达成成就{self.data[id]['name']}\n\t{self.data[id]['description']}")
        with open(self.file, "w+") as w:
            w.write(json.dumps(d))

    def get(self) -> list:
        try:
            with open(self.file, "r") as r:
                return json.loads(r.read())
        except IOError:
            with open(self.file, "w+") as w:
                w.write("[]")
            return []
    def show(self):
        l = self.get()
        for each in l:
            print(self.data[each]["name"])
            print("\t", self.data[each]["description"])


class Item(object):
    "物品"
    def __init__(self, game: "Game", id: int, amount: Optional[int]=1) -> None:
        self.game = game
        data = self.game.data["items"][id]
        self.id: int = data["id"]
        self.name: str = data["name"]
        self.description: str = data["description"]
        self.stackable: bool = data["stackable"] if "stackable" in data else False
        self.battle: bool = data["battle"] if "battle" in data else False
        if self.stackable:
            self.amount = amount
        if self.battle:
            self.use: list = data["use"]
        self.attack: Optional[int] = data["attack"] if "attack" in data else None
        self.defence: Optional[int] = data["defence"] if "defence" in data else None

    @property
    def info(self):
        "返回描述，对于可堆叠物品，额外返回数目。"
        info = self.description
        if self.stackable:
            info += f"/n你有{self.amount}个"
        return info




class Items(object):
    '''
    单实例类，提供一个“背包”。
    背包中的所有物品存储在其list属性中。
    可用items[id]返回指定id的物品（不是index）
    '''
    def __init__(self, game: "Game", ditems: Optional[List[int]] = None, dstackables: Optional[Dict[str, int]] = None) -> None:
        self.list: List[Item] = []
        self.game = game
        self.max = 10
        if not ditems or not dstackables:
            return None
        for ditem in ditems:
            self.list.append(Item(game, ditem, dstackables[str(ditem)] if ditem in dstackables else 1))
    def __getitem__(self, id: int) -> Optional[Item]:
        "items[id]返回指定id的物品（如果有）。注意不是指定索引的物品。"
        for each in self.list:
            if each.id == id:
                return each
        return None

    def append(self, item: Item):
        "向list中追加一项物品。"
        self.list.append(item)
    def add(self, item: int, amount: int):
        "用id添加一项物品。"
        it = self[item]
        if it and it.stackable:
            it.amount += amount
        else:
            self.append(Item(self.game, item, amount))
    def get_list(self) -> List[str]:
        "返回由物品名称组成的列表。"
        return [item.name for item in self.list]

    def dump(self):
        "将该实例转化为可以转为JSON的列表和字典。"
        stackables = {}
        for item in self.list:
            if item.stackable:
                stackables[item.id] = item.amount
        return [each.id for each in self.list], stackables

    def remove(self, index: int):
        "移除某位置的物品。"
        self.list.pop(index)

    def remove_item(self, item: Union[Item, int, None]):
        "移除某物品。如果提供整形，移除该id的物品。如果提供物品对象，移除该物品对象。"
        if type(item) is int:
            item = self[item]
        if type(item) is not Item:
            raise TypeError("No item")
        self.list.remove(item)

    def has(self, item: int) -> bool:
        "检查是否有某id的物品。"
        for each in self.list:
            if each.id == item:
                return True
        return False

    @property
    def battlable(self):
        "（动态属性）所有战斗可用的物品列表"
        res = []
        for i in range(len(self.list)):
            each = self.list[i]
            if each.battle:
                res.append(each)
        return res

    def use(self, item: Item, battle: Optional["Battle"] = None):
        "使用特定物品。注意：如果物品提升ATT、DEF或造成伤害需要传入战斗对象。"
        for each in item.use:
            self.game.execute(each, battle)

    def is_full(self):
        return len(self.list) >= self.max


class DictReader(object):
    "字典读取器。如果提供了不存在的键，并不会返回错误而是返回None。"
    def __init__(self, dct: dict) -> None:
        self.value = dct
    def __getitem__(self, key):
        return self.value[key] if key in self.value else None

class Enemy(object):
    "敌人"
    def __init__(self, battle: "Battle", enemy_data: DictReader) -> None:
        self.id = enemy_data["id"]
        self.battle = battle
        self.game = battle.game
        self.name = enemy_data["name"]
        self.full = enemy_data["health"]
        if self.full is None:
            raise TypeError("no full")
        self.health = self.full
        self.attack: int = enemy_data["attack"] or 0
        self.defence: int = enemy_data["defence"] or 0
        self.defense_rate: float = enemy_data["defenseRate"] or 0.0
        self.message: Optional[List[str]] = enemy_data["message"]
    
    @property
    def health(self):
        return self._health
    @health.setter
    def health(self, val: int):
        self._health = val
        if self._health <= 0: # 归零获胜
            self.battle.win()

class Battle(object):
    def __init__(self, game: "Game", battle_data: DictReader) -> None:
        self.game = game
        self.tutorial: bool = battle_data["tutorial"] or False # 是否为教程
        self.with_xk: bool = battle_data["withXk"] or False # 有无星空
        self.octahedron: bool = battle_data["octahedron"] or False # 几何八面体
        self.cure_magic_cost = 30
        self.cure_magic_plus = 40
        
        self.won = False
        self.after_win = battle_data["win"] # 获胜后的指令
        enemy_data = game.data["enemy"][battle_data["enemy"]]
        self.enemy = Enemy(self, DictReader(enemy_data))
        
        self.magic = 0
        self.rounds = 0

    def run(self):
        while True:
            self.round()
            if self.won:
                break

    def round(self):
        self.defense = False # 是否防御
        self.battle_magic = False # 战斗魔法是否启用
        self.round_attack = 0 # 回合中使用道具加的ATT，回合末扣除
        self.round_defence = 0 # 同理
        if self.tutorial:
            input("星空说：“让我描述详细一点吧，在魔法系统下，战斗就是我们的【魔法核心】相互接触的过程，每个人都有一个【魔法核心】，只不过大多数人都不会用罢了，我来教你怎么使用。")
            input("星空跟你详细说明了使用魔法核心的方法，你试了一下，突然你感觉世界一下就改变了！")
            input("星空：现在我们进入了战斗界面！当你听完我的这些话后，就可以加入战斗了。战斗分为准备阶段和对战阶段，在准备阶段时，你可以尝试A【物品】、B【防御】、C【魔法】、D【跳过】，不过你现在没有魔法值，没有物品，选择【防御】吧。")
            ch = self.game.choose(["防御", "跳过"])
            if ord(ch) - A: # 跳过（1）
                input("星空：你……不选防御吗？那也挺好。")
                input("星空：总之，现在是进入【战斗】的时间了！")
                input("敌人会利用A、B、C、D四种方式攻击你，每回合攻击五次，其中，D克A克B克C克D，这个木马接下来会使用AAAAA攻击，回复DDDDD来阻止它吧！")
            else: # 防御（0）
                input("星空：很好，让我们试一下战斗吧！")
                input("星空：现在是进入【战斗】的时间了！")
                input("敌人会利用A、B、C、D四种方式攻击你，每回合攻击五次，其中，D克A克B克C克D，这个木马接下来会使用AAAAA攻击，回复DDDDD来阻止它吧！因为我们点击了防御，我们无法对敌人造成伤害，但攻击可以增加魔法值！")
            if self.input5() == "DDDDD":
                input("星空：太棒了，现在我们有足够的魔法值来使用魔法了，试一下【魔法】吧，它会给你带来增益效果！剩下的你就自己摸索吧")
                self.magic = 40
            else:
                input("星空：呃……你没有听我的，看来你是想自己对战了，那我就不打扰你了！我先给你个治疗法术吧！")
                self.game.health += 240
            self.tutorial = False # 退出教程
            return
        input(f"第{self.rounds + 1}回合")
        print(f"你的HP为{self.game.health}，魔法值为{self.magic}，敌方HP为{self.enemy.health}")
        if self.enemy.id == 7: # CRD(2)
            if self.rounds == 9:
                print("CRD：“什么？！你们居然还能挺得住，看来我要动用增援了！”")
                print("第一个长矛向你袭来")
                self.game.battle(8)
                print("第二个长矛向你袭来")
                self.game.battle(8)
        elif self.enemy.id == 8: # 短矛
            if self.rounds == 6:
                self.game.achieve(2) # 论持久战
        if self.enemy.message:
            l = len(self.enemy.message)
            r = random.randint(1, l)
            if r < l:
                print(self.enemy.message[r])
        self.prepare()
        if self.won:
            return
        self.fight()
        self.game.attack -= self.round_attack
        self.game.defence -= self.round_defence
        self.rounds += 1
        
    @property
    def black(self):
        "有没有黑魔法"
        return self.game.judge(1024)

    def prepare(self):
        CH = ["物品", "防御", "魔法", "跳过"]
        ch = ord(self.game.choose(CH)) - A
        print(f"你选择了{CH[ch]}。")
        if ch == 0:
            battlable: List[Item] = self.game.items.battlable
            if not battlable: # 为空
                print("你没有可用的物品。")
                return self.prepare()
            ch = ord(self.game.choose([item.name for item in battlable])) - A
            self.game.items.use(battlable[ch], self)

        elif ch == 1:
            self.magic += 40
            self.defense = True
        elif ch == 2:
            if self.magic == 0 or (not self.octahedron and self.magic < self.cure_magic_cost):
                # 如果魔法值为0或无几何八面体且魔法值小于治疗魔法的消耗
                print("你的魔法值不够！")
                return self.prepare()
            magics = [f"治疗魔法（{self.cure_magic_cost}）", "战斗魔法（70）", f"黑暗魔法（{100 if self.black else '?'}）"]
            if self.octahedron:
                magics.append(f"几何八面体（{self.magic}）")
            def choose_magic():
                ch = ord(self.game.choose(magics)) - A
                if ch == 0: # 治疗魔法
                    if self.magic < self.cure_magic_cost:
                        print("你的魔法值不够！")
                        return choose_magic()
                    print(f"你选择了治疗魔法，HP恢复{self.cure_magic_plus}")
                    self.game.health += self.cure_magic_plus
                    self.magic -= self.cure_magic_cost
                elif ch == 1: # 战斗魔法
                    if self.magic < 70:
                        print("你的魔法值不够！")
                        return choose_magic()
                    print(f"你选择了战斗魔法，ATT提高5，持续一回合")
                    self.magic -= 70
                    self.game.health += 5
                    self.battle_magic = True
                elif ch == 2: # 黑暗魔法
                    if not self.black:
                        print("l͓̩̫̘͙͔̯͖̟̤̓͊̑̌́̂̆̚ò̥̪̭̱̰̝̒͂̄͋̿̏͆́̚c͍̲͇͚̖̬͈̪͙̳͌̉́̃k̪̥̱̝̱̑̈́̏̽͗̊̈́͂̀̍e̞͎̩̜̱̩͚̤̊͌̀̀d̠̖̞̝̙̪̟̞̐͛̈̊̀͂̄͌̓̏͌̓ͅ")
                        return choose_magic()
                    if self.magic == 100:
                        print("水晶被黑暗笼罩住了！黑暗法术增强了！")
                    else:
                        print("你的魔法值不够！")
                elif ch == 3: # 几何八面体
                    self.enemy.health -= self.magic // 2
                    print(f"你选择了几何八面体，对【{self.enemy.name}】造成{self.magic // 2}点伤害！")
                    self.magic = 0
            choose_magic()
        elif ch == 3:
            print("你选择了跳过。")

    def fight(self):
        "进行攻击"
        this_fight = Battle.input5()
        enemy_fight = ""
        harm, hurt = 0, 0 # 对敌方的伤害 对我方的伤害
        enemy_defense = random.random() < self.enemy.defense_rate # P([0, 1)的随机数小于防御率) = 防御率
        enemy_defence = self.enemy.defence if enemy_defense else 0
        same = None
        if self.enemy.id == 4 and self.rounds % 4 == 3: # 长矛特殊技能
            same = random.randint(0,3)
        for i in range(5):
            char_enemy = random.randint(0,3) if same is None else same
            char_this = ord(this_fight[i]) - A # 转成整形再运算克制关系
            enemy_fight += chr(char_enemy + A)
            if char_this == char_enemy - 1 or char_enemy == 0 and char_this == 3: # 字符转化为数字计算
                if not self.defense:
                    if self.game.attack > enemy_defence:
                        harm += self.game.attack
            elif char_enemy == char_this - 1 or char_this == 0 and char_enemy == 3:
                if self.game.defence < self.enemy.attack:
                    hurt += self.enemy.attack
        print(f"你的攻击是{this_fight}，对方的攻击是{enemy_fight}。")
        if enemy_defense:
            print(f"{self.enemy.name}选择了防御。")
        print(f"你对敌方造成{harm}伤害")
        print(f"敌方对你造成{hurt}伤害")
        self.game.health -= hurt
        self.enemy.health -= harm
        if self.with_xk:
            xk_harm = 20 - enemy_defence if enemy_defence < 20 else 0
            print(f"星空造成了${xk_harm}点伤害")
            self.enemy.health -= xk_harm
                
        if self.battle_magic: # 减掉战斗魔法的增益
            self.game.attack -= 5

    @property
    def magic(self):
        "魔法值，设定大于100将自动变为100。"
        return self._magic
    @magic.setter
    def magic(self, val):
        if val > 100:
            self._magic = 100
        else:
            self._magic = val

    @staticmethod
    def check5(s: str):
        "（静态方法）检查五个字符是否符合要求。"
        if len(s) != 5:
            return False
        for char in s:
            if ord(char) < A or ord(char) > D:
                return False
        return True
    @staticmethod
    def input5():
        "（静态方法）得到用户的攻击。"
        ipt = input("输入你的攻击")
        while not Battle.check5(ipt):
            ipt = input("你输的啥啊（")
        return ipt

    def win(self):
        "使战斗获胜"
        self.won = True
        print("您获胜了！")


class Game(object):
    def __init__(self) -> None:
        input("Re: Air Ticket Extend正在为您读取存档...")
        self.load()
        
    def read(self) -> None:
        "读取存档"
        self._armor = None
        self._weapon = None
        try:
            with open("store.json", "r", encoding="utf-8") as store_file:
                self.store = DictReader(json.load(store_file))
                self.health = self.store["health"] or 240
                self.chapter: int = self.store["chapter"] or 1
                self.cm = self.store["cm"] or 0
                if self.store["armor"]:
                    self.armor = Item(self, self.store["armor"])
                if self.store["weapon"]:
                    self.weapon = Item(self, self.store["weapon"])
                self.items: Items = Items(self, self.store["items"], self.store["stackables"])
                self.experience = self.store["experience"] or []
        except IOError: # 如果没有存档
            self.store = {}
            self.health = 240
            self.chapter = 1
            self.items = Items(self)
            self.cm = 0
            self.experience = []
        
        self.chapter_data = self.data[str(self.chapter)]
        self.achievements = Achievements(self)

    def load(self) -> None:
        "加载游戏内容剧情"
        self.attack = 15
        self.defence = 0
        with open("data.json", "r", encoding="utf-8") as data_file:
            self.data: dict = json.load(data_file)
        self.read()
        
    NORMAL = 0
    CROSS = 1
    BATTLE = 2
    def run(self):
        "跑起来"
        to = 0 if len(self.experience) == 0 else self.experience[-1] # 取消savepoint改用experience的最后一项
        while True:
            to = self.exp(to)

    def exp(self, id: int):
        self.experience.append(id)
        story: Union[dict, List[dict]] = self.chapter_data["story"][str(id)]
        if type(story) is list:
            story = self.judge_list(story)
        return self.story(story)

    def judge_list(self, arr: List[Union[Condition, str, int, dict]]):
        '''
        对一个三目表达式进行判断，条件项需要符合Game.judge的要求。
        不限于三目，只要满足 选项，条件，选项，条件……即为合法。
        判断标准是，满足选项后一个条件输出选项，无满足的条件则输出无条件选项（如果有只能有一个）
        '''
        l = len(arr)
        i = 0
        while i < l:
            if i == l - 1:
                return arr[i]
            if self.judge(arr[i + 1]):
                return arr[i]
            i += 2
        return None
        
    def judge(self, condition: Condition):
        "条件为整数或满足/[rihcaw][0-9]+/的字符串，非法返回False"
        if type(condition) is int:
            if condition in self.experience:
                return True
        elif type(condition) is str:
            p = condition[0]
            s = condition[1:]
            if p == "r": # 彩蛋随机数
                return R == int(s)
            elif p == "i": # 拥有某物品
                return self.items.has(int(s))
            elif p == "h": # 生命值为某值
                return self.health == int(s)
            elif p == "c": # CM币数量达到某值
                return self.cm >= int(s)
            elif p == "a": # 防具为
                return self.armor and self.armor.id == int(s)
            elif p == "w": # 武器为
                return self.weapon and self.weapon.id == int(s)
        return False

    def view_status(self):
        lst = self.items.get_list()
        print("HP:", self.health)
        print("ATT:", self.attack)
        print("DEF:", self.defence)
        print("防具:", self.armor.name if self.armor else "莫得")
        print("武器:", self.weapon.name if self.weapon else "木有")
        if len(lst):
            print("你有：", ", ".join(lst))
            print("你要看哪样？")
            ch = self.choose(lst + ["劳资不看"])
            if ord(ch) - A == len(lst):
                return
            item = self.items.list[ord(ch) - A]
            print(item.info)
            if item.attack is not None:
                print("要装备迈？")
                if not ord(self.choose(["我要我要", "不要！（大声"])) - A:
                    self.weapon = item
            elif item.defence is not None:
                print("要装备迈？")
                if not ord(self.choose(["我要我要", "不要！（大声"])) - A:
                    self.armor = item
        else:
            print("你啥子都没得")
        # Underdiscussion
        print("提示：按Q键可以保存")
        # endUnderdiscussion
    
    def choose(self, choices: List[str], fade_choice: Optional[List[int]] = None):
        "传入选项，返回用户选择"
        l = len(choices)
        lst = []
        for i in range(l):
            if not fade_choice or i in fade_choice:
                lst.append(chr(i + A) + choices[i]) 
        s = ",".join(lst)
        ipt = input(s)
        while len(ipt) != 1 or not (0 <= ord(ipt) - A < l):
            ipt = input(f"{('NND', '喵斯快跑', '***', '哼哼哼啊啊啊啊啊啊啊啊')[random.randint(0, 3)]}，为什么不选？不选，我就炸死你！\n{s}")
            # 喵斯快跑=MuseDash=MD
        else:
            return ipt

    def story(self, story) -> int:
        if type(story["message"]) is not list:
            raise TypeError("Story.message must be a list")
        
        # self.save()
        # 待定方式

        for msg in story["message"]:
            if type(msg) is list:
                msg = self.judge_list(msg)
            if not msg:
                continue
            if type(msg) is not str:
                raise TypeError("msg should be string")
            

            if msg[-1] == "/":
                print(msg[:-1])
            elif msg[0] == "/":
                self.execute(msg[1:])
            else:
                ipt = input(msg)
                if ipt == "Z":
                    self.view_status()
                elif ipt == "A":
                    self.achievements.show()
                # Underdiscussion
                elif ipt == "Q":
                    self.save()
                # endUnderdiscussion
        if "choice" in story:
            lst = []
            for each in story["choice"]:
                if type(each) is list:
                    each = self.judge_list(each)
                if not each:
                    continue
                lst.append(each)
            to = story["to"][ord(self.choose(lst, story["fadeChoice"] if "fadeChoice" in story else None)) - A]
        else:
            if "battle" in story:
                self.battle(story["battle"])
            to = story["to"]
        if type(to) is int:
            return to
        elif type(to) is list:
            return self.judge_list(to)

    def battle(self, id):
        Battle(self, DictReader(self.data["battle"][id])).run()

    @staticmethod
    def to_int(s: str):
        '''
        Convert string into integer
        Or get a random number in the range [start, stop] 
        '''
        if s[0] == "[" and s[-1] == "]":
            start, end = s[1:-1].split(",")
            start = to_int(start)
            end = to_int(end)
            if start and end:
                return random.randint(start, end)
            else:
                raise ValueError("Strings need to be able to be converted to integers")
        else:
            i = to_int(s)
            if i:
                return i
            else:
                raise ValueError("Strings need to be able to be converted to integers")

    def execute(self, command: str, battle: Optional[Battle] = None):
        "执行一项命令，命令的前面不应加上斜杠"
        tokens = command.split(" ")
        if tokens[0] == "sleep":
            time.sleep(float(tokens[1]))
        elif tokens[0] == "get":
            self.items.add(int(tokens[1]), int(tokens[2]) if len(tokens) == 3 else 1)
        elif tokens[0] == "remove":
            self.items.remove_item(int(tokens[1]))
        elif tokens[0] == "health":
            if tokens[1] == "+":
                self.health += Game.to_int(tokens[2])
            elif tokens[1] == "-":
                self.health -= Game.to_int(tokens[2])
        elif tokens[0] == "cm":
            if tokens[1] == "+":
                self.cm += Game.to_int(tokens[2])
            elif tokens[1] == "-":
                self.cm -= Game.to_int(tokens[2])
        elif tokens[0] == "attack":
            if not battle:
                raise TypeError("need argument battle if add/reduce att/def")
            if tokens[1] == "+":
                self.attack += Game.to_int(tokens[2])
                battle.round_attack += Game.to_int(tokens[2])
            elif tokens[1] == "-":
                self.attack -= Game.to_int(tokens[2])
        elif tokens[0] == "defence":
            if not battle:
                raise TypeError("need argument battle if add/reduce att/def")
            if tokens[1] == "+":
                self.defence += Game.to_int(tokens[2])
                battle.round_defence += Game.to_int(tokens[2])
            elif tokens[1] == "-":
                self.defence -= Game.to_int(tokens[2])
        elif tokens[0] == "achieve":
            self.achieve(int(tokens[1]))
        elif tokens[0] == "dodge":
            self.dodge(int(tokens[1]), tokens[2])
        elif tokens[0] == "bridge":
            self.bridge()
        elif tokens[0] == "shop":
            self.shop(self.data["shop"][int(tokens[1])])

    def die(self):
        if False: # 还没有超级爱心
            print('黑暗再度笼罩,使用超级爱心吗？')
            if self.choose(["使用","不使用"]) == 'A':
                input('那么，你将再次驱散黑暗')
                self.health = self.chapter_data["maxHealth"]
        else:
            print('黑暗再度笼罩,使用复活爱心吗？')
            if self.choose(["使用","不使用"]) == 'A':
                loveca = self.items[LOVECA]
                if loveca and loveca.amount <= 0:
                    input('但是，希望似乎保佑不了你')
                    input('看来，黑暗将会再度笼罩你')
                    with open("store.json",'w+') as _f:
                        pass
                    sys.exit(0)
                else:
                    input('那么，你将再次驱散黑暗')
                    self.read()
                    self.health = self.chapter_data["maxHealth"]
                    self.run() # 该方法永不返回
            else:
                input('看来，黑暗将会再度笼罩你')
                with open("store.json",'w+') as _f:
                    pass
                sys.exit(0)

    @property
    def health(self):
        "生命值溢出会自动设为上限值，生命归零自动寄"
        return self._health

    @health.setter
    def health(self, val: int) -> None:
        if val >= 240:
            self._health = 240
        elif val <= 0:
            return self.die()
        else:
            self._health = val

    def save(self):
        "保存存档"
        items, stackables = self.items.dump()
        self.store = {
            "items": items,
            "stackables": stackables,
            "health": self.health,
            "chapter": self.chapter,
            "experience": self.experience,
            "weapon": self.weapon.id if self.weapon else None,
            "armor": self.armor.id if self.armor else None,
            "cm": self.cm
        }
        with open("store.json", "w+", encoding="utf-8") as save:
            save.write(json.dumps(self.store))
        print("------保存成功！------")

    @property
    def armor(self):
        return self._armor
    @armor.setter
    def armor(self, item: Item):
        old = self._armor
        self._armor = item
        self.items.remove_item(item)
        if old:
            self.items.append(old)
            self.defence -= old.defence
        self.defence += item.defence
    
    @property
    def weapon(self):
        return self._weapon
    @weapon.setter
    def weapon(self, item: Item):
        old = self._weapon
        self._weapon = item
        self.items.remove_item(item)
        if old: 
            self.items.append(old)
            self.attack -= old.attack
        self.attack += item.attack # 零剑逻辑没加

    def dodge(self, base_enemy: int, name: str):
        "躲避"
        this_fight = Battle.input5()
        enemy_fight = ""
        hurt = 0
        for i in range(5):
            char_enemy = random.randint(0,3)
            char_this = ord(this_fight[i]) - A
            enemy_fight += chr(char_enemy + A)
            if char_enemy == char_this - 1 or char_this == 0 and char_enemy == 3:
                if self.defence < base_enemy:
                    hurt += base_enemy
        print(f"你的攻击是{this_fight}，{name}的攻击是{enemy_fight}。")
        print(f"你被扣血{hurt}")
        self.health -= hurt
    
    def bridge(self) -> None:
        "触发过桥情节"
        bridges = ("B,C", "A,C", "A,B")
        while True:
            print("选择一座桥以通过")
            choice = ord(self.choose(["", "", ""])) - A
            no_bridge = random.randint(0, 2) # 两个有桥相当于一个没桥
            if no_bridge == choice:
                print(f"翻转地板组成了桥{bridges[no_bridge]}，你没通过桥！")
            else:
                return print("你通过了桥！")
    @staticmethod
    def check2(s: str, num: int):
        "（静态方法）检查二进制字符是否符合要求。"
        if len(s) != num:
            return False
        for char in s:
            if ord(char) < 0 or ord(char) > 1:
                return False
        return True
    
    def door(self, amount: int, least: int) -> None:
        '''
        第二章升降门二进制版
        比特塔内还有字母版
        '''
        while True:
            choice = input(f'请输入你的通过方式，由{amount}个二进制字符组成，最低通过{least}/{amount}')  
            while not Game.check2(choice, least):
                print('你输的啥啊（')
            doors = ''
            count = 0
            for i in range(amount):
                door = random.choice(['0','1'])
                if door != choice[i]:
                    count += 1
                doors += door
            if count >= least:
                return print('你通过了升降门！')
            print(f'升降门的升降形式是{doors},你只通过了{count}道升降门，请重新来过')

    def shop(self, shop_data: dict) -> None:
        "商店"
        prices = {}
        item_ids = []
        items: List[str] = [] # 呈现给用户的选项
        for item in shop_data:
            price = shop_data[item]
            if type(price) is list:
                price = self.judge_list(price)
                if not price:
                    continue
            prices[int(item)] = price
            item_ids.append(int(item))
            items.append(self.data["items"][item]["name"] + f"[花费CM币{price}个]")
        leave_key = len(items) # 离开选项的列表下标
        items.append("离开")
        choice = ord(self.choose(items)) - A
        if choice == leave_key:
            return print("你离开了商店")
        if self.items.is_full():
            return print("背包空间不足，你离开了商店")
        bought = item_ids[choice]
        if self.cm < prices[bought]:
            print("你的CM币不够！")
        else:
            self.cm -= prices[bought]
            self.items.add(bought, 1)
        return self.shop(shop_data)

    def achieve(self, achievement: int):
        "达成某id成就"
        self.achievements.add(achievement)

if __name__ == "__main__":
    Game().run()

