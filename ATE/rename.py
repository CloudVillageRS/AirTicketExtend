import pygame
import os

false = False
true = True
items = [
    {
        "name": "一次性钥匙",
        "description": "一把闪着银光的钥匙（无法在战斗中使用）",
        "id": 0
    },
    {
        "name": "气球",
        "description": "普通的气球（无法在战斗中使用）",
        "id": 1
    },
    {
        "name": "复活爱心",
        "description": "具有强大能量的法术，可以使你在最近的存档区域复活",
        "stackable": true,
        "id": 2
    },
    {
        "name": "友好长矛",
        "description": "普通的长矛（Att+1）",
        "attack": 1,
        "id": 3
    },
    {
        "name": "黑色短裙",
        "description": "小型短裙，散发着不详的气息（Def+1）",
        "defence": 1,
        "id": 4
    },
    {
        "name": "冰棍",
        "description": "基础食品（HP+15）",
        "use": ["health + 15"],
        "battle": true,
        "id": 5
    },
    {
        "name": "杆草",
        "description": "很脆的草状植物，有一种香草味（HP+20）",
        "use": ["health + 20"],
        "battle": true,
        "id": 6
    },
    {
        "name": "流油果",
        "description": "最为便宜的几何作物之一（HP+40 Att+5）",
        "use": ["health + 40", "attack + 5"],
        "battle": true,
        "id": 7
    },
    {
        "name": "晶体项链",
        "description": "闪光的NaCl晶体项链（Def+10）",
        "defence": 10,
        "id": 8
    },
    {
        "name": "平行匕首",
        "description": "精致的曲线让你感到欣慰又反胃（Att+6）",
        "defence": 6,
        "id": 9
    },
    {
        "name": "短矛",
        "description": "短小不发光的矛（Att+2）",
        "attack": 2,
        "id": 10
    },
    {
        "name": "翻转裙",
        "description": "由许多翻转地板组成的短裙（Def+10）",
        "defence": 10,
        "id": 11
    },
    {
        "name": "燃烧碑",
        "description": "不怎么好用的魔法打火机",
        "id": 12
    },
    {
        "name": "水晶焰",
        "description": "你看不懂这是什么，或者这只是一坨棉絮？（HP+20）",
        "use": ["health + 20"],
        "battle": true,
        "id": 13
    },
    {
        "name": "生命宝石",
        "description": "终于……一个真正的魔法用具！（持有后治疗魔法回复的HP大幅提升）",
        "id": 14
    },
    {
        "name": "花色汉堡",
        "description": "由各种不同花色的扑克拼凑在一起的汉堡（HP+50）",
        "use": ["health + 50"],
        "battle": true,
        "id": 15
    },
    {
        "name": "魔法炸药",
        "description": "外形与大型铅锤无异（一次性使用，造成100ATT伤害，自己HP-30）",
        "use": ["harm 100", "health - 30"],
        "battle": true,
        "id": 16
    },
    {
        "name": "方块糖果",
        "description": "尖锐的软糖（HP+40）",
        "use": ["health + 40"],
        "battle": true,
        "id": 17
    },
    {
        "name": "坚硬冰棍",
        "description": "你把你的手接近冰棍，你感觉寒冬提前降临了。（一次性使用，造成100伤害）",
        "use": ["harm 100"],
        "battle": true,
        "id": 18
    },
    {
        "name": "红桃蛋糕",
        "description": "红桃果酱发出了某种著名品牌香水的气味（HP+100）",
        "battle": true,
        "id": 19
    },
    {
        "name": "J型剑",
        "description": "其实它不是用来砍人的，是用来锤人的（ATT+20）",
        "attack": 20,
        "id": 20
    },
    {
        "name": "水晶联结裙",
        "description": "肮脏的短裙，上面的灰尘无法掸除（Def+20）",
        "defence": 20,
        "id": 21
    },
    {
        "name": "透明蝴蝶结",
        "description": "水晶打造的蝴蝶结，造价极高（Def+35）",
        "defence": 20,
        "id": 22
    },
    {
        "name": "混乱护盾",
        "description": "散发出奇异光芒的一组扑克牌，每张牌的花色与数字在不断跳动着（Def+30，且装备后每局对战的每回合可以额外随机回复3-20HP）",
        "defence": 30,
        "id": 23
    },
    {
        "name": "零剑",
        "description": "看起来像一根长棍（ATT+5-50，现实时间每5秒变化一次）",
        "id": 24
    },
    {
        "name": "混沌匕首",
        "description": "看起来与普通的匕首没什么不同，但上面有很多锈斑（ATT+35）",
        "id": 25
    },
    {
        "name": "CRD硬糖",
        "description": "长矛形的蓝色薄荷味硬质糖果，并不是很甜（HP+14）（ATT+5）（Def+7）",
        "use": ["health + 14", "attack + 5", "defence + 7"],
        "battle": true,
        "id": 26
    },
    {
        "name": "占位卡",
        "description": "绑定诅咒 I",
        "throwable": false,
        "id": 27
    },
    {
        "name": "监狱钥匙",
        "description": "充满锈迹的钥匙",
        "throwable": false,
        "id": 28
    },
    {
        "name": "录像带",
        "description": "星空给的录像带，记录了熟悉又陌生的画面。",
        "id": 29
    },
    {
        "name": "黑暗之剑",
        "description": "从石台中拔出的剑",
        "id": 30
    }
]

def isint(s):
    r = True
    for each in s:
        if each not in {"1","2","3","4","5","6","7","8","9","0"}:
            r = False
            break
    return r

itemd = {}

for each in items:
    itemd[each["name"]] = each["id"]

def main():
    pygame.init()
    images = []
    for each in os.listdir(".\images"):
        if each[-4:] == ".png" and not isint(each[:-4]):
            images.append(each)

    window = pygame.display.set_mode((600,1000))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("方正粗黑宋简体", 20)
    text = ""
    index = 0
    while True:
        window.fill((127,127,127))
        window.blit(pygame.image.load(".\\images\\" + images[index]), (0,0))
        for each in items:
            window.blit(font.render(each["name"], True, (255,255,255)), (100, 200 + each["id"] * 20))
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[1] > 200:
                    os.rename("./images/" + images[index], "./images/" + str((event.pos[1]-200) // 20))
                    index += 1
        
        clock.tick(24)
        pygame.display.update()


if __name__ == "__main__":
    for each in os.listdir("./images/"):
        if isint(each): os.rename("./images/" + each, "./images/" + each + ".png")
