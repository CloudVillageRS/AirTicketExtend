#没毛线用但看起来很高大上的注释
#程序设计:有名,棉花糖,哈哈镜
#文案:end
#绘图:噩梦
#赞助方:part-time job
import random
import time as t
import os, sys
import json
#无需存档(其实应该也需要)
fun = random.randint(1,100) 
magic_core = 0 #为塞恩思战给的特别待遇
#需要存档
check = 0
item = []
fight_item = []
health = 240
att = 15
Def = 0
magic = 0
secretD = 0
love = 0
CM = 1000
armor = ''
weapon = ''
remove = ''
black = 0
eight = 0
HE = 1
health_plus = 40
health_point = 30
respawned = 0
savepoint = 0
chapter = 1
shops = []
E_cotton = 0
tower = 0
blood_stone = 0
o_up = 0
blood_block = 0
L_block = 0
UP_plus = 0
H_cube = 0
cosh_A = 0
shop_talk = 0
super_love = 0
M_up = 0
S_up = 0
hide = [0,0]

variables = [[],[],240,15,0,0,0,0,0,'','','',0,0,1,40,30,0,0,1,[],0,0,0,0,0,0,0,0,0,0,0,0]

#存档之前的准备（抄hs的
folder = os.path.expanduser("~/Desktop/AirTicketExtend")
file_name = "./ate_save.json"
"""
fileexist = os.path.exists(file_name)
folderexist = os.path.exists(folder)
if folderexist == False:
    os.mkdir(folder)
if fileexist == False:
    f = open(folder + '/ate_save' + '.txt', 'w')
    f.close()
"""
fileexist = os.path.exists(file_name)
if fileexist == False:
    f = open(file_name, 'w')
    f.close()

#进行一个档的读
def read_data():
    global item, fight_item, health, att, Def, magic, secretD, love, CM, armor, weapon, black, remove, eight, HE, health_plus, health_point, \
           E_cotton, tower, blood_stone, o_up, savepoint, chapter, shops,E_cotton,tower,blood_stone,o_up,blood_block,L_block,UP_plus,H_cube,cosh_A,shop_talk,shop_number
    with open(file_name, 'r') as file_object:
        text = file_object.read()
        if not text:
            return
        data = json.loads(text)
        item = data['item']
        fight_item = data['fight_item']
        health = data['health']
        att = data['att']
        Def = data['Def']
        magic = data['magic']
        secretD = data['secretD']
        love = data['love']
        CM = data['CM']
        armor = data['armor']
        weapon = data['weapon']
        remove = data['remove']
        black = data['black']
        eight = data['eight']
        HE = data['HE']
        health_plus = data['health_plus']
        health_point = data['health_point']
        savepoint = data['savepoint']
        chapter = data['chapter']
        shops = data['shops']
        E_cotton = data['E_cotton']
        tower = data['tower']
        blood_stone = data['blood_stone']
        o_up = data['o_up']
        blood_block = data['blood_block']
        L_block = data['L_block']
        UP_plus = data['UP_plus']
        H_cube = data['H_cube']
        cosh_A = data['cosh_A']
        shop_talk = data['shop_talk']
        super_love = data['super_love']
        M_up = data['M_up']
        S_up = data['S_up']
        hide = data['hide']
def save_data():
    global item, fight_item, health, att, Def, magic, secretD, love, CM, armor, weapon, black, remove, eight, HE, health_plus, health_point, E_cotton, tower, blood_stone, o_up, \
savepoint, chapter, shops,E_cotton,tower,blood_stone,o_up,blood_block,L_block,UP_plus,H_cube,cosh_A,shop_talk,shop_number
    #继续抄（
    with open(file_name,'w') as file_object:
        #自定义rec函数（记录），这样就不用每次都写换行符了（虽然没什么用）
        data = {}
        data['item'] = item
        data['fight_item'] = fight_item
        data['health'] = health
        data['att'] = att
        data['Def'] = Def
        data['magic'] = magic
        data['secretD'] = secretD
        data['love'] = love
        data['CM'] = CM
        data['armor'] = armor
        data['weapon'] = weapon
        data['remove'] = remove
        data['black'] = black
        data['eight'] = eight
        data['HE'] = HE
        data['health_plus'] = health_plus
        data['health_point'] = health_point
        data['savepoint'] = savepoint
        data['chapter'] = chapter
        data['shops'] = shops
        data['E_cotton'] = E_cotton
        data['tower'] = tower
        data['blood_stone'] = blood_stone
        data['o_up'] = o_up
        data['blood_block'] = blood_block
        data['L_block'] = L_block
        data['UP_plus'] = UP_plus
        data['H_cube'] = H_cube
        data['cosh_A'] = cosh_A
        data['shop_talk'] = shop_talk
        data['super_love'] = super_love
        data['M_up'] = M_up
        data['S_up'] = S_up
        data['hide'] = hide
        file_object.write(json.dumps(data))

read_data()
def item_find():
    global choose
    global item_att
    global hucker
    global E_cotton
    global check
    global item_choose
    global item
    global fight_item
    global respawned
    global health
    global boom_snake
    global H_icecream
    global hide
    item_choose = 1
    if check == '冰棍':
        choose = input('你使用了冰棍!你的HP增加了15点!')
        health += 15
    if check == '杆草':
        choose = input('你使用了杆草!你的HP增加了20点!')
        health += 20
    if check == '流油果':
        choose = input('你使用了流油果!你的HP增加了40点,ATT临时增加了5点!')
        health += 40
        item_att += 5
    if check == '花色汉堡':
        choose = input('你使用了花色汉堡!你的HP增加了50点!')
        health += 50
    if check == '方块糖果':
        choose = input('你使用了方块糖果!你的HP增加了40点!')
        health += 40
    if check == '红桃蛋糕':
        choose = input('你使用了红桃蛋糕!你的HP增加了100点!')
        health += 100
    if check == 'CRD硬糖':
        choose = input('你使用了CRD硬糖!你的HP增加了14点,ATT临时增加了5点!')
        health += 14
        item_att += 5
    if check == '冰淇淋':
        choose = input('你使用了冰淇淋!你的HP增加了40点,DEF扣了1点!')
        health += 40
        Def -= 1
    if check == '五彩糖':
        choose = input('你使用了五彩糖!你的HP增加了20点!')
        health += 20
    if check == '能量饮料':
        input('你使用了能量饮料!你的HP增加了20点,ATT临时增加了5点!')
        health += 20
        item_att += 5
    if check == '冰冻面包':
        health += 50
        choose = input('你使用了冰冻面包!你的HP增加了50点,本回合敌人无法对你造成伤害!')
        hide[1] = 100
    if check == '电路板寿司':
        health += 50
        choose = input('你使用了电路板寿司!你的HP增加了50点,ATT临时增加了20点!')
        item_att += 20
    if check == 'H-饼干':
        plus = random.randint(4,300)
        input(f'你使用了H-饼干!你的HP增加了{plus}点!')
        health += plus
    if check == 'Tetris彩糖':
        input('你吃下了Tetris彩糖！你的HP增加了10点，你的闪避率暂时提高了50%！')
        health += 10
        hide[1] = 50
    if check == '黑客三周年限定蛋糕':
        input('简单模式开启!你的血量增加了250点,本次战斗ATT增加10点,DEF增加30点!')
        hucker = 1
        health += 250
    if check == '核淇淋':
        input('你使用了核淇淋!你的HP提高到了最大，但之后三回合每回合扣除20点血量!')
        health = 300
        H_icecream = 3
    if check == '电子爆球':
        input('你使用了电子爆球！两只小电子蛇跑了出来协助战斗！')
        boom_snake = 3
    if check == '黑鸡尾酒':
        input('你喝下了黑鸡尾酒！你的血量增加了70点，本回合攻击力提高了15点！')
        item_att += 15
        health += 70
    if check == '电棉':
        E_cotton -= 1
        choose = input('你吞下了一大坨...电子蛇的排泄物，你的HP减少了1点！')
        health -= 1
        dead_interface()
        if respawned == 1:
            respawned = 0
    if check == 'COSH血包':
        plus = fight_item.count('COSH血包')*5
        if plus >= 150:
            plus = 150
        choose = input(f'你使用了所有COSH血包,你的HP增加了{plus}点!')
        health += plus
        for i in range(fight_item.count('COSH血包')-1):
            item.remove('COSH血包')
            fight_item.remove('COSH血包')
    if check in fight_item and check in item:
        item.remove(check)
        fight_item.remove(check)
if chapter == 2:
    def bit_magic(x):
        global health_point,health,health_plus,miaomiao,coat,M_up,S_up,magic_choose,att_choose,SO,NC,magic_core,chooseb,blood_block,magic_point
        if S_up == 1:
            SO = '高科技'
        else:
            SO = '暗蓝'
        if M_up == 1:
            NC = '万能'
        else:
            NC = '猫叫'
        if x == 'normal':
            if blood_block == 0:
                choose = input(f'A：治疗魔法（{health_point}）B：战斗魔法（70）C：黑暗魔法（？）D：{SO}卫衣（30-50）E：{NC}芯片（40）')
                while choose not in {'A','B','C','D','E'}:
                    print('请做出你的选择')
                    choose = input(f'A：治疗魔法（{health_point}）B：战斗魔法（70）C：黑暗魔法（？）D：{SO}卫衣（30-50）E：{NC}芯片（40）')
            elif blood_block > 0:
                choose = input(f'A：治疗魔法（0）B：战斗魔法（0）C：黑暗魔法（？）D：{SO}卫衣（0）E：{NC}芯片（0）')
                while choose not in {'A','B','C','D','E'}:
                    print('请做出你的选择')
                    choose = input(f'A：治疗魔法（0）B：战斗魔法（0）C：黑暗魔法（？）D：{SO}卫衣（0）E：{NC}芯片（0）')
        else:
            if blood_block == 0:
                choose = input(f'A：治疗魔法（{health_point}）B：战斗魔法（70）C：黑暗魔法（？）D：{SO}卫衣（30-50）E：{NC}芯片（40）F：逃脱（30）')
                while choose not in {'A','B','C','D','E','F'}:
                    print('请做出你的选择')
                    choose = input(f'A：治疗魔法（{health_point}）B：战斗魔法（70）C：黑暗魔法（？）D：{SO}卫衣（30-50）E：{NC}芯片（40）F：逃脱（30）')
            elif blood_block > 0:
                choose = input(f'A：治疗魔法（0）B：战斗魔法（0）C：黑暗魔法（？）D：{SO}卫衣（0）E：{NC}芯片（0）F：逃脱（0）')
                while choose not in {'A','B','C','D','E','F'}:
                    print('请做出你的选择')
                    choose = input(f'A：治疗魔法（0）B：战斗魔法（0）C：黑暗魔法（？）D：{SO}卫衣（0）E：{NC}芯片（0）F：逃脱（0）')
        magic_use = 0
        if choose == 'A':
            if magic_point < health_point and blood_block <= 0:
                input('你的魔法值不够!')
                magic_choose = 0
            else:
                input(f'你使用了治疗法术!你的血量回复了{health_plus}点!')
                health += health_plus
                magic_use = health_point
                magic_choose = 1
                magic_point -= health_point
                magic_core = 1
            if health > 300:
                health = 300
                magic_choose = 1
        elif choose == 'B':
            if magic_point < 70 and blood_block <= 0:
                input('你的魔法值不够!')
                magic_choose = 0
            else:
                input('你使用了战斗法术!你的攻击提高了5点,持续一回合!')
                att_choose = 1
                magic_use = 70
                magic_choose = 1
                magic_point -= 70
        elif choose == 'C':
            input('l͓̩̫̘͙͔̯͖̟̤̓͊̑̌́̂̆̚ò̥̪̭̱̰̝̒͂̄͋̿̏͆́̚c͍̲͇͚̖̬͈̪͙̳͌̉́̃k̪̥̱̝̱̑̈́̏̽͗̊̈́͂̀̍e̞͎̩̜̱̩͚̤̊͌̀̀d̠̖̞̝̙̪̟̞̐͛̈̊̀͂̄͌̓̏͌̓ͅ')
            magic_choose = 0
        elif choose == 'D':
            if magic_point < 50 and blood_block <= 0:
                input('你的魔法值不够!')
            else:
                coat_B = random.randint(30,50)
                magic_point -= coat_B
                magic_use = coat_B
                magic_choose = 1
                if S_up == 0:
                    coat = 1
                    input('你使用了暗蓝卫衣!你的闪避率提高了10％,持续一回合!')
                else:
                    input('你使用了高科技卫衣！卫衣创造了一个力场盾，你的周围闪起了蓝色的光芒！')
                    zero_H = 100
        elif choose == 'E':
            if magic_point < 40 and blood_block <= 0:
                choose = input('你的魔法值不够!')
                magic_choose = 0
            else:
                magic_use = 40
                magic_choose = 1
                magic_point -= 40
                if M_up == 0:
                    miaomiao = 1
                    input('你使用了猫叫芯片!敌人发出了喵喵叫的声音')
                    if random.randint(1,5) == 3:
                        print('喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵（')
                elif M_up == 1:
                    print('你使用了万能芯片！请选择它的效果')
                    choose= input('A：使对方本回合ATT变为原来的五分之一,B：使对方本回合受到伤害增加,C：使对方本回合只能打出相同的字母')
                    while choose not in {'A','B','C'}:
                        choose = input('A：使对方本回合ATT变为原来的五分之一,B：使对方本回合受到伤害增加,C：使对方本回合只能打出相同的字母')
                    if choose == 'A':
                        miaomiao = 2
                    elif choose == 'B':
                        miaomiao = 3
                    elif choose == 'C':
                        miaomiao = 4
        elif choose == 'F':
            if magic_point < 30 and blood_block == 0:
                input('你的魔法值不够！')
                magic_choose = 0
            else:
                magic_use = 30
                magic_choose = 1
                magic_point -= 30
                chooseb = 'C'
                input('你尝试挣脱麻醉机械臂的捕捉！')
        choose = 0
        if blood_block > 0:
            blood_block -= 1
            magic_point += magic_use
            view_status()
            magic_use = 0
def laser(Def):
    #新函数，用于激光枪类型武器
    global magic_point,item,weapon,hurt,health,magic_use
    if '电磁激光枪' in weapon and magic_point >= 10:
        hurt += 35
        magic_point -= 10
    if '毁灭激光枪' in weapon and magic_point >= 20:
        hurt += (50 + Def)
        magic_point -= 20
    if '恐惧激光枪' in weapon and magic_point >= 20:
        magic_point -= 15
        hurt += 40
        if random.randint(1,4) == 1:
            health += random.randint(9,14)
def view_status():
    global choose, health, att, Def, CM, weapon, armor, remove, o_up, E_cotton, blood_stone, health_plus, health_point,love,L_block,UP_plus,blood_block,H_cube,shop_number,super_love,hide
    if CM > 33333 and chapter == 2:
        CM = 33333
    if E_cotton > 100:
        E_cotton = 100
    if o_up > 20:
        o_up = 20
    if love > 0 and '复活爱心' not in item:
        item.append('复活爱心')
    if love == 0 and '复活爱心' in item:
        item.remove('复活爱心')
    if E_cotton > 0 and '电棉' not in item:
        item.append('电棉')
        fight_item.append('电棉')
    if E_cotton == 0 and '电棉' in item:
        item.remove('电棉')
        fight_item.remove('电棉')
    if blood_stone > 0 and '血石' not in item:
        item.append('血石')
    if blood_stone == 0 and '血石' in item:
        item.remove('血石')
    if blood_block > 0 and '纯净血晶体' not in item:
        item.append('纯净血晶体')
    if blood_block == 0 and '纯净血晶体' in item:
        item.remove('纯净血晶体')
    if o_up > 0 and '像素碎片' not in item:
        item.append('像素碎片')
    if o_up == 0 and ('像素碎片') in item:
        item.remove('像素碎片')
    if UP_plus > 0 and '像素板' not in item:
        item.append('像素板')
        fight_item.append('像素板')
    if UP_plus == 0 and '像素板' in item:
        item.remove('像素板')
        fight_item.remove('像素板')
    if L_block > 0 and '电方块' not in item:
        item.append('电方块')
    if L_block == 0 and '电方块' in item:
        item.remove('电方块')
    if H_cube > 0 and '能量晶体' not in item:
        item.append('能量晶体')
    if H_cube == 0 and '能量晶体' in item:
        item.remove('能量晶体')
    if super_love > 0 and '超级爱心' not in item:
        item.append('超级爱心')
    if super_love == 0 and '超级爱心' in item:
        item.remove('超级爱心')
    if '生命宝石' in item:
        health_plus = 80
        health_point = 50
    else:
        health_plus = 40
        health_point = 30
    if len(item) > 10:
        print(item)
        choose = input('请从0开始选择一个物品丢弃！')
        while (choose not in {'0','1','2','3','4','5','6','7','8','9','10'} and chapter == 1) or (choose not in {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'} and chapter == 2) or               item[int(choose)] == ['占位卡'] or item[int(choose)] == ['监狱钥匙']:
            if choose not in {'0','1','2','3','4','5','6','7','8','9','10'} and chapter == 1:
                choose = input('请选择您要丢弃的物品！')
            elif choose not in {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'} and chapter == 2:
                choose = input('请选择您要丢弃的物品！')
            else:
                choose = int(choose)
                if item[choose] == ['占位卡']:
                    print('∵这是占位卡∴你扔不掉他')
                    choose = input('请重新选择')
                if item[choose] in ['监狱钥匙','能量核心 ']:
                    print('重要物品，无法丢弃')
                    choose = input('请选择你要丢弃的物品')
        choose = int(choose)
        food = item[choose]
        if food in {'冰棍','杆草','流油果','水晶焰','花色汉堡','魔法炸药','方块糖果','坚硬冰棍','CRD硬糖','红桃蛋糕','冰淇淋','五彩糖','电路板寿司','冰冻面包','能量饮料','Tetris彩糖','H-饼干'                    ,'黑客三周年限定蛋糕','水晶焰-II','电棉','像素板'}:
            fight_item.remove(food)
        if food == '复活爱心':
            love = 0
        if food == '电棉':
            E_cotton = 0
        if food == '像素碎片':
            o_up = 0
        if food == '血石':
            blood_stone = 0
        if food == '电方块':
            L_block = 0
        if food == '血方块':
            blood_cube = 0
        if food == '能量晶体':
            H_cube = 0
        if food == '像素板':
            H_cube = 0
        if food == '超级爱心':
            super_love = 0
        item.remove(food)
    if choose == 'Z':
        if weapon != '零剑':
            print(f'您的HP为{health},ATT为{att},DEF为{Def+blood_stone},CM币为{CM}')
        else:
            print(f'您的HP为{health},ATT为?,DEF为{Def+blood_stone},CM币为{CM}')
        choose = input('按X以查看背包')
        if choose == 'X':
            print(f'{item}')
            choose = input('请从1开始选择你想查看物品的编号')
            list_number = len(item)
            choose = int(choose)
            if choose > len(item):
                print('未查找到相关物品')
            else:
                choose -= 1
                check = item[choose]
                if check == '一次性钥匙':
                    choose = input('一把闪着银光的钥匙（无法在战斗中使用）')
                if check == '气球':
                    choose = input('普通的气球（无法在战斗中使用）')
                if check == '复活爱心':
                    choose = input('具有强大能量的法术，可以使你在最近的存档区域复活')
                    choose = input(f'你现在有{love}个')
                if check == '友好长矛':
                    choose = input('普通的长矛（Att+1）')
                if check == '黑色短裙':
                    choose = input('小型短裙，散发着不详的气息（Def+1）')
                if check == '冰棍':
                    choose = input('基础食品（HP+15）')
                if check == '杆草':
                    choose = input('很脆的草状植物，有一种香草味（HP+20）')
                if check == '流油果':
                    choose = input('最为便宜的几何作物之一（HP+40 Att+5）')
                if check == '晶体项链':
                    choose = input('闪光的NaCl晶体项链（Def+10）')
                if check == '平行匕首':
                    choose = input('精致的曲线让你感到欣慰又反胃（Att+6）')
                if check == '短矛':
                    choose = input('短小不发光的矛（Att+2）')
                if check == '翻转裙':
                    choose = input('由许多翻转地板组成的短裙（Def+10）')
                if check == '燃烧碑':
                    choose = input('不怎么好用的魔法打火机（ATT+10）')
                if check == '水晶焰':
                    choose = input('你看不懂这是什么，或者这只是一坨棉絮？（HP+20）')
                if check == '生命宝石':
                    choose = input('终于……一个真正的魔法用具！（持有后治疗魔法回复的HP大幅提升）')
                if check == '花色汉堡':
                    choose = input('由各种不同花色的扑克拼凑在一起的汉堡（HP+50）')
                if check == '魔法炸药':
                    choose = input('外形与大型铅锤无异（一次性使用，造成100ATT伤害，自己HP-30）')
                if check == '方块糖果':
                    choose = input('尖锐的软糖（HP+40）')
                if check == '坚硬冰棍':
                    choose = input('你把你的手接近冰棍，你感觉寒冬提前降临了。（一次性使用，造成100伤害）')
                if check == '红桃蛋糕':
                    choose = input('红桃果酱发出了某种著名品牌香水的气味（HP+100）')
                if check == 'J型剑':
                    choose = input('其实它不是用来砍人的，是用来锤人的（ATT+20）')
                if check == '水晶联结裙':
                    choose = input('肮脏的短裙，上面的灰尘无法掸除（Def+20）')
                if check == '透明蝴蝶结':
                    choose = input('水晶打造的蝴蝶结，造价极高（Def+35）')
                if check == '混乱护盾':
                    choose = input('散发出奇异光芒的一组扑克牌，每张牌的花色与数字在不断跳动着（Def+30，且装备后每局对战的每回合可以额外随机回复3-20HP）')
                if check == '零剑':
                    choose = input('看起来像一根长棍（ATT+5-50，现实时间每5秒变化一次）')
                if check == '混沌匕首':
                    choose = input('看起来与普通的匕首没什么不同，但上面有很多锈斑（ATT+35）')
                if check == 'CRD硬糖':
                    choose = input('长矛形状的蓝色薄荷味硬质糖果，并不是很甜（HP+14）（ATT+5）（Def+7）')
                if check == '冰淇淋':
                    choose = input('普通的原味冰淇淋（HP+40，Def-1）')
                if check == '五彩糖':
                    choose = input('发出闪耀光芒的糖果（HP+20）')
                if check == '能量饮料':
                    choose = input('电机牌能量饮料。配料：煤、石油、天然气、能量法石（HP+20，一回合内ATT+5）')
                if check == '冰冻面包':
                    choose = input('看起来像电动机（HP+50，在战斗时使用，这一回合敌人无法对你造成伤害）')
                if check == '电路板寿司':
                    choose = input('两片显示屏夹集成电路，我们联合！（HP+50，一回合内ATT+20）')
                if check == '液晶裙':
                    choose = input('黑色的长裙，中间填充着某种奇怪的物质（Def+30，战斗中有2%闪避）')
                if check == '离子枪':
                    choose = input('看起来像是一座带着线圈的小型电塔（ATT+20，每次攻击有10%几率让对方ATT减半但只持续一回合）')
                if check == '电动围巾':
                    choose = input('电动仅用于除尘（Def+30，有3%几率闪避）')
                if check == 'Tetris彩糖':
                    choose = input('发着淡淡奶油味的粉红色糖果（HP+10，使用后本回合闪避率增加50%）')
                if check == '电磁激光枪':
                    choose = input('具有独特造型的手枪，你发现许多电流在枪身前流过（ATT+35）（每次攻击消耗10魔法值，若魔法不足则无法攻击）')
                if check == '神秘车票':
                    choose = input('发着紫色荧光的车票，上面有着淡淡的“H”字（无法在战斗中使用）')
                if check == 'FireFox.max（破损）':
                    choose = input('可-/以将#您｝：的HHHHPPPP：&23¥？降至^&《0')
                if check == 'H-饼干':
                    choose = input('金色的H形小饼干，散发着一股电子产品的香气（HP随机增加4-300）')
                if check == '黑客三周年限定蛋糕':
                    choose = input('黑客速通网络防御软件专属补给品，持有它可以使战斗极为轻松无聊（HP+250，本次对战ATT+10，Def+30）')
                if check == '水晶焰-II':
                    choose = input('棉絮的升级版，呈蓝色（HP+40）')
                if check == '电棉':
                    choose = input('电子蛇的排泄物，不可以吃（HP-1）')
                    choose = input(f'你现在有{E_cotton}个')
                if check == '战争宝石':
                    choose = input('利用战争宝石……战斗法术的性能将会大幅提高（战斗法术百分之5概率触发暴击，查看更多战斗数据）')
                if check == '血石':
                    choose = input('普通的红色宝石，不是艾哲红石（Def+1）')
                    choose = input(f'你现在有{blood_stone}个')
                if check == '像素碎片':
                    choose = input('非常小的残片，随着时间改变变换着光彩（不可在战斗中使用）')
                    choose = input(f'你现在有{o_up}个')
                if check == '能量晶体':
                    choose = input('发着绿光的结晶块（不可在战斗中使用）')
                if check == '电方块':
                    choose = input('非常漂亮的深蓝色方块，犹如宇宙飞船中的金属锭（不可在战斗中使用，可叠加）')
                if check == '像素板':
                    choose = input('像素拼图终于完成了（战斗中一次性使用，对所有敌人造成70ATT伤害，可叠加）')
                if check == '纯净血晶体':
                    choose = input('如史莱姆一般奇软的方块（战斗中将除黑暗法术外所有法术（包括友军的辅助法术）的魔法值降到0，使用一次后损失一个纯净血晶体，可叠加）')
                if check == '恐惧激光枪':
                    choose = input('和电磁激光枪一样，但这次流过的电流激发出红色的光芒（ATT+40，且有25%几率将攻击时造成的实际伤害的30%取整增加为我方HP，免疫普通电子蛇伤害）（每次攻击消耗15魔法值）')
                if check == '核激凌':
                    choose = input('发着灰光的冰淇淋，你认为这不是食物（HP增加到max，但之后3回合内每回合额外减少5HP）')
                if check == '能量核心':
                    choose = input('比能量晶体更璀璨夺目（不可在战斗中使用）')
                if check == 'FireFox.max':
                    choose = input('真正的纯力场（HP+1938393=rapletuca）')
                if check == 'H-Core':
                    choose = input('看起来像紫水晶，只不过……紫水晶会自己发光吗？（不可在战斗中使用）')
                if check == '电子爆球':
                    choose = input('水晶做成的小球，里面装着许多小小的电子蛇（战斗中一次性使用,并且在三回合内额外造成20的固定伤害）')
                if check == '黑鸡尾酒':
                    choose = input('充满着能量与混乱碎片的粒子风暴（战斗中使用，回复70HP，并且在本回合ATT提升15点）')
                if check == 'Complex机械长剑':
                    choose = input('非常无理，也非常无脑的重剑，你肯定不会喜欢这个（ATT+40，有10%几率暴击，暴击时ATT+50）')
                if check == '超级爱心':
                    choose = input('（可叠加，持有时在死亡界面时多出选项“使用超级爱心”，使用后原地复活，在战斗中失败后则回复到战斗开始状态）')
                if check == '水枪':
                    choose = input('毫无作用的废物道具（ATT+1）')
                if check == '能量核心 ':
                    choose = input('蓝色的发光方块（不可丢弃）')
                if check == '毁灭激光枪':
                    choose = input('适合战争使用的武器……但消耗有点大（ATT+50，无视一级防御,但每次攻击时消耗20魔法值）')
                if check == 'Complex':
                    choose = input('发着微弱光线的紫色水晶，犹如万花筒一样映衬着自身的形状。（不可在战斗中使用？）')
                if check == '虚空之刃':
                    choose = input('一把奇怪的发着黑白闪光的长剑，看起来很炫酷（ATT+35，有20%额外造成20%的百分比伤害，取整）')
                elif check == '零剑-II':
                    choose = input('更高级的神秘小刀（ATT随机加30-70）')
                if check in {'友好长矛','黑色短裙','晶体项链','平行匕首','短矛','翻转裙','燃烧碑','J型剑','水晶联结裙','透明蝴蝶结','混乱护盾','零剑','混沌匕首','液晶裙','离子枪','电磁激光枪','电动围巾','恐惧激光枪','Complex机械长剑','毁灭激光枪','虚空之刃','零剑-II'}:
                    print(f'是否装备{check}?')
                    choose = input('A.装备，B.不装备')
                    if choose == 'B':
                        check = check
                    if choose == 'A':
                        if check in {'友好长矛','平行匕首','短矛','燃烧碑','J型剑','零剑','混沌匕首','离子枪','电磁激光枪', '水枪','恐惧激光枪','Complex机械长剑','毁灭激光枪','虚空之刃','零剑-II'}:
                            remove = weapon
                        if check in {'黑色短裙','晶体项链','翻转裙','水晶联结裙','透明蝴蝶结','混乱护盾','液晶裙','电动围巾'}:
                            remove = armor
                        if check == '友好长矛':
                            if weapon != '':
                                item.append(weapon)
                            weapon = check
                            att += 1
                        if check == '黑色短裙':
                            if armor != '':
                                item.append(armor)
                            armor = check
                            Def += 1
                        if check == '晶体项链':
                            if armor != '':
                                item.append(armor)
                            armor = check
                            Def += 10
                        if check == '平行匕首':
                            if weapon != '':
                                item.append(weapon)
                            weapon = check
                            att += 6
                        if check == '短矛':
                            if weapon != '':
                                item.append(weapon)
                            weapon = check
                            att += 2
                        if check == '翻转裙':
                            if armor != '':
                                item.append(armor)
                            armor = check
                            Def += 10
                        if check == '燃烧碑':
                            if weapon != '':
                                item.append(weapon)
                            weapon = check
                            att += 10
                        if check == 'J型剑':
                            if weapon != '':
                                item.append(weapon)
                            weapon = check
                            att += 20
                        if check == '水晶联结裙':
                            if armor != '':
                                item.append(armor)
                            armor = check
                            Def += 20
                        if check == '透明蝴蝶结':
                            if armor != '':
                                item.append(armor)
                            armor = check
                            Def += 35
                        if check == '零剑':
                            if weapon != '':
                                item.append(weapon)
                            weapon = check
                        if check == '混沌匕首':
                            if weapon != '':
                                item.append(weapon)
                            weapon = check
                            att += 35
                        if check == '混乱护盾':
                            if armor != '':
                                item.append(armor)
                            armor = check
                            Def += 30 #无限增加def是吧
                        if check == '液晶裙':
                            if armor != '':
                                item.append(armor)
                            armor = check
                            Def += 30
                            hide[0] = 2
                        if check == '离子枪':
                            if weapon != '':
                                item.append(weapon)
                            weapon = check
                            att += 20
                        if check == '电磁激光枪':
                            if weapon != '':
                                item.append(weapon)
                            weapon = check
                        if check == '恐惧激光枪':
                            if weapon != '':
                                item.append(weapon)
                            weapon = check
                        if check == '毁灭激光枪':
                            if weapon != '':
                                item.append(weapon)
                            weapon = check
                        if check == '虚空之刃':
                            if weapon != '':
                                item.append(weapon)
                            weapon = check
                            att += 35
                        if check == '零剑-II':
                            if weapon != '':
                                item.append(weapon)
                            weapon = check
                        if check == '电动围巾':
                            if armor != '':
                                item.append(armor)
                            armor = check
                            Def += 30
                            hide[0] = 3
                        if check == 'Complex机械长剑':
                            if weapon != '':
                                item.append(weapon)
                            weapon = check
                            att += 40
                        if check == '水枪':
                            if weapon != '':
                                item.append(weapon)
                            weapon = check
                            att += 1
                        item.remove(check)

                        if remove == '友好长矛':
                            att -= 1
                        if remove == '黑色短裙':
                            Def -= 1
                        if remove == '晶体项链':
                            Def -= 10
                        if remove == '平行匕首':
                            att -= 6
                        if remove == '短矛':
                            att -= 2
                        if remove == '翻转裙':
                            Def -= 10
                        if remove == '燃烧碑':
                            att -= 10
                        if remove == 'J型剑':
                            att -= 20
                        if remove == '水晶联结裙':
                            Def -= 20
                        if remove == '透明蝴蝶结':
                            Def -= 35
                        if remove == '混沌匕首':
                            att -= 35
                        if remove == '混乱护盾':
                            Def -= 30
                        if remove == '液晶裙':
                            Def -= 30
                            hide[0] = 0
                        if remove == '离子枪':
                            att -= 20
                        if remove == '电动围巾':
                            Def -= 30
                            hide[0] = 0
                        if remove == 'Complex机械长剑':
                            att -= 40
                        if remove == '水枪':
                            att -= 1
                        if remove == '虚空之刃':
                            att -= 35

    elif choose == 'Y':
        choose = input(f'请从1开始按照序号选择你要去的商店：{shops}')
        choose = str(choose)
        choose = '商店' + choose
        if choose == 1 and choose in shops:
            shop = 0
            while shop == '商店1':
                choose = input('你会购买：A：五彩糖【20CMB】,B：电路板寿司【120CMB】,C：液晶裙【250CMB】,D：复活爱心【400CMB】,E：离开')
                while choose not in {'A','B','C','D','E'}:
                    choose = input('你会购买：A：五彩糖【20CMB】,B：电路板寿司【120CMB】,C：液晶裙【250CMB】,D：复活爱心【400CMB】,E：离开')
                else:
                    money = 0
                    buy = 0
                    if choose == 'A':
                        if CM < 20:
                            choose = input('你的CM币不够!')
                        else:
                            buy = '五彩糖'
                            money = 20
                    elif choose == 'B':
                        if CM < 120:
                            choose = input('你的CM币不够!')
                        else:
                            buy = '电路板寿司'
                            money = 120
                    elif choose == 'C':
                        if CM < 250:
                            choose = input('你的CM币不够!')
                        else:
                            buy = '液晶裙'
                            money = 250
                    elif choose == 'D':
                        if CM < 400:
                            choose = input('你的CM币不够!')
                        else:
                            buy = 0
                            heart += 1
                            CM -= 400
                            choose = input('你购买了复活爱心!')
                    elif choose == 'E':
                        shop = 1
                    if len(item) >= 10 and buy != 0:
                        view_status()
                    if ('液晶裙' in item or armor == '液晶裙') and buy == '液晶裙':
                        buy = 0
                        choose = input('你已经购买了这个物品了!')
                    if buy != 0:
                        item.append(buy)
                        if buy in {'五彩糖','电路板寿司'}:
                            fight_item.append(buy)
                        choose = input(f'你购买了{buy}!')
                        buy = 0
                        CM -= money
            if shop_talk == 1:
                input('你正准备离开，突然店主叫住了你：“诶，你那边是城市？是P区？！太好了我上次也去过，那里好多好玩的好吃的，你一定要试试啊！就是……我记得我在一个小巷里遇到了一个奇怪的人，呃我现在忘了，如果你能到那边的话，我会记得并提醒你的！”')
                shop_talk = 2
            if shop_talk == 3:
                input('你正准备离开，突然店主叫住了你：“诶，你现在的这条岔路口……就是我那天遇到那个奇怪的人的地方，你往右拐就可以看到他了……”')
        elif choose == '商店2' and choose in shops:
            shop = 0
            while shop == 0:
                output('请选择需要购买的物品：A：Tetris彩糖【100CMB】,B：电磁激光枪【200CMB】,C：神秘车票【400CMB】（限购一张）,D：FireFox.max（破损）【2000CMB】,E：离开')
                while choose not in {'A','B','C','D','E'}:
                    print('请做出您的选择')
                    output('你会购买：A：Tetris彩糖【100CMB】,B：电磁激光枪【200CMB】,C：神秘车票【400CMB】（限购一张）,D：FireFox.max（破损）【2000CMB】,E：离开')
                else:
                    money = 0
                    buy = 0
                    if choose == 'A':
                        if CM < 100:
                            choose = input('你的CM币不够!')
                        else:
                            buy = 'Tetris彩糖'
                            money = 100
                    if choose == 'B':
                        if CM < 200:
                            choose = input('你的CM币不够!')
                        else:
                            buy = '电磁激光枪'
                            money = 200
                    if choose == 'C':
                        if CM < 400:
                            choose = input('你的CM币不够!')
                        else:
                            buy = '神秘车票'
                            money = 400
                    if choose == 'D':
                        if CM < 2000:
                            choose = input('你的CM币不够!')
                        else:
                            buy = 'FireFox.max（破损）'
                            money = 2000
                    if choose == 'E':
                        shop = 1
                    if len(item) >= 10 and buy != 0:
                        view_status()
                    if ('电磁激光枪' in item or armor == '电磁激光枪') and buy == '电磁激光枪':
                        buy = 0
                        choose = input('你已经购买这个物品了!')
                    if 'FireFox.max（破损）' in item and buy == 'FireFox.max（破损）':
                        buy = 0
                        choose = input('你已经购买这个物品了!')
                    if buy != 0:
                        if buy in {'Tetris彩糖','FireFox.max（破损）'}:
                            fight_item.append(buy)
                        item.append(buy)
                        choose = input(f'你购买了{buy}!')
                    buy = 0
                    CM -= money
        elif choose == '商店3' and choose in shops:
            shop = 0
            while shop == 0:
                choose = input('请选择需要购买的物品：A：电棉【7CMB】,B：像素碎片【12CMB】,C：血石【244CMB】,D：能量晶体【1655CMB】,E：离开')
                while choose not in {'A','B','C','D','E'}:
                    print('请做出您的选择')
                    choose = input('请选择需要购买的物品：A：电棉【7CMB】,B：像素碎片【12CMB】,C：血石【244CMB】,D：能量晶体【1655CMB】,E：离开')
                else:
                    money = 0
                    buy = 0
                    if choose == 'A':
                        if CM < 7:
                            output('你的CM币不够!')
                        else:
                            buy = '电棉'
                            money = 7
                    if choose == 'B':
                        if CM < 12:
                            choose = input('你的CM币不够!')
                        else:
                            buy = '像素碎片'
                            money = 12
                    if choose == 'C':
                        if CM < 244:
                            choose = input('你的CM币不够!')
                        else:
                            buy = '血石'
                            money = 244
                    if choose == 'D':
                        if CM < 1655:
                            choose = input('你的CM币不够!')
                        else:
                            buy = '能量晶体'
                            money = 1655
                    if choose == 'E':
                        shop = 1
                    if E_cotton >= 100 and buy == '电棉':
                        choose = input('你装不下那么多电棉！')
                    elif o_up >= 30 and buy == '像素碎片':
                        choose = input('你装不下那么多像素碎片！')
                    elif buy != 0:
                        choose = input(f'你购买了{buy}!')
                        if buy == '电棉':
                            E_cotton += 1
                        elif buy == '像素碎片':
                            o_up += 1
                        elif buy == '血石':
                            blood_stone += 1
                        else:
                            item.append('能量晶体')
                    buy = 0
                    CM -= money
        elif choose == '商店4' and choose in shops:
            shop = 0
            while shop == 0:
                output('你会购买：A：电子爆球【277CMB】,B：黑鸡尾酒【426CMB】,C：Complex机械长剑【1170CMB】,D：超级爱心【4000CMB】,E：离开')
                while choose not in {'A','B','C','D','E'}:
                    output('你会购买：A：电子爆球【277CMB】,B：黑鸡尾酒【426CMB】,C：Complex机械长剑【1170CMB】,D：超级爱心【4000CMB】,E：离开')
                money = 0
                buy = 0
                if choose == 'A':
                    if CM < 277:
                        output('你的CM币不够!')
                    else:
                        buy = '电子爆球'
                        money = 277
                if choose == 'B':
                    if CM < 426:
                        output('你的CM币不够!')
                    else:
                        buy = '黑鸡尾酒'
                        money = 426
                if choose == 'C':
                    if CM < 1170:
                        output('你的CM币不够!')
                    else:
                        buy = 'Complex机械长剑'
                        money = 1170
                if choose == 'D':
                    if CM < 4000:
                        output('你的CM币不够!')
                    else:
                        buy = 0
                        choose = input('你购买了超级爱心!')
                        super_love += 1
                        CM -= 4000
                if len(item) >= 10 and buy != 0:
                    view_status()
                if ('Complex机械长剑' in item or weapon == 'Complex机械长剑') and buy == 'Complex机械长剑':
                    buy = 0
                    output('你已经购买了这个物品了!')
                if buy != 0:
                    item.append(buy)
                    if buy in {'电子爆球','黑鸡尾酒'}:
                        fight_item.append(buy)
                    output(f'你购买了{buy}!')
                    buy = 0
                    CM -= money
        else:
            choose = input('这可不兴买啊（')
def output(text):
    global choose
    choose = input(text)
    view_status()
#只能先写成这么啥b的if else了
#字典的话不是特别好存档所以放弃了

print('air ticket extend')
choose = input('正在为您载入存档......')
read_data()
t.sleep(1.0)
#既然没用上的话fight_random就删了
#删的好（
while True:
    if chapter == 2:
        def car_fight():
            global CM,item,fight_item,weapon,armor,att,Def,blood_stone,go_B
            choose = input('模拟对战开始！模拟对象[玩具车]')
            health_F = 300
            item_att = 0
            t.sleep(0.5)
            car = 170
            hucker = 0
            magic_point = 0
            check = 0
            win = 0
            a,b,c,d,e = '','','','',''
            while win == 0:
                magic_choose = 0
                att_choose = 0
                item_choose = 0
                while magic_choose == 0 and item_choose == 0:
                    chooseb = 'A'
                    print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health_F},玩具车血量为{car}')
                    choose = input('A,物品B,防御C,魔法D,跳过')
                    while choose not in {'A','B','C','D'}:
                        print('请做出你的选择')
                        choose = input('A,物品B,防御C,魔法D,跳过')
                    if choose == 'A':
                        choose = input(f'你现在可使用的物品有{fight_item},请从1开始输入序号以选择使用的物品')
                        if choose not in {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'}:
                            choose = input('物品序号输入错误!')
                        else:
                            choose = int(choose)
                            if choose > len(fight_item):
                                choose = input('物品序号输入错误!')
                            else:
                                choose -= 1
                                check = fight_item[choose]
                                if check == '冰棍':
                                    choose = input('你使用了冰棍!你的HP增加了15点!')
                                    health_F += 15
                                if check == '杆草':
                                    choose = input('你使用了杆草!你的HP增加了20点!')
                                    health_F += 20
                                if check == '流油果':
                                    choose = input('你使用了流油果!你的HP增加了40点,ATT临时增加了5点!')
                                    health_F += 40
                                    item_att += 5
                                if check == '花色汉堡':
                                    choose = input('你使用了花色汉堡!你的HP增加了50点!')
                                    health_F += 50
                                if check == '魔法炸药':
                                    choose = input('你对对方造成了100点伤害!但你也不小心受到了30点伤害')
                                    health_F -= 30
                                    car -= 100
                                    dead_interface()
                                    if respawned == 1:
                                        break
                                if check == '坚硬冰棍':
                                    choose = input('你使用了坚硬冰棍!玩具车的HP降低了100点!')
                                    car -= 100
                                if check == '方块糖果':
                                    choose = input('你使用了方块糖果!你的HP增加了40点!')
                                    health_F += 40
                                if check == '红桃蛋糕':
                                    choose = input('你使用了红桃蛋糕!你的HP增加了100点!')
                                    health_F += 100
                                if check == 'CRD硬糖':
                                    choose = input('你使用了CRD硬糖!你的HP增加了14点,ATT临时增加了5点!')
                                    health_F += 14
                                    item_att += 5
                                if check == '冰淇淋':
                                    choose = input('你使用了冰淇淋!你的HP增加了40点,DEF扣了1点!')
                                    health_F += 40
                                    Def -= 1
                                if check == '五彩糖':
                                    choose = input('你使用了五彩糖!你的HP增加了20点!')
                                    health_F += 20
                                if check == '冰冻面包':
                                    health_F += 50
                                    choose = input('你使用了冰冻面包!你的HP增加了50点,本回合敌人无法对你造成伤害!')
                                if check == '电路板寿司':
                                    health_F += 50
                                    choose = input('你使用了电路板寿司!你的HP增加了50点,ATT临时增加了20点!')
                                    item_att += 20
                                if check == '能量饮料':
                                    choose = input('你使用了能量饮料!你的HP增加了20点,ATT临时增加了5点!')
                                    health_F += 20
                                    item_att += 5
                                if check == 'H-饼干':
                                    plus = random.randint(4,300)
                                    choose = input(f'你使用了H-饼干!你的HP增加了{plus}点!')
                                    health_F += plus
                                if check == '黑客三周年限定蛋糕':
                                    choose = input('简单模式开启!你的血量增加了250点,本次战斗ATT增加10点,DEF增加30点!')
                                    hucker = 1
                                    health_F += 250
                                item.remove(check)
                                fight_item.remove(check)
                                item_choose = 1
                                if health > 300:
                                    health = 300
                    if choose == 'B':
                        choose = input('你选择了防御!')
                        magic_point += 40
                        magic_choose = 1
                        if magic_point >= 100:
                            magic_point = 100
                        chooseb = 'B'
                    if choose == 'C':
                        choose = input(f'A：治疗魔法（{health_point}）B：战斗魔法（70）C：黑暗魔法（？）')
                        while choose not in {'A','B','C'}:
                            print('请做出你的选择')
                            choose = input(f'A：治疗魔法（{health_point}）B：战斗魔法（70）C：黑暗魔法（？）')
                        else:
                            if choose == 'A':
                                if magic_point < health_point:
                                    choose = input('你的魔法值不够!')
                                    magic_choose = 0
                                if magic_point >= health_point:
                                    choose = input(f'你使用了治疗法术!你的血量回复了{health_plus}点!')
                                    health_F += health_plus
                                    magic_choose = 1
                                    magic_point -= 30
                                if health_F > 300:
                                    health_F = 300
                                    magic_choose = 1
                            if choose == 'B':
                                if magic_point < 70:
                                    choose = input('你的魔法值不够!')
                                    magic_choose = 0
                                if magic_point >= 70:
                                    choose = input('你使用了战斗法术!你的攻击提高了5点,持续一回合!')
                                    att_choose = 1
                                    magic_choose = 1
                                    magic_point -= 70
                            if choose == 'C':
                                choose = input('l͓̩̫̘͙͔̯͖̟̤̓͊̑̌́̂̆̚ò̥̪̭̱̰̝̒͂̄͋̿̏͆́̚c͍̲͇͚̖̬͈̪͙̳͌̉́̃k̪̥̱̝̱̑̈́̏̽͗̊̈́͂̀̍e̞͎̩̜̱̩͚̤̊͌̀̀d̠̖̞̝̙̪̟̞̐͛̈̊̀͂̄͌̓̏͌̓ͅ')
                                magic_choose = 0
                            choose = 0
                    if choose == 'D':
                        choose = input('你跳过了你的回合')
                        magic_choose = 1
                x = random.randint(1,4)
                a = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                b = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                c = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                d = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                e = chr(ord('A') + x - 1)
                enemy_fight = a+b+c+d+e
                enemy_fighta = [a,b,c,d,e]
                zero_att = 0
                if '零剑' in weapon:
                    zero_att = random.randint(5,50)
                if '混乱护盾' in armor:
                    health_F += random.randint(3,20)
                    if health_F >= 300:
                        health_F = 300
                car_act_B = random.randint(1,4)
                if car_act_B == 1:
                    choosec = input('玩具车发射着正常的激光')
                if car_act_B == 2:
                    choosec = input('你的周围激起电光')
                if car_act_B == 3:
                    choosec = input('玩具车向你冲来')
                if car_act_B == 4:
                    choosec = input('玩具车向你展示了精妙的格斗术')
                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                hurt = 0
                hurtB = 0
                chance = 0
                wrong = 0
                while wrong == 0:
                    wrong = 1
                    if len(choose) != 5:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[0] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[1] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[2] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[3] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[4] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                else:
                    cube_act = random.randint(1,5)
                    while chance < 5:
                        f = choose.pop()
                        g = enemy_fighta.pop()
                        if chooseb != 'B':
                            if (f == 'A' and g == 'B') or (f == 'B' and g == 'C') or (f == 'C' and g == 'D') or (f == 'D' and g == 'A'):
                                hurt += att
                                chance += 1
                                if att_choose == 1:
                                    hurt += 5
                                if cube_act > 3:
                                    hurt -= 10
                                hurt += item_att
                                hurt += zero_att
                                if hucker == 1:
                                    hurt += 10
                                if weapon == '电磁激光枪' and magic_point >=10:
                                    hurt += 35
                                    magic_point -= 10
                                if hurt <= 0:
                                    hurt = 0
                        if (f == 'D' and g == 'C') or (f == 'C' and g == 'B') or (f == 'B' and g == 'A') or (f == 'A' and g == 'D'):
                            hurtB += 25
                            if chooseb == 'B':
                                hurtB -= Def
                                if hucker == 1:
                                    hurtB -= 30
                            if hurtB <= 0:
                                hurtB = 0
                            chance += 1
                        else:
                            chance += 1
                    car -= hurt
                    if hide[0] + hide[1] > random.randint(1,100):
                        hurtB = 0
                    hide[1] = 0
                    health_F -= hurtB
                    item_att = 0
                    choose = input(f'玩具车的攻击是{enemy_fight}')
                    if cube_act > 3 :
                        choose = input('玩具车使用了防御!')
                    if chooseb != 'B':
                        choose = input(f'你对敌方造成了{hurt}点伤害!')
                        hurt = 0
                    if chooseb == 'B':
                        choose = input('因为你选择了防御,所以伤害不计入')
                    choose = input(f'你被敌人扣除了{hurtB}点血')
                    dead_interface()
                    if respawned == 1:
                        break
                    hurtB = 0
                    att_choose = 0
                if health_F <= 0:
                    choose = input('显示屏上出现字幕：“很遗憾，你输掉了对战！再试一次吗？”A：是（进入选择界面）,B：否（离开）')
                    while choose not in {'A','B'}:
                        choose = input('A：是（进入选择界面）,B：否（离开）')
                    if choose == 'B':
                        go_B = 1
                    win = 1
                    hucker = 0
                elif car <= 0:
                    choose = input('模拟结束！')
                    CM += 50
                    choose = input(f'你获得了50个CM币')
                    win = 1
                    hucker = 0
        def fly_fight():
            global CM,item,fight_item,weapon,armor,att,Def,blood_stone,go_B
            health_F = 300
            view_status()
            print('模拟对战开始！模拟对象[六芒星飞行器]')
            item_att = 0
            miaomiao = 0
            t.sleep(0.5)
            star = 200
            star_H = 100
            check = 0
            times = 0
            magic_point = 0
            win = 0
            a,b,c,d,e = '','','','',''
            while win == 0:
                magic_choose = 0
                att_choose = 0
                item_choose = 0
                while magic_choose == 0 and item_choose == 0:
                    chooseb = 'A'
                    print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health_F},六芒星飞行器血量为{star},护盾耐久度为{star_H}')
                    choose = input('A,物品B,防御C,魔法D,跳过')
                    while choose not in {'A','B','C','D'}:
                        print('请做出你的选择')
                        choose = input('A,物品B,防御C,魔法D,跳过')
                    if choose == 'A':
                        choose = input(f'你现在可使用的物品有{fight_item},请从1开始输入序号以选择使用的物品')
                        if choose not in {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'}:
                            choose = input('物品序号输入错误!')
                        else:
                            choose = int(choose)
                            if choose > len(fight_item):
                                choose = input('物品序号输入错误!')
                            else:
                                choose -= 1
                                check = fight_item[choose]
                                if check == '冰棍':
                                    choose = input('你使用了冰棍!你的HP增加了15点!')
                                    health_F += 15
                                if check == '杆草':
                                    choose = input('你使用了杆草!你的HP增加了20点!')
                                    health_F += 20
                                if check == '流油果':
                                    choose = input('你使用了流油果!你的HP增加了40点,ATT临时增加了5点!')
                                    health_F += 40
                                    item_att += 5
                                if check == '花色汉堡':
                                    choose = input('你使用了花色汉堡!你的HP增加了50点!')
                                    health_F += 50
                                if check == '魔法炸药':
                                    choose = input('你对对方造成了100点伤害!但你也不小心受到了30点伤害')
                                    health_F -= 30
                                    car -= 100
                                    dead_interface()
                                    if respawned == 1:
                                        break
                                if check == '坚硬冰棍':
                                    choose = input('你使用了坚硬冰棍!玩具车的HP降低了100点!')
                                    car -= 100
                                if check == '方块糖果':
                                    choose = input('你使用了方块糖果!你的HP增加了40点!')
                                    health_F += 40
                                if check == '红桃蛋糕':
                                    choose = input('你使用了红桃蛋糕!你的HP增加了100点!')
                                    health_F += 100
                                if check == 'CRD硬糖':
                                    choose = input('你使用了CRD硬糖!你的HP增加了14点,ATT临时增加了5点!')
                                    health_F += 14
                                    item_att += 5
                                if check == '冰淇淋':
                                    choose = input('你使用了冰淇淋!你的HP增加了40点,DEF扣了1点!')
                                    health_F += 40
                                    Def -= 1
                                if check == '五彩糖':
                                    choose = input('你使用了五彩糖!你的HP增加了20点!')
                                    health_F += 20
                                if check == '能量饮料':
                                    choose = input('你使用了能量饮料!你的HP增加了20点,ATT临时增加了5点!')
                                    health_F += 20
                                    item_att += 5
                                if check == '冰冻面包':
                                    health_F += 50
                                    choose = input('你使用了冰冻面包!你的HP增加了50点,本回合敌人无法对你造成伤害!')
                                if check == '电路板寿司':
                                    health_F += 50
                                    choose = input('你使用了电路板寿司!你的HP增加了50点,ATT临时增加了20点!')
                                    item_att += 20
                                if check == 'H-饼干':
                                    plus = random.randint(4,300)
                                    choose = input(f'你使用了H-饼干!你的HP增加了{plus}点!')
                                    health_F += plus
                                if check == '黑客三周年限定蛋糕':
                                    choose = input('简单模式开启!你的血量增加了250点,本次战斗ATT增加10点,DEF增加30点!')
                                    hucker = 1
                                    health_F += 250
                                item.remove(check)
                                fight_item.remove(check)
                                item_choose = 1
                                if health_F > 300:
                                    health_F = 300
                    if choose == 'B':
                        choose = input('你选择了防御!')
                        magic_point += 40
                        magic_choose = 1
                        if magic_point >= 100:
                            magic_point = 100
                        chooseb = 'B'
                    if choose == 'C':
                        choose = input(f'A：治疗魔法（{health_point}）B：战斗魔法（70）C：黑暗魔法（？）')
                        while choose not in {'A','B','C'}:
                            print('请做出你的选择')
                            choose = input(f'A：治疗魔法（{health_point}）B：战斗魔法（70）C：黑暗魔法（？）')
                        else:
                            if choose == 'A':
                                if magic_point < health_point:
                                    choose = input('你的魔法值不够!')
                                    magic_choose = 0
                                if magic_point >= health_point:
                                    choose = input(f'你使用了治疗法术!你的血量回复了{health_plus}点!')
                                    health_F += health_plus
                                    magic_choose = 1
                                    magic_point -= 30
                                if health_F > 300:
                                    health_F = 300
                                    magic_choose = 1
                            elif choose == 'B':
                                if magic_point < 70:
                                    choose = input('你的魔法值不够!')
                                    magic_choose = 0
                                if magic_point >= 70:
                                    choose = input('你使用了战斗法术!你的攻击提高了5点,持续一回合!')
                                    att_choose = 1
                                    magic_choose = 1
                                    magic_point -= 70
                            elif choose == 'C':
                                choose = input('l͓̩̫̘͙͔̯͖̟̤̓͊̑̌́̂̆̚ò̥̪̭̱̰̝̒͂̄͋̿̏͆́̚c͍̲͇͚̖̬͈̪͙̳͌̉́̃k̪̥̱̝̱̑̈́̏̽͗̊̈́͂̀̍e̞͎̩̜̱̩͚̤̊͌̀̀d̠̖̞̝̙̪̟̞̐͛̈̊̀͂̄͌̓̏͌̓ͅ')
                                magic_choose = 0
                    if choose == 'D':
                        choose = input('你跳过了你的回合')
                        magic_choose = 1
                x = random.randint(1,4)
                a = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                b = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                c = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                d = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                e = chr(ord('A') + x - 1)
                enemy_fight = a+b+c+d+e
                enemy_fighta = [a,b,c,d,e]
                zero_att = 0
                if '零剑' in weapon:
                    zero_att = random.randint(5,50)
                if '混乱护盾' in armor:
                    health += random.randint(3,20)
                    if health_F >= 300:
                        health_F = 300
                star_act_B = random.randint(1,5)
                if star_act_B == 1:
                    choosec = input('飞行器对你摆出炫酷的造型')
                if star_act_B == 2:
                    choosec = input('飞行器闪烁着蓝色的荧光')
                if star_act_B == 3:
                    choosec = input('飞行器试图维持秩序，但自己仍然在乱飞')
                if star_act_B == 4:
                    choosec = input('飞行器迫不及待地向你展示它的双发玩具机枪')
                if star_act_B == 5:
                    choosec = input('飞行器只是在服从命令')
                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                hurt = 0
                hurtB = 0
                chance = 0
                wrong = 0
                while wrong == 0:
                    wrong = 1
                    if len(choose) != 5:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[0] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[1] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[2] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[3] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[4] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                else:
                    star_act = random.randint(1,20)
                    while chance < 5:
                        f = choose.pop()
                        g = enemy_fighta.pop()
                        if chooseb != 'B':
                            if (f == 'A' and g == 'B') or (f == 'B' and g == 'C') or (f == 'C' and g == 'D') or (f == 'D' and g == 'A'):
                                hurt += att
                                chance += 1
                                if att_choose == 1:
                                    hurt += 5
                                if star_act > 17:
                                    hurt -= 20
                                hurt += item_att
                                hurt += zero_att
                                if hucker == 1:
                                    hurt += 10
                                if weapon == '电磁激光枪' and magic_point >=10:
                                    hurt += 35
                                    magic_point -= 10
                                if hurt <= 0:
                                    hurt = 0
                        if (f == 'D' and g == 'C') or (f == 'C' and g == 'B') or (f == 'B' and g == 'A') or (f == 'A' and g == 'D'):
                            hurtB += 25
                            if chooseb == 'B':
                                hurtB -= Def
                                if hucker == 1:
                                    hurtB -= 30
                            if hurtB <= 0:
                                hurtB = 0
                            chance += 1
                        else:
                            chance += 1
                    if check == '冰冻面包':
                        hurtB = 0
                        check = ''
                    if miaomiao == 1:
                        hurt_B /= 2
                        hurtB = int(hurtB)
                    if star_H <= 0:
                        star -= hurt
                        times -= 1
                        if times == 0:
                            choose = input('飞行器重新制造了一个护盾！')
                            star_H = 100
                    elif star_H > 0:
                        star_H -= hurt
                        if star_H <= 0:
                            times = 8
                            star_H = 0
                    if hide[0] + hide[1] > random.randint(1,100):
                        hurtB = 0
                    health_F -= hurtB
                    item_att = 0
                    choose = input(f'敌方的攻击是{enemy_fight}')
                    if star_act > 3 :
                        choose = input('六芒星使用了防御!')
                    if chooseb != 'B':
                        choose = input(f'你对敌方造成了{hurt}点伤害!')
                        hurt = 0
                    if chooseb == 'B':
                        choose = input('因为你选择了防御,所以伤害不计入')
                    if star_H <= 0 and times == 8:
                        choose = input('飞行器的护盾失效了！')
                    choose = input(f'你被敌人扣除了{hurtB}点血')
                    hide[1] = 0
                    dead_interface()
                    if respawned == 1:
                        break
                    hurtB = 0
                    att_choose = 0
                if health_F <= 0:
                    choose = input('显示屏上出现字幕：“很遗憾，你输掉了对战！再试一次吗？”A：是（进入选择界面）,B：否（离开）')
                    while choose not in {'A','B'}:
                        choose = input('A：是（进入选择界面）,B：否（离开）')
                    if choose == 'B':
                        go_B = 1
                    win = 1
                    hucker = 0
                elif star <= 0:
                    choose = input('模拟结束!')
                    CM += 100
                    choose = input(f'你获得了100个CM币')
                    win = 1
                    hucker = 0
        def arm_fight():
            global CM,item,fight_item,weapon,armor,att,Def,blood_stone,go_B
            health_F = 300
            print('模拟对战开始！模拟对象[机械臂]')
            item_att = 0
            t.sleep(0.5)
            miaomiao = 0
            clown = 240
            catch_A = 0
            catch_B = 0
            catch_C = 0
            magic_point = 0
            check = 0
            win = 0
            a,b,c,d,e = '','','','',''
            while win == 0:
                magic_choose = 0
                att_choose = 0
                item_choose = 0
                while magic_choose == 0 and item_choose == 0:
                    chooseb = 'A'
                    print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health_F},机械臂血量为{clown}')
                    choose = input('A,物品B,防御C,魔法D,跳过')
                    while choose not in {'A','B','C','D'}:
                        print('请做出你的选择')
                        choose = input('A,物品B,防御C,魔法D,跳过')
                    if choose == 'A':
                        choose = input(f'你现在可使用的物品有{fight_item},请从1开始输入序号以选择使用的物品')
                        if choose not in {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'}:
                            choose = input('物品序号输入错误!')
                        else:
                            choose = int(choose)
                            if choose > len(fight_item):
                                choose = input('物品序号输入错误!')
                            else:
                                choose -= 1
                                check = fight_item[choose]
                                if check == '冰棍':
                                    choose = input('你使用了冰棍!你的HP增加了15点!')
                                    health_F += 15
                                if check == '杆草':
                                    choose = input('你使用了杆草!你的HP增加了20点!')
                                    health_F += 20
                                if check == '流油果':
                                    choose = input('你使用了流油果!你的HP增加了40点,ATT临时增加了5点!')
                                    health_F += 40
                                    item_att += 5
                                if check == '花色汉堡':
                                    choose = input('你使用了花色汉堡!你的HP增加了50点!')
                                    health_F += 50
                                if check == '魔法炸药':
                                    choose = input('你对对方造成了100点伤害!但你也不小心受到了30点伤害')
                                    health_F -= 30
                                    car -= 100
                                    dead_interface()
                                    if respawned == 1:
                                        break
                                if check == '坚硬冰棍':
                                    choose = input('你使用了坚硬冰棍!玩具车的HP降低了100点!')
                                    car -= 100
                                if check == '方块糖果':
                                    choose = input('你使用了方块糖果!你的HP增加了40点!')
                                    health_F += 40
                                if check == '红桃蛋糕':
                                    choose = input('你使用了红桃蛋糕!你的HP增加了100点!')
                                    health_F += 100
                                if check == 'CRD硬糖':
                                    choose = input('你使用了CRD硬糖!你的HP增加了14点,ATT临时增加了5点!')
                                    health_F += 14
                                    item_att += 5
                                if check == '冰淇淋':
                                    choose = input('你使用了冰淇淋!你的HP增加了40点,DEF扣了1点!')
                                    health_F += 40
                                    Def -= 1
                                if check == '五彩糖':
                                    choose = input('你使用了五彩糖!你的HP增加了20点!')
                                    health_F += 20
                                if check == '能量饮料':
                                    choose = input('你使用了能量饮料!你的HP增加了20点,ATT临时增加了5点!')
                                    health_F += 20
                                    item_att += 5
                                if check == '冰冻面包':
                                    health_F += 50
                                    choose = input('你使用了冰冻面包!你的HP增加了50点,本回合敌人无法对你造成伤害!')
                                if check == '电路板寿司':
                                    health_F += 50
                                    choose = input('你使用了电路板寿司!你的HP增加了50点,ATT临时增加了20点!')
                                    item_att += 20
                                if check == 'H-饼干':
                                    plus = random.randint(4,300)
                                    choose = input(f'你使用了H-饼干!你的HP增加了{plus}点!')
                                    health_F += plus
                                if check == '黑客三周年限定蛋糕':
                                    choose = input('简单模式开启!你的血量增加了250点,本次战斗ATT增加10点,DEF增加30点!')
                                    hucker = 1
                                    health_F += 250
                                item.remove(check)
                                fight_item.remove(check)
                                item_choose = 1
                                if health_F > 300:
                                    health_F = 300
                    if choose == 'B':
                        choose = input('你选择了防御!')
                        magic_point += 40
                        magic_choose = 1
                        if magic_point >= 100:
                            magic_point = 100
                        chooseb = 'B'
                    if choose == 'C':
                        choose = input(f'A：治疗魔法（{health_point}）B：战斗魔法（70）C：黑暗魔法（？）D：逃脱（30）')
                        while choose not in {'A','B','C','D'}:
                            print('请做出你的选择')
                            choose = input(f'A：治疗魔法（{health_point}）B：战斗魔法（70）C：黑暗魔法（？）D：逃脱（30）')
                        else:
                            if choose == 'A':
                                if magic_point < health_point:
                                    choose = input('你的魔法值不够!')
                                    magic_choose = 0
                                if magic_point >= health_point:
                                    choose = input(f'你使用了治疗法术!你的血量回复了{health_plus}点!')
                                    health_F += health_plus
                                    magic_choose = 1
                                    magic_point -= 30
                                if health_F > 300:
                                    health_F = 300
                                    magic_choose = 1
                            if choose == 'B':
                                if magic_point < 70:
                                    choose = input('你的魔法值不够!')
                                    magic_choose = 0
                                if magic_point >= 70:
                                    choose = input('你使用了战斗法术!你的攻击提高了5点,持续一回合!')
                                    att_choose = 1
                                    magic_choose = 1
                                    magic_point -= 70
                            if choose == 'C':
                                choose = input('l͓̩̫̘͙͔̯͖̟̤̓͊̑̌́̂̆̚ò̥̪̭̱̰̝̒͂̄͋̿̏͆́̚c͍̲͇͚̖̬͈̪͙̳͌̉́̃k̪̥̱̝̱̑̈́̏̽͗̊̈́͂̀̍e̞͎̩̜̱̩͚̤̊͌̀̀d̠̖̞̝̙̪̟̞̐͛̈̊̀͂̄͌̓̏͌̓ͅ')
                                magic_choose = 0
                            if choose == 'D':
                                if magic_point < 30:
                                    choose = input('你的魔法值不够!')
                                    magic_choose = 0
                                if magic_point >= 30:
                                    choose = input('你尝试逃脱机械臂的抓捕!')
                                    magic_choose = 1
                                    magic_point -= 30
                                    chooseb = 'C'
                            choose = 0
                    if choose == 'D':
                        choose = input('你跳过了你的回合')
                        magic_choose = 1
                x = random.randint(1,4)
                a = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                b = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                c = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                d = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                e = chr(ord('A') + x - 1)
                enemy_fight = a+b+c+d+e
                enemy_fighta = [a,b,c,d,e]
                zero_att = 0
                if '零剑' in weapon:
                    zero_att = random.randint(5,50)
                if '混乱护盾' in armor:
                    health += random.randint(3,20)
                    if health_F >= 300:
                        health_F = 300
                clown_act_B = random.randint(1,3)
                if clown_act_B == 1:
                    choosec = input('机械臂张牙舞爪地向你伸来')
                if clown_act_B == 2:
                    choosec = input('机械臂展现了航天品质')
                if clown_act_B == 3:
                    choosec = input('机械臂的液压杆正缓缓伸缩')
                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                hurt = 0
                hurtB = 0
                chance = 0
                wrong = 0
                while wrong == 0:
                    wrong = 1
                    if len(choose) != 5:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[0] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[1] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[2] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[3] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[4] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                else:
                    clown_act = random.randint(1,5)
                    while chance < 5:
                        f = choose.pop()
                        g = enemy_fighta.pop()
                        if chooseb != 'B':
                            if (f == 'A' and g == 'B') or (f == 'B' and g == 'C') or (f == 'C' and g == 'D') or (f == 'D' and g == 'A'):
                                if chooseb == 'C':
                                    catch_C += 10
                                hurt += att
                                chance += 1
                                if att_choose == 1:
                                    hurt += 5
                                if clown_act > 3:
                                    hurt -= 50
                                hurt += item_att
                                if hurt <= 0:
                                    hurt = 0
                                hurt += zero_att
                                if hucker == 1:
                                    hurt += 10
                                if weapon == '电磁激光枪' and magic_point >=10:
                                    hurt += 35
                                    magic_point -= 10
                                if hurt <= 0:
                                    hurt = 0
                        if (f == 'D' and g == 'C') or (f == 'C' and g == 'B') or (f == 'B' and g == 'A') or (f == 'A' and g == 'D'):
                            hurtB += 15
                            catch_A += 10
                            if chooseb == 'C':
                                catch_A -= 10
                            if chooseb == 'B':
                                hurtB -= Def
                                if hucker == 1:
                                    hurtB -= 30
                            if hurtB <= 0:
                                hurtB = 0
                            chance += 1
                        else:
                            chance += 1
                    if hide[0] + hide[1] > random.randint(1,100):
                        hurtB = 0
                    clown -= hurt
                    health_F -= hurtB
                    item_att = 0
                    choose = input(f'敌方的攻击是{enemy_fight}')
                    if clown_act > 3 :
                        choose = input('机械臂使用了防御!')
                    if chooseb != 'B':
                        choose = input(f'你对敌方造成了{hurt}点伤害!')
                        hurt = 0
                    if chooseb == 'B':
                        choose = input('因为你选择了防御,所以伤害不计入')
                    choose = input(f'你被机械臂扣除了{hurtB}点血')
                    dead_interface()
                    if respawned == 1:
                        break
                    hurtB = 0
                    if chooseb == 'C':
                        choose = input(f'你的[{catch_C}%]逃脱了机械臂的捕捉！')
                        catch_B -= catch_C
                        if catch_B <= 0:
                            catch_B = 0
                    att_choose = 0
                    choose = input(f'机械臂捕捉了你的[{catch_A}%]!')
                    catch_B += catch_A
                    catch_A = 0
                    if catch_B >= 100:
                        choose= input('机械臂捕捉了你！你的HP减少了150！')
                        health_F -= 150
                        dead_interface()
                        choose = input('机械臂松开了。')
                        catch_B = 0
                    choose = input(f'你现在的累计捕捉度为[{catch_B}]')
                if health_F <= 0:
                    choose = input('显示屏上出现字幕：“很遗憾，你输掉了对战！再试一次吗？”A：是（进入选择界面）,B：否（离开）')
                    while choose not in {'A','B'}:
                        choose = input('A：是（进入选择界面）,B：否（离开）')
                    if choose == 'B':
                        go_B = 1
                    win = 1
                    hucker = 0
                elif clown <= 0:
                    choose = input('模拟结束!')
                    CM += 100
                    choose = input(f'你获得了100个CM币')
                    win = 1
                    hucker = 0
    def dead_interface():
        global health
        global love
        global respawned
        global super_love
        if health <= 0:
            super_q = 1
            if super_love in item:
                print('黑暗再度笼罩,使用超级爱心吗？')
                choose = input('A使用,B不使用')
                while choose not in {'A','B'}:
                    choose = input('请做出您的选择,A使用B不使用')
                if choose == 'A':
                    super_q = 0
                    chooseA = input('那么，你将再次驱散黑暗')
                    read_data()
                    if chapter == 1:
                        health = 240
                    elif chapter == 2:
                        health = 300
                    super_love -= 1
                else:
                    super_q = 1
            if super_q == 1:
                print('黑暗再度笼罩,使用复活爱心吗？')
                choose = input('A使用,B不使用')
                while choose not in {'A','B'}:
                    choose = input('请做出您的选择,A使用B不使用')
                else:
                    if choose == 'A':
                        if love <= 0:
                            chooseA = input('但是，希望似乎保佑不了你')
                            chooseA = input('看来，黑暗将会再度笼罩你')
                            with open(file_name,'w') as file_object:
                                file_object.write('you died')
                            sys.exit(0)
                        else:
                            chooseA = input('那么，你将再次驱散黑暗')
                            read_data()
                            if chapter == 1:
                                health = 240
                            elif chapter == 2:
                                health = 300
                            love -= 1
                            respawned = 1
                    else:
                        choose = input('看来，黑暗将会再度笼罩你')
                        with open(file_name,'w') as file_object:
                            file_object.write('you died')
                        sys.exit(0)
    def fight(enemy_name,HP,ATT,DEF,P,cm,magic_type,special_A = 0,enemy_number = 1,enemy_name_B = '',HP_B = 0,ATT_B = 0,DEF_B = 0,P_B = 0):
        global health,item,fight_item,att,Def,weapon,armor,CM,light_cube,chapter,M_up,S_up
        if enemy_number == 1:
            print(f'战斗开始,对战{enemy_name}')
        else:
            if enemy_name_B == enemy_name:
                print(f'战斗开始,对战{enemy_name} * 2')
            else:
                print(f'战斗开始,对战{enemy_name} + {enemy_name_B}')
        item_att = 0
        HP_B = 0
        miaomiao = 0
        coat = 0
        eight = 0
        if enemy_name == '罗尔斯':
            rules = 0
            rule_change = 0
            rule = 0
        if enemy_name == '六芒星飞行器':
            H = 100
        zero_att = 0
        t.sleep(0.5)
        magic_point = 0
        Zero_H = 0
        if chapter == 1:
            max_health = 240
        if chapter == 2:
            max_health = 300
        if enemy_number == 2 and enemy_name_B == enemy_name:
            enemy_name += 'A'
            enemy_name_B += 'B'
        att_point = 70
        att_plus = 5
        win = 0
        ATTE = 0
        a,b,c,d,e = '','','','',''
        #tetris:5,(2,3),(4,5)
        if enemy_name == 'CRD':
            eight = 1
        while win == 0:
            if enemy_name == 'CRD' and special_A > 0:
                special_A -= 1
                if special_A == 0:
                    choose = input('CRD：“什么？！你们居然还能挺得住，看来我要动用增援了！”')
                    choose = input('第一个短矛向你袭来！')
                    fight('短矛',50,5,10,10,5,'xk')
                    choose = input('第二个短矛向你袭来！')
                    fight('短矛',50,5,10,10,5,'xk')
            magic_choose = 0
            att_choose = 0
            item_choose = 0
            while magic_choose == 0 and item_choose == 0:
                chooseb = 'A'
                if enemy_name == '罗尔斯':
                    rule_change = rules
                    print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health},{enemy_name}血量为{HP},场上规则度为{rules}')
                elif enemy_name == '六芒星飞行器':
                    print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health},{enemy_name}血量为{HP},对方护盾为{H}')
                elif magic_type in {'so','bit'} and S_up == 1:
                    if enemy_number == 1:
                        print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health},护盾血量为{Zero_H},{enemy_name}血量为{HP}')
                    else:
                        print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health},护盾血量为{Zero_H},{enemy_name}血量为{HP},{enemy_name_B}血量为{HP_B}')
                else:
                    if enemy_number == 1:
                        print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health},{enemy_name}血量为{HP}')
                    else:
                        print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health},{enemy_name}血量为{HP},{enemy_name_B}血量为{HP_B}')
                choose = input('A,物品B,防御C,魔法D,跳过')
                while choose not in {'A','B','C','D'}:
                    print('请做出你的选择')
                    choose = input('A,物品B,防御C,魔法D,跳过')
                if enemy_name in {'电子蛇','电子蛇A','精英电子蛇','精英电子蛇A','飞碟','飞碟A','麻醉机械臂'} and special_A[0] == 1 and choose != 'B':
                    if enemy_name in {'电子蛇','电子蛇A','精英电子蛇','精英电子蛇A'}:
                        input('你被电子蛇的方块缠住了！请使用防御抖掉方块')
                    elif enemy_name in {'飞碟','飞碟A'}:
                        input('你还没有恢复过来！请选择防御缓解激光的伤害')
                    elif enemy_name == '麻醉机械臂':
                        input('你被机械臂麻醉了，你无法做出除了防御以外的行动')
                else:
                    if choose == 'A':
                        choose = input(f'你现在可使用的物品有{fight_item},请从1开始输入序号以选择使用的物品')
                        if choose not in {'1','2','3','4','5','6','7','8','9','10'}:
                            choose = input('物品序号输入错误!')
                        else:
                            choose = int(choose)
                            if choose > len(fight_item):
                                choose = input('物品序号输入错误!')
                            else:
                                choose -= 1
                                check = fight_item[choose]
                                item_find()
                                if check in fight_item and check in item:
                                    item.remove(check)
                                    fight_item.remove(check)
                            if health > max_health:
                                health = max_health
                            if random.randint(1,3) != 3 and enemy_name == '罗尔斯':
                                rules += 3
                    elif choose == 'B':
                        input('你选择了防御!')
                        if enemy_name in {'电子蛇','电子蛇A','精英电子蛇','精英电子蛇A'} and special_A[0] == 1:
                            print('你清理掉了身上的方块')
                            health -= 10
                        if enemy_name in {'电子蛇','电子蛇A','精英电子蛇','精英电子蛇A','飞碟','飞碟A','麻醉机械臂'} and special_A[0] == 1:
                            special_A[0] = 0
                        magic_point += 40
                        magic_choose = 1
                        if magic_point >= 100:
                            magic_point = 100
                        chooseb = 'B'
                    elif choose == 'C':
                        if magic_type == 'lorce':
                            choose = input(f'A：几何六面体（{magic_point}）B：规则防御（30）C：超级治疗（60）')
                            while choose not in {'A','B','C'}:
                                print('请做出你的选择')
                                choose = input(f'A：几何六面体（{magic_point}）B：规则防御（30）C：超级治疗（60）')
                            if choose == 'A':
                                input(f'你使用了几何八面体,你对敌方造成了{magic_point//2}点伤害!')
                                if magic_point == 0:
                                    choose = 'D'
                                lorce -= (magic_point // 2)
                                magic_choose = 1
                                magic_point = 0
                            elif choose == 'B':
                                if magic_point < 40:
                                    input('您的魔法值不够！')
                                else:
                                    if rule == 0:
                                        input('星空对你说：“罗尔斯的规则法术……好像对我们也有作用！”')
                                        rule = 1
                                    input('对方的攻击降低了！')
                                    ATTE = -10
                                    magic_choose = 1
                                    magic_point -= 30
                            elif choose == 'C':
                                if magic_point < 60:
                                    choose = input('您的魔法值不够')
                                else:
                                    input('你试着用尽全力使出治疗法术……你的血量和攻击力增加了！')
                                    health += 80
                                    if '生命水晶' in item:
                                        health += 100
                                    att_choose = 1
                                    magic_choose = 1
                                    magic_point -= 60
                                    if health > max_health:
                                        health = max_health
                            if random.randint(1,5) != 3 and enemy_name == '罗尔斯':
                                rules += 4
                        else:
                            if eight == 1:
                                eight = 0
                                input('你注意到星空抛给你了一个发着光的小物体')
                                input('星空：“接着！这是几何八面体，内部蕴含着巨大的能量”')
                                input('“你可以通过消耗自己的全部魔法值,对敌方造成自己魔法值一半的伤害,无视敌方护甲”')
                            if magic_type == 'normal':
                                input(f'A：治疗魔法（{health_point}）B：战斗魔法（{att_point}）C：黑暗魔法（？）')
                                while choose not in {'A','B','C'}:
                                    print('请做出你的选择')
                                    input(f'A：治疗魔法（{health_point}）B：战斗魔法（att_point）C：黑暗魔法（？）')
                            elif magic_type == 'xk':
                                input(f'A：治疗魔法（{health_point}）B：战斗魔法（{att_point}）C：黑暗魔法（？）,D：几何八面体（{magic_point//2}）')
                                while choose not in {'A','B','C','D'}:
                                    print('请做出你的选择')
                                    input(f'A：治疗魔法（{health_point}）B：战斗魔法（att_point）C：黑暗魔法（？）,D：几何八面体（{magic_point//2}）')
                            elif magic_type == 'nc':
                                if M_up == 1:
                                    NC = '万能'
                                else:
                                    NC = '猫叫'
                                input(f'A：治疗魔法（{health_point}）B：战斗魔法（{att_point}）C：黑暗魔法（？）,D：{NC}芯片（40）')
                                while choose not in {'A','B','C','D'}:
                                    print('请做出你的选择')
                                    input(f'A：治疗魔法（{health_point}）B：战斗魔法（att_point）C：黑暗魔法（？）,D：{NC}芯片（40）')
                            elif magic_type == 'so':
                                if M_up == 1:
                                    SO = '暗蓝'
                                else:
                                    SO = '高科技'
                                input(f'A：治疗魔法（{health_point}）B：战斗魔法（{att_point}）C：黑暗魔法（？）,D：{SO}芯片（30-50）')
                                while choose not in {'A','B','C','D'}:
                                    print('请做出你的选择')
                                    input(f'A：治疗魔法（{health_point}）B：战斗魔法（att_point）C：黑暗魔法（？）,D：{SO}芯片（30-50）')
                            if choose == 'A':
                                if magic_point < health_point:
                                    input('你的魔法值不够!')
                                    magic_choose = 0
                                if magic_point >= health_point:
                                    input(f'你使用了治疗法术!你的血量回复了{health_plus}点!')
                                    health += health_plus
                                    magic_choose = 1
                                    magic_point -= 30
                                elif health > max_health:
                                    health = max_health
                                    magic_choose = 1
                            elif choose == 'B':
                                if magic_point < 70:
                                    input('你的魔法值不够!')
                                    magic_choose = 0
                                elif magic_point >= 70:
                                    input(f'你使用了战斗法术!你的攻击提高了{att_plus}点,持续一回合!')
                                    att_choose = 1
                                    magic_choose = 1
                                    magic_point -= att_point
                            elif choose == 'C':
                                input('l͓̩̫̘͙͔̯͖̟̤̓͊̑̌́̂̆̚ò̥̪̭̱̰̝̒͂̄͋̿̏͆́̚c͍̲͇͚̖̬͈̪͙̳͌̉́̃k̪̥̱̝̱̑̈́̏̽͗̊̈́͂̀̍e̞͎̩̜̱̩͚̤̊͌̀̀d̠̖̞̝̙̪̟̞̐͛̈̊̀͂̄͌̓̏͌̓ͅ')
                                magic_choose = 0
                            elif choose == 'D' and magic_type == 'xk':
                                light_cube = 1
                                input(f'你使用了几何八面体！{enemy_name}的血量降低了{magic_point//2}点！')
                                HP -= (magic_point//2)
                                magic_point = 0
                            elif choose == 'D' and magic_type in {'nc','bit'}:
                                if magic_point < 40:
                                    choose = input('你的魔法值不够!')
                                    magic_choose = 0
                                else:
                                    magic_choose = 1
                                    magic_point -= 40
                                    if M_up == 0:
                                        miaomiao = 1
                                        input('你使用了猫叫芯片!敌人发出了喵喵叫的声音')
                                        if random.randint(1,5) == 3:
                                            print('喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵（')
                                    elif M_up == 1:
                                        print('你使用了万能芯片！请选择它的效果')
                                        choose= input('A：使对方本回合ATT变为原来的五分之一,B：使对方本回合受到伤害增加,C：使对方本回合只能打出相同的字母')
                                        while choose not in {'A','B','C'}:
                                            choose = input('A：使对方本回合ATT变为原来的五分之一,B：使对方本回合受到伤害增加,C：使对方本回合只能打出相同的字母')
                                        if choose == 'A':
                                            miaomiao = 2
                                        elif choose == 'B':
                                            miaomiao = 3
                                        elif choose == 'C':
                                            miaomiao = 4
                            elif (choose == 'D' and magic_type == 'so') or (choose == 'E' and magic_type == 'bit'):
                                if magic_point < 50:
                                    input('你的魔法值不够!')
                                else:
                                    magic_point -= random.randint(30,50)
                                    magic_choose = 1
                                    if S_up == 0:
                                        hide[1] += 10
                                        input('你使用了暗蓝卫衣!你的闪避率提高了10％,持续一回合!')
                                    else:
                                        input('你使用了高科技卫衣！卫衣创造了一个力场盾，你的周围闪起了蓝色的光芒！')
                                        Zero_H = 100
                    elif choose == 'D':
                        input('你跳过了你的回合')
                        magic_choose = 1
                        if random.randint(1,6) != 4 and enemy_name == '罗尔斯':
                            rules += 4
            if enemy_name == 'Tetris':
                if special_A[2] == 0:
                    special_A[2] = random.randint(3,5)
                    choose = input('Tetris的手上冒出了蓝色的火焰')
                    choose = input('Tetris的攻击增强了！')
                    ATTE += 10
            if armor == '混乱护盾':
                health += random.randint(3,20)
            elif enemy_name == '滚轮' and random.randint(1,4) <= 3:
                input(random.choice(['滚啊滚啊滚啊滚','滚轮用中心对称的身体掀起许多烟尘','星空正在尝试让他滚或不让他滚']))
            elif enemy_name == '四面体' and random.randint(1,4) <= 3:
                input(random.choice(['四面体的头顶上出现了一个顶点魔法球','远处似乎有微弱的长矛碰撞声','星空认为并不需要使用“几何八面体”']))
            elif enemy_name == 'CRD':
                input(random.choice(['几何八面体闪耀着淡黄色的光芒','CRD对战斗使用了一个夸张的修辞手法','你认为CRD的长矛有点像水果味硬糖',                                     '遗迹的轮廓在远处若隐若现']))
            elif enemy_name == '短矛' and random.randint(1,3) <= 2:
                input(random.choice(['短矛只是听从CRD的命令','CRD让短矛做了一个后空翻','似乎闻到了爆米花的气味，来自CRD?','你不认为这些短矛能造成什么威胁']))
            elif enemy_name == '鹿法师' and random.randint(1,4) <= 3:
                input(random.choice(['火焰的气味','鹿法师的服饰与遗迹融为了一体','如果你不够诚实，这一定会是一场艰难的战斗']))
            elif enemy_name == '骷髅':
                sc_act = random.randint(1,5)
                sc_talk = ['这两个持盾的骷髅不可开交的争吵着，声音十分地难听','一个骷髅拿起了盾,你的攻击下降了！','一个骷髅拿起了三叉戟,对方的攻击提升了！','什么语法玩意啊，老兄，你这不正常也太大了！','文艺气息传来']
                input(sc_talk[sc_act])
                if sc_act == 2:
                    ATTE = 5
            elif enemy_name == '扑克守卫':
                input(random.choice(['扑克守卫认为很快就能结束战斗','扑克守卫需要精神援助','扑克守卫发出刺耳的怪叫声','扑克守卫试图叠罗汉组成城堡，然后城堡塌了']))
            elif enemy_name == '罗尔斯':
                if rules < 72:
                    input(random.choice(['黑暗笼罩了战场','罗尔斯摇晃着他的长剑','扑克城堡被夜色覆盖','死亡的气息充斥着战场',                                          '危机感上升','罗尔斯不想快速结束战斗','星空向你晃了晃几何八面体']))
                else:
                    input(random.choice(['战争的气氛愈演愈烈','规则逐渐开始动摇','罗尔斯开始用尽全力','星空向你晃了晃几何八面体','月光映入扑克城堡']))
            elif enemy_name in {'玩具车A','玩具车B','玩具车'}:
                input(random.choice(['玩具车发射着正常的激光','你的周围激起电光','玩具车向你冲来','玩具车向你展示了精妙的格斗术']))
            elif enemy_name == '六芒星飞行器':
                input(random.choice(['飞行器对你摆出炫酷的造型','飞行器闪烁着蓝色的荧光','飞行器试图维持秩序','但自己仍然在乱飞','飞行器迫不及待地向你展示它的双发玩具机枪',\
'飞行器只是在服从命令']))
            elif enemy_name == 'Tetris':
                if special_A[0] == 6:
                    input('对战在列车上拉开帷幕')
                else:
                    input(random.choice(['Tetris看起来很严肃','Tetris召唤了一个方块，然后将它直接打碎','奶油的香味充斥着战场','城市似乎就在前方','Tetris似乎有点芯片故障'\
,'Tetris迫切地需要你们的性命','ERROR_error','经典电子游戏的气息','Firefox.max持续追踪战场','So给你使了个眼色，你没理他']))
            elif enemy_name in {'电子蛇A','电子蛇'}:
                input(random.choice(['电子蛇绕成一圈，你们不知道在玩什么花样','电子蛇发出来特有的嘶嘶声','你们闻到一股棉花味','商业化的气息充斥着街道','周围没啥人理你，看来习以为常','电子蛇希望你们能养它们','电子蛇有点想逃走','电子蛇不希望看到捕蛇圈']))
            if enemy_name == '鹿法师':
                special_A -= 1
                if special_A == 0:
                    special_A = 5
                    input('鹿法师使用了火魔法！鹿法师的ATT暂时提高了5点！')
                    ATTE = 5
            if enemy_name == '罗尔斯':
                if special_A[1] == 0:
                    special_A[0] = random.randint(1,10)
                else:
                    special_A[0] = random.randint(1,6)
                if special_A[0] <= 2 or (chooseb == 'B' and random.randint(1,2) == 1):
                    input('罗尔斯举起了重剑！罗尔斯的攻击力提高了！')
                    ATTE += 5
                if special_A[0] == 3:
                    poker = random.randint(15,35)
                    input(f'罗尔斯使用了一发扑克散弹,你受到了{poker}点伤害！')
                    health -= poker
            if HP > 0:
                x = random.randint(1,4)
                a = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                b = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                c = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                d = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                e = chr(ord('A') + x - 1)
                if enemy_name == '长矛' or miaomiao == 4:
                    b,c,d,e = a,a,a,a
                enemy_fightb = a+b+c+d+e
                enemy_fighta = [a,b,c,d,e]
                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                hurt = 0
                hurtB = 0
                chance = 0
                wrong = 0
                while wrong == 0:
                    wrong = 1
                    if len(choose) != 5:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[0] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[1] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[2] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[3] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[4] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                if '零剑' in weapon:
                    zero_att = random.randint(5,50)
                if 'Complex机械长剑' in weapon and random.randint(1,5) == 3:
                    zore_att = 10
                p_act = random.randint(1,100)
                while chance < 5:
                    f = choose.pop()
                    g = enemy_fighta.pop()
                    if chooseb != 'B':
                        if f == 'A' and g == 'B' or f == 'B' and g == 'C' or f == 'C' and g == 'D' or f == 'D' and g == 'A':
                            hurt += (att + zero_att)
                            if enemy_name == '骷髅':
                                if sc_act == 1:
                                    hurt -= 5
                            chance += 1
                            if att_choose == 1:
                                hurt += 5
                            if p_act <= P:
                                hurt -= DEF
                            if enemy_name == 'Tetris' and ATTE == 10:
                                hurt += 5
                            laser(DEF)
                            hurt += item_att
                    if f == 'D' and g == 'C' or f == 'C' and g == 'B' or f == 'B' and g == 'A' or f == 'A' and g == 'D':
                        hurtB += ATT
                        hurtB += ATTE
                        if chooseb == 'B':
                            hurtB -= Def
                            if enemy_name == '罗尔斯' and ATTE == 5 and random.randint(1,2) == 1:
                                hurtB += Def
                        chance += 1
                    else:
                        chance += 1
                if miaomiao == 1:
                    hurtB //= 2
                if miaomiao == 2:
                    hurtB //= 5
                if miaomiao == 3:
                    hurt *= 2
                if hide[0] + hide[1] >= random.randint(1,100):
                    hurtB = 0
                if hurtB < 0:
                    hurtB = 0
                if hurt < 0:
                    hurt -= 0
                HP -= hurt
                if enemy_name == '六芒星飞行器':
                    HP += hurt
                    H -= hurt
                    if H < 0:
                        H = 0
                        input('六芒星飞行器的护盾失效了！')
                    special_A = 8
                health -= hurtB
                item_att = 0
                choose = input(f'{enemy_name}的攻击是{enemy_fightb}')
                if P > p_act:
                    choose = input(f'{enemy_name}使用了防御!')
                if chooseb != 'B':
                    choose = input(f'你对{enemy_name}造成了{hurt}点伤害!')
                    hurt = 0
                if chooseb == 'B':
                    choose = input('因为你选择了防御,所以伤害不计入')
                if enemy_name in {'几何六面体','圆柱','长矛','滚轮','四面体','短矛','CRD','罗尔斯'} or (enemy_name == '扑克守卫' and magic_type == 'xk'):
                    xk_att = 20
                    if p_act <= P:
                        xk_att -= DEF
                        if xk_att < 0:
                            xk_att = 0
                    input(f'星空用魔法对敌人造成了{xk_att}点伤害！')
                    HP -= xk_att
                choose = input(f'你被敌人扣除了{hurtB}点血')
                if enemy_name in {'电子蛇A','精英电子蛇A'} and random.randint(1,10) <= 2:
                    input('电子蛇身上的方块脱落了！')
                    special_A[0] = 1
                if enemy_name == '六芒星飞行器':
                    special_A -= 1
                    if special_A == 0:
                        H = 100
                        input('六芒星为自己制造了一个力场盾！')
                if enemy_name == 'Tetris':
                    special_A[0] -= 1
                    special_A[1] -= 1
                    special_A[2] -= 1
                    if special_A[0] == 0:
                        special_A[0] = 5
                        HP += 100
                        input('Tetris使用了隐形方块！透明的护罩出现在了他的身前！')
                    if special_A[1] == 0:
                        special_A[1] = random.randint(2,4)
                        choose = input('Tetris使用了闪现方块！巨大的方块砸在了你身边！')
                        choose = input('回复3个大写字母以防御')
                        choose = list(input(f'请输入你的行动'))
                        chance = 0
                        while chance < 3:
                            chance += 1
                            a = random.choice(['A','B','C','D'])
                            enemy_fightb += a
                            enemy_fighta.append(a)
                        hurt = 0
                        hurtB = 0
                        chance = 0
                        wrong = 0
                        while wrong == 0:
                            wrong = 1
                            if len(choose) != 5:
                                wrong = 0
                                print('输入错误,请依照格式输入!')
                                choose = list(input(f'请选择你的防御!'))
                        while wrong_B < 4:
                            wrong_B += 1
                            if choose[wrong_B] not in {'A','B','C','D'}:
                                wrong = 0
                                wrong_B = 5
                                print('输入错误,请依照格式输入!')
                                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                            while chance < 3:
                                f = choose.pop()
                                g = enemy_fighta.pop()
                                if f == 'D' and g == 'C' or f == 'C' and g == 'B' or f == 'B' and g == 'A' or f == 'A' and g == 'D':
                                    hurtB += 22
                                    chance += 1
                                else:
                                    chance += 1
                            health -= hurtB
                            choose = input(f'闪现方块以{enemy_fight}的形式下落')
                            choose = input(f'你被闪现方块扣除了{hurtB}点血量')
                if enemy_name == '罗尔斯' and rule_change != rules:
                    input('规则的界限慢慢改变了')
                    if rules > 70 and special_A[1] == 0:
                        input('战斗逐渐趋近于白热化！')
                        special_A[1] = 1
                    if rules >= 100:
                        input('战斗的规则摇晃着崩塌了')
                        HP = 0
                if enemy_name in {'鹿法师','骷髅','罗尔斯','Tetris'}:
                    ATTE = 0
                if enemy_name == '扑克守卫':
                    special_A -= 1
                    if special_A == 0:
                        special_A = 3
                        input('扑克守卫加强了剑阵的魔法指数！')
                        ATTE += 3
                dead_interface()
                if respawned == 1:
                    break
                hurtB = 0
            if HP_B > 0:
                x = random.randint(1,4)
                a = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                b = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                c = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                d = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                e = chr(ord('A') + x - 1)
                if miaomiao == 4:
                    b,c,d,e = a,a,a,a
                enemy_fightb = a+b+c+d+e
                enemy_fighta = [a,b,c,d,e]
                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                hurt = 0
                hurtB = 0
                chance = 0
                wrong = 0
                while wrong == 0:
                    wrong = 1
                    if len(choose) != 5:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[0] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[1] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[2] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[3] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[4] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                if '零剑' in weapon:
                    zero_att = random.randint(5,50)
                if 'Complex机械长剑' in weapon and random.randint(1,5) == 3:
                    zore_att = 10
                p_act = random.randint(1,100)
                while chance < 5:
                    f = choose.pop()
                    g = enemy_fighta.pop()
                    if chooseb != 'B':
                        if f == 'A' and g == 'B' or f == 'B' and g == 'C' or f == 'C' and g == 'D' or f == 'D' and g == 'A':
                            hurt += (att + zero_att)
                            chance += 1
                            if att_choose == 1:
                                hurt += 5
                            if p_act <= P_B:
                                hurt -= DEF_B
                            laser(DEF)
                            hurt += item_att
                    if f == 'D' and g == 'C' or f == 'C' and g == 'B' or f == 'B' and g == 'A' or f == 'A' and g == 'D':
                        hurtB += ATT_B
                        hurtB += ATTE
                        if chooseb == 'B':
                            hurtB -= Def
                        chance += 1
                    else:
                        chance += 1
                if miaomiao == 1:
                    hurtB //= 2
                if miaomiao == 2:
                    hurtB //= 5
                if miaomiao == 3:
                    hurt *= 2
                if hurtB < 0:
                    hurtB = 0
                if hurt < 0:
                    hurt -= 0
                if hide[0] + hide[1] >= random.randint(1,100):
                    hurtB = 0
                HP_B -= hurt
                health -= hurtB
                item_att = 0
                choose = input(f'{enemy_name}的攻击是{enemy_fightb}')
                if P_B > p_act:
                    choose = input(f'{enemy_name}使用了防御!')
                if chooseb != 'B':
                    choose = input(f'你对{enemy_name}造成了{hurt}点伤害!')
                    hurt = 0
                else:
                    choose = input('因为你选择了防御,所以伤害不计入')
                choose = input(f'你被敌人扣除了{hurtB}点血')
                if enemy_name in {'电子蛇A','精英电子蛇A'} and random.randint(1,10) <= 2:
                    input('电子蛇身上的方块脱落了！')
                    special_A[0] = 1
                dead_interface()
                if respawned == 1:
                    break
            miaomiao = 0
            att_choose = 0
            hide[1] = 0
            if HP <= 0 and HP_B <= 0:
                choose = input('您获胜了!')
                CM += cm
                choose = input(f'你获得了{cm}个CM币')
                win = 1
    if savepoint == 0:
        save_data()
        output(f'黑暗')
        output('无边的黑暗')
        output('似乎有什么东西在流动着')
        output('越来越剧烈')
        output('直到......')
        output(f'冲破了你的感觉')
        output(f'明亮的光穿透了你的双眼，你坐起身，发现自己正在一个小房间里，天花板向下投射白色的光芒，可你并没有找到灯。房间里除了你坐着的那张灰色的小床，一个闭着的门，什么都没有。')
        output(f'你看了看自己，发现你正穿着一件短的出奇的衣服，看起来不是你的，你想要活动身体，却感觉十分酸痛')
        print(f'请问你现在要?')
        output(f'A.尝试站起来,B.回忆,C.什么也不做')
        #虽然但是第一个选项很有意义即使没什么用我也要写一个注释
        while choose not in {'A','B','C'}:
            print(f'请做出您的选择')
            output(f'A.尝试站起来,B.回忆,C.什么也不做')
        else:
            if choose == 'A':
                output(f'你尝试站起来，可是还没下床就瘫倒在床上')
                secretA = '0'
            if choose == 'B':
                output(f'你什么也回忆不起来')
                secretA = '1'
        #哦我的天哪！这是一个平平无奇，满大街到处都是的隐藏选项!!!
        #如果你这么说的话我就一点也激动不起来了(
            if choose == 'C':
                choose = input(f'你什么也不做')
                secretA = '0'
        #选项做完了多么有成就感啊，我一定要写一个注释！！！
        output(f'正当你在床上想来想去的时候，你突然听见“咚咚”的声音，突然，那道灰色的门猛地消失了。从门外走进来一个身穿黑色制服的人。你看到他手上拿着一张卡片。')
        output(f'你有点手足无措，那个身穿黑色制服的人走到了你的旁边，比划了一些手势，你的床边就忽然升起了一个蓝色方框，他拿着卡片，照着方框仔细比对了一下，点了点头，然后看向你，说了一个词')
        output(f'“Zero?”')
        output(f'你感到有点奇怪，想弄清楚这是哪')
        print(f'你现在要?')
        output('A：问他这是哪,B：呼呼大睡,C：什么也不做')
        while choose not in {'A','B','C'}:
            print(f'请您做出您的选择')
            output(f'A：问他这是哪,B：呼呼大睡,C：什么也不做')
        else:
            if choose == 'A':
                choose =input(f'你尝试问他这是哪，可是你发现你一个字都说不出来')
                secretB = '0'
            if choose == 'B':
                choose =input(f'你倒头大睡')
                secretB = '1'
        #众所周知,睡眠能够帮助人触发世界的特性(
            if choose == 'C':
                choose =input(f'你什么也不做')
                secretB = '0'
        if secretB == '0':
            output(f'那人显然是注意到了你的困惑，笑着对你说：“没关系，你现在还很虚弱，再试试就能说话了!”')
            output(f'你断断续续，无力地说了几个字。')
            output(f'“好吧，看来只能让我主动做自我介绍了。”那人笑着说。')
            output(f'“我是星空，这里是Cloud Village，也就是云村，我们现在位于机票总部，不是那个真正的机票啦，这里是一个推演基站，不需要管这么多。我们这个地方……”')
            output(f'许多崭新的名词在你耳边环绕着，你不自觉地打了个哈欠。')
            output(f'“好吧，看来你现在有点困了，你应该能说话了吧，有什么想问的，快说吧。”星空说')
            output(f'你想问?')
    #您看这里代码这么杂我还有空写注释吗......我还真有,这里代码别乱改(
            if secretA == '0':
                output(f'A：关于云村B：关于机票C：关于世界D：直接睡觉')
                while choose not in {'A','B','C','D'}:
                    print(f'请您做出您的选择')
                    output(f'A：关于云村B：关于机票C：关于世界D：直接睡觉')
                else:
                    if choose == 'A' or choose == 'B' or choose == 'C' :
                        input('星空说：“这个问题嘛……很复杂，今天很难跟你说清楚了，你先睡觉吧”')
                    else:
        #哦我的天那你知道这么套else会让我的脑子有多乱吗(
                        input(f'你直接睡觉')
        #虽然但是,我选择睡觉(
            if secretA == '1':
                output(f'A:关于云村B:关于机票C:关于世界D:直接睡觉,E:问他关于你自己')
                while choose not in {'A','B','C','D','E'}:
                    print(f'请您做出您的选择')
                    output(f'A:关于云村B:关于机票C:关于世界D:直接睡觉,E:问他关于你自己')
                else:
                    if choose == 'A' or choose == 'B' or choose == 'C':
                        output('星空说：“这个问题嘛……很复杂，今天很难跟你说清楚了，你先睡觉吧”')
                    if choose == 'D':
        #哦我的天那你知道这么套else会让我的脑子有多乱吗(
        #是的没错这段程序我是复制上面的他连注释都一样
                        input(f'你直接睡觉')
                    if choose == 'E':
        #隐藏剧情好耶！
                        input(f'星空说：“你啊……是个不太普通的普通人，不属于魔法体系成员，我们只能从记忆碎片里面找到你的名字……哦，你问我们是怎么发现你的，我们是在仓库里发现你的，不过当时嘛……有点难以启齿……这样吧，我给你一把[一次性钥匙]，你明天来会议室找我。”')
                        input('一次性钥匙加入了你的物品栏')
                        item.append('一次性钥匙')
                        input(f'现在你的物品有{item}')
        #《有关我不知道怎么一次性解决物品超过上限问题的这档事》
        #不过反正这是初期也没什么上限问题我直接摸鱼不搞也没差（
        if secretB == '1':
            output('zzzzzzzzzzz......')
        ###########（
        output(f'你不知道睡了多久，只是感觉一醒来，你的房间完全变了。')
        output(f'周围洁白一片的墙壁被粉色的壁纸覆盖，天花板上的白光换成了柔和的粉色微光，还挂着各种卡通图案。不知为何，你觉得你挺讨厌这些装饰的。')
        output(f'你下了床，感觉比昨天要舒畅多了。')
        #推荐现在上床再睡一觉(
        output(f'房间里有一个写字台，一个床头柜，还有一个摆了几本书的书橱')
        print(f'你现在要?')
        output('A：出门,B：看床头柜,C：看书,D：继续睡觉')
        while choose not in {'A','B','C','D'}:
            print('请做出您的选择')
            output('A：出门,B：看床头柜,C：看书,D：继续睡觉')
        else:
            if choose == 'A':
                if '一次性钥匙' not in item:
                    output('门似乎打不开')
                    secretA = 0
                else:
                    output(f'你查看了一番,插入了【一次性钥匙】')
                    output('你打开了门！')
                    item.remove('一次性钥匙')
                    secretA = 1
                    secretB = 1
                    secretD = 1
            if choose == 'B':
                output(f'你看了看床头柜，找到了一个【气球】！')
                output('气球加入了你的物品栏')
                item.append('气球')
                output(f'现在你的物品有{item}')
                secretA = 0
            if choose == 'C':
                output('书橱里都是很烂的美少女打怪漫画，你不喜欢那玩意儿')
                secretA = 0
            if choose == 'D':
                output('你继续睡觉，怎么也睡不着')
                secretA = 0
        #您终于睡不着了(
        if secretA == 0:
            output(f'你在房间里转了半天，没看到什么有意思的东西。')
            output(f'过了一会儿，你看到门像昨天一样被打开了，星空走了进来。')
            output(f'“真对不起，看来我昨天忘记给你钥匙了，不过我会把门设成自动的，哈哈！”星空说。“现在你可以出门随便逛逛了，我觉得你最好到训练场来，我会教你关于魔法体系的基本常识。”')
            output(f'你出了门，门外是一个巨大的建筑物，人来人往，十分嘈杂。喊叫声不绝入耳：')
            print('“踏平天空！”')
            #time的首次应用，你猜到时候我会不会把这个应用删掉(
            t.sleep(0.5)
            print('“给我来份有机化学和无机化学，快点。”')
            t.sleep(0.5)
            print('“这把金S稳了！”')
            t.sleep(0.5)
            if fun == 15:
                print('“养成亲社会行为！”')
                t.sleep(0.5)
            print('“三倍ice cream！！！”')
            output(f'“你感到有点乱，找到了一个地图，上面标着建筑物里的各个地点，有训练场、档案室、会议室等等。你注意到这个建筑叫“机票模拟大厦””')
            output('您现在要?')
            output('A：去训练场B：去档案室C：去会议室D：回到房间')
            while choose not in {'A','B','C','D'}:
                print('请做出您的选择')
                output('A：去训练场B：去档案室C：去会议室D：回到房间')
            else:
                if choose == 'A':
                    print('你去了训练场')
                    secretB = 0
                if choose == 'B':
                    print('你来到档案室前，门是锁的，你转头去了训练场')
                    secretB = 0
                if choose == 'C':
                    print('你去了会议室，门开了')
                    secretB = 1
                if choose == 'D':
                    print('你想回房间，但还是打不开门，你去了训练场')
                    secretB = 0
        #反正你就是回不去房间(
        if secretB == 0:
            output(f'你到了训练场，这是一个四周都是玻璃的封闭房间，屋子里有个木马，除此之外空无一物。')
            output(f'旁边有一个擂台，有几个人在外面观看，不过没人在里面。')
            output(f'你找了找，没看见星空')
            print('你会?')
            output('A：等待,B：摸摸木马,C：看看擂台')
            while choose not in {'A','B','C'}:
                print('请做出您的选择')
                output('A：等待,B：摸摸木马,C：看看擂台')
                
            else:
                if choose == 'A':
                    output('你什么也不做')
                    secretC = 0
                    view_status
                elif choose == 'B':
                    output('你摸了摸木马，突然，一阵奇怪的响声传来！')
                    #手欠,真的
                    print('你似乎看到了好几串字母在你眼前飘过：')
                    t.sleep(0.3)
                    print('AAAAA')
                    secretC = 1
                    #最终反击.JPG
                    output('一股刺痛传来，但你身上没出现伤口[HP-10]')
                    health -= 10
                    
                if choose == 'C':
                    output('你看了看擂台，没有发现异常')
                    secretC = 0
                    
                if secretC == 0:
                    output('你等了一会儿，星空来了。')
                    output('“很抱歉来晚了，刚才在整理资料忘了过来，我们现在开始吧！”星空说，随后指向那个木马。')
                    output('“看着这个木马，你感觉到了什么？”')
                    output('你对着木马，没有感到什么，只不过觉得有点怪异。')
                if secretC == 1:
                    output('你有点吃惊，但是没有办法，你只好等星空来。')
                    output('过了一会儿，你看到星空走了过来，他见到你抱歉地说：“对不起来晚了……”')
                    output('突然，他似乎注意到了什么，说到：“等等，你已经和这个木马战斗过了吗？”')
                    output('你对星空说了刚才的怪事。')
                    output('星空笑着说：“哦，没关系，你只是触发了它的攻击方式罢了。来，让我们试一试战斗吧。”')
                    #看end受伤了自己还笑的xk是屑
                output('星空说：“让我描述详细一点吧，在魔法系统下，战斗就是我们的【魔法核心】相互接触的过程，每个人都有一个【魔法核心】，只不过大多数人都不会用罢了，我来教你怎么使用。')
                output('星空跟你详细说明了使用魔法核心的方法，你试了一下，突然你感觉世界一下就改变了！')
                print('星空：现在我们进入了战斗界面！当你听完我的这些话后，就可以加入战斗了。战斗分为准备阶段和对战阶段，在准备阶段时，你可以尝试A【物品】、B【防御】、C【魔法】、D【跳过】，不过你现在没有魔法值，没有物品，选择【防御】吧，物品可以在获得后摁Z查看')
                t.sleep(0.5)
                wooden_horse = 60
                magic_point = 0
                win = 0
                choose = input('A,物品B,防御C,魔法D,跳过')
                while choose not in {'A','B','C','D'}:
                    print('请做出你的选择')
                    choose = input('A,物品B,防御C,魔法D,跳过')
                if choose == 'A':
                    print('你没有可以使用的物品')
                    secretC = 0
                if choose == 'B':
                   secretC = 1
                if choose == 'C':
                    choose = input('A：治疗魔法（30）B：战斗魔法（70）C：黑暗魔法（？）')
                    while choose not in {'A','B','C'}:
                        print('请做出你的选择')
                        choose = input('A：治疗魔法（30）B：战斗魔法（70）C：黑暗魔法（？）')
                    else:
                        choose = input('你的魔法值不够！')
                    secretC = 0
                if choose == 'D':
                    secretC = 0
                if secretC == 0:
                    choose = input('星空：你……不选防御吗？那也挺好。')
                    choose = input('星空：总之，现在是进入【战斗】的时间了！')
                    choose = input('敌人会利用A、B、C、D四种方式攻击你，每回合攻击五次，其中，D克A克B克C克D，这个木马接下来会使用AAAAA攻击，回复DDDDD来阻止它吧！')
                if secretC == 1:
                    choose = input('星空：很好，让我们试一下战斗吧！')
                    choose = input('星空：现在是进入【战斗】的时间了！')
                    choose = input('敌人会利用A、B、C、D四种方式攻击你，每回合攻击五次，其中，D克A克B克C克D，这个木马接下来会使用AAAAA攻击，回复DDDDD来阻止它吧！因为我们点击了防御，我们无法对敌人造成伤害，但攻击可以增加魔法值！')
                choose = input('请打出你的攻击')
                if choose == 'DDDDD':
                    choose = input('星空：太棒了，现在我们有足够的魔法值来使用魔法了，试一下【魔法】吧，它会给你带来增益效果！剩下的你就自己摸索吧')
                    magic_point += 40
                else:
                    choose = input('星空：呃……你没有听我的，看来你是想自己对战了，那我就不打扰你了！我先给你个治疗法术吧！')
                    choose = input('[你的HP回满了]')
                    health = 240
                a,b,c,d,e = '','','','',''
                while win == 0:
                    magic_choose = 0
                    att_choose = 0
                    item_choose = 0
                    while magic_choose == 0 and item_choose == 0:
                        chooseb = 'A'
                        print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health},敌人血量为{wooden_horse}')
                        choose = input('A,物品B,防御C,魔法D,跳过')
                        while choose not in {'A','B','C','D'}:
                            print('请做出你的选择')
                            choose = input('A,物品B,防御C,魔法D,跳过')
                        if choose == 'A':
                            print('你没有可以使用的物品')
                            item_choose = 0
                        if choose == 'B':
                            choose = input('你选择了防御!')
                            magic_point += 40
                            magic_choose = 1
                            if magic_point >= 100:
                                magic_point = 100
                            chooseb = 'B'
                        if choose == 'C':
                            choose = input(f'A：治疗魔法（{health_point}）B：战斗魔法（70）C：黑暗魔法（？）')
                            while choose not in {'A','B','C'}:
                                print('请做出你的选择')
                                choose = input(f'A：治疗魔法（{health_point}）B：战斗魔法（70）C：黑暗魔法（？）')
                            else:
                                if choose == 'A':
                                    if magic_point < health_point:
                                        choose = input('你的魔法值不够!')
                                        magic_choose = 0
                                    if magic_point >= health_point:
                                        choose = input(f'你使用了治疗法术!你的血量回复了{health_plus}点!')
                                        health += health_plus
                                        if health > 240:
                                            health = 240
                                        magic_choose = 1
                                        magic_point -= health_point
                                if choose == 'B':
                                    if magic_point < 70:
                                        choose = input('你的魔法值不够!')
                                        magic_choose = 0
                                    if magic_point >= 70:
                                        choose = input('你使用了战斗法术!你的攻击提高了5点,持续一回合!')
                                        att_choose = 1
                                        magic_choose = 1
                                        magic_point -= 70
                                if choose == 'C':
                                    choose = input('l͓̩̫̘͙͔̯͖̟̤̓͊̑̌́̂̆̚ò̥̪̭̱̰̝̒͂̄͋̿̏͆́̚c͍̲͇͚̖̬͈̪͙̳͌̉́̃k̪̥̱̝̱̑̈́̏̽͗̊̈́͂̀̍e̞͎̩̜̱̩͚̤̊͌̀̀d̠̖̞̝̙̪̟̞̐͛̈̊̀͂̄͌̓̏͌̓ͅ')
                                    magic_choose = 0
                                choose = 0
                        if choose == 'D':
                            choose = input('你跳过了你的回合')
                            magic_choose = 1
                    x = random.randint(1,4)
                    a = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    b = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    c = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    d = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    e = chr(ord('A') + x - 1)
                    enemy_fight = a+b+c+d+e
                    enemy_fighta = [a,b,c,d,e]
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    hurt = 0
                    hurtB = 0
                    chance = 0
                    wrong = 0
                    while wrong == 0:
                        wrong = 1
                        if len(choose) != 5:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[0] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[1] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[2] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[3] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[4] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    else:
                        while chance < 5:
                            #快悄悄这个地方,我把chance < 5写成了chance <= 5然后查了一天才查到这个bug
                            #悄悄改为瞧瞧,这是个错别字(划)通假字
                            f = choose.pop()
                            g = enemy_fighta.pop()
                            if chooseb != 'B':
                                if f == 'A' and g == 'B' or f == 'B' and g == 'C' or f == 'C' and g == 'D' or f == 'D' and g == 'A':
                                    hurt += 10
                                    chance += 1
                                    if att_choose == 1:
                                        hurt += 5
                            if f == 'D' and g == 'C' or f == 'C' and g == 'B' or f == 'B' and g == 'A' or f == 'A' and g == 'D':
                                hurtB += 5
                                if chooseb == 'B':
                                    hurtB -= Def
                                    if Def >= 5:
                                        hurtB = 0
                                chance += 1
                            else:
                                chance += 1
                        wooden_horse -= hurt
                        health -= hurtB
                        choose = input(f'敌方的攻击是{enemy_fight}')
                        if chooseb != 'B':
                            choose = input(f'你对敌方造成了{hurt}点伤害!')
                            hurt = 0
                        else:
                            choose = input('因为你选择了防御,所以伤害不计入')
                        choose = input(f'你被敌人扣除了{hurtB}点血')
                        hurtB = 0
                        att_choose = 0
                    if wooden_horse <= 0:
                        choose = input('您获胜了!')
                        #战斗系统,好耶!
                        win = 1
                    if health <= 20:
                        choose = input(f'您似乎要被打败了,星空赶了过来,给你释放了治疗魔法')
                        choose = input('你的HP回满了!')
                        health = 100
                output('星空说：“干得漂亮！你击败了敌人，不过这充其量只是个训练品而已，你还要遇到更强的战斗哦。”')
                output('你们一起走出了训练场，来到大厅。')
                output('星空说：“好啦，剩下的时间留给你自由探索云村吧！”说完就离开了。')
                secretB = 0
                secretA = 0
                secretE = 0
        if secretB == 1:
            output(f'你进入会议室，里面有个很大的红色圆桌，桌上摆了许多吃的')
            
            output(f'这时，你往一个角落看了看，发现星空正背对着你打电话')
            
            output('现在你要?')
            
            output('A：吃掉桌上的东西,B：等待,C：听听星空在讲什么')
            
            while choose not in {'A','B','C'}:
                print('请做出您的选择')
                output('A：吃掉桌上的东西,B：等待,C：听听星空在讲什么')
                
            else:
                if choose == 'A':
                    if fun == 18:
                        output('你吃了一些[水果]')
                        output('你在水果底下发现了一个[彩蛋]')
                        output('你把他留在了原处')
                    else:
                        output('你吃了一些水果，并没有感觉到什么')
                    #不要随便吃陌生人的东西,因为我们要行己有耻止于至善(
                if choose == 'B':
                    output('你什么也不做')
                if choose == 'C':
                    print('你凑近了星空，发现他在小声说着话，你勉强听清楚了一些：')
                    t.sleep(0.6)
                    print('“是的，渗透机器的事情，我会集中处理的，在事情搞好之前，千万不要轻举妄动，否则每个人都会有麻烦的……”')
            if secretD == 0:
                output('过了一会儿，星空挂了电话，走了出来看到了你，似乎很惊奇的样子。')
                
                #我可以说我这个搞代码的已经看不懂这个剧情发展了吗(
                #日常怀疑自己是搞错了代码
                output('“Zero……你怎么跑这来啦，不是让你去训练场吗？”')
                
                output('你没回答，冷冷地看着他')
                
                output('“呃……不要摆出这么恐怖的神色吧……”星空无奈地说道。')
                
                output('“总之，既然你到这来了，我就给你个东西，希望会对你有用。”')
                
                output('星空说着，给了你一个【复活爱心】')
                
                item.append('复活爱心')
                love += 1
                print('你会?')
                output('A：查看B：交谈C：离开')
                
                while choose not in {'A','B','C'}:
                    print('请做出您的选择')
                    output('A：查看B：交谈C：离开')
                    
                else:
                    if choose == 'A':
                        output('【复活爱心】具有强大能量的法术，可以使你在最近的存档区域复活')
                    if choose == 'B':
                        output('你想要交谈，没什么好说的')
                    if choose == 'C':
                        chooseb = input('你离开了会议室')
                    secretA = 0
                    if choose == 'C':
                        secretE = 0
                    else:
                        output('星空说道：“我还有点事先走了，你慢慢探索吧，不过注意一点……别去小镇尽头的废弃小店。”')
                        secretE = 1
            if secretD == 1:
                output('过了一会儿，星空挂了电话，看到你来了，说：“你来啦，现在我来给你看一个重要的东西。”')
                
                output('星空说着，给了你一盒录像带，示意你把它插入会议室的大屏幕上。')
                
                print('你会：')
                output('A：插录像带B：什么也不做C：逃跑')
                #各位觉得懵逼不要紧,我也觉得懵
                #他们应该是认识吧
                
                while choose not in {'A','B','C'}:
                    print('请做出您的选择')
                    output('A：插录像带B：什么也不做C：逃跑')
                    
                else:
                    if choose == 'A':
                        chooseb = input('你插入了录像带')
                    if choose == 'B':
                        chooseb = input('星空看了看你，说：“这……你这么无动于衷真的好嘛……我来插吧。”')
                    if choose == 'C':
                        chooseb = input('带着录像带跑了出去，星空在后面大声喊你，你不理他（获得【录像带】）')
                        item.append('录像带')
                        output('你逃出了会议室，一路狂奔，周围的人都不知道你着了什么魔。')
                        
                        output('你四处乱撞，跑出了大楼，外面是一个小镇，道路平坦开阔，并没有你想象中的那么多人。')
                        
                        output('你看到了一条小巷，随便撞了进去。')
                        
                        output('小巷空无一人，与大厅里的人员密布简直是天壤之别。')
                        
                        output('你往小巷里深入，经过好几个弯路，光线也越来越暗。')
                        
                        output('这时，你看到地上有一条奇怪的黑裙子，你捡了起来。（获得【黑色短裙】）')
                        item.append('黑色短裙')
                        
                        output('你继续向前走，阴暗狭窄的道路让你感到有些阴森，这时，面前出现了一扇门。')
                        
                        output('门没有锁，你打开了门。')
                        
                        output('屋内十分黑暗，但也不是一丝光线也没有。在你眼前，一座巨大、神秘的机器发着一丝微光。')
                        
                        output('你会：A：向前走,B：站着不动,C：逃跑')
                        #好嘛你以前是个二战的法国人吧
                        
                        while choose not in {'A','B','C'}:
                            print('请做出您的选择')
                            output('你会：A：向前走,B：站着不动,C：逃跑')
                            
                        else:
                            if choose == 'A':
                                output('你向前走，这时，奇怪的事情发生了！')
                                
                            if choose == 'B':
                                output('你站在原地一动不动。突然，一声巨响传来。')
                                
                            if choose == 'C':
                                output('你想逃跑，但你往后走时，门关上了，怎么也打不开门！')
                                
                            #boss战的感觉(
                            output('霎时间，周围警报声迭起，无数显示屏变成了凶恶的红光。')
                            
                            output('你不知道发生了什么，吓得呆站在原地。')
                            
                            output('一道刺眼的白光闪过，你顿时失去了知觉')
                            
                    if choose == 'A' or choose == 'B':
                        output('录像带渐渐启动，纯黑的大屏幕上出现了画面。')
                        
                        output('这是一个封闭的房间，被昏暗的光线照射着的一堆箱子杂乱地摆在地上，除此之外，什么都没有。你似乎认为这录像只由一幅画面组成。')
                        
                        output('忽然，你似乎听到了什么响声，屏幕剧烈抖动，然后一下变黑了。')
                        
                        output('过了一会儿，屏幕上再次出现了画面，你看见地上箱子摆放得整整齐齐，在没有箱子的地面上，多了一条玫瑰花图案的毯子，以及一些带刺的藤蔓。')
                        
                        output('不知怎么，你感到这场景有些熟悉。')
                        
                        output('录像又放了一会，仍然是这场景，没有一点变化，然后放映结束了。')
                        
                        output('星空说：“你看起来不太清楚吧。事实上，这个录像带是我们在仓库里发现的，就掉在你身边，我们不知道这是什么意思，所以嘛……我认为这可以让你的记忆恢复一点，你想起来什么东西了吗？”')
                        
                        output('你感觉什么也想不起来。')
                        
                        output('星空看着你，笑了笑：“想不起来也没关系，这盒录像带给你，我们就先走吧。接下来我们去训练场练习！（获得【录像带】）')
                        item.append('录像带')
                        #在编写这段代码时我三次把shift摁成了ctrl
                        #我是废物
                        
                        output('你们到了训练场，看到这里有个训练人偶。星空对你说：接下来我来解释一下战斗吧！')
                        
                        output('星空说：“让我描述详细一点吧，在魔法系统下，战斗就是我们的【魔法核心】相互接触的过程，每个人都有一个【魔法核心】，只不过大多数人都不会用罢了，我来教你怎么使用。')
                        
                        output('星空跟你详细说明了使用魔法核心的方法，你试了一下，突然你感觉世界一下就改变了！')
                        
                        print('星空：现在我们进入了战斗界面！当你听完我的这些话后，就可以加入战斗了。战斗分为准备阶段和对战阶段，在准备阶段时，你可以尝试A【物品】、B【防御】、C【魔法】、D【跳过】，不过你现在没有魔法值，没有物品，选择【防御】吧，物品可以在获得后摁Z查看')
                        t.sleep(0.5)
                        wooden_horse = 60
                        magic_point = 0
                        win = 0
                        choose = input('A,物品B,防御C,魔法D,跳过')
                        while choose not in {'A','B','C','D'}:
                            print('请做出你的选择')
                            choose = input('A,物品B,防御C,魔法D,跳过')
                        if choose == 'A':
                            print('你没有可以使用的物品')
                            secretC = 0
                        if choose == 'B':
                           secretC = 1
                        if choose == 'C':
                            choose = input('A：治疗魔法（30）B：战斗魔法（70）C：黑暗魔法（？）')
                            while choose not in {'A','B','C'}:
                                print('请做出你的选择')
                                choose = input('A：治疗魔法（30）B：战斗魔法（70）C：黑暗魔法（？）')
                            else:
                                choose = input('你的魔法值不够！')
                            secretC = 0
                        if choose == 'D':
                            secretC = 0
                        if secretC == 0:
                            choose = input('星空：你……不选防御吗？那也挺好。')
                            choose = input('星空：总之，现在是进入【战斗】的时间了！')
                            choose = input('敌人会利用A、B、C、D四种方式攻击你，每回合攻击五次，其中，D克A克B克C克D，这个木马接下来会使用AAAAA攻击，回复DDDDD来阻止它吧！')
                        if secretC == 1:
                            choose = input('星空：很好，让我们试一下战斗吧！')
                            choose = input('星空：现在是进入【战斗】的时间了！')
                            choose = input('敌人会利用A、B、C、D四种方式攻击你，每回合攻击五次，其中，D克A克B克C克D，这个木马接下来会使用AAAAA攻击，回复DDDDD来阻止它吧！因为我们点击了防御，我们无法对敌人造成伤害，但攻击可以增加魔法值！')
                        choose = input('请打出你的攻击')
                        if choose == 'DDDDD':
                            choose = input('星空：太棒了，现在我们有足够的魔法值来使用魔法了，试一下【魔法】吧，它会给你带来增益效果！剩下的你就自己摸索吧')
                            magic_point += 40
                        else:
                            choose = input('星空：呃……你没有听我的，看来你是想自己对战了，那我就不打扰你了！我先给你个治疗法术吧！')
                            choose = input('[你的HP回满了]')
                            health = 240
                        a,b,c,d,e = '','','','',''
                        while win == 0:
                            magic_choose = 0
                            att_choose = 0
                            item_choose = 0
                            while magic_choose == 0 and item_choose == 0:
                                chooseb = 'A'
                                print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health},敌人血量为{wooden_horse}')
                                choose = input('A,物品B,防御C,魔法D,跳过')
                                while choose not in {'A','B','C','D'}:
                                    print('请做出你的选择')
                                    choose = input('A,物品B,防御C,魔法D,跳过')
                                if choose == 'A':
                                    print('你没有可以使用的物品')
                                    item_choose = 0
                                if choose == 'B':
                                    choose = input('你选择了防御!')
                                    magic_point += 40
                                    magic_choose = 1
                                    if magic_point >= 100:
                                        magic_point = 100
                                    chooseb = 'B'
                                if choose == 'C':
                                    choose = input(f'A：治疗魔法（{health_point}）B：战斗魔法（70）C：黑暗魔法（？）')
                                    while choose not in {'A','B','C'}:
                                        print('请做出你的选择')
                                        choose = input(f'A：治疗魔法（{health_point}）B：战斗魔法（70）C：黑暗魔法（？）')
                                    else:
                                        if choose == 'A':
                                            if magic_point < health_point:
                                                choose = input('你的魔法值不够!')
                                                magic_choose = 0
                                            if magic_point >= health_point:
                                                choose = input(f'你使用了治疗法术!你的血量回复了{health_plus}点!')
                                                health += health_plus
                                                if health > 240:
                                                    health = 240
                                                magic_choose = 1
                                                magic_point -= health_point
                                        if choose == 'B':
                                            if magic_point < 70:
                                                choose = input('你的魔法值不够!')
                                                magic_choose = 0
                                            if magic_point >= 70:
                                                choose = input('你使用了战斗法术!你的攻击提高了5点,持续一回合!')
                                                att_choose = 1
                                                magic_choose = 1
                                                magic_point -= 70
                                        if choose == 'C':
                                            choose = input('l͓̩̫̘͙͔̯͖̟̤̓͊̑̌́̂̆̚ò̥̪̭̱̰̝̒͂̄͋̿̏͆́̚c͍̲͇͚̖̬͈̪͙̳͌̉́̃k̪̥̱̝̱̑̈́̏̽͗̊̈́͂̀̍e̞͎̩̜̱̩͚̤̊͌̀̀d̠̖̞̝̙̪̟̞̐͛̈̊̀͂̄͌̓̏͌̓ͅ')
                                            magic_choose = 0
                                        choose = 0
                                if choose == 'D':
                                    choose = input('你跳过了你的回合')
                                    magic_choose = 1
                            x = random.randint(1,4)
                            a = chr(ord('A') + x - 1)
                            x = random.randint(1,4)
                            b = chr(ord('A') + x - 1)
                            x = random.randint(1,4)
                            c = chr(ord('A') + x - 1)
                            x = random.randint(1,4)
                            d = chr(ord('A') + x - 1)
                            x = random.randint(1,4)
                            e = chr(ord('A') + x - 1)
                            enemy_fight = a+b+c+d+e
                            enemy_fighta = [a,b,c,d,e]
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                            hurt = 0
                            hurtB = 0
                            chance = 0
                            wrong = 0
                            while wrong == 0:
                                wrong = 1
                                if len(choose) != 5:
                                    wrong = 0
                                    print('输入错误,请依照格式输入!')
                                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                                elif choose[0] not in {'A','B','C','D'}:
                                    wrong = 0
                                    print('输入错误,请依照格式输入!')
                                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                                elif choose[1] not in {'A','B','C','D'}:
                                    wrong = 0
                                    print('输入错误,请依照格式输入!')
                                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                                elif choose[2] not in {'A','B','C','D'}:
                                    wrong = 0
                                    print('输入错误,请依照格式输入!')
                                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                                elif choose[3] not in {'A','B','C','D'}:
                                    wrong = 0
                                    print('输入错误,请依照格式输入!')
                                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                                elif choose[4] not in {'A','B','C','D'}:
                                    wrong = 0
                                    print('输入错误,请依照格式输入!')
                                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                            else:
                                while chance < 5:
                                    #快悄悄这个地方,我把chance < 5写成了chance <= 5然后查了一天才查到这个bug
                                    #悄悄改为瞧瞧,这是个错别字(划)通假字
                                    f = choose.pop()
                                    g = enemy_fighta.pop()
                                    if chooseb != 'B':
                                        if f == 'A' and g == 'B' or f == 'B' and g == 'C' or f == 'C' and g == 'D' or f == 'D' and g == 'A':
                                            hurt += 10
                                            chance += 1
                                            if att_choose == 1:
                                                hurt += 5
                                    if f == 'D' and g == 'C' or f == 'C' and g == 'B' or f == 'B' and g == 'A' or f == 'A' and g == 'D':
                                        hurtB += 5
                                        if chooseb == 'B':
                                            hurtB -= Def
                                            if Def >= 5:
                                                hurtB = 0
                                        chance += 1
                                    else:
                                        chance += 1
                                wooden_horse -= hurt
                                health -= hurtB
                                choose = input(f'敌方的攻击是{enemy_fight}')
                                if chooseb != 'B':
                                    choose = input(f'你对敌方造成了{hurt}点伤害!')
                                    hurt = 0
                                else:
                                    choose = input('因为你选择了防御,所以伤害不计入')
                                choose = input(f'你被敌人扣除了{hurtB}点血')
                                hurtB = 0
                                att_choose = 0
                            if wooden_horse <= 0:
                                choose = input('您获胜了!')
                                #战斗系统,好耶!
                                win = 1
                            if health <= 20:
                                choose = input(f'您似乎要被打败了,星空赶了过来,给你释放了治疗魔法')
                                choose = input('你的HP回满了!')
                                health = 100
                        output('星空说：“干得漂亮！你击败了敌人，不过这充其量只是个训练品而已，你还要遇到更强的战斗哦。”')
                        output('你们一起走出了训练场，来到大厅。')
                        output('星空说：“好啦，剩下的时间留给你自由探索云村吧！”说完就离开了。')
                        secretA = 0
                        secretE = 0
        #这里的缩进写的真的是不忍直视
        #我也这么认为（
        if secretA == 0:
            output('剩下的时间留给你自己了')
            walkA,walkB,walkC,walkD,walkE = 0,0,0,0,0
            super_market = 0
            while walkB == 0:
                chooseA = 1
                if secretE == 0:
                    output('你会：A：到处逛逛1,B：到处逛逛2,C：到处逛逛3,D：到处逛逛4,E：回房间')
                    
                    while choose not in {'A','B','C','D','E'}:
                        print('请做出您的选择')
                        output('你会：A：到处逛逛1,B：到处逛逛2,C：到处逛逛3,D：到处逛逛4,E：回房间')
                        
                if secretE == 1:
                    output('你会：A：到处逛逛1,B：到处逛逛2,C：到处逛逛3,D：到处逛逛4,E：回房间,F：去废弃小店')
                    
                    while choose not in {'A','B','C','D','E','F'}:
                        print('请做出您的选择')
                        output('你会：A：到处逛逛1,B：到处逛逛2,C：到处逛逛3,D：到处逛逛4,E：回房间,F：去废弃小店')
                        
                    
            #今天是2021年11月27日,虽然这个程序还有N多个bug,但我还是要催更一下end的文案(
            #现在还是2021年11月27日,end更了,但我看不懂了
                if choose == 'A':
                    output('你在大厅里逛了逛，这里人来人往，十分热闹。')
                    
                    output('这时，你看到一个人站在一家小店前吆喝：柠檬汁，免费品尝！')
                    
                    output('你会：A：品尝,B：不品尝')
                    
                    while choose not in {'A','B'}:
                        print('请做出你的选择')
                        output('你会：A：品尝,B：不品尝')
                        
                    else:
                        if choose == 'A':
                            output('你喝了几口，感觉在喝烈性毒药[HP-1]')
                            
                            health -= 1
                            dead_interface()
                            if respawned == 1:
                                respawned = 0
                                continue
                        if choose == 'B':
                            output('你没有喝')
                            
                    output('你又在大厅里逛了逛，发现了一家超市，不过里面的人太多了，似乎没什么好看的。')
                    
                    output('你会：A：去超市,B：继续逛逛')
                    
                    while choose not in {'A','B'}:
                        print('请做出你的选择')
                        output('你会：A：去超市,B：继续逛逛')
                        
                    else:
                        if choose == 'A':
                            choose = 'C'
                            chooseA = 0
                            #现在是2021年11月27日,end还没更这个超市支线,所以我很手足无措(
                        if choose == 'B':
                            output('你继续逛逛')
                            
                            walkA = 1
                            continue
                if choose == 'B':
                    output('你出了大厅，外面的人明显少了很多')
                    
                    output('你看到外面是个整整齐齐的小镇，你身后的大厦好像是唯一的大型建筑。午后的阳光照在大路上，使道路变得格外温和，你也踏上了这条路。')
                    
                    output('你走着走着，来到一个三岔路口，你会：A：向左走,B：向右走,C：原路返回')
                    
                    while choose not in {'A','B','C'}:
                        print('请做出您的选择')
                        output('你会：A：向左走,B：向右走,C：原路返回')
                        
                    else:
                        if choose == 'A':
                            output('你向左走去')
                            walkB = 1
                            
                            output('你看到路边楼房前，一个遮阳伞下有人在吆喝：“绝佳的冰棍哦！快来看看吧！”你走上前，发现是一位普通居民')
                            
                            output('你会：A：买个冰棍,B：继续向前走')
                            
                            while choose not in {'A','B'}:
                                print('请做出您的选择')
                                output('你会：A：买个冰棍,B：继续向前走')
                                
                            else:
                                if choose == 'A':
                                    output('你打算买冰棍，但你突然发现自己没有钱')
                                    
                                    output('卖冰棍的人看着你尴尬的样子，打算帮助你，却误解了你的意思')
                                    output('“呃……这位小妹妹是不是新来的那位？你还不知道这里的钱吗？我们的钱叫做【CM币】，是全球通用的货币！你也知道的！这样吧，这跟冰棍送你了！”')
                                    
                                    output('你接过冰棍，心想这里的人都已经知道自己了吗？')
                                    
                                    item.append('冰棍')
                                    fight_item.append('冰棍')
                                    choose = 'B'
                                if choose == 'B':
                                    output('你继续向前走，发现前面被墙挡住了，你只好去另一条路')
                                    
                                    choose = 'B'
                        if choose == 'B':
                            output('你向右走去')
                            walkB = 1
                            
                            output('你顺着一条很长的路走了一段时间，发现没路了，正当你准备离开时，你发现道路尽头有个漆黑的小巷！小巷看上去空无一人，十分阴森。但你还是决定看看，便钻了进去。')
                            
                            output('你往小巷里深入，经过好几个弯路，光线也越来越暗。最后，面前出现了一扇门，看上去门没有锁。')
                            
                            output('你推门而入，屋里漆黑一片，除了坐落在你面前的一座巨大的机器发着微弱的白光。这是什么样的大机器啊！在为数不多的光照下，机器复杂的线路结构与管道映入眼帘，无数个巨大的显示屏在你面前闪动。')
                            
                            output('这时，响声传来，机器似乎震动了一下，突然，你意识到机器前面有一个人！')
                            
                            print('那个人显然注意到了你，向你走来，你感到很害怕，但随即一个熟悉的声音传来：')
                            t.sleep(0.2)
                            output('"别怕，是我。"')
                            
                            output('星空出现在你的面前。')
                            
                            output('过了一会儿，星空面向你，对你说：“这，就是渗透机器，机票的核心装置。它是我们共同制造的，但自从半年前一位策划失踪了后，我们就再也无法通过这机器与外界取得联系了。我们只能靠9Y进行一些修补工作，当然，这机器还算正常，不像……')
                            
                            output('突然，你听到一声巨响，周围警报声迭起，无数显示屏变成了凶恶的红光。')
                            
                            output('你不知道发生了什么，吓得呆站在原地。')
                            
                            output('星空大声喊道：“坐标3.3异常！机器超负荷运作，冷却系统失灵！Zero快去把门打开，我们还有救！')
                            
                            output('你跑去门前，但门竟然打不开！')
                            
                            output('“我的天！完蛋了，这机器的牵连系统是……”星空吼道。')
                            
                            output('一阵刺眼白光把你们包围，你在失去知觉前，听到了星空最后的话：')
                            
                            output('“传送机器啊！！”')
                            
                        if choose == 'C':
                            output('你原路返回')
                            
                if choose == 'C' and walkC == 1:
                    output('不幸的是,已经逛过这里了')
                    
                    continue
                if choose == 'C' and chooseA == 1:
                    output('你随便转了转，发现了一家超市，超市里人员密集。')
                    choose = 'C'
                    
                if choose == 'C' and chooseA == 0:
                    chooseA = 1
                if choose == 'C':
                    output('你走到一个角落，这时，一个声音从你身后传来：“啊哈，这不是新来的那个小鬼吗！”')
                    
                    output('你转头看了看身后，一个穿着黑色风衣的人轻蔑地看向你，他抓住了你的手，恶狠狠地说：“哈，小鬼，最好给我乖点，惹毛了我就要你好看！”')
                    
                    output('虽然这是在公共场合，但周围的噪音太多了，基本上没人注意你们俩。')
                    
                    output('“呃……小黑，你没必要这么对一个新人吧，她看起来没有威胁啊。”一个站在黑风衣人旁边的，身穿花白色衣服的人说道，脸上的表情很无奈。')
                    #有关我现在才知道主角是个女生这件事(
                    
                    output('“哈，中烧，你根本就不懂！装模作样的故作柔弱的人最让我讨厌了！快滚吧！”')
                    
                    output('你不想和他们杠下去，离开了商店')
                    
                    walkC = 1
                if choose == 'D':
                    walkD = 1
                    output('你漫无目的地转了转，在大厅尽头发现了一道楼梯门。你走了进去，里面光照十分充足。')
                    
                    output('楼梯既有通往楼上的，也有去地下室的')
                    
                    output('你会：A：去楼上,B：去地下室,C：离开')
                    
                    while choose not in {'A','B','C'}:
                        print('请做出你的选择')
                        output('你会：A：去楼上,B：去地下室,C：离开')
                        
                    else:
                        if choose == 'A':
                            output('你去了楼上')
                            
                        if choose == 'B':
                            output('你下楼，发现楼下有一道锁着的铁门，隔着铁门你看见了一个满是灰尘的机器，你还是上了楼')
                            
                        if choose == 'C':
                            output('你离开了')
                            
                            continue
                        output('你到了楼上，发现这里是一个露天平台，你向远处眺望，发现这是一个精致的小镇，有人悠闲地漫步在镇上。小镇外面是一片稻田，不过现在似乎还不是收获的季节，只有青翠的连绵一片。更远处是一片大森林，在这个季节里格外茂盛，可惜你只能看到一片深绿色。')
                if choose == 'E':
                    output('可笑的是，你不知道它在哪【你 傻 了】')
                    #你 傻 了
                    output('不过你还是决定去找找')
                    #《找找》
                    
                    walkE = 1

                #棉花糖：你们是完全没有写废弃小店吗（（
                #当然，这是end以后可能用到的神奇道具（
                    
        #冒险路线好耶!
        #这应该是山丘线(
        output('再次睁开双眼时，你发现自己躺在地上，好在你恢复得很快，随即站起了身来,你站在一个类似于山顶的地方，脚下是黄色的土地，周围一棵树也没有。向山下看去，一片大森林包围了你。')
        
        output('现在是白天，但气温异常的寒冷，你穿着不合身的短袖短裙，没有鞋袜——任凭呼啸的寒风吹过你的身体，但奇怪的是，你却一点凉意也没有。')
        
        output('周围时不时传来尖啸声，是风声吗？')
        
        output('你会：A：向前走去,B：坐在原地等待救援,C：大声呼救')
        
        while choose not in {'A','B','C'}:
            print('请做出你的选择')
            output('你会：A：向前走去,B：坐在原地等待救援,C：大声呼救')
            
        else:
            if choose == 'A':
                output('你向前走去')
                
            if choose == 'B':
                output('你坐在原地，看着周围荒凉的景象，感觉十分害怕。你还是向前走了')
                
            if choose == 'C':
                output('你大声呼救，没有人来，不过好像听到了回声，但这浪费了体力，你还是向前走去[HP-5]')
                health -= 5
                dead_interface()
                if respawned == 1:
                    respawned = 0
                    continue
                
        output('你向前走，前面的路仍然一片黄色，死气沉沉，看不到一丝生机。')
        
        output('正当你精神恍惚之际，你听到脚下一阵响声，像是石头滚落的声音。')
        
        output('你向前迈出一步，突然脚下没有了陆地，你重心不稳跌了下去。')
        
        output('正在惊慌失措时，你看到旁边有一根藤蔓')
        
        output('你会：A：不管他,B：抓住,C：做好降落动作')
        
        while choose not in {'A','B','C'}:
            print('请做出你的选择')
            output('你会：A：不管他,B：抓住,C：做好降落动作')
        else:
            chooseb = 0
            if choose == 'A':
                chooseb = 1
                output('你不管他，似乎有点等死的感觉')
                
                vine = 0
            if choose == 'B':
                chooseb = 1
                output('你抓住了藤蔓')
                
                vine = 1
            if choose == 'C':
                output('虽然空中调整身体姿势很困难，但你还是努力做好降落的动作，突然，周围射出两根长矛，你全部躲过了！')
                
            if chooseb == 1:
                print('周围突然凭空伸出许多长矛，它们将矛头对准了你，向你发射！（回复五个大写字母,规则如教程）')
                chanceb = 2
                while chanceb > 0:
                    if chanceb == 2:
                        choose = list(input('请输入你的第一次躲避方式'))
                    if chanceb == 1:
                        choose = list(input('请输入你的第二次躲避方式'))
                    chanceb -= 1
                    x = random.randint(1,4)
                    a = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    b = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    c = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    d = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    e = chr(ord('A') + x - 1)
                    enemy_fight = a+b+c+d+e
                    enemy_fighta = [a,b,c,d,e]
                    hurt = 0
                    hurtB = 0
                    chance = 0
                    wrong = 0
                    while wrong == 0:
                        wrong = 1
                        if len(choose) != 5:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[0] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[1] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[2] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[3] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[4] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    else:
                        while chance < 5:
                        #快悄悄这个地方,我把chance < 5写成了chance <= 5然后查了一天才查到这个bug
                        #悄悄改为瞧瞧,这是个错别字(划)通假字
                        #快看,这里我复制的前面
                            f = choose.pop()
                            g = enemy_fighta.pop()
                            if f == 'D' and g == 'C' or f == 'C' and g == 'B' or f == 'B' and g == 'A' or f == 'A' and g == 'D':
                                hurtB += 10
                                chance += 1
                            else:
                                chance += 1
                        if vine == 1:
                            hurtB /= 2
                            hurtB = int(hurtB)
                        health -= hurtB
                        input(f'长矛的进攻方式是{enemy_fight}')
                        input(f'你被扣除了{hurtB}点血量')
                        dead_interface()
                        if respawned == 1:
                            respawned = 0
                            continue
        output('你躲开长矛，降到地面，许多玫瑰接住了你，你受了刺伤[HP-20]，这里似乎不像玫瑰生长的地方。')
        health -= 20
        dead_interface()
        if respawned == 1:
            respawned = 0
            continue
        
        output('不管怎么样，你忍住痛从玫瑰上爬起来，拼命向前跑去，你看见四周掠过的景象。')
        
        output('这里黄色的地面依旧，不过周围出现了许多低矮的灌木，灰色的树丛间依然是沉闷的气息。')
        
        output('看到长矛似乎没有追来，便放慢了脚步，在一个岔路前停了下来')
        
        output('左右两条路简直一模一样。')
        output('你会：A：向左走,B：向右走')
        while choose not in {'A','B'}:
            print('请做出您的选择')
            output('你会：A：向左走,B：向右走')
        else:
            if choose == 'B':
                output('你向右走，很快就没有了道路，但你在四周的岩壁上看到了插进石缝里的一把长矛，你稍用力把它拔了出来（获得【友好长矛】）然后沿原路返回，向另一条路走去。')
                item.append('友好长矛')
                
                choose = 'A'
            if choose == 'A':
                output('你向左一直走，走到了一座山峰的脚下，这里已经可以见到高大的树丛了，你继续向前走去。')
        output('这是一条很陡的下坡路，碎石遍布，把你的脚扎出了血。')
        
        output('花了很长一段时间的下坡，你来到了一座村庄前面，周围是用石砖堆积成的建筑，放眼望去一片死气沉沉，肯定已经废弃许久了。')
        
        output('一个花盆里栽种的玫瑰吸引了你的注意，但你想先在树下休息一下。')
        
        output('你会：A：看玫瑰,B：去树下,C：看看村庄,D：向前走')
        
        while choose not in {'A','B','C','D'}:
            print('请做出您的选择')
            output('你会：A：看玫瑰,B：去树下,C：看看村庄,D：向前走')
            
        else:
            if choose == 'A':
                output('你看了看玫瑰，突然，尖刺向你戳来。[HP-10]）')
                health -= 10
                dead_interface()
                if respawned == 1:
                    respawned = 0
                    continue
                
            if choose == 'B':
                output('你去树下休息了一会儿[HP+20]')
                health += 20
                if health >= 100:
                    health = 100
            if choose == 'C':
                output('你看了看村庄，没有找到有用的信息')
                
            if choose == 'D':
                output('你向前走去')
        output('你加快速度向前走，突然，一道刺眼的闪光划过天际，你被吓了一跳。')
        
        output('就在你不远处，一个黑影站在一块大石头上，你似乎听到了怪异的笑声。')
        
        output('你想好好看看黑影是谁，突然，地面剧烈摇晃着，你发现从村庄到你这儿的路塌陷了下去，前面是高大的断崖，你被困在了死路里！')
        
        output('正当你盯着岩层看时，你听到了周边风呼啸吹过的声音，转身一看，长矛又对准了你！')
        
        output('你想跑，两腿却发软跌倒在地上，好在躲过了一批朝你射来的长矛，可转过身来，又是一批长矛！')
        
        choose = list(input('请选择你的躲避方式!'))
        x = random.randint(1,4)
        if x == 1:
            a = 'A'
        if x == 2:
            a = 'B'
        if x == 3:
            a = 'C'
        if x == 4:
            a = 'D'
        x = random.randint(1,4)
        if x == 1:
            b = 'A'
        if x == 2:
            b = 'B'
        if x == 3:
            b = 'C'
        if x == 4:
            b = 'D'
        x = random.randint(1,4)
        if x == 1:
            c = 'A'
        if x == 2:
            c = 'B'
        if x == 3:
            c = 'C'
        if x == 4:
            c = 'D'
        x = random.randint(1,4)
        if x == 1:
            d = 'A'
        if x == 2:
            d = 'B'
        if x == 3:
            d = 'C'
        if x == 4:
            d = 'D'
        x = random.randint(1,4)
        if x == 1:
            e = 'A'
        if x == 2:
            e = 'B'
        if x == 3:
            e = 'C'
        if x == 4:
            e = 'D'
        enemy_fight = a+b+c+d+e
        enemy_fighta = [a,b,c,d,e]
        hurt = 0
        hurtB = 0
        chance = 0
        wrong = 0
        while wrong == 0:
            wrong = 1
            if len(choose) != 5:
                wrong = 0
                print('输入错误,请依照格式输入!')
                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
            elif choose[0] not in {'A','B','C','D'}:
                wrong = 0
                print('输入错误,请依照格式输入!')
                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
            elif choose[1] not in {'A','B','C','D'}:
                wrong = 0
                print('输入错误,请依照格式输入!')
                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
            elif choose[2] not in {'A','B','C','D'}:
                wrong = 0
                print('输入错误,请依照格式输入!')
                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
            elif choose[3] not in {'A','B','C','D'}:
                wrong = 0
                print('输入错误,请依照格式输入!')
                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
            elif choose[4] not in {'A','B','C','D'}:
                wrong = 0
                print('输入错误,请依照格式输入!')
                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
        else:
            while chance < 5:
                f = choose.pop()
                g = enemy_fighta.pop()
                if f == 'D' and g == 'C' or f == 'C' and g == 'B' or f == 'B' and g == 'A' or f == 'A' and g == 'D':
                    hurtB += 10
                    chance += 1
                else:
                    chance += 1
            health -= hurtB
            output(f'长矛的进攻方式是{enemy_fight}')
            output(f'你被扣除了{hurtB}点血量')
            dead_interface()
            if respawned == 1:
                respawned = 0
                continue
        output('你躲过了这一批长矛，更多的长矛又向你轮番袭来！')
        
        output('再这样下去不是办法。')
        
        output('你会：A：继续躲避,B：跳崖,C：借助石头抵挡')
        
        while choose not in {'A','B','C'}:
            print('请做出您的选择')
            output('你会：A：继续躲避,B：跳崖,C：借助石头抵挡')
            
        else:
            if choose == 'A':
                output('你继续躲避着长矛，突然，长矛在空中用空气动力学完全无法解释的动作旋转了90度，横劈了过来！你被推下了悬崖。')
                
            if choose == 'B':
                output('你跳下了悬崖')
                
            if choose == 'C':
                output('你想跑到石头后面，突然一批长矛袭来，你被击中了[HP-10]，你跌下悬崖。')
                health -= 10
                dead_interface()
                if respawned == 1:
                    respawned = 0
                    continue
                
        output('伴随着呼啸声，你迎着深渊掉下去。')
        output('一阵刺痛传来，你失去了知觉。')
        output('当你再睁开眼时，放心自己依然落在一片玫瑰丛上方，你抬头看去，上面是一眼看不到尽头的山体。从这么高的地方摔下来还没死，你感到奇怪，并没有任何庆幸的感觉。        再看看你自己，虽然没有死，但从头到脚全身是伤，好在都不算重，却仍然刺痛万分。你的衣物如同带有无数道缝隙的破布一般披在身上，看起来很快就要分崩离析。看着这花丛，不知为何，你似乎有一种奇怪但说不出来的熟悉感。')
        output('你降落在一片森林里，到处都是高大的林木与低矮的灌木，遮住了阳光，使前方的空间显得阴暗恐怖，更重要的是，这里一点人类活动的迹象都没有。')
        output('你想起身，但刚移动身体，一阵剧痛遍如风一般穿过。')
        output('你会：A：躺下,B：站起来,C：呼救')
        forest = 0
        while choose not in {'A','B','C'}:
            print('请做出您的选择')
            output('你会：A：躺下,B：站起来,C：呼救')
        else:
            if choose == 'A':
                output('你躺下身体昏睡过去')
            elif choose == 'B':
                output('你站起来走动')
                forest = 1
            elif choose == 'C':
                output('你大声呼救，并没有什么用，你最后体力不支昏了过去')  
        if forest == 0:
            output('不知过了多久，你再次醒来，你仍然躺在玫瑰丛上。')
            output('你站起身，感觉好了一些。')
            output('突然，那道熟悉的闪光再次划过天空，随即传来呼呼的风声。')
            output('你看了看四周，寂静一片，什么都没有。')
            output('你会：A：逃跑,B：观察')
            while choose not in {'A','B'}:
                print('请做出您的选择')
                output('你会：A：逃跑,B：观察')
            else:
                if choose == 'A':
                    output('你逃跑了')  
                elif choose == 'B':
                    output('你待在原地，突然你发现旁边有个白白的东西，是一张便条，上面写着，“向前走。”你便起身走去。') 
            output('向前行进了一段距离，你发现前方杂乱的树木挡住了道路。')
            
            output('你仔细看了看旁边，没有发现有用的东西。')
            
            output('这时，一声微弱的尖啸从密林深处传来，似乎像撕纸的声音。')
            
            output('你再环顾四周，吓了一跳：一条黑色的蛇盘绕在树上，似乎在向你逼近。')
            
            output('你会：A：向前跑,B：寻找尖啸声源,C：观察那条蛇')
            
            while choose not in {'A','B','C'}:
                print('请做出您的选择')
                output('你会：A：向前跑,B：寻找尖啸声源,C：观察那条蛇')
                
            else:
                if choose == 'A':
                    output('你向前跑去，可是树木太多划伤了你[HP-5]')
                    health -= 5
                    dead_interface()
                    if respawned == 1:
                        respawned = 0
                        continue
                    
                elif choose == 'B':
                    output('你顺着声音慢慢走去')
                    
                    forest = 1
                elif choose == 'C':
                    output('你看着那条蛇，突然，它从树上掉了下来，一动不动，你壮胆接近了它，发现它身上插着一条长矛，你赶快向前走开')
                    
                output('你向密林深处逼近，一路上扒开树枝和灌木丛，然而带刺的植物实在太多，你磕磕碰碰，终于到了一块开阔的地方。')
                
                output('这里被苍天大树笼罩着，四处似乎没有阳光，只有微弱的光线照射进来，你感觉有点奇怪。')
                
        if forest == 1:
            output('这时，你的前面出现了一条黑色的短裙、短袖，')
            
            output('看着你身上近乎破布般的衣物，你便换上了这套装束。')
            
        output('你继续往前走，穿过灌木丛组成的狭窄空间后，来到了一片巨大的空地。')
        
        output('出现在你前面的是一座像庙宇一样的建筑，由一座低矮的石头底座，四角那四根向上的横杆组成，看起来已经废弃许久。底座有楼梯通向建筑的平台。')
        
        output('你来到楼梯前，楼梯十分破旧，裂缝遍布，上面还有藤蔓。')
        
        output('突然一阵异样感袭来，你似乎听到呼呼的风声，抬头一看，又是成片的长矛横在你上空！')
        
        choose = list(input('回复三个大写字母以躲避!'))
        while len(choose) != 3:
            print('请依照格式输入!')
            choose = list(input('回复三个大写字母以躲避!'))
        else:
            output('这些长矛并没有像你预想的一样向你冲来，而是围成了一个笼子把你关了起来！')
            
            output('随着你完全困在笼子里之时，笼子极速上升，你被拖出地面。过了一段时间，你降落在建筑的平台上方，长矛随即散开了。')
            
            output('你环顾四周，前面只有一个长方体石台，除此之外空空荡荡的，什么也没有。')
            
            output('正当你想向前看看石台时，一声尖啸传来，石台前方出现了一个穿着灰色装甲的人，那人的身型在你的脑海里与黑影重合。')
            
            output('“啊哈！看这是什么好东西！”那人尖锐的声音传来，你承认你被吓了一跳。')
            
            output('那人走上跟前，对你说：')
            
            output('“天呐，送到门前的礼物啊！这下罗尔斯大人一定会高兴到炸……啊哈，根据规则他不允许爆炸的！”')
            
            output('“Zero，你一定不知道我是谁对吧，我的称号是CRD，是罗尔斯大人的秘书，但你不需要知道这个。我只是想让你知道，我会把你胖揍一顿，然后活捉给罗尔斯大人，他喜欢吃鲜美的玩意儿！啊，别激动，我不是食人族，只是个修辞手法罢了，为什么人们都对玩笑这么认真呢！”')
            
            output('“所以现在，乖乖站好，让我揍扁你吧！”')
            
            output('CRD对你发出恐怖的笑声')
            
            output('你会：A：站好,B：逃跑')
            
            while choose not in {'A','B'}:
                print('请做出您的选择')
                output('你会：A：站好,B：逃跑')
                
            else:
                if choose == 'A':
                    output('你站在原地，目视CRD逼近')
                    
                if choose == 'B':
                    output('你刚要跑，CRD大笑：“啊哈，多淘气的小……为什么没人听得懂我的话呢！”一根长矛把你戳了回去[HP-10]')
                    health -= 10
                    dead_interface()
                    if respawned == 1:
                        respawned = 0
                        continue
                    
        output('就在这时，一道黑影从天空降下，横在CRD前面，一道奇异的光束发出，CRD被逼退了几步。')
        
        output('“什么！你是怎么跑出来的！”CRD大叫')
        
        output('前面的黑影站起来面向CRD，你看清楚了他就是星空！')
        
        output('“你那长矛对我没有半点作用，快走开吧！让我们见见你那位大人！”星空喊道')
        
        output('“这句话应该是我说的！规则表明我才是阻止你们的人！”CRD发怒了，朝你们进攻。')
        
        output('星空拉住你的手：“别怕，我们一起上！”')
        
        print('战斗开始')
        t.sleep(0.5)
        CRD = 150
        magic_point = 0
        win = 0
        a,b,c,d,e = '','','','',''
        while win == 0:
            magic_choose = 0
            item_att = 0
            att_choose = 0
            item_choose = 0
            while magic_choose == 0 and item_choose == 0:
                chooseb = 'A'
                print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health},CRD血量为{CRD}')
                choose = input('A,物品B,防御C,魔法D,跳过')
                while choose not in {'A','B','C','D'}:
                    print('请做出你的选择')
                    choose = input('A,物品B,防御C,魔法D,跳过')
                if choose == 'A':
                    choose = input(f'你现在可使用的物品有{fight_item},请从1开始输入序号以选择使用的物品')
                    if choose not in {'1','2','3','4','5','6','7','8','9','10'}:
                        choose = input('物品序号输入错误!')
                    else:
                        choose = int(choose)
                        if choose > len(fight_item):
                            choose = input('物品序号输入错误!')
                        else:
                            choose -= 1
                            check = fight_item[choose]
                            item_find()
                            if check in fight_item and check in item:
                                item.remove(check)
                                fight_item.remove(check)
                        if health > 240:
                            health = 240

                if choose == 'B':
                    choose = input('你选择了防御!')
                    magic_point += 40
                    magic_choose = 1
                    if magic_point >= 100:
                        magic_point = 100
                    chooseb = 'B'
                if choose == 'C':
                    choose = input(f'A：治疗魔法（{health_point}）B：战斗魔法（70）C：黑暗魔法（？）')
                    while choose not in {'A','B','C'}:
                        print('请做出你的选择')
                        choose = input(f'A：治疗魔法（{health_point}）B：战斗魔法（70）C：黑暗魔法（？）')
                    else:
                        if choose == 'A':
                            if magic_point < health_point:
                                choose = input('你的魔法值不够!')
                                magic_choose = 0
                            if magic_point >= health_point:
                                choose = input(f'你使用了治疗法术!你的血量回复了{health_plus}点!')
                                health += health_plus
                                magic_choose = 1
                                magic_point -= health_point
                            if health > 240:
                                health = 240
                                magic_choose = 1
                        if choose == 'B':
                            if magic_point < 70:
                                choose = input('你的魔法值不够!')
                                magic_choose = 0
                            if magic_point >= 70:
                                choose = input('你使用了战斗法术!你的攻击提高了5点,持续一回合!')
                                att_choose = 1
                                magic_choose = 1
                                magic_point -= 70
                        if choose == 'C':
                            choose = input('l͓̩̫̘͙͔̯͖̟̤̓͊̑̌́̂̆̚ò̥̪̭̱̰̝̒͂̄͋̿̏͆́̚c͍̲͇͚̖̬͈̪͙̳͌̉́̃k̪̥̱̝̱̑̈́̏̽͗̊̈́͂̀̍e̞͎̩̜̱̩͚̤̊͌̀̀d̠̖̞̝̙̪̟̞̐͛̈̊̀͂̄͌̓̏͌̓ͅ')
                            magic_choose = 0
                        choose = 0
                if choose == 'D':
                    choose = input('你跳过了你的回合')
                    magic_choose = 1
            x = random.randint(1,4)
            a = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            b = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            c = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            d = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            e = chr(ord('A') + x - 1)
            enemy_fight = a+b+c+d+e
            enemy_fighta = [a,b,c,d,e]
            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
            hurt = 0
            hurtB = 0
            chance = 0
            wrong = 0
            while wrong == 0:
                wrong = 1
                if len(choose) != 5:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                elif choose[0] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                elif choose[1] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                elif choose[2] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                elif choose[3] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                elif choose[4] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
            else:
                CRD_act = random.randint(1,10)
                while chance < 5:
                    f = choose.pop()
                    g = enemy_fighta.pop()
                    if chooseb != 'B':
                        if f == 'A' and g == 'B' or f == 'B' and g == 'C' or f == 'C' and g == 'D' or f == 'D' and g == 'A':
                            hurt += att
                            chance += 1
                            if att_choose == 1:
                                hurt += 5
                            if CRD_act > 7:
                                hurt -= 5
                    if f == 'D' and g == 'C' or f == 'C' and g == 'B' or f == 'B' and g == 'A' or f == 'A' and g == 'D':
                        hurtB += 10
                        if chooseb == 'B':
                            hurtB -= Def
                            if Def >= 10:
                                hurtB = 0
                        chance += 1
                    else:
                        chance += 1
                CRD -= hurt
                health -= hurtB
                choose = input(f'敌方的攻击是{enemy_fight}')
                if CRD_act > 7 :
                    choose = input('CRD使用了防御!')
                if chooseb != 'B':
                    choose = input(f'你对敌方造成了{hurt}点伤害!')
                    hurt = 0
                if chooseb == 'B':
                    choose = input('因为你选择了防御,所以伤害不计入')
                if CRD_act <= 7:
                    choose = input('星空对CRD造成了20点伤害!')
                    CRD -= 20
                if CRD_act > 7:
                    choose = input('星空对CRD造成了15点伤害!')
                    CRD -= 15
                choose = input(f'你被敌人扣除了{hurtB}点血')
                dead_interface()
                if respawned == 1:
                    break
                hurtB = 0
                att_choose = 0
            if CRD <= 0:
                choose = input('您获胜了!')
                win = 1
        if respawned == 1:
            respawned = 0
            continue
        output('CRD喊道：“什么？你们战胜了我？那我只好……加入你们了。”')
        output('星空：“什么？！”')
        output('“骗你们的！嘿嘿，咱们下次再会！”CRD说着突然凭空消失了。')
        output('星空面向你，无奈的说：“咱们下次再找他吧。刚才我被他抓住时，我看到前面的山脚好像有个隧道，似乎还有矿车声，我们可以借此离开这里，我们走吧。”')
        output('他再看了看你')
        if health >= 240:
            output('星空：“我的天，Zero，你没事吧，你看起来一点伤都没受呢，真好！”')
            output('星空顿了顿，嘟囔道：“穿这么少不冷吗……”')
        else:
            output('星空：“天呐，Zero，你受伤了，我来给你治疗一下吧。”')
            output('他看向你，你发现你身上的伤都消失了，衣服也变完整了。[HPmax]')
            health = 240
            view_status()
        output('星空对你说：“总之，我们走吧！你来带头！”')
        output('你会：A：看石台,B：向前走')
        while choose not in {'A','B'}:
            print('请做出您的选择')
            output('你会：A：看石台,B：向前走')
        else:
            if choose == 'A':
                if '黑色短裙' in item or '黑色短裙' in armor:
                    output('你看了看石台，突然，黑色的光束传来，石台上多了一把奇形怪状的尖锐物,你获得了【黑暗之剑】')
                    item.append('黑暗之剑')
                    output('星空：“这是什么？我们还是赶路吧。”')
                else:
                    output('石台上有许多你看不懂的古代文字')
            if choose == 'B':
                output('你向前走')
        output('你们向前走去，穿过一层层树林，你们来到了一座岩壁底下，前面是一扇门。门没有锁，星空打开了门，是一个漆黑的隧道。')
        output('“让你看看这个！”星空说着，手上亮出一个发着强光的物体，照亮了整个隧道。')
        output('“这是几何八面体，它可以放出魔法光束，我们走吧。”')
        output('借着光线，你看到隧道的岩壁画满了奇形怪状的涂鸦，你不知道这是什么意思，但隐约可以看到CRD的轮廓以及“规则”几个大字。')
        output('你继续向前走，发现一个铁轨横在眼前，上面是个矿车。')
        output('星空说：“这个矿车应该可以送我们去别的地方，我们走吧。”')
        output('你想上前，但突然想到了之前的经历，你害怕有机关。')
        output('你会：A：上车,B：查看机关,C：跳上铁轨')
        while choose not in {'A','B','C'}:
            print('请做出你的选择')
            output('你会：A：上车,B：查看机关,C：跳上铁轨')
        else:
            if choose == 'A':
                output('你们上了车，突然，矿车自动启动了。')
            if choose == 'B':
                choose = input('你查看四周，没看到什么有用的东西，突然你找到了一张小卡片你获得了【占位卡】')
                item.append('占位卡')
                view_status()
            if choose == 'C':
                print('你跳上铁轨，这时矿车突然向你开来把你压扁了，伴随着一阵尖叫声')
                t.sleep(0.2)
                print('（划）')
                t.sleep(0.2)
                output('只是个涂鸦罢了！没什么特别的，你还是上了车，突然，矿车自动启动了。')
        output('你们乘着矿车向前行进。一路上你们什么话也没说。')
        output('突然，车身向前倾倒，进行了个急刹车。前面是个像废弃的月台一样的地方。你们下了车，前面是一扇门。')
        output('“不管以后要发生什么，我们新的冒险开始了。”星空打开门。')
        output('一道耀眼的光芒射门厅，你们的前方出现了一条黄色的路面，与山丘上不同，路面十分整洁。')
        output('你踏上了这条路。')
        #几何平原!
        #这块剧情好复杂(
        #即使复杂也不能忘了伟大的view_status()啊
        output('随着你们不断向前，一片金黄色的平原展现在了眼前，路的两边都是黄澄澄的柱子，由好几个斜方块连接而成，看上去十分可爱。')
        output('你们前面是个十字路口，旁边还站着一个身穿棕色棉衣的人。')
        output('你放眼望去，左边是一片金灿灿的稻田，右边是一片水塘，前方远处是低矮的丘陵。')
        chooseb = 'A'
        while chooseb != 'B':
            choose = input('你会：A：向前走,B：向左走,C：向右走,D：向人问路')
            chooseb = choose
            while choose not in {'A','B','C','D'}:
                print('请做出你的选择')
                choose = input('你会：A：向前走,B：向左走,C：向右走,D：向人问路')
                chooseb = choose
                view_status()
            else:
                if choose == 'A':
                    output('你向前走，一片低矮的小方块灌木在风中旋转着，挡住了去路')
                if choose == 'B':
                    output('你向左走')
                if choose == 'C':
                    output('你向右走，水塘里面许多白色的水花在跳动')
                    #这里end在编剧请时没写水花二字，特此留念（
                if choose == 'D':
                    output('那人说：“你们是新来这里的吗？这里是几何平原，我觉得你们可以向前去丘陵逛逛，那里适合露营。”')
        output('你沿着一条小路，穿过了许多多面体组成的林地，来到一片开阔地带。')
        output('这时前面有个路牌。')
        output('你会：A：读路牌,B：不读')
        while choose not in {'A','B'}:
            print('请做出你的选择')
            output('你会：A：读路牌,B：不读')
        else:
            if choose == 'A':
                output('你准备读路牌，这时天空一声巨响！从地里钻出来了一个凶神恶煞的方块，向你进攻了！')
                fight('几何六面体',70,10,10,10,random.randint(10,50),'normal')
                if respawned == 1:
                    respawned = 0
                    continue
                choose = input('你获得了【流油果】!')
                item.append('流油果')
                view_status()
                fight_item.append('流油果')
            if choose == 'B':
                output('你不读路牌，向前走去')
        output('你继续前进，穿过了许多低矮的四面体草丛，来到了一条小河边。')
        output('“看来我们要过去，可是怎么通过它呢？”星空说。')
        output('你看了看小河，发现河里许多白色浪花在跳动。')
        output('突然，这些浪花有规律地翻转起来，组成了一条小桥，你们正想通过，发现小桥又翻了一个面，组成了一座新桥。')
        output('你看了看河边，发现一个标牌，上面写道：“翻转地板：当你想过河时，有ABC三种道路可走，选一种吧，有两条道路让你通过。')
        output('如果摔下去了，就重来吧。”')
        go = 0
        while go == 0:
            output('回复A,B,C三个字母中的一个以上桥，翻转地板随机组成两座真桥，如果过不去要从新输入字母')
            while choose not in {'A','B','C'}:
                print('格式错误!')
                output('回复A,B,C三个字母中的一个以上桥，翻转地板随机组成两座真桥，如果过不去要从新输入字母')
            bridge = random.randint(1,3)
            if bridge == 1:
                bridge = 'AB'
            if bridge == 2:
                bridge = 'BC'
            if bridge == 3:
                bridge = 'AC'
            bridge = list(bridge)
            if choose in bridge:
                output('你通过了桥！')
                go = 1
            else:
                output(f'翻转地板组成了桥{bridge},你没通过桥！')
        output('通过了翻转地板的河流，你们走上了一片大田野，田野上泥泞不堪，不过因为你没有穿鞋，所以并没有感到很不舒服。')
        output('你看到田野里面种着各色作物，有细小的三棱柱形草，还有球形的果子。')
        output('你会：A：继续前进,B：摘一点草,C：摘一点果子')
        while choose not in {'A','B','C'}:
            print('请做出你的选择')
            output('你会：A：继续前进,B：摘一点草,C：摘一点果子')
        else:
            cube_fight = 0
            if choose == 'A':
                output('你们继续前进')
            elif choose == 'B':
                cube_fight = 1
                output('你摘了些草，星空有些尴尬：“这算偷盗吧……”')
                output('“当然了！”一个愤怒的声音传来，你发现一个方块从地里钻出来，朝你们攻击！')
            elif choose == 'C':
                cube_fight = 2
                output('你摘了些果子，星空有些尴尬：“这算偷盗吧……”')
                output('“当然了！”一个愤怒的声音传来，你发现一个方块从地里钻出来，朝你们攻击！')
            if cube_fight != 0:
                fight('几何六面体',70,10,10,10,random.randint(10,50),'normal')
                if respawned == 1:
                    respawned = 0
                    break
            if cube_fight == 2:
                output('你获得了【流油果】')
                item.append('流油果')
                fight_item.append('流油果')
            if cube_fight == 1:
                output('你获得了【杆草】')
                item.append('杆草')
                fight_item.append('杆草')
        output('穿过了金黄的田野，远处的丘陵离你们近了一点。')
        output('你们来到了一座厚实的泥土平台上，你想在这里歇一歇。')
        output('平台上有几个干完农活歇息的方块，旁边是小河。')
        chooseA = 0
        while chooseA == 0:
            choose = input('你会：A：去与方块交谈,B：坐着休息,C：去河边')
            while choose not in {'A','B','C'}:
                print('请做出你的选择')
                output('你会：A：去与方块交谈,B：坐着休息,C：去河边')
            else:
                if choose == 'A':
                    output('你们和方块交谈，方块们告诉你这是他们自由耕种的土地，粮食只有很少一部分对外销售。不过最近有一个新统治者加大了好多田租，现在他们的情况十分窘迫')
                if choose == 'B':
                    output('你们坐着休息了一会儿')
                if choose == 'C':
                    output('你们去了河边，河水很轻，但是十分凉，使你放弃了下河游泳的念头。')
                    chooseA = 1
        choose = input('突然，河的中央又升起了一座翻转地板桥。')
        choose = input('“又来了，咱们走吧。”星空拉住你的手说。')
        #在嗑了在嗑了(划)
        choose = input('你心里突然升起了一阵异样的感觉，不过转念一想，可能是你多虑了。')
        go = 0
        while go == 0:
            output('回复A,B,C三个字母中的一个以上桥')
            while choose not in {'A','B','C'}:
                print('格式错误!')
                output('回复A,B,C三个字母中的一个以上桥，翻转地板随机组成两座真桥，如果过不去要从新输入字母')
            bridge = random.randint(1,3)
            if bridge == 1:
                bridge = 'AB'
            if bridge == 2:
                bridge = 'BC'
            if bridge == 3:
                bridge = 'AC'
            bridge = list(bridge)
            if choose in bridge:
                output('你通过了桥！')
                go = 1
            else:
                output(f'翻转地板组成了桥{bridge},你没通过桥！')
        output('你们通过河流，前面放着许多正方体杆草块，挡住了去路。')
        output('“看来我们要过去。”星空说。')
        output('正当你们爬上杆草块时，一个圆柱挤了过来，大声喊道：“这是我的粮食！你们别碰！”')
        #end先生在线教你认识几何图形(
        output('星空解释道：“我们不是想拿……”')
        output('“我不管，你们要过去，就先击败我再说！”')
        fight('圆柱',100,5,20,30,random.randint(8,70),'normal')
        if respawned == 1:
            respawned = 0
            break
        output('圆柱说道：“你们能击败我？好厉害好厉害！过去吧！”说完滚走了。')
        # 活 泼 好 动 几 何 人
        output('你们上了杆草块，发现前面是个小村庄。村庄的格局不禁让你想起了山丘上的那个，不过没那么死气沉沉。')
        output('你们翻下杆草块，向前走去。')
        output('过了一会儿，你们来到了小村庄的门口，许多方块小贩在路上卖东西，不过你们的钱都不够。')
        output('进入村庄后，呈现在眼前的是一座座小房子，看起来都是民居，只有一个写着“商店”字样的牌子挂着。')
        output('你们的左边是一片麦田，右边似乎是一个广场。')
        choose = input('你的HP回满了![HPmax]')
        health = 240
        view_status
        farm = 0
        walkD = 0
        skirt = 0
        spearS = 0
        while farm == 0:
        #这段代码很乱(
            output('你会：A：继续前进,B：去商店,C：去麦田,D：去广场')
            while choose not in {'A','B','C','D'}:
                print('请做出你的选择')
                output('你会：A：继续前进,B：去商店,C：去麦田,D：去广场')
            else:
                if choose == 'A':
                    output('如果继续前进，你将离开村庄')
                    output('确定继续前进吗：A：继续前进,B：回到村庄')
                    while choose not in {'A','B'}:
                        print('请做出你的选择')
                        output('确定继续前进吗：A：继续前进,B：回到村庄')
                    else:
                        if choose == 'A':
                            output('你继续前进')
                            farm = 1
                        if choose == 'B':
                            output('你回到村庄')
                if choose == 'B':
                    output('你去商店')
                    shop = 0
                    while shop == 0:
                        choose = input('请选择需要购买的物品：A：杆草【10CM币】,B：流油果【30CM币】,C：短矛【50CM币】,D：翻转裙【100CM币】,E：离开商店')
                        while choose not in {'A','B','C','D','E'}:
                            print('请做出您的选择')
                            choose = input('请选择需要购买的物品：A：杆草【10CM币】,B：流油果【30CM币】,C：短矛【50CM币】,D：翻转裙【100CM币】,E：离开商店')
                        else:
                            money = 0
                            buy = 0
                            if choose == 'A':
                                if CM < 10:
                                    choose = input('你的CM币不够!')
                                else:
                                    buy = '杆草'
                                    money = 10
                            if choose == 'B':
                                if CM < 30:
                                    choose = input('你的CM币不够!')
                                else:
                                    buy = '流油果'
                                    money = 30
                            if choose == 'C':
                                if CM < 50:
                                    choose = input('你的CM币不够!')
                                else:
                                    buy = '短矛'
                                    money = 50
                            if choose == 'D':
                                if CM < 100:
                                    choose = input('你的CM币不够!')
                                else:
                                    buy = '翻转裙'
                                    money = 100
                            if len(item) >= 10 and buy != 0:
                                view_status()
                            if s('短矛' in item or weapon == '短矛') and buy == '短矛':
                                buy = 0
                                choose = input('你已经购买了这个物品了!')
                            if ('翻转裙' in item or armor == '翻转裙') and buy == '翻转裙':
                                buy = 0
                                choose = input('你已经购买这个物品了!')
                            if buy != 0:
                                item.append(buy)
                                if buy in {'杆草','流油果'}:
                                    fight_item.append(buy)
                                if buy == '翻转裙':
                                    skirt = 1
                                if buy == '短矛':
                                    spearS = 1
                                choose = input(f'你购买了{buy}!')
                                buy = 0
                                CM -= money
                            shop = 1
                if choose == 'C':
                    output('你来到了田野旁边，这里有个方块在散步，你们和他交谈。')
                    output('你要交谈什么：A：平原,B：居民,C：统治者,D：离开')
                    while choose not in {'A','B','C','D'}:
                        print('请做出您的选择')
                        output('你要交谈什么：A：平原,B：居民,C：统治者,D：离开')
                    else:
                        if choose == 'A':
                            output('他答道：“这片平原叫做【几何平原】，我们中的大多数人一直生活在这里，有一部分人去到了外地。前面是一片小丘陵，丘陵的尽头是远古遗迹，好像是旧王国的废墟。遗迹的那边新建了一座城堡，这都是那些出去的人告诉我的。”')
                        if choose == 'B':
                            output('他回答：“我们这里的居民并不是你们说的【人类】，可以说是掌握了魔法的物体，在魔法体系中保持他们特有的形态。少部分会魔法的人类成为了我们的统治者。”')
                        if choose == 'C':
                            output('他答道：“统治者嘛……我只记得以前的统治者是扑克国王，后面一个入侵者摧毁了他的城堡，建立了新的城市。最近有个自称是他助手的烦人家伙一直来我们这搞什么‘民意调查’。哦？CRD？谢谢你告诉我他的名字。”')
                        if choose == 'D':
                            output('你离开了这里')
                if choose == 'D' and walkD == 0:
                    output('你来到了广场，上面有一个告示牌：“公共财物摆放处。”')
                    output('你仔细一看，下面还有个贴纸，写道：“拿，都可以拿！”')
                    output('告示牌的后面有个箱子')
                    output('拿东西吗？A：拿B：不拿')
                    while choose not in {'A','B'}:
                        print('请做出您的选择')
                        output('拿东西吗？A：拿B：不拿')
                    else:
                        if choose == 'A':
                            choose = input('你得到了50CM币！')
                            CM += 50
                            view_status()
                        if choose == 'B':
                            output('你离开了广场')
                        walkD = 1
                if choose == 'D' and walkD == 1:
                    output('不幸的是,已经去过这里了')
        output('你们离开了小村庄，继续往前走去。')
        output('过了一会儿，前面又出现了一条大河挡住了道路。')
        output('“你们是新来的人类吧？这是最后一条河了，前面就是丘陵了。”一个在路边玩耍的四面体看到了你们，大声说。')
        go = 0
        while go < 2:
            output('回复A,B,C三个字母中的一个以上桥，翻转地板随机组成两座真桥，如果过不去要从新输入字母')
            while choose not in {'A','B','C'}:
                print('格式错误!')
                output('回复A,B,C三个字母中的一个以上桥，翻转地板随机组成两座真桥，如果过不去要从新输入字母')
            bridge = random.randint(1,3)
            if bridge == 1:
                bridge = 'AB'
            if bridge == 2:
                bridge = 'BC'
            if bridge == 3:
                bridge = 'AC'
            bridge = list(bridge)
            if choose in bridge:
                go += 1
                if go == 1:
                    output('你通过了第一座桥!')
                if go == 2:
                    output('你通过了第二座桥!')
            else:
                output(f'翻转地板组成了桥{bridge},你没通过桥！')
        output('你们从翻转地板上下来，向前走去，经过一条长长的大道，前面出现了一道大门，门后就是低矮起伏的丘陵了。')
        output('星空碰了碰大门，无奈地说：“打不开。”')
        output('“啊哈，当然打不开了！”一个声音从空中传来，突然，一个长矛飞插在地上。')
        output('CRD从长矛后面钻了出来，笑道：“此门可是我亲手关的，纵使你有千万力量，也无法动它分毫！”')
        output('星空想了想说：“那你能打开吗……”')
        output('“当然啦！”CRD不以为意，接着说：“现在，来尝尝我的‘超速矛矛雨流’吧！”')
        output('只听哐的一声，一大堆长矛从半空中俯冲下来，砸在了门上，门像玻璃摔碎一样化为碎片。')
        output('“我……放偏了！”CRD瞪着眼说道')
        output('星空：“现在我们可以过去了吗。”')
        output('CRD大声说：“当然不行！要过门，必过人！我的援兵，出来吧！”')
        output('一根长矛从天而降，横在了你们的面前。')
        output('“现在，向他们进攻！”CRD发出指示。')
        output('长矛向你们冲来')
        fight('长矛',150,15,10,30,50,'normal')
        if respawned == 1:
            respawned = 0
            break
        output('“这……我的援兵也不管用吗？？？可恶！可恶！可恶！！！弄坏了我的门，还没抓到人！我迟早有一天找你们算帐！”CRD说道，然后变了一堆长矛把自己抬走了。')
        output('“我们继续前进吧。”星空说。')
        output('你们通过了大门，来到了丘陵。路的两端一颗颗大树挺立着。')
        output('过了一会儿，道路在前方通向一片大草坪，旁边有个告示牌，似乎被安装在一个环形凸起上。')
        output('你会：A：向前走,B：看告示牌,C：看树')
        while choose not in {'A','B','C'}:
            print('请做出您的选择')
            output('你会：A：向前走,B：看告示牌,C：看树')
        else:
            if choose == 'A':
                output('你们向前走')
            if choose == 'B':
                output('你看告示牌，告示牌下面突然顶出一个滚轮，对你说：“CRD刚刚灰头土脸地过来了，不知道发生了什么，你们最好注意点。”然后钻了下去，告示牌也落下去了。你们向前走去。')
            if choose == 'C':
                output('你看了看树，树叶由复杂的分形图案组成……分形是什么啊')
                choose = input('树上有个箱子，你爬上去打开，发现是一个项链！你获得了【晶体项链】')
                item.append('晶体项链')
                view_status()
        output('你们走上草坪，草坪上面有一些帐篷，不过都很小，有几个方块在放风筝。')
        output('你们继续前进，星空停在了一道篱笆门前，说：“这是个迷宫！如果我们进去的话会发生什么呢？”')
        output('“你们会被我痛揍一顿！！！”突然天空传来一句话，CRD出现在你们面前。')
        output('“又来！”星空气愤地说。')
        output('“快进去，这迷宫是我专门为你们准备的！好好享受吧！”')
        output('星空看向你：“别进去，不要中计！”')
        output('你会：A：进去,B：不进')
        while choose not in {'A','B'}:
            print('请做出您的选择')
            output('你会：A：进去,B：不进')
        else:
            if choose == 'A':
                output('你们走进迷宫，星空无奈道：“这样不好吧……”')
            if choose == 'B':
                choose = input('CRD大笑：“啊哈！不进也得进！！”一根长矛把你们戳进迷宫，CRD跟在你们后面。[HP-5]')
                health -= 5
                dead_interface()
                if respawned == 1:
                    respawned = 0
                    continue
                view_status()
        output('你们向前走去，前方很快就是个岔路。')
        output('星空说：“我们可以贴着右壁走……”')
        output('“不行！我会把你们堵住的！”CRD在后面大喊。')
        output('你们只好随便拐进右侧。经过了几个弯路，你们来到了一座喷泉旁边。')
        output('CRD出现在你们面前，说道：“好了小东西们，你们将迎来我的绝世谜题！！！”')
        output('你们前面空降了三个盒子。')
        output('CRD喊道：“其中一个盒子里有前往下一道谜题的钥匙，另外两个没有，选一个吧！”')
        output('星空选了一个盒子，CRD顺势打开了另一个盒子，里面空空如也。')
        output('“好了，我给你们一次换盒子的机会，你要开哪个盒子？”')
        output('你会：A：开选的,B：开另一个')
        while choose not in {'A','B','AB'}:
            print('请做出您的选择')
            output('你会：A：开选的,B：开另一个')
        else:
            if choose == 'A' or choose == 'B':
                output('盒子里什么都没有，CRD大笑：“看来运气没有站在你们这边，再见喽！”说完消失了。')
            if choose == 'AB':
                output('你打开了两个盒子，里面什么都没有，星空大叫：“你……骗人！”')
                output('CRD笑道：“啊哈，你们不也作弊了？”现在在这里永远待着吧！说完消失了。')
        output('星空对你说：“别急，CRD绝不止是想把我们关在这里，你找找有什么有用的东西。”')
        output('你看看四周，这里除了喷泉与四周的墙壁外什么也没有。')
        choose = input('你会：A：原路返回,B：查看喷泉,C：查看盒子')
        while choose not in {'A','B','C'}:
            print('请做出您的选择')
            choose = input('你会：A：原路返回,B：查看喷泉,C：查看盒子')
        else:
            if choose == 'A':
                output('你想找进来的路，但四周都被墙壁封死了，没有一条路，你不禁感到奇怪。')
            if choose == 'B':
                output('你看了看喷泉，里面什么也没有。')
            if choose == 'C':
                choose = input('你看了看盒子，突然，在一个盒子下面发现了一把短刀!你获得了【平行匕首】')
                item.append('平行匕首')
                view_status()
        output('正当你四处寻找的时候，一只滚轮从迷宫墙上飞了下来。')
        output('滚轮对你们说：“我是滚轮，刚才CRD从我身边闪过，我脱离了轨道。我想滚，可以让我滚吗？”')
        output('你们会：A：让他滚,B：不让他滚')
        while choose not in {'A','B'}:
            print('请做出您的选择')
            output('你们会：A：让他滚,B：不让他滚')
        else:
            if choose == 'A':
                output('他大惊失色：“你竟然让我滚！你礼貌吗？”')
            if choose == 'B':
                output('他大惊失色：“你竟然拒绝我的请求！你礼貌吗？”')
        fight('滚轮',150,20,0,0,random.randint(30,70),'normal')
        if respawned == 1:
            respawned = 0
            continue
        output('滚轮大惊失色：“你居然击败了我！你礼……仪周全！我会报答你们的！”')
        output('他看了看四周，说道：“我可以带你们离开，骑在我身上，坐稳了。”')
        output('你们骑在滚轮身上，滚轮飞快地滚上了墙，向迷宫尽头滚去。')
        output('你看了看四周，发现一片城堡的残垣断壁在远处浮现。')
        output('“前面就是遗迹了。如果CRD让你们到达那里的话……很有趣的！我去过几次，最近他老是说统治者要在遗迹举行一场盛大的马拉松，说什么‘文化认同感’之类的，我对时事政治不感兴趣……”')
        output('滚轮说了一半，似乎看见了什么，朝你们大叫：“小心！”')
        output('一根长矛射来，把你们打下了墙。')
        output('你们摔在柔软的草地上，没有受什么伤，突然你听到星空欣喜的声音：“CRD真是个大好人啊！我们已经出迷宫了！”')
        output('你发现你降落在迷宫墙外面。')
        output('“可恶的长矛！尽坏我事！”CRD出现在你们面前恼怒地说。')
        output('“你现在又要干什么！”星空发起质问。')
        output('“继续弄点谜题呗！”CRD回答，你发现前面出现了两个箱子，用一个轨道连接着。')
        output('“学过碰撞吗？没学过也不要紧！现在Zero来推这个箱子，把它推到另一个箱子那头，只要撞到那个箱子又不让他移动，你就成功了！”CRD指着其中一个箱子，用轻蔑的语气说。')
        output('你走到那个箱子前，准备推它。')
        output('星空朝你喊道：“别信CRD的鬼话，那个箱子看上去这么重，你不可能推动的！”')
        output('你会：A：轻轻推,B：大力推,C：把箱子推向CRD')
        while choose not in {'A','B','C'}:
            print('请做出您的选择')
            output('你会：A：轻轻推,B：大力推,C：把箱子推向CRD')
        else:
            if choose == 'A':
                output('你轻轻推箱子，箱子纹丝不动，CRD大笑道：“啊哈，没想到Zero这小鬼怎么柔弱啊！我还以为……”')
                output('“闭嘴！”星空愤怒地朝向CRD，“尝尝几何八面体！”一道耀眼光芒射出，CRD惊叫一声，消失了。')
                #万能的集合八面体(
            if choose =='B':
                output('你扭动手腕，深吸一口气，用最大的力气把箱子推了出去，箱子飞出了原位置，和尽头的箱子相撞在一起，发出咚咚的声响。')
                output('你擦了擦手，听到星空大声地鼓掌，CRD下巴快掉到地面上，用难以置信的口吻说：“什么？什么？什么！不可能！你怎么……我特意装了好几块巨石，连我都推不走，你能推动？”')
                output('CRD顿了一下说：“咱们下次再会！”就消失了。')
            if choose == 'C':
                output('你用尽力气，把箱子推向CRD，箱子离开了轨道向CRD飞去，还没等他说“什么？”，就砸了他一个措手不及，便逃跑了。')
                output('星空过了拍了拍你，“干得不错！可是你怎么可以推动这么重的东西呢？”')
                output('你没有回答。')
        output('你们继续向前，穿过一个小山坡后，前方出现了一片开阔倾斜的草地的草地，视野很好。前方的遗迹一览无余，许多尖塔、石柱与城墙重叠映于眼前。')
        output('草地上有条小路，你们顺着小路走下坡。来到了一片树林前。小路再次分为左右两条，树林里还有个向前的石道。')
        output('你会：A：向左走,B：向右走,C：走石道')
        while choose not in {'A','B','C'}:
            print('请做出你的选择')
            output('你会：A：向左走,B：向右走,C：走石道')
        else:
            if choose == 'A':
                output('你向左走去')
                rock = 0
            if choose == 'B':
                output('你向右走，前面是一座吊桥，不过没有桥面。你便向反方向走去')
                rock = 0
            if choose == 'C':
                output('你继续前进')
                rock = 1
        if rock == 0:
            output('前面出现了一道石头门，星空说：“看来是个谜题，你找找有没有什么提示吧。”')
            choose = input('你往石门边上看去，发现一块刻着字的石板，上面写着：“方形对尖锐，三角对恒定，圆对滑。”') #所以这到底是什么意思（ #你觉得我可能知道吗
            view_status()
            output('你发现石板的下方有三个按钮，一个方形、一个圆形、一个三角形，星空说道：“看来我们要按这些按钮才能过去。看来这是个语言谜题，不妨试试字数或者特殊性？”')
            output('你会：A：按方形按钮,B：按圆形按钮,C：按三角形按钮,D：全按')
            while choose not in {'A','B','C','D'}:
                print('请做出你的选择')
                output('你会：A：按方形按钮,B：按圆形按钮,C：按三角形按钮,D：全按')
            else:
                if choose == 'A' or choose == 'C' or choose == 'D':
                    if choose == 'D':
                        choose = input('你先按方形按钮')
                    choose = input('门爆炸了，你们被炸伤了[HP-20]')
                    health -= 20
                    dead_interface()
                    if respawned == 1:
                        respawned = 0
                        continue
                    view_status()
                if choose == 'B':
                    output('门打开了，你们通了过去')
                word = '你们穿过石门，'
        if rock == 1:
            output('四面体看到了你说：“是新人们！必须要战斗才能激发稳定的幸福感！！”')
            fight('四面体',160,10,30,5,random.randint(40,80),'normal')
            if respawned == 1:
                respawned = 0
                continue
            word = '击败四面体后，你们穿过了森林，'
        output(f'{word}来到了一片大理石平台上，你们的前方出现了一座长长的吊桥，通向远处的遗迹')
        output('“看来前面就是我们要去的地方了，不过在这之前，我们还是先准备准备吧。”')
        choose = input('星空随手抛给你了三个心形物体')
        love += 3
        view_status()
        output('你看到平台上有一个自动售货机，一个长椅，还有一架望远镜。')
        output('你会：A：走向吊桥,B：在长椅上休息,C：看看自动售货机,D：看看望远镜')
        while choose not in {'A','B','C','D'}:
            print('请做出你的选择')
            output('你会：A：走向吊桥,B：在长椅上休息,C：看看自动售货机,D：看看望远镜')
        else:
            if choose == 'A':
                output('你走向吊桥')
            if choose == 'B':
                output('你在长椅上休息了一会儿[HP+20]')
                health += 20
                output('你们走上吊桥')
            if choose == 'C':
                output('你看向售货机，上面写着：“流油果25CM币限购一个”')
                output('要买吗？A：买,B：不买')
                while choose not in {'A','B'}:
                    print('请做出你的选择')
                    output('要买吗？A：买,B：不买')
                else:
                    if choose == 'A':
                        if CM < 25:
                            output('你的钱不够!')
                        if len(item) >= 10:
                            output('你的背包已经满了!')
                        else:
                            choose = input('你购买了流油果!')
                            item.append('流油果')
                            fight_item.append('流油果')
                            view_status()
                    if choose == 'B':
                        output('你离开了售货机。')
                    output('你们走上吊桥')
            if choose == 'D':
                output('你看向望远镜，发现它的镜面已经损坏了。')
                output('你们走上吊桥')
        savepoint = 1
    #做个存档点标记
    if savepoint == 1:
        save_data()
        output('CRD突然出现在你们面前，大笑着说道：“哈！又见面了，你们这群小……不说了，进入正题！”')
        output('“你们一定很想知道自己现在在什么地方，告诉你们吧，这座吊桥，是连接【自然】与【文明】的大通道！罗尔斯的帝国横跨【文明】之界，而且将会继续扩张，直到……不，规则告诉我们扩张不会停止！”')
        output('“按理来说在罗尔斯掌握的规则体系下，我们可以掌控这里的一切，然而最近预测出了问题，这是因为你们，这群不属于这个规则体系的小……啊哈！扰乱！动荡！我必须除掉你们，我不想再装一本正经了！”')
        output('“当然！！规则的指示不会出错！即使有扰动，其结果也不会改变！那就是——”')
        output('CRD顿了顿，恶狠狠地喊道：')
        output('“我会把你们揍扁。”')
        light_cube = 0
        fight('CRD',350,15,100,5,90,'xk',10)
        if respawned == 1:
            respawned = 0
            continue
        savepoint = 2
    #大家好我是有名现在是2021年12月20日我要把CRD削一下
    #起码要让我打的过去(

    #做个存档点标记
    if savepoint == 2:
        save_data()
        output('CRD败下阵来，说道：“你……你们居然击败了我！看来你们离罗尔斯大人已经不远了！”')
        output('星空不解：“什么意思？”')
        output('CRD大笑：“啊哈！看来你们这群小……注定要与罗尔斯一战！我只是负责把你们护送到他面前的……天哪！我CRD是一个伟大的护卫兵！！我爱死这东西了！！！”')
        output('星空有点疑惑：“看来你不会再与我们战斗了？”')
        output('“当然！！！你们击败了我，这表明罗尔斯大人的预判没有错！我现在会护送你们前往他的城堡！你们不会再遭受袭击啦！！”CRD回答')
        output('“我们怎么才能相信你！”星空大声说')
        output('“很简单！用我，护卫兵CRD对你们的信任！！！信任是规则的强大力量，符合规则体系的一切事物都具有伟大的可信力！！通过这种信任，我们将会成为挚友！！啊哈！友谊万……”')
        output('“等等！你说的信任是怎么回事？”星空打断他的话。')
        output('“呵呵”CRD沉静下来，随后放声说：“很早之前，在罗尔斯大人征战于规则世界，想要一统天下的时候，旧世界的保守分子们组建了各种力量，但都被一一击溃，其中有一个木马，是旧世界的战争机器，十分的强大啊！        罗尔斯动用了最强大的武力才把它击败，然而击败它之后，罗尔斯大人力排众议，把它收服了下来，如今它成为了我们最强大的助手之一！！如果没有规则的信任，木马怎么可能归属于我们的管辖？！！”')
        output('“厉害。”星空回了两个字。')
        output('“当然！！你们同意了？”')
        output('“暂时同意吧，反正我们击败了你，你也干不了什么。”星空点点头，转过来面向你。“Zero，你同意吗？”')
        choose = input('你会：A：同意,B：不同意')
        while choose not in {'A','B'}:
            print('请做出你的选择')
            output('你会：A：同意,B：不同意')
        else:
            if choose == 'A':
                output('你点头同意')
            if choose == 'B':
                output('你没搭理星空，星空看着你无奈地说：“咱们还是先穿过遗迹再说吧……”')
        output('CRD满意地说道：“好了！现在协议正式生效！我们前进！！！”说完消失不见了。')
        output('星空对你说：“我们继续前进吧！”说完便向前走。')
        output('你也跟着向前进，吊桥非常结实，你站在边缘护栏前面看下去，下面不见底的深渊被浓厚的迷雾环绕。你虽然不恐高，但仍然感到一阵凉意，你向前走去。')
        output('过了一会儿，你们来到了吊桥的终点，踏上了新的土地。')
        output('你发现你站在一座城堡的大门前，巨大的石柱分布在你们周围，看起来都十分古老。')
        #放飞自我中(
        output('你会：A：向大门走去,B：看看四周')
        while choose not in {'A','B'}:
            print('请做出您的选择')
            output('你会：A：向大门走去,B：看看四周')
        else:
            if choose == 'A':
                choose = input('你向大门走去，突然地底下冒出一个尖刺扎了你一脚[HP-5]')
                health -= 5
                dead_interface()
                if respawned == 1:
                    respawned = 0
                    continue
                view_status()
            if choose == 'B':
                output('你看看四周，并没有什么特殊的')
        output('这时，CRD突然出现在你们面前，大声说：“现在我们的保护措施已经生效！！正如你们所见，这里满地都是水晶！在这里水晶就和花草一样平常！稍不留神你们的小命就会……啊哈！为了防止这些发生，我将会带着你们穿越这里！        我知道一条‘秘密通道’，它仅能容纳一个人通过！你们中的一个人将会跟着我通过这条通道，另外一个，就委屈你穿过遗迹的城墙了！！”')
        #兄啊你肺活量好大
        output('星空生气地说：“不是说保护好我们两个吗？！”')
        output('“怎么不是了！你难道不知道，在我们的世界中单打独斗远胜于团战吗？！”CRD大叫道，“在魔法体系中为什么没有战争，因为战争限制了我们的实力！！啊哈！我怎么又正经了！！你难道不觉得一个人度过这美妙的单人时光很好吗？！！”')
        output('“你……要带谁去？”星空看起来有些晕。')
        output('“当然是带弱小的那个去啊！来！Zero快到这里！”')
        output('你会：A：走过去,B：无动于衷,C：做点什么')
        while choose not in {'A','B','C'}:
            print('请做出您的选择')
            output('你会：A：走过去,B：无动于衷,C：做点什么')
        else:
            if choose == 'A':
                output('你走了过去，CRD大笑：“什么？！你个笨……你不知道我在说反话吗？！啊哈！星空跟我过来吧！！”')
            if choose == 'B':
                output('CRD冷笑道：“挺有主见啊，小……当然啦！你比星空可强太多了！！你的力量将会化为你伟大的动力！！”')
            if choose == 'C':
                choose = input('你想了想，然后原地起跑想做个前空翻，但一手扎在水晶上[HP-5]')
                health -= 5
                dead_interface()
                if respawned == 1:
                    respawned = 0
                    continue
                view_status()
                output('“真是可爱的小……什么！你居然有‘勇气’！这可太厉害啦！我怕啦！星空，来吧！”')
            output('“什么？！！”星空惊讶之余，被CRD后面的几个长矛拖着飞了出去')
        output('你现在独自一人了，你绕过水晶前进，但前面又随即出现了许多水晶')
        output('你发现，随着你向门的接近，水晶就会从地下冒出来，不过你现在离门已经只剩下几米远了')
        output('你会：A：小心翼翼地前进,B：快速跑过去,C：跳到门前')
        while choose not in {'A','B','C','D'}:
            print('请做出您的选择')
            output('你会：A：小心翼翼地前进,B：快速跑过去,C：跳到门前')
        else:
            if choose == 'A':
                output('你小心翼翼地前进，水晶也从地下钻出来')
                choose = list(input('回复一次五个大写字母以躲避水晶!'))
                x = random.randint(1,4)
                a = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                b = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                c = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                d = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                e = chr(ord('A') + x - 1)
                enemy_fight = a+b+c+d+e
                enemy_fighta = [a,b,c,d,e]
                hurt = 0
                hurtB = 0
                chance = 0
                wrong = 0
                while wrong == 0:
                    wrong = 1
                    if len(choose) != 5:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的躲避方式!(5个一组,由五个大写字母构成)'))
                    elif choose[0] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的躲避方式!(5个一组,由五个大写字母构成)'))
                    elif choose[1] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的躲避方式!(5个一组,由五个大写字母构成)'))
                    elif choose[2] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的躲避方式!(5个一组,由五个大写字母构成)'))
                    elif choose[3] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的躲避方式!(5个一组,由五个大写字母构成)'))
                    elif choose[4] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的躲避方式!(5个一组,由五个大写字母构成)'))
                    else:
                        while chance < 5:
                        #快悄悄这个地方,我把chance < 5写成了chance <= 5然后查了一天才查到这个bug
                        #悄悄改为瞧瞧,这是个错别字(划)通假字
                        #快看,这里我复制的前面
                            f = choose.pop()
                            g = enemy_fighta.pop()
                            if f == 'D' and g == 'C' or f == 'C' and g == 'B' or f == 'B' and g == 'A' or f == 'A' and g == 'D':
                                hurtB += 5
                                chance += 1
                            else:
                                chance += 1
                        health -= hurtB
                        output(f'水晶的攻击是{enemy_fight}')
                        choose = input(f'你被扣除了{hurtB}点血量')
                        dead_interface()
                        if respawned == 1:
                            respawned = 0
                            continue
                        view_status()
            if choose == 'B':
                choose = input('你快速跑过去，踩到了许多水晶[HP-10]，你的脚被刺伤了。')
                health -= 10
                dead_interface()
                if respawned == 1:
                    respawned = 0
                    continue
                view_status()
            if choose == 'C':
                output('你一个立定跳远跳到了门前，这对你来说不算什么难事')
        output('你进入大门，来到了遗迹内部。')
        output('你的前方是一条大道，许多石柱整齐地分布在两边，地上也没有再出现水晶，你往前走去。')
        output('你看到有个石柱上刻着字，要看吗？A：看,B：不看')
        while choose not in {'A','B'}:
            print('请做出你的选择')
            output('你看到有个石柱上刻着字，要看吗？A：看,B：不看')
        else:
            if choose == 'A':
                output('你看向石柱：上面整齐地写着：“魔法师们可以利用的法术远远不止几种，在前面的石碑上，刻着更多法术的介绍，可惜我已经看不懂了。除了……不，不要提它！”')
            if choose == 'B':
                output('你向前走')
        output('你走到道路的尽头，这里石碑密布，上面刻着密密麻麻的文字，可惜你看不懂。')
        output('你向前穿过无数石碑组成的迷宫，来到一片空旷地带，这里只有一块石碑坐落在中央，旁边还有一只穿着黑袍的鹿。')
        #黑魔法线要开始了(
        ###
        #开始了个寂寞（
        #缩进看着好难受
        #所以HE==0要什么时候填（（
        #要有耐心，等那鸡吃完了米，狗舔完了面，火烧断了锁就可以了
        output('你会：A：看石碑,B：与鹿交谈,C：继续前进')
        while choose not in {'A','B','C'}:
            print('请做出您的选择')
            output('你会：A：看石碑,B：与鹿交谈,C：继续前进')
        else:
            if choose == 'A':
                output('你看石碑，勉勉强强可以看懂一部分：')
                output('“……魔法……清楚地写在……这些刻纹……经过……不行的话……角度F……试着看看……有人……”')
            if choose == 'B':
                output('他看了看你说：“你如果想去城堡，得先向前穿过文明遗迹，然后坐缆车就到了，不过他们大概会把你驱逐出去……”')
            if choose == 'C':
                output('你继续前进')
        output('你继续向前穿越石碑迷宫，前面出现了一堵墙，上面刻着许多文字，你几乎什么都看不懂。')
        output('你会：A：继续前进')
        if '黑暗之剑' not in item:
            while choose != 'A':
                print('请做出你的选择')
                output('你会：A：继续前进')
            output('你继续前进')
        if '黑暗之剑' in item:
            while choose not in {'A'}:
                print('请做出您的选择')
                output('你会：A：继续前进')
            #此线暂时封存
            if choose == 'F':
                output('你爬上墙，翻到墙后面，这里有一块石碑，你发现你可以看懂上面的文字！')
                output('石碑写道：“黑暗魔法——这是世界上最强大的法术，只有掌握【黑暗之剑】的人物才能领会它的内在，可惜啊，【黑暗之剑】已经失传许久了。它曾经被一个强大而有节制的法师掌握着，如果丢失，世界有可能因此被毁灭，前面的祭坛就是召唤黑暗法师之地。”')
                output('你看向前面，前面有一个小平台，要把黑暗之剑放在上面吗？A：放,B：不放')
                while choose not in {'A','B'}:
                    print('请做出您的选择')
                    output('A：放,B：不放')
                else:
                    if choose == 'A':
                        output('你轻轻地把剑放在祭坛上，什么也没有发生。')
                        output('但是你能明显感觉到，有些东西，改变了！')
                        black = 1
                    if choose == 'B':
                        output('你翻了回去')
            if choose == 'A':
                output('你继续前进')
        output('你向前走着，前面突然窜出一个水晶！')
        output('“谁以为水晶不会魔法了！”它大声说道')
        print('战斗开始,对战水晶')
        kill = 1
        item_att = 0
        t.sleep(0.5)
        tetrahedra = 120
        magic_point = 0
        win = 0
        a,b,c,d,e = '','','','',''
        while win == 0:
            magic_choose = 0
            att_choose = 0
            item_choose = 0
            while magic_choose == 0 and item_choose == 0:
                chooseb = 'A'
                print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health},水晶血量为{tetrahedra}')
                choose = input('A,物品B,防御C,魔法D,跳过')
                while choose not in {'A','B','C','D'}:
                    print('请做出你的选择')
                    choose = input('A,物品B,防御C,魔法D,跳过')
                if choose == 'A':
                    choose = input(f'你现在可使用的物品有{fight_item},请从1开始输入序号以选择使用的物品')
                    if choose not in {'1','2','3','4','5','6','7','8','9','10'}:
                        choose = input('物品序号输入错误!')
                    else:
                        choose = int(choose)
                        if choose > len(fight_item):
                            choose = input('物品序号输入错误!')
                        else:
                            choose -= 1
                            check = fight_item[choose]
                            item_find()
                            if check in fight_item and check in item:
                                item.remove(check)
                                fight_item.remove(check)
                        if health > 240:
                            health = 240
                if choose == 'B':
                    choose = input('你选择了防御!')
                    magic_point += 40
                    magic_choose = 1
                    if magic_point >= 100:
                        magic_point = 100
                    chooseb = 'B'
                if choose == 'C':
                    if black == 0:
                        choose = input(f'A：治疗魔法（{health_point}）B：战斗魔法（70）C：黑暗魔法（？）')
                        while choose not in {'A','B','C'}:
                            print('请做出你的选择')
                            choose = input(f'A：治疗魔法（{health_point}）B：战斗魔法（70）C：黑暗魔法（？）')
                    if black == 1:
                        choose = input(f'A：治疗魔法（30）B：战斗魔法（70）C：黑暗魔法（100）')
                        while choose not in {'A','B','C'}:
                            print('请做出你的选择')
                            choose = input(f'A：治疗魔法（30）B：战斗魔法（70）C：黑暗魔法（100）')
                    if choose == 'A':
                        if magic_point < health_point:
                            choose = input('你的魔法值不够!')
                            magic_choose = 0
                        if magic_point >= health_point:
                            choose = input(f'你使用了治疗法术!你的血量回复了{health_plus}点!')
                            health += health_plus
                            magic_choose = 1
                            magic_point -= 30
                        if health > 240:
                            health = 240
                            magic_choose = 1
                    if choose == 'B':
                        if magic_point < 70:
                            choose = input('你的魔法值不够!')
                            magic_choose = 0
                        if magic_point >= 70:
                            choose = input('你使用了战斗法术!你的攻击提高了5点,持续一回合!')
                            att_choose = 1
                            magic_choose = 1
                            magic_point -= 70
                    if choose == 'C':
                        if black == 0:
                            choose = input('l͓̩̫̘͙͔̯͖̟̤̓͊̑̌́̂̆̚ò̥̪̭̱̰̝̒͂̄͋̿̏͆́̚c͍̲͇͚̖̬͈̪͙̳͌̉́̃k̪̥̱̝̱̑̈́̏̽͗̊̈́͂̀̍e̞͎̩̜̱̩͚̤̊͌̀̀d̠̖̞̝̙̪̟̞̐͛̈̊̀͂̄͌̓̏͌̓ͅ')
                            magic_choose = 0
                        if black == 1:
                            if magic_point < 100:
                                choose = input('你的魔法值不够!')
                            else:
                                magic_point = 0
                                choose = input('水晶被黑暗笼罩住了！您获胜了，黑暗法术增强了！')
                                win = 1
                                HE = 0
                    choose = 0
                if choose == 'D':
                    choose = input('你跳过了你的回合')
                    magic_choose = 1
            if win == 0:
                x = random.randint(1,4)
                a = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                b = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                c = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                d = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                e = chr(ord('A') + x - 1)
                enemy_fight = a+b+c+d+e
                enemy_fighta = [a,b,c,d,e]
                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                hurt = 0
                hurtB = 0
                chance = 0
                wrong = 0
                while wrong == 0:
                    wrong = 1
                    if len(choose) != 5:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[0] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[1] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[2] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[3] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[4] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                else:
                    tetrahedra_act = random.randint(1,5)
                    while chance < 5:
                        f = choose.pop()
                        g = enemy_fighta.pop()
                        if chooseb != 'B':
                            if f == 'A' and g == 'B' or f == 'B' and g == 'C' or f == 'C' and g == 'D' or f == 'D' and g == 'A':
                                hurt += att
                                chance += 1
                                if att_choose == 1:
                                    hurt += 5
                                if tetrahedra_act == 5:
                                    hurt -= 20
                                    if hurt < 0:
                                        hurt = 0
                                hurt += item_att
                        if f == 'D' and g == 'C' or f == 'C' and g == 'B' or f == 'B' and g == 'A' or f == 'A' and g == 'D':
                            hurtB += 5
                            if chooseb == 'B':
                                hurtB -= Def
                                if Def >= 5:
                                    hurtB = 0
                            chance += 1
                        else:
                            chance += 1
                    tetrahedra -= hurt
                    health -= hurtB
                    item_att = 0
                    choose = input(f'水晶的攻击是{enemy_fight}')
                    if tetrahedra_act > 4 :
                        choose = input('水晶使用了防御!')
                    if chooseb != 'B':
                        choose = input(f'你对敌方造成了{hurt}点伤害!')
                        hurt = 0
                    if chooseb == 'B':
                        choose = input('因为你选择了防御,所以伤害不计入')
                    choose = input(f'你被水晶扣除了{hurtB}点血')
                    dead_interface()
                    if respawned == 1:
                        break
                    hurtB = 0
                    att_choose = 0
            if tetrahedra <= 0:
                choose = input('您获胜了!')
                CM += 100
                HE = 1
                choose = input(f'你获得了100个CM币')
                win = 1
        if respawned == 1:
            respawned = 0
            continue
        output('你击败了水晶后，水晶缩回了地下。')
        output('你继续向前走，拐过几个弯后，你来到了一座建筑物内。')
        output('你看见三个巨大的蓝色发光圆环竖放在你面前，前面一块石碑上写着：“遗迹传送门，左：石头堡垒，中：城墙，右：树林”')
        output('你会：A：钻进左边的传送门,B：钻进中间的传送门,C：钻进右边的传送门')
        while choose not in {'A','B','C'}:
            print('请做出您的选择')
            output('你会：A：钻进左边的传送门,B：钻进中间的传送门,C：钻进右边的传送门')
        input('你通过传送门，眼前的景物一下发生了变化！')
        view_status()
        if choose == 'A':
            output('你来到了一座石头堡垒前')
        if choose == 'B':
            output('你来到了一座城墙的上方，你向前走去，发现前面的路被封住了，旁边的告示牌上写着：“遗迹马拉松举行中。”')
            output('你走回传送门，但这次传到了一个新的地方！前面是一座石头堡垒')
        if choose == 'C':
            output('你来到了一个小树林前，不过树林被绳子挡住了，绳子上挂着许多广告，似乎在宣传一个马拉松比赛。')
            choose = input('你看到旁边有一个箱子，里面是一个像蜡烛一样的小石碑,你获得了【燃烧碑】.')
            item.append('燃烧碑')
            view_status()
            output('你走回传送门，但这次传到了一个新的地方！前面是一座石头堡垒')
        output('你推开堡垒的木门，走了进去，发现里面是一间咖啡厅！许多蜡烛一样的石碑发出火光，照亮了石制的墙壁与地板，许多人在石凳上坐着，不过并不像在交谈，气氛非常安静。')
        output('你会：A：从后门出去,B：找人交谈,C：买东西')
        while choose not in {'A','B','C'}:
            print('请做出您的选择')
            output('你会：A：从后门出去,B：找人交谈,C：买东西')
        if choose == 'B':
            input('你找到一个骷髅，他说：“最近新统治者搞了个环绕遗迹的马拉松比赛，搞了差不多一个月，我们居民都快被他烦死了，哎，还是扑克时代好！”')
            view_status()
        if choose == 'C':
            input('你走到前台，服务员是一个水晶。他看到你用极为机械的语气说道：“一杯咖啡50CM币”')
            view_status()
            output('要买吗？A：买,B：不买')
            while choose not in {'A','B'}:
                print('请做出您的选择')
                output('要买吗？A：买,B：不买')
            if choose == 'A':
                if CM >= 50:
                    input('你买了杯咖啡，尝了一下，感觉在喝史莱姆粘液[HP-1]')
                    health -= 1
                    CM -= 50
                    dead_interface()
                    if respawned == 1:
                        respawned = 0
                        continue
                    view_status()
                else:
                    input('水晶说：“你没有足够的CM币，购买失败”')
                    view_status()
            else:
                input('你离开前台')
                view_status()

        input('你从后门出去')
        input('你离开咖啡馆，走上了前面的城墙，你扶着墙壁看了看遗迹外面的景色，发现有一群人在城墙下方跑步，你不禁有种加入他们的冲动。')
        view_status()
        input('你向前走，到了一个两边都是楼梯的岔路口时，一堆水晶冲了上来！')
        view_status()
        input('你停下来看了看这群水晶，发现这波似乎没有结束的迹象，你认为应该钻缝隙冲过去！')
        view_status()
        choose = list(input('回复一次五个大写字母以躲避水晶!'))
        x = random.randint(1,4)
        a = chr(ord('A') + x - 1)
        x = random.randint(1,4)
        b = chr(ord('A') + x - 1)
        x = random.randint(1,4)
        c = chr(ord('A') + x - 1)
        x = random.randint(1,4)
        d = chr(ord('A') + x - 1)
        x = random.randint(1,4)
        e = chr(ord('A') + x - 1)
        enemy_fight = a+b+c+d+e
        enemy_fighta = [a,b,c,d,e]
        hurt = 0
        hurtB = 0
        chance = 0
        wrong = 0
        while wrong == 0:
            wrong = 1
            if len(choose) != 5:
                wrong = 0
                print('输入错误,请依照格式输入!')
                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
            elif choose[0] not in {'A','B','C','D'}:
                wrong = 0
                print('输入错误,请依照格式输入!')
                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
            elif choose[1] not in {'A','B','C','D'}:
                wrong = 0
                print('输入错误,请依照格式输入!')
                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
            elif choose[2] not in {'A','B','C','D'}:
                wrong = 0
                print('输入错误,请依照格式输入!')
                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
            elif choose[3] not in {'A','B','C','D'}:
                wrong = 0
                print('输入错误,请依照格式输入!')
                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
            elif choose[4] not in {'A','B','C','D'}:
                wrong = 0
                print('输入错误,请依照格式输入!')
                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
            else:
                while chance < 5:
                    f = choose.pop()
                    g = enemy_fighta.pop()
                    if f == 'D' and g == 'C' or f == 'C' and g == 'B' or f == 'B' and g == 'A' or f == 'A' and g == 'D':
                        hurtB += 5
                        chance += 1
                    else:
                        chance += 1
                health -= hurtB
                output(f'水晶的攻击是{enemy_fight}')
                choose = input(f'你被扣除了{hurtB}点血量')
                dead_interface()
                if respawned == 1:
                    respawned = 0
                    continue
                view_status()
        choose = input('你通过了水晶流，找到了一个宝箱，里面的东西你很难理解（获得【水晶焰】）')
        item.append('水晶焰')
        fight_item.append('水晶焰')
        view_status()
        output('过了一会儿，你通过另一个楼梯口下了城墙，来到一处房屋前，前面有一只鹿，还有一棵树，看来这是居民区')
        output('你会：A：向前走,B：与鹿交谈,C：看看树,D：看看房子')
        while choose not in {'A','B','C','D'}:
            print('请做出您的选择')
            output('你会：A：向前走,B：与鹿交谈,C：看看树,D：看看房子')
        else:
            if choose == 'A':
                output('你向前走去')
            if choose == 'B':
                output('你试图与鹿交谈，他看了看你，无声地走开了，你只好往前走')
            if choose == 'C':
                choose = input('你在树上找到了10CM币！【CM币+10】然后你往前走去')
                CM += 10
                view_status()
            if choose == 'D':
                output('你看了看房子，里面隐隐约约听到说话声，不过很模糊。你向前走去')
        if fun == 33: 
            output('你走到两座墙壁夹着的小巷中，旁边似乎有一扇门')
            output('进去吗：A：不进,B：进去')
            while choose not in {'A','B'}:
                print('请做出您的选择')
                output('进去吗：A：不进,B：进去')
            else:
                if choose == 'A':
                    output('你松了口气')
                if choose == 'B':
                    output('你进入门中')
                    output('门里面漆黑一片，什么都没有')
                    output('你感到害怕，想往后退，但找不到门在哪！')
                    output('周围到处都是迷迷糊糊的黑暗，什么都不存在，一切似乎都化为虚无。')
                    output('你伸手想在地上碰碰，可是你找不到地板，一切实体在这团黑暗中似乎都湮灭为虚无，你似乎只剩下思考的感觉了！')
                    output('一切感官都消失了，什么都结束了，黑暗在侵蚀……你突然感受到了无限的存在，你能接触到冥冥中的空间，那……似乎就是你的……')
                    output('突然，视野再度恢复了光明，你发现你坐在地上，转身看看侧面，门已经消失。')
                    output('你松了口气')
        output('你走了一会儿，来到一座石砖做的平台上，这时一只穿着长袍，提着一个形状怪异的灯的鹿走了过来。你认清楚了他就是刚才的那只鹿。')
        output('“我是法师，就在刚才，有人让我来这里找一个穿着短袖、短裙的女孩，你知道她在哪里吗？”他问道。')
        output('你会回答：A：不知道,B：就在这里！')
        while choose not in {'A','B'}:
            print('请做出您的选择')
            output('你会回答：A：不知道,B：就在这里！')
        else:
            if choose == 'A':
                output('你回答不知道，那只鹿面不改色地说：“撒谎的孩子可不对哦！看来你得挨一顿揍了！”')
                deer = 0
                fight('鹿法师',145,20,10,20,random.randint(150,190),'normal',5)
            if choose == 'B':
                output('他面不改色地回答：“哦，事实上我已经知道是你了，不过你居然能够诚实回答，这真令人难以置信。”')
                deer = 1
                fight('鹿法师',1,10,10,20,random.randint(150,190),'normal',5)
            if respawned == 1:
                respawned = 0
                continue
        if deer == 0:
            output('他看了看你，说：“看来我的魔法团能量耗尽了，你先过去吧。”说着就默默走开了。')
        if deer == 1:
            output('他对你说：“看在你这么真诚的份上，现在我来告诉你一个秘密。”')
            output('“那个人来问你之后，偷偷让我找一个木马，我在遗迹生活几百年了，从来没见过什么木马，他随后告诉我，让我提醒你看到木马一定要小心。”')
            if '水晶焰' not in item:
                output('“看起来你的装备还不够强……你最好小心点。”说完他就离开了。')
            if '水晶焰' in item:
                output('“看起来你的装备还不够强……什么，你有一个【水晶焰】？这可是强大的魔法原料啊，来，让我合成一下……”')
                output('他的手上出现一个橘红色的宝石。')
                choose = input('“这个送你了。”他面不改色地对你说，把宝石递给了你，说完就走开了。”')
                item.append('生命宝石')
                item.remove('水晶焰')
                fight_item.remove('水晶焰')
                health_plus = 80
                health_point = 50
                view_status()
        output('你继续前进，发现前面有一个大坑，坑里零零散散地放着几个箱子')
        output('你会：A：走下坑,B：绕过坑,C：踩着箱子跳过坑')
        while choose not in {'A','B','C'}:
            print('请做出您的选择')
            output('你会：A：走下坑,B：绕过坑,C：踩着箱子跳过坑')
        else:
            if choose == 'A':
                output('你走下坑')
                hole = 0
            if choose == 'B':
                output('你绕过坑')
                hole = 1
            if choose == 'C':
                output('你踩着几个箱子跳过了坑，一个巨大的虫子站在坑对面惊讶地看着你，你看了看它，它脸红地跑开了。')
                hole = 1
        if hole == 0:
            output('你走下坑，看了看箱子，箱子上贴着许多遗迹马拉松的广告，看来是物资箱。')
            output('其中一个大箱子上面画着一个奇形怪状的木马，与你之前见到的那个很不一样。')
            output('你会：A：离开,B：拿物资,C：拆开木马箱')
            while  choose not in {'A','B','C'}:
                print('请做出您的选择')
                output('你会：A：离开,B：拿物资,C：拆开木马箱')
            else:
                if choose == 'A':
                    output('你离开了大坑')
                if choose == 'B':
                    choose = input('你在箱子里发现了一个【花色汉堡】！随后你离开大坑')
                    item.append('花色汉堡')
                    fight_item.append('花色汉堡')
                    view_status()
                if choose == 'C':
                    output('你花了好大力气拆开木马箱，发现里面什么也没有。随后你离开大坑')
        output('前面是一座由石头房组成的小城，不过显然已经废弃许久了。')
        output('你径直走到小城的尽头，发现前方是通往城墙的楼梯，不过被封住了，显然又是为了遗迹马拉松。')
        output('你往左边看去，发现一个敞开的石门，里面又是两个传送门！')
        output('你会：A：走左边的传送门,B：走右边的传送门')
        while choose not in {'A','B'}:
            print('做出您的选择！')
            choose = input('你会：A：走左边的传送门,B：走右边的传送门')
            chooseb = choose
            view_status()
        else:
            output('你进入传送门')
            if chooseb == 'A':
                door =1
            if chooseb == 'B':
                door = 2
        if door == 1:
            output('你来到了一座平台上，你的前面是一座高塔，塔下站着一个骷髅。一扇紧闭的石门挡在你的左侧。')
            output('你和骷髅交谈，一个骷髅说：“我只是想来城墙找我哥们，但突然就被这该死的谜题困住了，我连箱子都搬不起来，我要杀了这出题人！！”')
            #我猜end是请来了某游戏的那两位来客串了
            output('你看向你的右边，右边有三个箱子，一个标有三角形标志，一个标有方形标志，还有一个标有圆形标志。你的面前有个长长的凹槽，前面还有个告示牌：“请把箱子按正确的顺序摆放到槽里，即可开门。”')
            output('你把三角箱摆在左边，突然头顶传来了一丝亮光，你发现头顶的许多彩灯中有三个发出了微弱的红光。你右移箱子，有一个彩灯熄灭了，再右移一次，又熄灭了一个。你取出三角箱，将方形箱放在凹槽里，最左边时四个灯发光了，往右边时熄灭了两个，再往右全部熄灭了。')
            output('最后，你放入圆形箱，无论它在什么位置，都没有一个彩灯发光。')
            output('你放了放箱子，发现头顶的彩灯超过五个发光时，发出了白光，没超过五个时发红光，不知道五个彩灯发光时会是怎么样的。')
            secret = 0
            while secret == 0:
                choose = list(input('（回复字母搬动箱子！A表示三角箱，B表示方形箱，C表示圆箱，按从左往右顺序排列字母！）'))
                while 'A' not in choose or 'B' not in choose or 'C' not in choose:
                    print('请按要求搬动箱子！')
                    choose = list(input('（回复字母搬动箱子！A表示三角箱，B表示方形箱，C表示圆箱，按从左往右顺序排列字母！）'))
                else:
                    light = 0
                    if choose[0] == 'A':
                        light += 3
                    if choose[0] == 'B':
                        light += 4
                    if choose[1] == 'A':
                        light += 1
                    if choose[1] == 'B':
                        light += 2
                    if choose[2] == 'A':
                        light += 1
                    if light == 5:
                        choose = input('五个彩灯被你点亮了，它们发出了绿光！门打开了')
                        secret = 1
                    if light != 5:
                        choose = input(f'你点亮了{light}个灯，门没有打开！')
            output('你穿过石门')
        if door == 2:
            output('你来到了一座高塔上，前面有一个骷髅，它看到了你，对你说：“最新遗迹直角滑道，不可不试！来看看吗？”')
            output('你来到塔边缘俯瞰着下面的城墙，看起来没有一点防护。')
            output('“跳下去就得了！”它对你说')
            output('你跳了下去，在下落的同时，你感到有一股力在把你往上托，并没有自由落体的感觉。')
            output('突然，前面闪过许多水晶：“有了这捷径，马上就可以到城堡啦！！！”')
            print('回复四次字母以躲避！')
            chanceb = 4
            while chanceb > 0:
                if chanceb == 4:
                    choose = list(input('请输入你的第一次躲避方式'))
                if chanceb == 3:
                    choose = list(input('请输入你的第二次躲避方式'))
                if chanceb == 2:
                    choose = list(input('请输入您的第三次躲避方式！'))
                if chanceb == 1:
                    choose = list(input('请输入你的最后一次躲避方式！'))
                chanceb -= 1
                x = random.randint(1,4)
                a = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                b = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                c = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                d = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                e = chr(ord('A') + x - 1)
                enemy_fight = a+b+c+d+e
                enemy_fighta = [a,b,c,d,e]
                hurt = 0
                hurtB = 0
                chance = 0
                wrong = 0
                while wrong == 0:
                    wrong = 1
                    if len(choose) != 5:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[0] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[1] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[2] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[3] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[4] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                else:
                    while chance < 5:
                    #快悄悄这个地方,我把chance < 5写成了chance <= 5然后查了一天才查到这个bug
                    #悄悄改为瞧瞧,这是个错别字(划)通假字
                    #快看,这里我复制的前面
                        #快看，我还是复制的前面（
                        f = choose.pop()
                        g = enemy_fighta.pop()
                        if f == 'D' and g == 'C' or f == 'C' and g == 'B' or f == 'B' and g == 'A' or f == 'A' and g == 'D':
                            hurtB += 10
                            chance += 1
                        else:
                            chance += 1

                    health -= hurtB
                    choose = input(f'水晶的进攻方式是{enemy_fight}')
                    choose = input(f'你被扣除了{hurtB}点血量')
                    dead_interface()
                    if respawned == 1:
                        respawned = 0
                        continue
                output('你从塔上落下')
        output('你来到了城墙上，你的面前是一座一座的石头堡垒，有些似乎在战争中被严重破坏了。')
        output('你向前走去，发现路在你的前方又分成了两条，左边的石头堡垒更多。')
        output('你会：A：往左走,B：往右走')
        while choose not in {'A','B','C','D'}:
            print('请做出您的选择！')
            output('你会：A：往左走,B：往右走')
        else:
            if choose == 'A':
                choose = input('左边是一个被许多堡垒拥簇着的高台，上面有一个箱子，你在里面发现了一个炮弹！你得到了【魔法炸药】，然后你离开了这里。')
                item.append('魔法炸药')
                fight_item.append('魔法炸药')
                view_status()
            if choose == 'B':
                output('你向右走去')
        output('你继续行走在这座城墙之上，你看了看城墙外面，那是一片郁郁葱葱的森林，远处又有一座城堡，粉色的尖塔融化在夕阳中。突然想到了星空与CRD，不知道他们现在如何。')
        output('你走上一座平台，突然，两个拿着盾牌的骷髅接近了你！')
        output('“诶，那边那个叫做Z什么的，有个人找到了我们【持盾骷髅组合】来灭了……”一个骷髅说道，然而马上被另一个打断了。“拜托，我们不迟钝，不迟钝……”')
        choose == input('“是持盾啊！老兄，你眼睛都闻了些什么呢！我觉得你应该重修高中文凭……”')
        view_status()
        output('“我的天，你不知道谐音是不吉利的嘛！”')
        output('“不！谐音梗扣钱！！！我不同意这样！”')
        output('“这不符合……”')
        output('你无视他们的争吵，向前走去。')
        output('“我认为……不好！！她逃跑了！快挡住他！”一个骷髅惊叫。')
        output('它们迅速调整姿势挡在你面前')
        fight('骷髅',200,20,0,0,120,'normal')
        if respawned == 1:
            respawned = 0
            continue
        output('骷髅们败下阵来，大怒，对你说：“啊啊啊啊啊什么东西啊你是！！！我们可是曾经扑克国王的护卫兵！你给我……”')
        output('“你的曾经是不是说错……”')
        output('“不不不！语法没有错误！！扑克国王不已经……”')
        output('“别说啦！现在，打倒这家伙才是正事！”')
        output('它们再次向你袭来，突然地底下钻出了一个水晶！')
        output('“你们在干什么啊！到底在干什么啊！”')
        output('“不！你们搞错啦！CRD哪有叫你们杀Zero？你们是要护卫她到文明遗迹！”')
        output('“什么？你……”一个骷髅惊讶地说道，转头看向另一个骷髅，“你是怎么听的，你语法不仅错误而且听力……”')
        output('“CRD说的是让Zero小心万分危险的东西，我们不就是……”')
        output('“好啦好啦，现在不是说这个的时候。最重要的是护送Zero到文明遗迹，我们走吧！”')
        output('你们向前走了一会儿，又来到一座平台，水晶对你说：“我们不妨在这儿歇一会吧。”')
        output('平台上有一座矮小的石柱，周边都是灰色的石头堡垒，看起来十分单调')
        output('你会：A：交谈,B：看石柱,C：向前走')
        while choose not in {'A','B','C'}:
            print('请做出您的选择')
            output('你会：A：交谈,B：看石柱,C：向前走')
        else:
            if choose == 'A':
                output('一个骷髅说：“啥？交谈？你也太嫩了！先回去见见你的老师吧！”')
            if choose == 'B':
                output('你看向石柱，上面模模糊糊地写道：“虽然没有悬念，但我们还是坚守阵地，直到木马前来，我们不能放弃。”')
        output('你们继续前进，前方是离开城堡的楼梯，不过被绳挡住了。')
        output('“啥？这也被封了，太可恶啦！让我！！”一个骷髅拿起手中的三叉戟，想要往下劈去。')
        output('“不！没有必要！”水晶大叫，然后钻到地下。过了一会儿，水晶钻了回来，对你们说：“我们往回走，地下有个传送门开关，我开启了传送门。”')
        output('“什么啊！传送门也太……”骷髅刚要发话，就被另一个打断了：“好吧，感觉随机传送也没关系啦。”')
        output('你们往回走，来到平台，发现之前的石柱前面出现了一个蓝色的传送门，你们钻了进去。')
        output('出口在一个狭窄的小巷里，周围高大的建筑应该是城堡。水晶看了看，对你说：“太好了，我们离出口不远了。”')
        output('你们向前走去，发现全面是一个十字路口，不过四周都是小巷。')
        go = 0
        candy = 0
        while go == 0:
            output('你会：A：我们分头行动！,B：向左走,C：向前走,D：向右走')
            while choose not in {'A','B','C','D'}:
                print('请做出您的选择')
                output('你会：A：我们分头行动！,B：向左走,C：向前走,D：向右走')
            else:
                if choose == 'A':
                    output('水晶说：“呃……分头行动好是好，可是这样我们也更弱了……算了吧。”')
                elif choose == 'B':
                    output('你向左走，是个死胡同，什么都没有。')
                elif choose == 'C':
                    output('你向前走')
                    go = 1
                elif choose == 'D' and candy == 0:
                    choose == input('你向右走，走了一会儿就没路了，不过尽头有个垃圾桶，你在里面找到了一个糖果。（获得【方块糖果】）')
                    view_status()
                    candy = 1
                    item.append('方块糖果')
                    fight_item.append('方块糖果')
                elif choose == 'D' and candy == 1:
                    output('你又去刨了刨垃圾桶')
                    output('什么也没找到')
        output('前面的道路越来越宽，最终汇入了一条大路，周围的石柱让你想到了刚进遗迹时的道路。')
        output('这时，路上窜出很多水晶，不过他们一见到你们的水晶就钻进地下了。')
        output('前方出现了一座巨大的拱形门，看起来十分崭新，不过细看裂痕也不少，你们穿了过去。')
        output('门外是一片树林，树林中有一条小路。')
        output('水晶对你说：“穿过这条路，就到文明遗迹了，不过在这之前去买点吃的吧。')
        output('水晶拉着你穿过另一条小路，到了一片空地，你看到这里摆着五颜六色的摊位，许多鹿在摊前卖东西。')
        print('鹿们看到了你，大声吆喝：')
        t.sleep(0.4)
        print('“卖冰棍咯，用它砸人多是人间一件美事啊！”')
        t.sleep(0.4)
        print('“香蕉球！完全非空气动力学设计！”')
        t.sleep(0.4)
        print('“飞镖比赛，胜者有礼！”')
        output('你会：A：买冰棍,B：买香蕉球,C：玩飞镖,D：离开')
        while choose not in {'A','B','C','D'}:
            print('请做出您的选择')
            output('你会：A：买冰棍,B：买香蕉球,C：玩飞镖,D：离开')
        else:
            if choose == 'A':
                if CM < 15:
                    output('你没有足够的CM币，购买失败')
                else:
                    if CM >= 15:
                        choose = input('你用15块买了个冰棍(获得【坚硬冰棍】)')
                        item.append('坚硬冰棍')
                        fight_item.append('坚硬冰棍')
                        view_status()
            if choose == 'B':
                output('你靠近小贩，他看到了你面带笑容地说：“只要没有空气就可以无视空气动力学了，哦，还要没重力，所以要买个马气无重力真空实验机吗，只需3000000000000CM币！”')
                output('你无视他，走了')
            if choose == 'C':
                output('你来到飞镖摊位，拿起几个飞镖闭着眼睛乱扔，射破了差不多五十米远的所有气球。飞镖摊主瞪着眼说：“你！你个纪……我可没准备礼物，从来没人射中过气球！你走吧。”')
            if choose == 'D':
                output('你离开这里')
        output('水晶买完了东西，看见你说：“你怎么什么吃的也没买……算了我们赶快走吧。”')
        output('你们回到了之前的路口，与两个骷髅一起向森林前进。')
        output('走过了一段路，你突然被什么东西绊了一下，你的脚底擦破了，在地上留下一些血迹。')
        output('“没事吧。”水晶在一旁说。')
        output('你会：A：回答没事,B：看看绊倒你的东西,C：继续前进')
        while choose not in {'A','B','C'}:
            print('请做出您的选择')
            output('你会：A：回答没事,B：看看绊倒你的东西,C：继续前进')
        else:
            if choose == 'A':
                output('水晶说：“没事就好，我们继续走。”')

            if choose == 'B':
                output('你看了看那个东西，发现是个三叉戟的头，显然被什么东西弄断了。')
        output('你继续往前走，发现前面杂乱地丢弃了许多盾牌、刀剑的碎片，甚至还有损毁的大炮。地面上有许多大坑，不过好在没有尸体。')
        output('“什么情况啊这是。”一个骷髅说。')
        output('“这就是那个令人恐惧的东西吗？”另一个骷髅发话。')
        output('你们继续向前，突然有一只猫头鹰从低空飞过来，大声对你们说：“不要再往前走了！前面有个令人难以置信的超超超超恐怖吓人的大东西！它刚才在攻击马拉松的游行卫兵，他们都遭殃啦！！！我们为了不引起恐慌才没上报的，你们快离开这里啊啊啊！！！”说完就飞走了。')
        output('你会：A：继续前进,B：交谈,C：观察场地')
        while choose not in {'A','B','C'}:
            print('请做出您的选择')
            output('你会：A：继续前进,B：交谈,C：观察场地')
        else:
            if choose == 'B':
                output('骷髅们说：“CRD那家伙搞什么啊是，让我们弄一个这么多人都打不过的……”')
                output('水晶说：“算了算了，CRD让我们这么做一定有原因，继续走吧。”')
            if choose == 'C':
                output('你看了看场地的残骸，除了碎片和尘土外没什么特别的东西。')
        savepoint = 3
    #做个存档点标记
    if savepoint == 3:
        save_data()
        output('你们向前走，在一个森林的转角处，你们看见一块大石头挡在路上。')
        output('你们刚想继续前进，突然石头后面伸出一个脑袋。')
        output('水晶示意你们待在原地别动，然后钻进地里，过了一会，他钻出来，对你们说：“只是一个小木马罢了，别怕。”')
        output('你似乎想起了什么，待在原地不动，然而两个骷髅已经向前走了过去，就在这时，那个脑袋突然消失了，一阵爆炸的响声传来，那块大石头瞬间炸裂，石块向你们飞了过来，还好骷髅眼疾手快把它们挡住了。')
        output('你向原处看去，发现原来石头坐落的地方，出现了一个巨大的奇形怪状的木马，它的身体中间有许多看上去像大炮的管状物，中间升起几丝烟尘。')
        output('“小心了！”还没等水晶说完，一发炮弹落在你们身边。')
        output('两个骷髅用盾挡在了你身前(DEF+20)')
        print('战斗开始,对战机械木马')
        item_att = 0
        t.sleep(0.5)
        fight = 4
        horse = 600
        magic_point = 0
        win = 0
        a,b,c,d,e = '','','','',''
        horse_att = 20
        your_att = att
        your_def = Def
        bullet = 0
        horse_up = 0
        hit = 0
        while win == 0:
            magic_choose = 0
            att_choose = 0
            item_choose = 0
            if horse < 400:
                choose = input('机械木马的HP降低了！')
                choose = input('机械木马使用了【自我修复】！机械木马的HP回升了70点！')
                if horse_up == 0 :
                    choose = input('“呃……这样真的能击败它吗？”水晶说道。')
                    choose = input('“Zero就不能用点什么手段吗……”一个骷髅抱怨道。')
                    choose = input('“呃……对了！我看到这个木马的炮管，在平常的时候好像都是掩着的，说不定这就是它的弱点！Zero，它等下发动炮弹攻击的时候，你向炮管打去，看看会怎么样！”水晶说。')
                    horse_up = 1
                    fight = 4
                horse += 70
            while magic_choose == 0 and item_choose == 0:
                chooseb = 'A'
                print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health},机械木马的血量为{horse}')
                choose = input('A,物品B,防御C,魔法D,跳过')
                while choose not in {'A','B','C','D'}:
                    print('请做出你的选择')
                    choose = input('A,物品B,防御C,魔法D,跳过')
                if choose == 'A':
                    choose = input(f'你现在可使用的物品有{fight_item},请从1开始输入序号以选择使用的物品')
                    if choose not in {'1','2','3','4','5','6','7','8','9','10'}:
                        choose = input('物品序号输入错误!')
                    else:
                        choose = int(choose)
                        if choose > len(fight_item):
                            choose = input('物品序号输入错误!')
                        else:
                            choose -= 1
                            check = fight_item[choose]
                            item_find()
                            if check == '魔法炸药':
                                choose = input('你对对方造成了100点伤害!但你也不小心受到了30点伤害')
                                health -= 30
                                cube -= 100
                                dead_interface()
                                if respawned == 1:
                                    break
                            if check == '坚硬冰棍':
                                choose = input('你使用了坚硬冰棍!敌方的HP降低了100点!')
                                cube -= 100
                            if check in fight_item and check in item:
                                item.remove(check)
                                fight_item.remove(check)
                        if health > 240:
                            health = 240
                if choose == 'B':
                    choose = input('你选择了防御!')
                    magic_point += 40
                    magic_choose = 1
                    if magic_point >= 100:
                        magic_point = 100
                    chooseb = 'B'
                if choose == 'C':
                    choose = input(f'A：治疗魔法（{health_point}）B：战斗魔法（70）C：黑暗魔法（？）')
                    while choose not in {'A','B','C'}:
                        print('请做出你的选择')
                        choose = input(f'A：治疗魔法（{health_point}）B：战斗魔法（70）C：黑暗魔法（？）')
                    else:
                        if choose == 'A':
                            if magic_point < health_point:
                                choose = input('你的魔法值不够!')
                                magic_choose = 0
                            if magic_point >= health_point:
                                if '生命宝石' not in item:
                                    choose = input(f'你使用了治疗法术!你的血量回复了{health_plus}点!')
                                    health += health_plus
                                if '生命宝石' in item:
                                    choose = input(f'你使用了治疗法术!你的血量回复了{health_plus}点!')
                                    health += health_plus
                                if health > 240:
                                    health = 240
                                magic_choose = 1
                                magic_point -= health_point
                                magic_choose = 1
                        if choose == 'B':
                            if magic_point < 70:
                                choose = input('你的魔法值不够!')
                                magic_choose = 0
                            if magic_point >= 70:
                                choose = input('你使用了战斗法术!你的攻击提高了5点,持续一回合!')
                                att_choose = 1
                                magic_choose = 1
                                magic_point -= 70
                        if choose == 'C':
                            choose = input('l͓̩̫̘͙͔̯͖̟̤̓͊̑̌́̂̆̚ò̥̪̭̱̰̝̒͂̄͋̿̏͆́̚c͍̲͇͚̖̬͈̪͙̳͌̉́̃k̪̥̱̝̱̑̈́̏̽͗̊̈́͂̀̍e̞͎̩̜̱̩͚̤̊͌̀̀d̠̖̞̝̙̪̟̞̐͛̈̊̀͂̄͌̓̏͌̓ͅ')
                            magic_choose = 0
                        choose = 0
                if choose == 'D':
                    choose = input('你跳过了你的回合')
                    magic_choose = 1
            horse_act = random.randint(1,6)
            if horse_act == 1:
                choosec = input('战争的气味在空气中迸发')
            if horse_act == 2:
                choosec = input('机械木马蓄势待发')
            if horse_act == 3:
                choosec = input('机械木马露出了恐怖的神情')
            if horse_act == 4:
                choosec = input('这是古战场吗')
            if horse_act == 5:
                choosec = input('不安和恐惧充斥着战场')
            if horse_act == 6:
                choose = input('机械感')
            fight -= 1
            jump = 0
            if bullet == 1:
                jump = 1
                bullet = 0
            if fight == 0:
                choose = input('机械木马正在准备一发重型火力攻击。')
                horse_att += 20
            while jump >= 0:
                jump -= 1
                x = random.randint(1,4)
                a = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                b = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                c = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                d = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                e = chr(ord('A') + x - 1)
                enemy_fight = a+b+c+d+e
                enemy_fighta = [a,b,c,d,e]
                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                hurt = 0
                hurtB = 0
                chance = 0
                wrong = 0
                while wrong == 0:
                    wrong = 1
                    if len(choose) != 5:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[0] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[1] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[2] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[3] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[4] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                else:
                    while chance < 5:
                        f = choose.pop()
                        g = enemy_fighta.pop()
                        if chooseb != 'B':
                            if f == 'A' and g == 'B' or f == 'B' and g == 'C' or f == 'C' and g == 'D' or f == 'D' and g == 'A':
                                if fight == 0 and horse_up == 1:
                                    hit += 1
                                hurt += att
                                chance += 1
                                if att_choose == 1:
                                    hurt += 5
                                hurt += item_att
                        if f == 'D' and g == 'C' or f == 'C' and g == 'B' or f == 'B' and g == 'A' or f == 'A' and g == 'D':
                            hurtB += horse_att
                            if chooseb == 'B':
                                hurtB -= Def
                                hurtB -= 10
                                if Def + 10>= horse_att:
                                    hurtB = 0
                            chance += 1
                        else:
                            chance += 1
                    horse -= hurt
                    health -= hurtB
                    item_att = 0
                    choose = input(f'机械木马的攻击是{enemy_fight}')
                    if chooseb != 'B':
                        choose = input(f'你对机械木马造成了{hurt}点伤害!')
                    if chooseb == 'B':
                        choose = input('因为你选择了防御,所以伤害不计入')
                    choose = input('骷髅和水晶对机械木马造成了20点伤害!')
                    horse -= 20
                    choose = input(f'你被敌人扣除了{hurtB}点血')
                    dead_interface()
                    if respawned == 1:
                        break
                    hurtB = 0
                    att_choose = 0
                    skeleton_att = 20
                    att = your_att
                if fight == 0 and horse_up == 1 and hurt > 0:
                    choose = input('你向机械木马的炮管攻去！机械木马开始松动了！')
                if fight == 0:
                    horse_att -= 20
                    choose = input('机械木马正在准备一发散弹攻击！')
                    bullet = 1
                    fight = 5
                hurt = 0
            if hit >= 5:
                choose = input('机械木马剧烈地抖动！你胜利了！')
                CM_get = random.randint(420,500)
                CM += CM_get
                choose = input(f'你获得了{CM_get}个CM币')
                win = 1
                savepoint = 4
            if horse <= 0:
                choose = input('木马的血条似乎空了……但不要以为【自我修复】的力量就这点！')
                horse += 200
        if respawned == 1:
            respawned = 0
            continue
    #做个存档点标记
    if savepoint == 4:
        save_data()
        output('机械木马发出了巨大的声响，随后轰地一声炸开，里面蹦出许多奇形怪状的小木马。')
        output('“什么精神污染……”一个骷髅说。')
        output('“算了，我们既然已经击败了它，我们就继续前进吧。”水晶说道。')
        output('你会：A：前进,B：看看木马')
        while choose not in {'A','B'}:
            print('请做出您的选择')
            output('你会：A：前进,B：看看木马')
        else:
            if choose == 'B':
                output('你看了看木马，做工非常粗糙。')
                output('突然，木马发出一阵莫名其妙的声音，听上去像是嘶吼声，你吓了一跳。')
                output('你决定不打扰它。')
        output('你们几个顺着小路向前穿过森林，来到一座城堡前。城堡粉红色的高塔和淡黄的外墙让你感觉十分轻松。')
        output('“这是文明遗迹了，你放心，这里没有战斗。”水晶说，“前面都是居住区，我们要前往的是缆车站，那是唯一一个可以前往扑克城堡的地方……呃，CRD也会在那等你，快走吧。”')
        output('你向前穿过城门，前方出现一座小镇，街道上许多奇形怪状的居民在散步。')
        output('你会：A：与居民交谈,B：与水晶交谈,C：与骷髅交谈,D：向前走')
        while choose not in {'A','B','C','D'}:
            print('请做出您的选择')
            output('你会：A：与居民交谈,B：与水晶交谈,C：与骷髅交谈,D：向前走')
        else:
            if choose == 'A':
                choose = input('一只鹿见到你说：“唔……城堡镇的居民都不太擅长谈话……你要不尝尝蛋糕？”说着塞给你一个小小的蛋糕（获得【红桃蛋糕】）')
                item.append('红桃蛋糕')
                fight_item.append('红桃蛋糕')
                view_status()
            if choose == 'B':
                output('水晶：“呃……我们继续赶路吧……”')
            if choose == 'C':
                output('一个骷髅说：“那个木马可真弱大了！就这么轻松……”')
                output('在城堡镇里不应该谈这种话题吧……”另一个骷髅说道。')
                output('“那有什么关系！居民的言论自由还……”')
                output('“什么事情都要扯到这里！这是礼节问题不是……”')
                output('“为什么这个要管！礼仪不早被罗尔斯……”')
                output('“闭嘴！你又谈令人不爽的话题了！”')
                output('水晶看着他们，无奈地说：“害，他们总是这样……”')
        output('你向前走到一座大的喷泉前，喷泉上面有一座巨大的雕像。喷泉内散落着一堆硬币。')
        output('你会：A：看雕像,B：扔硬币,C：往前走')
        while choose not in {'A','B','C','D'}:
            print('请做出您的选择')
            output('你会：A：看雕像,B：扔硬币,C：往前走')
        else:
            if choose == 'A':
                output('你看了看雕像，雕像上的人你并不认识。')
                output('“罗尔斯这家伙把国王的雕像换成了自己的？？？”一个骷髅恼怒地说。')
            if choose == 'B':
                if CM == 0:
                    output('你甚至没有硬币……')
                if CM < 0:
                    output('你是怎么做到欠了一屁股债的？')
                if CM > 0:
                    CM -= 1
                    output('你扔了个硬币进去[CM币-1]')
                    output('什么都没有发生【你 傻 了】')
        output('你们向前走到一座巨大的城楼前。一个骷髅打着哈欠说：“上面这就是缆车站了，那家伙也会出现在这儿……这个叛徒！我不想再为他服务了！”')
        output('你们穿过城楼的大门来到一条走廊之中。旁边有许多小店，不过大多数都打烊了。')
        output('“城堡镇居民不常在晚上出门的。”水晶说。你们随即走到走廊的尽头，顺着前面的楼梯走上顶楼，来到一座平台上，平台上人并不多，你向外面看去，一眼就看到了前方高山上的一座灰色的巨大城堡')
        output('“缆车站在前面，在那你就可以去扑克城堡了。不过在这时候，我要去买点东西。”水晶说')
        output('“啥？你要买东西，加我一个！”骷髅们说道，跟着水晶离开了。')
        output('你现在独自一人了。')
        output('你会：A：观景,B：去缆车站,C：买东西')
        while choose not in {'A','B','C','D'}:
            print('请做出你的选择')
            output('你会：A：观景,B：去缆车站,C：买东西')
        else:
            if choose == 'A':
                output('你看了看外面的景色，扑克城堡在暗蓝色的天空下散发出诡异的光芒。')
            if choose == 'B':
                output('你前往缆车站，发现前面的人排起了长队。')
            if choose == 'C':
                output('你好不容易找到一个小卖部，店主看到你不屑地说：“这年头哪有什么东西可以卖的。”')
        output('你漫无目的地走着，停留在一个观景平台前看着来往的缆车。突然，你感觉身后有人推了自己一把，一个熟悉的声音传来：')
        output('“嗨！我们又见面了。”')
        output('你转过身来，发现身后站着星空，不过你并没有看见CRD。')
        output('“你一定想知道我都经历了些什么，不过很无聊。我被CRD的矛弄走后一直飞到了这里，然后他让我在这儿随意走动，就跑掉了。我偷偷跟着他，发现他走到了前面的森林里，和两个骷髅和一个水晶聊了些什么，而且他的周围围了一大圈奇怪的木马……')
        output('我不知道他要做什么，不过那几个人聊完了就直接消失了，我从来都不知道CRD还能传走别人呢！我后来就来到平台上一直等。总之，你一个人穿越了遗迹，不是吗？')
        choose = input('星空打量着你，说：“遗迹的战斗看上去十分艰难，我来给你一些治疗吧。”[HPmax]')
        health = 240
        view_status()
        output('星空看了看缆车站前的长队，说道：“既然你已经来了，我也不用再担心什么了，我们排队吧。”')
        output('你会：A：答应,B：让星空等骷髅和水晶,C：让星空等CRD')
        while choose not in {'A','B','C'}:
            print('请做出您的选择')
            output('你会：A：答应,B：让星空等骷髅和水晶,C：让星空等CRD')
        else:
            if choose == 'B':
                output('星空惊讶地说：“什么？那骷髅和水晶……加入了你的队伍吗？？')
                output('“好吧……看来他们的目的只是护送你到这儿来，那现在不关他们什么事了，我们走吧。”')
            if choose == 'C':
                output('星空笑道：“CRD的传送距离其实很大，我刚才已经领会过了，所以你不用担心他。”')
        output('你们加入了缆车站前的长队，过了许久，当天色完全变黑之时，你们乘上了缆车。')
        output('缆车是一个方方整整的大盒子，充满了年代感，不过看起来是设计者刻意为之。缆车的内部只有一排座位，你们随便坐了下来。')
        output('“好吧，前面就是扑克城堡，我们的旅程马上就要结束了。”星空说')
        output('“出发啦！不过在前往城堡的过程中，你希望做点什么吗？”')
        output('你会：A：什么也不做,B：交谈,C：看后方,D：看前方')
        while choose not in {'A','B','C','D'}:
            print('请做出您的选择')
            output('你会：A：什么也不做,B：交谈,C：看后方,D：看前方')
        else:
            if choose == 'A':
                output('你什么也不做')
            if choose == 'B':
                output('星空说道：“你想知道我们究竟在哪里吗？实际上啊，我已经问过这里的人了，这里是完全的“魔法界域”，什么意思呢？这里人们的互动遵循的是魔法体系，而你的世界是“现实界域”，        人们的互动遵循现实体系。而我们的云村处于现实和魔法之间，是屏障一样的存在……算了吧你看上去有点懵，以后你就了解了。”')
            if choose == 'C':
                output('你看了看后方的平台，许多人聚集在缆车站前，吵闹声很大，不过你不清楚具体是什么。')
            if choose == 'D':
                output('你看了看前方的城堡，黑夜笼罩下的城堡仍然是一片阴森恐怖的气氛，不过城堡的亮光却比你想象的更充足。')
        output('过了好一段时间，缆车已经接近了高山上的城堡。突然，一个声音从缆车顶上传来：“可爱的小……们！！你们的旅途结束啦！”')
        output('“什么？CRD？”星空惊叫道，随后跑到窗前看了看，叫道：“你在车顶上做什么！！你……你一直在监视我们吧！”')
        output('“啊哈！真是异想天开！我们的同盟关系没有破裂！我只是想提醒一下你们，到了城堡后记得躲过扑克卫兵的剑雨哦！你们可能不知道，小镇的居民看到你们外人前往城堡，可是气得要咬死你们哦！总之，别怪我没提醒你！”')
        output('“什么？不可能！他们明明……”星空喊道，随即又停了下来。“他走了，我们必须想点办法，待会下缆车后，直接冲不要停。我的八面体可以帮你对付一些卫兵！”')
        output('随着时间一点一点过去，缆车里的气氛也越来越紧张，突然，缆车咣地一声停了下来，前面的门打开了。')
        output('星空对你说：“准备好了吗，三、二、一、我们冲！”')
        output('你们冲出缆车，来到一条小路上，城堡高耸的城墙就在眼前。')
        output('突然，城墙上传来声音：“看到了吗？就是他们！快放箭啊不对，放剑！！”')
        output('你看到一把把利剑组成剑阵，铺天盖地向你劈来。')
        chanceb = 3
        while chanceb > 0:
            if chanceb == 3:
                choose = list(input('请输入你的第一次躲避方式！'))
            if chanceb == 2:
                print('又一片剑雨齐刷刷的向你刺来！')
                choose = list(input('请输入您的第二次躲避方式！'))
            if chanceb == 1:
                print('大门近在眼前！')
                choose = list(input('请输入你的最后一次躲避方式！'))
            #又是我自己打的烂对话（
                #我想念HS了
            chanceb -= 1
            x = random.randint(1,4)
            a = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            b = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            c = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            d = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            e = chr(ord('A') + x - 1)
            enemy_fight = a+b+c+d+e
            enemy_fighta = [a,b,c,d,e]
            hurt = 0
            hurtB = 0
            chance = 0
            wrong = 0
            while wrong == 0:
                wrong = 1
                if len(choose) != 5:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(5个一组,由五个大写字母构成)'))
                elif choose[0] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(5个一组,由五个大写字母构成)'))
                elif choose[1] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(5个一组,由五个大写字母构成)'))
                elif choose[2] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(5个一组,由五个大写字母构成)'))
                elif choose[3] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(5个一组,由五个大写字母构成)'))
                elif choose[4] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(5个一组,由五个大写字母构成)'))
            else:
                while chance < 5:
                    #快悄悄这个地方,我把chance < 5写成了chance <= 5然后查了一天才查到这个bug
                    #悄悄改为瞧瞧,这是个错别字(划)通假字
                    #快看,这里我复制的前面
                        #快看，我还是复制的前面（
                    f = choose.pop()
                    g = enemy_fighta.pop()
                    if f == 'D' and g == 'C' or f == 'C' and g == 'B' or f == 'B' and g == 'A' or f == 'A' and g == 'D':
                        hurtB += 10
                        chance += 1
                    else:
                        chance += 1

                health -= hurtB
                output(f'剑以{enemy_fight}的方式向你刺去')
                output(f'你被扣除了{hurtB}点血量')
                dead_interface()
                if respawned == 1:
                    respawned = 0
                    continue
        output('你们向前通过剑阵，来到巨大但紧闭的城门前，这时一道闪光出现，城门被炸开“哪个……放的炸弹啊！！！”一个守卫喊道。')
        output('你们进入城堡，发现刚进门的区域居然是个公园。巨大的喷泉坐落于中央，你隐约看到一个路牌，上面写道：\n左：小丑乐园\n右：花园\n前：扑克城堡')

        output('前面的路被喷泉挡住了，你们只能向左或向右，而后面追兵的声音已经传来。')
        output('你会：A：向左走,B：向右走')
        while choose not in {'A','B'}:
            print('请做出您的选择')
            output('你会：A：向左走,B：向右走')
        else:
            if choose == 'A':
                output('你来到了一座大的旋转木马旁边，不过里面一个木马都没有，这里没有人。')
            if choose == 'B':
                output('你来到一座巨大的花丛前，你们没时间欣赏这些植物了。')
        output('你们抓紧时间朝前方走去，一直走到一座巨大建筑物的大门前，门没有开。')
        output('星空看了下周围地形，这里的道路向门凸了进去。“坏了，我们被堵死了。”星空说。')
        output('这时，一大群穿着重装备甲的卫兵围住了你。')
        output('“终于抓住你们了！吃我们一剑！”')
        output('剑阵从天上飞了下来，突然许多长矛横飞过来挡住了剑。')
        output('“诶等等等等，军令不统一啊！！啊哈！你们忘了我前面说过的？！星空和Zero可是我们保护的对象啊！！这就是信任哈哈哈！！我们的信用啊哈！！！”CRD突然横在卫兵前面开始长篇大论。')
        output('“你看向身旁，两个长矛飞在你身边，示意你进门。')
        if eight == 1:
            output('你会：A：进门,B：不进门,C：让星空用几何八面体攻击长矛')
            while choose not in {'A','B','C'}:
                print('请做出您的选择')
                choose = input('你会：A：进门,B：不进门')
        if eight == 0:
            output('你会：A：进门,B：不进门')
            while choose not in {'A','B'}:
                print('请做出您的选择')
                output('你会：A：进门,B：不进门')
        else:
            if choose == 'A':
                output('你碰了下城门，只听见轰的一声，城门向下直直地塌了下去，门的下方出现了一道漆黑的裂缝。你们跳过裂缝进了门。')
            if choose == 'B':
                output('你不理它，长矛突然向门冲了过去。只听见轰的一声，城门向下直直地塌了下去，门的下方出现了一道漆黑的裂缝。星空拉着你进了门。')
            if choose == 'C':
                output('几何八面体发出耀眼的闪光，长矛被你们击飞了。')
                output('CRD看到此景，叫道：“啥？这是你们对我的不信任哈哈哈！！！你们这群……！哈哈！哈！”突然门塌陷成了一堆废墟。')
                output('“这门形同虚设！快滚进去吧！小……们！”')
        output('你们进入了城堡大厅。')
        output('天花板上一个巨大的蜡烛发出明亮的火光，把大厅照得透亮')
        output('许多拿着长矛的扑克在大厅里匆匆忙忙地走着，看来是卫兵。')
        output('“别怕，那些扑克只会听别人的命令办事，它们不会主动出击，而且它们只能看到前方一排的东西。”星空悄悄对你说。')
        output('你往内部走去，进入一条走廊。左边出现了一道红色的门，上面写着：“马戏团”，右边出现了一道灰色的门，上面写着：“电影院”')
        brother = 0
        go = 0
        while go == 0:
            output('你会：A：向前走,B：去马戏团,C：去电影院')
            while choose not in {'A','B','C'}:
                print('请做出你的选择！')
                output('你会：A：向前走,B：去马戏团,C：去电影院')
            if choose == 'A':
                output('你向前走去')
                go = 1
            elif choose == 'C':
                output('你去电影院看了看，里面除了一些老式放映机，还有只通体发蓝的青蛙。')
                output('他看到你，主动凑上前朝你嚷道：“我是药剂师，你要买毒药吗？！”A：买,B：不买')
                while choose not in {'A','B'}:
                    print('请做出您的选择')
                    output('A：买,B：不买')
                else:
                    if choose == 'A':
                        output('要也不给你。”它说完就跑了')
                    if choose == 'B':
                        output('“不要也不给你。”它说完就跑了')
            elif choose == 'B':
                output('你进入马戏团，里面只有一个小丑在不断地练习杂技表演。')
                output('你会：A：交谈,B：离开')
                while choose not in {'A','B'}:
                    print('请做出您的选择')
                    output('你会：A：交谈,B：离开')
                else:
                    if choose == 'A':
                        clown = 1
                    if choose == 'B':
                        clown = 0
                while clown == 1:
                    if brother == 0:
                        output('你会谈：A：生活,B：统治者,C：你自己,D：离开')
                        while choose not in {'A','B','C','D'}:
                            print('请做出您的选择')
                            output('你会谈：A：生活,B：统治者,C：你自己,D：离开')
                    elif brother == 1:
                        output('你会谈：A：生活,B：统治者,C：你自己,D：离开,E：你兄弟')
                        while choose not in {'A','B','C','D','E'}:
                            print('请做出您的选择')
                            output('你会谈：A：生活,B：统治者,C：你自己,D：离开,E：你兄弟')
                    if choose == 'A':
                        output('“生活？我可没什么丰富多彩的生活方式，只不过每天弄点杂耍表演糊口罢了，尽管我可是……扑克皇室的御用小丑！”')
                    elif choose == 'B':
                        output('“罗尔斯？他是个混蛋啊！！！我不想多说什么，在这里并不会被他听到，可是我一想起他就烦。不过他的秘书还不错。”')
                    elif choose == 'C':
                        output('“你真的想听听关于我自己？？好吧，我曾经是扑克国王的小丑，我的代号就是小丑。负责搞些杂技表演，别以为我很凶狠，我并不会战斗，不过……呃……他……对！我兄弟就会战斗，不过你可别惹他……哦不，别遇见他，我说真的。”')
                        brother = 1
                    elif choose == 'D':
                        clown = 0
                    elif choose == 'E':
                        clown = 0
                        output('小丑对你说：“我的兄弟……曾经也是扑克城堡的御用小丑。不过呢，他会一种奇怪的，我也说不上是什么的法术……之前的扑克国王跟我说过这种法术……可以击败任何试图束缚住国家的势力。”')
                        output('“但事实上，这种法术根本就没有真正用过，我也不知道是什么样的。直到那一天，罗尔斯的军队开到城门下面，扑克国王才想到他。        不过，不知道什么原因，他并没有使用法术……最后罗尔斯占领城市时把他关了起来……关在监狱最阴暗的角落里，再也没人能见到他。”')
                        output('小丑看了看你们。“嗯……罗尔斯这家伙……贸然击败似乎是不可能的，但如果有他的帮助……不可能！以他的性格，绝对不会帮你们，但他或许能够使用某种手段自己破坏罗尔斯的屏障……那世界会乱套的！”')
                        output('“不过，你们是罗尔斯和CRD都中意的人，如果让你们来处理他，也未尝不可嘛，尽管把他放出来……肯定会闹出大乱子，不过，说句自私的，我早就习以为常啦。”')
                        choose = input('“如果你们想去见他，就拿上这个【监狱钥匙】，去监狱里找旧国王吧。”')
                        if '监狱钥匙' not in item:
                            item.append('监狱钥匙')
                        view_status()
                        output('说完，小丑把一块奇怪的东西塞到你手里')
                        if '占位卡' in item:
                            output('你们刚想走出马戏团，小丑突然叫住了你：“嘿，你身上有一张奇特的卡片，这种卡片所散发的能量极为强大，我可以用魔法把这个卡片转化为强力的道具，把它给我。”')
                            output('还没等你给他，那张占位卡就自动从你的身上向他飞了过去。')
                            choose = input('小丑捣鼓了一会儿后，给了你一叠奇怪的扑克，说道：“拿上这些扑克！他们的力量极为强大！”')
                            item.remove('占位卡')
                            item.append('混乱护盾')
                            #there is yincang line(((
                            view_status()
                        output('你们走出马戏团，来到前面的监狱。')
                        output('这里用铁闸门关着许多人。')
                        talk = 0
                        while talk == 0:
                            output('你会：A：找个囚犯交流,B：继续深入')
                            while choose not in {'A','B'}:
                                print('请做出您的选择')
                                output('你会：A：找个囚犯交流,B：继续深入')
                            else:
                                if choose == 'A':
                                    event = random.randint(1,5)
                                    if event == 1:
                                        AA = '“啊啊啊啊啊啊啊我要回几何平原平原平原平原……”'
                                    if event == 2:
                                        AA = '“我不是什么好人，放我走吧求求你了！”'
                                    if event == 3:
                                        AA = '“我是个是红桃6，有天我说我比红桃7要大，罗尔斯听到了就把我送进来了！放我出去！！”'
                                    if event == 4:
                                        AA = '“我动了黑桃炸弹！！呜呜呜呜疼死我了！”'
                                    if event == 5:
                                        AA = '“我是个音游人，我从城市来，这里没miamia打，我问他们有没有街机他们就把我关了起来！什么东西啊！”'#miamia草
                                    output(AA)
                                elif choose == 'B':
                                    talk = 1
                                    output('你往监狱深处走去，这里有一扇锁着的门。')
                                    output('你们拿出钥匙，那把钥匙突然飞到了空中，转了个圈冲向门，把门撞破了。')
                                    output('你们走近门的里面，通过一条漆黑的通道，来到了一间大房间，房间里的一个大铁笼子关着四个奇怪的人。每个人都穿着十分花哨的服饰。')
                                    output('其中一个穿着黑桃服饰的人看见了你们，说：“你们？你们来这里做什么？”')
                                    output('星空看了看他们，说道：“你们是？”')
                                    output('“我们是以前的扑克国王……”')
                                    output('“什么？扑克国王……有四个？”')
                                    output('“对，我们每个人代表一种花色的K，根据花色的不同来决定管理的不同。草花决定财政，红心决定民生，方块决定娱乐，黑桃决定军事……你们为什么要来这里？”')
                                    output('星空说：“我们想找一个有着奇异魔法，可以击败罗尔斯势力的人，你们知道他在哪吗？”')
                                    output('国王们面面相觑，“这怎么可能啊？没有人能击败罗尔斯啊……”')
                                    output('“真的没有吗，那个小丑说有哦。”星空说。')
                                    output('“小丑？”黑桃国王突然想到了什么。“你不会再说他吧？那个人确实可以击败罗尔斯，只是……他不知道为什么并没有使用法术。最后还是被罗尔斯俘虏了……怎么？你们想见他？”')
                                    output('“对啊。”星空回答。')
                                    output('“如果你们想见他，你们就要去花园找他，花园那里有隐藏的监狱，他被关在那里……这是另一个人告诉我的，他自愿成为我们的卧底，而且似乎混到了个不错的职位。不过他也不想打扰那人。”')
                                    output('“花园在哪？”星空问')
                                    output('“这我就不知道了，但肯定不是城堡外面的花园，这城堡本来根本就没有监狱，罗尔斯在这儿自己修建了监狱，鬼知道他能把监狱建在哪里，不过外面那花园我反复走过，哪里根本就不可能存在监狱，太平坦了。”')
                                    output('星空看了看你，说道：“现在我们要找到花园！”')
                                    output('你看了看面前的房间，除了关着国王们的大笼子外，只有一张挂历在墙上，房间里还有许多蜡烛状的灯。')
                                    king = 0
                                    while king == 0:
                                        output('你会：A：与国王交谈.B：看挂历,C：看灯')
                                        while choose not in {'A','B','C'}:
                                            print('请做出您的选择')
                                            output('你会：A：与国王交谈.B：看挂历,C：看灯')
                                        else:
                                            if choose == 'A':
                                                output('国王说：“我们没什么可谈的，我们今天才被关进来，我也不知道为什么会这样，不过听说这里来了两个新人，一男一女，听说他们可以破坏罗尔斯的屏障带领我们走向自由……”')
                                                output('国王看向你们，似乎察觉到了什么，突然说：')
                                                output('“不会就是你们吧？！”')
                                                output('没等你们回答，国王就说：“哈！一定是的，看来救赎肯定会到来，只是时间问题罢了。我给你们一个提示，那个人告诉我，罗尔斯有一位特殊犯人，他的监狱编号是J12132，希望这能对你有用。”')
                                            elif choose == 'C':
                                                output('你看了看灯，没发现什么异常')
                                            elif choose == 'B':
                                                output('你看了看挂历，没什么异常，正当你准备将它放下，你的手突然碰到了一个粗糙的地方，你把它拿起来看了看，发现这是隐藏在挂历背面的一组小小的齿轮，一共有五个，随着你的操作，齿轮上面能呈现出不同的数字。')
                                                output('你会将数字拨到？(请输入数字)')
                                                if choose != '12132':
                                                    output('什么事情都没有发生')
                                                else:
                                                    king = 1
                                                    output('突然，你听到一阵奇异的响动，你发现房间的墙壁上突然出现了一条通道。')
                                                    output('国王对你们说：“这应该就是通往花园的通道了，快去找他吧。”')
                                                    output('你们穿过通道，来到了室外。这里是一片小小的草坪，长满了各种各样的野花。草坪夹在许多大的建筑中，十分杂乱不堪，让你们感觉这不像花园而像一块荒地。')
                                                    output('你踩在花丛上四处张望，发现前面有一座小小的石头建筑。')
                                                    output('你们来到石头建筑前。突然，你们看见那把奇异的钥匙飞到了你们面前，冲向建筑的门，砰地一声把门撞破了，但钥匙自己也被撞得粉碎')
                                                    item.remove('监狱钥匙')
                                                    output('你们进入建筑，里面只有微量的火光，几乎漆黑一片，你们向前走去，走了好久才碰到一堵墙壁。')
                                                    output('你们正想掉头往回走，突然，墙壁后面传来了一阵令人毛骨悚然的笑声！')
                                                    output('你们赶快凑到墙壁上，那个声音对你们说')
                                                    output('“嘻嘻嘻……是人的感觉……这里有人……嘻嘻……如果你能进来……我会让你……感受到……前所未有的……快乐……嘻嘻嘻……”')
                                                    output('星空说：“你是谁？”')
                                                    output('“我……是一个普通人……被罗尔斯关……到了这里……如果你们能……把我救出来……我将会……使你们的世界……充满……自由……自由……自由…………”')
                                                    output('星空继续问道：“我们怎么救你出来？这里看上去没有门。”')
                                                    output('“嘻嘻嘻……为什么要有门……难道没有门……就不能过来了吗……”')
                                                    output('星空和你对视了一下。')
                                                    output('“拿上你的武器……朝墙壁轰过来……墙就会坏……快点……星空！”')
                                                    output('一听到自己的名字，星空有点震惊：“你是怎么知道我的名字的？”')
                                                    output('“嘻嘻嘻……我什么都知道……快开门吧……”')
                                                    output('你们有点束手无策。')
                                                    output('你会：A：“开门”,B：不开门')
                                                    while choose not in {'A','B'}:
                                                        print('请做出您的选择')
                                                        output('你会：A：“开门”,B：不开门')
                                                    if choose == 'A':
                                                        output('“嘻嘻嘻……这就对啦……快开门吧……”声音传来，星空拿出自己的几何八面体，朝墙上轰了一个大洞。')
                                                    elif choose == 'B':
                                                        output('“什么……你们不想开门……都走到这里了……你们还想放弃……”星空的几何八面体毫无预警地从身上飞了出来，朝墙上轰了个大洞。')
                                                    savepoint = 12132
                                                    talk = 1
                                                    go = 1

    #做个存档点标记
    if savepoint == 12132:
        save_data()
        output('你们朝着洞口走了进去，来到一个大房间，借着微光，你们看到房间里是一个小丑模样的人。')
        output('“嘻嘻嘻……你们终于进来啦……只需要完成下一步……我们都可以重获自由啦……”小丑说')
        output('星空对他说：“你想干什么？”')
        output('“嘻嘻嘻……我不想干什么……我只想……增大世界的无序度……熵……嘻嘻嘻……我忘了这是宏观世界哩……总之……我要使用我的……混沌魔法……把你们全部卷入一片大混沌里……你们就自由啦……”')
        output('“什么？混沌？”星空叫道')
        output('“对……混沌……你们……现在开始……所有人……都将卷入混沌的海洋里……让我们……开始吧……”')
        output('小丑对你们发出了恐怖的怪笑。')
        print('战斗开始,对战【J12132】')
        joker_att = 22
        surprise = 0
        surprise_B = 0
        surprise_C = 0
        surprise_D = 0
        time = 2
        t.sleep(0.5)
        joker = 2132
        chaos = 0
        magic_point = 0
        win = 0
        a,b,c,d,e = '','','','',''
        eight = 0
        while win == 0:
            hurt = 0
            hurtB = 0
            chance = 0
            wrong = 0
            item_att = 0
            magic_choose = 0
            att_choose = 0
            item_choose = 0
            if surprise == 0 and (joker <= 1600 or chaos >= 100) and surprise_D == 0:
                surprise_B = 1
                surprise_D = 1
            while magic_choose == 0 and item_choose == 0:
                magic_D = magic_point / 2
                chooseb = 'A'
                print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health},J12132血量为{joker},混沌值为{chaos}')
                choose = input('A,物品B,防御C,魔法D,跳过')
                while choose not in {'A','B','C','D'}:
                    print('请做出你的选择')
                    choose = input('A,物品B,防御C,魔法D,跳过')
                if choose == 'A':
                    choose = input(f'你现在可使用的物品有{fight_item},请从1开始输入序号以选择使用的物品')
                    if choose not in {'1','2','3','4','5','6','7','8','9','10'}:
                        choose = input('物品序号输入错误!')
                    else:
                        choose = int(choose)
                        if choose > len(fight_item):
                            choose = input('物品序号输入错误!')
                        else:
                            item_find()
                            if check == '魔法炸药':
                                choose = input('你对对方造成了100点伤害!但你也不小心受到了30点伤害')
                                health -= 30
                                joker -= 100
                                dead_interface()
                                if respawned == 1:
                                    break
                            if check == '坚硬冰棍':
                                choose = input('你使用了坚硬冰棍!敌方的HP降低了100点!')
                                joker -= 100
                            item.remove(check)
                            fight_item.remove(check)
                            item_choose = 1
                            if health > 240:
                                health = 240
                if choose == 'B':
                    choose = input('你选择了防御!')
                    magic_point += 40
                    magic_choose = 1
                    if magic_point >= 100:
                        magic_point = 100
                    chooseb = 'B'
                if choose == 'C':
                    choose = input(f'A：治疗魔法（{health_point}）B：战斗魔法（70）C：黑暗魔法（？）D：几何八面体（{magic_point}）')
                    while choose not in {'A','B','C','D'}:
                        print('请做出你的选择')
                        choose = input(f'A：治疗魔法（{health_point}）B：战斗魔法（70）C：黑暗魔法（？）D（{magic_point}）')
                    else:
                        if choose == 'A':
                            if magic_point < health_point:
                                choose = input('你的魔法值不够!')
                                magic_choose = 0
                            if magic_point >= health_point:
                                if '生命宝石' not in item:
                                    choose = input(f'你使用了治疗法术!你的血量回复了{health_plus}点!')
                                    health += health_plus
                                if '生命宝石' in item:
                                    choose = input(f'你使用了治疗法术!你的血量回复了{health_plus}点!')
                                    health += health_plus
                                magic_choose = 1
                                magic_point -= health_point
                            if health > 240:
                                health = 240
                                magic_choose = 1
                        if choose == 'B':
                            if magic_point < 70:
                                choose = input('你的魔法值不够!')
                                magic_choose = 0
                            if magic_point >= 70:
                                choose = input('你使用了战斗法术!你的攻击提高了5点,持续一回合!')
                                att_choose = 1
                                magic_choose = 1
                                magic_point -= 70
                        if choose == 'C':
                            choose = input('l͓̩̫̘͙͔̯͖̟̤̓͊̑̌́̂̆̚ò̥̪̭̱̰̝̒͂̄͋̿̏͆́̚c͍̲͇͚̖̬͈̪͙̳͌̉́̃k̪̥̱̝̱̑̈́̏̽͗̊̈́͂̀̍e̞͎̩̜̱̩͚̤̊͌̀̀d̠̖̞̝̙̪̟̞̐͛̈̊̀͂̄͌̓̏͌̓ͅ')
                            magic_choose = 0
                        if choose == 'D':
                            if magic_point <= 0:
                                print('您的魔法值不能为0！')
                            else:
                                light_cube = 1
                                choose = input(f'你使用了几何八面体,你对敌方造成了{magic_D}点伤害!')
                                joker -= magic_D
                                magic_choose = 1
                                magic_point = 0
                        choose = 0
                if choose == 'D':
                    choose = input('你跳过了你的回合')
                    magic_choose = 1
            if surprise == 0:
                joker_act_B = random.randint(1,7)
            if surprise == 1:
                joker_act_B = random.randint(8,10)
            if joker_act_B == 1:
                choosec = input('战斗在混沌中展开')
            if joker_act_B == 2:
                choosec = input('是谁给世界带来这种混乱的？')
            if joker_act_B == 3:
                choosec = input('战斗看来不会结束')
            if joker_act_B == 4:
                choosec = input('你尚未感觉到自由')
            if joker_act_B == 5:
                choosec = input('小丑发出了恐怖的笑声')
            if joker_act_B == 6:
                choosec = input('来耍我啊，蠢货')
            if joker_act_B == 7:
                choosec = input('为了那片混沌')
            if joker_act_B == 8:
                choosec = input('小丑发出了凄厉的怪叫')
            if joker_act_B == 9:
                choosec = input('空气中散布着自由')
            if joker_act_B == 10:
                choosec = input('快结束这一切吧')
            if chooseb != 'B' and surprise_B != 1:
                joker_act_C = random.randint(1,4)
                if joker_act_C == 1:
                    input('小丑使用了“方块箭矢”！')
                    choosec = input('你会：A：进攻 B：格挡')
                    while choosec not in {'A','B'}:
                        choosec = input('你会：A：进攻 B：格挡')
                    if choosec == 'A':
                        chaos += 2
                        hurt = random.randint(3,30)
                        health -= hurt
                        hurt = 0
                    elif choosec == 'B':
                        choose = input('你尽可能地格挡箭矢的进攻')
                        plus = random.randint(1,5)
                        chaos += plus
                        plus = 0
                if joker_act_C == 2:
                    input('小丑使用了“红心治疗”！')
                    choosec = input('你会：A：进攻 B：诅咒')
                    while choosec not in {'A','B'}:
                        choosec = input('你会：A：进攻 B：诅咒')
                    if choosec == 'A':
                        chaos += 4
                        plus = random.randint(5,50)
                        joker += plus
                        plus = 0
                    elif choosec == 'B':
                        choose = input('你诅咒小丑的治疗法术，小丑的法术失效了！')
                        chaos += 1
                if joker_act_C == 3:
                    input('小丑使用了“草花守护”！')
                    hit = random.randint(1,5)
                    guess = 8
                    choosec = input('你会：A：进攻 B：打散')
                    while choosec not in {'A','B'}:
                        choosec = input('你会：A：进攻 B：打散')
                    if choosec == 'A':
                        chaos += 3
                        joker_att += hit
                    elif choosec == 'B':
                        choose = input('你用力向草花打去')
                        chaos += random.randint(1,5)
                        guess = random.randint(1,10)
                        if guess > 7:
                            joker_att += hit
                if joker_act_C == 4:
                    input('小丑使用了“黑桃炸弹”！')
                    choosec = input('你会：A：进攻 B：闪躲')
                    while choosec not in {'A','B'}:
                        choosec = input('你会：A：进攻 B：闪躲')
                    if choosec == 'A':
                        chaos += 5
                        joker_att += random.randint(5,10)
                    elif choosec == 'B':
                        choose = input('你拼命闪躲着炸弹，你的防御增加了！')
                        chaos += random.randint(1,3)
                        joker_att += random.randint(1,5)
            if surprise_B == 1:
                choosec = input('小丑正在准备“混沌冲击”')
                joker_att += 5
                surprise_C = 1
            while surprise_B >= 0:
                surprise_B -= 1
                x = random.randint(1,4)
                a = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                b = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                c = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                d = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                e = chr(ord('A') + x - 1)
                enemy_fight = a+b+c+d+e
                enemy_fighta = [a,b,c,d,e]
                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                while wrong == 0:
                    wrong = 1
                    if len(choose) != 5:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[0] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[1] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[2] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[3] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[4] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                else:
                    joker_act = random.randint(1,100)
                    while chance < 5:
                        f = choose.pop()
                        g = enemy_fighta.pop()
                        if chooseb != 'B':
                            if f == 'A' and g == 'B' or f == 'B' and g == 'C' or f == 'C' and g == 'D' or f == 'D' and g == 'A':
                                hurt += att
                                chance += 1
                                if att_choose == 1:
                                    hurt += 5
                                if joker_act > 77:
                                    hurt -= 31
                                if surprise_C == 1 or (joker_act_C == 3 and guess > 7) or (joker_act_C == 1 and choosec == 'B'):
                                    hurt -= 12132
                                if hurt <= 0:
                                    hurt = 0
                        if f == 'D' and g == 'C' or f == 'C' and g == 'B' or f == 'B' and g == 'A' or f == 'A' and g == 'D':
                            if surprise_C == 1:
                                joker_att = random.randint(20,40)
                            hurtB += joker_att
                            if chooseb == 'B':
                                hurtB -= Def
                                if Def >= 15:
                                    hurtB = 0
                            chance += 1
                        else:
                            chance += 1
                joker -= hurt
                health -= int(hurtB * 1.5)
                if surprise_C == 1 and health <= 0:
                    health = 1
                surprise_C = 0
                choose = input(f'敌方的攻击是{enemy_fight}')
                if joker_act > 3 :
                    choose = input('J12132使用了防御!')
                if chooseb != 'B':
                    output(f'你对J12132造成了{hurt}点伤害!')
                    hurt = 0
                if chooseb == 'B':
                    choose = input('因为你选择了防御,所以伤害不计入')
                if joker_act <= 77:
                    choose = input('星空对J12132造成了20点伤害!')
                    joker -= 20
                if joker_act > 77:
                    choose = input('星空对J12132造成了0点伤害!')
                    joker -= 0
                choose = input(f'你被敌人扣除了{hurtB}点血量')
                joker_att = 22
                dead_interface()
                if respawned == 1:
                    break
                hurtB = 0
                att_choose = 0
            surprise_B = 0
            if joker <= 1500:
                choose = input('您获胜了!')
                win = 1
                savepoint = 12
            if chaos >= 100:
                choose = input('混沌盘旋着毁灭了战场，你胜利了。')
                win = 1
                savepoint = 23121

        if respawned == 1:
            respawned = 0
            continue
    #做个存档点标记
                
    if savepoint == 23121:
        save_data()
        if joker <= 1500 and chaos < 120:
            output('小丑说：“嘻嘻嘻……你们……很强……很强……但……即使再强……也逃不过……他……的手心……他是上帝……不是……比上帝更强        ……他是一切……万物的主宰……如果你们足够强……你们……就跑……赶快……跑出这个世界吧……这样……你们就会……获得……自由……”')
            output('星空有些迷糊：“呃，等等，你在说些什么啊……”')
            output('“嘻嘻嘻……混沌法术……只不过是……一般的混沌而已……不存在真正的混沌……什么都不存在……我们是棋子……        我们被规则束缚……我们逃不过……逃不过……但你们或许可以……所以……马上……用我的力量……打败虚空的电视主持人……获得自由吧……”')
            choose = input('小丑突然颤抖起来，震动越来越剧烈，最后在你面前变化成了一把小刀（获得【混沌匕首】）')
            item.append('混沌匕首')
            view_status()
            output('你们快速跑出了这里。')
        else:
            output('小丑对你们发出怪笑：“嘻嘻嘻……混沌……你们终于……陷入了这片混沌……太棒啦……我们终于……可以……无限地……玩下去……玩下去……玩下去……”')
            output('小丑在怪笑中开始像戳破的皮球一样泄气，最后只剩下一具空壳。')
            output('“这……精神污染……”星空有点吃惊地说道')
            output('你想快点逃离这个恐怖的地方。')
            output('你会：A：逃跑,B：再看看')
            while choose not in {'A','B'}:
                print('请做出您的选择')
                output('你会：A：逃跑,B：再看看')
            if choose == 'A':
                output('你们快速跑出了这里。')
            elif choose == 'B':
                choose = input('你翻着空壳看了看，突然在空壳里发现了一只奇怪的剑（获得【零剑】），你们快速跑出了这里。')
                item.append('零剑')
                view_status()
        output('你们跑出长长的通道，回到监狱里面')
        output('你会：A：找国王,B：找小丑,C：离开')
        while choose not in {'A','B','C'}:
            print('请做出您的选择')
            output('你会：A：找国王,B：找小丑,C：离开')
        if choose == 'A':
            output('你们找到了国王们')
            output('国王说：“啊，你们来了，看来你们已经见到他了……或者你们因为怕了根本没见他？”')
            output('“我们见过了。”星空回答。')
            output('“害，真好，那么，他同意破坏罗尔斯的秩序了？”')
            output('“他那么疯疯癫癫的，我们怎么知道他想干什么……”')
            output('“疯癫？看来监狱生活已经让他疯了……他本来不这样的。不过……呃……他说有一天一个人找到了他，那人说的话导致他很害怕……估计就是因为这个导致他疯癫的吧……”')
            output('国王无奈地摊了摊手：“看来你们可帮了罗尔斯忙咯，他的心腹大患被你解决了……不过这种情况下也不会更坏。你们离开吧，不用管我们，我们到时候就会出去了。”')
            output('你们离开监狱')
        elif choose == 'B':
            output('你们来到马戏团，找到小丑。小丑看了看你们：“你们看起来已经遇到我兄弟了……”')
            output('“是的。可是他似乎有点不太正常……”')
            output('“他正常的话才不正常。早些时候他遇到了一个人，不知道是谁，那人对他说了一番话，导致他整天精神恍惚。我也不知道发生了些什么，可能就是因为这些话，导致他没有抵抗罗尔斯的吧。”')
            output('“不过呢，虽然没人知道他到底听到了些什么，但我知道大概。”')
            output('听到这话，你们凑近了小丑。')
            output('“他在战斗前一天晚上，对我说了些奇怪的话，大概就是关于战斗的细节、规划之类的，但后面他又话题一转，跟我聊以后的生活。”')
            output('“突然，他抬起头神秘地看着我，笑着说：‘不过，这一切都改变不了。’”')
            output('“我怀疑那人跟他说了些关于命运决定论的话，他信了，于是就成这样了。只不过……他以前不是个很迷信的人……”')
            output('“不管怎么样，你们击败他了，那就继续前进吧。毕竟，你们在前面会遇到比他更凶恶的敌人，希望你们可以击败他。”')
        elif choose == 'C':
            output('你离开了')
        savepoint = 4
        

    #END又挖了一个坑，他连废弃小店都没填
    if savepoint == 4:
        save_data()
        output('前面出现了三道门，一道写着“礼堂”，一道写着“监狱”，还有一道写着“通向二楼”')
        second_floor = 0
        while second_floor == 0:
            output('你会：A：去礼堂,B：去监狱,C：上二楼')
            while choose not in {'A','B','C'}:
                print('请做出您的选择')
                output('你会：A：去礼堂,B：去监狱,C：上二楼')
            else:
                if choose == 'A':
                    output('你们来到礼堂，座位上坐着几个长得很奇怪的人，看起来是国际象棋棋子。其中一个拿着十字架，一个像马，还有一个看起来只是普通的小兵。')
                    output('星空说：“我们不妨交谈交谈，或许可以得到什么线索！”')
                    chess = 0
                    while chess == 0:
                        output('你会：A：和兵交谈,B：和马交谈,C：和拿着十字架的人交谈,D：离开')
                        while choose not in {'A','B','C','D'}:
                            print('请做出您的选择')
                            output('你会：A：和兵交谈,B：和马交谈,C：和拿着十字架的人交谈,D：离开')
                        else:
                            if choose == 'A':
                                output('他断断续续地说：“我是……兵……我来自……棋盘……联邦……呃……王和后……死掉啦……没……”')
                            if choose == 'B':
                                output('他似乎有点不满，示意你滚开。')
                                output('“别这样啊……”星空自言自语道。')
                            if choose == 'C':
                                output('他对你说：“我是主教。我发现这里的扑克不适合传教，因为他们只听自己上级的，这在我的传教生涯中可从未……不遇见过。”')
                            chess = 1
                if choose == 'B':
                    choose = input('你来到监狱，这里用铁闸门关着许多人。')
                    talk = 0
                    while talk == 0:
                        choose = input('你会：A：找个囚犯交流,B：继续深入,C：离开')
                        while choose not in {'A','B','C'}:
                            print('请做出您的选择')
                            choose = input('你会：A：找个囚犯交流,B：继续深入,C：离开')
                        else:
                            if choose == 'A':
                                event = random.randint(1,5)
                                if event == 1:
                                    AA = '“啊啊啊啊啊啊啊我要回几何平原平原平原平原……”'
                                if event == 2:
                                    AA = '“我不是什么好人，放我走吧求求你了！”'
                                if event == 3:
                                    AA = '“我是个是红桃6，有天我说我比红桃7要大，罗尔斯听到了就把我送进来了！放我出去！！”'
                                if event == 4:
                                    AA = '“我动了黑桃炸弹！！呜呜呜呜疼死我了！”'
                                if event == 5:
                                    AA = '“我是个音游人，我从城市来，这里没miamia打，我问他们有没有街机他们就把我关了起来！什么东西啊！”'#miamia草
                                output(AA)
                            if choose == 'B':
                                output('你往监狱深处走去，这里有一扇锁着的门。')
                            if choose == 'C':
                                output('你离开了这里')
                                choose == 0
                                talk = 1
                if choose == 'C':
                    output('你前往二楼')
                    second_floor = 1
        output('你走上二楼楼梯，突然你听见身后传来熟悉的声音：')
        output('“啊哈！我来特别提醒一下，二楼的人可不归我管，你们可得当心它们咯！”说完，CRD转身向后走去。')
        output('星空正要追问，突然楼上下来几个扑克围住了你们。')
        output('“吃我们剑阵！！！”扑克说')
        fight('扑克守卫',180,5,20,20,random.randint(100,300),'xk',2)
        if respawned == 1:
            respawned = 0
            continue
        output('你们击败了扑克守卫，它们丢下剑逃跑了。')
        output('“罗尔斯的护卫居然是这种懦夫吗……”星空说道。')
        output('你们继续往前走，来到城堡的二楼，你们前面又出现了一条十分长的走廊。走廊的墙上挂着许多扑克。')
        output('你们向前走，突然你发现一张桌子上盖着个盖子，不知道里面有什么。')
        output('你会：A：打开盖子,B：检查桌子,C：看扑克,D：向前走')
        while choose not in {'A','B','C','D'}:
            print('请做出您的选择')
            output('你会：A：打开盖子,B：检查桌子,C：看扑克,D：向前走')
        else:
            if choose == 'A':
                output('你打开盖子，里面装着一把长剑（获得【J型剑】）')
                item.append('J型剑')
            if choose == 'B':
                output('你在桌子下面找到了个脏兮兮的略微透明的短裙，你觉得这和你挺配的（获得【水晶联结裙】）')
                item.append('水晶联结裙')
            if choose == 'C':
                output('你看着墙上的扑克，没有发现一张黑桃。')
        output('你们继续向前走，来到一个大厅。许多扑克站在这里，一个人站在前面的讲台上大声喊道：')
        output('“怎么！怎么！怎么！怎么还惦记者你们的轨迹！你们！你们！你们！你们必须配合我完成我们的谜题！这样才能耗死星空他丫的！”')
        output('扑克和那人似乎都没有看见你们')
        output('你会：A：小心翼翼地摸向前进,B：待在原地不动,C：原路返回')
        while choose not in {'A','B','C'}:
            print('请做出您的选择')
            output('你会：A：小心翼翼地摸向前进,B：待在原地不动,C：原路返回')
        else:
            if choose == 'A':
                output('你们向前摸去')
            if choose == 'B':
                output('你们待在原地不动')
            if choose == 'C':
                output('你们原路返回，但刚才走廊上的地板全都消失了！只剩下空空的楼架。你们只好回到大厅。')
        output('你们听到台上那人大声说：“我！我！我！我城堡谜题制作者迈克！绝对！绝对！绝对！绝对不允许你们在配合我们谜题时犯傻！犯傻的人要——”')
        output('“获得CRD特享长矛硬糖一份哦！！！！！！！！！！”另一个声音传来，你们看见CRD从不知道哪个地方从天而降落到那人面前。')
        output('“好家伙！CRD，你要和我对着干对吧！你！你！你！你等着！”说完那人拿出大刀杀向CRD，CRD身边出现了几个长矛顶飞了大刀。')
        output('“啊哈！你这纸老虎根本吓不倒我！再会啦，迈克！记得在三楼领取糖果！”')
        output('“领取你个头！！！”迈克想冲向CRD，结果踩在自己的大刀上滑了一跤，CRD趁机跑走了。')
        output('“啊啊啊啊啊啊啊啊啊！！！！”迈克大声喊道，给我杀了他啊啊啊啊！！！”')
        output('这时，有个扑克看见了你们，它以为迈克是给自己下命令，于是朝你们喊道：“杀了他们！”')
        output('剑阵再次从天而降。')
        chanceb = 2
        while chanceb > 0:
            if chanceb == 2:
                choose = list(input('请输入你的第一次躲避方式！'))
            if chanceb == 1:
                print('又一片剑雨齐刷刷的向你刺来！')
                choose = list(input('请输入您的第二次躲避方式！'))
            #又是我自己打的烂对话（
                #我想念HS了
            chanceb -= 1
            x = random.randint(1,4)
            a = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            b = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            c = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            d = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            e = chr(ord('A') + x - 1)
            enemy_fight = a+b+c+d+e
            enemy_fighta = [a,b,c,d,e]
            hurt = 0
            hurtB = 0
            chance = 0
            wrong = 0
            while wrong == 0:
                wrong = 1
                if len(choose) != 5:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(5个一组,由五个大写字母构成)'))
                elif choose[0] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(5个一组,由五个大写字母构成)'))
                elif choose[1] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(5个一组,由五个大写字母构成)'))
                elif choose[2] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(5个一组,由五个大写字母构成)'))
                elif choose[3] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(5个一组,由五个大写字母构成)'))
                elif choose[4] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(5个一组,由五个大写字母构成)'))
            else:
                while chance < 5:
                    f = choose.pop()
                    g = enemy_fighta.pop()
                    if f == 'D' and g == 'C' or f == 'C' and g == 'B' or f == 'B' and g == 'A' or f == 'A' and g == 'D':
                        hurtB += 10
                        chance += 1
                    else:
                        chance += 1

                health -= hurtB
                choose = input(f'剑以{enemy_fight}的方式向你刺去')
                choose = input(f'你被扣除了{hurtB}点血量')
                dead_interface()
                if respawned == 1:
                    respawned = 0
                    continue
        output('你们躲过剑阵，前方又是一道楼梯。你向前冲去。突然，脚下的地板在你踩上去的瞬间向下塌陷。你重心不稳向前跌去。前面有一根硬钢管，你使劲抓住了它悬在空中。')
        output('“Zero？你没事吧？”星空在后面向你喊道。')
        output('突然，你看见之前的那个人出现在楼梯上，对你们摆出一脸恶相：“好啊！你！你！你！你们这群东西，竟敢亲自给我迈克送上门来，那么现在，你们就在城堡危险的谜题里等着死吧！！！”说完，迈克走上楼梯消失了。')
        output('你仍然抓着钢管，但你的下面出现了许多带刺的齿轮，飞速旋转着向你升来。')
        output('你会：A：爬到其它地方去 B：跳到齿轮上 C：用脚试探着拨齿轮 D：用武器试探着拨齿轮')
        while choose not in {'A','B','C','D'}:
            print('请做出您的选择')
            output('你会：A：爬到其它地方去 B：跳到齿轮上 C：用脚试探着拨齿轮 D：用武器试探着拨齿轮')
        if choose == 'A':
            output('你爬到了钢管的另一侧，但是这下面仍有许多齿轮向你飞升过来。')
            choose = 'B'
        if choose == 'D':
            if att >= 35:
                output('你用武器抵住齿轮，突然，齿轮转速慢了一点，天上掉下许多地砖悬浮在齿轮上方，你踩上地砖向前跑去。')
                falling = 1
            elif '零剑' in item or weapon == '零剑':
                event = random.randint(5,50)
                if event >= 20:
                    output('你用武器抵住齿轮，突然，齿轮转速慢了一点，天上掉下许多地砖悬浮在齿轮上方，你踩上地砖向前跑去。')
                    falling = 1
            else:
                input('你扔下武器，但是齿轮没有丝毫动静。你只能跳到齿轮上')
                view_status()
                choose = 'B'
        if choose == 'B':
            output('你跳到齿轮上。忍住尖刺扎进皮肤的痛苦跳向前面的齿轮，齿轮不断上升，最后升到了与楼梯相同的高度，你跃上前面的楼梯。[HP-50]')
            falling = 10
            health -= 50
            dead_interface()
            if respawned == 1:
                respawned = 0
                continue
            view_status()
        if choose == 'C':
            input('你用脚试探着拨齿轮，齿划破了你的脚[HP-30]，你试着抵住齿轮的转动，突然，齿轮转速慢了一点，天上掉下许多地砖悬浮在齿轮上方，你踩上地砖向前跑去。')
            view_status()
            health -= 30
            falling = 1
            dead_interface()
            if respawned == 1:
                respawned = 0
                continue
        input('你站上了楼梯')
        if falling == 1:
            input('地砖再次往下掉落，齿轮也消失不见。')
            view_status()
        else:
            input('齿轮顿时向下坠落。')
            view_status()
        output('星空在你的对面朝你喊道：“Zero，继续前进吧！不用担心我，我很快就会过来的！”说完就向后走去。')
        output('你又独自一人了。')
        output('你走上楼梯，来到城堡的三楼。你的前面出现了一个石台，你似乎在前面的冒险中已经见过了这东西。')
        output('石台上放了一些糖果，想拿几个？')
        output('A：不拿 B：拿一个 C：拿两个 D：拿三个 E：拿更多')
        while choose not in {'A','B','C','D','E'}:
            print('请做出您的选择')
            output('A：不拿 B：拿一个 C：拿两个 D：拿三个 E：拿更多')
        if choose == 'A':
            input('你没有获得糖果')
            view_status()
        elif choose == 'B':
            input('你获得了【CRD硬糖】')
            view_status()
            item.append('CRD硬糖')
            fight_item.append('CRD硬糖')
        elif choose == 'C':
            input('你获得了【CRD硬糖】*2')
            view_status()
            for i in range(2):
                item.append('CRD硬糖')
                fight_item.append('CRD硬糖')
        elif choose == 'D':
            input('你获得了【CRD硬糖】*3')
            view_status()
            for i in range(3):
                item.append('CRD硬糖')
                fight_item.append('CRD硬糖')
        elif choose == 'E':
            input('你并不爱吃甜食，你感到有点反胃，你吧所有糖果都放了回去。')
            view_status()
        input('你向前走去，又遇到了一个十字路口。你的左边写着“画廊”、右边写着“澡堂”、前面则是长廊。')
        view_status()
        output('你会：A：向左走 B：向前走 C：向右走')
        leave = 1
        while leave != 0:
            output('你会：A：向左走 B：向前走 C：向右走')
            while choose not in {'A','B','C'}:
                print('请做出您的选择')
                output('你会：A：向左走 B：向前走 C：向右走')
            if choose == 'A':
                input('画廊里面似乎有个上班族模样的扑克，要交谈吗？')
                view_status()
                chooseb = input('A：交谈 B：离开')
                view_status()
                while chooseb not in {'A','B'}:
                    print('请做出您的选择')
                    chooseb = input('A：交谈 B：离开')
                    view_status()
                if chooseb == 'A':
                    input('你上前交谈，他对你说：“我每次都会在休息时间来画廊，这简直太棒啦。可惜要绕过许多的天降地板阵。我们扑克只能看清楚前面一行，这对我们来说就是噩梦啊！”')
                    view_status()
            elif choose == 'C':
                input('你向右来到澡堂，一个棋子在前台迎接你，但她遗憾地对你说今天是休息日，澡堂不开放。你对澡堂也有休息日这点感到很奇怪。')
                view_status()
                input('这里还站着一个气呼呼的扑克，要交谈吗？')
                view_status()
                chooseb = input('A：交谈 B：离开 C：真的不能去洗澡吗？')
                view_status()
                while chooseb not in {'A','B','C'}:
                    print('请做出您的选择')
                    chooseb = input('A：交谈 B：离开 C：真的不能去洗澡吗？')
                    view_status()
                if chooseb == 'A':
                    input('你上前交谈，扑克说：“可恶可恶！迈克让我们做一个叫数独的东西！那玩意儿整了我半小时，之后答案上面那个3居然放在4的后面！！可恶啊！天下居然有这种东西吗？出题人早就被罗尔斯关进监狱里了吧！”')
                    view_status()
                elif chooseb == 'C':
                    input('确实不能呢……太可惜了')
                    view_status()
            elif choose == 'B':
                leave = 0
        output('正在你穿越由高高拱形柱子支撑的长廊时，一群扑克围住了你。')
        output('“啊！迈克让我们来搞！事！情！你猜我们要搞什么事情呢？！”')
        choose = input('你会回答：A：杀了我 B：放我过去') #这行写的……
        view_status()
        while choose not in {'A','B'}:
            print('请做出您的选择')
            output('你会回答：A：杀了我 B：放我过去')
        if choose == 'A':
            input('扑克说：“啊？你……你想被杀？好啊！”')
            view_status()
        elif choose == 'B':
            input('扑克说：“什么？你想轻松地过去？没门！欧对了，这建筑好像确实没有门耶！”')
            view_status()
        fight('扑克守卫',180,5,20,20,random.randint(100,300),'normal',2)
        if respawned == 1:
            respawned = 0
            continue
        input('你击败了扑克，他们哇哇叫着放你走了。')
        view_status()
        input('你继续前进，来到一个宽敞的大堂。扑克们在这儿悠闲地走着。大堂中央有一左一右两个小房间，看上去十分简陋。')
        view_status()
        leave = 1
        while leave != 0:
            output('你会：A：继续前进 B：去左边的房间 C：去右边的房间 D：找扑克交谈')
            while choose not in {'A','B','C','D'}:
                print('请做出您的选择')
                output('你会：A：继续前进 B：去左边的房间 C：去右边的房间 D：找扑克交谈')
            if choose == 'A':
                leave = 0
            elif choose == 'B':
                output('欢迎来到商店！')
                shop = 0
                bow = 0
                while shop == 0:
                    output('请选择需要购买的物品：A：CRD硬糖【50CM币】 B：花色汉堡【70CM币】 C：透明蝴蝶结【100CM币】 D：复活爱心【400CM币】,E：离开商店')
                    while choose not in {'A','B','C','D','E'}:
                        print('请做出您的选择')
                        output('请选择需要购买的物品：A：CRD硬糖【50CM币】 B：花色汉堡【70CM币】 C：透明蝴蝶结【100CM币】 D：复活爱心【400CM币】,E：离开商店')
                    else:
                        money = 0
                        buy = 0
                        if choose == 'A':
                            if CM < 50:
                                output('你的CM币不够!')
                            else:
                                buy = 'CRD硬糖'
                                money = 50
                        elif choose == 'B':
                            if CM < 70:
                                output('你的CM币不够!')
                            else:
                                buy = '花色汉堡'
                                money = 70
                        elif choose == 'C':
                            if CM < 100:
                                output('你的CM币不够!')
                            else:
                                buy = '透明蝴蝶结'
                                money = 100
                        elif choose == 'D':
                            if CM < 400:
                                output('你的CM币不够!')
                            else:
                                buy = '复活爱心'
                                money = 400
                        elif choose == 'E':
                            shop = 1
                        if len(item) >= 10 and buy != 0:
                            view_status()
                        if bow == 1 and buy == '透明蝴蝶结':
                            buy = 0
                            output('你已经购买这个物品了!')
                        if buy != 0 and buy != '复活爱心':
                            item.append(buy)
                            if buy in {'CRD硬糖','花色汉堡'}:
                                fight_item.append(buy)
                            if buy == '透明蝴蝶结':
                                bow = 1
                        elif buy == '复活爱心':
                            love += 1
                        output(f'你购买了{buy}!')
                        buy = 0
                        CM -= money
            elif choose == 'C':
                output('房间里面坐着一辆玩具车，它见到你居然开口说话了：“什么？你进来了？进来这里只能是来找国王吧，他们都不在，你出去吧。”')
            elif choose == 'D':
                output('扑克们不想理你')
        output('你继续向前走，前面又出现了一座楼梯。你走了上去。')
        output('一来到四楼，你就听到了前面的吵闹声：')
        output('“啊！你！你！你！你放开我！！！”')
        output('“啊哈！我可是把Zero送过来的大功臣，罗尔斯一定会……你就乖乖在这儿站好吧！”')
        output('“不要！！我！我！我！我怎么活！”')
        output('“你的谜题没有任何威胁，Zero不还是过来了嘛！！哈哈哈哈！我马上就要……罗尔斯……嘿嘿！我马上就可以获得，我想要的东西了！！！”')
        output('“什么玩意儿啊啊啊啊啊啊！！！”')
        output('你向前走去，拐了个弯，CRD的身影在前面出现，但你并没有看到迈克。')
        output('“啊哈！是可爱的Zero啊！继续向前走，你就可以见到罗尔斯了！！他有让你回家的方法呢！”')
        output('你会：A：向前走 B：询问罗尔斯 C：询问迈克 D：询问星空')
        while choose not in {'A','B','C','D'}:
            print('请做出您的选择')
            output('你会：A：向前走 B：询问罗尔斯 C：询问迈克 D：询问星空')
        if choose == 'A':
            input('你不理会CRD，向前走去')
            view_status()
        elif choose == 'B':
            input('“罗尔斯大人？很抱歉我们的计划出了点偏差，但……但这不影响我们的信任啊哈哈哈！我们赢定啦！！！”')
            view_status()
        elif choose == 'C':
            input('“你关心这蠢货干嘛？罗尔斯本来就不想杀你嘿嘿，迈克这家伙居然妄想阻止他伟大的指令！可真是个叛徒呢！可惜他现在已经被罗尔斯大人送进监狱里去啦！”')
            view_status()
        elif choose == 'D':
            input('“星空？他现在在三楼，马上就来！你向前走就是啦。”')
            view_status()
        input('前面又是一条长长的走廊，你刚想踏出一步，突然地面又开始向下塌陷。')
        input('“拜托！走路时记得看看地砖！”')
        go = 0
        while go == 0:
            output('回复A,B,C,D四个字母中的一个以通过地砖，地板随机组成三条路，如果过不去要从新输入字母')
            while choose not in {'A','B','C'}:
                print('格式错误!')
                output('回复A,B,C,D四个字母中的一个以通过地砖，地板随机组成三条路，如果过不去要从新输入字母')
            floor = random.randint(1,4)
            floor = chr(64+floor)
            if choose == floor:
                road = ['A','B','C','D']
                road.remove(floor)
                output(f'掉落地板组成了路{road},你没通过！')
            else:
                output('你通过了桥！')
                go = 1
        output('你穿过了塌陷地板阵，来到前面的一个大房间。房间正中央摆着一个金色的大型王座，四周摆着四个木制小型王座。')
        output('你会：A：往前走,B：看看大王座,C：看看小王座')
        while choose not in {'A','B','C'}:
            print('请做出您的选择')
            output('你会：A：往前走,B：看看大王座,C：看看小王座')
        else:
            if choose == 'B':
                output('王座上方放着一把长剑，但这剑太大了，你无法携带。')
            elif choose == 'C':
                output('小王座上到处都是裂痕，扑克牌四处散落着。')
        output('你穿过前面的门，来到了楼顶的一片开阔空间。夜色已深，冷风呼啸吹过，你孤零零地走在通向前方一座石头屋子的天台上。')
        output('突然，你发现地面再度塌陷下去，剩下的地板像几何平原一样开始翻转起来')
        output('回复4次字母以通过翻转地板桥')
        go = 0
        while go < 4:
            output('回复A,B,C三个字母中的一个以上桥，翻转地板随机组成两座真桥，如果过不去要从新输入字母')
            while choose not in {'A','B','C'}:
                print('格式错误!')
                output('回复A,B,C三个字母中的一个以上桥，翻转地板随机组成两座真桥，如果过不去要从新输入字母')
            bridge = random.randint(1,3)
            if bridge == 1:
                bridge = 'AB'
            if bridge == 2:
                bridge = 'BC'
            if bridge == 3:
                bridge = 'AC'
            bridge = list(bridge)
            if choose in bridge:
                go += 1
                if go == 1:
                    output('你通过了第一座桥!')
                if go == 2:
                    output('你通过了第二座桥!')
                if go == 3:
                    output('你通过了第三座桥!')
                if go == 4:
                    output('你通过了第四座桥!')
            else:
                output(f'翻转地板组成了桥{bridge},你没通过桥！')
        output('你通过了翻转地板桥，继续向前行进。来到一块大平台上。突然，你看见前面凭空出现了两个黑影。')
        output('你隐隐约约地能够听到对话：')
        output('“准备好了吧。”')
        output('“还差最关键的一步！他们自己送上门来当然不行！我们还需要捕获他们！别放他们跑了！”')
        output('“所以，你真的按照我的命令，把他们抓到了这里？”')
        output('“是的！是的！只需要您的亲自出击就行了！我们待会就可以……把他们……”')
        output('“很好，把他们带过来。”')
        output('“呃……这个要稍等！诶！其中一个研究站在这儿了！”')
        output('一个身材稍大的黑影稍微转了个身子面向你。')
        output('短暂的沉默过后，对话又出现了。')
        output('“你的计划和实践完全不同。”')
        output('“信任……有意思。”')
        output('那个黑影突然又转了个身。')
        output('“那么，另一个呢。”')
        output('“哦！Zero和他离开后我们用最大的兵力把他抓住了，现在他在一楼！”')
        output('你惊讶地后退了一步。')
        output('“把他送上来。”')
        output('“什么！！你想让他和Zero一起……”')
        output('“快点。”')
        output('“啊？！！”话音刚落，另一个黑影就凭空消失了。')
        output('那个黑影又转了个身，一言不发地看着你。')
        output('你会：A：逃跑,B：不动,C：交谈')
        while choose not in {'A','B','C'}:
            print('请做出您的选择')
            output('你会：A：逃跑,B：不动,C：交谈')
        else:
            if choose == 'A':
                output('你想跑，但你发现后面的地板早已全部塌陷。而黑影仍然在前面紧盯着你，看来注定跑不了了。')
            elif choose == 'B':
                output('你站着不动')
            elif choose == 'C':
                output('你和他打招呼，他并没有理你。')
        savepoint = 5
    #BOSS战，不仅仅会让游戏变得很难，也会让代码搞起来很难（
    if savepoint == 5:
    #做个存档点标记
        save_data()    
        output('过了一会儿，你听到后面传来吵闹声。回头一看，四个扑克兵押着五花大绑的星空通过一条从天而降的地砖道路走了过来。另一个黑影也出现在你的面前，你看清楚了他正是CRD。')
        output('“好啦，现在该如何处置？”CRD问')
        output('“解绑。”')
        output('“什么？！！这可玩不得啊！！！你想被……”CRD叫道')
        output('“这是规则。”黑影说，扑克兵瞬间给星空解了绑，然后跳到后面的深渊里去了。')
        output('“罗尔斯大人。现在我们该如何处置星空和Zero呢？”CRD问。')
        output('“你的任务完成了，但我的任务还差一步。”黑影回答。你看到他手中出现了一个亮闪闪的东西。')
        output('“怎么样的一步？”CRD问')
        output('“你不需要知道，给我下去。”')
        output('CRD无奈地消失在你面前。')
        output('“很好，很好。Zero……太棒了……你的能量，藏匿在你内心里的巨大能量，在我彻底抓住你之后……就可以得到释放。在这之后，我，还有我所掌控的‘规则’，将会统治整个魔法界域，进而统治全世界……”')
        output('“不得民心的统治是不会长久的。”星空在你旁边小声说道，不过还是被前面的黑影听见了。')
        output('“呵，你懂什么。我统治的手段是运用‘规则法术‘。动用一切种类的规矩，让万物运行在特定的框架内。这样的世界是永远不会崩塌的！”')
        output('“这样的世界……相当于死了。”星空说道。')
        output('“为什么死了？自然万物在一定的规律下运行，难道生命就不能存在？我的‘规则法术’只不过是让我所掌握的环境规则缩小到一定范围内，让我可以轻松掌控。哪怕有人逾越，我也可以轻松地把他投入监狱。这，就是我，罗尔斯，征服魔法界域的手段！”')
        output('罗尔斯向你们走来，你们看清了他是个穿着厚重盔甲的大家伙，手里持着你刚才看到的长剑。')
        output('“现在，我把我的手段告诉了你们，而你们，要偿还与我的手段等价的物资。星空，只要杀了你，我就可以得到你们的基地‘云村’，而Zero，我要把你送给‘他们’，让‘他们’来决定你最后的命运。”')
        #有名忽然惊讶的发现，在没有选择时去掉choose貌似也没什么影响
        #不，爱view_status()人士已经给我的电话打爆了！我只能改回来
        output('罗尔斯持剑继续向你们逼近。')
        output('“现在，我给你们公平斗争的机会，和我决斗吧。”')
        fight('罗尔斯',1500,25,40,50,0,'lorce',[0,0])
        if respawned == 1:
            respawned = 0
            continue
    #做个存档点标记
    if savepoint == 6:
        save_data()
        output('罗尔斯看着你们，说道：“看来……原有的规则已经动摇了。为了维护它，我将使用……”')
        output('突然，你看到一道闪光从罗尔斯身后发出。')
        output('“啊哈哈哈哈，规则炸弹来啦，啊哈哈哈哈！”一个熟悉的声音传来。')
        output('“什么？！”罗尔斯怒吼，但随后惊讶地发现自己的长剑突然化成了细小的粉尘，落到地上。')
        output('“啊哈哈哈哈！规则炸弹是你自己做的东西！现在搞到你自己头上去喽！啊哈哈哈哈！你个蠢货！”CRD在罗尔斯身后大笑道。')
        output('“你！！你这家伙！！我要杀了你！！！”罗尔斯大吼。')
        output('“你可动不了我！现在规则已经被我完全掌管了！规则炸弹是用来毁灭原有规则，构建新规则的东西！只有在万不得已的时候你才敢用！可惜啊！！这东西被我拿到喽！现在的规则体系就归我来管喽！！！”CRD大笑。')
        output('“你！！你是怎么拿到的！”')
        output('“啊！你以为是我拿的吗？不不不？我一个人怎么能突破你的重兵呢？还有他们～”')
        output('CRD的身后突然出现了无数道亮光，黑暗的平台上一下热闹了起来。你看见CRD身后有许多你认识的身影：方块、滚轮、鹿法师、骷髅、水晶、猫头鹰、还有扑克们。')
        output('“我们大家早就受不了你那蠢规则的压迫了，我们一直在想办法跟你战斗，可是一直没解决！直到Zero的到来，我们才看到了这样的机会！我知道你一定会亲自与Zero出战，所以在那时候召集了所有人！把你的炸弹给抢走咯！之前的所有事，都是骗你的！！！        绑星空只是做个样子而已，星空根本没在监狱待过，一直在店里喝茶呢！”')
        output('“确实。”星空回了一句。')
        output('“你们这群蠢货！规则会制裁你们的！”罗尔斯吼道。')
        output('“规则已经不由你管了！再会啦！在监狱里和迈克共度余生吧！”CRD说完，扑克守卫们已经把罗尔斯拉了下去。')
        output('事情一忙完，CRD就来到了你和星空面前，说：“哈！星空！Zero！干得漂亮！你们如果想回去，就请进入前面那座石头房里吧！当然，如果你想和老朋友们聊天，我也不会介意！”')
        output('你会：A：与CRD交谈,B：与骷髅、水晶交谈,C：下楼,D：向前进')
        go = 0
        while go == 0:
            while choose not in {'A','B','C','D'}:
                print('请做出您的选择')
                output('你会：A：与CRD交谈,B：与骷髅、水晶交谈,C：下楼,D：向前进')
            else:
                if choose == 'A':
                    output('CRD说：“啊……我将会指定一个更好的规则！当然不是由我一个人制定，是由一个委员会专门制定！！目前骷髅和水晶都愿意成为会员！不可能像罗尔斯一样专制了！”')
                elif choose == 'B':
                    output('骷髅们一见到你，大喊：“Zero！你不等我独自去扑克城堡了，真伤心啊！”')
                    output('另一个骷髅说道：“主语少了吧……”')
                    output('“啊！没关系！不用管语法！反正罗尔斯那规则被推翻了！谁都可以干”')
                    output('水晶在一旁补充道：“对的对的！以后我们就是规则的制定者了吧？”')
                    output('“啊！那可不能学罗尔斯……”')
                    output('“当然啦！”')
                    output('“也不要制定什么语法的规则，你说对吧？！”')
                    output('“啊！那可不行呢！我们快去一楼看看原来的规则是怎么样的吧！”')
                    output('骷髅、水晶互相看了看，都笑着离开了。')
                elif choose == 'C':
                    output('你向右走，发现两只木马挡在后面的天降地板上，你没办法下楼了。')
                elif choose == 'D':
                    go = 1
        output('你们与大家道别后，向前走到那座石头房前面，房子看上去十分普通。')
        output('星空推开门，里面一片漆黑，什么都没有。')
        output('突然，一座巨大的机器在你面前显现出来，它闪着诡异的红色荧光，发出滴滴的声音。')
        output('星空往前碰了碰机器，“看来是传送机器。”')
        output('突然，刺眼的白光再次在你眼前爆发，你失去了知觉。')
        output('当你再次睁开眼时，你发现你居然躺在你自己的房间里。')
        output('房间的格局没变，只是门显然经过了改装，很容易就你推出去。')
        output('你会：A：出门,B：在房间里看看')
        while choose not in {'A','B'}:
            #第一章都完结了我不必再打一行print提示了罢
            output('你会：A：出门,B：在房间里看看')
        else:
            if choose == 'B':
                output('你要看哪个地方：A：床头柜,B：书')
                while choose not in {'A','B'}:
                    output('你要看哪个地方：A：床头柜,B：书')
                if choose == 'A':
                    choose = input('你看了看床头柜，找到了50CM币（获得50CM币）')
                    CM += 50
                    view_status()
                elif choose == 'B':
                    output('你看了看书，之前的漫画书被换成了一本经济学书，你随便翻了翻：“CM币的流通政策是在魔法界域的任何区域里通用，汇率固定也无时效性……”')
                    output('你合上了书。')
        output('你推开门来到外面，大堂里十分冷清，只有一小部分人在散步。')
        output('你会：A：到处逛逛,B：找人交谈,C：出门')
        while choose not in {'A','B','C'}:
            output('你会：A：到处逛逛,B：找人交谈,C：出门')
        if choose == 'A':
            output('你四处转了转，商店门都关了，没什么好东西。')
        elif choose == 'B':
            output('你看到一个女孩从你面前走过，她头上的猫耳和身后的尾巴吸引了你的注意。')
            output('你的身后还有一个人穿着十分具有科技感的图片在……卖水果？')
            output('你会与谁交谈：A：猫女,B：水果贩')
            while choose not in {'A','B'}:
                output('你会与谁交谈：A：猫女,B：水果贩')
            if choose == 'A':
                output('那位猫女看了看你，大声叫道：“喵！我是昵称！”')
                output('你对她有点兴趣，戳了戳她，她可爱地喵了一声。')
                output('“啊——怎么都喜欢戳我……”昵称叫道，随后掏出了个银色的小方块，随便按了按，你的面前突然出现了一个全息投影，上面密密麻麻地写着许多数字，你看清楚了其中最显眼的一个是1001540。')
            elif choose == 'B':
                output('你朝水果摊走去，摊主见到你说：“山竹香又甜，便宜不要钱，免费品尝！！！真的不来看一看吗？”')
                output('你拿起来尝了尝，并不是很好吃。')
                output('“这吃山竹，多是人间一件美事啊。”摊主说道，“我是SuPrE_OnE，简称So，希望下次还能见面。”')
            elif choose == 'C':
                output('你来到大门，发现门锁了，你出不去。')
        output('你继续逛了逛，没看到什么别的，正准备回房间睡觉，这时你看到星空带着两个人走了过来。')
        output('“嗨！Zero！介绍一下这是我的两位副手，一个叫代数，一个叫点线，他们似乎可以帮你找到你以前的记忆，不过……要等几天，因为设备前几天坏了。”星空说。')
        output('“如果你没什么事，就跟我来会议室一趟吧，我要跟你说些事情。”')
        output('你会：A：去会议室,B：回房间')
        while choose not in {'A','B'}:
            output('你会：A：去会议室,B：回房间')
        if choose == 'A':
            output('你跟着星空三人前往会议室')
            room = 0
        elif choose == 'B':
            output('你告别了星空，回到房间')
            room = 1
        if room == 0:
            output('你们来到会议室坐下。星空亮出了一条挂着一块紫色水晶的项链。')
            output('“实话告诉你吧，当你来到这里的时候，你的身上有一条……这个项链，这个项链……可能有一些奇怪的用途吧……希望你能好好看看它。”星空说。')
            output('你接过项链仔细看了看，没有想起什么。')
            output('“看来你还是想不起来……好吧，你回去吧，现在已经很晚了。”')
            output('你会：A：回房间,B：看看会议室')
            while choose not in {'A','B'}:
                output('你会：A：回房间,B：看看会议室')
            if choose == 'B':
                output('你四处转了转，突然在墙上发现了一幅巨画，那是许多人的合照，你看出星空也在上面。')
                output('“那是我们CV成立时所有人的合照。现在……除了一个人失踪了之外都还在这儿。”星空说。')
                output('你追问星空失踪的人是谁。')
                output('星空似乎有些后悔提到那个人：“哦……失踪者叫End，是半年前失踪的，一直没有回来……很多人都认为他死了……不过现在也没有足够的证据证明这点，你还是回去吧。”')
            output('你回到房间')
        output('你简单洗过澡之后躺在床上。你突然发现这床并没有被子，睡着并不是很舒服。')
        output('你回想着之前的冒险经历，虽然感觉有意思，但又有些迷惑。')
        output('到底，什么是魔法界域，Cloud Village，究竟隐藏着什么秘密？')
        choose = input('【第一章完】')
        savepoint = 7
        chapter = 2

#这里棉花糖，我终于分完段了，写个注释吧（
#强烈建议下一章换个文件写
#冷知识，代码行数已经破万了（
#第一章完

    if savepoint == 7:
        health = 300
        save_data()
        output('迷迷糊糊的……')
        output('好粘稠，像糖一样……')
        output('想不起来，真的想不起来……')
        output('撕裂……')
        output('啊啊啊啊啊啊啊……')
        output('你突然从床上坐起，看着稍微有点熟悉的小房间，松了口气。')
        output('你穿好衣服，简单整理了一下，便走出房门。')
        output('屋外仍然是熟悉的大厅，阳光透过天花板上的玻璃天窗洒落在屋里，让大厅里看起来格外明亮。')
        output('你会：A：吃早餐,B：随便逛逛,C：找星空,D：随便找人交谈')
        while choose not in {'A','B','C','D'}:
            output('你会：A：吃早餐,B：随便逛逛,C：找星空,D：随便找人交谈')
        if choose == 'A':
            output('然而，你并不知道早餐在哪吃【你 傻 了】')
        elif choose == 'B':
            output('你看到了那家超市，不过你并不是很想去。')
        elif choose == 'C':
            output('你四处找星空，终于在大厅二楼找到了他。')
            output('星空正站在露天平台上观景。看到你来了，笑着说道：“是Zero啊！早上好！想做点什么？”')
            output('你并不想多说话，随便回答了几句就离开了。')
        elif choose == 'D':
            output('大厅里行走的人都很匆忙，没有时间理你。')
        output('你漫无目的地在大厅里走来走去，就在快接近出口的地方，你看到有……一对情侣牵着手散步。男的身穿一件蓝色卫衣，女的穿着一件白色长裙。两人的对话时不时传来：')
        output('“So我爱你喵……”')
        output('“昵称！我也爱你……”')
        output('“啊，So我又收了一首歌哦……”')
        output('“啊，昵称您太强了……”')
        output('“So，我要吃冰淇淋！喵！”')
        output('对话声十分清晰，你甚至认为他们在故意放大音量。不过那对情侣并没有朝你走过来，而是走出了大厅。')
        output('你没有理会他们，继续向前走去，出了大厅，来到小镇里。')
        choose = input ('你的前面是熟悉的三岔路口。')
        view_status()
        output('你会：A：向左走,B：向右走')
        while choose not in {'A','B'}:
            output('你会：A：向左走,B：向右走')
        if choose == 'A':
            output('你向左走去，前面屋子下站着那位卖冰棍的人。')
            output('“嗨！是你！你要买点……哦等等我的冰棍已经卖完了，真可惜。天气越冷的时候买冰棍的人就越多……话说你怎么还穿这么少，不会感冒吗？”')
            output('你没有继续向前走，而是原路返回。')
        elif choose == 'B':
            output('你向右走去，昨天进入那座神秘屋子的小路上站了一个穿着黑衣服的人，你认出了他就是小黑。')
            output('“啥？Zero？你个小鬼居然能跑这里来，你可真难缠啊！给我滚出去听到没有！”小黑对你吼道。')
            output('你不想招惹他，便原路返回。')
        output('你在小镇里转了转，突然听见后面有人在叫你。')
        output('你转过身看见一个穿白色风衣的人走来。')
        output('“你好，我是代数，我们昨天见过。”那个人对你说道。')
        output('你呆呆地看着代数，你发现他长得很像星空。')
        output('“是这样的，星空刚才叫我过来提醒你一下，虽然你经过昨天的冒险，但请你不要到处乱跑。我们CV的周围还是很危险的。”')
        output('你对他点了点头，并不是很在意。')
        output('你和代数在小镇里逛了逛，周围几乎没什么人，你也没发现什么新鲜的东西。')
        output('你会：A：离开,B：交谈')
        while choose not in {'A','B'}:
            output('你会：A：离开,B：交谈')
        if choose == 'B':
            output('代数说：“嗯……你对昨天的冒险很感兴趣吗？啊，是这样的，因为敌方没有大统领，白羽和我率领的小分队很快就可以掌管那个地方，这是我们CV控制的第一个魔法地界……哦，并不是像罗尔斯那样独裁，我是说，控制那边的魔法核心，只要有那东西就是胜利。”')
            output('他顿了顿说：“等等……魔法核心……啊这不关我事了，那是So的事情，你应该问问他。不过这时候他多半在和昵称约会呢……”')
        output('你正想离开，突然代数朝你严肃地说了一句：“嘿，Zero，听着，帮我们干个事。昨天我、星空和点线修复了储物室里那台损坏的渗透机器……很不幸点线在修复时受了点……辐射照射，请你现在帮我去小镇上的医务室拿一点药，叫做Sword-10，记住了吗？什么？你问我为什么不去？嗯，我还有其他事要做呢。”')
        output('听到这话，你看了看四周，小镇楼房上一片片红色的砖瓦映入眼帘，根本没法找出什么特别的。')
        output('“嗯……医务室的话，就在你刚进小镇那条路的左手边尽头。”')
        output('你告别代数向之前那条路跑去，经过那位冰棍小贩的遮阳伞一路向前跑，便来到了一座建筑前面。')
        output('你推开门走了进去，发现里面是个白色的房间，灯光非常刺眼。你前面的长桌上摆着各种乱七八糟的仪器和药物。')
        output('你会：A：查看仪器,B：看看四周,C：寻找药物')
        while choose not in {'A','B','C'}:
            output('你会：A：查看仪器,B：看看四周,C：寻找药物')
        if choose == 'A':
            output('你看了看桌上奇形怪状仪器，你觉得你肯定不会使用它们。')
        elif choose == 'B':
            output('你看了看四周，墙上挂着一份报纸，上面赫然列着许多医疗事故的文章。')
            output('四周没什么人，你感到有点奇怪。')
        elif choose == 'C':
            output('你翻了翻桌子，看见了大大小小的瓶子贴着“氰化钾”、“肉毒杆菌毒素”、“二甲基汞（这东西上面还额外贴了好几个骷髅头）”之类许多你不认识的药物标签，你并不想碰它们。')
        output('你到处翻找，终于在一个柜子里看见了一只紫色的小瓶，上面标签贴着“Sword-10”')
        output('你感觉这药物并不正常，你伸手碰了碰这瓶子。')
        output('就在一瞬间，四周发出了闪烁的红光，警报声迭起，你看了看周围，发现墙上打开了一道隐藏的门。')
        output('你钻进这道隐藏门，里面几乎一片漆黑，空气中似乎散发着冰淇淋的香味，这和外面医务室的药水气味并不相同。')
        output('你向前走去，突然，你的前身碰到了一个冰凉的东西，你向后退去仔细看了看，前面好像有一个冰淇淋机。')
        output('你会：A：继续向前摸去,B：拿一个冰淇淋')
        while choose not in {'A','B'}:
            output('你会：A：继续向前摸去,B：拿一个冰淇淋')
        if choose == 'B':
            choose = input('你摸黑操作着，拿了一个冰淇淋')
            item.append('冰淇淋')
            fight_item.append('冰淇淋')
            view_status()
        output('你向前摸去，前方好像又是一堵墙，当你朝向左边转过身体，那个梦魇般的东西再次在你眼前出现——')
        output('你前面的是一台渗透机器。')
        output('与第一次看到时不同，这台渗透机器发着恐怖的紫光，发出十分机械的声音。它那万分复杂的管道系统如昆虫的触角一般似乎在向你袭来，令你窒息。')
        output('你想跑，但双脚被巨大的恐惧与好奇震慑住了，无法移动。在紫光中，机器最终向你吞噬过来，你的眼前再次出现了那道猛烈的白光……')
        output('基本是一刹那间，你的意识恢复了过来。')
        output('你发现你趴在一大堆垃圾上，可乐瓶、剩饭剩菜和塑料袋围在你身上，一些鱼刺甚至扎进了你的皮肤里。')
        output('你清理了一下身体，看了看周围。你发现自己身在一个阴暗狭窄的，堆满垃圾的小巷里，三面都是绿色的墙壁，只有一面通往外面。')
        output('你在垃圾堆上站起身来')
        output('你会：A：找点有用的垃圾,B：躺着,C：去外面看看,D：观察地形')
        while choose not in {'A','B','C'}:
            output('你会：A：找点有用的垃圾,B：躺着,C：去外面看看,D：观察地形')
        if choose == 'A':
            choose = input('你在垃圾堆里发现了一块糖果')
            item.append('五彩糖')
            fight_item.append('五彩糖')
            view_status()
        elif choose == 'B':
            output('你躺着，感觉这样没有用，然后你又站了起来')
        elif choose == 'D':
            output('你的周边都是高大的绿色墙壁，但由于太暗了看不到墙上的东西。')
        output('过了一会儿，你感觉不能在这里再待下去了，你决定去外面看看。')
        output('你穿过狭窄的墙壁来到外面。')
        output('在你的面前出现了一道公路，路面黄澄澄的十分干净。在路的对面，一片青色的大森林在你面前展开，这种不寻常的配色让你觉得十分难受，而大森林的远处是连绵起伏的青色大山，你不敢再看下去，暂时把视线收了回来。')
        output('你会：A：走上公路,B：穿过公路,C：顺着公路走')
        while choose not in {'A','B','C'}:
            output('你会：A：走上公路,B：穿过公路,C：顺着公路走')
        if choose == 'A' or choose == 'B':
            choose = input('你走上公路，你感到脚有种触电的感觉，你跳到公路一旁。[HP-20]')
            health -= 20
            dead_interface()
            view_status()
        output('你决定在道路旁边顺着公路走下去，你所在的这一侧是高大的绿色围墙，上面密密麻麻地画满了电路，不知道是否可以运作。')
        output('你靠着墙向前走去，过了一会儿，公路通上了一座大桥继续向前伸展，大桥的边缘很窄，你无法顺着公路走下去了。')
        output('你看了看大桥的底下，是一片大森林，树木的颜色与你之前看到的无异。')
        output('你会：A：沿着桥的旁边攀爬上桥,B：跳下森林,C：原路返回')
        while choose not in {'A','B','C'}:
            output('你会：A：沿着桥的旁边攀爬上桥,B：跳下森林,C：原路返回')
        if choose == 'A':
            choose = input('你刚抓住大桥旁边的钢架，那条绿色的钢架突然闪烁了一下，随后一阵触电的刺痛感传来，你摔下森林[HP-60]')
            health -= 60
            dead_interface()
            view_status()
        elif choose == 'B':
            output('你跳下森林，树叶接住了你，你安全着地。')
        elif choose == 'C':
            choose = input('你正想原路返回，突然你的后方出现了一辆奇怪的车，车的强光让你自觉地退了一步，你摔下森林[HP-60]')
            health -= 60
            dead_interface()
            view_status()
        output('你掉落在地上，周围全是一模一样的大树，你完全找不到方向。')
        E_forest = 0
        E_zo = 1
        while E_forest == 0:
            output('你会：A：呼救,B：观察树干,C：观察树叶,D：向前探进')
            while choose not in {'A','B','C','D'}:
                output('你会：A：呼救,B：观察树干,C：观察树叶,D：向前探进')
            if choose == 'A':
                output('你大声呼救，并没有什么用')
            elif choose == 'B':
                output('你看了看树干，树干比你想象的光滑许多，上面密布的条状纹理中似乎有光芒闪过。')
                choose = input('突然，你发现许多电火花聚集在你附近的树干上，你和它们之间出现了一道闪电！你被击中了[HP-30]')
                health -= 30
                dead_interface()
                view_status()
            elif choose == 'C':
                output('你看了看树叶，叶色是无趣的蓝绿色，但你仔细瞧了瞧，上面似乎有数字在不断跳动着。')
                E_zo = 0
            elif choose == 'D':
                output('你向前走去，但完全找不到方向。你的脚下似乎有电火花闪过，它们击中了你[HP-20]')
                health -= 20
                dead_interface()
            output('你仔细观察着这些数字，发现它们中只有0和1出现，这些0和1在不断变化着，但你发现它们看起来像是有规律地在朝一个方向流动。')
            while E_zo == 0:
                output('你会：A：朝这个方向走去,B：再找一些树叶比对')
                while choose not in {'A','B'}:
                    output('你会：A：朝这个方向走去,B：再找一些树叶比对')
                if choose == 'A':
                    choose = input('你向前走去，但很快迷失了方向。你的脚下似乎有电火花闪过，它们击中了你[HP-20]')
                    health -= 20
                    dead_interface()
                    view_status()
                elif choose == 'B':
                    E_forest = 1
            #如果运气不好这块过完300血就只剩130了（
                    output('你又看了些树叶，很快，你发现这些数字都是朝一个方向流动的。')
                    output('看来，只需要一直保持往这个方向走，感觉偏离方向的时候找几片树叶比照一下，就可以确保一直沿着同一个方向前进了。')
                E_zo = 1
        output('你沿着这个方向向前走去，路上不断地拿树叶比照，经过了好长时间，你终于来到了一片开阔的地方。')
        output('你看了看四周，大桥早就消失不见，你的前面出现了许多大方块，你感觉像一座小镇，但你从来没有见过这样的小镇。')
        output('你再仔细看了看“小镇”，镇上一个人都没有，甚至没有看到一点活物。')
        choose = input('你会：A：去小镇上,B：向旁边走')
        while choose not in {'A','B'}:
            output('你会：A：去小镇上,B：向旁边走')
        if choose == 'A':
            choose = input('你来到了小镇上')
        elif choose == 'B':
            output('你向旁边走去，但没走几步你发现这里没有方向指示，反而更容易迷路。你还是回到了小镇。')
        output('你来到这座空无一人的小镇上，这里的道路似乎不会伤人，你沿着道路走向前去。')
        output('突然，你看见一个奇形怪状的玩具小车向你开来，没等你反应过来，他居然开口说话了：“你……你是哪里人？”')
        output('你没理他向前走去，他突然大叫起来：“又来了一个入侵者啊！把她抓起来！”')
        output('你面前的小车突然四处动来动去，随着一道光芒闪过，它向你直冲过来！')
        fight('玩具车',170,25,10,20,random.randint(90,180),'normal')
        if respawned == 1:
            respawned = 0
            continue
        output('玩具车发出了一阵嘈杂的金属撞击声，随后喊道：“什么？！你看起来并不是这边的人，你不是入侵者来这儿干嘛？有必要待在这穷乡僻壤吗？前面还会有更多【乡间警察队】成员等着你的！”')
        output('说完，玩具车便跑进了旁边的一座方块里。')
        output('你感到有点莫名其妙，继续向前走去，突然，你听见前面传来了呼救声。')
        output('你会：A：向旁边看去,B：向前走')
        while choose not in {'A','B'}:
            output('你会：A：向旁边看去,B：向前走')
        if choose == 'A':
            output('旁边都是耸立着的大方块，方块上似乎有许多彩灯在闪烁，并没有什么特别的。')
            output('不过你再仔细一看，发现了一个箱子，你在里面找到了复活爱心！')
            love += 1
        elif choose == 'B':
            output('你继续向前走去')
        output('随着你的继续前进，呼救声越来越明显，你加快速度继续前进，在一座小桥上停了下来。')
        output('桥的旁边耸立着许多看上去像发电塔一样的东西，但规模更小，闪耀着黄色的光芒。')
        output('正当你看着这些发电塔时，突然从桥旁边翻上来了好几辆玩具车！')
        output('“冲啊！又来了一个新的！抓住他，啊不对，抓住她！”')
        t.sleep(0.5)
        print('【对战开始】对战 玩具……')
        t.sleep(0.3)
        output('诶等等，突然出现了一些奇怪的事情，玩具车发出了嘈杂的响声，随后就不动了。')
        output('你会：A：观察玩具车,B：逃跑,C：看看桥边')
        while choose not in {'A','B','C'}:
            output('你会：A：观察玩具车,B：逃跑,C：看看桥边')
        if choose == 'A':
            output('玩具车看上去十分新颖，你甚至找不到一点点缝隙。然而它仍然一动不动。')
        elif choose == 'B':
            output('你快速地跑开了')
        elif choose == 'C':
            output('你看了看桥的边缘，你发现了一圈圈奇怪的凹槽，刚才的玩具车似乎就是顺着凹槽翻上来的。')
        output('突然，你又听见一阵奇怪的响动，你看着桥边突然缓缓升起了一条道路，一个机器人从一座发电塔里向你走过来。')
        output('“你好，我叫赛恩思，我的机械工件代号为S281738368，欢迎您来到科技山城！”那位机器人向你打招呼，后面的几座发电塔同时变得特别亮。')
        output('“非常抱歉，我们的警察队出了点小问题，有一个人黑进了警察队的管理系统，下了攻击指令。我们不是坏人，但没办法控制这指令，非常抱歉！”')
        output('“目前我们的系统已经修复完成，但还是会对你们发动攻击，因为你们并不是这里的人，所以你们还是会成为攻击目标……等等，你问我为什么是‘你们’？哦！抱歉！我忘了把她带出来了。”')
        output('赛恩思抬起手，桥下飞升上一个长方形的平台，一个粉发女孩站在平台上方瑟瑟发抖，你认出了她就是昵称。')
        output('“救命啊！！！”昵称一见到你就向你呼救。')
        output('“这位是先前抓住的入侵者，偶不对，是受害者，不过……我没法把她还给你，我的权限不足。这样，你只要往前走，然后坐电梯下到小镇的下层，然后前往镇政府，那里有人可以帮她解除入侵者的标记，这样她就可以自由啦。”')
        output('赛恩思说完，随着昵称的大叫，平台向下跌落。')
        output('你会：A：和赛恩思交谈,B：离开')
        while choose not in {'A','B'}:
            output('你会：A：和赛恩思交谈,B：离开')
        if choose == 'A':
            output('赛恩思说：“你想问这是哪？这是科技山城，不过只是个小镇。相比不远处的那座大城市来说还是太小了。”')
        output('你向前走去，通过大桥后，你看见前面的地上横着一个黄澄澄的长方块。')
        output('当你走近它时，突然方块向上升去，你发现方块两边被绿色的杆子连接着。')
        output('当你继续向前走时，方块突然又落了下来横在你前面。')
        output('“哦，我忘说了！”你的身边突然响起了赛恩思的声音，你定睛一看，原来是一个绿色的全息弹窗。')
        output('“这是升降门，我们这里的特产，会随机升降，就像这样。你问我它是用来干什么的？它会使过门变得更刺激！”')
        go = 0
        while go == 0:
            output('请回复0或1以尝试进入升降机')
            while choose not in {'1','0'}:
                print('格式错误!')
                output('请回复0或1以尝试进入升降机')
            else:
                choose = int(choose)
            floor = random.randint(0,1)
            if floor == choose:
                go = 1
                output('你成功走上了升降门！')
            else:
                choose = input('你选择了错误的时机，你被绊倒了！[HP-5]')
                health -= 5
                view_status()
        output('你通过升降门，前面是一座巨大的电梯，电梯前摆放着各种你不认识的机器。')
        output('你进入电梯，发现上面有写着3F、4F、5F字样的按钮。')
        go = 0
        while go == 0:
            output('你会：A：去三楼,B：去四楼,C：去五楼')
            while choose not in {'A','B','C'}:
                output('你会：A：去三楼,B：去四楼,C：去五楼')
            if choose == 'A':
                output('你来到3F，电梯门开了，你发现你正在一座巨大的建筑物前，建筑物前聚集着许多机器人，把路堵死了。')
                output('你会：A：回到电梯,B：交谈')
                while choose not in {'A','B'}:
                    output('你会：A：回到电梯,B：交谈')
                if choose == 'A':
                    output('你回到电梯，电梯上升到4F')
                    go = 1
                else:
                    output('一个机器人说：“你是谁？我怎么没见过你？哦你想去镇政府是吧，去2楼就好了。”')
                    output('你回到电梯，电梯上升到4F')
                    go = 1
            elif choose == 'B':
                output('你来到4F')
                go = 1
            elif choose == 'C':
                output('不幸的是，你已经在这里了')

        output('电梯门开了，一个崭新的世界在你眼前展开。')
        output('你的面前是一座绿色的、充满动感的城市，巨大的管道和机器横在城市上空，充满科技感的绿色建筑在各种颜色的巨大显示屏衬托下，矗立在你周围。')
        output('你的面前是一条黄色的道路，上面摆放着各种复杂的电路图案，激光在你周围闪烁着，使你眼花缭乱。')
        output('街道上到处都是路人……大多数都是机器人，还有一些飞行的汽车，向后面不断喷射着激光，十分引人注目。')
        output('你的前面出现了一个十字路口，看到这片繁华景象，你甚至不知道如何抉择')
        go = 0
        while go == 0:
            output('你会：A：向左走,B：向右走,C：向前走,D：问路人')
            while choose not in {'A','B','C','D'}:
                output('你会：A：向左走,B：向右走,C：向前走,D：问路人')
            if choose == 'A':
                output('你向左走去')
                go = 1
            elif choose == 'B':
                output('你向前走，来到一座大楼前面，大楼上面乱七八糟地出现了各种字幕，看起来像是广告。')
                output('一个弹窗出现在你面前：“能量饮料20元一瓶，要买吗？”')
                output('你会：A：购买,B：不买')
                while choose not in {'A','B'}:
                    output('你会：A：购买,B：不买')
                if choose == 'A':
                    if CM >= 20:
                        choose = input('弹窗消失了，一罐能量饮料从天而降掉到你手中（获得【能量饮料】）')
                        CM -= 20
                        item.append('能量饮料')
                        fight_item.append('能量饮料')
                        view_status()
                    else:
                        output('很遗憾，你没有足够的CM币')
                    go = 1
                else:
                    output('你离开了这里')
            elif choose == 'C':
                output('你向右走，前面是一座宣传一个赛车比赛的巨大海报，海报甚至把整个道路都横向占满了。')
                choose = input('海报的后面有个垃圾桶，你在里面找到了一块面包！（获得【冰冻面包】）')
                item.append('冰冻面包')
                fight_item.append('冰冻面包')
                view_status()
                go = 1
            elif choose == 'D':
                output('你找到了一个机器人，他说：“嘿嘿，左边有拐弯道路，你要沿着道路的切线走，如果你不知道切线是什么，你还是回去请你的数学老师吧。”')
        output('道路在你的前方拐了个弯，你来到了一条街道上，你发现其中一个楼房门开着，你走了进去。')
        output('里面是一个商店。')
        shop = 0
        while shop == 0:
            output('你会购买：A：五彩糖【20CMB】,B：电路板寿司【120CMB】,C：液晶裙【250CMB】,D：复活爱心【400CMB】,E：离开')
            while choose not in {'A','B','C','D','E'}:
                output('你会购买：A：五彩糖【20CMB】,B：电路板寿司【120CMB】,C：液晶裙【250CMB】,D：复活爱心【400CMB】,E：离开')
            else:
                money = 0
                buy = 0
                if choose == 'A':
                    if CM < 20:
                        output('你的CM币不够!')
                    else:
                        buy = '五彩糖'
                        money = 20
                if choose == 'B':
                    if CM < 120:
                        output('你的CM币不够!')
                    else:
                        buy = '电路板寿司'
                        money = 120
                if choose == 'C':
                    if CM < 250:
                        output('你的CM币不够!')
                    else:
                        buy = '液晶裙'
                        money = 250
                if choose == 'D':
                    if CM < 400:
                        output('你的CM币不够!')
                    else:
                        buy = 0
                        choose = input('你购买了复活爱心!')
                        love += 1
                        CM -= 400
                if len(item) >= 10 and buy != 0:
                    view_status()
                if ('液晶裙' in item or armor == '液晶裙') and buy == '液晶裙':
                    buy = 0
                    output('你已经购买了这个物品了!')
                if buy != 0:
                    item.append(buy)
                    if buy in {'五彩糖','电路板寿司'}:
                        fight_item.append(buy)
                    output(f'你购买了{buy}!')
                    buy = 0
                    CM -= money
                shop = 1
        output('你正想离开商店，店主——一个相貌奇特的机器人叫住了你')
        choose = input('“嗨！你应该知道【交易魔法】吧。就是，如果你按下键盘上的“Y”，你就可以通过魔法买东西了。什么？！你问我什么是Y？我也不知道，这是一个人打电话告诉我的。”')
        if '商店1' not in shops:
            shops.append('商店1')
        view_status()
        output('你离开商店，继续往前面走。前方又是一个十字路口，道路的周围都被建筑挡住了，显示屏在建筑上不断闪烁着。')
        enniu_A = 0
        enniu_B = 0
        enniu_C = 0
        give = 0
        lock = 1
        #(((((
        while enniu_A == 0:
            output('你会：A：向左走,B：向前走,C：向右走')
            while choose not in {'A','B','C'}:
                output('你会：A：向左走,B：向前走,C：向右走')
            if choose == 'A' and lock == 1:
                choose = input('你向左走去，前面出现了三道升降门，被传送带连接着，你必须一次性通过。')
                go = 0
                mark = 0
                while go == 0:
                    code = []
                    for i in range(3):
                        code.append(chr(ord('0')+random.randint(0,1))+chr(ord('0')+random.randint(0,1))+chr(ord('0')+random.randint(0,1)))

                    for i in range(1):
                        choose = input('请输入三个0-1的数字')
                        wrong = 0
                        while wrong == 0:
                            wrong = 1
                            if len(choose) != 3:
                                wrong = 0
                                print('输入错误,请依照格式输入!')
                                choose = input('请输入三个0-1的数字')
                            elif choose[0] not in {'0','1'}:
                                wrong = 0
                                print('输入错误,请依照格式输入!')
                                choose = input('请输入三个0-1的数字')
                            elif choose[1] not in {'0','1'}:
                                wrong = 0
                                print('输入错误,请依照格式输入!')
                                choose = input('请输入三个0-1的数字')
                            elif choose[2] not in {'0','1'}:
                                wrong = 0
                                print('输入错误,请依照格式输入!')
                                choose = input('请输入三个0-1的数字')
                        input('升降门密码是'+code[i-1])
                        if choose == code[i-1]:
                            input('你通过了所有升降门')
                            go = 1
                            lock = 0
                        else:
                            input('通过失败，请从1号升降门重新开始')
                            break
                output('你通过了升降门，前面出现了一个奇怪的按钮。你按下去后，刚才的升降门同时升到了最高处，传送带也不动了。')
                output('你回到了十字路口')
                enniu_B = 1
            if choose == 'A' and lock == 0:
                    choose = input('三道大门悬在半空中，看上去可能有掉下来的风险')
                    choose = input('你决定离开')
            elif choose == 'B':
                if enniu_B == 0:
                    output('前方是一道门框，不过它似乎被力场封住了。')
                    enniu_C = 1
                elif enniu_C == 1:
                    output('前方门框上的力场解开了，你向前走去。')
                    enniu_A = 1
                else:
                    output('前方是一道门框，只是普通的门框而已。')
                    output('你向前走去')
                    enniu_A = 1
            elif choose == 'C':
                if give == 0:
                    output('右边是一条小巷，里面挂着一张某知名电视主持人的海报。')
                    output('你往最深处走去，发现了一个箱子，你在里面找到了100CM币！')
                    CM += 100
                    give = 1
                elif give == 1:
                    if CM >= 1:
                        choose = input('你向那个箱子投入了1CM币，回应他对你的慷慨')
                        CM -= 1
                    else:
                        output('箱子里的钱已经满了，但你一分钱都拿不出来')
        #我就说缩进为什么这么离谱
        output('你继续向前走，前面是个悬崖。你想趴在悬崖边向下看，但你一靠近悬崖就被一股力场弹开了。')
        output('你沿着悬崖边上的道路走去，突然，你看见悬崖的外边升起了一座平台，而昵称正站在平台的上方。')
        output('“Zero！救救我！”昵称用十分可爱的语气向你喊道。')
        output('你会：A：不理她,B：交谈')
        while choose not in {'A','B'}:
            output('你会：A：不理她,B：交谈')
        if choose == 'A':
            output('你继续前进。')
        elif choose == 'B':
            output('昵称喊道：“Zero！救救我！我不知道这是什么地方呀！这里太可怕了！So呢？你到他了吗？我……我们怎么回去？”')
            output('昵称一连串的发问让你感到头晕，你继续前进。')
        output('你继续向前走去，昵称一直在你耳边唠叨着，不过你一次都没理她。')
        output('你走了一会儿，前面出现了一座巨大的机器，上面写着“气球游戏！击破气球获得奖励！”')
        output('你并不想玩这个游戏，想绕路，但前面的路被力场挡住了。')
        output('你看见一座告示牌横在路边，上面写着：“在气球游戏中取得胜利即可获得通关奖励。”')
        output('“Zero，你如果想过去，必须要先玩游戏！”')
        output('你回到机器前面，机器上面布满了激光显示屏，上面绑着许多气球，像是全息投影。一个显示屏在你面前弹出来：')
        output('“输入数字1-100，输入数字可以击破一个气球')
        output('击破含有钥匙的气球便可通关。”')
        key = 0
        while key != -1:
            choose = input('请输入数字')
            while choose.isdigit() == False or int(choose) not in list(range(101)):
                choose = input('请输入数字')
            if int(choose) == 0:
                choose = input('机器的中央突然上升了一个巨大的气球，它随之爆破，一个钥匙从中出现。你看见前面的力场消失了。')
                key = -1
            elif key == 2:
                choose = input('昵称在你身边嘀咕着：“Zero，你不试试其它的数字吗……”')
                key += 1
            else:
                choose = input('一个气球瞬间爆炸，但马上就有另一个气球补充回来。你并没有看到钥匙。')
                key += 1
        output('“哈！你赢了！不过这样我就没法继续跟着你了喵！”昵称说道。')
        output('你继续前进。')
        output('你向前走去，来到一条大道上，突然一群玩具车向你聚拢。')
        output('“啊！伙计们，这就是那个入侵者吧！我们得阻止她进电梯！”')
        print('战斗开始,对战 玩具车*2')
        #开抄！（（
        output('玩具车说：“啥？你不知道团战怎么打？需要我教吗？”')
        output('“这样，当你面对多个敌人时，你要进攻多次，进攻数量取决于敌人数量，但如果你选择防御，你就要同时对所有敌人防御。你必须击败所有敌人才可以获胜。”')
        output('“废话少说，开始对战！”')
        fight('玩具车',170,25,10,20,random.randint(180,360),'normal',0,2,170,25,10,20)
        if respawned == 1:
            respawned = 0
            continue
        output('你成功挡下了玩具车的进攻，它们快速地逃走了，不过，是飞走的……')
        output('你向前穿过大道，前面是5个连续的升降门，被传送带连接着，你必须一次性通过。')
        go = 0
        mark = 0
        while go == 0:
            code = []
            if mark % 3 == 2:
                for i in range(5):
                    code.append('00000')
            else:
                for i in range(5):
                    code.append(chr(ord('0')+random.randint(0,1))+chr(ord('0')+random.randint(0,1))+chr(ord('0')+random.randint(0,1))+chr(ord('0')+random.randint(0,1))+chr(ord('0')+random.randint(0,1)))

            for i in range(1):
                choose = input('请输入五个0-4的数字')
                wrong = 0
                while wrong == 0:
                    wrong = 1
                    if len(choose) != 5:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = input('请输入五个二进制的数字')
                    elif choose[0] not in {'0','1'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = input('请输入五个二进制的数字')
                    elif choose[1] not in {'0','1'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = input('请输入五个二进制的数字')
                    elif choose[2] not in {'0','1'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = input('请输入五个二进制数字')
                    elif choose[3] not in {'0','1'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = input('请输入五个二进制的数字')
                    elif choose[4] not in {'0','1'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = input('请输入五个二进制的数字')
                mark += 1
                input('升降门密码是'+code[i-1])
                if choose == code[i-1]:
                    input('你通过了所有升降门')
                    go = 1
                else:
                    input('通过失败，请从1号升降门重新开始')
                    break

        output('通过升降门后，前面出现了一道电梯。')
        output('你走进电梯，发现内部的布局与之前那座并不太相同，上面只有“3F”，“4F”的按钮。')
        output('你按下3F的按钮，来到了下方的楼层。')
        output('你走出电梯，外面出现了两座像高塔一样的建筑，上面闪烁着紫色的电弧。')
        output('你向前走去，突然你发现你的前面摆着许多圆筒状的东西，它们随着你的前进冒出红光。')
        choose = input('你会：A：前进,B：观察,C：后退,D：跳过去')
        while choose not in {'A','B','C','D'}:
            output('你会：A：前进,B：观察,C：后退,D：跳过去')
        if choose == 'A':
            output('你小心翼翼向前走去，圆筒的红光变成了紫光，还好没有什么大动静。')
        elif choose == 'B':
            output('你观察着圆筒，突然，红光闪烁了几下，一道红色的激光柱突然出现在你脚下，你被激光扫射到了【HP-40】')
            health -= 40
            dead_interface()
            if respawned == 1:
                respawned = 0
                continue
            output('你被激光扫中后，圆筒的光芒突然消失了')
        elif choose == 'C':
            output('你往后推去，没注意到后面突然出现了一截紫色的激光，你被激光扫射到了【HP-80】')
            health -= 80
            dead_interface()
            if respawned == 1:
                respawned = 0
                continue
            output('你被激光扫中后，圆筒的光芒突然消失了')
        elif choose == 'D':
            output('你跳着往前走去，红光闪烁了几下，一道蓝色的激光突然出现在你身旁，激光扫中了你【HP-120】')
            health -= 120
            dead_interface()
            if respawned == 1:
                respawned = 0
                continue
            output('你被激光扫中后，圆筒的光芒突然消失了')

        output('你通过激光，向前走去。前方又是一道悬崖，不过似乎不是很高。')
        output('你站在悬崖边上看着，突然，载着昵称的平台从下面升了上来。')
        output('“Zero！！我！我知道了！这平台是受我控制的！它……你到这来它就……啊这，这是不是你控制的……”昵称有点语无伦次。')
        output('突然，你看见昵称的旁边出现了两个显示屏，上面出现了许多字幕：')
        output('“我是赛恩思，昵称的敌人状态已经被我解除了，昵称可以下来了。”')
        output('昵称突然被什么东西推到了你所在的悬崖上。平台迅速降了下去。')
        output('弹窗上字幕不断地显现出来。')
        output('“然而，我不知道新一轮的攻击什么时候将前来，以防万一，我还是建议你们前往镇政府清除原始数据。只有你们亲自行动，数据才会被彻底清除。”')
        output('“我会带着你们前往镇政府，在这之前，你们需要先前往赛车场。”')
        output('最后这段话出现后，弹窗就没有动静了。')
        output('“啊……赛车场就在前面，我们走吧……”昵称往前走去，你也跟在后面。')
        output('你们左拐右拐，来到一座桥前，桥上装着传送带，传送带不断往后退。')
        output('“这……好像不能过去吧……”昵称说')
        go = 0
        while go == 0:
            output('你会：A：跳上桥,B：攀着桥沿过去,C：寻找其他道路')
            while choose not in {'A','B','C'}:
                output('你会：A：跳上桥,B：攀着桥沿过去,C：寻找其他道路')
            if choose == 'A':
                output('你跳上桥，传送带的速度并不快，但你发现昵称似乎跑不过去。你最后回到了起点。')
            elif choose == 'B':
                output('虽然但是，这桥没有桥沿，设计师是谁啊……')
            elif choose == 'C':
                output('你在旁边看了看，发现了一个红色的按钮，按下它之后，传送带停了。')
                go = 1
        output('你们通过桥，继续向前走，来到了一座巨大的绿色建筑物前面。')
        output('“嗨，这就是赛车场，不过这人也太……”昵称在你耳边小声说。')
        output('建筑物前面密密麻麻地布满了人，成群的车停在路边，他们把建筑以及周围的其它部分围了个水泄不通。')
        output('“哇……我们怎么进去呢？”昵称说。')
        output('你会：A：询问路人,B：随便逛逛')
        while choose not in {'A','B'}:
            output('你会：A：询问路人,B：随便逛逛')
        if choose == 'A':
            output('你找到了一个机器人，他有点不耐烦地说：“今年的赛车比赛是往年来最引人注目的，城市那帮家伙都跑过来了，票早都卖完了还堵在这里，我们都没法过去了。”')
        elif choose == 'B':
            output('建筑物的四周全都是密密麻麻的人和车，并没有什么有意思的。')
        output('你们在建筑物外面转了转，正当你们没辙的时候，昵称的身边出现了一个弹窗：')
        output('“警告！昵称已经被重新锁定为攻击对象——S281738368”')
        output('你回头一看，一些玩具车正在向昵称冲来，不过昵称似乎并没注意到。')
        output('你会：A：提醒昵称注意后方,B：推开昵称,C：挡在昵称前面')
        while choose not in {'A','B','C'}:
            output('你会：A：提醒昵称注意后方,B：推开昵称,C：挡在昵称前面')
        if choose == 'A':
            output('周围人车声十分嘈杂，昵称并没有听到你的提醒，玩具车向你们冲来')
            chooseb == 'fight'
        elif choose == 'B':
            output('你推开昵称，玩具车冲向你们后面的人群，人群发出了尖叫声，马上闪开一条道，赛车场大门露了出来。')
            output('“啊！我们快进去！”昵称对你说。')
            chooseb = 'peace'
        elif choose == 'C':
            output('你挡在昵称前面，玩具车向你们冲来')
            chooseb = 'fight'
        if chooseb == 'fight':
            choose = input('昵称吓了一跳：“什么东西？对……战？啊？我已经忘记怎么对战了，不过……”')
            choose = input('昵称干咳了一下：“好吧……我想想……啊！我想起来了！我有一个【猫叫芯片】，戳它可以……喵喵喵行吗……”')
            fight('玩具车',170,25,10,20,random.randint(180,360),'normal',0,2,170,25,10,20)
        savepoint = 9
    if savepoint == 9:
        save_data()
        output('你们快速冲进了赛车场，大厅里仍然是人山人海，把你们搞得晕头转向。')
        output('你好不容易找到了一个防火门，里面是一道楼梯，既有向上的也有向下的。')
        output('你转过头来，发现昵称并没有跟来，或许是跟丢了。')
        #恭喜go成为循环结构专用变量(
        go = 0
        up = 0
        while go == 0:
            output('你会：A：向上走,B：向下走,C：找昵称')
            while choose not in {'A','B','C'}:
                output('你会：A：向上走,B：向下走,C：找昵称')
            if choose == 'A':
                output('你向上走')
                up = 1
                go = 1
            elif choose == 'B':
                output('你向下走')
                go = 1
            elif choose == 'C':
                output('防火门开不开，看来是单向门，你不禁有点担心上面是否也无法开门。')
        if up == 1:
            output('你走上楼梯，前面又是一道防火门，你推开门来到外面。')
            output('你发现你来到了一个巨大的观众席上，上面挤满了人，你只能勉强挤到前面去。')
            choose = input('你勉强来到了一个能容身的地方，这时，一个弹窗出现在你面前。')
            output('“欢迎来到赛车场2F观众席，请记录你的购票信息。”')
            output('弹窗闪烁了一下，变成了一个输入界面。')
            output('你知道你没有购票。')
            output('你会：A：乱写一通,B：看看别人的弹窗,C：不理他')
            while choose not in {'A','B','C'}:
                output('你会：A：乱写一通,B：看看别人的弹窗,C：不理他')
            if choose in {'A','C'}:
                if choose == 'A':
                    output('你乱写一通，弹窗突然闪了一下，上面的字幕变成了：“发现逃票者，立即驱逐”')
                elif choose == 'C':
                    output('你不理会弹窗，这时，你的身前又出现了一个弹窗：“发现逃票者，立即驱逐”')
                output('你发现四周许多三角形的飞行器向你俯冲过来。')
                fight('六芒星飞行器',200,25,20,15,random.randint(40,440),'normal',0)
                if respawned == 1:
                    respawned = 0
                    continue
            elif choose == 'B':
                output('你看了看别人的弹窗，看见了一个购票ID，你把它填了上去。弹窗消失了。')
            output('你继续向前挤过人群，你的前面出现了一道楼梯，楼梯上的人不是很多。')
            go = 0
            while go == 0:
                output('你会：A：顺着楼梯向上走,B：顺着楼梯向下走,C：穿过楼梯向前走')
                while choose not in {'A','B','C'}:
                    output('你会：A：顺着楼梯向上走,B：顺着楼梯向下走,C：穿过楼梯向前走')
                if choose == 'A':
                    output('你向上走去，前面是一个升降门，不过一直在地上放着，并没有升起来的趋势。')
                elif choose == 'B':
                    output('你向下走去，下面是一个观景台，你看到了观景台下面绿色的充满着机械质感的赛道，不过比赛好像还没开始,周围人很多，你并不想和谁交谈')
                elif choose == 'C':
                    output('你穿过楼梯向前走去。')
                    go = 1
            output('你的前面出现了一座露天的平台，虽然平台上人很多，但你通过旁边的几个屏发现这似乎是个酒吧。')
            output('你穿过人群来到一个绿色的台子前，在你的前面，几个长相奇特的机器人正在捣鼓许多五颜六色的球状物。')
            output('过了一会儿，其中一个机器人看到你站在前面，开口说道：“这位先生，您需要来些什么？”')
            output('机器人旁边出现了一个绿色的弹窗，上面出现了各种奇怪的东西，不过全都写着“免费”字样。')
            output('你会选择：A：机械球,B：010鸡尾酒,C：霍拉克斯巧芙力洛马桑梅朵,D：更多弹窗,E：纠正机器人的对你性别的错误判断')
            while choose not in {'A','B','C','D','E'}:
                output('你会选择：A：机械球,B：010鸡尾酒,C：霍拉克斯巧芙力洛马桑梅朵,D：更多弹窗,E：纠正机器人的对你性别的错误判断')
            if choose == 'A':
                output('机器人给你了一个彩色的小球，你刚一拿起它，它立刻变身为一条彩色的、全身由方块组成的小蛇，然后跑走了。')
            elif choose == 'B':
                output('你的面前出现了一只力场组成的被子，里面凭空出现了许多彩色的小颗粒。但你一向它伸出手，那些小颗粒就从被子里溜到你的手臂上，钻进你的身体里。')
                output(f'你撩起衣服一看，发现你的肚皮变成了彩色的，而且在你的身上组成了一个{fun}的形状。')
                output('“这些是数据，可以标示世界的时空结构。”机器人说。')
            elif choose == 'C':
                output(f'你拿到了一把短剑，你挥了一下，发现它的形状在不断地变化。')
                output('“这东西是电脑模拟出的四维物体。”机器人说。')
                output('你感觉这东西并没有什么用。')
            elif choose == 'D':
                output('弹窗上面的文字突然变得十分扭曲，字样很快排列着向两边分散，然后弹窗分裂成了两个。')
                output('“绝佳的仿生技术——弹窗有丝分裂！伟大的发明！”机器人说。')
            elif choose == 'E':
                output('机器人说：“咱们的主机系统通过您的行为判断出了您是个男人，我也没办法哦！除非你——”')
            output('机器人突然说了一句：“哦对了，我忘记去楼上拿东西了，跟我过来一下。”')
            output('机器人起身离开，你跟着他走回了刚才的楼梯口。他走上楼梯，随即打开一个弹窗，楼梯上的那个升降门迅速升起，他快速通过了门。')
            go = 0
            while go == 0:
                output('请回复0或1以尝试进入电梯')
                while choose not in {'1','0'}:
                    print('格式错误!')
                    output('请回复0或1以尝试进入电梯')
                else:
                    choose = int(choose)
                floor = random.randint(0,1)
                if floor == choose:
                    go = 1
                    output('你成功走上了电梯！')
                else:
                    choose = input('你选择了错误的时机，你被绊倒了！[HP-5]')
                    health -= 5
                    dead_interface()
                    view_status()
            output('你爬上楼梯，你的旁边出现了一个写着“欢迎来到赛车场4F”的弹窗。')
            output('这里的人也十分密集，你小心地跟着机器人穿过人群，来到一座像是剧院的小房间里。房间里布满了座位，许多人围在一起在玩一种奇怪的桌游。')
            output('你跟着机器人来到一个门口，机器人突然对你说：“哦！我刚刚接收到了一些信号。看来您想前往电梯。电梯就在门后面，不过开门得经过看门老头的同意，他是个老赌徒，我估计您得和他玩点游戏啥的，祝您好运。”')
            choose = input('说完，机器人在你面前打开了一个弹窗，然后走开了。')
            output('你看了看这个弹窗，上面写着一个ID。你点了点这个ID，弹窗突然伸出了一道红线，一直延伸到一个正在玩桌游的机器人身上。')
            output('你来到机器人跟前，机器人注意到了你。')
            output('“嘿嘿……绿色3！赢啦！哦这里有一位新人呢！”')
            output('那个机器人站了起来：“嗨！您就是那位需要前往底下的？！走之前别忘了……玩点赛车棋哦！”')
            output('机器人身前弹出了一个弹窗，上面画着两个赛车。')
            output('哈！你，现在！快来玩这玩意儿！')
            print('[战斗开始]')
            compete_A = 0
            compete_B = 0
            compete_C = 0
            foot = 0
            enemy_foot = 0
            item_att = 0
            t.sleep(0.5)
            magic_point = 50
            win = 0
            a,b,c,d,e = '','','','',''
            choose = input('突然进入战斗界面的你有点懵。')
            choose = input('“我知道你在想什么！这游戏的规则很简单！每人都有两艘赛车，对战之前可以自选步数，谁先到终点谁就赢啦！”')
            choose = input('请点击魔法栏')
            while win == 0:
                magic_choose = 0
                att_choose = 0
                item_choose = 0
                while magic_choose == 0 and item_choose == 0:
                    chooseb = 'A'
                    print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health},你已经走了{foot}/10步,机器人走了{enemy_foot}/10步')
                    choose = input('A,物品B,防御C,魔法D,跳过')
                    while choose not in {'A','B','C','D'}:
                        print('请做出你的选择')
                        choose = input('A,物品B,防御C,魔法D,跳过')
                    if choose == 'A':
                        choose = input(f'你现在可使用的物品有{fight_item},请从1开始输入序号以选择使用的物品')
                        if choose not in {'1','2','3','4','5','6','7','8','9','10'}:
                            choose = input('物品序号输入错误!')
                        else:
                            choose = int(choose)
                            if choose > len(fight_item):
                                choose = input('物品序号输入错误!')
                            else:
                                if compete_B == 0:
                                    choose = input('机器人说：“哈哈哈！不行动你就加不了步数咯！”')
                                    compete_B = 1
                                choose -= 1
                                check = fight_item[choose]
                                if check == '冰棍':
                                    choose = input('你使用了冰棍!你的HP增加了15点!')
                                    health += 15
                                if check == '杆草':
                                    choose = input('你使用了杆草!你的HP增加了20点!')
                                    health += 20
                                if check == '流油果':
                                    choose = input('你使用了流油果!你的HP增加了40点,ATT临时增加了5点!')
                                    health += 40
                                    item_att += 5
                                if check == '花色汉堡':
                                    choose = input('你使用了花色汉堡!你的HP增加了50点!')
                                    health += 50
                                if check == '魔法炸药':
                                    choose = input('你使用了魔法炸药!莫得卵用(')
                                    health -= 30
                                    #假如说，你在这里爆炸了
                                    dead_interface()
                                    if respawned == 1:
                                        break
                                    if compete_C == 0:
                                        choose = input('机器人说：“啥？那东西对我无效！”')
                                        compete_C = 1
                                if check == '坚硬冰棍':
                                    choose = input('你使用了坚硬冰棍!莫得卵用(')

                                    if compete_C == 0:
                                        choose = input('机器人说：“啥？那东西对我无效！”')
                                        compete_C = 1
                                if check == '方块糖果':
                                    choose = input('你使用了方块糖果!你的HP增加了40点!')
                                    health += 40
                                if check == '红桃蛋糕':
                                    choose = input('你使用了红桃蛋糕!你的HP增加了100点!')
                                    health += 100
                                if check == 'CRD硬糖':
                                    choose = input('你使用了CRD硬糖!你的HP增加了14点,ATT临时增加了5点!')
                                    health += 14
                                    item_att += 5
                                if check == '冰淇淋':
                                    choose = input('你使用了冰淇淋!你的HP增加了40点,DEF扣了1点!')
                                    health += 40
                                    Def -= 1
                                if check == '能量饮料':
                                    choose = input('你使用了能量饮料!你的HP增加了20点,ATT临时增加了5点!')
                                    health += 20
                                    item_att += 5
                                if check == '五彩糖':
                                    choose = input('你使用了五彩糖!你的HP增加了20点!')
                                    health += 20
                                item.remove(check)
                                fight_item.remove(check)
                                item_choose = 1
                                if health > 240:
                                    health = 240
                    if choose == 'B':
                        if compete_B == 0:
                            choose = input('机器人说：“哈哈哈！不行动你就加不了步数咯！”')
                            compete_B = 1
                        choose = input('你选择了防御!')
                        magic_point += 40
                        magic_choose = 1
                        if magic_point >= 100:
                            magic_point = 100
                        chooseb = 'B'
                    if choose == 'C':
                        choose = input(f'A：走一步（10）B：走两步（20）C：走三步（30）')
                        while choose not in {'A','B','C'}:
                            print('请做出你的选择')
                            choose = input(f'A：走一步（10）B：走两步（20）C：走三步（30）')
                        else:
                            if choose == 'A':
                                if magic_point < 10:
                                    choose = input('你的魔法值不够!')
                                    magic_choose = 0
                                if magic_point >= 10:
                                    choose = input(f'你为赛车充了一部分能量')
                                    compete_A = 1
                                    magic_choose = 1
                                    magic_point -= 10
                            if choose == 'B':
                                if magic_point < 20:
                                    choose = input('你的魔法值不够!')
                                    magic_choose = 0
                                if magic_point >= 20:
                                    choose = input('你使用了一节虚拟的五号电池,赛车的能量回复了一半!')
                                    compete_A = 2
                                    att_choose = 1
                                    magic_choose = 1
                                    magic_point -= 20
                            if choose == 'C':
                                if magic_point < 30:
                                    choose = input('你的魔法值不够!')
                                    magic_choose = 0
                                if magic_point >= 30:
                                    choose = input('你擦动着一块充能水晶,赛车的能量被充满了!')
                                    compete_A = 3
                                    magic_choose = 1
                                    magic_point -= 30
                            choose = 0
                    if choose == 'D':
                        if compete_B == 0:
                            choose = input('机器人说：“哈哈哈！不行动你就加不了步数咯！”')
                            compete_B = 1
                        choose = input('你跳过了你的回合')
                        magic_choose = 1
                x = random.randint(1,4)
                a = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                b = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                c = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                d = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                e = chr(ord('A') + x - 1)
                enemy_fight = a+b+c+d+e
                enemy_fighta = [a,b,c,d,e]
                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                hurt = 0
                hurt_B = 0
                chance = 0
                wrong = 0
                while wrong == 0:
                    wrong = 1
                    if len(choose) != 5:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[0] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[1] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[2] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[3] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[4] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                else:
                    while chance < 5:
                        f = choose.pop()
                        g = enemy_fighta.pop()
                        if (f == 'A' and g == 'B') or (f == 'B' and g == 'C') or (f == 'C' and g == 'D') or (f == 'D' and g == 'A'):
                            hurt += 1
                            chance += 1
                        elif (f == 'D' and g == 'C') or (f == 'C' and g == 'B') or (f == 'B' and g == 'A') or (f == 'A' and g == 'D'):
                            hurt_B += 1
                            chance += 1
                        else:
                            chance += 1
                    choose = input(f'机器人的行动是{enemy_fight}')
                    if hurt > hurt_B:
                        choose = input(f'你前进了{compete_A}/10步!')
                        foot += compete_A
                    elif hurt < hurt_B:
                        go = random.randint(1,3)
                        choose = input(f'机器人前进了{go}/10步!')
                        enemy_foot += go
                    else:
                        choose = input('你们俩都没有前进')
                    hurt_B = 0
                    hurt = 0
                if foot >= 10:
                    choose = input('机器人说：“哈哈！恭喜你赢啦！咱们结束吧！”')
                    choose = input('您获胜了!')
                    win = 1
                elif enemy_foot >= 10:
                    choose = input('机器人说：“啊啊啊！你居然输啦！咱们再试一次吧！”')
                    foot = 0
                    enemy_foot = 0
                compete_A = 0
            output('机器人对你说道：“看来你赢啦！那么我就必须遵从指令了，你去门后吧。')
            output('你向门走去，门上弹起一个弹窗：\n“用户已确认”')
            output('门开了，你走进门里，你的前面出现了电梯，你走了进去。电梯只有“2F”的按钮，你乘着电梯来到了2楼。')
            output('电梯门开后，你走了出去，发现前面是一个绿色的平台，昵称正站在平台上。她看到了你，向你喊道：“Zero！我先到啦！”')
            output('你感到有点不快，但也没什么好说的，你们继续往前走去。')
            output('你来到了一座巨大的电梯前。')
            output('“我们到了呢。”昵称说。')
            output('你们走了进去。')
            output('电梯只有“2F”的按钮，你们乘着电梯来到了2楼。')
            output('电梯门开了，一个绿色的平台在你前面铺展开来。')
            output('你们往前走去。')
            output('你来到了一座巨大的电梯前。')
            output('“我们到了呢。”昵称说。')
            choose = input('你们走了进去。')
        if up == 0:
            output('你走下楼梯，前面是一道力场门。你看了看墙壁，上面是一个形状像数字33的灯。')
            output('你靠近力场门，突然一个弹窗出现在你面前，上面写着：“请输入正确的数码”')
            while choose not in {'100001'}:
                output('您输错了，请重新输入（')
            output('你通过了门')
            output('你输入了正确的数码，力场门一下子消失了。')
            output('你往前走去，来到了一个很大的办公室。里面并没有人在工作，不过四周的墙壁上挂着许多机械臂。')
            output('你来到一张工作台前面，上面摆放着许多你不认识的机器，各种奇怪的火光在工作台上跳动。你的旁边摆着一个灰色的小方块，它旁边一个蓝色的显示屏上写着“文件夹”三字。')
            output('你会：A：捣鼓工作台,B：查看文件夹,C：看看机械臂,D：向前走去')
            while choose not in {'A','B','C','D'}:
                output('你会：A：捣鼓工作台,B：查看文件夹,C：看看机械臂,D：向前走去')
            if choose == 'A':
                output('你摸了摸工作台，上面立即显示出乱七八糟的显示屏，上面标着各种复杂的符号。')
            elif choose == 'B':
                output('你凑近文件夹看了看，突然，方块的上方弹出了一个很大的显示屏，上面写着“选择资料”几个大字，下面是一行清单。')
                output('你看了看上面的资料，选了一本“正规电脑编程语言手册”，显示屏的周围立即弹出几个绿色的弹窗，围在显示屏旁边。')
                output('你看了看弹窗，其中一个写道')
                output('“如果你的电脑无法使用FireFox.max，请前往Y.Extend.exe查找相关下载地址。”')
                output('你关掉弹窗。')
            elif choose == 'C':
                output('你看了看机械臂，机械臂突然向你挥了挥手，看起来有点吓人。')
            output('你向前走去，办公室的前面有一扇自动门。当你穿过自动门后，前方出现了一条绿色的走廊。上面的电路图案以及四周的激光发射器看起来科技感十足。')
            output('你向前走去，刚踩在电路板上，四周就传来了一阵奇怪的类似猫叫的声音。')
            output('突然，旁边的墙壁向内凹去，许多机械臂伸了出来，向你做出奇怪的手势。')
            output('你发现其中一个机械臂拿着一片紫红色的芯片，你发现那就是昵称的“猫叫芯片”！')
            output('你会：A：继续前进,B：试图与机械臂交谈,C：向机械臂走去')
            while choose not in {'A','B','C'}:
                output('你会：A：继续前进,B：试图与机械臂交谈,C：向机械臂走去')
            if choose == 'A':
                output('你想继续前进，突然一个机械臂伸得长长的，挡住了你的去路！')
            elif choose == 'B' or choose == 'C':
                output('机械臂纷纷向前伸去，把你包围了起来。')
            output('前面的墙壁突然打开了一扇门，一个机械臂抓着灰头土脸的昵称向你伸来。')
            output('你的前面出现了一个显示屏：“种类：拟猫类\n威胁程度：2/5\n侵略指数：3/5”')
            output('两个机械臂突然伸到你面前，一道激光照射在你身上。')
            output('你的前面出现了一个显示屏，字幕不断跳动着：“种类：人类\n威胁指数：\n……\n威胁指数：\n无法测量”')
            output('弹窗闪了闪，然后消失了。')
            output('一声尖啸声传来，机械臂向你伸过来。')
            output('“开始捕捉”弹窗弹出')
            print('战斗开始,对战机械臂')
            item_att = 0
            t.sleep(0.5)
            miaomiao = 0
            clown = 240
            catch_A = 0
            catch_B = 0
            catch_C = 0
            magic_point = 0
            check = 0
            win = 0
            a,b,c,d,e = '','','','',''
            while win == 0:
                magic_choose = 0
                att_choose = 0
                item_choose = 0
                while magic_choose == 0 and item_choose == 0:
                    chooseb = 'A'
                    print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health},机械臂血量为{clown}')
                    choose = input('A,物品B,防御C,魔法D,跳过')
                    while choose not in {'A','B','C','D'}:
                        print('请做出你的选择')
                        choose = input('A,物品B,防御C,魔法D,跳过')
                    if choose == 'A':
                        choose = input(f'你现在可使用的物品有{fight_item},请从1开始输入序号以选择使用的物品')
                        if choose not in {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'}:
                            choose = input('物品序号输入错误!')
                        else:
                            choose = int(choose)
                            if choose > len(fight_item):
                                choose = input('物品序号输入错误!')
                            else:
                                choose -= 1
                                check = fight_item[choose]
                                if check == '冰棍':
                                    choose = input('你使用了冰棍!你的HP增加了15点!')
                                    health += 15
                                if check == '杆草':
                                    choose = input('你使用了杆草!你的HP增加了20点!')
                                    health += 20
                                if check == '流油果':
                                    choose = input('你使用了流油果!你的HP增加了40点,ATT临时增加了5点!')
                                    health += 40
                                    item_att += 5
                                if check == '花色汉堡':
                                    choose = input('你使用了花色汉堡!你的HP增加了50点!')
                                    health += 50
                                if check == '魔法炸药':
                                    choose = input('你对对方造成了100点伤害!但你也不小心受到了30点伤害')
                                    health -= 30
                                    clown -= 100
                                    dead_interface()
                                    if respawned == 1:
                                        break
                                if check == '坚硬冰棍':
                                    choose = input('你使用了坚硬冰棍!玩具车的HP降低了100点!')
                                    clown -= 100
                                if check == '方块糖果':
                                    choose = input('你使用了方块糖果!你的HP增加了40点!')
                                    health += 40
                                if check == '红桃蛋糕':
                                    choose = input('你使用了红桃蛋糕!你的HP增加了100点!')
                                    health += 100
                                if check == 'CRD硬糖':
                                    choose = input('你使用了CRD硬糖!你的HP增加了14点,ATT临时增加了5点!')
                                    health += 14
                                    item_att += 5
                                if check == '冰淇淋':
                                    choose = input('你使用了冰淇淋!你的HP增加了40点,DEF扣了1点!')
                                    health += 40
                                    Def -= 1
                                if check == '五彩糖':
                                    choose = input('你使用了五彩糖!你的HP增加了20点!')
                                    health += 20
                                if check == '能量饮料':
                                    choose = input('你使用了能量饮料!你的HP增加了20点,ATT临时增加了5点!')
                                    health += 20
                                    item_att += 5
                                if check == '冰冻面包':
                                    health += 50
                                    choose = input('你使用了冰冻面包!你的HP增加了50点,本回合敌人无法对你造成伤害!')
                                if check == '电路板寿司':
                                    health += 50
                                    choose = input('你使用了电路板寿司!你的HP增加了50点,ATT临时增加了20点!')
                                    item_att += 20
                                item.remove(check)
                                fight_item.remove(check)
                                item_choose = 1
                                if health > 300:
                                    health = 300
                    if choose == 'B':
                        choose = input('你选择了防御!')
                        magic_point += 40
                        magic_choose = 1
                        if magic_point >= 100:
                            magic_point = 100
                        chooseb = 'B'
                    if choose == 'C':
                        choose = input(f'A：治疗魔法（{health_point}）B：战斗魔法（70）C：黑暗魔法（？）D：逃脱（30）')
                        while choose not in {'A','B','C','D'}:
                            print('请做出你的选择')
                            choose = input(f'A：治疗魔法（{health_point}）B：战斗魔法（70）C：黑暗魔法（？）D：逃脱（30）')
                        else:
                            if choose == 'A':
                                if magic_point < health_point:
                                    choose = input('你的魔法值不够!')
                                    magic_choose = 0
                                if magic_point >= health_point:
                                    choose = input(f'你使用了治疗法术!你的血量回复了{health_plus}点!')
                                    health += health_plus
                                    magic_choose = 1
                                    magic_point -= 30
                                if health > 300:
                                    health = 300
                                    magic_choose = 1
                            if choose == 'B':
                                if magic_point < 70:
                                    choose = input('你的魔法值不够!')
                                    magic_choose = 0
                                if magic_point >= 70:
                                    choose = input('你使用了战斗法术!你的攻击提高了5点,持续一回合!')
                                    att_choose = 1
                                    magic_choose = 1
                                    magic_point -= 70
                            if choose == 'C':
                                choose = input('l͓̩̫̘͙͔̯͖̟̤̓͊̑̌́̂̆̚ò̥̪̭̱̰̝̒͂̄͋̿̏͆́̚c͍̲͇͚̖̬͈̪͙̳͌̉́̃k̪̥̱̝̱̑̈́̏̽͗̊̈́͂̀̍e̞͎̩̜̱̩͚̤̊͌̀̀d̠̖̞̝̙̪̟̞̐͛̈̊̀͂̄͌̓̏͌̓ͅ')
                                magic_choose = 0
                            if choose == 'D':
                                if magic_point < 30:
                                    choose = input('你的魔法值不够!')
                                    magic_choose = 0
                                if magic_point >= 30:
                                    choose = input('你尝试逃脱机械臂的抓捕!')
                                    magic_choose = 1
                                    magic_point -= 30
                                    chooseb = 'C'
                            choose = 0
                    if choose == 'D':
                        choose = input('你跳过了你的回合')
                        magic_choose = 1
                x = random.randint(1,4)
                a = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                b = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                c = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                d = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                e = chr(ord('A') + x - 1)
                enemy_fight = a+b+c+d+e
                enemy_fighta = [a,b,c,d,e]
                zero_att = 0
                if '零剑' in weapon:
                    zero_att = random.randint(5,50)
                if '混乱护盾' in armor:
                    health += random.randint(3,20)
                    if health >= 300:
                        health = 300
                clown_act_B = random.randint(1,3)
                if clown_act_B == 1:
                    choosec = input('机械臂张牙舞爪地向你伸来')
                if clown_act_B == 2:
                    choosec = input('机械臂展现了航天品质')
                if clown_act_B == 3:
                    choosec = input('机械臂紧紧地捏住昵称')
                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                hurt = 0
                hurtB = 0
                chance = 0
                wrong = 0
                while wrong == 0:
                    wrong = 1
                    if len(choose) != 5:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[0] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[1] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[2] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[3] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[4] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                else:
                    clown_act = random.randint(1,5)
                    while chance < 5:
                        f = choose.pop()
                        g = enemy_fighta.pop()
                        if chooseb != 'B':
                            if (f == 'A' and g == 'B') or (f == 'B' and g == 'C') or (f == 'C' and g == 'D') or (f == 'D' and g == 'A'):
                                if chooseb == 'C':
                                    catch_C += 10
                                hurt += att
                                chance += 1
                                if att_choose == 1:
                                    hurt += 5
                                if clown_act > 3:
                                    hurt -= 50
                                hurt += item_att
                                if hurt <= 0:
                                    hurt = 0
                                hurt += zero_att
                        if (f == 'D' and g == 'C') or (f == 'C' and g == 'B') or (f == 'B' and g == 'A') or (f == 'A' and g == 'D'):
                            hurtB += 15
                            catch_A += 10
                            if chooseb == 'C':
                                catch_A -= 10
                            if chooseb == 'B':
                                hurtB -= Def
                                if Def >= 15:
                                    hurtB = 0
                            chance += 1
                        else:
                            chance += 1
                    if armor == '液晶裙' and random.randint(1,50) == 20:
                        hurtB = 0
                    clown -= hurt
                    health -= hurtB
                    if check == '冰冻面包':
                        hurtB = 0
                        check = ''
                    item_att = 0
                    choose = input(f'敌方的攻击是{enemy_fight}')
                    if clown_act > 3 :
                        choose = input('机械臂使用了防御!')
                    if chooseb != 'B':
                        choose = input(f'你对敌方造成了{hurt}点伤害!')
                        hurt = 0
                    if chooseb == 'B':
                        choose = input('因为你选择了防御,所以伤害不计入')
                    choose = input(f'你被机械臂扣除了{hurtB}点血')
                    dead_interface()
                    if respawned == 1:
                        break
                    hurtB = 0
                    if chooseb == 'C':
                        choose = input(f'你的[{catch_C}%]逃脱了机械臂的捕捉！')
                        catch_B -= catch_C
                    att_choose = 0
                    choose = input(f'机械臂捕捉了你的[{catch_A}%]!')
                    catch_B += catch_A
                    catch_A = 0
                    if catch_B >= 100:
                        choose= input('机械臂捕捉了你！你的HP减少了150！')
                        health-=150
                        dead_interface()
                        if respawned == 1:
                            respawned = 0
                            continue
                        choose = input('机械臂松开了。')
                        catch_B = 0
                    choose = input(f'你现在的累计捕捉度为[{catch_B}%]')
                if clown <= 0:
                    choose = input('您获胜了!')
                    CM_get = random.randint(5,820)
                    CM += CM_get
                    choose = input(f'你获得了{CM_get}个CM币')
                    win = 1
            if respawned == 1:
                respawned = 0
                continue
            choose = input('机械臂乱抓着缩了回去。')
            choose = input('昵称被放了下来，然后向你大叫：“Zero！我刚刚被这群机械臂抓到下面了！要是你不来我就会被它……”')
            choose = input('昵称叫了好久，不过之后自己也感觉有点尴尬，逐渐停止了叫声。')
            choose = input('“我们走吧。”')
            choose = input('你和昵称向前走去，前面是一个三岔路口。四周的墙壁都发着淡淡的绿光')
            choose = input('你会：A：向左走,B：向右走')
            while choose not in {'A','B'}:
                choose = input('你会：A：向左走,B：向右走')
            if choose == 'A':
                choose = input('左边是一堵发着不同颜色荧光的墙，并没有什么特别的，你便向另一边走去')
            elif choose == 'B':
                choose = input('你向右走去')
        choose = input('你们来到一座巨大的传送带前，传送带上面又是一个升降门')
        go = 0
        while go == 0:
            output('请回复0或1以尝试进入升降门')
            while choose not in {'1','0'}:
                print('格式错误!')
                output('请回复0或1以尝试进入升降门')
            else:
                choose = int(choose)
            floor = random.randint(0,1)
            if floor == choose:
                go = 1
                output('你成功走上了升降门！')
            else:
                choose = input('你选择了错误的时机，你被绊倒了！[HP-5]')
                health -= 5
                dead_interface()
                view_status()
        output('你们通过升降门，来到传送带的对岸。')
        output('你们的前面是一座小房子，在周围的高楼衬托下显得平平无奇。')
        output('你的前面出现了一个弹窗：“前方：镇政府”')
        output('你走到玻璃房门前，突然，门上出现了一长串二进制数字，')
        savepoint = 10
    if savepoint == 10:
        save_data()
        output('这些数据快速跳动着，你不知道在表示什么。')
        output('你会：A：敲门,B：环顾四周,C：走开')
        while choose not in {'A','B','C'}:
            output('你会：A：敲门,B：环顾四周,C：走开')
        wait = 0
        if choose == 'A':
            output('你敲了敲门，并没有什么用。')
        elif choose == 'B':
            output('你环顾四周，周围的道路上人来人往，十分热闹')
        elif choose == 'C':
            output('你后退了一步，突然，你看清楚了前面门上的数字组成了一个“SCI”字样。就在这时，门打开了')
            wait = 1
        if wait == 0:
            output('门突然打开了，里面钻出两个机器人，友好地对你们说：“是塞恩斯先生请来的客人吗？”如果是的话，请回答出他的编号。”')
            output('你的前面出现了四个弹窗。')
        output('你会选择：A：S28I738368,B：S28I738398,C：S281738398,D：S281736368,E：无动于衷')
        while choose not in {'A','B','C','D','E'}:
            output('你会选择：A：S28I738368,B：S28I738398,C：S281738398,D：S281736368,E：无动于衷')
        if choose in {'A','B','D'}:
            output('你正要选择那个弹窗，突然昵称冲到你前面，选择了第三个弹窗')
            output('“不管怎么样我可是记得的……”')
        elif choose == 'C':
            output('你选择了第三个弹窗，弹窗变成了绿色。')
        elif choose == 'E':
            output('你无动于衷，昵称走上前选择了第三个弹窗')
            output('“不管怎么样我可是记得的……”')
        output('机器人说：“回答正确，请进。”')
        output('你们进入大厅，虽然这里的空间并不是很大，但因为没什么人，所以你们感觉十分宽敞。')
        output('你看了看大厅的内置，一个绿色的前台边站着一些机器人，你们的旁边是一个图书阅览室，前面还有两扇门。')
        output('你看了看大厅绿色的墙壁，上面挂着许多图形，在一个角落里还摆放着一座奇怪的机器。')
        output('你会：A：去前台,B：去图书阅览室,C：去前面的门,D：看看墙壁,E：看看机器')
        while choose not in {'A','B','C','D','E'}:
            output('你会：A：去前台,B：去图书阅览室,C：去前面的门,D：看看墙壁,E：看看机器')
        if choose == 'A':
            output('你来到了前台，机器人说：“您就是塞恩斯先生请来的客人。请稍等，塞恩斯先生的另一位委托人还没有来。')
        elif choose == 'B':
            output('你来到图书阅览室，发现里面都是一座一座的大机器，你不知道它们的操纵原理是什么。')
        elif choose == 'C':
            output('门打不开')
        elif choose == 'D':
            output('你看了看墙壁，突然，墙壁上放射出一阵电流，你被击中了[HP-10]')
            health -= 10
            dead_interface()
        elif choose == 'E':
            output('机器被力场包围，发着蓝光。一个全系铭牌上写着“力场发生器”的字样。')
        output('你在大厅里待了一会儿，这时有一个机器人来到了你们面前，说：')
        output('“您好，塞恩斯先生的委托人已经来了，请和我到后面的房间里去，我们会在那里进行解除手续。')
        output('昵称站起来跟着机器人前面走去，你也跟在昵称的身后。')
        output('随着你们的靠近，前面的门自动打开，出现一道向下的台阶，里面的灯光似乎在变暗。')
        output('“请下楼。”机器人说。')
        output('你们走下楼梯，机器人仍然站在楼上，你听见门关上了。')
        output('“委托人就在后面。”机器人说')
        output('你们转头看去，后面是一道长廊，一个身穿深蓝色卫衣的人向你们走来，你听见昵称在你身边发出一声惊叫：')
        output('“SO？！！！”')
        output('那人愣了一下，朝你们跑来，你看清了他就是So。')
        output('“怎么回事？塞恩斯的委托人呢？！”So见到了你们，惊讶地问道。')
        output('“我们也不清楚啊！他……也是让我们见委托……So你还好吗？”昵称呆呆地看着SO。')
        output('“我没事。可是这塞恩斯……他骗了我们！等等！小心前面！”')
        output('你发现前面走廊尽头突然冒出了一丝蓝光。')
        output('“小心激光阵！！！”So叫道，顺势拉起昵称躲在一边。')
        chanceb = 0
        choose = input('(输入ABCD以躲避激光)')
        while chanceb < 3:
            chanceb += 1
            choose = list(input(f'请输入你的第{chanceb}次躲避方式'))
            x = random.randint(1,4)
            a = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            b = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            c = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            d = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            e = chr(ord('A') + x - 1)
            enemy_fight = a+b+c+d+e
            enemy_fighta = [a,b,c,d,e]
            hurt = 0
            hurtB = 0
            chance = 0
            wrong = 0
            while wrong == 0:
                wrong = 1
                if len(choose) != 5:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请输入你的第{chanceb}次躲避方式'))
                elif choose[0] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请输入你的第{chanceb}次躲避方式'))
                elif choose[1] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请输入你的第{chanceb}次躲避方式'))
                elif choose[2] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请输入你的第{chanceb}次躲避方式'))
                elif choose[3] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请输入你的第{chanceb}次躲避方式'))
                elif choose[4] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请输入你的第{chanceb}次躲避方式'))
            else:
                while chance < 5:
                #快悄悄这个地方,我把chance < 5写成了chance <= 5然后查了一天才查到这个bug
                #悄悄改为瞧瞧,这是个错别字(划)通假字
                #快看,这里我复制的前面
                    f = choose.pop()
                    g = enemy_fighta.pop()
                    if f == 'D' and g == 'C' or f == 'C' and g == 'B' or f == 'B' and g == 'A' or f == 'A' and g == 'D':
                        hurtB += 15
                        chance += 1
                    else:
                        chance += 1
                health -= hurtB
                choose = input(f'激光的进攻方式是{enemy_fight}')
                choose = input(f'你被扣除了{hurtB}点血量')
                dead_interface()
                if respawned == 1:
                    respawned = 0
                    continue
        output('你们躲在一旁，前面的激光停止了射击。')
        output('“快！我们快走！前面走廊尽头有个电梯，我们可以从那儿下去！小心激光阵！”So说道。')
        output('你们向前跑去，然而当你们跑到走廊尽头时，你只发现了一道锁着的门和一个冒着蓝光的机器。')
        output('“我的天！我们被困住了！”')
        output('这时，你们听见你们后面传来了阵阵脚步声，许多拿着枪——看上去非常奇特的款式，上面有很多黄色的线圈——的机器人向你们冲来。')
        output('“不许动”为首的机器人说。')
        output('你发现身后的机器冒出了红光。')
        output('你听见So在身边悄悄对昵称说：“别怕，这是屏蔽笼，我可以用我的“暗蓝卫衣”把它转移出去，不过还是避免不了战斗……”')
        output('你突然听到一声巨响，你本能地躲开，却发现So已经脱下卫衣遮住后面的机器，而你的前面出现了一个奇异的红色光球。')
        output('“见鬼啦！这是怎么做到的！”机器人说道，顺便发出了几声嘈杂的金属响声，可能是在谩骂。')
        output('“这门的力场已经没了，我们撞出去！”So拾起卫衣说道。你们一起撞开了门，来到一片露天平台。')
        output('在你的前方便是一座高大的悬崖，悬崖下方的一片黑压压的森林，被在你前面远处，一片朝着视野尽头无限延伸的超巨大城市发出的蓝色绚烂光芒所掩盖。')
        output('你们快速跑上前面的一座传送带，前面出现了十道升降门阵。')
        output('“这不可能过吧……”昵称说。')
        output('“可以的，你观察一下，每几轮就会出现一个特殊类型，很容易的。”So回答。')
        go = 0
        mark = 0
        while go == 0:
            code = []
            if mark % 3 == 2:
                for i in range(5):
                    ke = random.randint(0,1)
                    if ke == 0:
                        code.append('0000000000')
                    elif ke == 1:
                        code.append('1111111111')
            else:
                for i in range(5):
                    code.append(chr(ord('0')+random.randint(0,1))+chr(ord('0')+random.randint(0,1))+chr(ord('0')+random.randint(0,1))+chr(ord('0')+random.randint(0,1))                                +chr(ord('0')+random.randint(0,1))+chr(ord('0')+random.randint(0,1))+chr(ord('0')+random.randint(0,1))+chr(ord('0')+random.randint(0,1))+chr(ord('0')+random.randint(0,1))+chr(ord('0')+random.randint(0,1)))

            for i in range(1):
                choose = input('请输入10个0-9的数字')
                wrong = 0
                while wrong == 0:
                    wrong = 1
                    if len(choose) != 10:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = input('请输入10个二进制的数字')
                    elif choose[0] not in {'0','1'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = input('请输入10个二进制的数字')
                    elif choose[1] not in {'0','1'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = input('请输入10个二进制的数字')
                    elif choose[2] not in {'0','1'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = input('请输入10个二进制的数字')
                    elif choose[3] not in {'0','1'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = input('请输入10个二进制的数字')
                    elif choose[4] not in {'0','1'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = input('请输入10个二进制的数字')
                    elif choose[5] not in {'0','1'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = input('请输入10个二进制的数字')
                    elif choose[6] not in {'0','1'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = input('请输入10个二进制的数字')
                    elif choose[7] not in {'0','1'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = input('请输入10个二进制的数字')
                    elif choose[8] not in {'0','1'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = input('请输入10个二进制的数字')
                    elif choose[9] not in {'0','1'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = input('请输入10个二进制的数字')
                mark += 1
                input('升降门密码是'+code[i-1])
                if choose == code[i-1]:
                    input('你通过了所有升降门')
                    go = 1
                else:
                    input('通过失败，请从1号升降门重新开始')
                    break
        
        output('你们通过升降门阵，来到一个大平台上，平台上只有一幅蓝色的大海报，一个扫地机器人在你们旁边工作着。')
        output('“我们往前走。”So说道。')
        output('你看了看前面，找到了一条小路，很不巧，一座力场门挡在前面。')
        output('“嗯……我们被困住了，好像是这样的。”So说。')
        output('你会：A：看海报,B：看力场门,C：问扫地机器人')
        go = 0
        while go == 0:
            while choose not in {'A','B','C'}:
                output('你会：A：看海报,B：看力场门,C：问扫地机器人')
            if choose == 'A':
                output('海报上画着一座奇怪的巨塔。')
            elif choose == 'B':
                output('力场门打不开')
            elif choose == 'C':
                go = 1
        output('机器人说：“我只是个普通的扫地机器人，一直固定在这里清扫，我不知道怎么帮你们。不过呢……或许你们可以把我拆解了借我身上的东西用？”')
        output('听到这句话，昵称便拿出芯片走近机器人：“让我看看……”')
        output('就在这时，你看到机器人旁边冒出了一个红色的气泡，So大声喊道：“昵称！快跑！别靠近它！”但是已经晚了，机器人身边的气泡突然变大，出现了奇怪的网状花纹，把昵称整个罩在了里面。')
        output('“远距离传输系统运行完毕，正在准备撤离。”机器人慢慢吞吞地说。')
        output('“你！你是……”So气愤地大叫道。')
        output('“我是塞恩斯。”机器人说道，“但你们不要妄想抓住我，我随时可以传输到魔法网络内部的任何一个主机节点上，即使你打爆这个可怜的机器人，受害的也只是它。”')
        output('“可恶！你为什么要这样！你为什么要抓走昵称！”So喊道')
        output('“不只是昵称。我的任务是抓住你们三个人，可惜我只剩这一个屏蔽笼了。”塞恩斯说着，往后退了几步。')
        output('“可恶啊啊啊啊！！！”So喊道，随即从衣服里取出几个光球，射向塞恩斯，不过这些光球一碰到塞恩斯周围，都在一个无形的圆周上化成一圈圈波纹。')
        output('“你无法伤害到我了，刚才我已经测试过你的能力。你很难缠，不过我已经解决了这个小问题。毕竟解决问题是我的本职工作。”塞恩斯用轻蔑的语气说。')
        output('“你！你到底要干什么！有本事就把昵称放下来打一场！”')
        output('So大声喊道，他生气的样子与刚才转移屏蔽笼时大相径庭。')
        output('“呵呵，我的任务与你们无关。我只是一个普通的网络科学家与社会学家而已，我的任务是研究网络事物的运行规律。很抱歉，你们三位外来人士正好是我研究课题的误差，我需要尽可能地减小误差。本来我想把你们一网打尽的，不过以后也还有机会，再见了。”')
        output('塞恩斯说完，旁边的墙壁上便打开一道漆黑的门，塞恩斯带着被包裹的昵称钻了进去，墙壁立刻恢复了原状。')
        output('“该死！把昵称还回来啊！！！”So无能狂怒。')
        output('你看到身后传来了一阵嘈杂声，你发现你们登上平台的传送带上已经出现了机器人。')
        output('你会：A：向左边跑去,B：向右边跑去')
        while choose not in {'A','B'}:
            output('你会：A：向左边跑去,B：向右边跑去')
        if choose == 'A':
            output('左边的不远处出现了许多电塔，你们认为可以顺着电塔的线圈滑下去。')
            output('“抓住卫衣，它可以屏蔽电场，不过这玩意儿的电流太大了，不是我不能屏蔽，是你得小心点别滑到外面去了。”So说')
            output('回复字母A、B、C、D以牢牢抓住卫衣')
            chanseb = 0
            while chanceb < 1:
                chanceb += 1
                choose = list(input(f'请输入你的行动'))
                x = random.randint(1,4)
                a = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                b = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                c = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                d = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                e = chr(ord('A') + x - 1)
                enemy_fight = a+b+c+d+e
                enemy_fighta = [a,b,c,d,e]
                hurt = 0
                hurtB = 0
                chance = 0
                wrong = 0
                while wrong == 0:
                    wrong = 1
                    if len(choose) != 5:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请输入你的行动'))
                    elif choose[0] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请输入你的行动'))
                    elif choose[1] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请输入你的行动'))
                    elif choose[2] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请输入你的行动'))
                    elif choose[3] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请输入你的行动'))
                    elif choose[4] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请输入你的行动'))
                while chance < 5:
                #快悄悄这个地方,我把chance < 5写成了chance <= 5然后查了一天才查到这个bug
                #悄悄改为瞧瞧,这是个错别字(划)通假字
                #快看,这里我复制的前面
                    f = choose.pop()
                    g = enemy_fighta.pop()
                    if f == 'D' and g == 'C' or f == 'C' and g == 'B' or f == 'B' and g == 'A' or f == 'A' and g == 'D':
                        hurtB += 15
                        chance += 1
                    else:
                        chance += 1
                health -= hurtB
                choose = input(f'电流以{enemy_fight}的形式在电塔上跳动')
                choose = input(f'你被电流扣除了{hurtB}点血量')
                dead_interface()
                if respawned == 1:
                    respawned = 0
                    continue
        elif choose == 'B':
            output('你们的右边出现了一堵高墙，你在墙边发现了一个红色的按钮，上面写着“小心触电。”')
            output('你会：A：按下它,B：让So按')
            while choose not in {'A','B'}:
                output('你会：A：按下它,B：让So按')
            if choose == 'A':
                choose = input('你按下按钮，感觉被电击了一下[HP-20]【你 傻 了】')
                health -= 20
                dead_interface()
                view_status()
            elif choose == 'B':
                output('So用卫衣护着手指按了按钮')
        savepoint = 11
    if savepoint == 11:
        save_data()
        output('你发现前面那条小路上的力场门打开了，你们跑进小路，你们的前面是电梯。')
        output('你们走进电梯，按下1F按钮，电梯往下降。')
        output('你们来到一楼，跑上一条发着黄色荧光的小路。你们的前面是茂密的蓝色森林，树木发着淡淡的光亮，但由于被远处城市的光芒掩盖了，看得并不是很清楚。')
        output('你们匆忙地跑了一段，道路在前面分出了一条通往森林里的小路。')
        output('你会：A：去森林,B：不去')
        while choose not in {'A','B'}:
            output('你会：A：去森林,B：不去')
        if choose == 'A':
            output('你进入森林')
        elif choose == 'B':
            output('你继续向前走，但前面的道路被一块大石头挡住了，你在石头的后面找到了一把玩具枪！')
            item.append('离子枪')
            output('你还是进入了森林。')
        output('小路在森林里延伸了一段，最后结束在一座绿色的墓碑前，So往前走去观察地形。')
        output('你会：A：观察墓碑,B：看看树叶,C：提防后方')
        go = 0
        while go == 0:
            while choose not in {'A','B','C'}:
                output('你会：A：观察墓碑,B：看看树叶,C：提防后方')
            if choose == 'A':
                output('墓碑上写着：')
                choose = input('愿此生的烈火永远延续下去。\nFirefox.max\n00000000000000\n网址终结代码【此处下载】')
                view_status()
            elif choose == 'B':
                output('你看着树叶，上面的数字流向三个方向')
                go = 1
            elif choose == 'C':
                output('后方一片寂静')
        output('So看见了你在观察树叶，疑惑地说：“这些树叶有什么特别的呢？”')
        output('正当So说完，你发现树叶前面突然出现了一个弹窗：')
        output('电子树编号：230282974方向1:城市\n向2:Tetris商店\n方向3:黑客村庄')
        output('So说道：“看来是个路标，我觉得我们应该去城市。”')
        output('你会：A：往方向1走,B：往方向2走,C：往方向3走')
        while choose not in {'A','B','C'}:
            output('你会：A：往方向1走,B：往方向2走,C：往方向3走')
        output('虽然这样，你却并不知道你选了哪个方向，你们只能摸着树叶小心翼翼地往前走去。')
        output('过一会儿，你们的视野逐渐开阔了起来，前方隐隐约约地出现了一个小房子。')
        output('正当你想往房子里走时，So上前拉住了你：“当心有埋伏！”')
        output('你会：A：向前冲出去,B：留在原地,C：观察地形')
        while choose not in {'A','B','C'}:
              output('你会：A：向前冲出去,B：留在原地,C：观察地形')
        if choose == 'A':
              output('你向前冲了出去，So没办法只能跟你出来')
        elif choose == 'B':
              choose = input('你留在原地，意外地在地上发现了一个围巾！')
              item.append('电动围巾')
              view_status()
        elif choose == 'C':
              output('你看了看房子，房子泛着蓝光，上面挂着一个带有“Tetris”字样的招牌，看起来是个小店。')
        output('你们接近小房子，这是一个小型便利店，不过旁边有个很大的停车场。')
        output('你们进入便利店，里面只有一个售货员在营业他看到你们，对你们打招呼说：“欢迎各位来到Tetris小店，你们要买什么？”')
        shop = 0
        while shop == 0:
            output('请选择需要购买的物品：A：Tetris彩糖【100CMB】,B：电磁激光枪【200CMB】,C：神秘车票【400CMB】（限购一张）,D：FireFox.max（破损）【2000CMB】,E：离开')
            while choose not in {'A','B','C','D','E'}:
                print('请做出您的选择')
                output('你会购买：A：Tetris彩糖【100CMB】,B：电磁激光枪【200CMB】,C：神秘车票【400CMB】（限购一张）,D：FireFox.max（破损）【2000CMB】,E：离开')
            else:
                money = 0
                buy = 0
                if choose == 'A':
                    if CM < 100:
                        output('你的CM币不够!')
                    else:
                        buy = 'Tetris彩糖'
                        money = 100
                if choose == 'B':
                    if CM < 200:
                        output('你的CM币不够!')
                    else:
                        buy = '电磁激光枪'
                        money = 200
                if choose == 'C':
                    if CM < 400:
                        output('你的CM币不够!')
                    else:
                        buy = '神秘车票'
                        money = 400
                if choose == 'D':
                    if CM < 2000:
                        output('你的CM币不够!')
                    else:
                        buy = 'FireFox.max（破损）'
                        money = 2000
                if choose == 'E':
                    shop = 1
                if len(item) >= 10 and buy != 0:
                    view_status()
                if ('电磁激光枪' in item or armor == '电磁激光枪') and buy == '电磁激光枪':
                    buy = 0
                    output('你已经购买这个物品了!')
                if 'FireFox.max（破损）' in item and buy == 'FireFox.max（破损）':
                    buy = 0
                    output('你已经购买这个物品了!')
                if buy != 0:
                    if buy in {'Tetris彩糖'}:
                        fight_item.append(buy)
                    if buy == '电磁激光枪':
                        laser = 1
                    if buy == 'FireFox.max（破损）':
                        aoenfewg = 1
                    item.append(buy)
                    output(f'你购买了{buy}!')
                buy = 0
                CM -= money
        tower = 0
        shops.append('商店2')
        output('你们正准备离开，售货员突然拉住你，说：“哦对了，你们需不需要车票——”')
        output('“什么车票？”So问')
        output('“你们要是想离开这里，你们就需要车票……呃……不是吗？”售货员说。')
        output('“嗯对。”So说。')
        output('“好吧，车票在这里免费取，你们需要什么线路？哦……对了，线路是一串五位二进制数字。”售货员说。')
        output('（请输入任意的五位二进制数字）')
        if len(choose) != 5:
            choose = '12345'
        while len(choose) != 5 or choose[0] not in {'1','0'} or choose[1] not in {'1','0'} or choose[2] not in {'1','0'} or choose[3] not in {'1','0'} or choose[4] not in {'1','0'}:
            choose = input('格式错误！请重新输入')
            if len(choose) != 5:
                choose = '12345'
        output('售货员拿出一张银色的小方块。“拿着，这是车票，请前往停车场候车。”')
        output('你们出了门，来到停车场，一辆你们之前看到的车子停在你们面前，车上并没有人。你一接近车，手中的车票便发出了彩色的光芒。')
        output('你们坐上车，车票便飞上了车前的一块面板上，车顿时启动，随即便朝前开始飞速行驶。')
        hecker = 0
        normal = 1
        if '神秘车票' in item:
            output('车子左拐右拐，在一个村庄前停了下来。')
            output('“这里好像不是我们要去的地方。”So说道')
            output('你会：A：继续前进,B：乘车离开')
            while choose not in {'A','B'}:
                output('你会：A：继续前进,B：乘车离开')
            if choose == 'A':
                hecker = 1
                normal = 0
            elif choose == 'B':
                output('你们进入车子，车子继续往前驶去')
                normal = 1
        if hecker == 1:
            output('你们向前走去，前面这是一个破破烂烂的小村庄。')
            output('你向前走了一段，突然你好像碰到了一堵墙，定睛一看前面并没有什么东西。')
            output('你伸手摸了摸前方，发现这里确实有一堵隐形的墙！')
            output('就在此时，一个显示屏在你面前弹出：\n“请出示车票。”')
            output('你拿出那张神秘车票，车票立刻发出了剧烈的紫光，和前面的“墙”融合在一起。前面的空间立即出现了一道紫色的方框。你和So随即通过了方框，来到墙后的地点。')
            item.remove('神秘车票')
            output('你发现这里是另一座小村庄，虽然看上去小，但完全不同于墙外看起来的那种破破烂烂的样子。绿色的荧光在房屋上跳动，路面的图案看上去十分复杂，许多机器人在街上缓慢地行走，看起来十分悠闲。')
            output('街上的房屋都紧闭着门，只有一座挂着许多彩灯的房子的大门敞开着，你的旁边是一座大大的“H”雕塑，后面出现了几座发电塔。')
            speak = 0
            act = 0
            go = 0
            cake = 0
            while go == 0:
                if speak == 0:
                    output('你会：A：找人聊天,B：前往彩灯房,C：前往雕塑,D：前往发电塔,E：离开此地')
                    while choose not in {'A','B','C','D','E'}:
                        output('你会：A：找人聊天,B：前往彩灯房,C：前往雕塑,D：前往发电塔,E：离开此地')
                    if choose == 'A':
                        act = 1
                    elif choose == 'B':
                        act = 2
                    elif choose == 'C':
                        act = 3
                    elif choose == 'D':
                        act = 4
                    elif choose == 'E':
                        act = 5
                elif speak == 1:
                    output('你会：A：前往彩灯房,B：前往雕塑,C：前往发电塔,D：离开此地')
                    while choose not in {'A','B','C','D'}:
                        output('你会：A：前往彩灯房,B：前往雕塑,C：前往发电塔,D：离开此地')
                    if choose == 'A':
                        act = 2
                    elif choose == 'B':
                        act = 3
                    elif choose == 'C':
                        act = 4
                    elif choose == 'D':
                        act = 5
                if act == 1:
                    output('你找到了一个机器人，他看着你，有点不耐烦地说：“这里是黑客村庄。我们都是黑客，你想聊什么？”')
                    leave = 0
                    while leave == 0:
                        output('你想问:A：村庄B：居民,C：城市,D：塞恩思,E：离开')
                        while choose not in {'A','B','C','D','E'}:
                            output('你想问:A：村庄B：居民,C：城市,D：塞恩思,E：离开')
                        if choose == 'A':
                            output('机器人说：“这座村庄在很早之前就存在了，是城市内的许多精英被放逐的产物……你难道没学过近代史吗？”')
                        elif choose == 'B':
                            output('机器人说：“我说过了我们是黑客，是最早一批黑客的后代。别看我们平时一直在瞎逛，实际上我们内部一直在做你们永远都搞不懂的复杂运算！”')
                        elif choose == 'C':
                            output('机器人说：“城市？我不喜欢那里，又脏又乱又挤，就比特区好一点，况且比特区就是我们黑客投资建的。”')
                        elif choose == 'D':
                            output('机器人说：“你是说SCI吗？他本来就是我们黑客的一份子，不知道造了什么孽被贬去小镇了，不知道他现在混的如何……啥？混成科学家了？这也正常。反正这里比他强的人一抓一大把，只是我们懒得出面处理罢了。”')
                        elif choose == 'E':
                            output('机器人说：“没事了？那就走吧，别再来找我了。”')
                            leave = 1
                            speak = 1
                if act == 2:
                    output('你们来到了彩灯房里，一位机器人殷勤地招待了你们。说：“欢迎来到模拟对战房！请选择你们想进行模拟对战的对象！”')
                    output('他随即点开一个显示屏，上面出现了三个附有文字说明的图片。')
                    go_B = 0
                    while go_B == 0:
                        output('请选择你的对手：\nA：CAR-XXX\nB：FLY-XXX\nC：MCE-XXX\nD：离开\nE：使用100CM币购买补给')
                        while choose not in {'A','B','C','D','E'}:
                            output('请选择你的对手：\nA：CAR-XXX\nB：FLY-XXX\nC：MCE-XXX\nD：离开\nE：使用100CM币购买补给')
                        if choose == 'E':
                            if money < 100:
                                output('余额不足！请充值')
                            else:
                                choose = input('你购买了一块H-饼干！')
                                item.append('H.饼干')
                                fight_item.append('H.饼干')
                                view_status()
                        elif choose == 'D':
                            go_B = 1
                        elif choose == 'C':
                            arm_fight()
                        elif choose == 'B':
                            fly_fight()
                        elif choose == 'A':
                            car_fight()
                        if CM > 33333:
                            CM = 33333
                if act == 3:
                    output('你在雕塑下到处转了转，发现了一个发着闪耀光束的机器，上面写着：\n“升降门调控器，正确操作即可关闭所有升降门！”\“正确的代码为：比特塔信标谜题方程的二进制解”')
                    output('你会：A：输入代码调控,B：离开')
                    while choose not in {'A','B','C'}:
                        output('你会：A：输入代码调控,B：离开')
                    if choose == 'A':
                        output('请输入对应的代码！')
                        if choose == '101001001':
                            tower = 1
                            choose = input('')
                        else:
                            output('你看了看升降门，什么也没有发生')
                    elif choose == 'C':
                        output('你在旁边看了看，发现了一行细小的标语：')
                        output('//////////////FireFox///////////////')
                if act == 4:
                    output('你来到一座发电塔下，这里有一名装修工人，他看到了你，说：“非硅基自主意识体重心距小于五倍波距的接受概率等于0”')
                    output('你没听懂他的话，离开了这里')
                    if cake == 0:
                        choose = input('不过在你离开前，你在发电塔下找到了一块蛋糕！')
                        item.append('黑客三周年限定蛋糕')
                        fight_item.append('黑客三周年限定蛋糕')
                        view_status()
                    cake = 1
                if act == 5:
                    go = 1
            output('你们原路返回，离开黑客村庄，一从墙里走出去，你发现村庄立刻变成了之前的样子，看起来破烂不堪。')
            output('你们的车子依然停在前面，你们上了车，车子向前开动。')
            normal = 1
        if normal == 1:
            output('随着车子向前行驶，你们前方的其它车子越来越多，最后你们停在一座蓝色大平台前，许多汽车堵在这里。')
            output('你们下了车，穿过几乎不动的车流往前走去。当你们走上平台后，你发现前面是一座大桥，城市的轮廓在桥对岸显现出来。')
            output('平台上密密麻麻地布满了机器人，你们不知道该干什么。')
            output('你会：A：向人询问,B：四处走走')
            while choose not in {'A','B'}:
                output('你会：A：向人询问,B：四处走走')
            if choose == 'A':
                output('你找到了一个机器人。机器人对你说：“这座大桥是连接城市与郊区的通道之一，上面有高铁可以载人过去。城市周围一共有十三座这样的大桥，当然，这么多大桥可能还是有点太少了。”')
            if choose == 'B':
                choose = input('你四处走了走，意外在地上找到了100CM币！')
                CM += 100
                view_status()
            output('你们在平台上转悠了一会儿，有个机器人注意到了你们，对你们说：“嗨！你们想去城市吗？车站在你们前面，你们可以免费到那儿取票！”')
            choose = input('你们向前走去，来自“便民服务站37号2.0”的治疗光线笼罩着你，你的HP回满了[HPmax]')
            health = 300
            view_status()
            output('你们向前走去，来到了一座蓝色的大建筑物前面，看上去像一座高塔')
            output('许多机器人聚集在这里，你发现你们前面出现了一个弹窗：\n“点击扫描并取票。”')
            output('你会：A：点击弹窗,B：关闭弹窗')
            while choose not in {'A','B'}:
                output('你会：A：点击弹窗,B：关闭弹窗')
            if choose == 'A':
                output('你点了下弹窗，弹窗突然消失，一道蓝色的力场出现在你周围，这时候一个弹窗出现在你的面前：')
                output('“请前往四楼候车”')
            elif choose == 'B':
                output('你关闭弹窗，弹窗突然向你飘了过来穿过了你，这时候另一个弹窗出现在你的面前：')
                output('“请前往四楼候车”')
                choose = input('你发现你的背包重了一点。（获得【水晶焰-II】）')
                item.append('水晶焰-II')
                fight.item.append('水晶焰-II')
            output('你们来到高塔的下方，一个电梯门出现在你面前，你们进入电梯，你注意到你穿过电梯门时好像有一阵微弱的蓝光照了你一下。')
            output('请选择你所要去的楼层（1-4）')
            while choose not in {'1','2','3','4'}:
                output('请选择你所要去的楼层（1-4）')
            if choose == '1':
                output('不幸的是，你已经在这里了')
            elif choose == '2' or choose == '3':
                output('电梯出现了一阵咔咔的响声，电梯没有动！')
            output('电梯开始上升，你们来到了高塔的四楼。')
        savepoint = 12
    if savepoint == 12:
        save_data()
        output('当你们走出电梯时，你发现你正站在一座像是战舰舰桥的地方，你们的旁边停着一座很短的列车，列车没有窗户，只有蓝色的条状大灯围绕在列车的车身周围，你并没有看到轨道与车轮。')
        output('“这上面几乎没什么人，挺奇怪的。”So说道，“我们快进去吧。”')
        output('你们进入列车，车门随即关闭，列车缓缓开动。')
        output('你们在列车里逛了逛，没看到车里有什么人，甚至连普通的座位都没看到。')
        output('“坏了，有问题，这趟车一定有问题！”So说。')
        output('正当这时，你发现前面有一个人向你走了过来，你发现他就是Tetris小店的那位蓝发售货员！')
        output('“啊？你们也在这里，这难道不是包车吗？”售货员看到了你们惊奇地说。')
        output('“我想问问你，你觉得这么繁忙的车站会接受包车吗？！”So问。')
        output('“啥？包车难道不是很正常的？反正四楼的车都短，载客量也少，有人包车也没问题吧。”售货员说。')
        output('“嗯，可是从这儿到城市，我看也就不到几分钟车程，有包车的必要吗？”So追问道。')
        output('“这估计是个人爱好吧……”售货员说。')
        output('“我开始纳闷了，你们机器人，我猜应该总是追求效益最大化吧，怎么还能允许短途包车这种事？难道……你们机器人的设计已经考虑到……享乐方式了？”So继续质问道。')
        output('售货员顿了顿，突然向你们露出了一阵诡异的笑容。')
        output('“是的，是的，是的，你说的都对！我Tetris就喜欢这种！哈哈！被逼到绝路的感觉了！毕竟这样才能消除一些东西嘛！”')
        output('售货员目露凶光地向你们逼近，So看到他性情大变，本能地向后闪了一下。')
        output('“告诉你们！你们猜对了！我根本就不是想包车！是我把你们引到车站的，是我操控了内部数据把你们调到这里，是我弄坏了电梯按钮，这一切，都是为了把这辆车，变成你们的棺材！”')
        output('售货员手中冒出了蓝色的火焰。')
        output('“塞恩思！你到底想干什么！”So喊道。')
        output('“哼，我不是赛恩思，赛恩思可不会亲自干这行，可惜啊，你们想逃出他的手心，那是根本不可能的！上一个这样做的人……”')
        output('售货员顿了顿，突然一个方块砸到了你面前。')
        output('“已经烂成碎末了！”售货员露出恐怖的笑。')
        fight('Tetris',380,25,30,15,random.randint(400,500),'so',[6,random.randint(2,4),random.randint(3,5)])
        if respawned == 1:
            respawned = 0
            continue
        health = 300
        choose = input('Tetris见状况不妙，随即召唤了一个巨大的方块朝你们砸来，激起一阵烟雾；So拉着你躲到一边。')
        choose = input('就在这时，你瞥见Tetris的腰后侧似乎有个小小的红色凸起，你指了指它示意So')
        choose = input('So看了看那个红色凸起，又发现Tetris马上转过身朝你们这边奔来，赶快跑到一边说：“这是薄弱环节，把它打掉！”（输入5个字母以攻击）')
        tetris_red = 0
        while tetris_red < 2:
            tetris_red = 0
            choose = list(input(f'请输入你的攻击方式！'))
            x = random.randint(1,4)
            a = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            b = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            c = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            d = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            e = chr(ord('A') + x - 1)
            enemy_fight = a+b+c+d+e
            enemy_fighta = [a,b,c,d,e]
            hurt = 0
            hurtB = 0
            chance = 0
            wrong = 0
            while wrong == 0:
                wrong = 1
                if len(choose) != 5:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请输入你的攻击方式！'))
                elif choose[0] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请输入你的攻击方式！'))
                elif choose[1] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请输入你的攻击方式！'))
                elif choose[2] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请输入你的攻击方式！'))
                elif choose[3] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请输入你的攻击方式！'))
                elif choose[4] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请输入你的攻击方式！'))
            while chance < 5:
            #好，我决定换一次注释！
                f = choose.pop()
                g = enemy_fighta.pop()
                if f == 'C' and g == 'D' or f == 'B' and g == 'C' or f == 'A' and g == 'B' or f == 'D' and g == 'A':
                    chance += 1
                    tetris_red += 1
                else:
                    chance += 1
            health -= hurtB
            choose = input(f'Tetris以{enemy_fight}的方式躲避')
            if tetris_red < 2:
                choose = input(f'你们没有打掉红色凸起,这时一发方块落了下来打伤了你[HP-10]')
                health -= 10
            dead_interface()
            if respawned == 1:
                respawned = 0
                continue
        savepoint = 13
    if savepoint == 13:
        save_data()
        output('红色的凸起在你们的进攻下破裂开来，Tetris脸上顿时露出吃惊的神情：“这……那个芯片？！……你们想干什么？！！”')
        output('突然，你发现红色的凸起突然碎裂，Tetris露出了奇怪的表情，手舞足蹈地乱动了好一会儿，然后倒在地上。')
        output('“他死啦？”So说道。')
        output('突然，Tetris从地上直接站了起来，So被吓了一跳。')
        output('“啥？你们是谁？我不是在小店里吗……这……这是哪儿？”Tetris看起来很吃惊。')
        output('“他看起来好像失忆了。”So小声对你说，不过这话显然被Tetris给听见了，他张大嘴看着你们，说道：“不可能！！！我上一秒还在店里呢！！！这是瞬移！！！”')
        output('“什么？！”So吃惊地喊道。')
        output('Tetris呆呆地望着地面，突然发现了一些红色碎屑，他随即捡起碎屑看了一阵。')
        output('“扫描结果：植入芯片，来源：NOT FOUND”')
        output('“植入芯片？”So说道，“没记错的话，我记得你刚才提到了塞恩思是吧……没准这芯片是……”')
        output('“赛恩思？！！”Tetris突然叫起来，“我想起来了！”')
        output('“就在刚才，不对，或许是很久之前了——植入芯片后我的本体就被冻结了——我在小店里，眼前突然出现一道红光，很短的时间，但是确实有点异常，我似乎还听到有人在说话……记不清了，但是提到了三个人的名字，其中一个就是这个赛恩思！”')
        output('“另外两个是谁呢？”So问。')
        output('“这……我不太清楚了……现在又有点能想起来，一个好像叫阿尔法，一个叫贝塔好像，我完全不了解。”Tetris说完后走到一边。')
        output('“他们，难道是赛恩思的同伙吗……”So有点疑惑的说道，“怎么又多两个。”')
        choose = input('你会：A：和So讨论,B：和Tetris讨论')
        while choose not in {'A','B'}:
            choose = input('你会：A：和So讨论,B：和Tetris讨论')
        if choose == 'A':
            choose = input('So没有回答，只是在自言自语道：“阿尔法、贝塔，听起来像某种编号，可能不是个人名。”')
        elif choose == 'B':
            choose = input('Tetris说：“唔，小妹妹，城市马上就到了，你想吃点啥？”')
            choose = input('你会选择：A：辣椒,B：大蒜,C：胡椒粉')
            while choose not in {'A','B','C'}:
                choose = input('你会选择：A：辣椒,B：大蒜,C：胡椒粉')
            choose = input('Tetris笑着说：“这些东西都很常见的！待会就去！”')
        output('你们在列车里待了好一段时间，突然，你听见了车门打开的声音，而完全没有感到车已经停了下来。')
        output('“啊这！这是到城市了！我们下车吧”Tetris说。')
        output('你们走出列车，发现这里是另一座车站，你们的四周跳动着蓝色的星点光芒，脚下的玻璃地板上扭动着像蛇一样的光道。')
        output('一条光道窜到你们脚下，你们面前出现了一个显示屏，上面写着：“请旅客前往E区”')
        output('“跟我来，我带你们出去。”Tetris对你们说。你们很快跟着他从一个像管道一样的出口滑出了车站。')
        output('当你们出来时，你发现外面一片热闹景象：形形色色的机器人与车子穿行在暗蓝色的楼房之间，都市的上空被巨大的蓝色光带笼罩，你花了好长时间才看清那光带是数不清的巨大显示屏。')
        output('“这里是E区，城市里出名的商业区之一，我现在得前往市场了，你们就在这儿转转吧。”Tetris说完，伸手在一个弹出的显示屏上点了几下，一辆飞车顿时赶了过来，Tetris直接上车，随着车飞走了')
        output('你们站在一群巨大建筑物的底下不知所措。')
        output('你会：A：随便走走,B：找点东西')
        while choose not in {'A','B'}:
            output('你会：A：随便走走,B：找点东西')
        if choose == 'A':
            output('你四处逛了逛，来到一条车道前')
        elif choose == 'B':
            choose = input('你在一条车道前找到了一张小卡片（获得【占位卡】）')
            item.append('占位卡')
            view_status()
        choose = input('你前面的车道上布满了飞速行驶的车辆，虽然车辆的密度极高，但它们像晶体管里面的一个个分子一样，在混乱中行进着，似乎永远不可能碰撞。')
        choose = input('“我们该怎么过去呢？”So说道。')
        if tower == 0:
            choose = input('So话音刚落，你们前面出现了一条蓝色的巨大条带，上面似乎有液体朝一个方向均匀地流动着，随之出现的还有你们熟悉的东西：蓝紫色的升降门在条带上起伏着。')
            choose = input('降门在条带上起伏着。“咋又是这玩意儿……”So有些烦。“不过还好，由于是力场，通过只会减速，大概只需要通过五分之三的门就可以了吧。”')
            go = 0
            mark = 0
            while go == 0:
                code = []
                for i in range(5):
                    code.append(chr(ord('0')+random.randint(0,1))+chr(ord('0')+random.randint(0,1))+chr(ord('0')+random.randint(0,1))+chr(ord('0')+random.randint(0,1))+chr(ord('0')+random.randint(0,1)))

                for i in range(1):
                    choose = input('请输入五个二进制的数字')
                    wrong = 0
                    while wrong == 0:
                        wrong = 1
                        if len(choose) != 5:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = input('请输入五个二进制的数字')
                        elif choose[0] not in {'0','1'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = input('请输入五个二进制的数字')
                        elif choose[1] not in {'0','1'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = input('请输入五个二进制的数字')
                        elif choose[2] not in {'0','1'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = input('请输入五个二进制数字')
                        elif choose[3] not in {'0','1'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = input('请输入五个二进制的数字')
                        elif choose[4] not in {'0','1'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = input('请输入五个二进制的数字')
                    input('升降门密码是'+code[i-1])
                    answer = code[i-1]
                    compare = 0
                    while compare < 5:
                        if answer[compare] == choose[compare]:
                            mark += 1
                        compare += 1
                    if choose == code[i-1]:
                        input(f'你通过了{mark}道升降门')
                        go = 1
                    if mark >= 3:
                        input('你通过了升降门阵！')
                        go = 1
                    if mark < 3:
                        mark = 0
                        input('你未能通过升降门阵！')
        if tower == 1:
            choose = input('So话音刚落，你们面前出现了一条蓝色的巨大条带，上面似乎有液体朝一个方向均匀地流动着')
            choose = input('“看来是步行道，我们一起过去吧。”So说。')
        choose = input('你们通过车道，前方似乎是一条商业街，许多看起来很高级的店铺排列在道路的两侧。')
        choose = input('你会选择哪家店铺？A：服装店,B：首饰店,C：餐饮店,D：不选择')
        while choose not in {'A','B','C','D'}:
            choose = input('你会选择哪家店铺？A：服装店,B：首饰店,C：餐饮店,D：不选择')
        if choose == 'A':
            choose = input('你找到一家服装店，购买【顶级晚会礼服】吗？只需444444CMB！')
            choose = input('你显然没这么多钱，省点时间无需选择')
        elif choose == 'B':
            choose = input('你找到一家首饰店，购买【亚历山大变色石】吗？只需77777CMB！')
            choose = input('你显然没这么多钱，省点时间无需选择')
            if '水晶焰-II' in item:
                choose = input('在你离开店铺的时候，你发现自己的背包重了一点，你发现你的水晶焰突然不见了，取而代之的是一个发着蓝光的宝石！')
                item.append('战争宝石')
                item.remove('水晶焰-II')
                fight_item.remove('水晶焰-II')
        elif choose == 'C':
            choose = input('请选择你要点的食物：A：辣椒,B：大蒜,C：胡椒粉')
            while choose not in {'A','B','C'}:
                choose = input('请选择你要点的食物：A：辣椒,B：大蒜,C：胡椒粉')
            choose = input('你收获了一袋像雪一样的棉絮')
            E_cotton += 1
        choose = input('你们通过了这条商业街，街道的尽头是一座巨大的雕像，许多机器人在雕像前围观。')
        choose = input('你会：A：看看雕像,B：与机器人交谈,C：即兴表演一番')
        while choose not in {'A','B','C'}:
            choose = input('你会：A：看看雕像,B：与机器人交谈,C：即兴表演一番')
        if choose == 'A':
            choose = input('你看着雕像，上面的图案太过于抽象了，你不是很懂这方面的艺术')
        elif choose == 'B':
            choose = input('机器人说：“这玩意叫做捕蛇圈，是用来抓电子蛇的，我们的先人用捕蛇技术创造了辉煌的农业文明，在E区还有电子蛇农场的遗存……当然它更像是宠物。”')
        elif choose == 'C':
            choose = input('你大庭广众之下做了个后空翻，没人理你【你 傻 了】')
        choose = input('你们离开雕像继续往前走，前面是一座天桥，正当你们想通过时，桥下突然窜出两条奇形怪状的，由方块组成的蛇挡住了你们的去路。')
        choose = input('“这是……电子蛇？”So有点疑惑地说')
        choose = input('一个路过的机器人看到了，说：“啊，不必紧张，电子蛇在这一带很常见，跟他们打一场不就行了。”')
        choose = input('“啊这，奇怪的城市治安。”So说。')
        fight('电子蛇A',277,27,27,27,random.randint(27,227),'so',[0],2,'电子蛇B',277,27,27,27)
        if respawned == 1:
            respawned = 0
            continue
        choose = input('你们击败了电子蛇，电子蛇“嘶嘶”地逃走了。')
        choose = input('你们继续前进前往天桥，桥上又出现许多升降门，你不禁感觉有点烦。')
        what_happen = random.randint(1,3)
        go = 0
        mark = 0
        while go == 0:
            code = []
            if what_happen == 2:
                code.append('11111')
            else:
                for i in range(5):
                    code.append(chr(ord('0')+random.randint(0,1))+chr(ord('0')+random.randint(0,1))+chr(ord('0')+random.randint(0,1))+chr(ord('0')+random.randint(0,1))+chr(ord('0')+random.randint(0,1)))
            for i in range(1):
                choose = input('请输入五个二进制的数字')
                wrong = 0
                while wrong == 0:
                    wrong = 1
                    if len(choose) != 5:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = input('请输入五个二进制的数字')
                    elif choose[0] not in {'0','1'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = input('请输入五个二进制的数字')
                    elif choose[1] not in {'0','1'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = input('请输入五个二进制的数字')
                    elif choose[2] not in {'0','1'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = input('请输入五个二进制数字')
                    elif choose[3] not in {'0','1'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = input('请输入五个二进制的数字')
                    elif choose[4] not in {'0','1'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = input('请输入五个二进制的数字')
                input('升降门密码是'+code[i-1])
                answer = code[i-1]
                compare = 0
                while compare < 5:
                    if answer[compare] == choose[compare]:
                        mark += 1
                    compare += 1
                if choose == code[i-1]:
                    input(f'你通过了{mark}道升降门')
                    go = 1
                if mark >= 3:
                    input('你通过了升降门阵！')
                if mark < 3:
                    mark = 0
                    input('你未能通过升降门阵！')
        output('正当你们准备从天桥上下来的时候，你听见So发出一声惊呼，急忙跑向下面的人行道。')
        output('你跟着So走下人行道，发现昵称正站在道路中央！')
        output('So急忙向昵称跑去，昵称随之往后退了一步，动作似乎不太自然。')
        output('随着So的接近，你看见昵称从地上直接飘了起来，往身后的小巷飞去。')
        output('你和So跟着昵称跑进身后的小巷，昵称突然飞到了小巷的上空飘走了。')
        output('“可恶！中计了！”So气恼道，准备往回走，一道力场门早已在小巷的入口出现，封死了你们的道路。')
        output('你会：A：看看力场门,B：找点东西,C：往小巷深处走')
        while choose not in {'A','B','C'}:
            output('你会：A：看看力场门,B：找点东西,C：往小巷深处走')
        if choose == 'A':
            output('你走到力场门前，力场门发出了低沉的嗡嗡声，一条蓝色的透明电子蛇的图案在门上显示出来')
        elif choose == 'B':
            output('你在周围找到了许多棉絮（获得【电棉】x4）')
            E_cotton += 4
        output('你们往小巷深处走去，这里没有一个人，虽然光线没有变暗，但四周的噪音逐渐减小了，你感到有点冷清。')
        output('在小巷的深处，你们面前出现了一条十字路口，一个显示屏出现在你们面前：\n“向左：小卖铺\n向前：商业中心\n向右：电玩世界”')
        go = 0
        why = 0
        while go == 0:
            if why == 0:
                choose = input('你会：A：向左走,B：向前走,C：向右走')
                while choose not in {'A','B','C'}:
                    choose = input('你会：A：向左走,B：向前走,C：向右走')
            if why == 1:
                choose = input('你会：A：向前走,B：向右走')
                while choose not in {'A','B'}:
                    choose = input('你会：A：向左走,B：向前走,C：向右走')
            if choose == 'A' and why == 0:
                choose = input('你们向左走去，发现一个自助售卖机孤零零地站在墙角，看起来已经坏了')
                choose = input('想试试购买吗：A：是,B：否')
                while choose not in {'A','B'}:
                    choose = input('想试试购买吗：A：是,B：否')
                if choose == 'A':
                    choose = input('自助售卖机吐出了一堆棉絮（获得【电棉】x2）')
                    E_cotton += 2
                output('你们不想再来这里了')
                why = 1
            if (choose == 'B' and why == 0) or (choose == 'A' and why == 1):
                output('你们走了一会儿，面前出现了好几座大厦，不过你们似乎没有看到入口。')
            if (choose == 'C' and why == 0) or (choose == 'B' and why == 1):
                output('你们朝右走去')
                go = 1
        output('过了一会儿，你们的前方出现了一片空旷的地带，昵称就站在这中间。')
        output('“你怎么啦，昵称？”So关切地问道，“有没有什么事？”')
        output('昵称有点胆怯地回答：“我……没事，可是他们……”')
        output('话音未落，你们面前的墙上突然开了几个洞，几条电子蛇从洞里钻了出来，昵称吓得闪在一边。')
        output('“不会吧……又来！”So大声说，“别怕，昵称，躲到我后面，我们来解决这些东西！”')
        output('电子蛇看到了你们，却并没有向你们冲过来，而是包围在你们周围，组成一座庞大的迷宫。')
        output('“呃呃……我们被困住了，不是吗……”昵称小声说道。')
        output('“既然这样，我们只能”So皱了皱眉，接着说道：“只能冲出去了！”')
        savepoint = 14
    if savepoint == 14:
        save_data()
        print('【战斗开始】')
        t.sleep(0.5)
        output('So对你说：“我们要绕过这些蛇的包围，但不能撞上他们，不然我们会受伤的……你应该听说过赛车棋吧……”')
        output('A：听说过,B：没有')
        while choose not in {'A','B'}:
            output('A：听说过,B：没有')
        if choose == 'A':
            output('So回答：“那就好，这东西和赛车棋操作差不多，我们开始吧。”')
        elif choose == 'B':
            output('So说：“这样啊，那我来介绍一下，我知道这个东西。我们在魔法界面会增加一些【步数项】，通过它，我们可以选择我们每个人走的步数，走到25步就到终点，可以出去了。')
            output('当然，这种时候每走一步，电子蛇就会出来攻击我们，我们会受到伤害！而且每走几步，电子蛇就会组成很多花样来攻击我们！')
            output('你问我怎么知道的？当然是网上查的啊……”')
            #看这段空白，多适合写一段赛车棋啊，棉花糖帮帮我（
            #（
        sweater = 0
        snake_A = 0
        cat = 0
        magic_point = 0
        hucker = 0
        win = 0
        compete_A,compete_B,compete_C = 0,0,0
        a,b,c,d,e = '','','','',''
        while win == 0:
            magic_choose = 0
            att_choose = 0
            item_choose = 0
            snake_A += 1
            snake_A = str(snake_A)
            if snake_A in {'5','15','20','25','27','28','29','30'}:
                snake_A = int(snake_A)
                input('电子蛇聚成了庞大的立体形状阻拦你！你必须击破它们才能前进！')
                hucker = 0
                big_fight = 0
                t.sleep(0.5)
                car_A = 277
                check = 0
                miaomiao = 0
                coat = 0
                win_B = 0
                a,b,c,d,e = '','','','',''
                while win_B == 0:
                    magic_choose = 0
                    att_choose = 0
                    item_choose = 0
                    while magic_choose == 0 and item_choose == 0:
                        if car_A <= 0:
                            car_A = 0
                        chooseb = 'A'
                        if '战争宝石' in item:
                            print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health},阻拦电子蛇血量为{car_A},攻击力为27，防御力5，防御率10%暴击数{big_fight},')
                        if '战争宝石' not in item:
                            print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health},阻拦电子蛇血量为{car_A}')
                        choose = input('A,物品B,防御C,魔法D,跳过')
                        while choose not in {'A','B','C','D'}:
                            print('请做出你的选择')
                            choose = input('A,物品B,防御C,魔法D,跳过')
                        if choose == 'A':
                            choose = input(f'你现在可使用的物品有{fight_item},请从1开始输入序号以选择使用的物品')
                            if choose not in {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'}:
                                choose = input('物品序号输入错误!')
                            else:
                                choose = int(choose)
                                if choose > len(fight_item):
                                    choose = input('物品序号输入错误!')
                                else:
                                    choose -= 1
                                    check = fight_item[choose]
                                    item_find()
                                    if check == '魔法炸药':
                                        choose = input('你对对方造成了100点伤害!但你也不小心受到了30点伤害')
                                        health -= 30
                                        cube -= 100
                                        dead_interface()
                                        if respawned == 1:
                                            break
                                    if check == '坚硬冰棍':
                                        choose = input('你使用了坚硬冰棍!敌方的HP降低了100点!')
                                        cube -= 100
                                    if check in fight_item and check in item:
                                        item.remove(check)
                                        fight_item.remove(check)
                                if health > 300:
                                    health = 300
                        elif choose == 'B':
                            choose = input('你选择了防御!')
                            magic_point += 40
                            magic_choose = 1
                            if magic_point >= 100:
                                magic_point = 100
                            chooseb = 'B'
                        elif choose == 'C':
                            choose = input(f'A：治疗魔法（{health_point}）B：战斗魔法（70）C：黑暗魔法（？）D：暗蓝卫衣（30-50）E：猫叫芯片（40）')
                            while choose not in {'A','B','C','D'}:
                                print('请做出你的选择')
                                choose = input(f'A：治疗魔法（{health_point}）B：战斗魔法（70）C：黑暗魔法（？）D：暗蓝卫衣（30-50）E：猫叫芯片（40）')
                            else:
                                if choose == 'A':
                                    if magic_point < health_point:
                                        choose = input('你的魔法值不够!')
                                        magic_choose = 0
                                    if magic_point >= health_point:
                                        choose = input(f'你使用了治疗法术!你的血量回复了{health_plus}点!')
                                        health += health_plus
                                        magic_choose = 1
                                        magic_point -= 30
                                    if health > 300:
                                        health = 300
                                        magic_choose = 1
                                elif choose == 'B':
                                    if magic_point < 70:
                                        choose = input('你的魔法值不够!')
                                        magic_choose = 0
                                    if magic_point >= 70:
                                        choose = input('你使用了战斗法术!你的攻击提高了5点,持续一回合!')
                                        att_choose = 1
                                        magic_choose = 1
                                        magic_point -= 70
                                elif choose == 'C':
                                    choose = input('l͓̩̫̘͙͔̯͖̟̤̓͊̑̌́̂̆̚ò̥̪̭̱̰̝̒͂̄͋̿̏͆́̚c͍̲͇͚̖̬͈̪͙̳͌̉́̃k̪̥̱̝̱̑̈́̏̽͗̊̈́͂̀̍e̞͎̩̜̱̩͚̤̊͌̀̀d̠̖̞̝̙̪̟̞̐͛̈̊̀͂̄͌̓̏͌̓ͅ')
                                    magic_choose = 0
                                elif choose == 'D':
                                    if magic_point < 50:
                                        choose = input('你的魔法值不够!')
                                    elif magic_point >= 50:
                                        magic_point -= random.randint(30,50)
                                        coat = 1
                                        magic_choose = 1
                                        choose = input('你使用了暗蓝卫衣!你的闪避率提高了10％,持续一回合!')
                                elif choose == 'E':
                                    if magic_point < 40:
                                        choose = input('你的魔法值不够!')
                                        magic_choose = 0
                                    if magic_point >= 40:
                                        choose = input('你使用了猫叫芯片!电子蛇发出了喵喵叫的声音!')
                                        magic_choose = 1
                                        magic_point -= 40
                                        miaomiao = 1
                                        if random.randint(1,5) == 3:
                                            print('喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵（')
                                else:
                                    magic_choose == 1
                                choose = 0
                        elif choose == 'D':
                            choose = input('你跳过了你的回合')
                            magic_choose = 1
                    car_act_B = random.randint(1,6)
                    if '混乱护盾' in armor:
                        health += random.randint(3,20)
                        if health >= 300:
                            health = 300
                    if car_act_B == 1:
                        input('电子蛇绕成一圈，你们不知道在玩什么花样')
                    if car_act_B == 2:
                        input('电子蛇发出来特有的嘶嘶声')
                    if car_act_B == 3:
                        input('你们闻到一股棉花味')
                    if car_act_B == 4:
                        input('电子蛇希望你们能养它们')
                    if car_act_B == 5:
                        input('电子蛇有点想逃走')
                    if car_act_B == 6:
                        input('电子蛇不希望看到捕蛇圈')
                    if car_A > 0:
                        x = random.randint(1,4)
                        a = chr(ord('A') + x - 1)
                        x = random.randint(1,4)
                        b = chr(ord('A') + x - 1)
                        x = random.randint(1,4)
                        c = chr(ord('A') + x - 1)
                        x = random.randint(1,4)
                        d = chr(ord('A') + x - 1)
                        x = random.randint(1,4)
                        e = chr(ord('A') + x - 1)
                        enemy_fight = a+b+c+d+e
                        enemy_fighta = [a,b,c,d,e]
                        zero_att = 0
                        if '零剑' in weapon:
                            zero_att = random.randint(5,50)
                        choose = list(input(f'请选择你对阻拦电子蛇的攻击!(5个一组,由五个大写字母构成)'))
                        hurt = 0
                        hurtB = 0
                        chance = 0
                        wrong = 0
                        while wrong == 0:
                            wrong = 1
                            if len(choose) != 5:
                                wrong = 0
                                print('输入错误,请依照格式输入!')
                                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                            elif choose[0] not in {'A','B','C','D'}:
                                wrong = 0
                                print('输入错误,请依照格式输入!')
                                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                            elif choose[1] not in {'A','B','C','D'}:
                                wrong = 0
                                print('输入错误,请依照格式输入!')
                                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                            elif choose[2] not in {'A','B','C','D'}:
                                wrong = 0
                                print('输入错误,请依照格式输入!')
                                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                            elif choose[3] not in {'A','B','C','D'}:
                                wrong = 0
                                print('输入错误,请依照格式输入!')
                                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                            elif choose[4] not in {'A','B','C','D'}:
                                wrong = 0
                                print('输入错误,请依照格式输入!')
                                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        else:
                            war = random.randint(1,20)
                            cube_act = random.randint(1,10)
                            while chance < 5:
                                f = choose.pop()
                                g = enemy_fighta.pop()
                                if chooseb != 'B':
                                    if (f == 'A' and g == 'B') or (f == 'B' and g == 'C') or (f == 'C' and g == 'D') or (f == 'D' and g == 'A'):
                                        hurt += att
                                        chance += 1
                                        if att_choose == 1:
                                            hurt += 5
                                            if '战争宝石' in item and war <= 3:
                                                hurt += 2 * att + 2 * item_att + 2 * zero_att
                                        if cube_act > 9:
                                            hurt -= 5
                                        hurt += item_att
                                        hurt += zero_att
                                        if hucker == 1:
                                            hurt += 10
                                        if '电磁激光枪' in weapon and magic_point >= 10:
                                            hurt += 35
                                if (f == 'D' and g == 'C') or (f == 'C' and g == 'B') or (f == 'B' and g == 'A') or (f == 'A' and g == 'D'):
                                    hurtB += 27
                                    if miaomiao == 1:
                                        hurtB //= 2
                                    if chooseb == 'B':
                                        hurtB -= Def
                                        if hucker == 1:
                                            hurtB -= 30
                                        if hurtB < 0:
                                            hurtB = 0
                                    chance += 1
                                    if coat == 1 and random.randint(1,10) == 5:
                                        hurtB = 0
                                    else:
                                        health += 10
                                else:
                                    chance += 1
                            if random.randint(1,20) == 3 and '战争宝石' in item and att_choose == 1:
                                hurt *= 3
                            if hide[0] + hide[1] >= random.randint(1,100):
                                hurtB = 0
                            hide[1] = 0
                            health -= hurtB
                            item_att = 0
                            choose = input(f'阻拦电子蛇的攻击是{enemy_fight}')
                            if cube_act > 9 :
                                choose = input('阻拦电子蛇使用了防御!')
                            if chooseb != 'B':
                                choose = input(f'你对阻拦电子蛇造成了{hurt}点伤害!')
                                car_A -= hurt
                                hurt = 0
                            if chooseb == 'B':
                                choose = input('因为你选择了防御,所以伤害不计入')
                            choose = input(f'你被敌人扣除了{hurtB}点血')
                            dead_interface()
                            if respawned == 1:
                                break
                    coat = 0
                    miaomiao = 0
                    if car_A <= 0:
                        choose = input('你击退了阻拦电子蛇!')
                        if len(item) < 15 and random.randint(1,2) == 2:
                            plus = random.choice(['能量饮料'],['冰冻面包'],['电路板寿司'],['H-饼干'])
                            input(f'阻拦电子蛇留下了一个{plus},你将其拾到了背包')
                            item.append(plus)
                            fight_item.append(plus)
                        E_cotton += 1
                        win_B = 1
                        magic_choose = 0
                        item_choose = 0
            snake_A = int(snake_A)
            win_B = 0
            while magic_choose == 0 and item_choose == 0:
                chooseb = 'A'
                print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health},你已经走了{compete_B}/25步')
                choose = input('A,物品B,防御C,魔法D,跳过')
                while choose not in {'A','B','C','D'}:
                    print('请做出你的选择')
                    choose = input('A,物品B,防御C,魔法D,跳过')
                if choose == 'A':
                    choose = input(f'你现在可使用的物品有{fight_item},请从1开始输入序号以选择使用的物品')
                    if choose not in {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'}:
                        choose = input('物品序号输入错误!')
                    else:
                        choose = int(choose)
                        if choose > len(fight_item):
                            choose = input('物品序号输入错误!')
                        else:
                            choose -= 1
                            check = fight_item[choose]
                            item_find()
                            if check == '魔法炸药':
                                choose = input('你对对方造成了100点伤害!但你也不小心受到了30点伤害')
                                health -= 30
                                cube -= 100
                                dead_interface()
                                if respawned == 1:
                                    break
                            if check == '坚硬冰棍':
                                choose = input('你使用了坚硬冰棍!敌方的HP降低了100点!')
                                cube -= 100
                            if check in fight_item and check in item:
                                item.remove(check)
                                fight_item.remove(check)
                        if health > 300:
                            health = 300
                if choose == 'B':
                    choose = input('你选择了防御!')
                    magic_point += 40
                    magic_choose = 1
                    if magic_point >= 100:
                        magic_point = 100
                    chooseb = 'B'
                if choose == 'C':
                    choose = input(f'A：走一步（10）B：走两步（20）C：走三步（30）D：猫叫芯片（40）E:暗蓝卫衣（30-50）F：治疗魔法（{health_point}）G：战斗魔法（70）')
                    while choose not in {'A','B','C','D','E'}:
                        print('请做出你的选择')
                        choose = input(f'A：走一步（10）B：走两步（20）C：走三步（30）D：猫叫芯片（40）E:暗蓝卫衣（30-50）F：治疗魔法（{health_point}）G：战斗魔法（70）')
                    else:
                        if choose == 'A':
                            if magic_point < 10:
                                choose = input('你的魔法值不够!')
                                magic_choose = 0
                            if magic_point >= 10:
                                choose = input(f'你尝试向前移动一小步')
                                compete_A = 1
                                magic_choose = 1
                                magic_point -= 10
                        if choose == 'B':
                            if magic_point < 20:
                                choose = input('你的魔法值不够!')
                                magic_choose = 0
                            if magic_point >= 20:
                                choose = input('你使用了魔法为你的鞋子充能！你的速度变快了！')
                                compete_A = 2
                                att_choose = 1
                                magic_choose = 1
                                magic_point -= 20
                        if choose == 'C':
                            if magic_point < 30:
                                choose = input('你的魔法值不够!')
                                magic_choose = 0
                            if magic_point >= 30:
                                choose = input('你施展了一次速度魔法！你的移动速度大幅提升！')
                                compete_A = 3
                                magic_choose = 1
                                magic_point -= 30
                        if choose == 'D':
                            if magic_point < 40:
                                choose = input('你的魔法值不够!')
                                magic_choose = 0
                            if magic_point >= 40:
                                choose = input('你使用了猫叫芯片!电子蛇发出了喵喵叫的声音!')
                                magic_choose = 1
                                magic_point -= 40
                                cat = 1
                                if random.randint(1,5) == 3:
                                    print('喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵（')
                        if choose == 'E':
                            if magic_point < 50:
                                choose = input('你的魔法值不够!')
                                magic_choose = 0
                            if magic_point >= 50:
                                choose = input('你使用了暗蓝卫衣！你的闪避率提高了10％！')
                                magic_choose = 1
                                magic_point -= random.randint(30,50)
                                sweater = 1
                        if choose == 'F':
                            if magic_point < health_point:
                                choose = input('你的魔法值不够!')
                                magic_choose = 0
                            if magic_point >= health_point:
                                choose = input(f'你使用了治疗法术!你的血量回复了{health_plus}点!')
                                health += health_plus
                                magic_choose = 1
                                magic_point -= 30
                            if health > 300:
                                health = 300
                                magic_choose = 1
                        if choose == 'G':
                            if magic_point < 70:
                                choose = input('你的魔法值不够!')
                                magic_choose = 0
                            if magic_point >= 70:
                                choose = input('你使用了战斗法术!你的攻击提高了5点,持续一回合!')
                                att_choose = 1
                                magic_choose = 1
                                magic_point -= 70
                        choose = 0
                if choose == 'D':
                    choose = input('你跳过了你的回合')
                    magic_choose = 1
            if compete_A == 0 and random.randint(1,5) <= 3:
                E_cotton += random.randint(1,4)
            x = random.randint(1,4)
            a = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            b = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            c = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            d = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            e = chr(ord('A') + x - 1)
            enemy_fight = a+b+c+d+e
            enemy_fighta = [a,b,c,d,e]
            zero_att = 0
            if '零剑' in weapon:
                zero_att = random.randint(5,50)
            car_act_B = random.randint(1,7)
            if '混乱护盾' in armor:
                health += random.randint(3,20)
                if health >= 300:
                    health = 300
            if car_act_B == 1:
                input('电子蛇绕成一圈，你们不知道在玩什么花样')
            if car_act_B == 2:
                input('电子蛇发出来特有的嘶嘶声')
            if car_act_B == 3:
                input('你们闻到一股棉花味')
            if car_act_B == 4:
                input('电子蛇希望你们能养它们')
            if car_act_B == 5:
                input('电子蛇有点想逃走')
            if car_act_B == 6:
                input('电子蛇不希望看到捕蛇圈')
            if car_act_B == 7:
                input('仿佛来到了电子蛇窝')
            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
            hurt = 0
            hurtB = 0
            chance = 0
            wrong = 0
            while wrong == 0:
                wrong = 1
                if len(choose) != 5:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                elif choose[0] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                elif choose[1] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                elif choose[2] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                elif choose[3] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                elif choose[4] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
            else:
                hurtB_E = 0
                while chance < 5:
                    f = choose.pop()
                    g = enemy_fighta.pop()
                    if chooseb != 'B':
                        if (f == 'A' and g == 'B') or (f == 'B' and g == 'C') or (f == 'C' and g == 'D') or (f == 'D' and g == 'A'):
                            hurt += 1
                            chance += 1
                    if (f == 'D' and g == 'C') or (f == 'C' and g == 'B') or (f == 'B' and g == 'A') or (f == 'A' and g == 'D'):
                        hurtB_E += 1
                        hurtB += 27
                        if check == '冰冻面包':
                            hurtB = 0
                            check = ''
                        if chooseb == 'B':
                            hurtB -= Def
                            if Def >= 27:
                                hurtB = 0
                        if cat == 1:
                            hurtB /= 2
                        if hurtB <= 0:
                            hurtB = 0
                        chance += 1
                        if sweater == 1:
                            hurtB = 0
                        else:
                            health += 10
                    else:
                        chance += 1
                if hide[0] + hide[1] >= random.randint(1,100):
                    hurtB = 0
                hide[1] = 0
                cat = 0
                sweater = 0
                #论coat和sweater的区别（
                health -= hurtB
                item_att = 0
                choose = input(f'敌方的攻击是{enemy_fight}')
                choose = input(f'你被电子蛇扣除了{hurtB}点血')
                dead_interface()
                if respawned == 1:
                    break
                if hurt > hurtB_E and compete_A != 0:
                    choose = input(f'你行走了{compete_A}步！')
                    compete_B += compete_A
                if hurt <= hurtB_E and compete_A != 0:
                    choose = input('你前进时被电子蛇击退了！你只得留在原地')
                hurtB = 0
                att_choose = 0
                compete_A = 0
            if compete_B >= 25:
                choose = input('你通过了电子迷宫！')
                CM_get = random.randint(27,227)
                CM += CM_get
                choose = input(f'你获得了{CM_get}个CM币，还有一坨雪白的棉花')
                E_cotton += 1
                hucker = 0
                savepoint = 15
                win = 1
        if respawned == 1:
            respawned = 0
            continue
    if savepoint == 15:
        #搞完了！（bug送给棉花糖）
        save_data()
        what = 0
        choose = input('你们冲出电子蛇组成的迷宫，往小巷的前方跑去，前面出现了一道道激光组成的迷阵。')
        choose = input('“这……这些是赛恩思布置的，但我不知道他为什么要这样……”昵称说。')
        choose = input('“还不是为了抓我们……不过就不怕我们被这些机关杀死吗……”So说道。')
        choose = input('你看着激光，发现它们分为红蓝两种，由一个巨大的发射器向四周放射出来。')
        choose = input('“赛恩思说这是‘电磁激光阵’，听说没什么危险。”昵称说')
        choose = input('“电磁激光阵？什么伪科学……”So有点轻蔑地说。')
        choose = input('你会：A：看看发射器,B：穿过激光阵,C：在四周看看')
        while choose not in {'A','B','C'}:
            choose = input('你会：A：看看发射器,B：穿过激光阵,C：在四周看看')
        if choose == 'A':
            choose = input('你看着发射器，你几乎无法理解发射器的结构')
            choose = input('突然，发射器冒出一阵蓝光，吓了你一跳。')
            if '电磁激光枪' not in item and weapon != '电磁激光枪':
                choose = input('一道蓝色的光线击中了你，你闪到一边[HP-50]')
                health -= 50
                dead_interface()
            else:
                choose = input('一道蓝色的光线从天而降，你的背包随即发出了一道红光，两道光相遇后消失在空中。')
                choose = input('“电磁激光枪！它救了我们……这也是魔法啊”昵称喃喃自语。')
        elif choose == 'B':
            choose = input('你试图穿过激光阵，然而你一靠近激光，激光就被“吸”到了你身上，击中了你[HP-70]')
            health -= 70
            dead_interface()
            choose = input('“看起来一定是魔法！”So说。')
        elif choose == 'C':
            what = 1
            choose = input('在四周的墙壁上发现了一个红色的按钮与一个蓝色的按钮。')
            choose = input('你会：A：按红色,B：按蓝色,C：两个都按')
            while choose not in {'A','B','C'}:
                choose = input('你会：A：按红色,B：按蓝色,C：两个都按')
            if choose == 'A':
                choose = input('你按下红色按钮，突然，你被一道激光击中了[HP-50]，你发现所有红色的激光都消失了')
                health -= 50
                dead_interface()
            elif choose == 'B':
                choose = input('你按下蓝色按钮，突然，你被一道激光击中了[HP-50]，你发现所有蓝色的激光都消失了')
                health -= 50
                dead_interface()
            elif choose == 'C':
                choose = input('你按了两个按钮，你被激光击中了两次[HP-100]，所有激光都消失了')
                health -= 100
                dead_interface()
        choose = input('So说：“啥？你怎么不请我来？”')
        if what == 0:
            choose = input('So看到前面的墙壁上有两个按钮，随即用卫衣按下按钮，所有的激光都消失了。')
            choose = input('“我们走吧”So说。')
            choose = input('你们快速通过这里')
        else:
            choose = input('激光消失后，你们快速通过这里。')
        choose = input('你们向前走去，随着你们的前进，你发现小巷开始变宽，直到一条人来人往的街道出现在你们面前。')
        choose = input('“我们到了。”So说，“所以，我亲爱的昵称……我们一起向前走吧！”')
        choose = input('“等等，我好像，有点……”昵称支支吾吾地说道')
        choose = input('突然，你发现昵称的身边出现了一个红色的光球，没等So反应过来，光球迅速扩大，把昵称包了进去。光球随即消失了，而昵称开始往天上飞去。')
        choose = input('“昵称你！！！！”So大叫道，脱下卫衣往天上够，可惜并没有够到。你们眼睁睁地看着昵称往天上越烦越远，直到从你们视野里消失。')
        choose = input('“啊这，我忘了屏蔽笼这东西了……”So懊恼地说道。')
        choose = input('“我们走！Zero！等咱们找到赛恩思，一定把他暴揍一顿！我们走！”So气愤地说')
        choose = input('你会：A：提醒So他找不到赛恩思,B ：提醒So别被赛恩思探测到了')
        while choose not in {'A','B'}:
            choose = input('你会：A：提醒So他找不到赛恩思,B ：提醒So别被赛恩思探测到了')
        if choose == 'A':
            choose = input('So皱了皱眉，说：“对哦，我们去哪里找他呢”')
        elif choose == 'B':
            choose = input('So说：“这倒没事，我们不是机器人，赛恩思侦测不到我们……可是我们去哪找他呢……”')
        choose = input('正当So思索的时候，突然，一个小小的蓝色弹窗在你们面前展开。“到这里来。”')
        choose = input('So看到弹窗，走上去点了点，弹窗上的字幕突然改变了。')
        choose = input('“不要这样，说话就好。”')
        choose = input('“你是谁？”So问。')
        choose = input('“等你们到这里来，我就告诉你们。”')
        choose = input('“到哪里？”So问。')
        choose = input('“我的地址是LC区208路4号，你们可以坐车来。”')
        choose = input('“你要干什么？”So问。')
        choose = input('“我可以帮你们找到赛恩思。”')
        choose = input('“我们怎么相信你……”So有点恼怒。')
        choose = input('“我没有办法让你们相信我，一切都靠你们自己。我只能告诉你们，如果没有我的帮助，你们不可能找到赛恩思。”')
        choose = input('“这……那你是怎么发现我们的？”So问。')
        choose = input('“无法告诉你们太多，我只能跟你说，我一直在监视赛恩思的电子网络，我从一些信息里面发现了你们，我就找上了你们，至于定位系统，这是我自己的研究成果。”')
        choose = input('“你是科学家吗……”So问。')
        choose = input('“等你们过来我就告诉你。”')
        choose = input('“你……你真的不是赛恩思的人吗？这样做不怕被反侦察吗？”So有些抓狂。')
        choose = input('“我可以告诉你，我完全不怕赛恩思，即使被他反侦察，我也没有任何危险。因为我不是个机器人，我和你们一样，也是人！”')
        choose = input('“这……那么你能告诉我们昵称在哪吗？”')
        choose = input('“等你们过来我就告诉你们，虽然我不怕他，但长时间远距离通话也有危险，我下了。”弹窗顿时关闭。')
        choose = input('“我觉得……我不太相信这个人。”So对你说。')
        choose = input('你不怎么想理So。')
        choose = input('你会：A：点头,B：走开')
        while choose not in {'A','B'}:
            choose = input('你会：A：点头,B：走开')
        if choose == 'A':
            choose = input('你点了点头，So说：“不过……再这样下去也不是办法，我们还是去一趟吧。”')
        elif choose == 'B':
            choose = input('你转身走开，周围有个冰淇淋摊，买个冰淇淋吗？A：买,B：不买')
            while choose not in {'A','B'}:
                choose = input('A：买,B：不买')
            if choose == 'A':
                if CM < 20:
                    choose = input('你莫得钱（')
                if CM >= 20:
                    choose = input('你购买了一个冰淇淋！')
                    CM -= 20
                    item.append('冰淇淋')
                    fight_item.append('冰淇淋')
                    view_status()
            elif choose == 'B':
                choose = input('你没有买冰淇淋')
        choose = input('So从你后面跟上来：“那个……我想我们还是去一趟那里吧。”')
        choose = input('So说：“我们可能得叫个车。”')
        choose = input('就在此时，一个很大的弹窗出现在你们面前。')
        choose = input('“叫车热线：2849293816”')
        choose = input('你们有点不知所措，你们前面又出现了一个弹窗')
        go = 0
        choose = input('“请输入热线号码（十位数字）。”')
        while go == 0:
            while choose not in {'12132','2849293816','00000000000000','281738368'}:
                choose = input('请重新输入')
            if choose == '12132':
                choose = input('这里没有混沌')
            elif choose == '2849293816':
                choose = input('叫车成功')
                go = 1
            elif choose == '00000000000000':
                choose = input('地杜鹃小姐杜鹃洗涤设备信息开始')
            elif choose == '281738368':
                choose = input('赛恩思不在线')
        output('你们输入热线号码后不久，一辆飞车来到了你们面前。')
        output('“请上车”一个弹窗在你们面前出现')
        output('你们坐上了车，发现和之前你们坐的那辆车没什么区别，位置很挤不太舒服。')
        output('你们的前方出现了一个弹窗，上面要求输入地址，So把你们要去的地方填上后，车开始朝前面飞去。')
        output('你会：A：看看车上B ：看看外面,C：试图交谈')
        while choose not in {'A','B','C'}:
            choose = input('你会：A：看看车上B ：看看外面,C：试图交谈')
        if choose == 'A':
            output('车上没有司机，你想不清楚这车是怎么开的')
        elif choose == 'B':
            output('你看着外面，无数高楼从你们面前向后退去')
        elif choose == 'C':
            output('没有什么可谈的')
        output('正当你发呆的时候，车上突然传来一个声音：“你们是想去LC区吗？”')
        output('你看了看车上，除了So并没有什么人。')
        output('“哦，我忘了你们是外人……我是这车上的AI。”')
        output('AI继续说道：“我来给你们讲一下这城市吧。这座城市的修建历史很长，但它几乎没什么大事发生，所有区域都保存得很好……”')
        output('你听着AI的讲解，不知不觉就睡着了……')
        output('当你醒来的时候，你发现周围的区域发生了一些变化，由蓝色变成了暗蓝色，周边还有许多不明飞行物在穿行。')
        output('“我们现在所在的D区主要产业仍然是高新技术，以能量核心的开发与设计为主，当然这些飞碟也是他们弄的一些玩意儿，圆盘形的设计符合核心的嵌入……”')
        output('So打断了AI的话：“我插一句，我们现在离目的地有多远？”')
        output('“还剩20分钟吧，我们已经到D区的边沿地带了，LC区就靠在D区边上，当然你们待会儿也可以考虑去P区转转，那里是城市的中心地带，吃的玩的都多。”')
        output('“赛恩思可能躲在那里。”So小声对你说。')
        output('“总之，我们穿过前面那座大厦，我们就离LC区很近了，现在我们就享受剩下的旅程吧。”')
        output('你坐了起来看向外面，许多热闹的街道在你的下方浮现，街道上放射出明亮的闪光，你注意到车的速度似乎在增加。')
        output('突然，你听见AI发出了有点着急的叫声：“等等！我，我转不了弯了，车上好像有哪些部件坏掉了，我检查下……”')
        output('你们看见前方那座大厦向你们越来越近，车在加速撞向大厦！')
        output('“你们快跳下去！车修不了了，撞上大厦后你们都会死的！！！”')
        output('车门顿时打开，从高速行驶的车上往下跳完全是必死无疑。')
        output('你会：A：跳下去,B：在车上找找东西')
        while choose not in {'A','B'}:
            choose = input('你会：A：跳下去,B：在车上找找东西')
        if choose == 'A':
            choose = input('你直接跳了下去，你感到身体突然有点重，一道隐形的力场正在接住你，你安全地落在一条步行道上，So也接着落了下来。')
        elif choose == 'B':
            choose = input('你在车上找东西，没有什么有用的，情急之下你跳了下去，不小心扭伤了脚[HP-5]')
            health -= 5
            dead_interface()
            choose = input('你跳了下去，突然身体突然有点重，一道隐形的力场正在接住你，你安全地落在一条步行道上，So也接着落了下来。')
        choose = input('你抬头看了看天上，那座大厦上出现了一团巨大的火焰，许多飞碟围在大厦边上喷洒着白色烟雾。')
        choose = input('“好险……”So说道。你发现身边许多机器人也朝着那个方向看去，发出议论。')
        choose = input('“可能还是被赛恩思盯上了，总之我们可不能再坐车去那里，走路去估计会安全一些。”')
        choose = input('你们向前走去。')
        choose = input('你们的前面是一座广场，广场上有许多商铺，许多黑色的飞碟在广场上空喷洒着像激光一样的水花。')
        choose = input('你会：A：去商铺,B：去看飞碟')
        while choose not in {'A','B'}:
            choose = input('你会：A：去商铺,B：去看飞碟')
        if choose == 'A':
            choose = input('你来到一座商铺，店员看到你，对你说：“欢迎光临，买点能量晶体吗，只需要1200CMB！”')
            choose = input('你会：A：购买,B：不买')
            while choose not in {'A','B'}:
                choose = input('你会：A：购买,B：不买')
            if choose == 'A':
                if CM < 1200:
                    choose = input('你莫得钱（')
                if CM >= 1200:
                    choose = input('你购买了一个能量晶体！')
                    CM -= 1200
                    item.append('能量晶体')
                    view_status()
            elif choose == 'B':
                choose = input('店员说：“啊这，那么祝您愉快。”')
        elif choose == 'B':
            item.append('能量晶体')
            output('飞碟散发出强烈的光芒，你在光芒内部感到了一阵不轻松。你发现你的背包重了一些（获得【能量晶体】）')
        output('你们走出广场，前方是一条宽大的车道，许多飞碟形状的车在道路上穿行。')
        output('蓝色的力场步行道出现在你们面前')
        if tower == 1:
            choose = input('你们穿过了步行道')
        else:
            choose = input('你们前面又出现了许多升降门')
            go = 0
            mark = 0
            while go == 0:
                code = []
                for i in range(8):
                    code = chr(ord('0')+random.randint(0,1)) + chr(ord('0')+random.randint(0,1)) + chr(ord('0')+random.randint(0,1)) + chr(ord('0')+random.randint(0,1)) + chr(ord('0')+random.randint(0,1)) + chr(ord('0')+random.randint(0,1)) + chr(ord('0')+random.randint(0,1)) + chr(ord('0')+random.randint(0,1))

                for i in range(1):
                    choose = input('请输入八个二进制的数字')
                    wrong = 0
                    while wrong == 0:
                        wrong = 1
                        if len(choose) != 8:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = input('请输入八个二进制的数字')
                        elif choose[0] not in {'0','1'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = input('请输入八个二进制的数字')
                        elif choose[1] not in {'0','1'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = input('请输入八个二进制的数字')
                        elif choose[2] not in {'0','1'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = input('请输入八个二进制数字')
                        elif choose[3] not in {'0','1'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = input('请输入八个二进制的数字')
                        elif choose[4] not in {'0','1'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = input('请输入八个二进制的数字')
                        elif choose[5] not in {'0','1'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = input('请输入八个二进制的数字')
                        elif choose[6] not in {'0','1'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = input('请输入八个二进制的数字')
                        elif choose[7] not in {'0','1'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = input('请输入八个二进制的数字')
                    input('升降门密码是'+code)
                    mark = 0
                    for i in range(8):
                        if code[i] == choose[i]:
                            mark += 1

                    input(f'你通过了{mark}道升降门')
                    
                    if mark >= 6:
                        input('你通过了升降门阵！')
                        go = 1
                    if mark < 6:
                        mark = 0
                        input('你未能通过升降门阵！')
        choose = input('你们来到街道对面。正当你们在街道上走着时，前面突然窜出两个小飞碟围住了你们。')
        choose = input('“我们是巡警，刚才上面接到了消息说有两个人类正在破坏公共财产，你们看到他们了吗？”')
        choose = input('“没有。”So说。')
        choose = input('“好的。”飞碟掉头就走，突然转了回来。')
        output('“不对啊……你们，就是人类吧……”一个飞碟说。两个飞碟顿时展开讨论。')
        output('“确实，很像照片里的那俩。”')
        output('“听说还有一个已经被抓去啦！”')
        output('“那啥啥，我们抓了他们吧！”')
        output('两个飞碟突然逼上前，向你们发出了闪光。')
        output('“拘捕令！现在！开始！对战！”一个飞碟说。')
        output('“真麻烦，要是能不对战直接抓了多好。”另一个插嘴道。')
        output('“不，不，不，我们没有破坏公共财物，是那个叫赛恩思的告诉你们上面的吧……”')
        choose = input('“什么赛恩思，我不知道，废话少说快束手就擒吧。”一个飞碟说。')
        print('战斗开始,对战飞碟*2')
        hucker = 0
        big_fight = 0
        t.sleep(0.5)
        car_A,car_B = 373,373
        check = 0
        magic_point = 0
        miaomiao = 0
        coat = 0
        win = 0
        DS = 3
        DSB = 0
        a,b,c,d,e = '','','','',''
        while win == 0:
            magic_choose = 0
            att_choose = 0
            item_choose = 0
            while magic_choose == 0 and item_choose == 0:
                item_att = 0
                if car_A <= 0:
                    car_A = 0
                if car_B <= 0:
                    car_B = 0
                chooseb = 'A'
                if DSB <= 60:
                    DSB = 0
                    if '战争宝石' in item:
                        print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health},飞碟A血量为{car_A},攻击力为27，飞碟B血量为{car_B},攻击为24，暴击数{big_fight}，飞碟防御力10，防御率20%')
                    if '战争宝石' not in item:
                        print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health},飞碟A血量为{car_A},飞碟B血量为{car_B}')
                    choose = input('A,物品B,防御C,魔法D,跳过')
                    while choose not in {'A','B','C','D'}:
                        print('请做出你的选择')
                        choose = input('A,物品B,防御C,魔法D,跳过')
                    if choose == 'A':
                        choose = input(f'你现在可使用的物品有{fight_item},请从1开始输入序号以选择使用的物品')
                        if choose not in {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'}:
                            choose = input('物品序号输入错误!')
                        else:
                            choose = int(choose)
                        if choose > len(fight_item):
                            choose = input('物品序号输入错误!')
                        else:
                            choose -= 1
                            check = fight_item[choose]
                            item_find()
                            if check == '魔法炸药':
                                choose = input('你对对方造成了100点伤害!但你也不小心受到了30点伤害')
                                health -= 30
                                cube -= 100
                                dead_interface()
                                if respawned == 1:
                                    break
                            if check == '坚硬冰棍':
                                choose = input('你使用了坚硬冰棍!敌方的HP降低了100点!')
                                cube -= 100
                            if check in fight_item and check in item:
                                item.remove(check)
                                fight_item.remove(check)
                            item_choose = 1
                            if health > 300:
                                health = 300
                    if choose == 'B':
                        choose = input('你选择了防御!')
                        magic_point += 40
                        magic_choose = 1
                        if magic_point >= 100:
                            magic_point = 100
                        chooseb = 'B'
                    if choose == 'C':
                        choose = input(f'A：治疗魔法（{health_point}）B：战斗魔法（70）C：黑暗魔法（？）D：暗蓝卫衣（30-50）')
                        while choose not in {'A','B','C','D'}:
                            print('请做出你的选择')
                            choose = input(f'A：治疗魔法（{health_point}）B：战斗魔法（70）C：黑暗魔法（？）D：暗蓝卫衣（30-50）')
                        else:
                            if choose == 'A':
                                if magic_point < health_point:
                                    choose = input('你的魔法值不够!')
                                    magic_choose = 0
                                if magic_point >= health_point:
                                    choose = input(f'你使用了治疗法术!你的血量回复了{health_plus}点!')
                                    health += health_plus
                                    magic_choose = 1
                                    magic_point -= 30
                                if health > 300:
                                    health = 300
                                    magic_choose = 1
                            if choose == 'B':
                                if magic_point < 70:
                                    choose = input('你的魔法值不够!')
                                    magic_choose = 0
                                if magic_point >= 70:
                                    choose = input('你使用了战斗法术!你的攻击提高了5点,持续一回合!')
                                    att_choose = 1
                                    magic_choose = 1
                                    magic_point -= 70
                            if choose == 'C':
                                choose = input('l͓̩̫̘͙͔̯͖̟̤̓͊̑̌́̂̆̚ò̥̪̭̱̰̝̒͂̄͋̿̏͆́̚c͍̲͇͚̖̬͈̪͙̳͌̉́̃k̪̥̱̝̱̑̈́̏̽͗̊̈́͂̀̍e̞͎̩̜̱̩͚̤̊͌̀̀d̠̖̞̝̙̪̟̞̐͛̈̊̀͂̄͌̓̏͌̓ͅ')
                                magic_choose = 0
                            if choose == 'D':
                                if magic_point < 50:
                                    choose = input('你的魔法值不够!')
                                elif magic_point >= 50:
                                    magic_point -= random.randint(30,50)
                                    coat = 1
                                    magic_choose = 1
                                    choose = input('你使用了暗蓝卫衣!你的闪避率提高了10％,持续一回合!')
                            choose = 0
                    if choose == 'D':
                        choose = input('你跳过了你的回合')
                        magic_choose = 1
                elif DSB >  60:
                    magic_choose = 1
                    DSB = 0
                    chooseb = 'B'
            car_act_B = random.randint(1,10)
            if '混乱护盾' in armor:
                health += random.randint(3,20)
                if health >= 300:
                    health = 300
            DS -= 1
            if DS == 0:
                DSB = 1
                input('飞碟正在准备一发激光打击！')
            if car_act_B == 1:
                input('飞碟正在蓄力射击')
            if car_act_B == 2:
                input('无聊的拉锯战就此展开')
            if car_act_B == 3:
                input('飞碟认为没有必要攻击太多')
            if car_act_B == 4:
                input('飞碟想保留实力，否则会挨骂')
            if car_act_B == 5:
                input('飞碟变成了飞饼')
            if car_act_B == 6:
                input('能量核心的气味')
            if car_act_B == 7:
                input('街道上人来人往')
            if car_act_B == 8:
                input('So用暗蓝卫衣掩护着你')
            if car_act_B == 9:
                input('TtTtT……PpPpP')
            if car_act_B == 10:
                input('你纳闷飞碟为什么没有警车')
            if car_A > 0:
                x = random.randint(1,4)
                a = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                b = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                c = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                d = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                e = chr(ord('A') + x - 1)
                enemy_fight = a+b+c+d+e
                enemy_fighta = [a,b,c,d,e]
                zero_att = 0
                if '零剑' in weapon:
                    zero_att = random.randint(5,50)
                choose = list(input(f'请选择你对飞碟A的攻击!(5个一组,由五个大写字母构成)'))
                hurt = 0
                hurtB = 0
                chance = 0
                wrong = 0
                while wrong == 0:
                    wrong = 1
                    if len(choose) != 5:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[0] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[1] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[2] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[3] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[4] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                else:
                    cube_act = random.randint(1,5)
                    while chance < 5:
                        f = choose.pop()
                        g = enemy_fighta.pop()
                        if chooseb != 'B':
                            if (f == 'A' and g == 'B') or (f == 'B' and g == 'C') or (f == 'C' and g == 'D') or (f == 'D' and g == 'A'):
                                hurt += att
                                chance += 1
                                if att_choose == 1:
                                    hurt += 5
                                if cube_act > 4:
                                    hurt -= 10
                                hurt += item_att
                                hurt += zero_att
                                if hucker == 1:
                                    hurt += 10
                                if '电磁激光枪' in weapon and magic_point >= 10:
                                    hurt += 35
                        if (f == 'D' and g == 'C') or (f == 'C' and g == 'B') or (f == 'B' and g == 'A') or (f == 'A' and g == 'D'):
                            hurtB += 24
                            if DS == 0:
                                hurtB += 21
                                DSB += 45
                            if chooseb == 'B':
                                hurtB -= (Def+blood_stone)
                                if hucker == 1:
                                    hurtB -= 30
                                if hurtB < 0:
                                    hurtB = 0
                            chance += 1
                            if coat == 1 and random.randint(1,10) == 5:
                                hurtB = 0
                            else:
                                health += 10
                        else:
                            chance += 1
                    if random.randint(1,20) == 3 and '战争宝石' in item and att_choose == 1:
                        hurt *= 3
                        big_fight += 1
                    if hide[0] + hide[1] >= random.randint(1,100):
                            hurtB = 0
                    health -= hurtB
                    item_att = 0
                    choose = input(f'飞碟A的攻击是{enemy_fight}')
                    if cube_act > 4 :
                        choose = input('飞碟A使用了防御!')
                    if chooseb != 'B':
                        choose = input(f'你对飞碟A造成了{hurt}点伤害!')
                        car_A -= hurt
                        hurt = 0
                    if chooseb == 'B':
                        choose = input('因为你选择了防御,所以伤害不计入')
                    choose = input(f'你被敌人扣除了{hurtB}点血')
                    dead_interface()
                    if respawned == 1:
                        break
            if car_B > 0:
                x = random.randint(1,4)
                a = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                b = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                c = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                d = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                e = chr(ord('A') + x - 1)
                enemy_fight = a+b+c+d+e
                enemy_fighta = [a,b,c,d,e]
                zero_att = 0
                if '零剑' in weapon:
                    zero_att = random.randint(5,50)
                choose = list(input(f'请选择你对飞碟B的攻击!(5个一组,由五个大写字母构成)'))
                hurt = 0
                hurtB = 0
                chance = 0
                wrong = 0
                while wrong == 0:
                    wrong = 1
                    if len(choose) != 5:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[0] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[1] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[2] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[3] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[4] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                else:
                    cube_act = random.randint(1,5)
                    while chance < 5:
                        f = choose.pop()
                        g = enemy_fighta.pop()
                        if chooseb != 'B':
                            if (f == 'A' and g == 'B') or (f == 'B' and g == 'C') or (f == 'C' and g == 'D') or (f == 'D' and g == 'A'):
                                hurt += att
                                chance += 1
                                if att_choose == 1:
                                    hurt += 5
                                if cube_act > 4:
                                    hurt -= 10
                                hurt += item_att
                                hurt += zero_att
                                if hucker == 1:
                                    hurt += 10
                                if '电磁激光枪' in weapon and magic_point >= 10:
                                    hurt += 35
                        if (f == 'D' and g == 'C') or (f == 'C' and g == 'B') or (f == 'B' and g == 'A') or (f == 'A' and g == 'D'):
                            hurtB += 24
                            if DS == 0:
                                hurtB += 21
                                DSB += 45
                            if chooseb == 'B':
                                hurtB -= (Def+blood_stone)
                                if hucker == 1:
                                    hurtB -= 30
                                if hurtB < 0:
                                    hurtB = 0
                            chance += 1
                            if coat == 1 and random.randint(1,10) != 5:
                                hurtB = 0
                            else:
                                health += 10
                        else:
                            chance += 1
                    if hide[0] + hide[1] >= random.randint(1,100):
                            hurtB = 0
                    health -= hurtB
                    item_att = 0
                    if random.randint(1,20) == 3 and '战争宝石' in item and att_choose == 1:
                        hurt *= 3
                        big_fight += 1
                    choose = input(f'飞碟B的攻击是{enemy_fight}')
                    if cube_act > 4:
                        choose = input('飞碟B使用了防御!')
                    if chooseb != 'B':
                        choose = input(f'你对飞碟B造成了{hurt}点伤害!')
                        car_B -= hurt
                        hurt = 0
                    if chooseb == 'B':
                        choose = input('因为你选择了防御,所以伤害不计入')
                    choose = input(f'你被飞碟B扣除了{hurtB}点血')
                    dead_interface()
                    hurtB = 0
                    att_choose = 0
                    if respawned == 1:
                        break
            hide[1] = 0
            coat = 0
            if DS == 0:
                DS = 3
            if DSB > 60:
                input('你被激光重击了！')
            if car_A > 0:
                car_A += random.randint(1,4)
            if car_B > 0:
                car_B += random.randint(1,4)
            if car_A <= 0 and car_B <= 0:
                choose = input('您获胜了!')
                CM_get = random.randint(241,494)
                CM += CM_get
                choose = input(f'你获得了{CM_get}个CM币')
                E_cotton += 1
                win = 1

        if respawned == 1:
            respawned = 0
            continue

        output('飞碟败下阵来。')
        output('“恶心的制度，要是能直接抓多好。”一个飞碟说。')
        output('“呃呃呃……你最好问一问他们有关同党的事情……”另一个飞碟小声对他说。')
        output('“好吧。”那个飞碟说着，对你们亮出一只显示屏：“你们认识这个人吗？”')
        output('显示屏上出现了昵称的照片！昵称被关在一个笼子里，笼子上面放射着电弧，昵称看起来十分惊慌。')
        output('So有点惊慌，你会回答：A：不认识,B：不认识')
        while choose not in {'A','B'}:
            output('So有点惊慌，你会回答：A：不认识,B：不认识')
        output('So有些恼怒地看着你，还好机器人没发现。')
        output('“好吧，那么我们暂时放过你们，你们走吧。”一个飞碟说，随后消失在房屋的角落里。')
        output('你们向前走去，So有点郁闷地看着你：“我的天，你不回答不就行了。”')
        output('你没理他，继续向前行进。')
        output('你们前面出现一条大街，许多小摊摆在道路两旁，摊后面是数不清的高档商店。')
        output('你会：A：看看小摊,B：看看高档商店,C：向前走')
        while choose not in {'A','B','C'}:
            output('你会：A：看看小摊,B：看看高档商店,C：向前走')
        if choose == 'A':
            output('小摊上摆放着许多能量饮料，机器人摊主对你说：“拿一瓶吧。”')
            output('你会：A：不拿,B：拿一瓶,C：全部拿走')
            while choose not in {'A','B','C'}:
                output('你会：A：不拿,B：拿一瓶,C：全部拿走')
            if choose == 'A':
                output('你没拿饮料')
            elif choose == 'B':
                choose = input('你拿了一瓶饮料（获得【能量饮料】）')
                item.append('能量饮料')
                view_status()
            elif choose == 'C':
                output('你刚想拿走，突然饮料瓶全都爆炸了，饮料洒了你一身。')
                output('“哈哈哈哈……”摊主大笑')
        elif choose == 'B':
            output('商店里陈列着一排排亮晶晶的珠宝，你会选择哪种颜色的？')
            output('A：蓝色,B：红色,C：紫色')
            while choose not in {'A','B','C'}:
                output('A：蓝色,B：红色,C：紫色')
            if choose == 'A':
                output('确认支付1000CMB购买吗？')
                output('A：确认,B：不买')
                while choose not in {'A','B'}:
                    choose = input('A：确认,B：不买')
                if choose == 'A':
                    if CM >= 1000:
                        CM -= 1000
                        item.append('战争宝石')
                        output('你获得了战争宝石')
                    elif CM < 1000:
                        choose = input('你的钱不够！')
                elif choose == 'B':
                    choose = input('你没有购买')
            elif choose == 'B':
                choose = input('确认支付1000CMB购买吗？')
                choose = input('A：确认,B：不买')
                while choose not in {'A','B'}:
                    choose = input('A：确认,B：不买')
                if choose == 'A':
                    if CM >= 1000:
                        CM -= 1000
                        item.append('生命宝石')
                        choose = input('你获得了生命宝石')
                    elif CM < 1000:
                        choose = input('你的钱不够！')
                elif choose == 'B':
                    choose = input('你没有购买')
            elif choose == 'C':
                output('一个写着“暂未开放购买”的显示屏出现在你面前，你隐隐约约地看到显示屏左下角有个“法术宝石”字样')
        output('你离开商店')
        output('你们继续前进，街道的尽头是一堵深蓝色的墙，墙上镶嵌着各式精美的艺术品。墙的后面林立着暗黄色的高楼群。')
        output('你们的面前出现了一个显示屏：\n“前方：LC区，因车祸事件地面道路暂时封锁。造成不便敬请谅解”')
        output('“嗯，看来我们要绕路。”So自言自语道，你们沿着墙向前走。')
        output('过了一会儿，你们来到一座开阔的空地，看起来是座公园。')
        output('你们向公园里走，来到一座倾斜的小坡下，一个机器人在这儿摆了个摊。')
        output('你们走到摊前，机器人招呼着对你说：“我是公园管理员，想去LC区吗？你们只需游玩我们的气球游戏，扎破所有气球后我就会给你们开门！”')
        output('你们看了看天空，三只气球被绳子绑着飘在空中。')
        output('看着你们犹豫的眼神，机器人说：“收益全部来自气球爆破获得的能量！”')
        output('So有点无奈地笑笑，对你说：“你来吧，我就算了。”')
        output('你看了看在天空中飘着的气球，感觉有些烦躁')
        output('机器人给你几根长矛，一旁的So对你说：“我刚才测了下气球对你的高度角，一个是24度，一个是31度，一个是45度。你扔就是了。”')
        output('你感到有些无奈')
        go = 0
        first = 0
        second = 0
        third = 0
        while go != 3:
            choose = input('你会朝哪个角度扔长矛？（回复角度的角度值，无需单位）')
            if choose in {'41','42'} and first == 0:
                go += 1
                first = 1
                input('你击中了第一个气球')
            elif choose in {'50','51'} and second == 0:
                go += 1
                second = 1
                input('你击中了第二个气球')
            elif choose in {'63','64'} and third == 0:
                go += 1
                third = 1
                input('你击中了第三个气球')
            else:
                input('你射空了！')
        output('你击中了所有气球！')
        output('你们击破了所有气球，机器人祝贺你们：“恭喜！我已经把门打开了，你们往那个地方走。”说完他给你们指了一个地方，那是围墙前面的一个缺口。')
        output('你们通过缺口，前面出现了一条平整的小路。')
        output('“我们要去208路4号……”我们走吧。So对你说，你们向前走去。')
        output('你们周围的颜色渐变成昏暗的黄绿色，街上的行人越来越多，那些看起来高科技的机器与汽车反而少了很多。')
        output('过了一会儿，你们来到一条开阔的大街，街道上人来人往，周围到处都是商铺，你们前面的显示屏上写着这条街就是LC区208路。')
        output('“我们到了，现在要找4号，简直是易如反掌了。”')
        go = 0
        while go == 0:
            output('你会：A：买点东西,B：交谈,C：看看门牌号')
            while choose not in {'A','B','C'}:
                output('你会：A：买点东西,B：交谈,C：看看门牌号')
            if choose == 'A':
                output('你来到一座商铺，店员殷勤地招待你们。')
                shop = 0
                while shop == 0:
                    output('请选择需要购买的物品：A：电棉【7CMB】,B：像素碎片【12CMB】,C：血石【244CMB】,D：能量晶体【1655CMB】,E：离开')
                    while choose not in {'A','B','C','D','E'}:
                        print('请做出您的选择')
                        output('请选择需要购买的物品：A：电棉【7CMB】,B：像素碎片【12CMB】,C：血石【244CMB】,D：能量晶体【1655CMB】,E：离开')
                    else:
                        money = 0
                        buy = 0
                        if choose == 'A':
                            if CM < 7:
                                output('你的CM币不够!')
                            else:
                                buy = '电棉'
                                money = 7
                        if choose == 'B':
                            if CM < 12:
                                output('你的CM币不够!')
                            else:
                                buy = '像素碎片'
                                money = 12
                        if choose == 'C':
                            if CM < 244:
                                output('你的CM币不够!')
                            else:
                                buy = '血石'
                                money = 244
                        if choose == 'D':
                            if CM < 1655:
                                output('你的CM币不够!')
                            else:
                                buy = '能量晶体'
                                money = 1655
                        if choose == 'E':
                            shop = 1
                        if E_cotton >= 20 and buy == '电棉':
                            view_status()
                            choose = input('你装不下那么多电棉！')
                        elif o_up >= 20 and buy == '像素碎片':
                            view_status()
                            choose = input('你装不下那么多像素碎片！')
                        elif buy != 0:
                            item.append(buy)
                            output(f'你购买了{buy}!')
                            if buy == '电棉':
                                E_cotton += 1
                            if buy == '像素碎片':
                                o_up += 1
                            if buy == '血石':
                                blood_stone += 1
                            else:
                                item.append('能量晶体')
                        buy = 0
                        CM -= money
                shops.append('商店3')
            elif choose == 'B':
                output('你找到一个机器人，他对你说：“嗯……这条街是旅游景点耶，我不是这里人不知道，不过……我觉得你可以查查导航系统')
                go = 1
            elif choose == 'C':
                num = random.randint(1,3)
                if num == 1:
                    num = 183
                elif num == 2:
                    num = 265
                elif num == 3:
                    num = 438
                output(f'你随便点了个门牌号，发现这是{num}号，你不知道要点到啥时候')
        output('你们点开了一个导航系统的显示屏，当So输入目的地时，显示屏立刻化成了一条长长的细线，一个蓝色的箭头在细线上出现，与你们伴随在一起。')
        output('你们顺着箭头向前走去，来到一座大楼前，细线向大楼内部转去。你们看向这座大楼，大楼与周围的众多建筑似乎不同，建筑风格是你们熟悉的现代风，失去了城市里建筑的前卫感。')
        output('你们正想走进大楼，一个机器人提醒你们：“喂！你们去干嘛？这楼是个废弃楼，马上要拆了！”')
        output('你们再次打量了下这大楼，发现它的外灯是灭的，而周围楼房外灯都亮得刺眼，同时，你们发现大楼上没有亮起任何显示屏。')
        output('你们有点不知所措，So说：“怎么办，看起来更像圈套了。”')
        output('你会：A：进去,B：问人')
        while choose not in {'A','B'}:
            output('你会：A：进去,B：问人')
        if choose == 'A':
            output('你们还是进入了大楼')
        elif choose == 'B':
            output('一个机器人说：“我知道，这楼毕竟是4号，很早的时候就建成了，只是最近要拆的，虽然楼里的其他人都搬出去了，但还是有个人一直反对，这种钉子户真的烦。')
            output('你们听了这话，有些疑惑地进了大楼')
        output('你们进入大楼，里面的房间一反城市的整洁，遍布着灰尘。楼里空无一人，你们小心翼翼地往前走去。')
        output('楼里出现一座电梯，你们刚接近电梯，电梯门上突然出现了一个显示屏，把你们吓了一跳：\n“电梯坏了，走楼梯上来。”')
        output('你们的旁边出现了一个楼梯，你们从楼梯上去，二楼被一道铁门锁着，一个显示屏在门上出现：\n“一直上到顶。”')
        output('你们继续上楼梯，每一楼都有铁门锁着，最后的五楼铁门开着，你们面前出现了一条走廊。走廊尽头有一扇门。')
        output('“进来吧。”一个显示屏在走廊墙上出现。')
        output('“我们……”So小声说。')
        output('你会：A：小心翼翼地进去,B：冲进去')
        while choose not in {'A','B'}:
            output('你会：A：小心翼翼地进去,B：冲进去')
        if choose == 'A':
            output('你们小心翼翼地挪到门前，缓缓打开门')
        elif choose == 'B':
            output('你们冲到门前，猛地一下子推开门')
        output('门后是一个小小的房间，里面只有一张办公桌，一堆机器杂乱无章地摆放在房间里，但你发现然而在这杂乱无章的世界里居然出现了绿色植物！房间的窗前摆放着许多植物，与城市周围那些奇奇怪怪的植物不同，这是你真正见过的植物！可惜的是，你并不知道它们的名字。')
        output('“这里很乱，希望你们不要嫌弃它。”一个声音传来。')
        output('你和So顺着声音望去，一位天蓝色头发、穿着浅紫色短裤、短袖的男孩站在你们面前。')
        output('“你们好，感谢你们能过来，你们叫我小天就好。”')
        output('“嗯……就是你给我们发消息的？”So问。')
        output('“没错，都是我发的，我一直在用显示屏追踪你们，在赛恩思那东西疏忽的时候我就马上发信息给你们，可惜每次只能发一些提示。只有你们进入城市，我才能和你们远程通话。总之，我真的很感谢你们可以来这里，真的……”')
        output('小天对你们露出了真诚的微笑。')
        output('“嗯，那么，你叫我们过来是为了干什么呢？”')
        output('“你忘了吗？我可以帮你们找到赛恩思，不过……”')
        output('小天走到一旁，你发现那边的墙上，在电线和机器组成的庞大空间之外，有一张小小的海报。')
        output('你凑近看了看海报，海报上面站着一个人，虽然穿着不同，但是你很快就看清楚了那是谁，你感到一阵晕厥——')
        output('那是罗尔斯！！！')
        output('“SEED。”小天慢慢地说，你发现小天刚才的笑容消失了，他的蓝色眼睛里似乎有怒火在积攒。')
        output('“我会告诉你们，我为什么如此希望你们来，我会告诉你们，我的生活是怎么被毁掉的，我会告诉你们，我为什么会跑这儿来干这种事，一切都是……”')
        output('小天突然停住了，他看着你们，突然说：“你们……应该有注意到四处的那个奇怪的东西，FireFox.max吧。”')
        output('你点点头。')
        output('“好，我现在就从这玩意儿讲起吧。”小天说。')
        output('“FireFox，也就是火狐，是我的大学同学，我的舍友，他是我最好的朋友。')
        output('就在半年前，他的父母——嗯，他的父母在特警部队工作——在一次执行任务之前被人暗杀了，暗杀的地点，以及他父母的……死状都很不光彩……是一个赌场，他们死时怀里揣着大把的百元钞票。他的父母随后被判定为“与黑恶势力勾结的叛徒”这件事给火狐的打击很大。他在整理父母的遗物时，意外发现了一个标有“SEED”字样的信件，是他父母关于一个不明组织的侦查记录，一直到死前，他的父母一直在与这个组织作对。”')
        output('“从那时起，火狐，他下定决心一定要消灭SEED，这个使他失去父母，让父母名声尽毁的组织。”')
        output('“他认识父母部队里的人，尽管他屡次被警告不要沉迷于这事上，但他没有改，”')
        output('“他整天搜集SEED的资料，我们其他人都睡了的时候，他还在网上搜索那些父母遗留下来的图片，终于，他发现了一个可疑对象，一个叫罗尔斯的武器商，他是SEED的负责人。”')
        output('“可是当他把这些线索发给父母的部队时，部队里的人却不重视这些辛辛苦苦找来的线索，用他们的话来说，火狐这个学生不学习整天找这些没用的东西干什么。火狐没办法，只能自己去找。')
        output('“可惜这一找就出事了，当他费尽心思找到罗尔斯的地址拍下照片的时候，却没发现罗尔斯正在暗处看着他。”')
        output('“当然，火狐对这些事情毫不知情，他屡次碰壁，没有人相信他搜索的证据是关于危险组织的，这可能有点荒谬，但实在是没办法，即使是魔法普及的时代，政府的工作纪律也是不能被打乱的。为了搜集这些证据，火狐甚至不惜熬夜，旷课，被学校批评了好几次。”')
        output('“就在他快要崩溃的时候，又发生了一件雪上加霜的事情，火狐的小妹妹，当时正在上初中的雪狐，在首都郊外的一次滑雪旅行中发生了意外事故，有目击者看到载着雪狐的电子滑雪板失控了，没有减速直接冲下了几百米高的悬崖！尽管搜救队员努力寻找，最后只在山谷中找到了断掉的滑雪板，而不见雪狐的踪影。”')
        output('“意外发生的这件事情使火狐几乎要崩溃了，他放弃了自己的搜察，整天郁郁不乐。直到有一天，我看见火狐抱着那双断裂的滑雪板，对我说，他发现这滑雪板里面被植入了恶意软件，SEED一定行动了。”')
        output('“接下来的事情让我有点震惊，火狐头一低，对我说：')
        output('“小天……我……我要走了，我一个人去干掉他们……”')
        output('“别啊……你……你还有那么好的前途，你你不要这样想，你还是……”我慌张地劝他')
        output('“首都……不，整个魔法界域都没办法为我的父母求个公道，如果这样的话……我只能自己上了！”')
        output('“别这样！你不要拿前途开玩笑啊！求你了！”')
        output('“唉……”火狐轻声叹了口气，“这种情况下，我应该不会有什么前途吧。”')
        output('“火狐没有听我的，当天晚上他就失踪了。令我没有想到的是，仅仅一周之后，有人在首都一座公园的湖里打捞出了他的尸体。”')
        output('“等等。”So打住了小天的话，“能不能说下重点，你一直都在说别人。”')
        output('“嗯……其实也差不多了。”小天有点尴尬地说，“好吧我再来说下我自己的……”')
        output('“是这样的，火狐死后有一天，我的期末作业……就是一个自己做的很大的电元件炸了，炸伤了我的几个室友。在这之后，我不断地遭到一些不明的攻击，我怀疑我被盯上了。')
        output('“我报了警，警方说这是一种魔法追踪导弹，只要取到我的一些个人特征，哪怕是信息也好，就可以对我进行人身追踪，远程攻击我。”')
        output('“警方建议我请假去其他地方避难，这种导弹很容易伤及无辜，并且法律上也有相关的规定，他们需要大概三天时间把这个导弹清除掉。于是我就随便买了张车票跑来了这座小城市。现在想想，也许这也是个圈套。”')
        output('So突然打断：“等等，你说这是个小城市？！”')
        output('“和首都相比当然小。”小天平静地说。')
        output('“当我刚来到这里的时候，并没有什么异状，我免费得到了这个快要废弃的房间，在网上继续我的学习。')
        output('可是有一天，当我散步的时候，我突然发现了一个巨大的SEED海报！就摆在道路中最显眼的位置。”')
        output('“我有点害怕，我觉得这可能是个圈套，我顿时想到离开这里，可是当我打开列车购票栏，我发现我已经被划了一道“失信被执行人”！我无法购票！这座城市地面被巨大的河流环绕，只有高价架列车这一种交通工具可以出去，如果我不能买票，就意味着我被困住了！”')
        output('“我十分害怕，赶快回到我的房间，我当时根本不知道怎么办。”')
        output('“直到我看到了前面闪烁着的电脑标签，我想，既然SEED要陷害我，而他们却没有直接采取行动，只能是因为他们在等待时机，如果是这样的话，我必须抢先行动击败SEED，只有这种方法才能让我活下来！”')
        output('“我随即搜索了很多关于SEED的资料，资料非常的细碎，但我至少发现了其中一个重要的成员赛恩思，                       也就是SCI或者S 281738368，他是一名被放逐的黑客，目前在SEED当目标攻击员。我和火狐受到的攻击应该就是他发动的。赛恩思操控着这座城市的绝大部分网络系统，我不可能逃离他的手心。”')
        output('“然而，在经过我的观察后，我发现赛恩思并不是不可击败，我发现赛恩思只能随机穿行于网络世界中，利用网络世界的节点法则攻击并入侵具体的机器人，但对于现实的事物，赛恩思的能力非常有限，他只是一个利用光传感器进行自我判断的普通智能机器人，即使他入侵其它机器人，我也能利用我的技术反击，因此我并非没有胜算。”')
        output('“我很快想了个办法，在网络上发布一个代号为00000000000000，标签为Firefox.max的程序，这个名字是故意引起赛恩思的注意。这个程序可以自动潜伏在所有的实体计算器内部，这样我就可以通过它来连接各个网络节点，制造一个伪系统侦查赛恩思的动向，这个系统在被赛恩思监控后将会自毁，并发送数据，使我能够对赛恩思在网络世界的范围提供了解，并且进一步侦测赛恩思的现实动向。”')
        output('“经过我的不懈努力，我成功了。我找到了赛恩思的定位。”')
        output('“但是，令我没想到的是，在我侦查的最后关头，赛恩思行动了。”')
        output('“有一天，当我在街上搜集资料时，两个机器人突然把我拉到了一个小巷里，许多电子蛇向我冲了过来，我立即将我的武器——一个停摆程序给他们安上，他们立刻停下了攻击，但令我吃惊的是，我的停摆程序不仅威胁到了他们，还威胁到了我身下的地板！”')
        output('“地板是由力场组成的，我的停摆程序不仅使他们停摆了，还顺带罢工了附近的一个力场发生器！我顿时向下坠去，另一个力场将我捉住，我滚到了一个奇怪的平台上，平台上还站着一个机器人，他就是我无数次在网上看到的那个人，赛恩思。”')
        output('“赛恩思笑着对我说：“小天啊，你好，听说你给我造成了许多麻烦，但你知道吗？这些麻烦我——根本就感觉不到！你看看，我也能侦查你哦——”')
        output('“赛恩思说完后，对我伸出了一把电磁激光枪，里面突然出现一个红色的笼子，我根本就没什么魔法攻击力，对这情况完全束手无策，在慌乱中我被击中了，晕了过去。”')
        output('“当我醒来的时候，我发现我正躺在这个房间里，看来赛恩思并没有伤害我。”')
        choose = input('“但当我想看看网络的时候，我突然意识到赛恩思做了什么：\n我无法打开网络！')
        output('赛恩思不知道做了些什么，把我与这网络世界的一切联系都切断了，我在这城市里相当于变得透明，我跑到街上尽可能地想引人注意，没有人注意到我，我想逃跑，可是每个区的边界都是力场门，我根本出不去，我尝试过搭便车出去，可是到了城市边界时，我仍然要乘列车，这意味着我需要通过力场门……我什么方法都试过了，但现在只能说明，我被困死在了这里！”')
        output('“最后，我回到了这座房间，我只想用我最后的一点器材，在这庞大的网络世界里，自己制造一点节点，尽量让我和这网络能连接起来，在半年来，我取得了一点成果，但想要逃脱，仍然希望渺茫。”')
        output('“当我看到你们到来的时候，我重新燃起了希望，如果你们可以帮我击败赛恩思，那么我就可以得到解脱，当我看到你们挡住了那红色笼子的时候，我更坚定地相信了这一点！所以，请你们一定要帮帮我……”')
        output('“等等，”So插了句，“你刚才让我们来帮你，但……你还记不记得你叫我们过来的时候，你说的是你可以帮我们呢……”')
        output('“嗯！我要说的就是这个！”小天点了点头')
        output('“你还记得我已经知道了赛恩思的活动范围吗？我发现，赛恩思本体一直在P区的比特塔——那是P区的特别区域比特区的地标建筑啊——活动，那座建筑虽说是地标，但是却禁止外人进入游览，最近似乎开放了一点点。经过我的侦查，那里面有一个“终极核心”，赛恩思好像很重视那玩意儿，如果你们可以进入那里，并且摧毁它，赛恩思就可能被击败！我不会战斗，所以我苦于没办法进去，你们一定可以——”')
        output('“好了，我知道了。”So平静地说。“只是，你知道昵称……”')
        output('小天有些纳闷：“昵称？不知道是谁，我只是说，你们可以先去P区，可以坐列车去，城市里到处……”')
        output('“昵称就是我们的另一个伙伴啊！”So有些急了。')
        output('“你说啥……啊？就是那个猫人……她收到了那玩意儿的攻击，我也不清楚她现在怎么了……”小天说。')
        output('“这样啊……”So有些懊恼，“那，Zero，我们去P区吧。”')
        output('你会：A：去P区,B：再问些问题,C：到处看看')
        while choose not in {'A','B','C'}:
            output('你会：A：去P区,B：再问些问题,C：到处看看')
        ask = 0
        if choose == 'B':
            output('So问道：“那，有两个人，阿尔法和贝塔，你知道这是谁吗？”')
            output('小天有些惊奇：“这是谁？赛恩思的同伙吗？赛恩思没有同伙啊……”')
            output('So只好作罢')
            ask = 1
        elif choose == 'C':
            output('你到处看了看四周，并没有什么特别的')
        output('你们正要出门，小天突然叫住了你们。')
        output('So有些懊恼地回头，小天在你们身后招着手：“下次再来啊！”')
        output('你们走出建筑的大门，来到外面的街道。')
        output('你会：A：随便逛逛,B：找列车站')
        while choose not in {'A','B'}:
            output('你会：A：随便逛逛,B：找列车站')
        if choose == 'A':
            output('你到处逛了逛，并没有什么用')
        elif choose == 'B':
            output('你开了个显示屏找列车站，意外地发现了一个废弃的显示屏，里面有20CMB！')
            CM += 20
        output('就在这时，So打开了关于列车的显示屏，向你指出了一个最近的列车站，你们便往前走去。')
        output('当你们来到列车站前的时候，发现车站就是一座巨大的发电塔，各式列车穿行在塔的上空。')
        output('你们随着人群挤进车站，前面出现了几道升降门')
        if tower == 1:
            choose = input('你通过了升降门')
        else:
            go = 0
            mark = 0
            while go == 0:
                code = []
                for i in range(3):
                    code.append(chr(ord('0')+random.randint(0,1))+chr(ord('0')+random.randint(0,1))+chr(ord('0')+random.randint(0,1)))
                for i in range(1):
                    choose = input('请输入三个二进制的数字')
                    wrong = 0
                    while wrong == 0:
                        wrong = 1
                        if len(choose) != 3:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = input('请输入三个二进制的数字')
                        elif choose[0] not in {'0','1'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = input('请输入三个二进制的数字')
                        elif choose[1] not in {'0','1'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = input('请输入三个二进制的数字')
                        elif choose[2] not in {'0','1'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = input('请输入三个二进制数字')
                    input('升降门密码是'+code[i-1])
                    answer = code[i-1]
                    compare = 0
                    while compare < 3:
                        if answer[compare] == choose[compare]:
                            mark += 1
                        compare += 1
                    if choose == code[i-1]:
                        input(f'你通过了{mark}道升降门')
                        go = 1
                    if mark >= 2:
                        input('你通过了升降门阵！')
                    if mark < 2:
                        mark = 0
                        input('你未能通过升降门阵！')
        output('你们来到了一条巨大的力场道上，许多子弹形状的列车悬浮穿梭在这条道路上空，你看见一只绿色的列车在你们面前停了下来，你们进入列车。')
        output('你们来到了列车内部，找到了座位坐好。你们旁边有许多机器人，看起来像是上班族，你们前面，一位机器人推着餐车向你们走来。')
        output('你会：A：交谈,B：看列车时间表,C：看餐车,D：不管他')
        while choose not in {'A','B','C','D'}:
            output('你会：A：交谈,B：看列车时间表,C：看餐车,D：不管他')
        if choose == 'A':
            output('机器人看起来很忙，不想跟你交谈')
        if choose == 'B':
            output('你看了看列车时间表：\n“下一站：LZTR4027，下下站：45MZEE12D7432……”')
            output('你不想看下去了。')
        if choose == 'C':
            output('餐车员看到你过来，丢给你了一份能量饮料，惊奇地说：“我天，这是第一个主动找我的……”（获得【能量饮料】）	')
            item.append('能量饮料')
            fight_item.append('能量饮料')
        choose = input('你们在列车上休息了一小会儿，在这段时间里，列车全身变得透明，你们可以通过车身看到外面城市的景色，宁静祥和的景色令你放松[HPmax]。')
        health = 300
        view_status()
        output('正当你们欣赏着城市繁华的灯火时，餐车员突然向你们走来，小声对你们说：“您们好，请问您们想不想尝试一下我们的【特殊餐饮服务】呢，请跟我来到前面吧。”')
        print('你会：A：接受,B：拒绝,C：啥是【特殊餐饮服务】')
        t.sleep(0.7)
        print('餐车员没等你们回答，一下把餐车向你们推了过来（请快速回复数字闪开！要求每位二进制数字与攻击不相同）')
        t.sleep(0.5)
        code = []
        for i in range(3):
            code.append(chr(ord('0')+random.randint(0,1))+chr(ord('0')+random.randint(0,1))+chr(ord('0')+random.randint(0,1)))
        t1 = t.time()
        choose = input(f'{code},请选择你的躲避方式！')
        t2=t.time()
        t3 = t2 - t1
        if t3 <= 5 and choose == code:
            output('你们闪在一边，但餐车的食品纷纷掉落，向你们冲过来，你们要躲避这些食品！')
            print('回复字母以躲避！')
            choose = list(input('请输入你的躲避方式！'))
            x = random.randint(1,4)
            a = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            b = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            c = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            d = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            e = chr(ord('A') + x - 1)
            enemy_fight = a+b+c+d+e
            enemy_fighta = [a,b,c,d,e]
            hurt = 0
            hurtB = 0
            chance = 0
            wrong = 0
            while wrong == 0:
                wrong = 1
                if len(choose) != 5:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(5个一组,由五个大写字母构成)'))
                elif choose[0] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(5个一组,由五个大写字母构成)'))
                elif choose[1] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(5个一组,由五个大写字母构成)'))
                elif choose[2] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(5个一组,由五个大写字母构成)'))
                elif choose[3] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(5个一组,由五个大写字母构成)'))
                elif choose[4] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(5个一组,由五个大写字母构成)'))
            else:
                while chance < 5:
                #快悄悄这个地方,我把chance < 5写成了chance <= 5然后查了一天才查到这个bug
                #悄悄改为瞧瞧,这是个错别字(划)通假字
                #快看,这里我复制的前面
                    #快看，我还是复制的前面（
                    f = choose.pop()
                    g = enemy_fighta.pop()
                    if f == 'D' and g == 'C' or f == 'C' and g == 'B' or f == 'B' and g == 'A' or f == 'A' and g == 'D':
                        hurtB += 5
                        chance += 1
                    else:
                        chance += 1

                health -= hurtB
                choose = input(f'服务员的进攻方式是{enemy_fight}')
                choose = input(f'你被扣除了{hurtB}点血量')
                dead_interface()
                if respawned == 1:
                    respawned = 0
                    continue
        else:
            choose = input('你们被餐车击中了[HP-50]')
            health -= 50
            dead_interface()
            view_status()
        output('你们躲向一块背景板旁边，在城市的灿烂灯火中，你们发现车上的所有旅客都变了个样，他们眼睛里闪着红光向你们逼近，而那个餐车员在人群之中一动不动，似乎着了魔。')
        output('一个机器人走到你跟前，你发现他的腰上也出现了那个红色的凸起，你发现那原来是个巨大的镶嵌在他身上的水晶！')
        output('正当你想攻击水晶时，机器人突然闪电般地用拳头向你挥打过来，你赶快闪在一旁，向机器人还击，机器人转身接过你的还击，你们两个扭打在一起。')
        output('你们打得正激烈时，你突然瞟了一眼旁边的So，他完全接不住机器人的攻势，被机器人打翻在地，又被另一个机器人踢向餐车员旁边，餐车员还在那儿若无其事地冷笑着。')
        output('就在你看了眼这一切时，那个机器人用手刀向你腰部切过来，你向后弯腰躲过机器人手刀，翻过身全力向机器人的头部虚打一拳，当机器人伸手护住时，你的那一拳早已退下来做掩护，另一只拳全力打向水晶，水晶炸裂开来！')
        output('机器人向后退了退，随即倒在地上，旁边的几个机器人见不能取胜便赶快向你包围过来。')
        output('你会：A：继续攻击杀出一条道,B：趁还未包围全速后退,C：向机器人的间隙间冲出去')
        while choose not in {'A','B','C'}:
            output('你会：A：继续攻击杀出一条道,B：趁还未包围全速后退,C：向机器人的间隙间冲出去')
        if choose == 'A':
            choose = input('你一个人迎着几个机器人的攻势冲了上去，将一个机器人的水晶击破，打开了一条缺口，但自己也挨了几拳[HP-140]')
            health -= 140
            dead_interface()
            view_status()
        elif choose == 'B':
            choose = input('你往后翻上一只椅子，虽然逃离了机器人的包围圈，但更多的机器人在你后面向你赶来，你从椅子上跃起踩在机器人身上向前跳，却没想到列车高度太低，撞到了天花板摔了下来[HP-40]')
            health -= 40
            dead_interface()
            view_status()
        elif choose == 'C':
            output('你趁机器人没合拢找到间隙冲了出去，机器人对你出拳的时机似乎早了点，你躲过了机器人的出拳')
        output('你来到餐车员的旁边抓起So准备逃跑，餐车员突然微笑着说了一句：“慢着。”')
        output('你身后传来一片破碎声，你回头看向后面，所有的机器人纷纷跌倒在地，水晶似乎全都破裂了。')
        output('“这水晶我可以量产，可以随便安在任何一个机器人上，可以随便启动甚至销毁它们，只要我想。”餐车员说。')
        output('“你是赛恩思！”So喊道')
        output('“赛恩思？不我不是。”餐车员回答。“可是啊，要是赛恩思没有我，准确来说是我们，他也不可能对你们这么强的对手造成什么实质性的伤害，唯独……”')
        output('餐车员伸手指了指你们身下的城市：“这座城市，本身就是沙漠界域高度集中化管辖体制的表现，如果我们可以利用好这一点……我的天，那咱们就无敌了不是吗，想象一只百万机器人组成的大军，什么类型的都有，而且……永不疲劳，永不死亡！调动这样的大军便是我的自负之处！！”')
        output('“我，就是赛恩思的左参谋机器人，阿尔法！！！”餐车员用装的无比凶狠的表情向你们看过来。')
        output('“阿尔法？！！”So惊叫道，“那么是不是还有个贝塔……”')
        output('“贝塔他不屑于来这种地方。”阿尔法说。“他也只能在比特塔里面研究研究能量核心，仅此而已！统帅机器人大军是我一个人的责任！”')
        if ask == 1:
            output('So凑到你身边，小声地对你说：“小天该不会骗了我们吧……”')
        savepoint = 16
    if savepoint == 16:
        save_data()
        output('阿尔法上前一步：“不过呢，很遗憾，我们的团战系统做得不够好，现在只能容纳下三个人，但以后肯定会出现更多甚至任意人数的团战系统吧！所以呢，今天只能由我一个人解决你们啦！”')
        print('战斗开始,对战阿尔法')
        hucker = 0
        big_fight = 0
        t.sleep(0.5)
        alpha = 1000
        check = 0
        magic_point = 0
        miaomiao = 0
        item_att = 0
        coat = 0
        win = 0
        alpha_first = 1
        alpha_robot = 2
        alpha_robot_B = 0
        alpha_punch = random.randint(2,9)
        zero_att = 0
        a,b,c,d,e = '','','','',''
        while win == 0:
            magic_choose = 0
            att_choose = 0
            item_choose = 0
            while magic_choose == 0 and item_choose == 0:
                chooseb = 'A'
                if alpha_robot_B == 0:
                    if '战争宝石' in item:
                        print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health},阿尔法血量为{alpha},攻击力为30，防御力50，防御率10%，暴击数{big_fight}')
                    if '战争宝石' not in item:
                        print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health},阿尔法血量为{alpha}')
                    choose = input('A,物品B,防御C,魔法D,跳过')
                    while choose not in {'A','B','C','D'}:
                        print('请做出你的选择')
                        choose = input('A,物品B,防御C,魔法D,跳过')
                    if choose == 'A':
                        choose = input(f'你现在可使用的物品有{fight_item},请从1开始输入序号以选择使用的物品')
                        if choose not in {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'}:
                            choose = input('物品序号输入错误!')
                        else:
                            choose = int(choose)
                            if choose > len(fight_item):
                                choose = input('物品序号输入错误!')
                            else:
                                choose -= 1
                                check = fight_item[choose]
                                if check == '冰棍':
                                    choose = input('你使用了冰棍!你的HP增加了15点!')
                                    health += 15
                                if check == '杆草':
                                    choose = input('你使用了杆草!你的HP增加了20点!')
                                    health += 20
                                if check == '流油果':
                                    choose = input('你使用了流油果!你的HP增加了40点,ATT临时增加了5点!')
                                    health += 40
                                    item_att += 5
                                if check == '花色汉堡':
                                    choose = input('你使用了花色汉堡!你的HP增加了50点!')
                                    health += 50
                                if check == '魔法炸药':
                                    choose = input('你对对方造成了100点伤害!但你也不小心受到了30点伤害')
                                    health -= 30
                                    car_A -= 100
                                    car_B -= 100
                                    dead_interface()
                                    if respawned == 1:
                                        break
                                if check == '坚硬冰棍':
                                    choose = input('你使用了坚硬冰棍!飞碟的HP降低了100点!')
                                    car_A -= 100
                                    car_B -= 100
                                if check == '方块糖果':
                                    choose = input('你使用了方块糖果!你的HP增加了40点!')
                                    health += 40
                                if check == '红桃蛋糕':
                                    choose = input('你使用了红桃蛋糕!你的HP增加了100点!')
                                    health += 100
                                if check == 'CRD硬糖':
                                    choose = input('你使用了CRD硬糖!你的HP增加了14点,ATT临时增加了5点!')
                                    health += 14
                                    item_att += 5
                                if check == '冰淇淋':
                                    choose = input('你使用了冰淇淋!你的HP增加了40点,DEF扣了1点!')
                                    health += 40
                                    Def -= 1
                                if check == '能量饮料':
                                    choose = input('你使用了能量饮料!你的HP增加了20点,ATT临时增加了5点!')
                                    health += 20
                                    item_att += 5
                                if check == '五彩糖':
                                    choose = input('你使用了五彩糖!你的HP增加了20点!')
                                    health += 20
                                if check == 'H-饼干':
                                    plus = random.randint(4,300)
                                    choose = input(f'你使用了H-饼干!你的HP增加了{plus}点!')
                                    health += plus
                                if check == '黑客三周年限定蛋糕':
                                    choose = input('简单模式开启!你的血量增加了250点,本次战斗ATT增加10点,DEF增加30点!')
                                    hucker = 1
                                    health += 250
                                if check == '电棉':
                                    E_cotton -= 1
                                    choose = input('你吞下了一大坨...电子蛇的排泄物，你的HP减少了1点！')
                                    health -= 1
                                    dead_interface()
                                    if respawned == 1:
                                        break
                                item.remove(check)
                                fight_item.remove(check)
                                item_choose = 1
                                if health > 300:
                                    health = 300
                    if choose == 'B':
                        choose = input('你选择了防御!')
                        magic_point += 40
                        magic_choose = 1
                        if magic_point >= 100:
                            magic_point = 100
                        chooseb = 'B'
                    if choose == 'C':
                        choose = input(f'A：治疗魔法（{health_point}）B：战斗魔法（70）C：黑暗魔法（？）D：暗蓝卫衣（30-50）')
                        while choose not in {'A','B','C','D'}:
                            print('请做出你的选择')
                            choose = input(f'A：治疗魔法（{health_point}）B：战斗魔法（70）C：黑暗魔法（？）D：暗蓝卫衣（30-50）')
                        else:
                            if choose == 'A':
                                if magic_point < health_point:
                                    choose = input('你的魔法值不够!')
                                    magic_choose = 0
                                if magic_point >= health_point:
                                    choose = input(f'你使用了治疗法术!你的血量回复了{health_plus}点!')
                                    health += health_plus
                                    magic_choose = 1
                                    magic_point -= 30
                                if health > 300:
                                    health = 300
                                    magic_choose = 1
                            if choose == 'B':
                                if magic_point < 70:
                                    choose = input('你的魔法值不够!')
                                    magic_choose = 0
                                if magic_point >= 70:
                                    choose = input('你使用了战斗法术!你的攻击提高了5点,持续一回合!')
                                    att_choose = 1
                                    magic_choose = 1
                                    magic_point -= 70
                            if choose == 'C':
                                choose = input('l͓̩̫̘͙͔̯͖̟̤̓͊̑̌́̂̆̚ò̥̪̭̱̰̝̒͂̄͋̿̏͆́̚c͍̲͇͚̖̬͈̪͙̳͌̉́̃k̪̥̱̝̱̑̈́̏̽͗̊̈́͂̀̍e̞͎̩̜̱̩͚̤̊͌̀̀d̠̖̞̝̙̪̟̞̐͛̈̊̀͂̄͌̓̏͌̓ͅ')
                                magic_choose = 0
                            if choose == 'D':
                                if magic_point < 50:
                                    choose = input('你的魔法值不够!')
                                elif magic_point >= 50:
                                    magic_point -= random.randint(30,50)
                                    coat = 1
                                    magic_choose = 1
                                    choose = input('你使用了暗蓝卫衣!你的闪避率提高了10％,持续一回合!')
                            choose = 0
                    if choose == 'D':
                        choose = input('你跳过了你的回合')
                        magic_choose = 1
                else:
                    magic_choose = 1
            car_act_B = random.randint(1,10)
            alpha_robot_B = 0
            if '混乱护盾' in armor:
                health += random.randint(3,20)
                if health >= 300:
                    health = 300
            if alpha_first == 1:
                input('一场充满危机感的战斗开始')
                alpha_first = 0
            else:
                if car_act_B == 1:
                    input('阿尔法阻止了你们的进攻')
                if car_act_B == 2:
                    input('阿尔法正在组织一轮攻势')
                if car_act_B == 3:
                    input('阿尔法的攻击如雨点般打向你们')
                if car_act_B == 4:
                    input('城市的景色在你们身后')
                if car_act_B == 5:
                    input('列车上其他机器人集体震了震')
                if car_act_B == 6:
                    input('So指了指他的暗蓝卫衣')
                if car_act_B == 7:
                    input('你发现阿尔法正在思索着什么')
                if car_act_B == 8:
                    input('So用暗蓝卫衣掩护着你')
                if car_act_B == 9:
                    input('自助食品散落在你们周围')
                if car_act_B == 10:
                    input('你们觉得阿尔法似乎不想让战斗过得太快')
            alpha_robot -= 1
            alpha_punch -= 1
            if alpha_punch == 0 and alpha_robot == 0:
                alpha_punch += 1
            if alpha_robot == 0:
                alpha_robot = 4
                input('阿尔法利用红色水晶制造了两个机器人挡在你们面前，你们必须先消灭它们！')
                chanceb = 2
                while chanceb > 0:
                    if chanceb == 2:
                        choose = list(input('请输入你对第一个机器人的进攻方式'))
                    if chanceb == 1:
                        choose = list(input('请输入你对第二个机器人的进攻方式'))
                    chanceb -= 1
                    x = random.randint(1,4)
                    a = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    b = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    c = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    d = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    e = chr(ord('A') + x - 1)
                    enemy_fight = a+b+c+d+e
                    enemy_fighta = [a,b,c,d,e]
                    hurt = 0
                    hurtB = 0
                    chance = 0
                    wrong = 0
                    while wrong == 0:
                        wrong = 1
                        if len(choose) != 5:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[0] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[1] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[2] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[3] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[4] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    else:
                        while chance < 5:
                            f = choose.pop()
                            g = enemy_fighta.pop()
                            if f == 'D' and g == 'C' or f == 'C' and g == 'B' or f == 'B' and g == 'A' or f == 'A' and g == 'D':
                                hurtB += 10
                                chance += 1
                            else:
                                chance += 1

                        health -= hurtB
                        choose = input(f'机器人的进攻方式是{enemy_fight}')
                        choose = input(f'你被扣除了{hurtB}点血量')
                        dead_interface()
                        if respawned == 1:
                            respawned = 0
                            continue
                input('你们击破了机器人的红色水晶！机器人退下阵来！')
                alpha_robot_B = random.randint(0,1)
            if alpha > 0:
                if alpha_punch != 0:
                    x = random.randint(1,4)
                    a = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    b = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    c = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    d = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    e = chr(ord('A') + x - 1)
                    enemy_fight = a+b+c+d+e
                    enemy_fighta = [a,b,c,d,e]
                    zero_att = 0
                    if '零剑' in weapon:
                        zero_att = random.randint(5,50)
                    choose = list(input(f'请选择你对阿尔法的攻击!(5个一组,由五个大写字母构成)'))
                    hurt = 0
                    hurtB = 0
                    chance = 0
                    wrong = 0
                    while wrong == 0:
                        wrong = 1
                        if len(choose) != 5:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[0] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[1] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[2] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[3] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[4] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    else:
                        alpha_fight = random.randint(1,10)
                        cube_act = random.randint(1,10)
                        while chance < 5:
                            f = choose.pop()
                            g = enemy_fighta.pop()
                            if chooseb != 'B':
                                if (f == 'A' and g == 'B') or (f == 'B' and g == 'C') or (f == 'C' and g == 'D') or (f == 'D' and g == 'A'):
                                    hurt += att
                                    chance += 1
                                    if att_choose == 1:
                                        hurt += 5
                                    if cube_act == 1:
                                        hurt -= 50
                                    hurt += item_att
                                    hurt += zero_att
                                    if hucker == 1:
                                        hurt += 10
                                    if '电磁激光枪' in weapon and magic_point >= 10:
                                        hurt += 35
                            if (f == 'D' and g == 'C') or (f == 'C' and g == 'B') or (f == 'B' and g == 'A') or (f == 'A' and g == 'D'):
                                hurtB += 20
                                if alpha_fight <= 3:
                                    hurtB += 5
                                if chooseb == 'B':
                                    hurtB -= Def
                                    hurtB -= blood_stone
                                    if hucker == 1:
                                        hurtB -= 30
                                    if hurtB < 0:
                                        hurtB = 0
                                chance += 1
                                if coat == 1 and random.randint(1,10) == 5:
                                    hurtB = 0
                                else:
                                    health += 10
                            else:
                                chance += 1
                    if hurt < 0:
                        hurt = 0
                    if random.randint(1,20) == 3 and '战争宝石' in item and att_choose == 1:
                        hurt *= 3
                        big_fight += 1
                    if alpha_fight <= 3:
                        hurt *= 1.5
                        hurt = int(hurt)
                    if hide[0] + hide[1] >= random.randint(1,100):
                            hurtB = 0
                    hide[1] = 0
                    health -= hurtB
                    alpha -= hurt
                    item_att = 0
                    choose = input(f'阿尔法的攻击是{enemy_fight}')
                    if cube_act == 1 :
                        choose = input('阿尔法使用了防御!')
                    choose = input(f'你对阿尔法造成了{hurt}点伤害!')
                    if chooseb == 'B':
                        choose = input('因为你选择了防御,所以伤害不计入')
                    choose = input(f'你被敌人扣除了{hurtB}点血')
                    dead_interface()
                    if respawned == 1:
                        break
                else:
                    alpha_punch_B = 0
                    alpha_punch = random.randint(2,9)
                    input('阿尔法利用组合拳向你们攻来！回复三次字母进行抵挡！')
                    hurt = 0
                    hurtB = 0
                    small = 0
                    while alpha_punch_B != 3:
                        alpha_punch_B += 1
                        x = random.randint(1,4)
                        a = chr(ord('A') + x - 1)
                        x = random.randint(1,4)
                        b = chr(ord('A') + x - 1)
                        x = random.randint(1,4)
                        c = chr(ord('A') + x - 1)
                        x = random.randint(1,4)
                        d = chr(ord('A') + x - 1)
                        x = random.randint(1,4)
                        e = chr(ord('A') + x - 1)
                        enemy_fight = a+b+c+d+e
                        enemy_fighta = [a,b,c,d,e]
                        zero_att = 0
                        if '零剑' in weapon:
                            zero_att = random.randint(5,50)
                        choose = list(input(f'请选择你对阿尔法的第{alpha_punch_B}次攻击!(5个一组,由五个大写字母构成)'))
                        chance = 0
                        wrong = 0
                        while wrong == 0:
                            wrong = 1
                            if len(choose) != 5:
                                wrong = 0
                                print('输入错误,请依照格式输入!')
                                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                            elif choose[0] not in {'A','B','C','D'}:
                                wrong = 0
                                print('输入错误,请依照格式输入!')
                                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                            elif choose[1] not in {'A','B','C','D'}:
                                wrong = 0
                                print('输入错误,请依照格式输入!')
                                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                            elif choose[2] not in {'A','B','C','D'}:
                                wrong = 0
                                print('输入错误,请依照格式输入!')
                                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                            elif choose[3] not in {'A','B','C','D'}:
                                wrong = 0
                                print('输入错误,请依照格式输入!')
                                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                            elif choose[4] not in {'A','B','C','D'}:
                                wrong = 0
                                print('输入错误,请依照格式输入!')
                                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        alpha_fight = random.randint(1,10)
                        cube_act = random.randint(1,10)
                        while chance < 5:
                            f = choose.pop()
                            g = enemy_fighta.pop()
                            if chooseb != 'B':
                                if (f == 'A' and g == 'B') or (f == 'B' and g == 'C') or (f == 'C' and g == 'D') or (f == 'D' and g == 'A'):
                                    hurt += att
                                    chance += 1
                                    if att_choose == 1:
                                        hurt += 5
                                    if cube_act == 1:
                                        hurt -= 50
                                    hurt += item_att
                                    hurt += zero_att
                                    if hucker == 1:
                                        hurt += 10
                                    if '电磁激光枪' in weapon and magic_point >= 10:
                                        hurt += 35
                            if (f == 'D' and g == 'C') or (f == 'C' and g == 'B') or (f == 'B' and g == 'A') or (f == 'A' and g == 'D'):
                                hurtB += 20
                                if alpha_fight <= 3:
                                    hurtB += 5
                                if chooseb == 'B':
                                    hurtB -= Def
                                    if hucker == 1:
                                        hurtB -= 30
                                    if hurtB < 0:
                                        hurtB = 0
                                chance += 1
                                if coat == 1 and random.randint(1,10) == 5:
                                    hurtB = 0
                                else:
                                    health += 10
                            else:
                                chance += 1
                        if random.randint(1,20) == 3 and '战争宝石' in item and att_choose == 1:
                            hurt *= 3
                            big_fight += 1
                        if hurt < small:
                            small = hurt
                            hurt = 0
                        choose = input(f'阿尔法的攻击是{enemy_fight}')
                        health -= hurtB
                        input(f'你被扣除了{hurtB}点血量')
                    alpha -= small
            coat = 0
            if alpha <= 0:
                choose = input('您获胜了!')
                CM += 1000
                choose = input(f'你获得了1000个CM币')
                E_cotton += 1
                win = 1
            if respawned == 1:
                respawned = 0
        output('阿尔法后退一步，随即发出了一阵机械的声音。“有点能耐嘛！不过呢，我这副装甲是防御型，我认为用我的攻击型装甲来打你们的话可能会获得更好的效果哦！”')
        output('So上前一步：“所以你现在想要干什么？！”')
        output('阿尔法大笑：“天哪！你居然不知道现在我要干什么吗？麻烦你重做一下小学的阅读理解题吧！我开头就说过我要干掉你们啊！”')
        output('阿尔法随后又发出了一阵机械声，感觉是在嘲笑你们。突然，阿尔法站在地上不动了。')
        output('“死了？”So上前碰了碰，“嗯……这个机器人停摆了，不过我想阿尔法可能只是跑了，所以——”')
        output('So话音未落，突然周围的车厢变成了红色，四周警报迭起：“警报！列车已严重超速！请各位旅客做好应急准备措施，从车门逃逸！”')
        output('“什么情况！”So大叫。')
        output('你会：A：从车门逃出去,B：坐在座位上,C：找机器人帮忙')
        while choose not in {'A','B','C'}:
            output('你会：A：从车门逃出去,B：坐在座位上,C：找机器人帮忙')
        if choose == 'A':
            output('你跑到车门前，车门打不开！')
        elif choose == 'B':
            output('座位开始剧烈摇晃，你感到一阵恶心[HP-10]')
            health -= 10
            dead_interface()
        elif choose == 'C':
            output('机器人全都倒在地上一动不动')
        output('正当你们一筹莫展时，So突然对你说：“那个，我们的列车的力场发生器好像被锁定了，如果我们可以找到这个力场发生器并且摧毁它，我们就可以逃出去了……但愿如此吧。”')
        output('你们现在需要分头寻找力场发生器，但这不是一件容易的事情！')
        output('你会：A：不管他,B：在机器人身上寻找,C：去驾驶室,D：在座位下方寻找')
        go = 0
        while go == 0:
            while choose not in {'A','B','C','D'}:
                output('你会：A：不管他,B：在机器人身上寻找,C：去驾驶室,D：在座位下方寻找')
            if choose == 'A':
                output('不管这事怎么行呢？！')
            elif choose == 'B':
                output('机器人身上没有力场发生器')
            elif choose == 'C':
                output('你们前往驾驶室')
                go = 1
            elif choose == 'D':
                if '遥控器' not in item:
                    choose = input('你在座位下方找到了一个遥控器')
                    item.append('遥控器')
                    view_status()
                else:
                    output('你嘛都没找到')
        output('你们来到一个看着像驾驶室的地方，这里位于车厢最前端，大门已被破坏了，你们很轻易地进了里面，你们发现里面空无一人，一个冒着红光的机器出现在你面前')
        output('“这就是力场发生器？”So说。')
        output('你会：A：摧毁它,B：找找其它的')
        while choose not in {'A','B'}:
            output('你会：A：摧毁它,B：找找其它的')
        choose_a = choose
        lichang = 4
        if choose == 'A':
            mark = 0
            while mark < 3:
                mark = 0
                choose = list(input('请输入你的摧毁方式(五个字母)'))
                x = random.randint(1,4)
                a = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                b = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                c = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                d = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                e = chr(ord('A') + x - 1)
                enemy_fight = a+b+c+d+e
                enemy_fighta = [a,b,c,d,e]
                hurt = 0
                hurtB = 0
                chance = 0
                wrong = 0
                while wrong == 0:
                    wrong = 1
                    if len(choose) != 5:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的摧毁方式!(5个一组,由五个大写字母构成)'))
                    elif choose[0] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的摧毁方式!(5个一组,由五个大写字母构成)'))
                    elif choose[1] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的摧毁方式!(5个一组,由五个大写字母构成)'))
                    elif choose[2] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的摧毁方式!(5个一组,由五个大写字母构成)'))
                    elif choose[3] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的摧毁方式!(5个一组,由五个大写字母构成)'))
                    elif choose[4] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的摧毁方式!(5个一组,由五个大写字母构成)'))
                else:
                    while chance < 5:
                    #快悄悄这个地方,我把chance < 5写成了chance <= 5然后查了一天才查到这个bug
                    #悄悄改为瞧瞧,这是个错别字(划)通假字
                    #快看,这里我复制的前面
                        f = choose.pop()
                        g = enemy_fighta.pop()
                        if f == 'D' and g == 'C' or f == 'C' and g == 'B' or f == 'B' and g == 'A' or f == 'A' and g == 'D':
                            chance += 1
                            mark += 1
                        else:
                            chance += 1
                    health -= hurtB
                    choose = input(f'机器的结构是{enemy_fight}')
                    if mark < 3:
                        choose = input(f'你打破了{mark}个结构,请重试！')
                    else:
                        choose = input('你打破了机器！')
            choose = input('红色的机器发出耀眼的闪光，突然几道激光束向你们发来，你们被击中了！[HP-40]')
            health -= 40
            dead_interface()
            view_status()
            output('“我的天！这不是力场发生器！”So惊叫道，“下面那个才是！”')
            output('你看到红色机器下面还有一个蓝色的装置。')
            lichang = 5
        elif choose == 'B':
            mark = 0
            while mark < lichang:
                mark = 0
                choose = list(input('请输入你的摧毁方式(五个字母)'))
                x = random.randint(1,4)
                a = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                b = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                c = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                d = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                e = chr(ord('A') + x - 1)
                enemy_fight = a+b+c+d+e
                enemy_fighta = [a,b,c,d,e]
                hurt = 0
                hurtB = 0
                chance = 0
                wrong = 0
                while wrong == 0:
                    wrong = 1
                    if len(choose) != 5:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的摧毁方式!(5个一组,由五个大写字母构成)'))
                    elif choose[0] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的摧毁方式!(5个一组,由五个大写字母构成)'))
                    elif choose[1] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的摧毁方式!(5个一组,由五个大写字母构成)'))
                    elif choose[2] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的摧毁方式!(5个一组,由五个大写字母构成)'))
                    elif choose[3] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的摧毁方式!(5个一组,由五个大写字母构成)'))
                    elif choose[4] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的摧毁方式!(5个一组,由五个大写字母构成)'))
                else:
                    while chance < 5:
                    #快悄悄这个地方,我把chance < 5写成了chance <= 5然后查了一天才查到这个bug
                    #悄悄改为瞧瞧,这是个错别字(划)通假字
                    #快看,这里我复制的前面
                        f = choose.pop()
                        g = enemy_fighta.pop()
                        if f == 'D' and g == 'C' or f == 'C' and g == 'B' or f == 'B' and g == 'A' or f == 'A' and g == 'D':
                            chance += 1
                            mark += 1
                        else:
                            chance += 1
                    health -= hurtB
                    choose = input(f'装置的结构是{enemy_fight}')
                    ran = random.randint(1,10)
                    if mark < lichang:
                        choose = input(f'你打破了{mark}个结构,请重试！')
                    if mark >= lichang or ran == 1:
                        choose = input('你打破了装置！')
        output('你们摧毁了蓝色装置，突然列车发出了巨大的响声，灯光暗淡下来，随之传来的是巨大的抖动。')
        output('“快趴下！列车要解体了！”So喊道。')
        output('没等你做好准备，你的身边传来了一阵猛烈的爆炸，你感到自己在不断地下坠。')
        if choose_a == 'A':
            output('这样的感觉持续了好一会儿，你才勉强睁开眼睛，看清自己身在地上，So不见踪影，你衣衫褴褛，身上到处都是碎屑与血迹。你抬头看了看四周，发现你处在一座深蓝色的建筑群里，一群穿着奇装异服的路人正在好奇地围观着你。')
            output('你勉强从地上站起身，一瘸一拐地往前走去，尽量回避周围人的视线。')
            output('走了好一会儿，你看见So就在前面看着一个显示屏，他看上去比你好很多。')
            output('“嗯……你来啦，你咋这样？”So看到你，只是简单地说了句。')
        if choose_a == 'B':
            output('在下坠的同时，你感到一道升力拖住了你，你缓慢降到地上，So也随你一起降落。')
            output('你看了看四周，发现你处在一座深蓝色的建筑群里。')
            output('“这里应该就是P区。”说完，So点开了一个显示屏')
        output('你看向显示屏，发现上面是一个大地图，你会找什么？')
        output('A：比特塔,B：其它地方')
        while choose not in {'A','B'}:
            output('A：比特塔,B：其它地方')
        if choose == 'A':
            output('你在地图上找到了比特塔，发现它离你们并不是很远')
        elif choose == 'B':
            output('你在地图上找到了你们之前去过的所有地方，并没有什么特别的')
        savepoint = 17
    #做个存档点标记
    if savepoint == 17:
        save_data()
        output('你们往前走去，So突然有点恼怒地对你说：“我tm再也不想坐这该死的列车了……”')
        output('你没怎么理会So，这让他有点尴尬')
        if tower == 0:
            output('So转移了个话题继续说：“嗯……我看接下来的谜题一定是那个又恶心又费时的升降门吧……”')
            output('你向前看了看，前面又是一条宽宽的车道，你做了个叹气的动作')
            go = 0
            mark = 0
            while go == 0:
                code = []
                for i in range(7):
                    code.append(chr(ord('0')+random.randint(0,1))+chr(ord('0')+random.randint(0,1))+chr(ord('0')+random.randint(0,1))+chr(ord('0')+random.randint(0,1))+chr(ord('0')+random.randint(0,1))+chr(ord('0')+random.randint(0,1))+chr(ord('0')+random.randint(0,1)))

                for i in range(1):
                    choose = input('请输入七个二进制的数字')
                    wrong = 0
                    while wrong == 0:
                        wrong = 1
                        if len(choose) != 7:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = input('请输入七个二进制的数字')
                        elif choose[0] not in {'0','1'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = input('请输入七个二进制的数字')
                        elif choose[1] not in {'0','1'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = input('请输入七个二进制的数字')
                        elif choose[2] not in {'0','1'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = input('请输入七个二进制数字')
                        elif choose[3] not in {'0','1'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = input('请输入七个二进制的数字')
                        elif choose[4] not in {'0','1'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = input('请输入七个二进制的数字')
                        elif choose[5] not in {'0','1'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = input('请输入七个二进制的数字')
                        elif choose[6] not in {'0','1'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = input('请输入七个二进制的数字')
                    input('升降门密码是'+code[i-1])
                    answer = code[i-1]
                    compare = 0
                    while compare < 7:
                        if answer[compare] == choose[compare]:
                            mark += 1
                        compare += 1
                    if choose == code[i-1]:
                        input(f'你通过了{mark}道升降门')
                    if mark >= 4:
                        input('你通过了升降门阵！')
                        go = 1
                    if mark < 4:
                        mark = 0
                        input('你未能通过升降门阵！')
        else:
            output('你们往前走去，通过了一条宽阔的车道。')
        output('你们继续向前走，来到由错综复杂的高楼组成的一片城区，楼房闪烁着红蓝色的光芒，形形色色的机器人穿行在街道上。[HPmax]')
        health = 300
        output('So看了看一个显示屏，对你说：“这里很难走，我知道一条捷径。”说罢，So拉着你向前跑去，你转了一个又一个弯，一条紫黑色的小巷出现在你面前。')
        output('“这是个迷宫，不过我有地图，很快就能过去。”So对你说。')
        output('你跟着So向前走去，在曲折的紫黑色墙壁间穿行。')
        output('当你向前通过一座墙壁的空隙时，你突然感觉到了有点不对劲，你转过身来看了下后面，一个幽灵出现在你身后。你赶快提醒了So')
        output('幽灵向你们不断地逼近')
        print('战斗开始,对战像素小怪')
        item_att = 0
        t.sleep(0.5)
        cube = 400
        coat = 0
        zero_att = 0
        ghost_att = 0
        magic_point = 0
        ghost_att = 0
        hucker = 0
        z = 0
        win = 0
        a,b,c,d,e = '','','','',''
        while win == 0:
            magic_choose = 0
            att_choose = 0
            item_choose = 0
            while magic_choose == 0 and item_choose == 0:
                chooseb = 'A'
                print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health},像素小怪血量为{cube}')
                choose = input('A,物品B,防御C,魔法D,跳过')
                while choose not in {'A','B','C','D'}:
                    print('请做出你的选择')
                    choose = input('A,物品B,防御C,魔法D,跳过')
                if choose == 'A':
                    choose = input(f'你现在可使用的物品有{fight_item},请从1开始输入序号以选择使用的物品')
                    if choose not in {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'}:
                        choose = input('物品序号输入错误!')
                    else:
                        choose = int(choose)
                        if choose > len(fight_item):
                            choose = input('物品序号输入错误!')
                        else:
                            choose -= 1
                            check = fight_item[choose]
                            item_find()
                            if check == '魔法炸药':
                                choose = input('你对对方造成了100点伤害!但你也不小心受到了30点伤害')
                                health -= 30
                                cube -= 100
                                dead_interface()
                                if respawned == 1:
                                    break
                            if check == '坚硬冰棍':
                                choose = input('你使用了坚硬冰棍!敌方的HP降低了100点!')
                                cube -= 100
                            if check in fight_item and check in item:
                                item.remove(check)
                                fight_item.remove(check)
                        if health > 300:
                            health = 300
                if choose == 'B':
                    choose = input('你选择了防御!')
                    magic_point += 40
                    magic_choose = 1
                    if magic_point >= 100:
                        magic_point = 100
                    chooseb = 'B'
                if choose == 'C':
                    choose = input(f'A：治疗魔法（{health_point}）B：战斗魔法（70）C：黑暗魔法（？）D：暗蓝卫衣（30-50）')
                    while choose not in {'A','B','C','D'}:
                        print('请做出你的选择')
                        choose = input(f'A：治疗魔法（{health_point}）B：战斗魔法（70）C：黑暗魔法（？）D：暗蓝卫衣（30-50）')
                    else:
                        if choose == 'A':
                            if magic_point < health_point:
                                choose = input('你的魔法值不够!')
                                magic_choose = 0
                            if magic_point >= health_point:
                                choose = input(f'你使用了治疗法术!你的血量回复了{health_plus}点!')
                                health += health_plus
                                magic_choose = 1
                                magic_point -= 30
                            if health > 300:
                                health = 300
                                magic_choose = 1
                        if choose == 'B':
                            if magic_point < 70:
                                choose = input('你的魔法值不够!')
                                magic_choose = 0
                            if magic_point >= 70:
                                choose = input('你使用了战斗法术!你的攻击提高了5点,持续一回合!')
                                att_choose = 1
                                magic_choose = 1
                                magic_point -= 70
                        if choose == 'C':
                            choose = input('l͓̩̫̘͙͔̯͖̟̤̓͊̑̌́̂̆̚ò̥̪̭̱̰̝̒͂̄͋̿̏͆́̚c͍̲͇͚̖̬͈̪͙̳͌̉́̃k̪̥̱̝̱̑̈́̏̽͗̊̈́͂̀̍e̞͎̩̜̱̩͚̤̊͌̀̀d̠̖̞̝̙̪̟̞̐͛̈̊̀͂̄͌̓̏͌̓ͅ')
                            magic_choose = 0
                        if choose == 'D':
                            if magic_point < 50:
                                choose = input('你的魔法值不够!')
                            elif magic_point >= 50:
                                magic_point -= random.randint(30,50)
                                coat = 1
                                magic_choose = 1
                                choose = input('你使用了暗蓝卫衣!你的闪避率提高了10％,持续一回合!')
                        choose = 0
                if choose == 'D':
                    choose = input('你跳过了你的回合')
                    magic_choose = 1
            else:
                magic_choose = 1
            if random.randint(1,2) == 1:
                choose = input('请输入本回合你想自定义的ATT，仅限1-50之间')
                while choose.isalpha() or choose == '':
                    choose = input('请输入本回合你想自定义的ATT，仅限1-50之间')
                choose = int(choose)
                if 1 <= choose <= 50:
                    z = random.randint(1,2)
                    ghost_att = choose
                    if z == 1:
                        input(f'恭喜你在本回合战斗中获得了[{ghost_att}]ATT！')
                    elif z == 2:
                        input(f'恭喜你在本回合战斗中施舍了对手[{ghost_att}]ATT!')
                else:
                    input('你输的什么玩意儿，想挨揍吗？[HP-50]')
                    health -= 50
                    dead_interface()
                    if respawned == 1:
                        break
            x = random.randint(1,4)
            a = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            b = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            c = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            d = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            e = chr(ord('A') + x - 1)
            enemy_fight = a+b+c+d+e
            enemy_fighta = [a,b,c,d,e]
            cube_act_B = random.randint(1,7)
            if cube_act_B == 1:
                choosec = input('幽灵蹭着迷宫墙')
            if cube_act_B == 2:
                choosec = input('幽灵不喜欢“像素小怪”这个称呼')
            if cube_act_B == 3:
                choosec = input('幽灵跟你玩起了躲猫猫')
            if cube_act_B == 4:
                choosec = input('你认为这幽灵有些可憎')
            if cube_act_B == 5:
                choosec = input('战斗似乎变得有点无趣')
            if cube_act_B == 6:
                choosec = input('So在寻找吃豆人”')
            if cube_act_B == 7:
                choosec = input('So希望尽快结束战斗')
            if '零剑' in weapon:
                zero_att = random.randint(5,50)
            if '混乱护盾' in weapon:
                health += random.randint(5,15)
            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
            hurt = 0
            hurtB = 0
            chance = 0
            wrong = 0
            while wrong == 0:
                wrong = 1
                if len(choose) != 5:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                elif choose[0] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                elif choose[1] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                elif choose[2] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                elif choose[3] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                elif choose[4] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
            else:
                cube_act = random.randint(1,2)
                while chance < 5:
                    f = choose.pop()
                    g = enemy_fighta.pop()
                    if chooseb != 'B':
                        if (f == 'A' and g == 'B') or (f == 'B' and g == 'C') or (f == 'C' and g == 'D') or (f == 'D' and g == 'A'):
                            hurt += att
                            if z == 1:
                                hurt += ghost_att
                            chance += 1
                            if att_choose == 1:
                                hurt += 5
                            if cube_act == 2:
                                hurt -= 7
                            hurt += item_att
                            hurt += zero_att
                            if hucker == 1:
                                hurt += 10
                            if '电磁激光枪' in weapon and magic_point >= 10:
                                hurt += 35
                    if (f == 'D' and g == 'C') or (f == 'C' and g == 'B') or (f == 'B' and g == 'A') or (f == 'A' and g == 'D'):
                        hurtB += 15
                        if z == 2:
                            hurtB += ghost_att
                        if chooseb == 'B':
                            hurtB -= (Def+blood_stone)
                            if hucker == 1:
                                hurtB -= 30
                        chance += 1
                        if coat == 1 and random.randint(1,10) == 5:
                            hurtB = 0
                        else:
                            health += 10
                    else:
                        chance += 1
                if hurtB < 0:
                    hurtB = 0
                if hurt < 0:
                    hurt = 0
                coat = 0
                if random.randint(1,20) == 3 and '战争宝石' in item and att_choose == 1:
                    hurt *= 3
                    big_fight += 1
                if hide[0] + hide[1] >= random.randint(1,100):
                    hurtB = 0
                hide[1] = 0
                item_att = 0
                cube -= hurt
                health -= hurtB
                choose = input(f'像素小怪的攻击是{enemy_fight}')
                if cube_act == 2:
                    choose = input('像素小怪使用了防御!')
                if chooseb != 'B':
                    choose = input(f'你对敌方造成了{hurt}点伤害!')
                    hurt = 0
                if chooseb == 'B':
                    choose = input('因为你选择了防御,所以伤害不计入')
                choose = input(f'你被敌人扣除了{hurtB}点血')
                ghost_att = 0
                dead_interface()
                if respawned == 1:
                    break
                hurtB = 0
                att_choose = 0
            if cube <= 0:
                choose = input('您获胜了!')
                CM_get = random.randint(70,140)
                CM += CM_get
                choose = input(f'你获得了{CM_get}个CM币')
                win = 1
        if respawned == 1:
            respawned = 0
            continue
        output('你们击败了幽灵，幽灵咆哮着跑走了，你们继续前进。')
        output('你们继续穿过迷宫，在一座墙下你看见了两个奇形怪状的机器人，一个机器人头是吃豆人，身子却是一座拿着斧子的炮台，一个机器人头是国际象棋的骑士，但身子是一副履带。')
        output('你会A：与吃豆人交谈,B：与骑士交谈,C：不管他')
        while choose not in {'A','B','C'}:
            output('你会A：与吃豆人交谈,B：与骑士交谈,C：不管他')
        if choose == 'A':
            output('吃豆人说：“劳资已经被困在这里三年了，每天都有一堆烦人的幽灵打扰我，没一个玩家能通过去，烦！”')
        elif choose == 'B':
            output('骑士说：“我不是这里的人，可这群机器人强加了我一个履带……他们让我造第三十个机……算了你不需要知道。”')
        if fun == 33:
            output('你向前走去，走到了一条阴森的小巷中，旁边似乎有一扇门，你发现So不见了踪影')
            output('进去吗：A：不进,B：进去')
            while choose not in {'A','B'}:
                output('进去吗：A：不进,B：进去')
            if choose == 'A':
                output('你松了口气')
            else:
                output('门内漆黑一团，一切都化为虚无')
                output('你奋力地奔跑，跑不到尽头，奋力地挣扎，却无法挣脱黑暗的束缚，奋力地哭喊，却听不到发出的声音')
                output('最后，你完全放弃了抵抗，缓缓地坐了下来，或者，你感觉你坐了下来')
                output('什么，感觉？感觉也不存在，或者，你完全无法理解这里是什么，换句话说，理解在这里也用不上')
                output('你的精神被某种不明物体抚摸着，玩弄着，你感觉这就是黑暗……或者，死亡')
                output('你已经没有思考能力了')
                output('无尽的黑暗')
                output('超越黑暗的黑暗')
                output('在这黑暗中，似乎还剩下什么，一种你完全无法理解的存在，是记忆吗？')
                output('你似乎看到了黑暗中迸发出了一道光。')
                output('在那道光中，你重生了。')
                output('视野再度恢复了光明，你发现你坐在地上，转身看看侧面，门已经消失。')
                output('你松了口气')
        output('你走了一会儿，来到了一条比较开阔的道路上，你的前面有两只灰色的幽灵在漫无目的地走着')
        output('你会：A：交谈,B：不管他')
        while choose not in {'A','B'}:
            output('你会：A：交谈,B：不管他')
        if choose == 'A':
            output('灰色幽灵突然撞向你[HP-25]')
        else:
            choose = list(input('幽灵突然向你撞来，请回复五个字母以穿过幽灵'))
            x = random.randint(1,4)
            a = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            b = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            c = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            d = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            e = chr(ord('A') + x - 1)
            enemy_fight = a+b+c+d+e
            enemy_fighta = [a,b,c,d,e]
            hurt = 0
            hurtB = 0
            chance = 0
            wrong = 0
            while wrong == 0:
                wrong = 1
                if len(choose) != 5:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                elif choose[0] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                elif choose[1] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                elif choose[2] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                elif choose[3] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                elif choose[4] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
            else:
                while chance < 5:
                    f = choose.pop()
                    g = enemy_fighta.pop()
                    if f == 'D' and g == 'C' or f == 'C' and g == 'B' or f == 'B' and g == 'A' or f == 'A' and g == 'D':
                        hurtB += 15
                        if z == 2:
                            hurtB += ghost_att
                        chance += 1
                    else:
                        chance += 1

                health -= hurtB
                choose = input(f'幽灵的进攻方式是{enemy_fight}')
                choose = input(f'你被扣除了{hurtB}点血量')
                dead_interface()
                if respawned == 1:
                    respawned = 0
                    continue
        if shop_talk == 2:
            shop_talk = 3
        output('你们穿过幽灵，前方出现了一条岔路口，不过左边的岔路被垃圾挡住了。')
        output('“嗯，通过这个岔路口往前走就是像素广场，从那里可以直接到达比特区。”So说')
        #然后我们来和棉花糖合（
        output('你会：A：向前走,B：向右拐')
        while choose not in {'A','B'}:
            output('你会：A：向前走,B：向右拐')
        if choose == 'B':
            output('你们向右走去，前面是一条漆黑的小巷。走了一会儿，你来到了一片空地。你身旁的墙上贴着一张海报')
            choose = input('你会：A：看看海报,B：和So交谈')
            while choose not in {'A','B'}:
                output('你会：A：看看海报,B：和So交谈')
            if choose == 'A':
                output('海报上画着一个你不认识的机器人，看起来有点像一个电视节目的宣传图片')
            elif choose == 'B':
                output('So有点懊恼：“这地方是个死胡同，我们走吧。”')
            output('你们刚想离开，突然，你发现原本阴暗的四周突然出现了道道彩色的闪光，周围突然开启了一群彩色的弹窗，一道像聚光灯一样的强烈白光笼罩了你们。当你突然感到有点晕眩时，一个声音传来：')
            output('“观众朋友们晚上好！Tis COSH！！！欢迎各位收看我们的——晚——间——节——目！！！今天的节目内容是——0女士和SO S先生的惨烈修——题——大——赛！！！”一个长相奇怪的机器人从墙壁上一个突然打开的缺口钻了出来。')
            output('“等等！你是谁！”So有点吃惊地问道“你怎么知道——”')
            output('“我说过啦！Tis COSH！！！我就是——大名鼎鼎的——成功娱乐主持人的模范——专家——教授——COSH！！！叫我双曲余弦吧同志——”')
            output('叫做COSH的机器人突然怪笑了一下，随后说：“我不仅知道你们，还知道昵称、赛恩思、黑客们、甚至——你们的CV——星空、白羽、代数……总之，别傻傻地问问题！接下来你将看到——”')
            output('COSH又顿了顿：“史上最经典最激动人心最有趣的答题游戏——有你们这俩完美无缺的嘉宾，有那么多鼎力支持的观众，再加上——我这个神一般的完美主持人，我们的节目——一定会——一定会——除了……”')
            output('COSH的眼神突然暗淡下来：“我们的收视率，惨淡啊！！惨淡啊！！我们的努力都会白费！！！观众们总是喜欢那种，完全没有营养的，小孩子就能做的那种超简单答题游戏！！！哈哈！他们问参赛者负二的绝对值是多少！！！我这种——精心制作的高质量作品已经无人问津了……只能被打进——阴森的——小巷！但！我是一个重视工匠精神的人！！！我的作品绝对是最棒的！！这是因为，我们的嘉宾，完全真实——完全无辜——完全可怜！！！哈哈哈！我们一定……”')
            output('在COSH一连串的大笑中，So小声在你旁边嘀咕着：“这人……可能有点精神问题。”')
            output('“好了好了，废话少说，让我们开始答题节目哦！我们可爱的Zero……”COSH转向你，你注意到他的手上出现了一把电磁激光枪。')
            output('“要是答不上来的话……”COSH怪笑着向你们靠近。“ZeroZeroZero……小心——小心大难0头哦，哈哈哈……”')
            cosh_A = 1
            output('剧烈的光束把你们笼罩着。')
            print('战斗开始,对战COSH')
            output('COSH说：“好啦，观众朋友们！本次的节目——劲爆的答题对战现在开始！')
            Q_and_A = {'COSH节目的性质是什么？\nA：政治 B：娱乐 C：科普 D：魔法': 'B',
                   '黑客村庄在哪？\nA：城市 B：山城 C：森林 D：迷宫': 'C',
                   'SCI的编号是什么？\nA：S28I738368 B：S28I738398 C：S281738398 D：S281736368': 'C',
                   '力场门的通过方式是什么？\nA：回复字母通过 B：回复数字通过 C：直接通过 D：关闭力场后通过': 'D',
                   '请数出以下字母的数量：COSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOS\nA：134 B：167 C：191 D：':'C',
                   '为什么是Tis COSH？\nA：自我介绍罢了 B：Tetris！ C：T代表【，i代表《，s代表¥ D：观众！！！收视率增长！！！':'A',
                   '能量饮料含有以下哪种成分？\nA：魔法核心 B：生命晶体 C：战斗宝石 D：纯净法术':'D',
                   '下面哪个词最让人害怕！\nA：疾病 B：见证 C：射线 D：魔王':'B', #记住，光光，要杀，我了
                   '速算：284929381+281738368=？A：566667749 B：566667748 C：566667747 D：566667746':'A',
                   '填空：规则，___，魔法的障碍，是你不可逾越的障碍\nA：冒险 B：科技 C：时间 D：死亡':'B',
                   '你希望我们的收视率上升吗？\nA：希望 B：希望 C：希望 D：希望':'A'}
            cosh_blood = 0
            for i in Q_and_A.keys():
                print(f'现在请您选择您的行动')
                choose = input('A,物品B,魔法C,跳过')
                while choose not in {'A','B','C'}:
                    print('请做出你的选择')
                    choose = input('A,物品B,魔法C,跳过')
                if choose == 'A':
                    choose = input(f'你现在可使用的物品有{fight_item},请从1开始输入序号以选择使用的物品')
                    if choose not in {'1','2','3','4','5','6','7','8','9','10'}:
                        choose = input('物品序号输入错误!')
                    else:
                        if choose > len(fight_item):
                            choose = input('物品序号输入错误!')
                        else:
                            choose -= 1
                            input('“什么？你还有时间吃东西？看来你想吃点苦头了”')
                            check = fight_item[choose]
                            if check == '冰棍':
                                choose = input('你使用了冰棍!你的HP减少了15点!')
                                health -= 15
                            if check == '杆草':
                                choose = input('你使用了杆草!你的HP减少了20点!')
                                health -= 20
                            if check == '流油果':
                                choose = input('你使用了流油果!你的HP减少了40点!')
                                health -= 40
                            if check == '花色汉堡':
                                choose = input('你使用了花色汉堡!你的HP减少了50点!')
                                health -= 50
                            if check == '方块糖果':
                                choose = input('你使用了方块糖果!你的HP减少了40点!')
                                health -= 40
                            if check == '红桃蛋糕':
                                choose = input('你使用了红桃蛋糕!你的HP减少了100点!')
                                health -= 100
                            if check == 'CRD硬糖':
                                choose = input('你使用了CRD硬糖!你的HP减少了14点!')
                                health -= 14
                            if check == '冰淇淋':
                                choose = input('你使用了冰淇淋!你的HP减少了40点!')
                                health -= 40
                            if check == '五彩糖':
                                choose = input('你使用了五彩糖!你的HP减少了20点!')
                                health -= 20
                            if check == '能量饮料':
                                choose = input('你使用了能量饮料!你的HP减少了20点!')
                                health -= 20
                            if check == '冰冻面包':
                                health -= 50
                                choose = input('你使用了冰冻面包!你的HP减少了50点!')
                            if check == '电路板寿司':
                                health -= 50
                                choose = input('你使用了电路板寿司!你的HP减少了50点!')
                            if check == 'H-饼干':
                                plus = random.randint(4,300)
                                choose = input(f'你使用了H-饼干!你的HP减少了{plus}点!')
                                health -= plus
                            if check == '黑客三周年限定蛋糕':
                                choose = input('你的血量减少了250点!')
                                health -= 250
                            if check == '电棉':
                                E_cotton -= 1
                                choose = input('你吞下了一大坨...电子蛇的排泄物，你的HP减少了1点！')
                                health -= 1
                            if check == 'COSH血包':
                                plus = fight_item.count('COSH血包')*5
                                if plus >= 150:
                                    plus = 150
                                choose = input(f'你使用了所有COSH血包,你本轮将不会受到伤害!')
                                cosh_blood = 1
                                for i in range(fight_item.count('COSH血包')-1):
                                    item.remove('COSH血包')
                                    fight_item.remove('COSH血包')
                                
                        dead_interface()
                        if respawned == 1:
                            respawned = 0
                        if health > 240:
                            health = 240
                if choose == 'B':
                    choose = input('A：查看, B：求饶')
                    while choose not in {'A','B'}:
                        print('请做出你的选择')
                        choose = input('A：查看, B：求饶')
                    else:
                        if choose == 'A':
                            if '战争宝石' in item:
                                print(f'您的HP为{health},攻击力为{att},防御力为{Def+blood_stone},防御率为50%,CM币为{math.floor(CM/10)},COSH的HP为{cube},攻击力为?,防御力为{random.randint(1937273828810,1937273828820)},防御率为100%,CM币为0')
                            else:
                                print(f'您的HP为{health},攻击力为{att},COSH的HP为{cube},攻击力为?')
                        if choose == 'B':
                            input('COSH说：“太棒了！！！观众对这么可爱的嘉宾一定会过于兴奋的！！！”')
                            if random.randint(0,1) == 1:
                                input('COSH很高兴，给你扔了个补血包（获得【COSH血包】）')
                                item.append('COSH血包')
                                fight_item.append('COSH血包')
                
                        choose = 0
                if choose == 'C':
                    choose = input('你跳过了你的回合')
                if i != '请数出以下字母的数量：COSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOSHCOS\nA：134 B：167 C：191 D：':
                    print(i)
                else:
                    if random.randint(1,100) <= 33:
                        print(i+'333')
                    else:
                        print(i+'202')
                starttime = t.time()
                choose = input('请选择：')
                if i != '你希望我们的收视率上升吗？\nA：希望 B：希望 C：希望 D：希望':
                    endtime = t.time()
                    if cosh_blood != 1:
                        cosh_blood = 0
                        if endtime-starttime >= 30:
                            input('什么——你想让观众老死吗？扣你血量！【HP-50】')
                            health -= 50
                        else:
                            if choose == Q_and_A[i]:
                                input(['你戳戳戳戳——戳中了正确选项','很遗憾！！你——答对了！','你以完全逆天——的方式获得了正确选项！'][random.randint(0,2)])
                            else:
                                input(['嗨，我就知道！！！你将被扣除血量！','你怎么能答错呢？！！手抖害人是吗！','嘿嘿嘿——可恶啊，观众们对你——失望啦！'][random.randint(0,2)])
                                health -= 30
                    else:
                        cosh_blood = 0
                        if choose == Q_and_A[i]:
                            input(['你戳戳戳戳——戳中了正确选项','很遗憾！！你——答对了！','你以完全逆天——的方式获得了正确选项！'][random.randint(0,2)])
                        else:
                            input(['嗨，我就知道！！！你将被扣除血量！','你怎么能答错呢？！！手抖害人是吗！','嘿嘿嘿——可恶啊，观众们对你——失望啦！'][random.randint(0,2)])
                            cosh_blood = 0
                else:
                    while choose not in {'A','B','C','D'}:
                        choose = input('错误，请重新选择')
                    input('收视率？！收视率？收视率！你真的希望那东西上升吗？！！！')
                    input('哎孩子，我看你也就是个孩子而已？你不知道，这世界有多——多——多多多的复杂！！！你不知道！！！这个娱乐至死的时代下——收视率是多么恶心多么下贱多么流氓的东西！！！啊孩子，我觉得你已经不需要这参加这个节目了，我们走吧。')
                    input('COSH看着你们，说：“好啦！既然节目已经结束，我们就没必要多讲啦！！！我们Bye！Bye！')
                    input('周围的灯光突然暗淡下来，COSH随着一个平台降到地下。')
                    input('“我们赶快跑吧。”So对你说。')
                    input('你们原路返回，当你快走出小巷时，你突然瞥见一个小小的弹窗，上面写着：\n“我很看好你，你快来像素大街2号”')

        if shop_talk == 3:
            shop_talk == 4
        output('你们继续向前走，前方的道路一下子宽敞起来，你们的面前出现一座巨大的广场。')
        output('“这里可以找到能直接走到比特塔的步行道。”So对你说。“我们快点走吧。”')
        go = 0
        another_go = 0
        fix = 0
        nc = 0
        while another_go == 0:
            while go == 0:
                while choose not in {'A','B'}:
                    output('你会：A：寻找步行道,B：去广场其它地方')
                    output('你会：A：寻找步行道,B：去广场其它地方')
                if choose == 'A':
                    output('你在广场四处找了找，毫不费力地找到了一个力场门，力场门上标着：“前方可到达比特高塔。”然而力场门是关着的，你找不到打开的方法')
                    choose = input('你会：A：去问问其他人,B：去广场其它地方')
                    while choose not in {'A','B'}:
                        output('你会：A：去问问其他人,B：去广场其它地方')
                    if choose == 'A':
                        output('你找到了一个机器人，机器人说：“这些力场门是经常出现问题，很可能是某些人在搞恶作剧，建议你去维修室看看……哦你好像没有权限的样子。')
                        fix = 1
                    elif choose == 'B':
                        go = 1
                elif choose == 'B':
                    go = 1
            output('你来到了一座大商场里。')
            aanother_go = 0
            while aanother_go == 0:
                if fix == 1 and nc == 0:
                    act = 0
                    output('你会：A：去买东西,B：与人交谈,C：找游戏厅,D：去维修室,E：离开')
                    while choose not in {'A','B','C','D','E'}:
                        output('你会：A：去买东西,B：与人交谈,C：找游戏厅,D：去维修室,E：离开')
                    act = ord(choose) - 64
                elif fix == 0 and nc == 0:
                    output('你会：A：去买东西,B：与人交谈,C：找游戏厅,D：离开')
                    while choose not in {'A','B','C','D'}:
                        output('你会：A：去买东西,B：与人交谈,C：找游戏厅,D：离开')
                    if choose == 'A':
                        act = 1
                    if choose == 'B':
                        act = 2
                    if choose == 'C':
                        act = 3
                    if choose == 'D':
                        act = 5
                elif fix == 0 and nc == 1:
                    output('你会：A：去买东西,B：与人交谈,C：离开')
                    while choose not in {'A','B','C'}:
                        output('你会：A：去买东西,B：与人交谈,C：离开')
                    if choose == 'A':
                        act = 1
                    if choose == 'B':
                        act = 2
                    else:
                        act = 5
                else:
                    output('你会：A：去买东西,B：与人交谈,C：去维修室,D：离开')
                    while choose not in {'A','B','C','D'}:
                        output('你会：A：去买东西,B：与人交谈,C：去维修室,D：离开')
                    if choose == 'A':
                        act = 1
                    if choose == 'B':
                        act = 2
                    if choose == 'C':
                        act = 4
                    if choose == 'D':
                        act = 5
                if act == 1:
                    output('你来到一座超市，这里的人实在太多了，把你弹了出去。')
                elif act == 2:
                    output('你试图找人交谈，这里的人实在太多了，没人理你')
                elif act == 3:
                    output('你并不喜欢游戏，但还是发现了这里的游戏厅，游戏厅内摆放着许多街机，许多人在令人眩晕的灯光与音乐中操作着各式各样的操纵杆。')
                    output('你会：A：随便玩一个街机,B：去人最多的街机看看,C：离开')
                    while choose not in {'A','B','C'}:
                        output('你会：A：随便玩一个街机,B：去人最多的街机看看,C：离开')
                    if choose == 'A':
                        choose = input('你来到了一个称为“怪兽大战”的街机前，街机上立即出现字幕：\n请登录或者使用游客模式！')
                        view_status()
                        output('你由于害怕被侦测到，使用了游客模式，字幕立即改变')
                        output('请选择你想进行对战的对象！')
                        output('你的面前出现了五个附有文字说明的图片。')
                        output('请选择你的对手，花费20CMB进入游戏！')
                        go_B = 0
                        while go_B == 0:
                            if CM >= 20:
                                choose = input('A：CAR-XXX（进入玩具车战）\nB：FLY-XXX（进入飞行器战）\nC：MCE-XXX（进入机械臂战）\nD：ELE-XXX（进入电子蛇战）\nE：1UP-XXX（进入幽灵战）\nF：离开')
                                while choose not in {'A','B','C','D','E','F'}:
                                    choose = input('A：CAR-XXX（进入玩具车战）\nB：FLY-XXX（进入飞行器战）\nC：MCE-XXX（进入机械臂战）\nD：ELE-XXX（进入电子蛇战）\nE：1UP-XXX（进入幽灵战）\nF：离开')
                                    view_status()
                            else:
                                choose = input('A：离开')
                                while choose not in {'A'}:
                                    output('A：离开')
                                choose = 'F'
                            if choose == 'A':
                                CM -= 20
                                car_fight()
                            elif choose == 'B':
                                fly_fight()
                                CM -= 20
                            elif choose == 'C':
                                CM -= 20
                                arm_fight()
                            elif choose == 'D':
                                CM -= 20
                                input('维修中（恼）')
                            elif choose == 'E':
                                input('维修中（恼）')
                            else:
                                go_B = 1
                    elif choose == 'B':
                        nc = 1
                        output('你来到了许多像滚筒洗衣机一样的机器前，这里人非常多，看来你是无法加入游戏了。')
                        output('这时，你前面的So突然瞪大了眼睛：“这？这？！昵称！！！”')
                        output('你看见昵称站在一台街机前飞速地敲打着从机器中心飞出的物体，引起了周围其他人一阵阵的议论声。')
                        output('昵称也注意到了你们，她赶快跑了出来：“So！！！你们也在这里啊！！”')
                        output('So有点担心地问道：“你还好吗……”')
                        output('“我嘛……赛恩思关了我一阵，好像是翻了什么东西来着，然后就把我送到了这里，把前面一大堆排队的人挤下来让我……打游戏！居然是最新版的miamia！不过这游戏真简单，                                       我随便打了几盘就拿下了那什么悖论来着……反正……”')
                        output('昵称意识到自己有些滔滔不绝，赶快闭上了嘴。')
                        output('“你没事吧。”So问。')
                        output('“我没事呢。”昵称回答。')
                        output('“没事就好，我快担心死了。”So有点颤抖地说道。')
                        output('“我也很担心……”昵称有些哽塞')
                        output('你赶快转过身，过了一会儿才回头，昵称和So两人已经往外走了，你在后面慢慢地跟着。')
                elif act == 4:
                    if nc == 0:
                        output('保安检查了你们，“你们还没有权限，我不会给你们打开维修室的力场门的。')
                        output('你们只好暂时离开维修室')
                    elif nc == 1:
                        output('保安仔细打量你们：“这位……猫？虽然我不知道什么情况，但她的权限在我之上，我同意给你们开门。”')
                        output('保安拿出一个蓝色按钮，维修室的门随即打开，保安跟着你们进入了维修室。')
                        output('So把力场门的情况和保安讲了一遍，保安在电脑前捣鼓了一阵，然后对你们说：“现在可以了，你们走吧。”')
                        output('你们来到之前的力场门前，发现门已经打开了。')
                        output('“我们走吧。”So说')
                        another_go = 1
                        aanother_go = 1
                elif act == 5:
                    aanother_go = 1
                    go = 0
        output('你们来到一座天桥上，这座天桥的地板是由力场构成的。因为地板透明，你们可以俯瞰下面的城市。')
        output('So和昵称一路上都在热切地交谈，你觉得你没有必要参与。')
        output('这时，你的前面凭空出现了几个升降门！')
        output('“哦我的天，不要这样！”So用疲惫的语气喊道。')
        output('你会：A：直接通过,B：待会通过')
        while choose not in {'A','B'}:
            output('你会：A：直接通过,B：待会通过')
        if choose == 'A':
            output('你直接冲过去，却被突然升起的升降门顶飞了好远[HP-30]')
            health -= 30
            dead_interface()
            if respawned == 1:
                respawned = 0
                continue
        elif choose == 'B':
            output('昵称突然说道：“让我试试……”')
            output('昵称的身边出现了几个蓝色的显示屏，这些显示屏飞快地转动着，最后变成了红色。这时，所有的升降门都凭空消失了，就像突然关掉的3D投影。')
            output('你们通过了升降门')
        output('你们走了一段路，前面出现了许多激光发射器，红色的激光和蓝色的激光组成了一道道激光阵。')
        output('“这些激光……如果跑得足够快，造不成什么威胁……”昵称说。')
        output('你会：A：跑过去,B：留在原地')
        while choose not in {'A','B'}:
            output('你会：A：跑过去,B：留在原地')
        if choose == 'A':
            output('你飞奔过去，然而还是被激光扫射到了。[HP-50]')
            health -= 50
            dead_interface()
            if respawned == 1:
                respawned = 0
                continue
            output('“害，我还没说完呐……”昵称说')
        elif choose == 'B':
            output('“……可是，我有全部关掉他们的方法。”昵称说着，拿出一个小小的遥控器，按下了上面的两个按钮，激光阵顿时消失不见。')
            output('“昵称……你的权力已经这么高了？”So问')
            output('“嗯……要问赛恩思。”昵称轻轻地回答')
        output('随着你们的前进，周围的景象变成了绿色，外面的世界充满了代码的质感。')
        output('路上时不时地出现了一些你们之前见到过的敌人，他们看到了昵称，掉头就走，有一些胆子大的在你们面前绕了几圈才离开。')
        output('你们在一座高塔之前停了下来')
        output('“这里就是比特塔了。”So说。“我们快进去。”')
        output('“你想进比特塔吗？So？”昵称突然说。')
        output('“什么？”So似乎被吓到了。')
        output('“哈哈，比特塔是赛恩思列出的唯一禁地，我们想轻易进去估计是很难的。”昵称说。')
        output('“这……确实，但我们总该……”')
        output('“你先等等。”昵称说着向前跑去，来到一个看起来很小的力场门前，门前摆放着一台奇形怪状的机器，上面绑着五个红色的气球。')
        output('“赛恩思给我看过这个机器，为了净化比特塔的来人，赛恩思亲手设计了一个超难谜题，五个气球分别有红蓝绿三种颜色，用0、1、2代替，按下这些按钮可以改变气球的颜色，以红、蓝、绿、红的顺序改变。按钮A控制1、4号气球，按钮B控制1、2、3号气球，按钮C控制2、3、4号气球，按钮D控制1、3、5号气球。而按钮F，按下它可以恢复初始状态。你必须把这些气球全部变成绿色的，才能打开力场门……可惜我是没有成功过。”')
        output('So对昵称如此的滔滔不绝有点惊奇，而你已走到机器前。')
        go = 0
        tip = 0
        a,b,c,d,e = 0,0,0,0,0
        while go == 0:
            output('你会按下哪个按钮？(A-1-4,B-1-2-3,C-2-3-4,D-1-3-5)')
            while choose not in {'A','B','C','D','E','F'}:
                output('你会按下哪个按钮？(A-1-4,B-1-2-3,C-2-3-4,D-1-3-5)')
            if choose == 'A':
                a += 1
                d += 1
            elif choose == 'B':
                a += 1
                b += 1
                c += 1
            elif choose == 'C':
                b += 1
                c += 1
                d += 1
            elif choose == 'D':
                a += 1
                c += 1
                e += 1
            if choose == 'E' and tip == 0:
                if b != 0:
                    input('你瞥了一下旁边的So，So打着哈欠看着你，说：“这个谜题看上去是无解的，不过呢……我的“暗蓝卫衣”可以改变这系统里的一个内容，不能再多了。等时机成熟时，我的“暗蓝卫衣”可以使红色的第二个气球直接变成绿色。”')
                elif b == 0:
                    tip = 1
                    input('So使用了暗蓝卫衣，第二个气球变成了绿色！')
                    input('“接下来应该就没什么难度了”So继续打着哈欠')
                    b = 2
            if a == 3:
                a = 0
            if b == 3:
                b = 0
            if c == 3:
                c = 0
            if d == 3:
                d = 0
            if e == 3:
                e = 0
            now = str(a)+str(b)+str(c)+str(d)+str(e)
            print(f'现在气球的状态为{now}')
            if now == '22222':
                input('你通过了谜题！')
                go = 1
        output('当你把正确地把气球改变颜色的同时，力场随之关闭，你们赶快通过了力场门。')
        output('你们的前面出现了一条灰绿色的大道，这条大道通向你们前方那座高塔')
        output('“这就是比特塔，只不过……”昵称说道，她的双手突然向前伸去，原本空旷的道路上突然多出了许多蓝色光道组成的机器。')
        output('“这些是3D投影，没有威胁，但是如果碰到了他们，就会触发比特塔里的武器，所以我们要多加注意……”')
        output('“等一下，比特塔里有武器吗？”So问。')
        output('“有啊，怎么啦？”昵称回答。')
        output('“看来小天这点说得没错，比特塔里面确实有很重要的东西……”So小声嘀咕着。')
        output('你们小心翼翼地向前走去，一直走到了比特塔的门口。')
        output('“我们……可以先不进去，如果想的话，可以在这里直接叫车前往能去的地方……”昵称说道。')
        output('“啥？我对这里的交通工具已经没有半点信任了……”So有点恼火地回答。')
        savepoint = 18
    #做个存档点标记
    if savepoint == 18:
        save_data()
        output('你会：A：进比特塔门,B：叫车')
        go = 0
        #这里是目前最********的一个东西了
        while go == 0:
            while choose not in {'A','B'}:
                output('你会：A：进比特塔门,B：叫车')
            if choose == 'A':
                output('警告：进了门后，你就没有回头的机会，你仍然要进去吗？')
                output('A：进去,B：不进')
                while choose not in {'A','B'}:
                    output('A：进去,B：不进')
                if choose == 'A':
                    output('你进了门')
                    go = 1
                elif choose == 'B':
                    output('你没进门')
            elif choose == 'B':
                if cosh_A != 1:
                    output('A：去LC区、小天住房,B：去P区、像素广场,C：去P区、比特塔')
                    while choose not in {'A','B','C'}:
                        output('A：去LC区、小天住房,B：去P区、像素广场,C：去P区、比特塔')
                elif cosh_A == 1:
                    output('A：去LC区、小天住房,B：去P区、像素广场,C：去P区、比特塔,D：去P区、像素大街')
                    while choose not in {'A','B','C','D'}:
                        output('A：去LC区、小天住房,B：去P区、像素广场,C：去P区、比特塔,D：去P区、像素大街')
                if choose == 'A':
                    output('你前往小天的住房，小天看到你们的到来，开心地对你们说：“你们好！请问你们想做些什么呢？”')
                    if 'FireFox.max（破损）' not in item and 'FireFox.max' not in item:
                        output('A：随便聊聊,B：询问赛恩思的消息,C：离开')
                        while choose not in {'A','B','C'}:
                            output('A：随便聊聊,B：询问赛恩思的消息,C：离开')
                        if choose == 'C':
                            choose = 'D'
                    elif 'FireFox.max（破损）' in item and 'FireFox.max' not in item:
                        output('A：随便聊聊,B：询问赛恩思的消息,C：拿出破损的Firefox.max,D：离开')
                        while choose not in {'A','B','C','D'}:
                            output('A：随便聊聊,B：询问赛恩思的消息,C：拿出破损的Firefox.max,D：离开')
                    elif 'FireFox.max' in item:
                        output('A：随便聊聊,B：询问赛恩思的消息,S：拿出FireFox.max,D：离开')
                        while choose not in {'A','B','S','D'}:
                            output('A：随便聊聊,B：询问赛恩思的消息,S：拿出FireFox.max,D：离开')
                    if choose == 'A':
                        output('小天说：“嗯……你们已经找到比特塔啦，太棒啦！我也在努力修复我这里的网络，估计很快我就可以出去了！”')
                    elif choose == 'B':
                        output('小天有点失落：“赛恩思已经有好长一段时间没什么消息了，我猜他一直躲在比特塔里面不出来。”')
                        output('So追问了阿尔法的事情，小天有些迷糊：“你们遭到了一个叫阿尔法的人的袭击？我可以确定的是我没有……当然，也许我在赛恩思面前太弱了点……”')
                    elif choose == 'C':
                        output('你拿出破损的FireFox.max，周围顿时出现一堆散布着乱码的显示屏')
                        output('小天有点惊讶：“你们居然有这个东西……它好像坏掉了，也许你们可以找某个人修好它，到时候再来找我，我会给你们看个大的！”')
                    elif choose == 'D':
                        go_car = 1
                    elif choose == 'S':
                        output('你拿出来FireFox.max，周围突然出现一个巨大的显示屏，上面出现了更多的显示屏，每个显示屏都写着许多代码。')
                        output('“什么？这是FireFox.max！”小天惊讶地说，“你们……果然不简单啊……”')
                        output('小天想了一会儿，在机器前捣鼓了一阵，他随即拿出了一个紫色的晶体。')
                        choose = input('“我决定了，把这个东西交给你，我除了观察赛恩思之外，还会找一些其它东西帮助我逃出去，这就是一个重要的东西……只可惜我需要到像素塔里面，它才能帮我逃出去，如果你们可以进入像素塔……”小天有点激动。（获得【H-Core】）')
                        item.remove('FireFox.max')
                        item.append('H-Core')
                        view_status()
                elif choose == 'B':
                    output('你来到了像素广场')
                    go_up = 0
                    while go_up == 0:
                        output('你会：A：去买东西,B：去打游戏,C：离开')
                        while choose not in {'A','B','C'}:
                            output('你会：A：去买东西,B：去打游戏,C：离开')
                        if choose == 'A':
                            output('你去买东西，商场人依然很多，你逛了好几个商店，突然发现了一个叫做“合成中心”的商铺，你走了进去。')
                            output('商店里只有一个店员。他见到你们来，跟你们打招呼：“想升级你的装备吗？想修复你的装备吗？来我这吧！”')
                            go_fix = 0
                            while go_fix == 0:
                                output('你会：A：合成物品,B：离开')
                                while choose not in {'A','B'}:
                                    output('你会：A：合成物品,B：离开')
                                if choose == 'B':
                                    go_fix = 1
                                elif choose == 'A':
                                    choose = input('请选择你想合成的物品：\n合成表：\nA：电方块（需要【电棉*10】）\nB：像素板（需要【像素碎片*5】）\nC：纯净血晶体（需要【血石*3】）\nD：恐惧激光枪（需要【电方块*1】、【像素板*1】、【电磁激光枪*1】）\nE：核琪淋（需要【电方块*1】、【冰淇淋*1】）\nF：能量核心（需要【能量晶体*3】）\nG：FireFox.max（需要【Firefox.max（破损）*1】【电方块*4】）')
                                    view_status()
                                    while choose not in {'A','B','C','D','E','F','G'}:
                                        choose = input('请选择你想合成的物品：\n合成表：\nA：电方块（需要【电棉*10】）\nB：像素板（需要【像素碎片*5】）\nC：纯净血晶体（需要【血石*3】）\nD：恐惧激光枪（需要【电方块*1】、【像素板*1】、【电磁激光枪*1】）\nE：核琪淋（需要【电方块*1】、【冰淇淋*1】）\nF：能量核心（需要【能量晶体*3】）\nG：FireFox.max（需要【Firefox.max（破损）*1】【电方块*4】）')
                                        view_status()
                                    if choose == 'A':
                                        if E_cotton < 10:
                                            input('你的物品不足！')
                                        else:
                                            input('你获得了电方块！')
                                            E_cotton -= 10
                                            L_block += 1
                                    elif choose =='B':
                                        if o_up < 5:
                                            input('你的物品不足！')
                                        else:
                                            input('你获得了像素板！')
                                            o_up -= 5
                                            UP_plus += 1
                                    elif choose =='C':
                                        if blood_stone < 3:
                                            input('你的物品不足！')
                                        else:
                                            input('你获得了纯净血晶体！')
                                            blood_stone -= 3
                                            blood_block += 1
                                    elif choose =='D':
                                        if UP_plus < 1 or L_block < 1 or ('电磁激光枪' not in item and '电磁激光枪 not in weapon'):
                                            input('你的物品不足！')
                                        else:
                                            input('你获得了恐惧激光枪！')
                                            UP_plus -= 1
                                            L_block -= 1
                                            if weapon == '电磁激光枪':
                                                weapon = ''
                                            if '电磁激光枪' in item:
                                                item.remove('电磁激光枪')
                                            item.append('恐惧激光枪')
                                    elif choose =='E':
                                        if '冰淇淋' not in item or L_block < 1:
                                            input('你的物品不足！')
                                        else:
                                            input('你获得了核淇淋！')
                                            L_block -= 1
                                            item.remove('冰淇淋')
                                            fight_item.remove('冰淇淋')
                                            item.append('核淇淋')
                                            fight_item.append('核淇淋')
                                    elif choose =='F':
                                        if H_cube < 3:
                                            input('你的物品不足！')
                                        else:
                                            input('你获得了能量核心！')
                                            H_cube -= 5
                                            item.append('能量核心')
                                    elif choose =='G':
                                        if 'FireFox.max（破损）' not in item or L_block < 4:
                                            input('你的物品不足！')
                                        else:
                                            input('你获得了FireFox.max！')
                                            L_block -= 4
                                            item.append('FireFox.max')
                                            item.remove('FireFox.max（破损）')
                                            input('店员说：“这个发着紫光的东西……看起来不属于我们这个世界……我觉得它恐怕没什么用。')
                                    view_status()
                        elif choose == 'B':
                            output('你来到游戏厅。')
                            choose = input('你来到了一个称为“怪兽大战”的街机前，街机上立即出现字幕：\n请登录或者使用游客模式！')
                            view_status()
                            output('你由于害怕被侦测到，使用了游客模式，字幕立即改变')
                            output('请选择你想进行对战的对象！')
                            output('你的面前出现了五个附有文字说明的图片。')
                            go_B = 0
                            while go_B == 0:
                                if CM >= 20:
                                    choose = input('A：CAR-XXX（进入玩具车战）\nB：FLY-XXX（进入飞行器战）\nC：MCE-XXX（进入机械臂战）\nD：ELE-XXX（进入电子蛇战）\nE：1UP-XXX（进入幽灵战）\nF：离开')
                                    while choose not in {'A','B','C','D','E','F'}:
                                        choose = input('A：CAR-XXX（进入玩具车战）\nB：FLY-XXX（进入飞行器战）\nC：MCE-XXX（进入机械臂战）\nD：ELE-XXX（进入电子蛇战）\nE：1UP-XXX（进入幽灵战）\nF：离开')
                                        view_status()
                                else:
                                    choose = input('A：离开')
                                    while choose not in {'A'}:
                                        output('A：离开')
                                    choose = 'F'
                                if choose == 'A':
                                    CM -= 20
                                    car_fight()
                                elif choose == 'B':
                                    fly_fight()
                                    CM -= 20
                                elif choose == 'C':
                                    CM -= 20
                                    arm_fight()
                                elif choose == 'D':
                                    CM -= 20
                                    input('维修中（恼）')
                                elif choose == 'E':
                                    input('维修中（恼）')
                                else:
                                    go_B = 1
                        elif choose == 'C':
                            output('你离开了像素广场')
                            go_up = 1
                elif choose == 'C':
                    output('不幸的是，你已经在这里了')
                elif choose == 'D':
                    output('你来到像素大道，这里不像你们之前见到P区的其它建筑一样，而是一条由矮矮的房子组成的大街。')
                    output('你来到像素大道2号，这是一座气派的花园，园里种着许多墨绿色的代码树。')
                    output('你敲了敲屋子门，里面顿时传来回音：“是观众吗？？？？？？？？？？？”')
                    output('你会回答：A：是,B：不是')
                    while choose not in {'A','B'}:
                        output('你会回答：A：是,B：不是')
                    output('门里传来怪笑声：“啊！我就知道你是可爱的Zero！！！')
                    output('嘿嘿，我只是想找你完成一件事啦，毕竟Zero——你——我可是信任你滴！！！”')
                    output('门里面的声音继续说：“去找小天！给他看他的什么火狐狸点最大——是破损的那个！！他会告诉你要去修复，你需要去像素广场找到合成站修复它！！！哈哈！这可真够累的！！！修复完成后，拿着那玩意儿找小天，他会给你一个东西……接下来带着那个东西去比特塔……让你们自己探索吧！！！我不喜欢剧透！！！！！”')
                    output('So有点反感地问道：“你为什么不自己去……”')
                    output('“什么？你们让我自己去？！！让我自己去受苦吗？！！哈哈哈！！！你不知道外面人都认为我是疯子吗？！？哈哈哈哈哈哈哈哈哈哈——”')
                    output('“所以……你怎么知道这些的……”So问道。')
                    output('“我还是那句话哈——别傻傻地问问题！！！去吧孩子们，等你们在比特塔的——地下室拿到伟大的“零件”后——我就！！我就！！我就可以统治世界！！每个人——每个人——每个人——都可以因为COSH而得到解放！！！快滚吧小宝贝！！！”')
                    output('你们迅速离开门口。')
                    cosh_A = 2
        output('你们进入比特塔，周围的守卫看见了你们，慌慌张张地躲在一边。')
        output('比特塔的内部是一座大厅，里面摆着许多巨大的不明所以的雕像，但你没有看到什么有用的东西。')
        output('你会：A：看看雕像,B：四处搜寻,C：继续深入')
        while choose not in {'A','B','C'}:
            output('你会：A：看看雕像,B：四处搜寻,C：继续深入')
        if choose == 'A':
            output('你看了看雕像，这里的雕像无一例外都发着显眼的绿光，你仔细看了看这些雕像，发现它们其实是同一个机器人的各种姿势。')
        elif choose == 'B':
            choose = input('你四处搜寻着，在一块地砖上找到了300CMB！')
            CM += 300
            view_status()
        output('你们向比特塔的内部深处走去，你们的前方是一条长长的走廊，走廊上铺着一条红色的地毯。')
        output('你们正要往前走，突然一个奇怪的绿色机器人从走廊尽头滚了过来，机器人一见到你就向你们热情地打招呼：')
        output('“嗨！Zero！So！昵称！欢迎来到比特塔！我是这里的管理员——阿尔法！”')
        output('“阿尔法？！”So看着眼前的机器人大惊失色道。')
        output('“是的！我是阿尔法！”机器人大声说。“我承认列车那次，我对你们手下留情了，否则你们不可能走到这儿来哦！不过呢，现在，你们面对的可是比特塔……在这里消灭你们简直是易如反掌啊！！所以呢，不要抱有太多的侥幸！乖乖的束手就擒，等到贝塔提取到你们的记忆碎片后，你们就可以离开了！”')
        output('“你说什么？！什么记忆碎片？！”So大叫。')
        output('“你们可不需要知道呢！”阿尔法向前一步。“总之！你们将在这里面对……你们遭遇过敌人中的精锐部队！玩得开心！”阿尔法说完向后迅速地跑开了。')
        output('“别跑！”So刚想追上去。突然，你们的两侧传来了奇怪的声音，你扭头一看，发现你们侧面的墙壁上出现了两个缺口，一个巨大的车辆和一个奇异的六芒星飞了出来。')
        output('“来试试吧！你们先前碰到的敌人，充其量只是城市里的普通居民而已，而现在，你们将会面对专业的雇佣兵！！祝你们好运！！！”阿尔法怪笑着跑开了。')
        output('车辆和六芒星摆成进攻阵型向你们逼近')
        print('战斗开始,对战：重型装甲车 x 地狱六芒星')
        hucker = 0
        big_fight = 0
        t.sleep(0.5)
        car,fly = 520,300
        H = 250
        H_icecream = 0
        fly_B = 3
        item_att = 0
        check = 0
        magic_use = 0
        magic_point = 0
        miaomiao = 0
        H_fix = 10
        coat = 0
        win = 0
        a,b,c,d,e = '','','','',''
        while win == 0:
            magic_choose = 0
            att_choose = 0
            item_choose = 0
            while magic_choose == 0 and item_choose == 0:
                if car <= 0:
                    car = 0
                if fly <= 0:
                    fly = 0
                chooseb = 'A'
                if '战争宝石' in item:
                    print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health},重型装甲车血量为{car},攻击力为30，防御力35，防御率40%,地狱六芒星血量为{fly},护盾血量{H},攻击力为30，防御力30，防御率15%，你的暴击数{big_fight}')
                if '战争宝石' not in item:
                    print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health},重型装甲车血量为{car},地狱六芒星血量为{fly},护盾血量{H}')
                choose = input('A,物品B,防御C,魔法D,跳过')
                while choose not in {'A','B','C','D'}:
                    print('请做出你的选择')
                    choose = input('A,物品B,防御C,魔法D,跳过')
                if choose == 'A':
                    choose = input(f'你现在可使用的物品有{fight_item},请从1开始输入序号以选择使用的物品')
                    if choose not in {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'}:
                        choose = input('物品序号输入错误!')
                    else:
                        choose = int(choose)
                        if choose > len(fight_item):
                            choose = input('物品序号输入错误!')
                        else:
                            check = fight_item[choose]
                            item_find()
                            if check == '魔法炸药':
                                choose = input('你对对方造成了100点伤害!但你也不小心受到了30点伤害')
                                health -= 30
                                car -= 100
                                if H > 0:
                                    H -= 100
                                elif H <= 0:
                                    fly -= 100
                                dead_interface()
                                if respawned == 1:
                                    break
                            if check == '坚硬冰棍':
                                choose = input('请选择投掷的对象（填A或者B）')
                                while choose not in {'A','B'}:
                                    choose = input('请选择投掷的对象（填A或者B）')
                                if choose == 'A':
                                    choose = input('你使用了坚硬冰棍!重型装甲车的HP降低了100点!')
                                    car -= 100
                                else:
                                    if H <= 0:
                                        choose = input('你使用了坚硬冰棍!地狱六芒星的HP降低了100点!')
                                        fly -= 100
                                    elif H > 0:
                                        choose = input('你使用了坚硬冰棍!地狱六芒星的护盾耐久度降低了100点!')
                                        H -= 100
                            if check == '像素板':
                                choose = input('你使用了像素板！重型装甲车和地狱六芒星受到了70点伤害！')
                                car -= 70
                                fly -= 70
                            if check in fight_item and check in item:
                                item.remove(check)
                                fight_item.remove(check)
                        if H < 0:
                            H = 0
                        if health > 300:
                            health = 300
                elif choose == 'B':
                    choose = input('你选择了防御!')
                    magic_point += 40
                    magic_choose = 1
                    if magic_point >= 100:
                        magic_point = 100
                    chooseb = 'B'
                elif choose == 'C':
                    if blood_block <= 0:
                        choose = input(f'A：治疗魔法（{health_point}）B：战斗魔法（70）C：黑暗魔法（？）D：暗蓝卫衣（30-50）E：猫叫芯片（40）')
                        while choose not in {'A','B','C','D','E'}:
                            print('请做出你的选择')
                            choose = input(f'A：治疗魔法（{health_point}）B：战斗魔法（70）C：黑暗魔法（？）D：暗蓝卫衣（30-50）E：猫叫芯片（40）')
                    elif blood_block > 0:
                        choose = input('A：治疗魔法（{0）B：战斗魔法（0）C：黑暗魔法（？）D：暗蓝卫衣（0）E：猫叫芯片（0）')
                        while choose not in {'A','B','C','D','E'}:
                            print('请做出你的选择')
                            choose = input(f'A：治疗魔法（0）B：战斗魔法（0）C：黑暗魔法（？）D：暗蓝卫衣（0）E：猫叫芯片（0）')
                    if choose == 'A':
                        if magic_point < health_point and blood_block <= 0:
                            input('你的魔法值不够!')
                            magic_choose = 0
                        else:
                            input(f'你使用了治疗法术!你的血量回复了{health_plus}点!')
                            health += health_plus
                            magic_use = health_point
                            magic_choose = 1
                            magic_point -= 30
                        if health > 300:
                            health = 300
                            magic_choose = 1
                    if choose == 'B':
                        if magic_point < 70 and blood_block <= 0:
                            input('你的魔法值不够!')
                            magic_choose = 0
                        else:
                            input('你使用了战斗法术!你的攻击提高了5点,持续一回合!')
                            att_choose = 1
                            magic_use = 70
                            magic_choose = 1
                            magic_point -= 70
                    if choose == 'C':
                        input('l͓̩̫̘͙͔̯͖̟̤̓͊̑̌́̂̆̚ò̥̪̭̱̰̝̒͂̄͋̿̏͆́̚c͍̲͇͚̖̬͈̪͙̳͌̉́̃k̪̥̱̝̱̑̈́̏̽͗̊̈́͂̀̍e̞͎̩̜̱̩͚̤̊͌̀̀d̠̖̞̝̙̪̟̞̐͛̈̊̀͂̄͌̓̏͌̓ͅ')
                        magic_choose = 0
                    if choose == 'D':
                        if magic_point < 50 and blood_block <= 0:
                            input('你的魔法值不够!')
                        else:
                            coat_B = random.randint(30,50)
                            magic_point -= coat_B
                            magic_use = coat_B
                            coat = 1
                            magic_choose = 1
                            input('你使用了暗蓝卫衣!你的闪避率提高了10％,持续一回合!')
                    if choose == 'E':
                        if magic_point < 40 and blood_block <= 0:
                            choose = input('你的魔法值不够!')
                            magic_choose = 0
                        else:
                            magic_use = 40
                            input('你使用了猫叫芯片!敌人发出了喵喵叫的声音')
                            magic_choose = 1
                            magic_point -= 40
                            miaomiao = 1
                            if random.randint(1,5) == 3:
                                print('喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵（')
                            choose = 0
                        choose = 0
                    if blood_block > 0:
                        blood_block -= 1
                        magic_point += magic_use
                        view_status()
                        magic_use = 0
                elif choose == 'D':
                    choose = input('你跳过了你的回合')
                    magic_choose = 1
            if '混乱护盾' in armor:
                health += random.randint(3,20)
                if health >= 300:
                    health = 300
            if H_icecream > 0:
                H_icecream -= 1
                health -= 20
            if car > 0:
                car_F = random.randint(1,5)
                car_P = random.randint(1,5)
                car_P_B = 0
                car_act_B = random.randint(1,4)
                if car_act_B == 1:
                    input('装甲车发射着紫红色的恐怖激光')
                if car_act_B == 2:
                    input('装甲车试图与周围的电路产生共鸣，等等机械振动与电磁振动会产生共振吗？')
                if car_act_B == 3:
                    input('装甲车向你碾来！')
                if car_act_B == 4:
                    input('装甲车四处张望着')
                x = random.randint(1,4)
                a = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                b = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                c = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                d = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                e = chr(ord('A') + x - 1)
                enemy_fight = a+b+c+d+e
                enemy_fighta = [a,b,c,d,e]
                zero_att = 0
                if '零剑' in weapon:
                    zero_att = random.randint(5,50)
                choose = list(input(f'请选择你对重型装甲车的攻击!(5个一组,由五个大写字母构成)'))
                hurt = 0
                hurtB = 0
                chance = 0
                wrong = 0
                while wrong == 0:
                    wrong = 1
                    if len(choose) != 5:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[0] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[1] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[2] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[3] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[4] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                else:
                    cube_act = random.randint(1,4)
                    while chance < 5:
                        f = choose.pop()
                        g = enemy_fighta.pop()
                        if chooseb != 'B':
                            if (f == 'A' and g == 'B') or (f == 'B' and g == 'C') or (f == 'C' and g == 'D') or (f == 'D' and g == 'A'):
                                hurt += att
                                chance += 1
                                if att_choose == 1:
                                    hurt += 5
                                if cube_act == 1:
                                    hurt -= 35
                                    laser(35)
                                else:
                                    laser(0)
                                hurt += item_att
                                hurt += zero_att
                                if hucker == 1:
                                    hurt += 10
                        if (f == 'D' and g == 'C') or (f == 'C' and g == 'B') or (f == 'B' and g == 'A') or (f == 'A' and g == 'D'):
                            if car_P == 3:
                                car_P_B += 1
                            if car_F != 1:
                                hurtB += 30
                            if chooseb == 'B':
                                hurtB -= (Def+blood_stone)
                                if hucker == 1:
                                    hurtB -= 30
                                if hurtB < 0:
                                    hurtB = 0
                            chance += 1
                            if coat == 1 and random.randint(1,10) == 5:
                                hurtB = 0
                            if miaomiao == 1:
                                hurtB /= 2
                                hurt_B = int(hurtB)
                            else:
                                health += 10
                        else:
                            chance += 1
                    if random.randint(1,20) == 3 and '战争宝石' in item and att_choose == 1:
                        hurt *= 3
                        big_fight += 1
                    if hide[0] + hide[1] >= random.randint(1,100):
                        hurtB = 0
                    if hurt > 50 and car_F == 1:
                        hurt = 50
                    health -= hurtB
                    item_att = 0
                    choose = input(f'重型装甲车的攻击是{enemy_fight}')
                    if cube_act == 1 :
                        choose = input('重型装甲车使用了防御!')
                    if chooseb != 'B':
                        choose = input(f'你对重型装甲车造成了{hurt}点伤害!')
                        car -= hurt
                        hurt = 0
                    if chooseb == 'B':
                        choose = input('因为你选择了防御,所以伤害不计入')
                    if car_P == 3:
                        health -= 30 * car_P_B
                        input(f'重型装甲车向你射出了一枚炮弹！对你造成了{30*car_P_B}点伤害')
                    choose = input(f'你被重型装甲车扣除了{hurtB+(30*car_P_B)}点血')
                    car_P_B = 0
                    dead_interface()
                    if respawned == 1:
                        break
            if fly > 0:
                fly_B -= 1
                car_act_B = random.randint(1,6)
                if car_act_B == 1:
                    input('六芒星展示着自己的突刺')
                if car_act_B == 2:
                    input('六芒星向你们俯冲过来')
                if car_act_B == 3:
                    input('六芒星对你们发动了猛烈的炮轰！')
                if car_act_B == 4:
                    input('六芒星正在准备一发地毯式轰炸！')
                if car_act_B == 5:
                    input('你们没有找到对手的破绽')
                if car_act_B == 6 and H > 0:
                    input('六芒星对自己的电磁防护罩非常满意')
                if car_act_B == 6 and H <= 0:
                    input('六芒星感到焦虑不安')
                x = random.randint(1,4)
                a = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                b = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                c = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                d = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                e = chr(ord('A') + x - 1)
                enemy_fight = a+b+c+d+e
                enemy_fighta = [a,b,c,d,e]
                zero_att = 0
                if '零剑' in weapon:
                    zero_att = random.randint(5,50)
                if fly_B != 0:
                    choose = list(input(f'请选择你对地狱六芒星的攻击!(5个一组,由五个大写字母构成)'))
                    hurt = 0
                    hurtB = 0
                    chance = 0
                    wrong = 0
                    while wrong == 0:
                        wrong = 1
                        if len(choose) != 5:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[0] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[1] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[2] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[3] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[4] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    else:
                        cube_act = random.randint(1,20)
                        while chance < 5:
                            f = choose.pop()
                            g = enemy_fighta.pop()
                            if chooseb != 'B':
                                if (f == 'A' and g == 'B') or (f == 'B' and g == 'C') or (f == 'C' and g == 'D') or (f == 'D' and g == 'A'):
                                    hurt += att
                                    chance += 1
                                    if att_choose == 1:
                                        hurt += 5
                                    if cube_act <= 3:
                                        hurt -= 30
                                        laser(30)
                                    else:
                                        laser(0)
                                    hurt += item_att
                                    hurt += zero_att
                                    if hucker == 1:
                                        hurt += 10
                            if (f == 'D' and g == 'C') or (f == 'C' and g == 'B') or (f == 'B' and g == 'A') or (f == 'A' and g == 'D'):
                                hurtB += 30
                                if chooseb == 'B':
                                    hurtB -= (Def+blood_stone)
                                    if hucker == 1:
                                        hurtB -= 30
                                    if hurtB < 0:
                                        hurtB = 0
                                chance += 1
                                if coat == 1 and random.randint(1,10) != 5:
                                    hurtB = 0
                                else:
                                    health += 10
                            else:
                                chance += 1
                    if hide[0] + hide[1] >= random.randint(1,100):
                        hurtB = 0
                    health -= hurtB
                    item_att = 0
                    if random.randint(1,20) == 3 and '战争宝石' in item and att_choose == 1:
                        hurt *= 3
                        big_fight += 1
                    choose = input(f'地狱六芒星的攻击是{enemy_fight}')
                    if cube_act <= 3:
                        choose = input('地狱六芒星使用了防御!')
                    if chooseb != 'B':
                        choose = input(f'你对地狱六芒星造成了{hurt}点伤害!')
                        if H > 0:
                            H -= hurt
                        elif H <= 0:
                            fly -= hurt
                        if H < 0:
                            H = 0
                        hurt = 0
                    if chooseb == 'B':
                        choose = input('因为你选择了防御,所以伤害不计入')
                    choose = input(f'你被地狱六芒星扣除了{hurtB}点血')
                    H_fix -= 1
                    if H_fix == 0:
                        H += 250
                        input('六芒星继续制造了一个护盾！')
                        H_fix = 10
                elif fly_B == 0:
                    fly_B = 3
                    input('六芒星开启了地狱眼模式！！！一波狂轰滥炸即将开始！')
                    boom = 6
                    while boom > 0:
                        boom -= 1
                        choose = list(input('请输入两个大写字母，共输入六次！'))
                        x = random.randint(1,4)
                        a = chr(ord('A') + x - 1)
                        x = random.randint(1,4)
                        b = chr(ord('A') + x - 1)
                        enemy_fight = a+b
                        enemy_fighta = [a,b]
                        hurt = 0
                        hurtB = 0
                        chance = 0
                        wrong = 0
                        while wrong == 0:
                            wrong = 1
                            if len(choose) != 2:
                                wrong = 0
                                print('输入错误,请依照格式输入!')
                                choose = list(input(f'请选择你的攻击!'))
                            elif choose[0] not in {'A','B','C','D'}:
                                wrong = 0
                                print('输入错误,请依照格式输入!')
                                choose = list(input(f'请选择你的攻击!'))
                            elif choose[1] not in {'A','B','C','D'}:
                                wrong = 0
                                print('输入错误,请依照格式输入!')
                                choose = list(input(f'请选择你的攻击!'))
                        cube_act = random.randint(1,20)
                        while chance < 2:
                            f = choose.pop()
                            g = enemy_fighta.pop()
                            if (f == 'A' and g == 'B') or (f == 'B' and g == 'C') or (f == 'C' and g == 'D') or (f == 'D' and g == 'A'):
                                hurt += att
                                chance += 1
                                if att_choose == 1:
                                    hurt += 5
                                if cube_act <= 3:
                                    hurt -= 30
                                    laser(30)
                                else:
                                    laser(0)
                                hurt += item_att
                                hurt += zero_att
                                if hucker == 1:
                                    hurt += 10
                                
                            elif (f == 'D' and g == 'C') or (f == 'C' and g == 'B') or (f == 'B' and g == 'A') or (f == 'A' and g == 'D'):
                                hurtB += 30
                                chance += 1
                                if coat == 1 and random.randint(1,10) != 5:
                                    hurtB = 0
                                if miaomiao == 1:
                                    hurtB /= 2
                                    hurt_B = int(hurtB)
                                else:
                                    health += 10
                            else:
                                chance += 1
                        health -= hurtB
                        choose = input(f'地狱六芒星的攻击是{enemy_fight}')
                        if chooseb != 'B':
                            choose = input(f'你对地狱六芒星造成了{hurt}点伤害!')
                            if H > 0:
                                H -= hurt
                            elif H <= 0:
                                fly -= hurt
                            if H < 0:
                                H = 0
                            hurt = 0
                        choose = input(f'你被地狱六芒星扣除了{hurtB}点血')
                        H_fix -= 1
                    if H_fix == 0:
                        H += 250
                        input('六芒星继续制造了一个护盾！')
                        H_fix = 10
                dead_interface()
                hurtB = 0
                att_choose = 0
                if respawned == 1:
                    break
            hide[1] = 0
            coat = 0
            miaomiao = 0
            if car <= 0 and fly <= 0:
                choose = input('您获胜了!')
                CM_get = random.randint(730,1750)
                CM += CM_get
                choose = input(f'你获得了{CM_get}个CM币')
                E_cotton += 1
                win = 1

        if respawned == 1:
            respawned = 0
            continue
        output('你们击败了装甲车和六芒星，两个佣兵逃跑了。')
        savepoint = 19
    #做个存档点标记
    if savepoint == 19:
        save_data()
        output('你们继续前进，来到一座大堂。这里精致地布置着一条人造小河，河上有一座小桥')
        output('你的面前有一座商店和一个仓库')
        go = 0
        while go == 0:
            output('你会：A：去桥上逛逛,B：看看商店,C：看看仓库,D：继续前进')
            while choose not in {'A','B','C','D'}:
                output('你会：A：去桥上逛逛,B：看看商店,C：看看仓库,D：继续前进')
            if choose == 'A':
                if 60<= fun <= 80:
                    output('你来到桥上往下看，下面的水并不是那么清澈,突然，你脚有点不稳掉了下去，摔到水中。')
                    output('你惊慌失措地想要稳住身子，突然，你看到有许多金属制品杂乱地摆放在水底，像是机器人的零件。')
                    output('你快速挣扎浮上水面，游到岸边爬了上去。')
                    output('你穿着湿衣服直打哆嗦。')
                else:
                    output('你来到桥上往下看，下面的水并不是那么清澈')
            if choose == 'B':
                output('你来到商店，这里的商品看起来十分高端')
                shop = 0
                if '商店4' not in shops:
                    shops.append('商店4')
                while shop == 0:
                    output('你会购买：A：电子爆球【277CMB】,B：黑鸡尾酒【426CMB】,C：Complex机械长剑【1170CMB】,D：超级爱心【4000CMB】,E：离开')
                    while choose not in {'A','B','C','D','E'}:
                        output('你会购买：A：电子爆球【277CMB】,B：黑鸡尾酒【426CMB】,C：Complex机械长剑【1170CMB】,D：超级爱心【4000CMB】,E：离开')
                    money = 0
                    buy = 0
                    if choose == 'A':
                        if CM < 277:
                            output('你的CM币不够!')
                        else:
                            buy = '电子爆球'
                            money = 277
                    elif choose == 'B':
                        if CM < 426:
                            output('你的CM币不够!')
                        else:
                            buy = '黑鸡尾酒'
                            money = 426
                    elif choose == 'C':
                        if CM < 1170:
                            output('你的CM币不够!')
                        else:
                            buy = 'Complex机械长剑'
                            money = 1170
                    elif choose == 'D':
                        if CM < 400:
                            output('你的CM币不够!')
                        else:
                            buy = 0
                            choose = input('你购买了超级爱心!')
                            super_love += 1
                            CM -= 400
                    elif choose == 'E':
                        shop = 1
                    if len(item) >= 10 and buy != 0:
                        view_status()
                    if ('Complex机械长剑' in item or weapon == 'Complex机械长剑') and buy == 'Complex机械长剑':
                        buy = 0
                        output('你已经购买了这个物品了!')
                    if buy != 0:
                        item.append(buy)
                        if buy in {'电子爆球','黑鸡尾酒'}:
                            fight_item.append(buy)
                        output(f'你购买了{buy}!')
                        buy = 0
                        CM -= money
                shop = 1
            elif choose == 'C':
                output('仓库前面摆放着一个武器架可惜上面的武器拿不下来')
            elif choose == 'D':
                output('你继续前进')
                go = 1
        output('你们走了一会，前面出现了一座餐厅，几名机器人服务员在餐厅里工作。')
        output('你会：A：点餐,B：交谈,C：离开')
        while choose not in {'A','B','C'}:
            output('你会：A：点餐,B：交谈,C：离开')
        if choose == 'A':
            output('你点了一份餐，机器人掏出了一份巨大无比的生牛排，由于实在是太大了，你不准备吃它。')
        elif choose == 'B':
            output('你找到一个服务员。服务员说：“比特塔最近没什么客人，我们也没什么生意……')
            output('什么？你说雇佣兵？我从来没有听说过比特塔里面有雇佣兵啊，这塔不是个实验室吗？”')
        output('你们离开餐厅，前面是一座通向地下的楼梯。')
        if tower == 0:
            output('楼梯的上方升起了许多升降门，与众不同的是，这些升降门顶上显示着一串在快速变化着的代码。')
            output('“小心这里的升降门，它们会以不同形态出现……你们得用一般的格式躲避了。”')
            go = 0
            while go == 0:
                count = 0
                choose = list(input('请输入你的通过方式'))
                x = random.randint(1,4)
                a = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                b = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                c = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                d = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                e = chr(ord('A') + x - 1)
                enemy_fight = a+b+c+d+e
                enemy_fighta = [a,b,c,d,e]
                hurt = 0
                hurtB = 0
                chance = 0
                wrong = 0
                while wrong == 0:
                    wrong = 1
                    if len(choose) != 5:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[0] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[1] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[2] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[3] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[4] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                else:
                    while chance < 5:
                    #快悄悄这个地方,我把chance < 5写成了chance <= 5然后查了一天才查到这个bug
                    #悄悄改为瞧瞧,这是个错别字(划)通假字
                    #快看,这里我复制的前面
                        #快看，我还是复制的前面（
                        f = choose.pop()
                        g = enemy_fighta.pop()
                        if f == 'D' and g == 'C' or f == 'C' and g == 'B' or f == 'B' and g == 'A' or f == 'A' and g == 'D':
                            hurtB += 5
                            chance += 1
                        else:
                            chance += 1
                            count += 1
                    choose = input(f'升降门的升降方式是{enemy_fight}')
                    if count >= 3:
                        input('你通过了升降门！')
                        go = 1
                    else:
                        health -= hurtB
                        choose = input(f'你没能通过升降门！你被扣除了{hurtB}点血量')
                    dead_interface()
                    if respawned == 1:
                        respawned = 0
                        continue
        else:
            output('你们走下楼梯')
        output('你们向前走去，穿过了阴森的商场，在唯一一家亮着灯的服装店门口停了下来。')
        output('这家服装店里面只有两个机器人售货员招待台边，里面的服装架空荡荡地站在地上，几乎看不到什么像样的衣服。')
        output('这时，其中一个售货员叫住了你们：“虽然我们还没有开业，但……你们也来试试我们的尝鲜饰品吧！价格……我们送你好了！”')
        output('另一个售货员端出了一个紫色的小盒子递给你们，So不情愿地接了下来。')
        output('你们离开服装店。“我想知道这玩意是什么东西。”So说。')
        output('你会：A：打开盒子,B：不管他')
        while choose not in {'A','B'}:
            output('你会：A：打开盒子,B：不管他')
        if choose == 'A':
            output('你打开盒子，并没有什么耀眼的光芒传来。盒子里面什么也没有。不过就在这时，盒子上方蹦出一个显示屏。')
            output('“是否升级你们的技能？”')
            output('“什么？”你们都凑上前去，显示屏突然分成了三个出现着加载页面的新显示屏。其中两个显示屏很快就跳出了界面：')
            choose = input('“种类：人类\n威胁程度：1/5\n侵略指数：4/5')
            view_status()
            output('是否将你的技能升级为“高科技卫衣”，花费：【能量晶体*2】”')
            choose = input('“种类：拟猫类\n威胁程度：2/5\n侵略指数：3/5')
            view_status()
            output('是否将你的技能升级为“万能芯片”，花费：【能量晶体*2】”')
            output('“技能升级？？？什么东西……”So说。')
            choose = input('你看了看第三个弹窗，仍处在加载界面，最后变成了红色：\n“请求超时。”')
            view_status()
            go = 0
            while go == 0:
                output('你会：A：升级So的技能,B：升级昵称的技能,C：不管他')
                while choose not in {'A','B','C'}:
                    output('你会：A：升级So的技能,B：升级昵称的技能,C：不管他')
                if choose == 'A':
                    if H_cube >= 2 and S_up == 0:
                        S_up = 1
                        output('升级成功！')
                    elif S_up == 1:
                        output('请求超时')
                    elif S_up == 0 and H_cube < 2:
                        output('资源不够！')
                elif choose == 'B':
                    if H_cube >= 2 and M_up == 0:
                        M_up = 1
                        output('升级成功！')
                    elif M_up == 1:
                        output('请求超时')
                    elif M_up == 0 and H_cube < 2:
                        output('资源不够！')
                else:
                    go = 1
        output('你们向商场深处继续探索，前面出现了一堵玻璃墙，玻璃墙上有一扇电梯门，上面贴着黄黑色的禁止标签。')
        output('你仔细看看了门，发现门上有一个很小的方形凹槽，凹槽下面装着一个十分复杂的装置，看起来是侦测器。')
        if 'H-Core' in item:
            output('你会：A：离开,B：再仔细检查一下,C：使用【H-Core】')
            while choose not in {'A','B','C'}:
                output('你会：A：离开,B：再仔细检查一下,C：使用【H-Core】')
        else:
            output('你会：A：离开,B：再仔细检查一下')
            while choose not in {'A','B'}:
                output('你会：A：离开,B：再仔细检查一下')
        if choose == 'B':
            output('电梯门上似乎布满了许多白色的细小碎末，闻起来像蛋糕粉。')
        elif choose == 'C':
            output('你拿出了紫色晶体，晶体太大了，根本塞不进凹槽。')
        output('你们沿着玻璃墙向前走，你的前面出现了一个像锅炉一样的装置，上面出现了一个黄色的扇形标志，你很容易看出来这是核辐射的标志。')
        output('“这里为什么会有这种玩意……”So说。“好在我的卫衣有防核……别激动，真的是防核，我们都有Sword-10了核防护服也能造出来来着，你们闪开。”')
        output('So趴在锅炉前面，拿出了一个机器仔细探测着。')
        output('“虚张声势罢了，根本没有核辐射！”So喊道，不过这个锅炉好像上锁了，如果你们要打开的话应该是不容易的。')
        if 'H-Core' in item:
            output('你会：A：走开,B：拿出【H-Core】')
            while choose not in {'A','B'}:
                output('你会：A：走开,B：拿出【H-Core】')
        else:
            output('你会：A：走开')
            while choose != 'A':
                output('你会：A：走开')
        if choose == 'A':
            output('你离开了这里')
        elif choose == 'B':
            choose = input('你拿出【H-Core】、So轻轻将紫色的结晶触碰着锅炉前面，突然，锅炉发出了奇异的闪光，你们面前的空间顿时被撕出了一道缺口！')
            item.remove('H-Core')
            view_status()
        savepoint = -1
    if savepoint == -1:
        save_data()
        output('So向你们点了点头，你们钻进了缺口。')
        output('你们从缺口里走了出来，你发现外面是一座小村庄，大大的“H”雕塑出现在你们面前。')
        output('你们的前面出现了一个绿色的弹窗，上面写着“欢迎来到黑客村庄！”')
        output('你走进村庄搜寻了一番，街道上并没有什么人，只有一座亮着彩灯的房子敞开大门出现在你们面前。')
        output('你会：A：看看H雕塑,B：进入彩灯房')
        while choose not in {'A','B'}:
            output('你会：A：看看H雕塑,B：进入彩灯房')
        if choose == 'A':
            output('一位看起来像工人的人坐在雕塑下，他一看到你便开口：“时空坐标：3377.14，4261.71，551.63，22404.39，满足洛伦兹变换与黎曼空间坐标系，碳基细胞构体落进入硅元件K、硅元件S额定射程……”')
            output('你觉得有点无聊，便向彩灯房走去')
        output('你们来到了彩灯房里面，这里有一堆奇形怪状的控制台。你在一个控制台前停下了脚步。')
        output('控制台突然发出了一阵奇怪的“嗞嗞”声，一个显示屏出现在控制台上方：\n“嗨！Zero！So！昵称！你们好！”')
        output('“你是？”So有些疑惑地看着显示屏。')
        output('“我是H，黑客村庄的控制机器人！你们能够拿到H-Core，再通过比特塔的折跃机器来到这里，真了不起！不过呢，如今你们还剩下最后的一道考验！”')
        output('“什么考验？”So问。')
        output('“你们想不想了解些关于赛恩思的事？”显示屏突然反问道。')
        output('你会回答：A：想,B：不想，继续说吧')
        while choose not in {'A','B'}:
            output('你会回答：A：想,B：不想，继续说吧')
        if choose == 'B':
            output('显示屏上的字突然改变：“可惜的是，你们并没有选择的余地。因为赛恩思是你们逃脱这里的唯一机会！”')
        output('显示屏上出现一行行大字：')
        output('“赛恩思，也就是SCI，或者S281738368，是黑客村庄的人。虽然赛恩思生长在黑客村庄，但是他对外界事物抱有很强的野心，征服欲太强。')
        output('你要知道，黑客村庄从来都是与世隔绝的，无论如何都必须这样，只有这才能保证我们的运算高效率地进行。因此我们认为赛恩思会对黑客村庄不利，因此我们设了一个局，把他赶了出去。但是很快，我们就意识到事情有些不对劲，赛恩思离开后，我们发现他并没有像一般被放逐的黑客一样，只有黑客偏僻的一技之长而很快被冷落，而是加入了一个叫SEED的奇怪组织。我们调查了这个组织，很奇怪，以黑客村庄的数据处理能力，居然探索不到什么消息，只知道组织的创建者，一个叫罗尔斯的人，把“权力”与“规则”视为组织的目标与信条。')
        output('我们无法过多调查SEED的真相，但如果我们的推测属实，SEED很可能会对位于魔法界域的核心，也就是大名鼎鼎的“魔法喷泉”造成威胁，这很可能会导致原来魔法界域的崩塌和毁灭，而SEED自己，犹如一颗种子，靠着本身修订的“规则”在崩塌的界域里重新站稳，来获得至高无上的“权力”')
        output('我们黑客村庄从不会过多插手外界的事情，但要是推测属实，假设魔法界域崩塌了，我们也自身难保。因此我们需要找到可信赖的伙伴，联合起来击败SEED，而第一个任务，就是击败赛恩思。可惜的是，我们并没有找到可信赖的人，外面的机器人，充其量就是赛恩思的傀儡罢了，而唯一一个可靠伙伴小天，目前完全没有抵抗能力。因此，请珍惜我们对你们的尊重与信任，拿着这个“魔法方块”，前往比特塔的最深层找到赛恩思的终极武器“Complex”，拿上它，去击败赛恩思吧！”')
        output('显示屏顿时消失，控制台上出现了一个蓝色的小方块。')
        choose = input('你拿上了方块，方块顿时释放出惊人的能量。（获得【能量核心】）')
        item.append('能量核心 ')
        view_status()
        output('你们正要离开，突然，显示屏再次出现：“等等！如果你们想贸然闯进比特塔深层，必定会遭到赛恩思手下的攻击。我送给你们一个蛋糕，你们可以带上它一起去。')
        choose = input('控制台上出现了一个大蛋糕（获得【黑客三周年限定蛋糕】）')
        item.append('黑客三周年限定蛋糕')
        fight_item.append('黑客三周年限定蛋糕')
        view_status()
        output('你们走出了彩灯房，传送门仍然立在你们前面，你们钻了进去')
        output('你们回到了比特塔大楼。')
        output('你会：A：去之前的电梯门,B：离开这里')
        while choose not in {'A','B','C'}:
            choose = input('你会：A：去之前的电梯门,B：离开这里')
        if choose == 'B':
            output('你向另一个方向走去')
            savepoint = 20
        else:
            output('你来到电梯门前，将蓝色的能量核心放在凹槽里，电梯门顿时发出了闪光，然后缓缓打开。你们的前面出现了一道楼梯，你们顺着楼梯向下走去。')
            output('你们来到了一座并不黑暗的房间，只是墙壁涂成了灰黑色。一条十字路口出现在你们面前。')
            output('你会：A：向左走,B：向右走,C：向前走')
            while choose not in {'A','B','C'}:
                output('你会：A：向左走,B：向右走,C：向前走')
            savepoint = -2
    if savepoint == -2:
        save_data()
        output('突然，四条路上窜出了一大群电子蛇，把路围了个水泄不通！')
        output('“这又是一个电子迷宫！”So叫道。')
        output('你注意到蛇群中有些电子蛇似乎与众不同，通体发红。')
        print('【战斗开始】')
        t.sleep(0.5)
        input('电子蛇组成了长达40步的超长迷宫！')
        sweater = 0
        snake_A = 0
        cat = 0
        magic_point = 0
        hucker = 0
        win = 0
        compete_A,compete_B,compete_C = 0,0,0
        a,b,c,d,e = '','','','',''
        while win == 0:
            magic_choose = 0
            att_choose = 0
            item_choose = 0
            snake_A += 1
            snake_A = str(snake_A)
            if snake_A == '36':
                input('昵称在一旁大喊“小心！这些电子蛇的进攻更加频繁了！”')
                input('“赛恩思为什么要在这里养这种东西啊...”So嘀咕道’')
            if snake_A in {'5','15','25','27','29','30','37','39','46','47','50'}:
                snake_A = int(snake_A)
                snake_type = random.randint(1,2)
                if snake_type == 1:
                    snake_name = '阻拦电子蛇'
                    car_A = 277
                    car_att = 17
                else:
                    snake_name = '精英阻拦电子蛇'
                    car_A = 477
                    car_att = 27
                input('电子蛇聚成了庞大的立体形状阻拦你！你必须击破它们才能前进！')
                if snake_A == 50:
                    input('“看来这应该是最后一只！”昵称叫道')
                hucker = 0
                big_fight = 0
                t.sleep(0.5)
                check = 0
                miaomiao = 0
                boom_snake = 0
                coat = 0
                win_B = 0
                a,b,c,d,e = '','','','',''
                while win_B == 0:
                    magic_choose = 0
                    att_choose = 0
                    item_choose = 0
                    while magic_choose == 0 and item_choose == 0:
                        if boom_snake > 0:
                            boom_snake -= 1
                            car_A -= 20
                            input('两只小电子蛇对敌人造成了20点伤害！')
                        if car_A <= 0:
                            car_A = 0
                        chooseb = 'A'
                        if '战争宝石' in item:
                            print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health},{snake_name}血量为{car_A},攻击力为27，防御力0，暴击数{big_fight},')
                        if '战争宝石' not in item:
                            print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health},{snake_name}血量为{car_A}')
                        choose = input('A,物品B,防御C,魔法D,跳过')
                        while choose not in {'A','B','C','D'}:
                            print('请做出你的选择')
                            choose = input('A,物品B,防御C,魔法D,跳过')
                        if choose == 'A':
                            choose = input(f'你现在可使用的物品有{fight_item},请从1开始输入序号以选择使用的物品')
                            if choose not in {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'}:
                                choose = input('物品序号输入错误!')
                            else:
                                check = fight_item[choose]
                                item_find()
                                if check == '像素板':
                                    choose = input('你使用了像素板！阻拦电子蛇受到了70点伤害！')
                                    car_A -= 70
                                if check == '魔法炸药':
                                    choose = input('你对对方造成了100点伤害!但你也不小心受到了30点伤害')
                                    health -= 30
                                    car_A -= 100
                                    dead_interface()
                                    if respawned == 1:
                                        break
                                if check == '坚硬冰棍':
                                    choose = input('你使用了坚硬冰棍!阻拦电子蛇的HP降低了100点!')
                                    car_A -= 100
                                item.remove(check)
                                fight_item.remove(check)
                                if health > 300:
                                    health = 300
                        elif choose == 'B':
                            choose = input('你选择了防御!')
                            magic_point += 40
                            magic_choose = 1
                            if magic_point >= 100:
                                magic_point = 100
                            chooseb = 'B'
                        elif choose == 'C':
                            bit_magic('normal')
                        elif choose == 'D':
                            choose = input('你跳过了你的回合')
                            magic_choose = 1
                    car_act_B = random.randint(1,6)
                    if '混乱护盾' in armor:
                        health += random.randint(3,20)
                        if health >= 300:
                            health = 300
                    if car_act_B == 1:
                        input('电子蛇绕成一圈，你们不知道在玩什么花样')
                    if car_act_B == 2:
                        input('电子蛇发出来特有的嘶嘶声')
                    if car_act_B == 3:
                        input('你们闻到一股棉花味')
                    if car_act_B == 4:
                        input('电子蛇希望你们能养它们')
                    if car_act_B == 5:
                        input('电子蛇有点想逃走')
                    if car_act_B == 6:
                        input('电子蛇不希望看到捕蛇圈')
                    if car_A > 0:
                        x = random.randint(1,4)
                        a = chr(ord('A') + x - 1)
                        x = random.randint(1,4)
                        b = chr(ord('A') + x - 1)
                        x = random.randint(1,4)
                        c = chr(ord('A') + x - 1)
                        x = random.randint(1,4)
                        d = chr(ord('A') + x - 1)
                        x = random.randint(1,4)
                        e = chr(ord('A') + x - 1)
                        enemy_fight = a+b+c+d+e
                        enemy_fighta = [a,b,c,d,e]
                        zero_att = 0
                        if '零剑' in weapon:
                            zero_att = random.randint(5,50)
                        choose = list(input(f'请选择你对{snake_name}的攻击!(5个一组,由五个大写字母构成)'))
                        hurt = 0
                        hurtB = 0
                        chance = 0
                        wrong = 0
                        while wrong == 0:
                            wrong = 1
                            if len(choose) != 5:
                                wrong = 0
                                print('输入错误,请依照格式输入!')
                                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                            elif choose[0] not in {'A','B','C','D'}:
                                wrong = 0
                                print('输入错误,请依照格式输入!')
                                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                            elif choose[1] not in {'A','B','C','D'}:
                                wrong = 0
                                print('输入错误,请依照格式输入!')
                                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                            elif choose[2] not in {'A','B','C','D'}:
                                wrong = 0
                                print('输入错误,请依照格式输入!')
                                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                            elif choose[3] not in {'A','B','C','D'}:
                                wrong = 0
                                print('输入错误,请依照格式输入!')
                                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                            elif choose[4] not in {'A','B','C','D'}:
                                wrong = 0
                                print('输入错误,请依照格式输入!')
                                choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        else:
                            war = random.randint(1,20)
                            while chance < 5:
                                f = choose.pop()
                                g = enemy_fighta.pop()
                                if chooseb != 'B':
                                    if (f == 'A' and g == 'B') or (f == 'B' and g == 'C') or (f == 'C' and g == 'D') or (f == 'D' and g == 'A'):
                                        hurt += att
                                        chance += 1
                                        if att_choose == 1:
                                            hurt += 5
                                            if '战争宝石' in item and war <= 3:
                                                hurt += 2 * att + 2 * item_att + 2 * zero_att
                                        hurt += item_att
                                        hurt += zero_att
                                        if hucker == 1:
                                            hurt += 10
                                        if '电磁激光枪' in weapon and magic_point >= 10:
                                            hurt += 35
                                if (f == 'D' and g == 'C') or (f == 'C' and g == 'B') or (f == 'B' and g == 'A') or (f == 'A' and g == 'D'):
                                    hurtB += car_att
                                    if miaomiao == 1:
                                        hurtB /= 2
                                    if chooseb == 'B':
                                        hurtB -= Def
                                        if hucker == 1:
                                            hurtB -= 30
                                        if hurtB < 0:
                                            hurtB = 0
                                    chance += 1
                                    if coat == 1:
                                        if random.randint(1,10) == 5:
                                            hurtB = 0
                                        else:
                                            health += 10
                                else:
                                    chance += 1
                            if random.randint(1,20) == 3 and '战争宝石' in item and att_choose == 1:
                                hurt *= 3
                            if hide[0] + hide[1] >= random.randint(1,100):
                                hurtB = 0
                            hide[1] = 0
                            health -= hurtB
                            item_att = 0
                            choose = input(f'{snake_name}的攻击是{enemy_fight}')
                            if chooseb != 'B':
                                choose = input(f'你对{snake_name}造成了{hurt}点伤害!')
                                car_A -= hurt
                                hurt = 0
                            if chooseb == 'B':
                                choose = input('因为你选择了防御,所以伤害不计入')
                            choose = input(f'你被敌人扣除了{hurtB}点血')
                            dead_interface()
                            if respawned == 1:
                                break
                    coat = 0
                    miaomiao = 0
                    if car_A <= 0:
                        choose = input(f'你击退了{snake_name}!')
                        E_cotton += 1
                        if len(item) < 15 and random.randint(1,2) == 2:
                            plus = random.choice(['能量饮料'],['冰冻面包'],['电路板寿司'],['H-饼干'],['能量饮料'],['冰冻面包'],['黑鸡尾酒'])
                            input(f'阻拦电子蛇留下了一个{plus},你将其拾到了背包')
                            item.append(plus)
                            fight_item.append(plus)
                        win_B = 1
                        magic_choose = 0
                        item_choose = 0
            snake_A = int(snake_A)
            win_B = 0
            while magic_choose == 0 and item_choose == 0:
                chooseb = 'A'
                print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health},你已经走了{compete_B}/40步')
                choose = input('A,物品B,防御C,魔法D,跳过')
                while choose not in {'A','B','C','D'}:
                    print('请做出你的选择')
                    choose = input('A,物品B,防御C,魔法D,跳过')
                if choose == 'A':
                    choose = input(f'你现在可使用的物品有{fight_item},请从1开始输入序号以选择使用的物品')
                    if choose not in {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'}:
                        choose = input('物品序号输入错误!')
                    else:
                        item_find()
                        if check == '魔法炸药':
                            choose = input('你对电子迷宫造成了许多伤害!但你也不小心受到了30点伤害')
                            choose = input('一条电子蛇被击退后许多电子蛇补了上来，这似乎起不到作用')
                            health -= 30
                            dead_interface()
                            if respawned == 1:
                                break
                        if check == '坚硬冰棍':
                            choose = input('你使用了坚硬冰棍!电子蛇的HP降低了许多!')
                            choose = input('一条电子蛇被击退后许多电子蛇补了上来，这似乎起不到作用')
                        if check == '像素板':
                            input('你使用了像素板,电子蛇被驱逐了，你向前行走了4步！')
                            compete_B += 4
                        item.remove(check)
                        fight_item.remove(check)
                        item_choose = 1
                        if health > 300:
                            health = 300
                if choose == 'B':
                    choose = input('你选择了防御!')
                    magic_point += 40
                    magic_choose = 1
                    if magic_point >= 100:
                        magic_point = 100
                    chooseb = 'B'
                if choose == 'C':
                    choose = input(f'A：走一步（10）B：走两步（20）C：走三步（30）D：治疗魔法（{health_point}）E：战斗魔法（70）')
                    while choose not in {'A','B','C','D','E'}:
                        print('请做出你的选择')
                        choose = input(f'A：走一步（10）B：走两步（20）C：走三步（30）D：治疗魔法（{health_point}）E：战斗魔法（70）')
                    else:
                        if choose == 'A':
                            if magic_point < 10:
                                choose = input('你的魔法值不够!')
                                magic_choose = 0
                            if magic_point >= 10:
                                choose = input(f'你尝试向前移动一小步')
                                compete_A = 1
                                magic_choose = 1
                                magic_point -= 10
                        if choose == 'B':
                            if magic_point < 20:
                                choose = input('你的魔法值不够!')
                                magic_choose = 0
                            if magic_point >= 20:
                                choose = input('你使用了魔法为你的鞋子充能！你的速度变快了！')
                                compete_A = 2
                                att_choose = 1
                                magic_choose = 1
                                magic_point -= 20
                        if choose == 'C':
                            if magic_point < 30:
                                choose = input('你的魔法值不够!')
                                magic_choose = 0
                            if magic_point >= 30:
                                choose = input('你施展了一次速度魔法！你的移动速度大幅提升！')
                                compete_A = 3
                                magic_choose = 1
                                magic_point -= 30
                        if choose == 'D':
                            if magic_point < health_point:
                                choose = input('你的魔法值不够!')
                                magic_choose = 0
                            if magic_point >= health_point:
                                choose = input(f'你使用了治疗法术!你的血量回复了{health_plus}点!')
                                health += health_plus
                                magic_choose = 1
                                magic_point -= 30
                            if health > 300:
                                health = 300
                                magic_choose = 1
                        if choose == 'E':
                            if magic_point < 70:
                                choose = input('你的魔法值不够!')
                                magic_choose = 0
                            if magic_point >= 70:
                                choose = input('你使用了战斗法术!你的攻击提高了5点,持续一回合!')
                                att_choose = 1
                                magic_choose = 1
                                magic_point -= 70
                        choose = 0
                if choose == 'D':
                    choose = input('你跳过了你的回合')
                    magic_choose = 1
            if compete_A == 0 and random.randint(1,5) <= 2:
                E_cotton += random.randint(1,4)
            x = random.randint(1,4)
            a = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            b = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            c = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            d = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            e = chr(ord('A') + x - 1)
            enemy_fight = a+b+c+d+e
            enemy_fighta = [a,b,c,d,e]
            zero_att = 0
            if '零剑' in weapon:
                zero_att = random.randint(5,50)
            car_act_B = random.randint(1,9)
            if '混乱护盾' in armor:
                health += random.randint(3,20)
                if health >= 300:
                    health = 300
            if car_act_B == 1:
                input('电子蛇绕成一圈，你们不知道在玩什么花样')
            if car_act_B == 2:
                input('电子蛇发出来特有的嘶嘶声')
            if car_act_B == 3:
                input('你们闻到一股棉花味')
            if car_act_B == 4:
                input('电子蛇希望你们能养它们')
            if car_act_B == 5:
                input('电子蛇有点想逃走')
            if car_act_B == 6:
                input('电子蛇不希望看到捕蛇圈')
            if car_act_B == 7:
                input('电子迷宫正在不断扩大')
            if car_act_B == 8:
                input('精英电子蛇会是比特塔的研究成果吗?')
            if car_act_B == 9:
                input('无聊又漫长的闯关继续进行，看起来永远不会结束')
            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
            hurt = 0
            hurtB = 0
            chance = 0
            wrong = 0
            while wrong == 0:
                wrong = 1
                if len(choose) != 5:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                elif choose[0] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                elif choose[1] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                elif choose[2] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                elif choose[3] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                elif choose[4] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
            else:
                hurtB_E = 0
                while chance < 5:
                    f = choose.pop()
                    g = enemy_fighta.pop()
                    if chooseb != 'B':
                        if (f == 'A' and g == 'B') or (f == 'B' and g == 'C') or (f == 'C' and g == 'D') or (f == 'D' and g == 'A'):
                            hurt += 1
                            chance += 1
                    if (f == 'D' and g == 'C') or (f == 'C' and g == 'B') or (f == 'B' and g == 'A') or (f == 'A' and g == 'D'):
                        hurtB_E += 1
                        hurtB += 27
                        if check == '冰冻面包':
                            hurtB = 0
                            check = ''

                        if chooseb == 'B':
                            hurtB -= Def
                            if Def >= 27:
                                hurtB = 0
                        if cat == 1:
                            hurtB /= 2
                        if hurtB <= 0:
                            hurtB = 0
                        chance += 1
                        if sweater == 1:
                            hurtB = 0
                        else:
                            health += 10
                    else:
                        chance += 1
                cat = 0
                sweater = 0
                #论coat和sweater的区别（
                if hide[0] + hide[1] >= random.randint(1,100):
                    hurtB = 0
                hide[1] = 0
                health -= hurtB
                item_att = 0
                choose = input(f'敌方的攻击是{enemy_fight}')
                choose = input(f'你被电子蛇扣除了{hurtB}点血')
                dead_interface()
                if respawned == 1:
                    break
                if hurt >= hurtB_E and compete_A != 0:
                    choose = input(f'你行走了{compete_A}步！')
                    compete_B += compete_A
                if hurt < hurtB_E and compete_A != 0:
                    choose = input('你前进时被电子蛇击退了！你只得留在原地')
                hurtB = 0
                att_choose = 0
                compete_A = 0
                if snake_A == 11 and compete_B < 6:
                    #我可不能指望玩家们玩这种无聊的战斗时同意没有一点剧情（
                    input('“你有没有觉得我们的速度好像太慢了点？”So问')
                    if magic_point < 40:
                        input('在激烈的战斗中，你已经无暇顾及他们在说什么了')
                    else:
                        choose = input('你会回答：A:是的，B:并没有')
                        while choose not in {'A','B'}:
                            choose = input('你会回答：A:是的，B:并没有')
                        if choose == 'A':
                            input('“这样啊...让我来整个大的”So答道')
                            input('“我们好像飞起来了诶！”昵称兴奋的说')
                            input('So耗费40魔法值使用了卫衣！你们向前飞行了5格')
                            magic_point -= 40
                            compete_B += 5
            if compete_B >= 40:
                choose = input('你通过了电子迷宫！')
                CM_get = random.randint(27,681)
                CM += CM_get
                choose = input(f'你获得了{CM_get}个CM币，还有一坨雪白的棉花')
                E_cotton += 1
                hucker = 0
                savepoint = 15
                win = 1
        if respawned == 1:
            respawned = 0
            continue

        output('你们通过了电子迷宫后，发现电子蛇把你们引导到了一个奇怪的地方，这里到处都是复杂的机器与交错的管道，让你感到有些心慌。')
        go = 0
        while go == 0:
            output('你会：A：寻找出口,B：查看机器')
            while choose not in {'A','B'}:
                output('你会：A：寻找出口,B：查看机器')
            if choose == 'A':
                output('你转了转，发现周围除了来路之外并没有其它的出口。')
            elif choose == 'B':
                go = 1
        output('你看了看机器，机器上出现了一个横放的显示屏，上面写着：“请输入密码。”')
        output('你发现根本就没有输入密码的地方，机器上只有一堆奇形怪状的操纵杆。')
        output('你会：A：仔细看看操纵杆,B：重新看显示屏')
        while choose not in {'A','B'}:
            output('你会：A：仔细看看操纵杆,B：重新看显示屏')
        if choose == 'A':
            output('你仔细看了看操纵杆，其中一个操纵杆看上去像行李箱的提手，上面写着：“10110011001”')
        elif choose == 'B':
            output('你看了看显示屏，发现上面还有一行小字“想想你们之前遇到过的机关。”')
            output('你又仔细看了看操纵杆，其中一个操纵杆看上去像行李箱的提手，上面写着：“10110011001”')
        output('操纵杆下面出现了一个小小的显示屏，上面写着：“请输入密码。”')
        output('“警告！如果输入错误，你将受到严重的惩罚！”')
        go = 0
        while go == 0:
            choose = input('请输入密码！')
            while choose == '':
                choose = input('请输入密码！')
            if choose != '01001100110':
                choose = input('你被一道激光射中了！[HP-50]')
                health -= 50
                dead_interface()
                if respawned == 1:
                    respawned = 0
                continue
                view_status()
            else:
                go = 1
        savepoint = -3
    if savepoint == -3:
        save_data()
        output('机器突然隆隆地响了一声，你发现其中一个管道口发出了激烈的火光，砰地一声把对面的墙壁打出了一个洞。')
        output('“这样设计谜题的啊……”So说，你们往洞里面走去。')
        output('洞口里面非常黑，你们借助一丝丝微光小心翼翼地往深处走，经过了一个向下的楼梯，来到了一个铺着地毯的走廊，天花板上坏掉的小黄灯散发着微光。')
        output('突然，你听到周围传来了“嘶嘶”的响声。')
        output('“什么动静？”So说着向后退去。突然，你们旁边的墙壁裂开了一条缝，一只巨大而诡异的机械臂从缝里伸了出来。')
        output('“嘻嘻嘻……又有好吃的了……”一个沙哑的机械声响起，机械臂开始向你们飞速抓来。')
        output('“当心！”So大声说，“咱们一起干掉这家伙！”')
        print('战斗开始,对战麻醉机械臂')
        item_att = 0
        t.sleep(0.5)
        miaomiao = 0
        boom_snake = 0
        H_icecream = 0
        clown = 616
        catch_A = 0
        catch_B = 0
        catch_C = 0
        catch_D = 0
        big_catch = 100
        MZ = random.randint(4,8)
        MZ_B = 0
        magic_point = 0
        check = 0
        win = 0
        a,b,c,d,e = '','','','',''
        while win == 0:
            magic_choose = 0
            att_choose = 0
            item_choose = 0
            if boom_snake > 0:
                boom_snake -= 1
                clown -= 20
                input('两只小电子蛇对敌人造成了20点伤害！')
            while magic_choose == 0 and item_choose == 0:
                chooseb = 'A'
                if '战争宝石' in item:
                     print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health},麻醉机械臂血量为{clown},攻击力为{25+catch_D},防御力为100,防御率为20%')
                else:
                    print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health},麻醉机械臂血量为{clown}')
                choose = input('A,物品B,防御C,魔法D,跳过')
                while choose not in {'A','B','C','D'}:
                    print('请做出你的选择')
                    choose = input('A,物品B,防御C,魔法D,跳过')
                if choose == 'A':
                    if MZ_B == 0:
                        choose = input(f'你现在可使用的物品有{fight_item},请从1开始输入序号以选择使用的物品')
                        if choose not in {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'}:
                            choose = input('物品序号输入错误!')
                        else:
                            check = fight_item[choose]
                            item_find()
                            if check == '魔法炸药':
                                choose = input('你对对方造成了100点伤害!但你也不小心受到了30点伤害')
                                health -= 30
                                clown -= 100
                                dead_interface()
                                if respawned == 1:
                                    break
                            if check == '坚硬冰棍':
                                choose = input('你使用了坚硬冰棍!麻醉机械臂的HP降低了100点!')
                                clown -= 100
                            if check == '像素板':
                                choose = input('你使用了像素板!麻醉机械臂的HP降低了70点!')
                                clown -= 70
                            if health > 300:
                                health = 300
                            if check in fight_item and check in item:
                                item.remove(check)
                                fight_item.remove(check)
                    else:
                        input('麻醉剂让你无法做出行动')
                if choose == 'B':
                    choose = input('你选择了防御!')
                    magic_point += 40
                    magic_choose = 1
                    if magic_point >= 100:
                        magic_point = 100
                    chooseb = 'B'
                if choose == 'C':
                    if MZ_B == 0:
                        bit_magic('arm')
                    else:
                        input('麻醉剂让你无法做出行动')
                if choose == 'D':
                    choose = input('你跳过了你的回合')
                    magic_choose = 1
            MZ_B = 0
            x = random.randint(1,4)
            a = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            b = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            c = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            d = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            e = chr(ord('A') + x - 1)
            enemy_fight = a+b+c+d+e
            enemy_fighta = [a,b,c,d,e]
            zero_att = 0
            if '零剑' in weapon:
                zero_att = random.randint(5,50)
            if '混乱护盾' in armor:
                health += random.randint(3,20)
                if health >= 300:
                    health = 300
            clown_act_B = random.randint(1,7)
            if clown_act_B == 1:
                choosec = input('机械臂张牙舞爪地向你伸来')
            if clown_act_B == 2:
                choosec = input('机械臂展现了航天品质')
            if clown_act_B == 3:
                choosec = input('机械臂麻臂了')
            if clown_act_B == 4:
                choosec = input('机械臂展现着它的娴熟手艺')
            if clown_act_B == 5:
                choosec = input('机械臂向你露出诡异的手影笑容')
            if clown_act_B == 6:
                choosec = input('机械臂向你展示机肉')
            if clown_act_B == 7:
                choosec = input('机械臂发出了恐怖的金属碰撞声')
            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
            hurt = 0
            hurtB = 0
            chance = 0
            wrong = 0
            if MZ == 0:
                MZ_B = 1
                input('麻醉机械臂对你使用了一发麻醉剂！')
                MZ = random.randint(4,8)
            while wrong == 0:
                wrong = 1
                if len(choose) != 5:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                elif choose[0] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                elif choose[1] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                elif choose[2] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                elif choose[3] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                elif choose[4] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
            else:
                clown_act = random.randint(1,5)
                while chance < 5:
                    f = choose.pop()
                    g = enemy_fighta.pop()
                    if chooseb != 'B':
                        if (f == 'A' and g == 'B') or (f == 'B' and g == 'C') or (f == 'C' and g == 'D') or (f == 'D' and g == 'A'):
                            if chooseb == 'C':
                                catch_C += 10
                            hurt += att
                            chance += 1
                            if att_choose == 1:
                                hurt += 5
                            if clown_act > 4:
                                hurt -= 50
                            hurt += item_att
                            if hurt <= 0:
                                hurt = 0
                            hurt += zero_att
                    if (f == 'D' and g == 'C') or (f == 'C' and g == 'B') or (f == 'B' and g == 'A') or (f == 'A' and g == 'D'):
                        hurtB += 25
                        hurtB += catch_D
                        catch_A += 10
                        big_catch -= 1
                        if chooseb == 'C':
                            catch_A -= 10
                        if chooseb == 'B':
                            hurtB -= Def
                            if random.randint(1,5) == 1:
                                hurtB += Def
                        chance += 1
                    else:
                        chance += 1
                if MZ_B == 1:
                    hurt = 0
                if hurtB < 0:
                    hurtB = 0
                clown -= hurt
                if hide[0] + hide[1] >= random.randint(1,100):
                    hurtB = 0
                hide[1] = 0
                health -= hurtB
                item_att = 0
                choose = input(f'敌方的攻击是{enemy_fight}')
                if clown_act > 3 :
                    choose = input('麻醉机械臂使用了防御!')
                if chooseb == 'B':
                    choose = input('因为你选择了防御,所以伤害不计入')
                elif MZ_B == 1:
                    input('你被麻醉机械臂麻醉了，你无法对敌人造成伤害！')
                else:
                    choose = input(f'你对敌方造成了{hurt}点伤害!')
                    hurt = 0
                choose = input(f'你被麻醉机械臂扣除了{hurtB}点血')
                dead_interface()
                if respawned == 1:
                    break
                hurtB = 0
                if chooseb == 'C':
                    choose = input(f'你的[{catch_C}%]逃脱了机械臂的捕捉！')
                    catch_B -= catch_C
                att_choose = 0
                choose = input(f'麻醉机械臂捕捉了你的[{catch_A}%]!')
                catch_B += catch_A
                if big_catch < 10:
                    big_catch = 10
                input(f'麻醉机械臂离捕捉你靠近了[{int(catch_A / 10)}%]！你当前的最大捕捉度为[{big_catch}%]')
                catch_A = 0
                if catch_B >= big_catch:
                    choose= input('你的HP减少了150，机械臂ATT上升[5-10]点！')
                    health -= 150
                    catch_D += random.randint(5,10)
                    if catch_D > 25:
                        catch_D = 25
                    dead_interface()
                    if respawned == 1:
                        respawned = 0
                        continue
                    choose = input('机械臂松开了。')
                    catch_B = 0
                MZ -= 1
                choose = input(f'你现在的累计捕捉度为[{catch_B}%]')
            if clown <= 0:
                choose = input('您获胜了!')
                CM_get = random.randint(5,1740)
                CM += CM_get
                choose = input(f'你获得了{CM_get}个CM币')
                win = 1
        if respawned == 1:
            respawned = 0
        output('你们斩断了机械臂，机械臂的一根手掌掉在地上。')
        output('“好恐怖……”昵称说。')
        savepoint = -4
    if savepoint == -4:
        save_data()
        output('你们穿过走廊，两边似乎有阴森的笑声。你们加快了脚步。')
        output('你们很快来到了走廊尽头，这是一个漆黑一片的房间，一个小小的水晶悬浮在空中，反射着异样的光芒。')
        output('“这就是……Complex？秘密武器？”So有些疑惑。')
        output('“不管怎么样，我们先拿走吧。”昵称说。')
        choose = input('你伸手触碰水晶，水晶似乎感应到了你的伸手，自动飞到了你的背包里')
        item.append('Complex')
        item.remove('能量核心 ')
        view_status()
        output('你们继续向前走去，一个电梯树立在你们前方。')
        output('“好家伙，我们赶快离开这里吧！”昵称说。')
        output('你们进入电梯，里面只有“1F”一个按钮。你按了下去来到了比特塔1楼')
        output('碧绿色的大厅出现在你们面前，你们顿时舒畅了很多。')
        output('你观察了一下电梯的位置，发现电梯位于一个巨大的雕塑后面。')
        output('“我们……现在去哪？”昵称问。')
        output('“我也不知道……这个东西看起来不像是我们能用的，既然Zero也不会用，我们……算了看看Zero是怎么想的。”')
        if cosh_A == 2:
            output('A：继续前进,B：去像素大街')
            while choose not in {'A','B'}:
                output('A：继续前进,B：去像素大街')
        else:
            choose = input('A：继续前进')
            savepoint = 20
            view_status()
            while choose != 'A':
                output('A：继续前进')
        if choose == 'A':
            output('你们继续前进')
        elif choose == 'B':
            output('你们前往像素大街')
            cosh_A = -1
        if cosh_A == -1:
            output('你们来到了像素大街2号的花园。你们重新站在屋子旁敲了敲门')
            output('诶哈哈，是Zero吧！亲爱的Zero，你有没有帮我把“零件”带来了呢？”')
            output('“已经带来了，你要干什么？”So叫道。')
            output('门应声打开，COSH从门厅里露了出来。')
            output('进来。”COSH说。')
            output('你们跟随COSH走进客厅，发现这里的陈设不是一般的杂乱。')
            output('“让我看看零件——叫Complex。”')
            output('你拿出了那个奇怪的紫色水晶。COSH两眼忽然冒出闪光。')
            output('“真的！！！真的！！！你们拿到了！！！你们击败了比特塔里那些鬼东西们拿到了！？！！！！？！”')
            choose = input('COSH打开一个像力场一样的东西，水晶顿时被收了进去')
            item.remove('Complex')
            view_status()
            output('COSH对你们说：“诶，其实你们没有能力使用这玩意儿——全世界能使用它的人不超过三个！！！让我操作操作！！！我会给你们整点大的！！！稍等。”')
            output('COSH说完后，你发现他站着的地板突然陷了下去，随后又恢复了原状。')
            output(' 你在屋子里随便走了走，突然被放在地板上一把激光枪的模型吸引住了')
            output('你会：A：不管他, B：放点东西在上面')
            while choose not in {'A','B'}:
                output('你会：A：不管他, B：放点东西在上面')
            if choose == 'A':
                output('你不管他')
            else:
                if '占位卡' not in 'item':
                    output('没有什么东西可放')
                else:
                    item.remove('占位卡')
                    output('你把占位卡放在了模型上面，突然，模型和占位卡开始融合起来。')
                    output('一把全新的激光枪摆在你面前（获得【毁灭激光枪】）')
                    item.append('毁灭激光枪')
            output('你在房间里转悠了一会儿，突然，你面前出现了一个显示屏：\n“来地下室找我。”')
            output('没等你反应过来，你脚下的地面突然向下陷去，你下降到了一个黑漆漆的地方。')
            output('你发现So和昵称也来到了这里。昵称对这次的突然袭击有点惊魂未定。')
            output('你发现前面出现了一道亮光。你们向前走去，发现一台巨大的机器摆在你们面前。')
            output('你看了看这个机器，一个紫色的发光方块摆在机器的前方，整个机器像许多奇怪的箱子组成的一条长长的大蛇，许多裸露在外的电线杂乱地绕在机器旁。')
            output('你刚想触碰这个机器，突然，机器的紫色方块晃了一下，把你吓了一跳。')
            output('你身边突然出现了一个蓝色的显示屏，显示屏随即分裂成两个、四个、八个，很快，你前面的区域出现了一座由显示屏组成的巨大蓝色屏障，无数数字在你面前跳动着，像沸腾的海水。')
            output('在这数据海洋之下，你面前的巨大机器突然做出了一个你难以想象的动作：组成它黑色的厢体瞬间解体成很薄的一片一片，电线四分五裂，这些薄片在你面前绕着紫色的方块旋转起来，重聚成了一个更加怪异的形状，好像一个愤怒的孩子三下两下捏成的橡皮泥娃娃，只不过……放大了很多倍。')
            output('你旁边的So和昵称似乎都有点呆住了，而你却听到了声音：')
            output('你的周围，许多声音混杂在一起，不过你基本听清了内容：')
            output('“TIS COSH！！！！！！！！！！”')
            print('那些完全不相同，邪恶的，恐怖的，又甚至是软绵绵的声音突然一同对你开口：')
            t.sleep(0.5)
            print('“神……”')
            t.sleep(0.5)
            print('“我将会成为神……”')
            t.sleep(0.5)
            print('“再也不用被世间的低俗娱乐所束缚了……”')
            t.sleep(0.5)
            print('“Complex的力量……”')
            t.sleep(0.5)
            output('“哈哈哈哈哈哈哈哈哈！！！Zero，你可是我的大恩人啊！！！我要好好地奖励你一番！！！”')
            output('“和我一起……我的观众……享受这份美好……享受这——无上的——快乐吧！！！”')
            output('声音突然放大，把你吓了一跳：')
            output('“先学会接受你的生死吧！”')
            print('【战斗开始】对战 COSH Complex')
            hucker = 0
            boom_snake = 0
            zero_H = ''
            zero_W = ''
            if S_up == 1:
                zero_H = 0
                zero_H = int(zero_H)
                zero_W = '护盾血量'
            big_fight = 0
            t.sleep(0.5)
            H_icecream = 0
            cosh = 3326
            cosh_talk_A = 1
            cosh_talk_B = 0
            cosh_fight = [0,5,random.randint(3,6)]
            nothing_fight = 0
            item_att = 0
            cosh_C = 0
            sans = 0
            check = 0
            snake_block = 0
            magic_point = 0
            miaomiao = 0
            coat = 0
            big_sans = 0
            win = 0
            a,b,c,d,e = '','','','',''
            magic_use = 0
            while win == 0:
                zero_att = 0
                magic_choose = 0
                att_choose = 0
                item_choose = 0
                while magic_choose == 0 and item_choose == 0:
                    if boom_snake > 0:
                        boom_snake -= 1
                        cosh -= 20
                        input('两只小电子蛇对敌人造成了20点伤害！')
                    chooseb = 'A'
                    if '战争宝石' in item:
                        print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health}{zero_W}{zero_H},暴击数{big_fight},COSH Complex血量为{cosh},攻击力为145,防御力为???,场上虚空度为{sans}')
                    if '战争宝石' not in item:
                        print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health}{zero_W}{zero_H},COSH Complex血量为{cosh},虚空度为{sans}')
                    if sans < 30:
                        choose = input('A,物品B,防御C,魔法D,跳过')
                    elif sans < 75 and sans >= 30:
                        choose = input('a_物品B,防御c,魔瞂D,跳+&过')
                    else:
                        choose = input('a_物?B,锟斤#拷-<,_魔瞂D,跳*&过')
                    while choose not in {'A','B','C','D'}:
                        choose = input('请做出你的选择')
                    if choose == 'A':
                        choose = input(f'你现在可使用的物品有{fight_item},请从1开始输入序号以选择使用的物品')
                        if choose not in {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'}:
                            choose = input('物品序号输入错误!')
                        else:
                            choose = int(choose)
                            if choose > len(fight_item):
                                choose = input('物品序号输入错误!')
                            else:
                                check = fight_item[choose]
                                item_find()
                                if check == '魔法炸药':
                                    input('你对COSH Complex造成了100点伤害!但你也不小心受到了30点伤害')
                                    health -= 30
                                    cosh -= 100
                                    dead_interface()
                                    if respawned == 1:
                                        break
                                if check == '坚硬冰棍':
                                    choose = input('你使用了坚硬冰棍!COSH Complex的HP降低了100点!')
                                    cosh -= 100
                                if check == '像素板':
                                    choose = input('你使用了像素板!COSH Complex受到了90点伤害！')
                                    cosh -= 90
                                if check in fight_item and check in item:
                                    item.remove(check)
                                    fight_item.remove(check)
                                if health > 300:
                                    health = 300
                    if choose == 'B':
                        if sans < 40:
                            choose = input('你选择了防御!')
                        else:
                            choose = input('你选择了FN*&###虚---空_____')
                        magic_point += 40
                        magic_choose = 1
                        if magic_point >= 100:
                            magic_point = 100
                        chooseb = 'B'
                    if choose == 'C':
                        bit_magic('normal')
                    elif choose == 'D':
                        choose = input('你跳过了你的回合')
                        magic_choose = 1
                if cosh_talk_A == 1:
                    cosh_talk_A = 0
                    input('So有点为难地问：“这玩意儿怎么打啊……”')
                    input('你听见那个声音答复了：“你居然妄想击败【我】？好啊，让我来陪你玩一玩……”')
                    input('“Complex的能量，会彻底改变你的战斗形式，认真点，我没在和你开玩笑！”')
                    input('“你现在需要面对一次全新的挑战！看着这些数字，如果你想进攻它们，你就需要弄点……与众不同的东西！否则——吃点苦头！”')
                    input('“可惜的是！！你光反击是没用的，你需要再限定的时间内击中我，否则……我将还给你你一发——更强的——攻击！只有你出招了，你才能知道你究竟有没有超时！”')
                    input('“直到完成这些考验，你才有正式面对我的机会！！！”')
                    input('“这些数字...或许我们需要进行一些与他们相反的攻击才能击破他们”So正在思考')
                cosh_fight[0] += 1
                C_time = 2.5
                C_number = 5
                C_hurt = 30
                if cosh_fight[0] >= 6:
                    C_number = 7
                    C_hurt = 50
                if cosh_fight[0] >= 10:
                    C_time = 3
                    C_number = 9
                    C_hurt = 70
                if cosh_fight[0] >= 14:
                    C_time = 3.4
                    C_number = 10
                    C_hurt = 80
                if cosh_fight[0] == 6 or cosh_fight[0] == 10:
                    input('COSH Complex加强了二进制数码的速度！')
                if cosh_fight[0] == 14:
                    input('COSH Complex的数码进入暴走状态！')
                cosh_attack = ''
                while len(cosh_attack) < C_number:
                    cosh_attack += random.choice(['0','1'])
                if cosh_fight[0] == 1:
                    print('首回合限定,两秒后你需要迅速开始对二进制字符进行反制')
                    t.sleep(2.0)
                t1 = t.time()
                hurtB = 0
                if sans < 65:
                    choose = input(f'数据的洪流以{cosh_attack}的形式向你进攻而来！')
                elif 65 <= sans and sans < 80:
                    choose = input(f'NUM-(**&ne的{cosh_attack}的形式_进攻而来')
                else:
                    choose = input(f'NUM0011012?(**&ne的{cosh_attack}.type_进攻->')
                while choose == '':
                    choose = input('请重新输入！')
                t2 = t.time()
                if t2 - t1 >= C_time:
                    fight_talk = random.randint(1,3)
                    if fight_talk == 1:
                        input(f'“ZE--RO,你--超时啦！[HP-{C_hurt}]”')
                    if fight_talk == 2:
                        input(f'“你太慢了！！[HP-{C_hurt}]”')
                    if fight_talk == 3:
                        input(f'“天啊！！难道你想让观众们老死吗？！！[HP-{C_hurt}]”')
                    health -= C_hurt
                else:
                    chance = 0
                    co = len(choose)
                    if co >= C_number:
                        co = C_number
                    if co < C_number:
                        hurtB += 10 * (len(cosh_attack) - co)
                    while chance < co:
                        hurtB += 10
                        if (choose[chance] == '0' and cosh_attack[chance] == '1') or (choose[chance] == '1' and cosh_attack[chance] == '0'):
                            hurtB -= 10
                        chance += 1
                    if sans < 70:
                        input(f'二进制的洪流对你造成了{hurtB}点伤害')
                    else:
                        input(f'2010001#&CHH你造成了{hurtB}点ATD#???*T')
                    if chooseb != 'B':
                        if hurtB == 0:
                            sans += 3
                        else:
                            sans += 1
                    health -= hurtB
                if nothing_fight == 0:
                    car_act_B = random.randint(1,11)
                else:
                    car_act_B = random.randint(12,15)
                if cosh < 500:
                    sans = big_sans
                big_sans = sans
                if '混乱护盾' in armor:
                    health += random.randint(3,20)
                    if health >= 300:
                        health = 300
                if H_icecream > 0:
                    H_icecream -= 1
                    health -= 20
                if car_act_B == 1:
                    input('COSH Complex形态堂堂出击！')
                if car_act_B == 2:
                    input('混沌风暴开始侵蚀你')
                if car_act_B == 3:
                    input('海量的显示屏投影着数据')
                if car_act_B == 4:
                    input('不需要理会这些，尽管冲吧！')
                if car_act_B == 5:
                    input('不可直视神！！！')
                if car_act_B == 6:
                    input('你需要更多的挑战！！！')
                if car_act_B == 7:
                    input('神！！！神的力量开始光顾这儿！')
                if car_act_B == 8:
                    input('虚空中的混沌组成了扭曲的高维矩阵')
                if car_act_B == 9:
                    input('祝你好运！Zero！')
                if car_act_B == 10:
                    input('COSH = complex(#i0100010)---Error')
                if car_act_B == 11:
                    input('我的天——发生什么了——')
                #以下为大招对话
                if car_act_B == 12:
                    input('最后的风暴——已完全到来！')
                if car_act_B == 13:
                    input('虚空！虚空！虚空！')
                if car_act_B == 14:
                    input('侵略与毁灭，无视它吧！')
                if car_act_B == 15:
                    input('已经竭尽全力了！')
                if cosh > 0:
                    if (cosh < 500 or sans > 82) and nothing_fight == 0:
                        nothing_fight = 1
                    if '零剑' in weapon:
                        zero_att = random.randint(5,50)
                    if 'Complex机甲长剑' in weapon and random.randint(1,10) == 3:
                        zero_att += 10
                    cosh_fight[1] -= 1
                    cosh_fight[2] -= 1
                    if cosh_fight[1] == 0 and cosh_fight[2] == 0:
                        cosh_fight[1] += 1
                    if nothing_fight == 1 or (nothing_fight == 2 and random.randint(1,6) == 4):
                        nothing_fight = 2
                        input('你面前的空间似乎有点虚无飘渺……')
                        input('“COSH Complex使用了虚空之刃！接下来场面将充满轰炸与斩击！！！”')
                        cosh_chance = 9
                        cosh_att = 10
                        while cosh_chance > 0:
                            cosh_chance -= 1
                            C_number = random.randint(5,9)
                            if cosh_chance == 0:
                                C_number = 20
                                input('最终的恐怖攻击即将到来！！！')
                            cosh_attack = ''
                            chance = 0
                            while len(cosh_attack) < C_number:
                                cosh_attack += random.choice(['0','1'])
                            t1 = t.time()
                            choose = input(f'虚空之刃以{cosh_attack}的形式向你袭来！请防御！')
                            while choose == '':
                                choose = input('请重新输入！')
                            t2 = t.time()
                            if (t2 - t1 >= 2 and len(cosh_attack) <= 6) or (t2 - t1 >= 2.5 and len(cosh_attack) > 6 and len(cosh_attack) < 15) or (t2 - t1 >= 5 and len(cosh_attack) == 20):
                                print('虚空之刃贯穿了你的身体[HP/2]')
                                health //= 2
                                t.sleep(0.1)
                            else:
                                hurtB = 0
                                chance = 0
                                co = len(choose)
                                if co >= C_number:
                                    co = C_number
                                if co < C_number:
                                    hurtB += 10 * (len(cosh_attack) - co)
                                while chance < co:
                                    hurtB += cosh_att
                                    if (choose[chance] == '0' and cosh_attack[chance] == '1') or (choose[chance] == '1' and cosh_attack[chance] == '0'):
                                        hurtB -= 10
                                    chance += 1
                                if hurtB == 0:
                                    sans += 1
                                    cosh -= 20
                                else:
                                    if random.randint(1,2) == 1:
                                        sans += 1
                                print(f'虚空之刃对你造成了{hurtB}点伤害!')
                                t.sleep(0.1)
                                health -= hurtB
                                if health <= 0:
                                    health = 1
                    elif cosh_fight[1] == 0:
                        cosh_fight[1] = 5
                        input('我希望你还记得这个！')
                        Q_number = ''
                        chanceb = 4
                        if random.randint(0,1) == 0:
                            chance = 10
                            while len(Q_number) < chance:
                                x = random.randint(1,4)
                                a = chr(ord('A') + x - 1)
                                Q_number += a
                            answer = []
                            answer_A = ''
                            while len(answer_A) < chance:
                                a = len(answer_A)
                                if Q_number[a] == 'A':
                                    answer_A += 'D'
                                if Q_number[a] == 'B':
                                    answer_A += 'A'
                                if Q_number[a] == 'C':
                                    answer_A += 'B'
                                if Q_number[a] == 'D':
                                    answer_A += 'C'
                            answer.append(answer_A)
                            right_answer = answer_A
                            count = 0
                            while count < 3:
                                answer_A = ''
                                count += 1
                                while len(answer_A) < chance:
                                    x = random.randint(1,4)
                                    answer_A += chr(ord('A') + x - 1)
                                answer.append(answer_A)
                        else:
                            chance = 20
                            while len(Q_number) < chance:
                                Q_number += random.choice(['0','1'])
                            answer = []
                            answer_A = ''
                            while len(answer_A) < chance:
                                a = len(answer_A)
                                if Q_number[a] == '1':
                                    answer_A += '0'
                                if Q_number[a] == '0':
                                    answer_A += '1'
                            answer.append(answer_A)
                            right_answer = answer_A
                            count = 0
                            while count < 3:
                                answer_A = ''
                                count += 1
                                while len(answer_A) < chance:
                                    answer_A += random.choice(['0','1'])
                                answer.append(answer_A)
                        tihao = random.randint(1,1000)
                        random.shuffle(answer)
                        A_c = answer[0]
                        B_c = answer[1]
                        C_c = answer[2]
                        D_c = answer[3]
                        t1 = t.time()
                        if sans < 62:
                            choose = input(f'题号：{tihao}想要全克制以下{Q_number}，标准的回答是：\nA：{A_c}\nB：{B_c}\nC：{C_c}\nD：{D_c}')
                        else:
                            choose = input(f'_题#号：-{tihao}想要`克制以下{Q_number}，标准的回答是：\nA：{A_c}\nB：{B_c}\nC：!<[链接已屏#@=_蔽]\nD：{D_c}')
                        while choose not in {'A','B','C','D'}:
                            choose = input('请输入正确格式的输入！')
                        t2 = t.time()
                        t3 = t2 - t1
                        if (choose == 'A' and A_c == right_answer) or (choose == 'B' and B_c == right_answer) or (choose == 'C' and C_c == right_answer) or (choose == 'D' and D_c == right_answer):
                            if t3 > 8:
                                input('真遗憾，你超时啦！”[HP/2]')
                                health //= 2
                            else:
                                talk = random.randint(1,2)
                                sans += 2
                                if talk == 1:
                                    input('看来你没有忘记！')
                                if talk == 2:
                                    input('难以置信！！漂亮的回答！')
                        else:
                            input('真遗憾，你答错啦！[HP/2]')
                            health //= 2
                    elif cosh_fight[2] == 0:
                        challenge = random.randint(1,3)
                        cosh_fight[2] = random.randint(2,5)
                        if challenge != 1:
                            input('COSH把你拉进了无限的虚空中！')
                            input('下面，越快越好，迎接来自虚空的数据风暴吧！')
                            cosh_chance = 5
                            cosh_att = 10
                            while cosh_chance > 0:
                                cosh_chance -= 1
                                C_number = random.randint(3,7)
                                cosh_attack = ''
                                chance = 0
                                while len(cosh_attack) < C_number:
                                    if random.randint(1,2) == 1:
                                        cosh_attack += '0'
                                    else:
                                        cosh_attack += '1'
                                t1 = t.time()
                                choose = input(f'数据风暴以{cosh_attack}的形式向你进攻而来！请防御！')
                                while choose == '':
                                    choose = input('请重新输入！')
                                t2 = t.time()
                                if t2 - t1 >= 2.5:
                                    fight_talk = random.randint(1,3)
                                    if fight_talk == 1:
                                        input(f'“ZE-RO,你--超时啦！[HP减半]”')
                                    if fight_talk == 2:
                                        input(f'“你的身体被无数二进制数据穿透而过[HP减半]”')
                                    if fight_talk == 3:
                                        input(f'“天啊！！难道你想让观众们老死吗？！！[HP减半]”')
                                    health /= 2
                                    health = int(health)
                                else:
                                    hurtB = 0
                                    chance = 0
                                    co = len(choose)
                                    if co >= C_number:
                                        co = C_number
                                    if co < C_number:
                                        hurtB += 10 * (len(cosh_attack) - co)
                                    while chance < co:
                                        hurtB += cosh_att
                                        if (choose[chance] == '0' and cosh_attack[chance] == '1') or (choose[chance] == '1' and cosh_attack[chance] == '0'):
                                            hurtB -= cosh_att
                                        chance += 1
                                    if hurtB == 0:
                                        if random.randint(1,2) == 1:
                                            sans += 1
                                        cosh -= 20
                                    else:
                                        if random.randint(1,3) == 1:
                                            sans += 1
                                    input(f'二进制的洪流对你造成了{hurtB}点伤害')
                                    if S_up == 1:
                                        if zero_H > 0:
                                            zero_H -= hurtB
                                        else:
                                            health -= hurtB
                                    else:
                                        health -= hurtB
                                    if health <= 0:
                                        health = 1
                                cosh_att += 5
                        else:
                            input('虚空竞技场（Challenge）正式开始啦！！！')
                            if cosh_talk_B == 0:
                                cosh_talk_B = 1
                                input('根据二进制的克制规则，进行正确的攻击，你就可以获得——超豪华的ATT礼包哦！！！')
                                input('当然，假如你输错或者超时了……嘻嘻嘻！！！')
                            input('输少了没有关系，但是切记...不要贪心呦！！')
                            C_time = random.randint(6,9)
                            C_number = random.randint(55,150)
                            cosh_attack = ''
                            chance = 0
                            while len(cosh_attack) < C_number:
                                if random.randint(1,2) == 1:
                                    cosh_attack += '0'
                                else:
                                    cosh_attack += '1'
                            t1 = t.time()
                            choose = input(f'那么，限时{C_time}秒,本回合Challenge，{cosh_attack}现在开始！')
                            t2 = t.time()
                            if t2 - t1 >= C_time:
                                fight_talk = random.randint(1,2)
                                if fight_talk == 1:
                                    input(f'“ZERO,你太贪心啦！[HP减半]”')
                                if fight_talk == 2:
                                    input(f'数以百计的二进制字符串迎面而过[HP减半]')
                                health //= 2
                            else:
                                hurtB = 0
                                hurt = 0
                                chance = 0
                                co = len(choose)
                                if co >= C_number:
                                    co = C_number
                                n = 1
                                while chance < co:
                                    if (choose[chance] == '0' and cosh_attack[chance] == '0') or (choose[chance] == '1' and cosh_attack[chance] == '1'):
                                        n += 1
                                        if n != 0:
                                            hurtB += 2 ** n * 5
                                    else:
                                        hurt += 15
                                    chance += 1
                                if hurtB == 0:
                                    if random.randint(1,2) == 1:
                                        sans += 1
                                else:
                                    if random.randint(1,3) == 1:
                                        sans += 1
                                cosh -= hurt
                                input(f'二进制的洪流对你造成了{hurtB}点伤害')
                                input(f'你对COSH Complex造成了{hurt}点伤害')
                                if S_up == 1:
                                    if zero_H > 0:
                                        zero_H -= hurtB
                                    else:
                                        health -= hurtB
                                else:
                                    health -= hurtB
                                if health <= 0:
                                    health = 1
                    else:
                        x = random.randint(1,4)
                        a = chr(ord('A') + x - 1)
                        x = random.randint(1,4)
                        b = chr(ord('A') + x - 1)
                        x = random.randint(1,4)
                        c = chr(ord('A') + x - 1)
                        x = random.randint(1,4)
                        d = chr(ord('A') + x - 1)
                        x = random.randint(1,4)
                        e = chr(ord('A') + x - 1)
                        if miaomiao == 4:
                            b,c,d,e = a
                        enemy_fight = a+b+c+d+e
                        enemy_fighta = [a,b,c,d,e]
                        zero_att = 0
                        if sans < 82:
                            choose = list(input(f'请选择你对COSH Complex的攻击!(5个一组,由五个大写字母构成)'))
                        else:
                            choose = list(input(f'请Ch00_E你对C_SH Co plex的攻击?#'))
                        hurt = 0
                        hurtB = 0
                        chance = 0
                        wrong = 0
                        while wrong == 0:
                            wrong = 1
                            if len(choose) != 5:
                                wrong = 0
                            elif choose[0] not in {'A','B','C','D'}:
                                wrong = 0
                            elif choose[1] not in {'A','B','C','D'}:
                                wrong = 0
                            elif choose[2] not in {'A','B','C','D'}:
                                wrong = 0
                            elif choose[3] not in {'A','B','C','D'}:
                                wrong = 0
                            elif choose[4] not in {'A','B','C','D'}:
                                wrong = 0
                            if wrong == 0:
                                if sans < 50:
                                    print('输入错误,请依照格式输入!')
                                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                                elif sans >= 50 and sans < 82:
                                    print('输入错错_错EOR,请依照格式输入')
                                    choose = list(input(f'请选择你的攻击!(5个 组,由五个大_%N构成)'))
                                else:
                                    print('&&&#|误？》请>>inp#?_True')
                                    choose = list(input(f'请选&择___你的SyntaxError: EOL while scanning string literal'))
                        else:
                            while chance < 5:
                                f = choose.pop()
                                g = enemy_fighta.pop()
                                if chooseb != 'B':
                                    if (f == 'A' and g == 'B') or (f == 'B' and g == 'C') or (f == 'C' and g == 'D') or (f == 'D' and g == 'A'):
                                        hurt += att
                                        hurt += 50
                                        chance += 1
                                        if att_choose == 1:
                                            hurt += 5
                                            if '战争宝石' in item:
                                                hurt += 5
                                        hurt += item_att
                                        hurt += zero_att
                                        if miaomiao == 3:
                                            hurt += random.randint(10,50)
                                        if hucker == 1:
                                            hurt += 10
                                        laser(0)
                                if (f == 'D' and g == 'C') or (f == 'C' and g == 'B') or (f == 'B' and g == 'A') or (f == 'A' and g == 'D'):
                                    hurtB += 39
                                    if chooseb == 'B':
                                        hurtB -= Def
                                        if hucker == 1:
                                            hurtB -= 30
                                        if hurtB < 0:
                                            hurtB = 0
                                    chance += 1
                                else:
                                    chance += 1
                            if hide[0] + hide[1] >= random.randint(1,100):
                                hurtB = 0
                            hide[1] = 0
                            if coat == 1:
                                if random.randint(1,10) == 5:
                                    hurtB = 0
                                elif coat == 1:
                                    health += 10
                            if random.randint(1,20) == 3 and '战争宝石' in item and att_choose == 1:
                                hurt *= 3
                            if miaomiao == 1:
                                hurtB /= 2
                            if miaomiao == 2:
                                hurtB /=5
                            hurtB = int(hurtB)
                            if check == '冰冻面包':
                                hurtB = 0
                                check = ''
                            if S_up == 1:
                                if zero_H > 0:
                                    zero_H -= hurtB
                                else:
                                    health -= hurtB
                            else:
                                health -= hurtB
                            item_att = 0
                            choose = input(f'COSH Complex的攻击是{enemy_fight}')
                            cosh -= hurt
                            if chooseb == 'B':
                                choose = input('因为你选择了防御,所以伤害不计入')
                            else:
                                if cosh < 70:
                                    input(f'你对COSH Complex造成了{hurt}点伤害！')
                                else:
                                    input(f'Z#?AAA对CO_H Complex造成成成了{hurt}点伤害')
                            hurt = 0
                            if sans < 80:
                                choose = input(f'你被COSH Complex扣除了{hurtB}点血')
                            else:
                                error_A = random.randint(1,299)
                                error_B = random.randint(1,111)
                                choose = input(f'你被SP??nh Complex扣除[-{error_A}.#%33^3+6.{error_B}i(0/#0!!))点血')
                            dead_interface()
                            if respawned == 1:
                                break
                if cosh < 500 and cosh_C == 0:
                    input('COSH看上去有点虚弱。')
                    cosh_C = 1
                if S_up == 1:
                    if zero_H < 0:
                        zero_H = 0
                coat = 0
                miaomiao = 0
                if cosh <= 0 or sans >= 100:
                    if sans >= 100:
                        input('你面前的空间似乎虚无化了起来！')
                    choose = input('您获胜了!')
                    CM += 1450
                    choose = input(f'你获得了1450个CM ‘Cosin’')
                    win = 1

            if respawned == 1:
                respawned = 0
                continue

            output('COSH Complex发出了巨大而恐怖的怪笑：“你以为这就结束了？虚空！虚空！我将会获得一切……一切……”')
            choose = input('你看见它的身体突然开始旋转、解体，化作无数的尘埃。声音从尘埃中传来：\n“嘻嘻嘻嘻，在你们看来，你们击败了我，可是，我获得的可是无限呢——嘿嘿，我，COSH！成功了！我终于摆脱了这个世界！！！变态的世界——嘿嘿！！！再见吧！！！”')
            view_status()
            choose = input('尘埃以惊人的速度旋转着，最后，一道紫光在你们面前闪烁着。你们听到了COSH最后的声音：\n“交易魔法！！！哈哈！！！”')
            view_status()
            output('紫光吞没了你。')
            output('你们醒了过来，发现自己躺在COSH的大厅里。')
            if sans >= 100:
                choose = input('你突然发现前面出现了一把小刀（获得【零剑-II】）')
                if '零剑' in item:
                    item.remove('零剑')
                item.append('零剑-II')
                view_status()
            else:
                choose = input('你突然发现前面出现了一把重剑（获得【虚空之刃】）')
                item.append('虚空之刃')
                view_status()
            output('你们走出COSH的房子，你发现花园前面站着一个推着除草机的机器人')
            output('你会：A：不管他，B：随便问几句')
            while choose not in {'A','B'}:
                output('你会：A：不管他，B：随便问几句')
            if choose == 'A':
                output('你不管他')
            elif choose == 'B':
                output('那机器人看到你们，说：“你问我COSH啊……我告诉你我知道的吧……”')
                output('我是他的朋友，当时也是电视节目主持人。只不过我是新闻节目的主持人，COSH是娱乐节目主持人。')
                output('我的业绩非常的惨淡，几乎只能够我自己使用，而COSH靠着他的娱乐节目，收视率一涨再涨，事业非常的成功。')
                output('然而，虽然COSH的娱乐节目很火爆，但……嫉妒的人也非常多，可是COSH他……并没有什么很恶劣的私生活行为，黑料太少，因此大家都拿他没办法。')
                output('然而，就在他的娱乐事业发展到最顶峰时，他却出了车祸。这城市全是飞车，车祸很少见，偏偏发生在他身上。')
                output('COSH因为车祸受了重伤，他被迫住院了两个月，而在这个时候，COSH的娱乐节目策划非常不人道地，以不再能胜任主持工作为由，把他炒掉了。”')
                output('一连串的打击使COSH非常沮丧，但他没有一蹶不振，我去看望他时，他说要从头做起，努力地干出之前的业绩。可惜令我没想到的是，我去看望他的几天之后，他就疯了。')
                output('我不知道发生了什么，我听医院的通讯工作人员说，COSH住院时，曾有人试图超距离联系COSH，当工作人员发现并试图追踪时，联系停止了。在这之后，COSH就疯了。')
                output('至于我，过了不久，就因为太过惨淡的收视率而被我的上司辞退，COSH疯了不能照顾自己，但他还算有钱。    我就到他家打点零工赚点小钱，虽然……他说的话我一句都听不懂。有一次他在我旁边大谈特谈“收视率虚空”，我从来都没有听过这个词。')
                output('好了，我要干活去了，希望你们……不会像COSH这样吧。”')
                output('你们重新回到了比特塔。')
                output('“我们……继续前进吧……”')
        savepoint = 20
    if savepoint == 20:
        save_data()
        output('你们进入电梯，电梯里只有“61F”一个按钮。')
        output('“这么高！”So感叹道。')
        output('你们按下按钮，电梯的周围出现了许多道光束，光束开始缓慢旋转起来。从感受到的加速度来看，你们正在上升。')
        output('你会：A：休息一下，B：看看旁边的光束')
        while choose not in {'A','B'}:
            output('你会：A：休息一下，B：看看旁边的光束')
        if choose == 'A':
            output('电梯足够大，你坐下休息了一会儿[HP+50]')
            health += 50
        elif choose == 'B':
            output('你看了看旁边的光束，一个显示屏在光束上出现，上面写着许多关于比特塔的信息。')
            output('正当你想进一步看时，另一个显示屏突然覆盖在了原先的显示屏上，上面写着：“被骗了吧！哈哈！”')
            output('你想都不用想就知道这是谁干的。')
        output('过一会儿，电梯停了下来，你们从打开的电梯门走了出去。')
        output('你们的前面出现一座宽敞的小房间，由于四周突然冒出了淡淡的来苏水气味，你顿时感觉这里有点像医院。')
        output('你会：A：向前走,B：看看旁边有什么')
        while choose not in {'A','B'}:
            output('你会：A：向前走,B：看看旁边有什么')
        if choose == 'B':
            output('房间里几乎空无一物，只有一个孤零零的自助售货机，')
            output('你看向售货机，上面写着：“能量饮料，200RS币可购买，限购一个！”')
            output('要买吗？A：买,B：不买')
            if choose not in {'A','B'}:
                output('要买吗？A：买,B：不买')
            if choose == 'B':
                output('你离开了售货机。')
            elif choose == 'A':
                if CM >= 200:
                    output('你购买了能量饮料（获得【能量饮料】）')
                    CM -= 200
                elif CM < 200:
                    output('你的钱不够！')
        output('你们向前穿过房间，前面出现了一个巨大的显示屏，上面写着“比特塔地图”')
        output('“有地图诶……恐怕是个圈套，我们快走。”So说。')
        output('你向前来到了一个小房间里，房间的左边、前面和右边各有一个门。')
        output('“刚才的地图上标着……左边是个死胡同，前面和右边的路会汇聚成一条，我们去哪？”So问')
        snake_F = 0
        output('你会：A：前往左边的房间,B：前往右边的房间,C：前往前面的房间,D：后退')
        go = 0
        while go == 0:
            while choose not in {'A','B','C','D'}:
                output('你会：A：前往左边的房间,B：前往右边的房间,C：前往前面的房间,D：后退')
            if choose == 'A':
                snake_F = 1
                output('你来到了左边的房间，这里光线阴暗，许多机器杂乱无章地摆在这里，房间的正中央是一个巨大的试剂瓶。')
                output('你仔细看了看周围，并没有发现出口。')
                output('突然，你的周围传来“嘶嘶嘶”的声音，你感到有些不对劲，快速离开了房间')
            elif choose == 'B':
                output('你的前面出现了一条长长的走廊，地上放着一块面包（获得【冰冻面包】）')
                go = 1
                item.append('冰冻面包')
                fight_item.append('冰冻面包')
            elif choose == 'C':
                go = 1
                output('你来到了一条普通的走廊，这条走廊向右汇合到一条长长的走廊中')
            elif choose == 'D':
                output('你向后走去，巨大的地图已经消失，你的后面传来嘈杂的响声。你们感到有些不对劲，顿时回到前面的房间。')
        output('你们沿着长长的走廊快速向前走去，突然，你发现走廊的旁边有一些显示屏。')
        output('你会：A：不管他,B：阅读显示屏')
        while choose not in {'A','B:'}:
            output('你会：A：不管他,B：阅读显示屏')
        if choose == 'A':
            output('你们继续向前赶路')
        elif choose == 'B':
            output('你看了看显示屏，上面写着：“电子蛇定期喂食时间：早7:00、晚7:00')
        if snake_F == 1:
            output('突然，你们后面传来嘈杂的嘶嘶声，几条通体发红的电子蛇一下冲到了你们的前面。')
            output('“我的天！这么快！”So说。')
            output('你们快速摆好姿势迎战向你们逼近的红电子蛇')
            print('战斗开始,对战精英电子蛇*2')
            hucker = 0
            boom_snake = 0
            zero_H = ''
            zero_W = ''
            item_att = 0
            if S_up == 1:
                zero_H = 0
                zero_H = int(zero_H)
                zero_W = '护盾血量'
            big_fight = 0
            t.sleep(0.5)
            magic_use = 0
            car_A,car_B = 477,477
            H_icecream = 0
            check = 0
            magic_point = 0
            miaomiao = 0
            coat = 0
            win = 0
            snake_block = 0
            snake_run = [random.randint(3,5),random.randint(3,5)]
            a,b,c,d,e = '','','','',''
            while win == 0:
                zero_att = 0
                magic_choose = 0
                att_choose = 0
                item_choose = 0
                while magic_choose == 0 and item_choose == 0:
                    if boom_snake > 0:
                        boom_snake -= 1
                        car_A -= 20
                        car_B -= 20
                        input('两只小电子蛇对敌人造成了20点伤害！')
                    if car_A <= 0:
                        car_A = 0
                    if car_B <= 0:
                        car_B = 0
                    chooseb = 'A'
                    if '战争宝石' in item:
                        print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health}{zero_W}{zero_H},精英电子蛇A血量为{car_A},攻击力为27，精英电子蛇B血量为{car_B},攻击为27，暴击数{big_fight}')
                    if '战争宝石' not in item:
                        print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health}{zero_W}{zero_H},精英电子蛇A血量为{car_A},精英电子蛇B血量为{car_B}')
                    if snake_block == 0:
                        choose = input('A,物品B,防御C,魔法D,跳过')
                        while choose not in {'A','B','C','D'}:
                            print('请做出你的选择')
                            choose = input('A,物品B,防御C,魔法D,跳过')
                        if choose == 'A':
                            choose = input(f'你现在可使用的物品有{fight_item},请从1开始输入序号以选择使用的物品')
                            if choose not in {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'}:
                                choose = input('物品序号输入错误!')
                            else:
                                choose = int(choose)
                                if choose > len(fight_item):
                                    choose = input('物品序号输入错误!')
                                else:
                                    check = fight_item[choose]
                                    item_find()
                                    if check == '魔法炸药':
                                        input('你对对方造成了100点伤害!但你也不小心受到了30点伤害')
                                        health -= 30
                                        car_A -= 100
                                        car_B -= 100
                                        dead_interface()
                                        if respawned == 1:
                                            break
                                    if check == '坚硬冰棍':
                                        choose = input('请选择投掷的对象（填A或者B）')
                                        while choose not in {'A','B'}:
                                            choose = input('请选择投掷的对象（填A或者B）')
                                        if choose == 'A':
                                            choose = input('你使用了坚硬冰棍!精英电子蛇A的HP降低了100点!')
                                            car_A -= 100
                                        else:
                                            choose = input('你使用了坚硬冰棍!精英电子蛇B的HP降低了100点!')
                                            car_B -= 100
                                    if check == '像素板':
                                        choose = input('你使用了像素板!精英电子蛇受到了70点伤害！')
                                        car_A -= 70
                                        car_B -= 70
                                    item_choose = 1
                                    if health > 300:
                                        health = 300
                        if choose == 'B':
                            choose = input('你选择了防御!')
                            magic_point += 40
                            magic_choose = 1
                            if magic_point >= 100:
                                magic_point = 100
                            chooseb = 'B'
                        if choose == 'C':
                            bit_magic('normal')
                        elif choose == 'D':
                            choose = input('你跳过了你的回合')
                    magic_choose = 1
                if snake_block == 1:
                    choose = input('A:丢弃方块')
                    while choose != 'A':
                        choose = input('A:丢弃方块')
                    chooseb = 'B'
                    snake_block = 0
                    health -= 10
                    dead_interface()
                    if respawned == 1:
                        break
                car_act_B = random.randint(1,8)
                if '混乱护盾' in armor:
                    health += random.randint(3,20)
                    if health >= 300:
                        health = 300
                if H_icecream > 0:
                    H_icecream -= 1
                    health -= 20
                if car_act_B == 1:
                    input('电子蛇绕成一圈，你们不知道在玩什么花样')
                if car_act_B == 2:
                    input('电子蛇发出来特有的嘶嘶声')
                if car_act_B == 3:
                    input('你们闻到一股棉花味')
                if car_act_B == 4:
                    input('电子蛇对你们目露凶光')
                if car_act_B == 5:
                    input('电子蛇不希望看到捕蛇圈')
                if car_act_B == 6:
                    input('电子蛇希望你们能养它们')
                if car_act_B == 7:
                    input('电子蛇有点想逃走')
                if car_A > 0:
                    snake_run[0] -= 1
                    if snake_run[0] == 1:
                        input('电子蛇开始卷缩着身体')
                    if snake_run[0] == 0:
                              input('电子蛇向你冲来！')
                    x = random.randint(1,4)
                    a = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    b = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    c = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    d = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    e = chr(ord('A') + x - 1)
                    if miaomiao == 4:
                        b,c,d,e = a
                    enemy_fight = a+b+c+d+e
                    enemy_fighta = [a,b,c,d,e]
                    zero_att = 0
                    if '零剑' in weapon:
                        zero_att = random.randint(5,50)
                    if '零剑-II' in weapon:
                        zero_att = random.randint(30,70)
                    if 'Complex机甲长剑' in weapon and random.randint(1,10) == 3:
                        zero_att = 10
                    choose = list(input(f'请选择你对精英电子蛇A的攻击!(5个一组,由五个大写字母构成)'))
                    hurt = 0
                    hurtB = 0
                    chance = 0
                    wrong = 0
                    while wrong == 0:
                        wrong = 1
                        if len(choose) != 5:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[0] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[1] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[2] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[3] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[4] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    else:
                        cube_act = random.randint(1,100)
                        while chance < 5:
                            f = choose.pop()
                            g = enemy_fighta.pop()
                            if chooseb != 'B':
                                if (f == 'A' and g == 'B') or (f == 'B' and g == 'C') or (f == 'C' and g == 'D') or (f == 'D' and g == 'A'):
                                    hurt += att
                                    chance += 1
                                    if att_choose == 1:
                                        hurt += 5
                                        if '战争宝石' in item:
                                            hurt += 5
                                    if '虚空之刃' in weapon and random.randint(1,5) == 2:
                                        hurt += int(car_A/5)
                                    if cube_act <= 27:
                                        hurt -= 27
                                        laser(27)
                                    else:
                                        laser(0)
                                    hurt += item_att
                                    hurt += zero_att
                                    if miaomiao == 3:
                                        hurt += random.randint(10,50)
                                    if hucker == 1:
                                        hurt += 10
                            if (f == 'D' and g == 'C') or (f == 'C' and g == 'B') or (f == 'B' and g == 'A') or (f == 'A' and g == 'D'):
                                hurtB += 27
                                if chooseb == 'B':
                                    hurtB -= Def
                                    if hucker == 1:
                                        hurtB -= 30
                                    if hurtB < 0:
                                        hurtB = 0
                                chance += 1
                                if coat == 1 and random.randint(1,10) == 5:
                                    hurtB = 0
                                else:
                                    health += 10
                            else:
                                chance += 1
                        if hide[0] + hide[1] >= random.randint(1,100):
                            hurtB = 0
                        if snake_run[0] == 1:
                            hurtB = 0
                        if snake_run[0] == 0:
                            hurtB *= 2
                            snake_run[0] = random.randint(3,5)
                        if random.randint(1,20) == 3 and '战争宝石' in item and att_choose == 1:
                            hurt *= 3
                        if miaomiao == 1:
                            hurtB /= 2
                        if miaomiao == 2:
                            hurtB /=5
                        hurtB = int(hurtB)
                        if S_up == 1:
                            if zero_H > 0:
                                zero_H -= hurtB
                            else:
                                health -= hurtB
                        else:
                            health -= hurtB
                        item_att = 0
                        choose = input(f'精英电子蛇A的攻击是{enemy_fight}')
                        if cube_act <= 27:
                            choose = input('精英电子蛇A使用了防御!')
                        if chooseb != 'B':
                            choose = input(f'你对精英电子蛇A造成了{hurt}点伤害!')
                            car_A -= hurt
                            hurt = 0
                        if chooseb == 'B':
                            choose = input('因为你选择了防御,所以伤害不计入')
                       
                        choose = input(f'你被敌人扣除了{hurtB}点血')
                        dead_interface()
                        if respawned == 1:
                            break
                        if random.randint(1,10) <= 1:
                            choose = input('电子蛇身上的方块脱落了！')
                            snake_block = 1
                if car_B > 0:
                    snake_run[1] -= 1
                    if snake_run[1] == 1:
                        input('电子蛇开始卷缩着身体')
                    if snake_run[1] == 0:
                              input('电子蛇向你冲来！')
                    x = random.randint(1,4)
                    a = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    b = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    c = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    d = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    e = chr(ord('A') + x - 1)
                    if miaomiao == 4:
                        b,c,d,e = a
                    enemy_fight = a+b+c+d+e
                    enemy_fighta = [a,b,c,d,e]
                    zero_att = 0
                    if '零剑' in weapon:
                        zero_att = random.randint(5,50)
                    if '零剑-II' in weapon:
                        zero_att = random.randint(30,70)
                    if 'Complex机甲长剑' in weapon and random.randint(1,10) == 3:
                        zero_att += 10
                    choose = list(input(f'请选择你对精英电子蛇B的攻击!(5个一组,由五个大写字母构成)'))
                    hurt = 0
                    hurtB = 0
                    chance = 0
                    wrong = 0
                    while wrong == 0:
                        wrong = 1
                        if len(choose) != 5:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[0] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[1] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[2] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[3] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[4] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    else:
                        cube_act = random.randint(1,100)
                        while chance < 5:
                            f = choose.pop()
                            g = enemy_fighta.pop()
                            if chooseb != 'B':
                                if (f == 'A' and g == 'B') or (f == 'B' and g == 'C') or (f == 'C' and g == 'D') or (f == 'D' and g == 'A'):
                                    hurt += att
                                    chance += 1
                                    if att_choose == 1:
                                        hurt += 5
                                        if '战争宝石' in item:
                                            hurt += 5
                                    if '虚空之刃' in weapon and random.randint(1,5) == 2:
                                        hurt += int(car_A/5)
                                    if cube_act <= 27:
                                        hurt -= 27
                                        laser(27)
                                    else:
                                        laser(0)
                                    hurt += item_att
                                    hurt += zero_att
                                    if hucker == 1:
                                        hurt += 10
                                    if miaomiao == 3:
                                        hurt += random.randint(10,50)
                            if (f == 'D' and g == 'C') or (f == 'C' and g == 'B') or (f == 'B' and g == 'A') or (f == 'A' and g == 'D'):
                                hurtB += 27
                                if chooseb == 'B':
                                    hurtB -= Def
                                    if hucker == 1:
                                        hurtB -= 30
                                    if hurtB < 0:
                                        hurtB = 0
                                chance += 1
                                if coat == 1 and random.randint(1,10) != 5:
                                    hurtB = 0
                                else:
                                    health += 10
                            else:
                                chance += 1
                        if snake_run[1] == 1:
                            hurtB = 0
                        if snake_run[1] == 0:
                            hurtB *= 2
                            snake_run[0] = random.randint(3,5)
                        if miaomiao == 1:
                            hurtB /= 2
                        if miaomiao == 2:
                            hurtB /=5
                        hurtB = int(hurtB)
                        if hide[0] + hide[1] >= random.randint(1,100):
                            hurtB = 0
                        if S_up == 1:
                            if zero_H > 0:
                                zero_H -= hurtB
                            else:
                                health -= hurtB
                        else:
                            health -= hurtB
                        item_att = 0
                        if random.randint(1,20) == 3 and '战争宝石' in item and att_choose == 1:
                            hurt *= 3
                        choose = input(f'精英电子蛇B的攻击是{enemy_fight}')
                        if cube_act <= 27 :
                            choose = input('精英电子蛇B使用了防御!')
                        if chooseb != 'B':
                            choose = input(f'你对精英电子蛇B造成了{hurt}点伤害!')
                            car_B -= hurt
                            hurt = 0
                        if chooseb == 'B':
                            choose = input('因为你选择了防御,所以伤害不计入')
                        choose = input(f'你被精英电子蛇B扣除了{hurtB}点血')
                        dead_interface()
                        hurtB = 0
                        att_choose = 0
                        if respawned == 1:
                            break
                        if random.randint(1,10) <= 1:
                            choose = input('电子蛇身上的方块脱落了！')
                            snake_block = 1
                if S_up == 1:
                    if zero_H < 0:
                        zero_H = 0
                hide[1] = 0
                coat = 0
                miaomiao = 0
                if car_A <= 0 and car_B <= 0:
                    choose = input('您获胜了!')
                    CM_get = random.randint(477,1077)
                    CM += CM_get
                    choose = input(f'你获得了{CM_get}个CM币')
                    E_cotton += 1
                    win = 1

            if respawned == 1:
                respawned = 0
                continue
        output('你们向前跑去，很快来到了走廊的尽头。这里是一个摆放着许多大箱子与书架的密室。')
        output('“这里一定会有出口的，不然阿尔法的佣兵们怎么才能在比特塔里穿行呢？”So说。')
        output('你们分头在房间里寻找机关，但找了半天仍然一无所获。')
        go = 0
        while go == 0:
            output('你会：A：看看书架,B：看看大箱子,C：回到走廊')
            while choose not in {'A','B','C'}:
                output('你会：A：看看书架,B：看看大箱子,C：回到走廊')
            if choose == 'A':
                output('你看了看书架，上面有一份写着档案的文件，你随便翻了翻，上面全是各种奇怪的网址。')
            elif choose == 'B':
                output('你看了看大箱子，里面有一把重到你拿不起来的铁锤。')
            elif choose == 'C':
                go = 1
        output('你回到了前面的走廊，你看了看旁边的显示屏，突然，其中一个显示屏向墙里凹陷下去，随后向外发出一条光道。')
        output('你顺着光道来到走廊尽头的房间。昵称和So也注意到了光道，你们一起凑向光道的尽头——房间墙壁上的一个不起眼的地方。光道触碰到墙壁的位置出现了一个显示屏，上面写着：“对此显示屏造成超过4000点伤害，即可开启秘密通道。”')
        output('“4000点伤害？那我们要被困在这里一辈子了……”昵称说。')
        output('“快过来！我找到一个好东西。”So说，你们转过头去，看见So正骑在一个箱子上：“这个箱子里有一座大炮！我正在想办法驱动这个大炮，小心——”')
        output('轰的一声，箱子被炸出一个大口，你发现一个铁锤形状的大炮从箱子里露出来。')
        output('“过来驾驶这个大炮射向那边的墙壁，就可以造成足够的伤害了，不过……这个大炮很不稳，要驾驶好了！”')
        boom = 5000
        while boom > 0:
            choose = list(input(f'回复字母瞄准，2/5瞄准成功,墙的血量是{boom}'))
            x = random.randint(1,4)
            a = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            b = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            c = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            d = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            e = chr(ord('A') + x - 1)
            enemy_fight = a+b+c+d+e
            enemy_fighta = [a,b,c,d,e]
            hurt = 0
            hurtB = 0
            chance = 0
            wrong = 0
            while wrong == 0:
                wrong = 1
                if len(choose) != 5:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                elif choose[0] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                elif choose[1] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                elif choose[2] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                elif choose[3] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                elif choose[4] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
            else:
                while chance < 5:
                #快悄悄这个地方,我把chance < 5写成了chance <= 5然后查了一天才查到这个bug
                #快看,这里我复制的前面
                    #??????
                    f = choose.pop()
                    g = enemy_fighta.pop()
                    if g == 'D' and f == 'C' or g == 'C' and f == 'B' or g == 'B' and f == 'A' or g == 'A' and f == 'D':
                        hurt += 1
                        chance += 1
                    else:
                        chance += 1
                if hurt >= 2:
                    hurtB = 1000
                choose = input(f'墙的构造是{enemy_fight}')
                choose = input(f'你对墙造成了了{hurtB}点伤害')
                boom -= hurtB
        output('你通过了墙！')
        output('大炮击中的墙壁顿时碎裂，你们从裂口钻了进去。')
        output('一个看上去很像澡堂的地方出现在你们面前，不过这里只有悬挂在空中的莲蓬头，没有隔板门和衣架，换句话说，除了莲蓬头与地上的排水口，这里空无一物。')
        output('你们有些害怕。')
        output('你会：A：开莲蓬头,B：离开这里')
        while choose not in {'A','B'}:
            output('你会：A：开莲蓬头,B：离开这里')
        if choose == 'A':
            output('你的面前出现了一个弹窗，你在弹窗上一阵操作打开了莲蓬头，莲蓬头便开始洒水，你试图用手碰了碰，确定了这只是水而不是其它的东西。')
            output('“处刑台……”So说，“估计可以让机器人短路，不过这种级别的机器人真的会怕水吗？”')
        output('你们跑出之前的“澡堂”，来到一个很像书房的地方，一个工作台和许多书架出现在你面前。')
        output('“这里怎么这么奇怪？明明是实验室为什么要搞得这么复杂……”So说，“我想，即使是训练佣兵，也不需要布置这么多密室……”')
        go = 0
        while go == 0:
            output('你会：A：看看书架,B：看看工作台,C：爬上工作台')
            while choose not in {'A','B','C'}:
                output('你会：A：看看书架,B：看看工作台,C：爬上工作台')
            if choose == 'A':
                output('你看了看书架，上面有一些讲述关于机器人机体构造工程的著作，由于内容十分高深，你不想看下去。')
                choose = 'idiot'
            elif choose == 'B':
                if '水枪' not in item:
                    output('工作台上只有一只笔和一把……水枪？')
                    choose = input('你拿走了水枪（获得【水枪】）')
                    item.append('水枪')
                    view_status()
                else:
                    choose = input('工作台上只有一支笔')
                choose = 'C'
            if choose == 'C':
                output('你突然一时兴起翻上了工作台，你突然发现有个软梯高高地挂在天上。')
                output('“这是？？？”昵称问。')
                output('你跳起来抓住软梯，软梯顿时向下落去，一块天花板也跟着掉落下来，不过它们下落了一阵子便悬在了半空中。')
                output('你们顺着软梯向上爬去。登上了那块掉下来的天花板上了楼。')
                go = 1
        output('楼上是一个很普通的房间，你们从房间里唯一一个门走了出去，来到了一座桥上。')
        output('你们从桥上看下去俯视着比特塔的内部结构，你发现比特塔内部只有一个个方块状的房间，依靠着长长短短的棍状走廊连接起来，漂浮在塔内的空间中。')
        output('“这样的设计，空间浪费也太大了。”So说道。')
        output('“空间浪费大？那只不过是你们的自以为是罢了！”一个声音突然传来，你看见阿尔法乘着一个缓缓上升的平台飞了上来，你发现这平台与赛恩思的平台基本上完全一样。')
        output('“这些看似虚无的空间，便是我们的实验基地！我们最好的练兵场！这些平台可以给予他们最残酷的试验条件，使他们的野性得到充——分的磨练！只有这样，我们才能告别“软弱的机器人时代”，实现我们，伟大的，统治计划！”')
        output('阿尔法说完，下面又一个平台升起，你看见了一群佣兵乘着平台升了上来。')
        output('“如果你们不相信，我就让你们尝尝被我的绝赞佣兵攻打的机会咯！战斗阵型！”阿尔法说完向远处飞去。')
        savepoint = 21
    if savepoint == 21:
        save_data()
        output('佣兵接近你们后，纷纷跳上桥把你们包围了起来。')
        output('【战斗开始】对战：重型装甲车 x 地狱六芒星 x 精英电子蛇')
        zero_H = ''
        item_att = 0
        zero_W = ''
        if S_up == 1:
            zero_H = 0
            zero_H = int(zero_H)
            zero_W = '护盾血量'
        hucker = 0
        big_fight = 0
        t.sleep(0.5)
        car,fly,car_B = 520,300,477
        H = 250
        H_icecream = 0
        fly_B = 3
        check = 0
        magic_use = 0
        magic_point = 0
        miaomiao = 0
        snake_run = random.randint(3,5)
        snake_block = 0
        boom_snake = 0
        H_fix = 10
        coat = 0
        win = 0
        a,b,c,d,e = '','','','',''
        while win == 0:
            zero_att = 0
            magic_choose = 0
            att_choose = 0
            item_choose = 0
            while magic_choose == 0 and item_choose == 0:
                if boom_snake > 0:
                    boom_snake -= 1
                    car -= 20
                    car_B -= 20
                    if H > 0:
                        H -= 20
                        if H < 0:
                            H = 0
                    else:
                        fly -= 20
                    input('两只小电子蛇对敌人造成了20点伤害！')
                if car <= 0:
                    car = 0
                if fly < 0:
                    fly = 0
                if car_B <= 0:
                    car_B = 0
                chooseb = 'A'
                if '战争宝石' in item:
                    print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health}{zero_W}{zero_H},重型装甲车血量为{car},攻击力为30，防御力35，防御率40%,地狱六芒星血量为{fly},护盾血量{H},攻击力为30，防御力30，防御率15%，精英电子蛇血量为{car_B},攻击力为27，防御力27，防御率27%，你的暴击数{big_fight}')
                if '战争宝石' not in item:
                    print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health},重型装甲车血量为{car},地狱六芒星血量为{fly},护盾血量{H},精英电子蛇血量为{car_B}')
                if snake_block == 0:
                    choose = input('A,物品B,防御C,魔法D,跳过')
                    while choose not in {'A','B','C','D'}:
                        print('请做出你的选择')
                        choose = input('A,物品B,防御C,魔法D,跳过')
                    if choose == 'A':
                        choose = input(f'你现在可使用的物品有{fight_item},请从1开始输入序号以选择使用的物品')
                        if choose not in {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'}:
                            choose = input('物品序号输入错误!')
                        else:
                            check = fight_item[choose]
                            item_find()
                            if check == '魔法炸药':
                                choose = input('你对对方造成了100点伤害!但你也不小心受到了30点伤害')
                                health -= 30
                                car -= 100
                                if H > 0:
                                    H -= 100
                                elif H <= 0:
                                    fly -= 100
                                car_B -= 100
                                dead_interface()
                                if respawned == 1:
                                    break
                            if check == '坚硬冰棍':
                                choose = input('请选择投掷的对象（填A或B或C）')
                                while choose not in {'A','B','C'}:
                                    choose = input('请选择投掷的对象（填A或B或C）')
                                if choose == 'A':
                                    input('你使用了坚硬冰棍!重型装甲车的HP降低了100点!')
                                    car -= 100
                                elif choose == 'B':
                                    if H <= 0:
                                        input('你使用了坚硬冰棍!地狱六芒星的HP降低了100点!')
                                        fly -= 100
                                    elif H > 0:
                                        input('你使用了坚硬冰棍!地狱六芒星的护盾耐久度降低了100点!')
                                        H -= 100
                                elif choose == 'C':
                                    car_B -= 100
                                    input('你使用了坚硬冰棍!精英电子蛇的HP降低了100点!')
                            if check == '像素板':
                                choose = input('你使用了像素板！重型装甲车,地狱六芒星和精英电子蛇受到了70点伤害！')
                                car -= 70
                                fly -= 70
                                car_B -= 70
                            if H < 0:
                                H = 0
                            item.remove(check)
                            fight_item.remove(check)
                            item_choose = 1
                            if health > 300:
                                health = 300
                    elif choose == 'B':
                        choose = input('你选择了防御!')
                        magic_point += 40
                        magic_choose = 1
                        if magic_point >= 100:
                            magic_point = 100
                        chooseb = 'B'
                    elif choose == 'C':
                        bit_magic('normal')
                    elif choose == 'D':
                        choose = input('你跳过了你的回合')
                        magic_choose = 1
                else:
                    choose = input('A：丢弃方块')
                    while choose != 'A':
                        choose = input('A：丢弃方块')
                    chooseb = 'B'
                    magic_choose = 1
            snake_block = 0
            if '混乱护盾' in armor:
                health += random.randint(3,20)
                if health >= 300:
                    health = 300
            if H_icecream > 0:
                H_icecream -= 1
                health -= 20
            if car > 0:
                car_F = random.randint(1,5)
                car_P = random.randint(1,5)
                car_P_B = 0
                car_act_B = random.randint(1,4)
                if car_act_B == 1:
                    input('装甲车发射着紫红色的恐怖激光')
                if car_act_B == 2:
                    input('装甲车试图与周围的电路产生共鸣，等等机械振动与电磁振动会产生共振吗？')
                if car_act_B == 3:
                    input('装甲车向你碾来！')
                if car_act_B == 4:
                    input('装甲车四处张望着')
                x = random.randint(1,4)
                a = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                b = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                c = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                d = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                e = chr(ord('A') + x - 1)
                enemy_fight = a+b+c+d+e
                enemy_fighta = [a,b,c,d,e]
                zero_att = 0
                if '零剑' in weapon:
                    zero_att = random.randint(5,50)
                if '零剑-II' in weapon:
                    zero_att = random.randint(30,70)
                if 'Complex机甲长剑' in weapon and random.randint(1,10) == 3:
                    zero_att = 10
                choose = list(input(f'请选择你对重型装甲车的攻击!(5个一组,由五个大写字母构成)'))
                hurt = 0
                hurtB = 0
                chance = 0
                wrong = 0
                while wrong == 0:
                    wrong = 1
                    if len(choose) != 5:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[0] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[1] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[2] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[3] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[4] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                else:
                    cube_act = random.randint(1,4)
                    while chance < 5:
                        f = choose.pop()
                        g = enemy_fighta.pop()
                        if chooseb != 'B':
                            if (f == 'A' and g == 'B') or (f == 'B' and g == 'C') or (f == 'C' and g == 'D') or (f == 'D' and g == 'A'):
                                hurt += att
                                chance += 1
                                if att_choose == 1:
                                    hurt += 5
                                if cube_act == 1:
                                    hurt -= 35
                                    laser(35)
                                else:
                                    laser(0)
                                if '虚空之刃' in weapon and random.randint(1,5) == 2:
                                    hurt += int(car/5)
                                hurt += item_att
                                hurt += zero_att
                                if hucker == 1:
                                    hurt += 10
                        if (f == 'D' and g == 'C') or (f == 'C' and g == 'B') or (f == 'B' and g == 'A') or (f == 'A' and g == 'D'):
                            if car_P == 3:
                                car_P_B += 1
                            if car_F != 1:
                                hurtB += 30
                            if chooseb == 'B':
                                hurtB -= (Def+blood_stone)
                                if hucker == 1:
                                    hurtB -= 30
                                if hurtB < 0:
                                    hurtB = 0
                            chance += 1
                        else:
                            chance += 1
                    if coat == 1:
                        if random.randint(1,10) == 5:
                            hurtB = 0
                        else:
                            health += 10
                    if miaomiao == 1:
                        hurtB /= 2
                        hurt_B = int(hurtB)
                    if random.randint(1,20) == 3 and '战争宝石' in item and att_choose == 1:
                        hurt *= 3
                        big_fight += 1
                    if hide[0] + hide[1] >= random.randint(1,100):
                        hurtB = 0
                    if hurt > 50 and car_F == 1:
                        hurt = 50
                    if miaomiao == 1:
                        hurtB /= 2
                    if miaomiao == 2:
                        hurtB /= 5
                    if S_up == 1:
                        if zero_H > 0:
                            zero_H -= hurtB
                        else:
                            health -= hurtB
                    else:
                        health -= hurtB
                    item_att = 0
                    choose = input(f'重型装甲车的攻击是{enemy_fight}')
                    if cube_act == 1:
                        choose = input('重型装甲车使用了防御!')
                    if chooseb != 'B':
                        choose = input(f'你对重型装甲车造成了{hurt}点伤害!')
                        car -= hurt
                        hurt = 0
                    if chooseb == 'B':
                        choose = input('因为你选择了防御,所以伤害不计入')
                    if car_P == 3:
                        health -= 30 * car_P_B
                        input(f'重型装甲车向你射出了一枚炮弹！对你造成了{30*car_P_B}点伤害')
                    choose = input(f'你被重型装甲车扣除了{hurtB+(30*car_P_B)}点血')
                    car_P_B = 0
                    dead_interface()
                    if respawned == 1:
                        break
            if fly > 0:
                car_act_B = random.randint(1,6)
                if car_act_B == 1:
                    input('六芒星展示着自己的突刺')
                if car_act_B == 2:
                    input('六芒星向你们俯冲过来')
                if car_act_B == 3:
                    input('六芒星对你们发动了猛烈的炮轰！')
                if car_act_B == 4:
                    input('六芒星正在准备一发地毯式轰炸！')
                if car_act_B == 5:
                    input('你们没有找到对手的破绽')
                if car_act_B == 6 and H > 0:
                    input('六芒星对自己的电磁防护罩非常满意')
                if car_act_B == 6 and H <= 0:
                    input('六芒星感到焦虑不安')
                x = random.randint(1,4)
                a = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                b = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                c = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                d = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                e = chr(ord('A') + x - 1)
                enemy_fight = a+b+c+d+e
                enemy_fighta = [a,b,c,d,e]
                zero_att = 0
                if '零剑' in weapon:
                    zero_att = random.randint(5,50)
                if '零剑-II' in weapon:
                    zero_att = random.randint(30,70)
                if 'Complex机甲长剑' in weapon and random.randint(1,10) == 3:
                    zero_att = 10
                if fly_B != 0:
                    fly_B -= 1
                    choose = list(input(f'请选择你对地狱六芒星的攻击!(5个一组,由五个大写字母构成)'))
                    hurt = 0
                    hurtB = 0
                    chance = 0
                    wrong = 0
                    while wrong == 0:
                        wrong = 1
                        if len(choose) != 5:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[0] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[1] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[2] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[3] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[4] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    else:
                        cube_act = random.randint(1,20)
                        while chance < 5:
                            f = choose.pop()
                            g = enemy_fighta.pop()
                            if chooseb != 'B':
                                if (f == 'A' and g == 'B') or (f == 'B' and g == 'C') or (f == 'C' and g == 'D') or (f == 'D' and g == 'A'):
                                    hurt += att
                                    chance += 1
                                    if att_choose == 1:
                                        hurt += 5
                                    if cube_act <= 3:
                                        hurt -= 30
                                        laser(30)
                                    else:
                                        laser(0)
                                    if '虚空之刃' in weapon and random.randint(1,5) == 2:
                                        hurt += int(fly/5)
                                    hurt += item_att
                                    hurt += zero_att
                                    if hucker == 1:
                                        hurt += 10
                                    
                            if (f == 'D' and g == 'C') or (f == 'C' and g == 'B') or (f == 'B' and g == 'A') or (f == 'A' and g == 'D'):
                                hurtB += 30
                                if chooseb == 'B':
                                    hurtB -= (Def+blood_stone)
                                    if hucker == 1:
                                        hurtB -= 30
                                    if hurtB < 0:
                                        hurtB = 0
                                chance += 1
                                if coat == 1 and random.randint(1,10) != 5:
                                    hurtB = 0
                                else:
                                    health += 10
                            else:
                                chance += 1
                        if hide[0] + hide[1] >= random.randint(1,100):
                            hurtB = 0
                        if miaomiao == 1:
                            hurtB /= 2
                        if miaomiao == 2:
                            hurtB /= 5
                        if S_up == 1:
                            if zero_H > 0:
                                zero_H -= hurtB
                            else:
                                health -= hurtB
                        else:
                            health -= hurtB
                    item_att = 0
                    if random.randint(1,20) == 3 and '战争宝石' in item and att_choose == 1:
                        hurt *= 3
                        big_fight += 1
                    choose = input(f'地狱六芒星的攻击是{enemy_fight}')
                    if cube_act <= 3:
                        choose = input('地狱六芒星使用了防御!')
                    if chooseb != 'B':
                        choose = input(f'你对地狱六芒星造成了{hurt}点伤害!')
                        if H > 0:
                            H -= hurt
                        elif H <= 0:
                            fly -= hurt
                        if H < 0:
                            H = 0
                        hurt = 0
                    if chooseb == 'B':
                        choose = input('因为你选择了防御,所以伤害不计入')
                    choose = input(f'你被地狱六芒星扣除了{hurtB}点血')
                    H_fix -= 1
                    if H_fix == 0:
                        H += 250
                        input('六芒星继续制造了一个护盾！')
                        H_fix = 10
                if fly_B == 0:
                    fly_B = 3
                    input('六芒星开启了地狱眼模式！！！一波狂轰滥炸即将开始！')
                    boom = 6
                    while boom > 0:
                        boom -= 1
                        choose = input('请输入两个大写字母，共输入六次！')
                        x = random.randint(1,4)
                        a = chr(ord('A') + x - 1)
                        x = random.randint(1,4)
                        b = chr(ord('A') + x - 1)
                        enemy_fight = a+b
                        enemy_fighta = [a,b]
                        hurt = 0
                        hurtB = 0
                        chance = 0
                        wrong = 0
                        while wrong == 0:
                            wrong = 1
                            if len(choose) != 2:
                                wrong = 0
                                print('输入错误,请依照格式输入!')
                                choose = list(input(f'请选择你的攻击!'))
                            elif choose[0] not in {'A','B','C','D'}:
                                wrong = 0
                                print('输入错误,请依照格式输入!')
                                choose = list(input(f'请选择你的攻击!'))
                            elif choose[1] not in {'A','B','C','D'}:
                                wrong = 0
                                print('输入错误,请依照格式输入!')
                                choose = list(input(f'请选择你的攻击!'))
                        cube_act = random.randint(1,20)
                        while chance < 2:
                            f = choose.pop()
                            g = enemy_fighta.pop()
                            if (f == 'A' and g == 'B') or (f == 'B' and g == 'C') or (f == 'C' and g == 'D') or (f == 'D' and g == 'A'):
                                hurt += att
                                chance += 1
                                if att_choose == 1:
                                    hurt += 5
                                if cube_act <= 3:
                                    hurt -= 30
                                    laser(30)
                                else:
                                    laser(0)
                                if '虚空之刃' in weapon and random.randint(1,5) == 2:
                                    hurt += int(car_A/5)
                                hurt += item_att
                                hurt += zero_att
                                if hucker == 1:
                                    hurt += 10
                                
                            elif (f == 'D' and g == 'C') or (f == 'C' and g == 'B') or (f == 'B' and g == 'A') or (f == 'A' and g == 'D'):
                                hurtB += 30
                                chance += 1
                                if coat == 1 and random.randint(1,10) != 5:
                                    hurtB = 0
                                if miaomiao == 1:
                                    hurtB /= 2
                                    hurt_B = int(hurtB)
                                else:
                                    health += 10
                            else:
                                chance += 1
                        if hide[0] + hide[1] >= random.randint(1,100):
                            hurtB = 0
                        if miaomiao == 1:
                            hurtB /= 2
                        if miaomiao == 2:
                            hurtB /= 5
                        if S_up == 1:
                            if zero_H > 0:
                                zero_H -= hurtB
                            else:
                                health -= hurtB
                        choose = input(f'地狱六芒星的攻击是{enemy_fight}')
                        if chooseb != 'B':
                            choose = input(f'你对地狱六芒星造成了{hurt}点伤害!')
                            if H > 0:
                                H -= hurt
                            elif H <= 0:
                                fly -= hurt
                            if H < 0:
                                H = 0
                            hurt = 0
                        choose = input(f'你被地狱六芒星扣除了{hurtB}点血')
                        H_fix -= 1
                    if H_fix == 0:
                        H += 250
                        input('六芒星继续制造了一个护盾！')
                        H_fix = 10
                dead_interface()
                hurtB = 0
                att_choose = 0
                if respawned == 1:
                    break
            if car_B > 0:
                car_act_B = random.randint(1,7)
                if car_act_B == 1:
                    input('电子蛇绕成一圈，你们不知道在玩什么花样')
                if car_act_B == 2:
                    input('电子蛇发出来特有的嘶嘶声')
                if car_act_B == 3:
                    input('你们闻到一股棉花味')
                if car_act_B == 4:
                    input('电子蛇对你们目露凶光')
                if car_act_B == 5:
                    input('电子蛇不希望看到捕蛇圈')
                if car_act_B == 6:
                    input('电子蛇希望你们能养它们')
                if car_act_B == 7:
                    input('电子蛇有点想逃走')
                snake_run -= 1
                if snake_run == 1:
                    input('电子蛇开始卷缩着身体')
                if snake_run == 0:
                          input('电子蛇向你冲来！')
                x = random.randint(1,4)
                a = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                b = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                c = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                d = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                e = chr(ord('A') + x - 1)
                if miaomiao == 4:
                    b,c,d,e = a
                enemy_fight = a+b+c+d+e
                enemy_fighta = [a,b,c,d,e]
                zero_att = 0
                if '零剑' in weapon:
                    zero_att = random.randint(5,50)
                if '零剑-II' in weapon:
                    zero_att = random.randint(30,70)
                if 'Complex机甲长剑' in weapon and random.randint(1,10) == 3:
                    zero_att = 10
                choose = list(input(f'请选择你对精英电子蛇的攻击!(5个一组,由五个大写字母构成)'))
                hurt = 0
                hurtB = 0
                chance = 0
                wrong = 0
                while wrong == 0:
                    wrong = 1
                    if len(choose) != 5:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[0] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[1] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[2] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[3] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[4] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                else:
                    cube_act = random.randint(1,100)
                    while chance < 5:
                        f = choose.pop()
                        g = enemy_fighta.pop()
                        if chooseb != 'B':
                            if (f == 'A' and g == 'B') or (f == 'B' and g == 'C') or (f == 'C' and g == 'D') or (f == 'D' and g == 'A'):
                                hurt += att
                                chance += 1
                                if att_choose == 1:
                                    hurt += 5
                                    if '战争宝石' in item:
                                        hurt += 5
                                if cube_act <= 27:
                                    hurt -= 27
                                    laser(27)
                                else:
                                    laser(0)
                                hurt += item_att
                                hurt += zero_att
                                if hucker == 1:
                                    hurt += 10
                                if miaomiao == 3:
                                    hurt += random.randint(10,50)
                                
                        if (f == 'D' and g == 'C') or (f == 'C' and g == 'B') or (f == 'B' and g == 'A') or (f == 'A' and g == 'D'):
                            hurtB += 27
                            if chooseb == 'B':
                                hurtB -= Def
                                if hucker == 1:
                                    hurtB -= 30
                                if hurtB < 0:
                                    hurtB = 0
                            chance += 1
                        else:
                            chance += 1
                    if snake_run == 1:
                        hurtB = 0
                    if snake_run == 0:
                        hurtB *= 2
                        snake_run = random.randint(3,5)
                    if coat == 1:
                        if random.randint(1,10) == 5:
                            hurtB = 0
                        else:
                            health += 10
                    if miaomiao == 1:
                        hurtB /= 2
                    if miaomiao == 2:
                        hurtB /=5
                    hurtB = int(hurtB)
                    if hide[0] + hide[1] >= random.randint(1,100):
                        hurtB = 0
                    if S_up == 1:
                        if zero_H > 0:
                            zero_H -= hurtB
                        else:
                            health -= hurtB
                    item_att = 0
                    if random.randint(1,20) == 3 and '战争宝石' in item and att_choose == 1:
                        hurt *= 3
                    choose = input(f'精英电子蛇的攻击是{enemy_fight}')
                    if cube_act <= 27 :
                        choose = input('精英电子蛇使用了防御!')
                    if chooseb != 'B':
                        choose = input(f'你对精英电子蛇造成了{hurt}点伤害!')
                        car_B -= hurt
                        hurt = 0
                    if chooseb == 'B':
                        choose = input('因为你选择了防御,所以伤害不计入')
                    choose = input(f'你被精英电子蛇扣除了{hurtB}点血')
                    dead_interface()
                    hurtB = 0
                    att_choose = 0
                    if respawned == 1:
                        break
                    if random.randint(1,10) <= 1:
                        choose = input('电子蛇身上的方块脱落了！')
                        snake_block = 1
            hide[1] = 0
            coat = 0
            miaomiao = 0
            if magic_use != 0:
                magic_point += magic_use
                blood_block -= 1
            if car <= 0 and fly <= 0 and car_B <= 0:
                choose = input('您获胜了!')
                CM_get = random.randint(730,1750)
                CM += CM_get
                choose = input(f'你获得了{CM_get}个CM币')
                E_cotton += 1
                win = 1

        if respawned == 1:
            respawned = 0
            continue
        output('你们击败了佣兵，它们乘着平台逃走了。')
        savepoint = 22
    #做个存档点标记
    if savepoint == 22:
        save_data()
        output('你们向桥的前方走去，一座电梯树立在桥的尽头。')
        output('“又有电梯，太好了。”昵称说完，你们进入了电梯，一股绿色的光笼罩着电梯，你得到了治愈[HPmax]”')
        health = 300
        output('你们来到了第72楼')
        output('这一楼的电梯门外是一个像电影院的地方，一条长廊旁边接着许多小门，不过这些门都是关着的。')
        output('你们向前走去，来到一个三岔路口。')
        output('“诶等等，我想想……左边好像又是一个谜题，右边是怪。”昵称说。')
        output('“呃……你怎么知道的……”So问。')
        output('“啊？！之前不是有一个地图吗？我存到芯片里了……喵。”')
        output('“嗯……”So说，“这里的敌人太强了，我不想再和他们打了，我们走左边吧。”')
        output('你会：A：走左边,B：走右边')
        while choose not in {'A','B'}:
            output('你会：A：走左边,B：走右边')
        if choose == 'A':
            output('你们来到一个红色的房间，这里有一只非常大的鼓。')
            output('“这个谜题很显然，我们需要打鼓，打出相应的节奏就能通关了，多简单无脑的谜题设计。”So无奈地说。')
            output('“没有提示吗？”昵称说道。')
            output('你会：A：找提示,B：砸鼓')
            while choose not in {'A','B'}:
                output('你会：A：找提示,B：砸鼓')
            if choose == 'A':
                output('你向四周看了看，并没有任何有用的提示。')
                output('“看来……我觉得……这可能需要我敲一首miamia的节奏来着……我试试”昵称说，然后在鼓上奋力地敲起来')
            elif choose == 'B':
                output('你向鼓发起挑战！')
                print('【战斗开始】对战 鼓')
                t.sleep(0.3)
                print('【你 傻 了】')
                print('回复4个字母和鼓对战，2/4通过')
                go = 0
                while go == 0:
                    count = 0
                    choose = list(input('请输入你的击打方式'))
                    x = random.randint(1,4)
                    a = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    b = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    c = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    d = chr(ord('A') + x - 1)
                    enemy_fight = a+b+c+d
                    enemy_fighta = [a,b,c,d]
                    hurt = 0
                    hurtB = 0
                    chance = 0
                    wrong = 0
                    while wrong == 0:
                        wrong = 1
                        if len(choose) != 4:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的击打方式!(4个一组,由4个大写字母构成)'))
                        elif choose[0] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的击打方式!(4个一组,由4个大写字母构成)'))
                        elif choose[1] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的击打方式!(4个一组,由4个大写字母构成)'))
                        elif choose[2] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的击打方式!(4个一组,由4个大写字母构成)'))
                        elif choose[3] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的击打方式!(4个一组,由4个大写字母构成)'))
                    else:
                        while chance < 4:
                        #快悄悄这个地方,我把chance < 5写成了chance <= 5然后查了一天才查到这个bug
                        #悄悄改为瞧瞧,这是个错别字(划)通假字
                        #快看,这里我复制的前面
                            #快看，我还是复制的前面（
                            f = choose.pop()
                            g = enemy_fighta.pop()
                            if f == 'D' and g == 'C' or f == 'C' and g == 'B' or f == 'B' and g == 'A' or f == 'A' and g == 'D':
                                chance += 1
                            else:
                                chance += 1
                                count += 1
                        choose = input(f'铺面的形式是{enemy_fight}')
                        if count >= 2:
                            input('你通过了铺面！')
                            go = 1
                            if count == 2:
                                print('评级：A')
                            if count == 3:
                                print('评级：EX(?)')
                            if count == 4:
                                print('评级：Million master(?)')
                        else:
                            health -= hurtB
                            choose = input(f'Track Lost!(?)')
                output('鼓上面突然出现了许多显示屏，显示屏飞到了对面的墙上把墙打开了！')
                output('“成功了！我们走！”So说。')
        elif choose == 'B':
            output('你们前面出现三个升降门！')
            output('“这……就这？”So问')
            go = 0
            while go == 0:
                count = 0
                choose = list(input('请输入你的通过方式（回复3个字母通过升降门，1/3通过）'))
                x = random.randint(1,4)
                a = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                b = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                c = chr(ord('A') + x - 1)
                enemy_fight = a+b+c
                enemy_fighta = [a,b,c]
                hurt = 0
                hurtB = 0
                chance = 0
                wrong = 0
                while wrong == 0:
                    wrong = 1
                    if len(choose) != 3:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的通过方式!(3个一组,由3个大写字母构成)'))
                    elif choose[0] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的通过方式!(3个一组,由3个大写字母构成)'))
                    elif choose[1] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的通过方式!(3个一组,由3个大写字母构成)'))
                    elif choose[2] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的通过方式!(3个一组,由3个大写字母构成)'))
                else:
                    while chance < 3:
                    #快悄悄这个地方,我把chance < 5写成了chance <= 5然后查了一天才查到这个bug
                    #悄悄改为瞧瞧,这是个错别字(划)通假字
                    #快看,这里我复制的前面
                        #快看，我还是复制的前面（
                        f = choose.pop()
                        g = enemy_fighta.pop()
                        if f == 'D' and g == 'C' or f == 'C' and g == 'B' or f == 'B' and g == 'A' or f == 'A' and g == 'D':
                            hurtB += 20
                            chance += 1
                        else:
                            chance += 1
                            count += 1
                    choose = input(f'升降门的升降方式是{enemy_fight}')
                    if count >= 1:
                        input('你通过了升降门！')
                        go = 1
                    else:
                        health -= hurtB
                        choose = input(f'你没能通过升降门！你被扣除了{hurtB}点血量')
                    dead_interface()
                    if respawned == 1:
                        respawned = 0
                        continue
            output('你们通过了升降门')
        output('你们继续向前走去，来到一个像地下通道一样的长廊，旁边的墙上画满了一些电视节目主持人，可惜你一个也不认识。')
        output('穿过走廊后，前面又出现了一座电梯。电梯的旁边有一个看上去像激光发射器的东西。')
        output('“是电梯！我们进去吧！”')
        output('你会：A：进入电梯,B：看看激光发射器')
        while choose not in {'A','B'}:
            output('你会：A：进入电梯,B：看看激光发射器')
        if choose == 'B':
            output('你看了看激光发射器，并没有什么特别的。')
        output('你们进入电梯')
        output('迎面而来的并不是电梯厢体，而是两个发着蓝光的飞碟。')
        output('“赛恩思让我们抓三个人，不是你们还能是谁？别跑！”')
        output('“等一下！”So大喊，“我们不能谈判吗？”')
        output('“谈判？”飞碟思考了一下“你指什么？”')
        output('“要是你们没有完成赛恩思的任务，你们肯定会受到惩罚的吧，但如果你们能够做我们的帮手，我们就可以一起击败赛恩思，你也知道我们是有这个能力的……”So急匆匆地说。')
        output('“如果你们击败了赛恩思，我们……我们去哪呢？”飞碟问。')
        output('“去外面啊！魔法界域大得很呢！”')
        output('“可是，离开了赛恩思，我们……我们能做些什么呢……”飞碟说。')
        output('“想做什么就做什么呗！”')
        output('“想做什么就做什么？？？这是什么意思？？？我……我们可以想做什么就做什么？？？这？？？什么？？？不可能？？？”飞碟似乎被你们问晕了，在电梯门前四处乱飞，但仍然挡在门口。')
        output('突然，飞碟一下子在门口定住了：“错误，错误，启动战争模式。”')
        output('你看见飞碟的光变成了红色。')
        output('“好家伙，这回逃不过了。”So说。')
        print('【战斗开始】对战 飞碟骑兵*2')
        hucker = 0
        DSC = random.randint(4,5)
        zero_H = ''
        zero_W = ''
        if S_up == 1:
            zero_H = 0
            zero_H = int(zero_H)
            zero_W = '护盾血量'
        boom_snake = 0
        big_fight = 0
        H_icecream = 0
        t.sleep(0.5)
        car_A,car_B = 404,404
        check = 0
        magic_point = 0
        miaomiao = 0
        coat = 0
        win = 0
        item_att = 0
        DS = random.randint(3,5)
        DSB = 0
        a,b,c,d,e = '','','','',''
        while win == 0:
            if boom_snake > 0:
                boom_snake -= 1
                car_A -= 20
                car_B -= 20
                input('两只小电子蛇对敌人造成了20点伤害！')
            zero_att = 0
            magic_choose = 0
            att_choose = 0
            item_choose = 0
            while magic_choose == 0 and item_choose == 0:
                if car_A <= 0:
                    car_A = 0
                if car_B <= 0:
                    car_B = 0
                chooseb = 'A'
                if DSB <= 60:
                    DSB = 0
                    if '战争宝石' in item:
                        print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health},飞碟骑兵A血量为{car_A},攻击力为27，飞碟骑兵B血量为{car_B},攻击为27，暴击数{big_fight}，飞碟骑兵防御力10，防御率20%')
                    if '战争宝石' not in item:
                        print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health},飞碟骑兵A血量为{car_A},飞碟骑兵B血量为{car_B}')
                    choose = input('A,物品B,防御C,魔法D,跳过')
                    while choose not in {'A','B','C','D'}:
                        print('请做出你的选择')
                        choose = input('A,物品B,防御C,魔法D,跳过')
                    if choose == 'A':
                        choose = input(f'你现在可使用的物品有{fight_item},请从1开始输入序号以选择使用的物品')
                        if choose not in {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'}:
                            choose = input('物品序号输入错误!')
                        else:
                            choose = int(choose)
                            if choose > len(fight_item):
                                choose = input('物品序号输入错误!')
                            else:
                                check = fight_item[choose]
                                item_find()
                                if check == '魔法炸药':
                                    choose = input('你对对方造成了100点伤害!但你也不小心受到了30点伤害')
                                    health -= 30
                                    car_A -= 100
                                    car_B -= 100
                                    dead_interface()
                                    if respawned == 1:
                                        break
                                if check == '坚硬冰棍':
                                    choose = input('请选择攻击的对象！（用A或B表示）')
                                    while choose not in {'A','B'}:
                                        choose = input('请选择攻击的对象！（用A或B表示）')
                                    if choose == 'A':
                                        input('你使用了坚硬冰棍！对飞碟骑兵A造成了100点伤害！')
                                        car_A -= 100
                                    if choose == 'B':
                                        input('你使用了坚硬冰棍！对飞碟骑兵B造成了100点伤害！')
                                        car_B -= 100
                                if health > 300:
                                    health = 300
                    if choose == 'B':
                        choose = input('你选择了防御!')
                        magic_point += 40
                        magic_choose = 1
                        if magic_point >= 100:
                            magic_point = 100
                        chooseb = 'B'
                    if choose == 'C':
                        bit_magic('normal')
                        choose = 0
                    if choose == 'D':
                        choose = input('你跳过了你的回合')
                        magic_choose = 1
                elif DSB >  60:
                    magic_choose = 1
                    DSB = 0
            car_act_B = random.randint(1,10)
            if '混乱护盾' in armor:
                health += random.randint(3,20)
                if health >= 300:
                    health = 300
            if H_icecream > 0:
                H_icecream -= 1
                health -= 20
            DS -= 1
            if DS < 0:
                DS = 0
            if DS == 0:
                DSB = 1
                input('飞碟正在准备一发激光打击！')
            if car_act_B == 1:
                input('飞碟正在蓄力射击')
            if car_act_B == 2:
                input('无聊的拉锯战就此展开')
            if car_act_B == 3:
                input('飞碟希望通过红色激光扫射你')
            if car_act_B == 4:
                input('飞碟变成了飞饼')
            if car_act_B == 5:
                input('能量核心的气味')
            if car_act_B == 6:
                input('飞碟骑兵并没有坐骑')
            if car_act_B == 7:
                input('Emp干扰器的气味')
            if car_act_B == 8:
                input('TtTtT……PpPpP')
            if car_act_B == 9:
                input('你闻到了一股皇帝般的气息')
            if DSC != 0 and (car_A > 0 or car_B > 0):
                DSC -= 1
            if car_A > 0:
                x = random.randint(1,4)
                a = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                b = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                c = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                d = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                e = chr(ord('A') + x - 1)
                if miaomiao == 4:
                    b,c,d,e = a
                enemy_fight = a+b+c+d+e
                enemy_fighta = [a,b,c,d,e]
                zero_att = 0
                if '零剑' in weapon:
                    zero_att = random.randint(5,50)
                if '零剑-II' in weapon:
                    zero_att = random.randint(30,70)
                if 'Complex机甲长剑' in weapon and random.randint(1,10) == 3:
                    zero_att = 10
                choose = list(input(f'请选择你对飞碟骑兵A的攻击!(5个一组,由五个大写字母构成)'))
                hurt = 0
                hurtB = 0
                chance = 0
                wrong = 0
                while wrong == 0:
                    wrong = 1
                    if len(choose) != 5:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[0] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[1] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[2] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[3] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[4] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                else:
                    cube_act = random.randint(1,5)
                    while chance < 5:
                        f = choose.pop()
                        g = enemy_fighta.pop()
                        if chooseb != 'B':
                            if (f == 'A' and g == 'B') or (f == 'B' and g == 'C') or (f == 'C' and g == 'D') or (f == 'D' and g == 'A'):
                                hurt += att
                                chance += 1
                                if att_choose == 1:
                                    hurt += 5
                                if cube_act > 4:
                                    hurt -= 27
                                    laser(35)
                                else:
                                    laser(0)
                                if '虚空之刃' in weapon and random.randint(1,5) == 2:
                                    hurt += int(car_A/5)
                                hurt += item_att
                                hurt += zero_att
                                if miaomiao == 3:
                                    hurt += random.randint(10,50)
                                if hucker == 1:
                                    hurt += 10
                        if (f == 'D' and g == 'C') or (f == 'C' and g == 'B') or (f == 'B' and g == 'A') or (f == 'A' and g == 'D'):
                            hurtB += 27
                            if DS == 0:
                                hurtB += 23
                                DSB += 45
                            if chooseb == 'B':
                                hurtB -= (Def+blood_stone)
                                if hucker == 1:
                                    hurtB -= 30
                                if hurtB < 0:
                                    hurtB = 0
                            chance += 1
                            if coat == 1 and random.randint(1,10) == 5:
                                hurtB = 0
                            else:
                                health += 10
                        else:
                            chance += 1
                    if random.randint(1,20) == 3 and '战争宝石' in item and att_choose == 1:
                        hurt *= 3
                        big_fight += 1
                    if hide[0] + hide[1] >= random.randint(1,100):
                        hurtB = 0
                    if miaomiao == 1:
                        hurtB /= 2
                    if miaomiao == 2:
                        hurtB /= 5
                    if S_up == 1:
                        if zero_H > 0:
                            zero_H -= hurtB
                        else:
                            health -= hurtB
                    else:
                        health -= hurtB
                    item_att = 0
                    choose = input(f'飞碟骑兵A的攻击是{enemy_fight}')
                    if cube_act > 4 :
                        choose = input('飞碟骑兵A使用了防御!')
                    if chooseb != 'B':
                        choose = input(f'你对飞碟骑兵A造成了{hurt}点伤害!')
                        car_A -= hurt
                        hurt = 0
                    if chooseb == 'B':
                        choose = input('因为你选择了防御,所以伤害不计入')
                    choose = input(f'你被敌人扣除了{hurtB}点血')
                    hurtB = 0
                    dead_interface()
                    if respawned == 1:
                        break
            if car_B > 0:
                x = random.randint(1,4)
                a = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                b = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                c = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                d = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                e = chr(ord('A') + x - 1)
                if miaomiao == 4:
                    b,c,d,e = a
                enemy_fight = a+b+c+d+e
                enemy_fighta = [a,b,c,d,e]
                zero_att = 0
                if '零剑' in weapon:
                    zero_att = random.randint(5,50)
                if '零剑-II' in weapon:
                    zero_att = random.randint(30,70)
                if 'Complex机甲长剑' in weapon and random.randint(1,10) == 3:
                    zero_att = 10
                choose = list(input(f'请选择你对飞碟骑兵B的攻击!(5个一组,由五个大写字母构成)'))
                hurt = 0
                hurtB = 0
                chance = 0
                wrong = 0
                while wrong == 0:
                    wrong = 1
                    if len(choose) != 5:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[0] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[1] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[2] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[3] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[4] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                else:
                    cube_act = random.randint(1,5)
                    while chance < 5:
                        f = choose.pop()
                        g = enemy_fighta.pop()
                        if chooseb != 'B':
                            if (f == 'A' and g == 'B') or (f == 'B' and g == 'C') or (f == 'C' and g == 'D') or (f == 'D' and g == 'A'):
                                hurt += att
                                chance += 1
                                if att_choose == 1:
                                    hurt += 5
                                if cube_act > 4:
                                    hurt -= 27
                                    laser(27)
                                else:
                                    laser(0)
                                if '虚空之刃' in weapon and random.randint(1,5) == 2:
                                    hurt += int(car_B/5)
                                hurt += item_att
                                hurt += zero_att
                                if hucker == 1:
                                    hurt += 10
                                if miaomiao == 3:
                                    hurt += random.randint(10,50)
                                
                        if (f == 'D' and g == 'C') or (f == 'C' and g == 'B') or (f == 'B' and g == 'A') or (f == 'A' and g == 'D'):
                            hurtB += 24
                            if DS == 0:
                                hurtB += 23
                                DSB += 45
                            if chooseb == 'B':
                                hurtB -= (Def+blood_stone)
                                if hucker == 1:
                                    hurtB -= 30
                                if hurtB < 0:
                                    hurtB = 0
                            chance += 1
                            if coat == 1 and random.randint(1,10) != 5:
                                hurtB = 0
                            else:
                                health += 10
                        else:
                            chance += 1
                    if hide[0] + hide[1] >= random.randint(1,100):
                        hurtB = 0
                    if miaomiao == 1:
                        hurtB /= 2
                    if miaomiao == 2:
                        hurtB /= 5
                    if S_up == 1:
                        if zero_H > 0:
                            zero_H -= hurtB
                        else:
                            health -= hurtB
                    else:
                        health -= hurtB
                    item_att = 0
                    if random.randint(1,20) == 3 and '战争宝石' in item and att_choose == 1:
                        hurt *= 3
                        big_fight += 1
                    choose = input(f'飞碟骑兵B的攻击是{enemy_fight}')
                    if cube_act > 4:
                        choose = input('飞碟骑兵B使用了防御!')
                    if chooseb != 'B':
                        choose = input(f'你对飞碟骑兵B造成了{hurt}点伤害!')
                        car_B -= hurt
                        hurt = 0
                    if chooseb == 'B':
                        choose = input('因为你选择了防御,所以伤害不计入')
                    choose = input(f'你被飞碟骑兵B扣除了{hurtB}点血')
                    dead_interface()
                    hurtB = 0
                    att_choose = 0
                    if respawned == 1:
                        break
            if DSC == 0 and car_A > 0 and car_B > 0:
                input('飞碟正在准备一次联合激光打击！')
                DSC = random.randint(4,5)
                boom = 3
                while boom > 0:
                    boom -= 1
                    x = random.randint(1,4)
                    a = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    b = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    c = chr(ord('A') + x - 1)
                    enemy_fight = a+b+c
                    enemy_fighta = [a,b,c]
                    hurt = 0
                    hurtB = 0
                    chance = 0
                    wrong = 0
                    choose = list(input('请输入三个大写字母，共输入三次！'))
                    while wrong == 0:
                        wrong = 1
                        if len(choose) != 3:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!'))
                        elif choose[0] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!'))
                        elif choose[1] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!'))
                    cube_act = random.randint(1,20)
                    if '零剑' in weapon:
                        zero_att = random.randint(5,50)
                    if '零剑-II' in weapon:
                        zero_att = random.randint(30,70)
                    if 'Complex机甲长剑' in weapon and random.randint(1,10) == 3:
                        zero_att = 10
                    while chance < 3:
                        f = choose.pop()
                        g = enemy_fighta.pop()
                        if (f == 'A' and g == 'B') or (f == 'B' and g == 'C') or (f == 'C' and g == 'D') or (f == 'D' and g == 'A'):
                            hurt += att
                            chance += 1
                            if att_choose == 1:
                                hurt += 5
                            if cube_act <= 3:
                                hurt -= 40
                                laser(40)
                            else:
                                laser(0)
                            if '虚空之刃' in weapon and random.randint(1,5) == 2:
                                hurt += int((car_A+car_B)/5)
                            hurt += item_att
                            hurt += zero_att
                            if hucker == 1:
                                hurt += 10
                            if miaomiao == 3:
                                hurt += random.randint(10,50)
                        if (f == 'D' and g == 'C') or (f == 'C' and g == 'B') or (f == 'B' and g == 'A') or (f == 'A' and g == 'D'):
                            hurtB += 27
                            chance += 1
                            if coat == 1 and random.randint(1,10) != 5:
                                hurtB = 0
                            if miaomiao == 1:
                                hurtB /= 2
                                hurt_B = int(hurtB)
                            else:
                                health += 10
                        else:
                            chance += 1
                    if hide[0] + hide[1] >= random.randint(1,100):
                        hurtB = 0
                    if miaomiao == 1:
                        hurtB /= 2
                    if miaomiao == 2:
                        hurtB /= 5
                    if S_up == 1:
                        if zero_H > 0:
                            zero_H -= hurtB
                        else:
                            health -= hurtB
                    else:
                            health -= hurtB
                    choose = input(f'飞碟骑兵的攻击是{enemy_fight}')
                    if chooseb != 'B':
                        choose = input(f'你对两个飞碟骑兵造成了{hurt}点伤害!')
                        car_A -= hurt
                        car_B -= hurt
                        hurt = 0
                    choose = input(f'你被地飞碟骑兵扣除了{hurtB}点血')
                if car_A > 0:
                    car_A += 50
                if car_B > 0:
                    car_B += 50
            dead_interface()
            hurtB = 0
            att_choose = 0
            if respawned == 1:
                break
            hide[1] = 0
            coat = 0
            miaomiao = 0
            if DS == 0:
                DS = random.randint(3,5)
            if DSB > 75:
                input('你被激光重击了！')
                chooseb = 'B'
            if car_A > 0:
                car_A += random.randint(1,4)
            if car_B > 0:
                car_B += random.randint(1,4)
            if car_A <= 0 and car_B <= 0:
                choose = input('您获胜了!')
                CM_get = random.randint(1216,1522)
                CM += CM_get
                choose = input(f'你获得了{CM_get}个CM币')
                E_cotton += 1
                win = 1

        if respawned == 1:
            respawned = 0
            continue

        output('你们击败了飞碟，飞碟飞速地砸到地面上发出巨响，随后像滚轮一般地滚走了。')
        output('你们进入了电梯，电梯随即向上升去。')
        output('你突然感到有点不对劲，这时，电梯里的灯光突然暗了下来！')
        output('“什么？这是陷阱吗？！”So问。')
        output('一道道激光突然从你旁边射出，还好没有射中你。')
        output('“天哪！太危险了！”So惊叫。')
        if '遥控器' in item:
            output('你突然想到拿出遥控器，按了下上面的红蓝按钮，激光顿时消失，旁边出来了一个红色和蓝色的显示屏。')
            output('“啊……终于，不过我没看到激光发射器啊……”昵称看向电梯的墙壁说。')
            output('你看了看显示屏，，又按了一下红色的按钮，一道红色的激光从红显示屏上发出来。')
            output('“显示屏也能发激光……太危险了。”So说。')
        else:
            output('激光顿时消失，你的周围突然出现了许多红蓝色的小光点。')
            output('“当心！这些光点，马上就会有激光射出来！”黑暗中一个声音传来。')
            go = 1
            while go <= 10:
                count = 0
                choose = list(input(f'请输入你的第{go}次躲避方式（回复1个字母,一共需要回复十次）'))
                go += 1
                x = random.randint(1,4)
                a = chr(ord('A') + x - 1)
                enemy_fighta = a
                hurt = 0
                hurtB = 0
                chance = 0
                wrong = 0
                while wrong == 0:
                    wrong = 1
                    if len(choose) != 1:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的躲避方式!(1个一组,由1个大写字母构成)'))
                    elif choose[0] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的躲避方式!(1个一组,由1个大写字母构成)'))
                else:
                    while chance < 1:
                    #快悄悄这个地方,我把chance < 5写成了chance <= 5然后查了一天才查到这个bug
                    #悄悄改为瞧瞧,这是个错别字(划)通假字
                    #快看,这里我复制的前面
                        #快看，我还是复制的前面（
                        f = choose.pop()
                        g = enemy_fighta
                        laser = random.randint(1,2)
                        if f == 'D' and g == 'C' or f == 'C' and g == 'B' or f == 'B' and g == 'A' or f == 'A' and g == 'D':
                            if laser == 1:
                                hurtB = 20
                            elif laser == 2:
                                hurtB = 30
                            chance += 1
                        else:
                            chance += 1
                            count += 1
                    choose = input(f'激光的进攻方式是{enemy_fighta}')
                    if hurtB == 0:
                        input('你通过了这条激光！')
                    else:
                        health -= hurtB
                        if hurtB == 20:
                            input('你被蓝激光击中了,你受到了20点伤害！')
                        if hurtB == 30:
                            input('你被红激光击中了,你受到了30点伤害！')
                    dead_interface()
                    if respawned == 1:
                        respawned = 0
                        continue

        output('电梯过了好一会儿才到顶，你们发现自己身处比特塔的90楼。')
        output('“比特塔只有92楼，我们现在已经快接近顶点了。”昵称说。')
        output('你们来到了一个类似于科技馆穹顶的地方。前面有两条路，各自通往后面漆黑一片的地方。')
        output('你刚想上前试探一下，却听见了右边的道路上好像有交谈声。')
        output('你会：A：继续听，B：走左边的道路，C：走右边的道路')
        while choose not in {'A','B'}:
            output('你会：A：继续听，B：走左边的道路，C：走右边的道路')
        if choose == 'C':
            output('你刚想凑上去，却被So拉住了。“冷静！不能硬上！”')
            choose = 'A'
        if choose == 'A':
            output('你继续听，隐隐约约地能听到交谈的内容：')
            output('“……是的，阿尔法，他们马上就会接近……我们最好快点……”')
            output('“你说得对，贝塔，但……以So的能力……最后的战斗会很困难……”')
            output('“记住，我们是目标指向型！目标指向型！记得我们的目标吗？”')
            output('“记得是记得，你……说话太大声了……不会被听到吗？”')
            output('“怕什么？哪怕他们走到这来都没关系……我们只需要……守住终极核心……然后……提取他们的记忆碎片……So和昵称不需要太多，Zero……”')
            output('“可是……万一计划失败了……”')
            output('“在前面……最后让他们来接应……我们一起……走吧……”')
            output('谈话声消失了，你发现右边的通道里隐隐约约地有一个自动门关闭了。')
            output('你决定走左边')
        elif choose == 'B':
            output('你走左边的路')
        output('你们向前走去，经过了一段黑暗的过道，来到了一座实验室。许多金属与玻璃仪器摆在旁边的桌子上，几个看起来像平板车一样的东西靠在墙角。')
        output('“地图上显示，前面是一段楼梯，过了楼梯之后是露天的平台……”昵称说。')
        output('你们在实验室里绕来绕去，并没有找到门，倒是在一块空地上发现了三个路障，这些路障在实验室里显得很突兀。')
        output('“恐怕是一个谜题……”So说。')
        output('你会：A：寻找实验器材,B：翻动路障')
        while choose not in {'A','B'}:
            output('你会：A：寻找实验器材,B：翻动路障')
        if choose == 'A':
            output('你发现了试管、烧杯、注射器等常见的实验器材以及一些不常见的像金属片一样的器材，没有一样东西和路障有关联。')
        elif choose == 'B':
            output('你翻了翻路障，在路障下面找到了500CMB')
            CM += 500
        output('这时，正在墙壁上仔细寻找的So突然说：“嘿，快来看，这里有个显示屏！”')
        output('你们马上凑到So跟前，So念显示屏上的文字说：“这是一个多人合作谜题，你们只需要将三个路障在同一时间移动到相应的位置，就能开启前面墙壁上的大门。注意，如果不能在同一时间从其它地方移动到规定位置，将不会触发机关。”')
        output('你看了看三个路障，发现路障周围的地上出现了两个蓝色的圆圈。')
        output('“只给了两个位置……看来第三个要自己找。”')
        output('你会：A：到实验室其它地方找,B：直接推开路障')
        while choose not in {'A','B'}:
            output('你会：A：到实验室其它地方找,B：直接推开路障')
        if choose == 'A':
            choose = input('你没找到另一个圆圈，却在一把椅子上意外地发现了一个能量核心！（获得【能量核心】）')
            item.append('能量核心')
            view_status()
        output('你想了想，推开了中间的那个路障，一个蓝色的圆圈出现在了路障的下面。')
        output('“原来是这点小把戏。”So说道。')
        output('So和昵称把另外两个路障推到了那两个圆圈旁边：“倒数三个数，我们一起推到圆圈里面：3、2、1——”')
        output('你用力把路障推到了圆圈里面。墙壁上顿时出现了一道门。')
        output('你转头看了看So和昵称，两人却不见了踪影！地上的圆圈已经消失，取而代之的是两个大坑')
        output('你趴在坑上向下看去，里面是深不见底的比特塔内部。')
        output('从这么高的楼上掉下去，肯定必死无疑。')
        output('这时，你的后面传来了阵阵脚步声。')
        output('你会：A：继续趴在坑上看,B：向前跑')
        while choose not in {'A','B'}:
            output('你会：A：继续趴在坑上看,B：向前跑')
        if choose == 'A':
            output('你趴在坑上看了一会儿，脚步声越来越近，你出于本能向门口跑去')
        elif choose == 'B':
            output('你向门口跑去')
        output('你跑出大门，前面是一排排楼梯，楼梯上有一排排的升降门拦着。')
        output('没有必要多想。')
        go = 0
        while go == 0:
            count = 0
            choose = list(input('请输入你的通过方式（回复字母通过升降门，4/7通过）'))
            x = random.randint(1,4)
            a = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            b = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            c = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            d = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            e = chr(ord('A') + x - 1)
            enemy_fight = a+b+c+d+e+y+z
            enemy_fighta = [a,b,c,d,e,y,z]
            hurt = 0
            hurtB = 0
            chance = 0
            wrong = 0
            while wrong == 0:
                wrong = 1
                if len(choose) != 7:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(7个一组,由7个大写字母构成)'))
                elif choose[0] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(7个一组,由7个大写字母构成)'))
                elif choose[1] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(7个一组,由7个大写字母构成)'))
                elif choose[2] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(7个一组,由7个大写字母构成)'))
                elif choose[3] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(7个一组,由7个大写字母构成)'))
                elif choose[4] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(7个一组,由7个大写字母构成)'))
                elif choose[5] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(7个一组,由7个大写字母构成)'))
                elif choose[6] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(7个一组,由7个大写字母构成)'))
            else:
                while chance < 7:
                    #快看，我还是复制的前面（
                    f = choose.pop()
                    g = enemy_fighta.pop()
                    if f == 'D' and g == 'C' or f == 'C' and g == 'B' or f == 'B' and g == 'A' or f == 'A' and g == 'D':
                        hurtB += 5
                        chance += 1
                    else:
                        chance += 1
                        count += 1
                choose = input(f'升降门的升降方式是{enemy_fight}')
                if count >= 4:
                    input('你通过了升降门！')
                    go = 1
                else:
                    health -= hurtB
                    choose = input(f'你没能通过升降门！你被扣除了{hurtB}点血量')
                dead_interface()
                if respawned == 1:
                    respawned = 0
                    continue
        output('你通过了升降门，来到一座露天的平台。')
        output('平台的前面有另一个门，正当你观察着门里的情况时，你发现你身后的楼梯上冲出来许多端着枪的机器人。')
        output('“这就是Zero！别让她跑了！！！”为首的机器人说。')
        if '水枪' in item:
            output('你会：A：逃跑,B：拿出水枪射击')
            while choose not in {'A','B'}:
                output('你会：A：逃跑,B：拿出水枪射击')
        else:
            output('你会：A：逃跑')
            while choose != 'A':
                output('你会：A：逃跑')
        if choose == 'A':
            output('你向门口逃去，你听见机器人大叫一声：“开枪！”')
            output('子弹如流星雨般向你划来。')
            choose = input(f'请输入你的躲避方式（回复5个字母）')
            x = random.randint(1,4)
            a = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            b = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            c = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            d = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            e = chr(ord('A') + x - 1)
            hurt = 0
            hurtB = 0
            chance = 0
            wrong = 0
            while wrong == 0:
                wrong = 1
                if len(choose) != 1:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(5个一组,由5个大写字母构成)'))
                elif choose[0] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(5个一组,由5个大写字母构成)'))
                elif choose[1] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(5个一组,由5个大写字母构成)'))
                elif choose[2] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(5个一组,由5个大写字母构成)'))
                elif choose[3] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(5个一组,由5个大写字母构成)'))
                elif choose[4] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(5个一组,由5个大写字母构成)'))
            if choose[4] == 'A':
                e = 'D'
            if choose[4] == 'B':
                e = 'A'
            if choose[4] == 'C':
                e = 'B'
            if choose[4] == 'D':
                e = 'C'
            enemy_fighta = [a,b,c,d,e]
            enemy_fight = a+b+c+d+e
            while chance < 1:
            #快悄悄这个地方,我把chance < 5写成了chance <= 5然后查了一天才查到这个bug
            #悄悄改为瞧瞧,这是个错别字(划)通假字
            #快看,这里我复制的前面
                #快看，我还是复制的前面（
                f = choose.pop()
                g = enemy_fighta.pop()
                laser = random.randint(1,2)
                if f == 'D' and g == 'C' or f == 'C' and g == 'B' or f == 'B' and g == 'A' or f == 'A' and g == 'D':
                    hurtB += 15
                    chance += 1
                else:
                    chance += 1
                    count += 1
            choose = input(f'敌人的进攻方式是{enemy_fight}')
            health -= hurtB
            input(f'你受到了{hurtB} 点伤害！')
            dead_interface()
            if respawned == 1:
                respawned = 0
                continue


        elif choose == 'B':
            output('你试着拿水枪射击，前面的一个机器人应声倒地。')
            output('“什么？她敢玩这个？！给我还击！火力压制！！！”机器人怒骂道。')
            output('机器人一齐向你开火。')
            choose = input(f'请输入你的躲避方式（回复3个字母）')
            x = random.randint(1,4)
            a = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            b = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            c = chr(ord('A') + x - 1)
            hurt = 0
            hurtB = 0
            chance = 0
            wrong = 0
            while wrong == 0:
                wrong = 1
                if len(choose) != 1:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(3个一组,由3个大写字母构成)'))
                elif choose[0] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(3个一组,由3个大写字母构成)'))
                elif choose[1] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(3个一组,由3个大写字母构成)'))
                elif choose[2] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(3个一组,由3个大写字母构成)'))
            if choose[2] == 'A':
                e = 'D'
            if choose[2] == 'B':
                e = 'A'
            if choose[2] == 'C':
                e = 'B'
            if choose[2] == 'D':
                e = 'C'
            enemy_fighta = [a,b,c]
            enemy_fight = a+b+c
            while chance < 3:
            #快悄悄这个地方,我把chance < 5写成了chance <= 5然后查了一天才查到这个bug
            #悄悄改为瞧瞧,这是个错别字(划)通假字
            #快看,这里我复制的前面
                #快看，我还是复制的前面（
                f = choose.pop()
                g = enemy_fighta.pop()
                laser = random.randint(1,2)
                if f == 'D' and g == 'C' or f == 'C' and g == 'B' or f == 'B' and g == 'A' or f == 'A' and g == 'D':
                    hurtB += 15
                    chance += 1
                else:
                    chance += 1
                    count += 1
            choose = input(f'敌人的进攻方式是{enemy_fight}')
            health -= hurtB
            input(f'你受到了{hurtB} 点伤害！')
            dead_interface()
            if respawned == 1:
                respawned = 0
                continue
        savepoint = 23
    #做个存档点标记
    if savepoint == 23:
        save_data()
        output('你尽力地躲避机器人的攻击，但还是被击中了几枪。')
        output('你带伤走到前面长廊的深处，这里的光线非常暗。由于剧痛你有点站不稳，跌跌撞撞地向前走去，不小心被一个台阶绊倒在地。')
        output('你捂住伤口卷缩在地上。')
        output('意识开始模糊，要死了吗？')
        output('黑暗中，你似乎感到一个人影向你面前走来。')
        output('突然间，你感到了一丝丝阵痛，就像一个人在你的身体里不断地用皮鞭抽打你一样')
        output('手脚冰凉，你动弹不得。')
        output('你的意识逐渐被黑暗侵蚀。')
        output('【进入：记忆碎片-455023A】')
        health = 300
        output('遥远的地方，似乎有两个意识正在试图把你唤醒——')
        output('想象一般的画面感，不过有什么东西被剥离出去了，留下了纯纯的记忆……')
        output('在城市的夜空下，So和昵称正在一条繁华的大街上散步。')
        output('“亲爱的昵称称，你想吃点什么吗？”So亲切地对昵称说。')
        output('“嗯……我想想，我们买冰激凌，你一个我一个，就这么决定了！”昵称开心地回答。')
        output('两人散步在街头，影子在城市的灯光下呈现出一个扁扁的心形。')
        output('很快，他们走到了一个冰激凌摊前，可是摊前人太多了，排成了一个长队')
        output('要排队吗：A：排队,B：去其它地方')
        while choose not in {'A','B'}:
            output('要排队吗：A：排队,B：去其它地方')
        output('人太多了，没有必要一直排下去。')
        output('两人静静走在嘈杂的街头上。迎面走来一个街头游行队，许多机器人拥簇着一个大得吓人的木马上前走来，没过多久，迎面又到来一个木马，这样反反复复，一共十二个木马经过了他们面前。')
        output('“这些木马好吓人啊。”昵称说。')
        output('So会做什么呢？')
        output('A：不管他,B：问下游行群众')
        while choose not in {'A','B'}:
            output('A：不管他,B：问下游行群众')
        if choose == 'B':
            output('一个机器人说：“这些是机械木马，城市里许多著名的建筑工匠锻造了这些，一共有十三个，都是上等的工艺品。木马的材料是从外地购入的小型木马，利用特殊手段拼接而成。它是我们游行活动非常重要的环节。不过大概半年前，有四个像扑克一样的人想花大价钱购买一个木马，本来我们不想给他，但想了想，木马一共十三个也不太吉利，于是就卖给他们了一个最小的……狠赚了一笔呢！”')
        output('两人离开了木马游行队，不知不觉间走上了一座桥。')
        output('众多粉红色的显示屏，如粉色的气球，摆成各种图案飞上天空。在夜空中显得格外动人。')
        output('“好美的景色，好美的城市！”昵称说')
        output('“真美……”So回答')
        output('“好想留在这里……”昵称说')
        output('接下来So的态度是？A：表示认可,B：提醒昵称还有可恶的赛恩思')
        while choose not in {'A','B'}:
            output('接下来So的态度是？A：表示认可,B：提醒昵称还有可恶的赛恩思')
        output('“可是昵称……这里这么好，还有一个……大坏蛋赛恩思在这儿，如果我们能先击败他，再留下来也好啊……”')
        output('“你说得对！我们这就去击败赛恩思！”昵称说完对天空做了个挥剑的动作，但很快就停了下来。')
        output('“话说回来，我们摔下来的时候，你……真的昏倒了吗？”昵称问。')
        output('“我看到你昏倒了才叫起来的……我感觉可能睡了个觉……不，我觉得我真的昏了过去！”')
        output('“可是被力场接住不是不会有事的吗？为什么会昏倒呢？”')
        output('就在这时，粉色的显示屏背景中突然亮出了一个刺眼的蓝色显示屏：')
        output('“因为，我们提取了你们的记忆碎片！”')
        output('“你是！！！”So站在昵称前面大声说。')
        output('“我是阿尔法啊！嘿嘿，当你们还沉浸在，你们那狭小的二人世界中时，你不知道的是，我们的任务已经完成了！你失败了！')
        output('“什么？！！你们干了什么？！！”So大叫')
        output('“我们提取了你们的记忆碎片。利用力场提取记忆碎片的技术是贝塔的功劳，而我……设计了路障谜题，让你们进入了我们的圈套！哈哈！很快，当我们对你们的碎片完成加工，你们就会像小天一样，在这个世界变得透明，再也没人会注意你，你们将被困死在这里，再也没人会对我们造成威胁啦！哈哈哈！”显示屏发出一阵颤抖。')
        output('“你！！你！！”So气急败坏地喊道。')
        output('“生气也没用哦，你们已经被永久逐出比特塔，永远也离不开这里啦！等贝塔解决掉比特塔上的Zero，赛恩思，以及他所在的SEED，就可以征服整个魔法界域，我们的计划，就彻底地完成啦！！！”显示屏闪了两下，然后消失了')
        output('“不！！！！！”So歇斯底里地大叫，他似乎从来都没有这么激动过，甚至……这根本就不是他的声音。愤怒的喊叫声似乎把世界撕出了一条缝，一些崭新的东西从缝里流了出来，逐渐将世界填满。')
        output('你醒了过来')
        output('你发现自己躺在一大块硬铁板上，四肢都被一个类似于手铐的东西锁在床上动弹不得。')
        output('你看了看自己的身体，发现之前的枪伤已经消失。')
        output('一个扁扁的机器人走到你躺的铁板……床前，对你说：“醒了，那你也应该知道我是谁了。”')
        output('“在我完成任务之前，我必须先介绍一下所谓的记忆碎片。不能让你不明不白地丧失掉。”')
        output('“所谓记忆碎片，就是你灵魂中的记忆片段。你的灵魂是一个记忆储存器，它将记忆储存、整合起来，压缩成许多个可以提取使用的片段。这些片段就是我们说的“记忆碎片”。每个人都可以读取自身的“记忆碎片”来回想起以前的事情。”')
        output('“然而，有些事情我们并不能回想起来，我们称之为“遗忘的记忆”，然而这些记忆并不是遗忘，而是以备份的形式储存在灵魂的一角，它仍然能被提取和导出。这就是我的“记忆碎片提取器”的任务。”')
        output('“记忆碎片被提取之后，可以导入到其他人的魔法核心，使被导入者获得碎片中的记忆，只不过，由于记忆的冲突性，这样的导入往往会让被导入者痛苦无比。”')
        output('“记忆碎片与魔法核心密切相关，要是一个人的记忆碎片被导出，就说明他的魔法核心已经暴露无疑，可以随意加工改造，甚至摧毁。我们在抓到小天后，提取了他的记忆碎片，并进行了加工，使他没有办法被正常探测到，变成了透明人，我们删掉了他记忆里关于我们的部分，使他不知道我们几个帮手的存在。我们也准备对So和昵称进行类似的加工。”')
        output('“而对于你，我们可不能简简单单地提取一个记忆碎片完事。我们要置你于死地，我们希望提取你所有的记忆碎片，这样你会很快丧失所有的记忆，变成只能进行生理活动而没有任何灵魂能力的“植物人”，你不会死，但很难恢复原状。”')
        output('机器人平静地说完了这些恐怖的话语，你感到他可能比阿尔法更不好对付。')
        output('机器人突然从你身边走开，在一个柜子上拿起了许许多多的金属刷子。')
        output('“力场提取记忆碎片的技术是不彻底的，对你，我们还是要采取传统的提取方式。”')
        output('机器人把刷子挨个地放在你身上。')
        output('你会：A：不管他,B：挣扎')
        while choose not in {'A','B'}:
            output('你会：A：不管他,B：挣扎')
        if choose == 'B':
            output('你使劲乱动着身子，金属刷像黏在你皮肤上一样纹丝不动。')
        output('机器人继续在你身上摆放着金属刷子，很快，你的全身，甚至是最私密的部位都被贴上了金属刷子。')
        output('你看着机器人把刷子用电线连接在一个十分奇怪的机器上，机器人突然开始倒数计时：')
        output('“10、9、8……”')
        output('你闭上眼睛。')
        output('但当机器人数到5时，四周突然出现了吓人的警报声，你睁开眼睛一看，墙壁都变成了红色。机器前，一个巨大显示屏标着显眼的“ERROR”字样。')
        output('“反射过度，我得马上离开。”机器人自言自语道，似乎在自我镇定，马上从你前面的一个门逃走了。')
        output('你发现类似手铐的东西突然打开了，你坐起身来，身上的刷子纷纷掉落在地。')
        output('你会：A：立刻离开,B：看看机器')
        while choose not in {'A','B'}:
            output('你会：A：立刻离开,B：看看机器')
        if choose == 'B':
            output('机器上闪着不详的红色光芒。')
        output('你来到房间外，这里也响起了凄厉的警报声，你并不知道这意味着什么。')
        output('你的前面是一条走廊，走廊上方的顶灯泛出蓝色的微光')
        output('你向前面跑去，顿时听到之前机器人的大喊声：')
        output('“目标已经逃跑！坐标：91楼，第四走廊，瑞德、布鲁，你们需要立即追击！”')
        output('走廊上方传来了诡异的骚动，你发现两个黑影从你前后向你包围过来。')
        output('“B计划：发现目标！立即处置！我只说一遍！立即处置！”机器人的声音传来。')
        output('两个黑影在黑暗中现身，你发现他们是一红一蓝的两个像素幽灵。')
        savepoint = 24
    #做个存档点标记
    if savepoint == 24:
        save_data()
        output('两个幽灵迅速向你靠近。')
        print('【战斗开始】 对战 瑞德 x 布鲁')
        frozen_cd = random.randint(5,6)
        frozen = 0
        blue_shield = 0
        fire_cd = random.randint(3,5)
        red_fire = 0
        item_att = 0
        fire_count = 0
        laser_barrier = 4
        hucker = 0
        boom_snake = 0
        zero_H = ''
        zero_W = ''
        if S_up == 1:
            zero_H = 0
            zero_H = int(zero_H)
            zero_W = '护盾血量'
        big_fight = 0
        t.sleep(0.5)
        car_A,car_B = 623,554
        check = 0
        magic_point = 0
        miaomiao = 0
        coat = 0
        win = 0
        a,b,c,d,e = '','','','',''
        while win == 0:
            zero_att = 0
            magic_choose = 0
            att_choose = 0
            item_choose = 0
            item_att = 0
            while magic_choose == 0 and item_choose == 0:
                if car_A <= 0:
                    car_A = 0
                if car_B <= 0:
                    car_B = 0
                chooseb = 'A'
                if '战争宝石' in item:
                    print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health}{zero_W}{zero_H},暴击数{big_fight},布鲁血量为{car_A}加冰障{blue_shield},攻击力为30，防御力为15，防御率70%,瑞德血量为{car_B},攻击力为33，防御力28，防御率30%')
                if '战争宝石' not in item:
                    print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health}{zero_W}{zero_H},布鲁血量为{car_A}加冰障{blue_shield},瑞德血量为{car_B}')
                choose = input('A,物品B,防御C,魔法D,跳过')
                while choose not in {'A','B','C','D'}:
                    print('请做出你的选择')
                    choose = input('A,物品B,防御C,魔法D,跳过')
                if choose == 'A':
                    choose = input(f'你现在可使用的物品有{fight_item},请从1开始输入序号以选择使用的物品')
                    if choose not in {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'}:
                        choose = input('物品序号输入错误!')
                    else:
                        choose = int(choose)
                        if choose > len(fight_item):
                            choose = input('物品序号输入错误!')
                        else:
                            check = fight_item[choose]
                            item_find()
                            if check == '魔法炸药':
                                input('你对对方造成了100点伤害!但你也不小心受到了30点伤害')
                                health -= 30
                                car_A -= 100
                                car_B -= 100
                                dead_interface()
                                if respawned == 1:
                                    break
                            if check == '坚硬冰棍':
                                choose = input('请选择投掷的对象（填A或者B）')
                                while choose not in {'A','B'}:
                                    choose = input('请选择投掷的对象（填A或者B）')
                                if choose == 'A':
                                    choose = input('你使用了坚硬冰棍!瑞德的HP降低了100点!')
                                    car_A -= 100
                                else:
                                    choose = input('你使用了坚硬冰棍!布鲁的HP降低了100点!')
                                    car_B -= 100
                            if check == '像素板':
                                choose = input('你使用了像素板!幽灵受到了70点伤害！')
                                car_A -= 70
                                car_B -= 70
                            item_choose = 1
                            if health > 300:
                                health = 300
                elif choose == 'B':
                    choose = input('你选择了防御!')
                    magic_point += 40
                    magic_choose = 1
                    if magic_point >= 100:
                        magic_point = 100
                    chooseb = 'B'
                elif choose == 'C':
                    bit_magic('normal')
                elif choose == 'D':
                    input('你跳过了你的回合')
                    magic_choose = 1
                if car_A >= 0 and car_B >= 0:
                    if laser_barrier > 0:
                        laser_barrier -= 1
                    else:
                        input('瑞德与布鲁共同构建了一个红蓝激光屏障！')
                        laser_barrier_hurt = 0
                        rb_laser = [['R','B'][random.randint(0,1)],['R','B'][random.randint(0,1)],['R','B'][random.randint(0,1)]]
                        laser_barrier = 4
                        choose = input('请回复三个由R和B组成的字母通过激光！')
                        while len(choose) != 3 or choose.count('R')+choose.count('B') != 3:
                            choose = input('输入错误，请回复三个由R和B组成的字母通过激光！')
                        else:
                            input(f'激光屏障为{rb_laser}')
                            for i in range(0,2):
                                if rb_laser[i] != choose[i]:
                                    if rb_laser[i] == 'R':
                                        laser_barrier_hurt += 20
                                    else:
                                        laser_barrier_hurt += 30
                            if laser_barrier_hurt > 0:
                                input(f'你没有通过激光屏障，受到了{laser_barrier_hurt}点伤害')
                            else:
                                input('你通过了激光屏障')
            car_act_B = random.randint(1,6)
            if '混乱护盾' in armor:
                health += random.randint(3,20)
                if health >= 300:
                    health = 300
            if car_act_B == 1:
                input('激烈的战斗持续进行着')
            if car_act_B == 2:
                input('幽灵认为没有必要多想')
            if car_act_B == 3:
                input('幽灵重复着自己的攻击')
            if car_act_B == 4:
                input('幽灵们在周围制造了一发装饰性激光')
            if car_act_B == 5:
                input('你和幽灵在昏暗的走廊周旋着')
            if car_act_B == 6:
                input('幽灵认为对付你简直易如反掌')
            if car_A > 0:
                x = random.randint(1,4)
                a = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                b = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                c = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                d = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                e = chr(ord('A') + x - 1)
                if miaomiao == 4:
                    b,c,d,e = a
                enemy_fight = a+b+c+d+e
                enemy_fighta = [a,b,c,d,e]
                zero_att = 0
                if '零剑' in weapon:
                    zero_att = random.randint(5,50)
                if '零剑-II' in weapon:
                    zero_att = random.randint(30,70)
                if 'Complex机甲长剑' in weapon and random.randint(1,10) == 3:
                    zero_att = 10
                choose = list(input(f'请选择你对布鲁的攻击!(5个一组,由五个大写字母构成)'))
                hurt = 0
                hurtB = 0
                chance = 0
                wrong = 0
                while wrong == 0:
                    wrong = 1
                    if len(choose) != 5:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[0] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[1] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[2] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[3] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[4] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                else:
                    if frozen_cd <= 0:
                        frozen_cd = random.randint(5,6)
                        input('布鲁在四周召唤了一股强烈的旋风！周围开始结冰！你的攻击下降10点')
                        att -= 10
                        frozen = 1
                    else:
                        frozen_cd -= 1
                    cube_act = random.randint(1,10)
                    while chance < 5:
                        f = choose.pop()
                        g = enemy_fighta.pop()
                        if chooseb != 'B':
                            if (f == 'A' and g == 'B') or (f == 'B' and g == 'C') or (f == 'C' and g == 'D') or (f == 'D' and g == 'A'):
                                hurt += att
                                chance += 1
                                if att_choose == 1:
                                    hurt += 5
                                    if '战争宝石' in item:
                                        hurt += 5
                                if cube_act > 7:
                                    hurt -= 15
                                    laser(15)
                                else:
                                    laser(0)
                                if '虚空之刃' in weapon and random.randint(1,5) == 2:
                                    hurt += int(car_A/5)
                                hurt += item_att
                                hurt += zero_att
                                if miaomiao == 3:
                                    hurt += random.randint(10,50)
                                if hucker == 1:
                                    hurt += 10
                                
                        if (f == 'D' and g == 'C') or (f == 'C' and g == 'B') or (f == 'B' and g == 'A') or (f == 'A' and g == 'D'):
                            hurtB += 30
                            if chooseb == 'B':
                                hurtB -= Def
                                if hucker == 1:
                                    hurtB -= 30
                                if hurtB < 0:
                                    hurtB = 0
                            chance += 1
                            if coat == 1 and random.randint(1,10) == 5:
                                hurtB = 0
                            else:
                                health += 10
                        else:
                            chance += 1
                    if random.randint(1,20) == 3 and '战争宝石' in item and att_choose == 1:
                        hurt *= 3
                    if miaomiao == 1:
                        hurtB /= 2
                    if miaomiao == 2:
                        hurtB /=5
                    hurtB = int(hurtB)
                    if hide[0] + hide[1] >= random.randint(1,100):
                        hurtB = 0
                    if S_up == 1:
                        if zero_H > 0:
                            zero_H -= health
                        else:
                            health -= hurtB
                    else:
                        health -= hurtB
                    item_att = 0
                    choose = input(f'布鲁的攻击是{enemy_fight}')
                    if cube_act > 7 :
                        choose = input('布鲁使用了防御!')
                    if chooseb != 'B':
                        choose = input(f'你对布鲁造成了{hurt}点伤害!')
                        if blue_shield > hurt:
                            blue_shield -= hurt
                        else:
                            blue_shield = 0
                            car_A -= abs(blue_shield - hurt)
                        hurt = 0
                    if chooseb == 'B':
                        choose = input('因为你选择了防御,所以伤害不计入')
                   
                    choose = input(f'你被敌人扣除了{hurtB}点血')
                    if car_A > 0 and frozen == 1:
                        input('布鲁获得了一个冰障！')
                        blue_shield = 125
                        frozen = 0
                    dead_interface()
                    if respawned == 1:
                        break
            if car_B > 0:
                x = random.randint(1,4)
                a = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                b = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                c = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                d = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                e = chr(ord('A') + x - 1)
                if miaomiao == 4:
                    b,c,d,e = a
                enemy_fight = a+b+c+d+e
                enemy_fighta = [a,b,c,d,e]
                zero_att = 0
                if '零剑' in weapon:
                    zero_att = random.randint(5,50)
                if '零剑-II' in weapon:
                    zero_att = random.randint(30,70)
                if 'Complex机甲长剑' in weapon and random.randint(1,10) == 3:
                    zero_att = 10
                choose = list(input(f'请选择你对瑞德的攻击!(5个一组,由五个大写字母构成)'))
                hurt = 0
                hurtB = 0
                chance = 0
                wrong = 0
                while wrong == 0:
                    wrong = 1
                    if len(choose) != 5:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[0] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[1] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[2] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[3] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[4] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                else:
                    if fire_cd <= 0:
                        fire_cd = random.randint(3,5)
                        input('瑞德在四周放射出强烈的火焰！')
                        red_fire = 3
                        fire_count = 0
                    else:
                        fire_cd -= 1
                    cube_act = random.randint(1,10)
                    while chance < 5:
                        f = choose.pop()
                        g = enemy_fighta.pop()
                        if chooseb != 'B':
                            if (f == 'A' and g == 'B') or (f == 'B' and g == 'C') or (f == 'C' and g == 'D') or (f == 'D' and g == 'A'):
                                hurt += att
                                chance += 1
                                if att_choose == 1:
                                    hurt += 5
                                    if '战争宝石' in item:
                                        hurt += 5
                                if cube_act <= 3:
                                    hurt -= 28
                                    laser(28)
                                else:
                                    laser(0)
                                if '虚空之刃' in weapon and random.randint(1,5) == 2:
                                    hurt += int(car_B/5)
                                hurt += item_att
                                hurt += zero_att
                                if hucker == 1:
                                    hurt += 10
                                if miaomiao == 3:
                                    hurt += random.randint(10,50)
                                
                        if (f == 'D' and g == 'C') or (f == 'C' and g == 'B') or (f == 'B' and g == 'A') or (f == 'A' and g == 'D'):
                            if red_fire > 0:
                                fire_count += 1
                            hurtB += 33
                            if chooseb == 'B':
                                hurtB -= Def
                                if hucker == 1:
                                    hurtB -= 30
                                if hurtB < 0:
                                    hurtB = 0
                            chance += 1
                            if coat == 1 and random.randint(1,10) != 5:
                                hurtB = 0
                            else:
                                health += 10
                        else:
                            chance += 1
                    if miaomiao == 1:
                        hurtB /= 2
                    if miaomiao == 2:
                        hurtB /=5
                    hurtB = int(hurtB)
                    if hide[0] + hide[1] >= random.randint(1,100):
                        hurtB = 0
                    if S_up == 1:
                        if zero_H > 0:
                            zero_H -= hurtB
                        else:
                            health -= hurtB
                    else:
                        health -= hurtB
                    item_att = 0
                    if random.randint(1,20) == 3 and '战争宝石' in item and att_choose == 1:
                        hurt *= 3
                    choose = input(f'瑞德的攻击是{enemy_fight}')
                    if cube_act <= 3 :
                        choose = input('瑞德使用了防御!')
                    if chooseb != 'B':
                        choose = input(f'你对瑞德造成了{hurt}点伤害!')
                        car_B -= hurt
                        hurt = 0
                    if chooseb == 'B':
                        choose = input('因为你选择了防御,所以伤害不计入')
                    choose = input(f'你被瑞德扣除了{hurtB}点血')
                    if red_fire > 0:
                        input(f'你被瑞德的火焰焚烧了，你的HP降低了{fire_count*10}点！')
                        red_fire -= 1
                    dead_interface()
                    hurtB = 0
                    att_choose = 0
                    if respawned == 1:
                        break
            if S_up == 1:
                if zero_H < 0:
                    zero_H = 0
            hide[1] = 0
            coat = 0
            miaomiao = 0
            if car_A <= 0 and car_B <= 0:
                choose = input('您获胜了!')
                CM_get = random.randint(508,1561)
                CM += CM_get
                choose = input(f'你获得了{CM_get}个CM币')
                win = 1

        if respawned == 1:
            respawned = 0
            continue
#布鲁（BLUE）
#HP：623
#ATT：30
#Def：15
#P：70%
#CMB：50-1000
#特殊：
#【封冻】每5-6回合回复“布鲁在四周召唤了一股强烈的旋风！周围开始结冰”本回合你的攻击下降10点（若攻击小于10则为0），并且在下一回合准备阶段开始时若布鲁没有阵亡，回复“布鲁获得了一个冰障！”相当于一个血量为125的护盾
#瑞德（RED）
#HP：554
#ATT：33
#Def：28
#P：30%
#CMB：458-561
#特殊：
#【焚烧】每3-5回合回复“瑞德在四周放射出强烈的火焰！”，使得接下来的3回合对你持续造成焚烧伤害，造成的伤害为本回合被克制数*10，同时回复“你被瑞德的火焰焚烧了，你的HP降低了【本回合焚烧伤害】点！”
#瑞德x布鲁组合技
#当场上有瑞德和布鲁时，每4回合准备阶段结束后回复：“瑞德与布鲁共同构建了一个红蓝激光屏障！”
#需要回复三个字母通过激光，才能开始对战，激光伤害为50%20、50%30，对应蓝激光与红激光
#对话
#激烈的战斗持续进行着
#幽灵认为没有必要多想
#幽灵重复着自己的攻击
#幽灵们在周围制造了一发装饰性激光
#你和幽灵在昏暗的走廊周旋着
#幽灵认为对付你简直易如反掌
        output('你击倒了两个幽灵，向走廊尽头狂奔而去。')
        output('一跑出走廊，你发现外面是一个小小的露天过道，就在比特塔的楼墙外面，由于过道太窄，你险些翻了下去。好在你及时抓住了旁边的扶手。')
        output('这时，你突然发现塔外传来一道强烈的闪光，你马上遮住眼睛。')
        output('当你再睁开眼睛时，你发现外面停着一辆巨大的飞车，你看到So，昵称站在车上向你招手。你仔细看了看，发现车上还出现了许多熟悉的面孔：你们曾经的敌人玩具车、电子蛇与Tetris，小天也在车上对你露出了灿烂的笑容。')
        output('飞车很快停靠在塔边，So和昵称从车上下来，对你说：“Zero……你没事吧。”')
        output('So看到你没事，说：“嗯……我想你可能有点懵，我先介绍一下这位朋友。”')
        output('So的身边出现了一个大大的显示屏，上面出现了一个H字样。')
        output('“这是H，黑客村庄的机器人。虽然黑客村庄一直与世隔绝，但是他们面对赛恩思的行径终于出手了。我们掉下去之后，H帮我们找到了这辆飞车飞了上来。H还在一路上帮助这些机器人摆脱了赛恩思的控制，还复原了小天……总之，大家都回来了，这一切都要结束了。”')
        output('So意识到通道有点窄，便向后退了一步。')
        output('“我们离击败赛恩思只差一步，最关键的一步。前面有一座楼梯，走上去就是赛恩思的房间。里面有一个“终极核心”，它是赛恩思一切能力的根源。摧毁它，我们就胜利了！”')
        output('你会：A：走上楼梯,B：继续交谈')
        while choose not in {'A','B'}:
            output('你会：A：走上楼梯,B：继续交谈')
        if choose == 'B':
            output('So说：“嗯……你想知道记忆碎片的事？我其实也不怎么清楚来着。”')
        output('你走上楼梯，来到楼顶的一座屋子前。整座城市的景色在你们身后呈现出来。')
        output('你会：A：走进屋子,B：休息一会儿')
        while choose not in {'A','B'}:
            output('你会：A：走进屋子,B：休息一会儿')
        if choose == 'B':
            output('你在楼顶稍作休息了一会儿，HP完全恢复了。[HPMax]')
            health = 300
        output('你们进入屋子，里面是一个设备齐全的小房间。看上去像是书房。')
        output('你坐在房间的床上，So和昵称翻着书架上的书。这时，写字台上的一个显示屏引起了你的注意。')
        output('你会：A：看看显示屏,B：不管他,C：翻书柜,D：去其它地方看看')
        while choose not in {'A','B','C','D'}:
            output('你会：A：看看显示屏,B：不管他,C：翻书柜,D：去其它地方看看')
        if choose == 'A':
            choose = input('你看了看显示屏，上面写着：\n“A计划：提取So、昵称的部分碎片、收集Zero的全部碎片\nB计划：万一目标在搜集途中逃走，立即击毙\nC计划：若计划失败，与罗尔斯商议援兵事宜。”')
            view_status()
            output('你感到好笑。')
        elif choose == 'B':
            output('你继续坐在床上')
        elif choose == 'C':
            output('书柜上是整本整本的《社会学》与《经济管理学》，你感到有点犯困。')
        elif choose == 'D':
            output('你来到书房一个角落，这里有一个造型奇特的机器')
            output('放点东西在上面吗？A：放,B：不放')
            while choose not in {'A','B'}:
                output('放点东西在上面吗？A：放,B：不放')
            if choose == 'B':
                output('并不需要放东西')
            elif choose == 'A':
                if 'Complex' not in item:
                    output('并没有什么能放的')
                else:
                    item.remove('Complex')
                    output('你将Complex慢慢放在机器上，突然机器里面钻出了一本用显示屏显示着的书。')
                    output('你翻开看了看，居然是一本日记。')
                    output('你随便看了看日记上的内容：')
                    choose = input('XX年2月21日\n怎么……为什么……为什么会这样，我为什么会被赶出来……黑客村庄为什么会……\n好害怕，我会不会死\n好害怕\n谁来救救我……\n我不想死……')
                    view_status()
                    choose = input('XX年2月25日\n我真的绝望了，没有一个人理我\n为什么，没有一个人能关心一下我……\n我做错了……什么\n我再也不敢这样了……\n求求你们，让我进去……\n让我进去')
                    view_status()
                    choose = input('XX年2月27日\n有一个奇怪的电话找到我，说可以让我活下去。\nSEED，好奇怪，是种子吗？')
                    view_status()
                    choose = input('XX年2月28日\n名叫罗尔斯的人说要见我，说可以让我逃离现状。\n真的如此吗？我真的可以做到？\n我只不过是一个没人喜欢的废物罢了。')
                    view_status()
                    choose = input('XX年3月1日\n我的天！我的天！\n罗尔斯……SEED……真的可以拯救我……\n我太激动了……\n你们没有抛弃我……没有抛弃我……')
                    view_status()
                    choose = input('XX年3月10日\n我试着完成了SEED交给我的第一个任务，太棒了，我的账户上多了整整……十万CMB！\n这下好了，我又有希望了，先去买几个冰冻面包，然后弄一套好的出租屋……就这样了。')
                    view_status()
                    choose = input('XX年4月28日\n阿尔法和贝塔做得很不错。我的第一份记忆碎片到手了。')
                    view_status()
                    choose = input('XX年5月2日\n击败了小天那家伙，我的天，SEED这是怎么样的待遇啊——\n这么强的大厦，我们完全不怕了！')
                    view_status()
                    choose = input('XX年9月26日\n罗尔斯突然警告我注意“宿命”？\n什么是宿命……我不认识诶')
                    view_status()
                    choose = input('XX年9月27日\n恐怕有点危险\n罗尔斯说要尽快解决城市的防御工作……Zero是谁？\n罗尔斯好像很怕她\n我得找找看')
                    view_status()
                    choose = input('XX年9月28日\nZero来了。\n不过我不需要怕，瑞德和布鲁已经布置好所有的机关，必要时出动阿尔法，贝塔一直潜伏在后面。\n切记，谨慎行事！一定要谨慎！\n敌人不是不可战胜的！')
                    view_status()
                    choose = input('XX年9月28日\n完蛋了，完蛋了，为什么会这样\n我……什么工作都做好了，为什么会变成这个样子\n罗尔斯一天没回我消息了。\nSo和昵称，他们虽然强，但我靠一点计谋都可以击败他们，唯独这个Zero……为什么会……\n我到底遭到了……\nZero，你是人吗？！！！！！！！！！！')
                    view_status()
                    output('笔记到这就结束了，最后一篇看来是刚刚才写好的。')
        output('离开书房后，你们来到了一座廊桥上。')
        output('这里虽然位于比特塔顶，但你却没有看到比特塔的内部结构，看来比特塔内部和外界是隔离的。')
        output('廊桥通往前面的另一个房间，房间直接与比特塔身相连，你感到这房间的结构有些异常。')
        output('“我的卫衣显示……前面的房间存在能量密度异常大的发射体……那就是我们要找的终极核心了！错不了！”So说')
        output('你向前方的房间走去。一进门，就出现了一条宽阔的走廊。')
        output('你正想向前走去，突然So大喊一声：“小心！”')
        print('你看见旁边的墙壁上突然出现了几根像爪子一样的东西，飞速向你刺来（回复5次字母以躲避）')
        go = 0
        while go < 5:
            go += 1
            choose = input('请输入你的躲避方式')
            x = random.randint(1,4)
            a = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            b = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            c = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            d = chr(ord('A') + x - 1)
            x = random.randint(1,4)
            e = chr(ord('A') + x - 1)
            enemy_fight = a+b+c+d+e
            enemy_fighta = [a,b,c,d,e]
            hurt = 0
            hurtB = 0
            chance = 0
            wrong = 0
            while wrong == 0:
                wrong = 1
                if len(choose) != 5:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(5个一组,由五个大写字母构成)'))
                elif choose[0] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(5个一组,由五个大写字母构成)'))
                elif choose[1] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(5个一组,由五个大写字母构成)'))
                elif choose[2] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(5个一组,由五个大写字母构成)'))
                elif choose[3] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(5个一组,由五个大写字母构成)'))
                elif choose[4] not in {'A','B','C','D'}:
                    wrong = 0
                    print('输入错误,请依照格式输入!')
                    choose = list(input(f'请选择你的躲避方式!(5个一组,由五个大写字母构成)'))
            else:
                while chance < 5:
                #快悄悄这个地方,我把chance < 5写成了chance <= 5然后查了一天才查到这个bug
                #悄悄改为瞧瞧,这是个错别字(划)通假字
                #快看,这里我复制的前面
                    #快看，我还是复制的前面（
                    f = choose.pop()
                    g = enemy_fighta.pop()
                    if f == 'D' and g == 'C' or f == 'C' and g == 'B' or f == 'B' and g == 'A' or f == 'A' and g == 'D':
                        hurtB += 13
                        chance += 1
                    else:
                        chance += 1
                choose = input(f'飞爪的进攻方式是{enemy_fight}')
                choose = input('你被扣除了hurtB点血量')
                dead_interface()
                if respawned == 1:
                    respawned = 0
                    continue
#最终BOSS!!!
        output('你们躲过了爪子的攻击，来到房间的前面。')
        choose = input('一个巨大的玻璃容器出现在你面前，容器里，一个绿色的发着荧光的巨大方块出现在你们面前。[HPmax]')
        health = 300
        view_status()
        output('“这是……”So说。')
        output('“这是你们心心念念的【终极核心】”一个声音传来。')
        output('你看见一个机器人出现在容器旁边，你发现他便是你第一次见到赛恩思时的那个机器人，或者，长得完全一样。')
        output('“我是赛恩思，我本来没打算让你们进入这里来着。”机器人说。')
        output('“不过，既然这样，我也只好背水一战了。在这里不能使用佣兵，你们很快就会把我打退，然后使用【终极核心】的能量离开这里……”')
        output('“不过，从你们一到来开始，我就在思考着用什么样的方式对付你们，虽然任何的努力对你们来说都是徒劳的。但我却……在这里看到了一丝丝……希望？”')
        output('“从我被逐出黑客村庄开始，我就在思索着我们的【意义】，我们存在的意义究竟是什么，我们有什么用？”')
        output('“你，Zero，你的存在又有什么意义呢？”')
        output('So有点忍不住了：“胡言乱语什么？！”')
        output('“先听我把话说完，意义的实现，在于有东西能够看到他，不管是人还是物，只要有东西见证过他们的存在了，他们的存在便有了意义，不管这意义是什么。”')
        output('“我说过，我需要你们帮我研究我的社会学课题，我得到的……很多呢。”')
        output('你发现赛恩思的身边突然出现了一阵异样的绿光。')
        output('“我说过了，Zero、还有So和昵称，我很看重你们，你们是很强大的对手。那么，就让你们这么强大的对手，充当我的“观察者”，来看看我，我们的意义到底是吧！')
        output('赛恩思周围的绿光正在迅速增强！')
        output('一阵耀眼的强光正在吞噬你们，但很快消失不见。')
        output('赛恩思正站在你们前面，而他的后面，两只蜘蛛形态的机器人正被吊着晃来晃去。')
        output('“他们就是阿尔法和贝塔……最终形态……”昵称说，“这是刚才H告诉我的”')
        output('“我希望，不管是输是赢，这都会是我们的最后一战。阿尔法和贝塔，你们也是一样。”赛恩思说')
        output('“我们尽全力。”')
        savepoint = 25
    #做个存档点标记
    if savepoint == 25:
        save_data()
        print('【战斗开始】对战 赛恩思 x 阿尔法（Final） x 贝塔（Final）')
        hucker = 0
        boom_snake = 0
        s_att = 10
        item_att = 0
        zero_H = ''
        zero_W = ''
        if S_up == 1:
            zero_H = 0
            zero_H = int(zero_H)
            zero_W = '护盾血量'
        big_fight = 0
        t.sleep(0.5)
        H_icecream = 0
        car_A,car_B,car_C = 852,649,2817
        alpha_boom = random.randint(3,5)
        alpha_random = random.randint(4,6)
        alpha_random_B = 0
        beta_stick = 3
        beta_stick_att = 0
        beta_stick_cheat = 0
        beta_break = 5
        AB = 4
        core = 100
        core_weapon = 4
        core_fix = random.randint(3,5)
        core_ball = random.randint(2,3)
        core_boom = 0
        check = 0
        magic_point = 0
        miaomiao = 0
        coat = 0
        win = 0
        a,b,c,d,e = '','','','',''
        while win == 0:
            zero_att = 0
            magic_choose = 0
            att_choose = 0
            item_choose = 0
            while magic_choose == 0 and item_choose == 0:
                magic_core = 0
                if boom_snake > 0:
                    boom_snake -= 1
                    car_A -= 20
                    car_B -= 20
                    input('两只小电子蛇对敌人造成了20点伤害！')
                if car_A <= 0:
                    car_A = 0
                if car_B <= 0:
                    car_B = 0
                chooseb = 'A'
                if '战争宝石' in item:
                    print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health}{zero_W}{zero_H},阿尔法(final)血量为{car_A},攻击力为30，贝塔(final)血量为{car_B},攻击为27，塞恩思血量为{car_C}攻击为{s_att}暴击数{big_fight}')
                if '战争宝石' not in item:
                    print(f'现在请您选择您的行动,您的魔法值为{magic_point},血量为{health}{zero_W}{zero_H},阿尔法（Final）血量为{car_A},贝塔(final)血量为{car_B}，塞恩思血量为{car_C}')
                if core_boom == 0:
                    choose = input('A,物品B,防御C,魔法D,跳过')
                    while choose not in {'A','B','C','D'}:
                        print('请做出你的选择')
                        choose = input('A,物品B,防御C,魔法D,跳过')
                    if choose == 'A':
                        choose = input(f'你现在可使用的物品有{fight_item},请从1开始输入序号以选择使用的物品')
                        if choose not in {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'}:
                            choose = input('物品序号输入错误!')
                        else:
                            choose = int(choose)
                            if choose > len(fight_item):
                                choose = input('物品序号输入错误!')
                            else:
                                check = fight_item[choose]
                                item_find()
                                if check == '魔法炸药':
                                    input('你对对方造成了100点伤害!但你也不小心受到了30点伤害')
                                    health -= 30
                                    car_A -= 100
                                    car_B -= 100
                                    car_C -= 100
                                    dead_interface()
                                    if respawned == 1:
                                        break
                                if check == '坚硬冰棍':
                                    choose = input('请选择投掷的对象（填A或B或C）')
                                    while choose not in {'A','B','C'}:
                                        choose = input('请选择投掷的对象（填A或B或C）')
                                    if choose == 'A':
                                        choose = input('你使用了坚硬冰棍!阿尔法(final)的HP降低了100点!')
                                        car_A -= 100
                                    elif choose == 'B':
                                        choose = input('你使用了坚硬冰棍!贝塔(final)的HP降低了100点!')
                                        car_B -= 100
                                    elif choose == 'C':
                                        choose = input('你使用了坚硬冰棍!塞恩思的HP降低了100点!')
                                        car_C -= 100
                                if check == '像素板':
                                    choose = input('你使用了像素板!敌人受到了70点伤害！')
                                    car_A -= 70
                                    car_B -= 70
                                    car_C -= 70
                                item_choose = 1
                                if health > 300:
                                    health = 300
                    if choose == 'B':
                        choose = input('你选择了防御!')
                        magic_point += 40
                        magic_choose = 1
                        if magic_point >= 100:
                            magic_point = 100
                        chooseb = 'B'
                    if choose == 'C':
                        bit_magic('normal')
                    elif choose == 'D':
                        choose = input('你跳过了你的回合')
                    magic_choose = 1
                else:
                    core_boom = 0
                    chooceb = 'B'
                    magic_point += 40
                    if magic_point > 100:
                        magic_point = 100
            if '混乱护盾' in armor:
                health += random.randint(3,20)
                if health >= 300:
                    health = 300
            if H_icecream > 0:
                H_icecream -= 1
                health -= 20
            if car_A > 0 or car_B > 0:
                car_act_B = random.randint(1,7)
                if car_act_B == 1:
                    input('阿尔法和贝塔以你意想不到的形态向你袭来！')
                if car_act_B == 2:
                    input('室内狂风大作')
                if car_act_B == 3:
                    input('So和昵称盯着阿尔法和贝塔')
                if car_act_B == 4:
                    input('机器人的视线始终没有离开你')
                if car_act_B == 5:
                    input('赛恩思正在稳定战局')
                if car_act_B == 6:
                    input('机器人似乎在战斗中占上风')
                if car_act_B == 7:
                    input('能量核心发着诡异的光芒')
            elif car_B <= 0 and car_A <= 0:
                car_act_B = random.randint(8,12)
                if car_act_B == 8:
                    input('能量核心狂啸着发出警报')
                if car_act_B == 9:
                    input('许多晶体在赛恩思周围出现')
                if car_act_B == 10:
                    input('战争持续着白热化')
                if car_act_B == 11:
                    input('赛恩思正在竭尽全力抵抗！')
                if car_act_B == 12:
                    input('战局看起来很快就会结束')
            AB -= 1
            if car_A > 0:
                chance = 0
                alpha_random -= 1
                if alpha_random == 0:
                    alpha_random_B = random.randint(2,3)
                if alpha_random_B <= 0:
                    x = random.randint(1,4)
                    a = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    b = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    c = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    d = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    e = chr(ord('A') + x - 1)
                    if miaomiao == 4:
                        b,c,d,e = a,a,a,a
                    enemy_fight = a+b+c+d+e
                    enemy_fighta = [a,b,c,d,e]
                    zero_att = 0
                    if '零剑' in weapon:
                        zero_att = random.randint(5,50)
                    if '零剑-II' in weapon:
                        zero_att = random.randint(30,70)
                    if 'Complex机甲长剑' in weapon and random.randint(1,10) == 3:
                        zero_att = 10
                    choose = list(input(f'请选择你对阿尔法的攻击!(5个一组,由五个大写字母构成)'))
                    hurt = 0
                    hurtB = 0
                    chance_B = 5
                    wrong = 0
                    while wrong == 0:
                        wrong = 1
                        if len(choose) != 5:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!'))
                        elif choose[0] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!'))
                        elif choose[1] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!'))
                        elif choose[2] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!'))
                        elif choose[3] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!'))
                        elif choose[4] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!'))
                else:
                    alpha_random_B -= 1
                    if alpha_random == 0:
                        alpha_random = random.randint(4,6)
                        input('阿尔法召唤出了一把‘霍拉克斯巧芙力洛马桑梅朵’！')
                    chance_B = random.randint(3,7)
                    i = 0
                    enemy_fight = ''
                    enemy_fighta = []
                    while i < chance_B:
                        i += 1
                        x = random.randint(1,4)
                        a = chr(ord('A') + x - 1)
                        enemy_fight += a
                        enemy_fighta.append(a)
                        if miaomiao == 4:
                            enemy_fight[i] = enemy_fight[0]
                            enemy_fighta[i] = enemy_fighta[0]
                    zero_att = 0
                    if '零剑' in weapon:
                        zero_att = random.randint(5,50)
                    if '零剑-II' in weapon:
                        zero_att = random.randint(30,70)
                    if 'Complex机甲长剑' in weapon and random.randint(1,10) == 3:
                        zero_att = 10
                    choose = list(input(f'请选择你对阿尔法的攻击!({chance_B}个一组)'))
                    hurt = 0
                    hurtB = 0
                    wrong = 0
                    while wrong == 0:
                        wrong = 1
                        if len(choose) != chance_B:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!'))
                        else:
                            count = 0
                            while count < chance_B:
                                if choose[count] not in {'A','B','C','D'}:
                                    wrong = 0
                                    print('输入错误,请依照格式输入!')
                                    choose = list(input(f'请选择你的攻击!'))
                                count += 1
                cube_act = random.randint(1,5)
                chance = 0
                while chance < chance_B:
                    f = choose.pop()
                    g = enemy_fighta.pop()
                    if (f == 'A' and g == 'B') or (f == 'B' and g == 'C') or (f == 'C' and g == 'D') or (f == 'D' and g == 'A'):
                        hurt += att
                        chance += 1
                        if att_choose == 1:
                            hurt += 5
                        if cube_act > 3:
                            hurt -= 10
                            laser(10)
                        else:
                            laser(0)
                        if '虚空之刃' in weapon and random.randint(1,5) == 2:
                            hurt += int(car_A/5)
                        hurt += item_att
                        hurt += zero_att
                        if miaomiao == 3:
                            hurt += random.randint(10,50)
                        if hucker == 1:
                            hurt += 10
                            
                    elif (f == 'D' and g == 'C') or (f == 'C' and g == 'B') or (f == 'B' and g == 'A') or (f == 'A' and g == 'D'):
                        hurtB += 30
                        if chooseb == 'B':
                            hurtB -= Def
                            if hucker == 1:
                                hurtB -= 30
                            if hurtB < 0:
                                hurtB = 0
                        chance += 1
                        if coat == 1:
                            if  random.randint(1,10) == 5:
                                hurtB = 0
                            else:
                                health += 10
                    else:
                        chance += 1
                if chooseb == 'B':
                    hurt = 0
                if random.randint(1,20) == 3 and '战争宝石' in item and att_choose == 1:
                    hurt *= 3
                if miaomiao == 1:
                    hurtB //= 2
                if miaomiao == 2:
                    hurtB //=5
                hurtB = int(hurtB)
                if hide[0] + hide[1] >= random.randint(1,100):
                    hurtB = 0
                if S_up == 1:
                    if zero_H > 0:
                        zero_H -= hurtB
                    else:
                        health -= hurtB
                else:
                    health -= hurtB
                choose = input(f'阿尔法的攻击是{enemy_fight}')
                if cube_act > 3 :
                    choose = input('阿尔法使用了防御!')
                if chooseb != 'B':
                    choose = input(f'你对阿尔法造成了{hurt}点伤害!')
                    car_A -= hurt
                    hurt = 0
                if chooseb == 'B':
                    choose = input('因为你选择了防御,所以伤害不计入')
               
                choose = input(f'你被敌人扣除了{hurtB}点血')
                alpha_boom -= 1
                dead_interface()
                if respawned == 1:
                    break
                if alpha_boom == 0:
                    alpha_boom = random.randint(3,5)
                    x = random.randint(1,4)
                    a = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    b = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    c = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    d = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    e = chr(ord('A') + x - 1)
                    enemy_fight = a+b+c+d+e
                    enemy_fighta = [a,b,c,d,e]
                    input('阿尔法召唤出了一枚“克制炸弹”！')
                    choose = list(input('请输入五个大写字母，克制数大于等于两个拆除'))
                    chance = 0
                    count = 0
                    wrong = 0
                    while wrong == 0:
                        wrong = 1
                        if len(choose) != 5:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[0] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[1] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[2] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[3] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[4] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    cube_act = random.randint(1,5)
                    while chance < 5:
                        f = choose.pop()
                        g = enemy_fighta.pop()
                        if (f == 'A' and g == 'B') or (f == 'B' and g == 'C') or (f == 'C' and g == 'D') or (f == 'D' and g == 'A'):
                            count += 1
                        chance += 1
                    input(f'炸弹的结构是{enemy_fight}')
                    if count >= 2:
                        input('炸弹被你们拆除了。')
                    else:
                        input('炸弹爆炸了！你受到了70点伤害')
                        if S_up == 1:
                            if zero_H > 0:
                                zero_H -= 70
                            else:
                                health -= 70
                        else:
                            health -= 70
                        dead_interface()
                        if respawned == 1:
                            break
            if car_B > 0:
                beta_att = 0
                beta_hurt = 0
                beta_break -= 1
                beta_break_hurt = 0
                beta_attack = 1
                beta_fight = ''
                z = random.randint(1,2)
                beta_stick_att = 0
                beta_wrong = 0
                beta_stick -= 1
                if beta_break == 0:
                    beta_attack = 2
                    input('贝塔使用了一发碎片！本回合你需要攻击两次')
                if beta_stick == 0:
                    beta_stick = 3
                    input('贝塔召唤出了一根调试棒！')
                    x = random.randint(1,4)
                    a = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    b = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    c = chr(ord('A') + x - 1)
                    d = [a,b,c]
                    choose = input(f'请依次回复{a} {b} {c}的被克制(不需要空格)')
                    chance = 0
                    if len(choose) == 3:
                        while chance < 3 and beta_wrong == 0:
                            beta_wrong = 1
                            if (choose[chance] == 'D' and d[chance] == 'C') or (choose[chance] == 'C' and d[chance] == 'B') or (choose[chance] == 'B' and d[chance] == 'A') or (choose[chance] == 'A' and d[chance] == 'D'):
                                beta_wrong = 0
                            chance += 1
                    else:
                        beta_wrong = 0
                    if beta_wrong == 1:
                        input('你没有输入指定内容，贝塔的攻击力本回合上升了10点！')
                    else:
                        beta_stick_att = input('请输入本回合你想设置的ATT，仅限1-50之间')
                        while beta_stick_att == '':
                            beta_stick_att = input('请输入本回合你想设置的ATT，仅限1-50之间')
                        beta_stick_att = int(beta_stick_att)
                        if 1 <= beta_stick_att and beta_stick_att <= 50:
                            ghost_att = beta_stick_att
                            if z == 1:
                                input(f'恭喜你在本回合战斗中获得了[{beta_stick_att}]ATT！')
                            elif z == 2:
                                input(f'恭喜你在本回合战斗中施舍了贝塔[{beta_stick_att}]ATT!')
                        else:
                            input('你输的什么玩意儿，想挨揍吗？[HP-50]')
                            health -= 50
                            dead_interface()
                            if respawned == 1:
                                break
                while beta_attack > 0:
                    beta_attack -= 1
                    x = random.randint(1,4)
                    a = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    b = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    c = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    d = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    e = chr(ord('A') + x - 1)
                    if miaomiao == 4:
                        b,c,d,e = a
                    enemy_fight = a+b+c+d+e
                    enemy_fighta = [a,b,c,d,e]
                    zero_att = 0
                    if '零剑' in weapon:
                        zero_att = random.randint(5,50)
                    if '零剑-II' in weapon:
                        zero_att = random.randint(30,70)
                    if 'Complex机甲长剑' in weapon and random.randint(1,10) == 3:
                        zero_att = 10
                    choose = list(input(f'请选择你对贝塔的攻击!(5个一组,由五个大写字母构成)'))
                    hurt = 0
                    hurtB = 0
                    chance = 0
                    wrong = 0
                    while wrong == 0:
                        wrong = 1
                        if len(choose) != 5:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[0] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[1] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[2] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[3] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                        elif choose[4] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    cube_act = random.randint(1,100)
                    while chance < 5:
                        f = choose.pop()
                        g = enemy_fighta.pop()
                        if (f == 'A' and g == 'B') or (f == 'B' and g == 'C') or (f == 'C' and g == 'D') or (f == 'D' and g == 'A'):
                            hurt += att
                            chance += 1
                            if att_choose == 1:
                                hurt += 5
                            if cube_act <= 27:
                                hurt -= 22
                                laser(27)
                            else:
                                laser(0)
                            if '虚空之刃' in weapon and random.randint(1,5) == 2:
                                hurt += int(car_B/5)
                            hurt += item_att
                            hurt += zero_att
                            if beta_stick_att != 0:
                                if z == 1:
                                    hurt += beta_stick_att
                            if hucker == 1:
                                hurt += 10
                            if miaomiao == 3:
                                hurt += random.randint(10,50)
                            
                        if (f == 'D' and g == 'C') or (f == 'C' and g == 'B') or (f == 'B' and g == 'A') or (f == 'A' and g == 'D'):
                            hurtB += 27
                            if beta_stick_att != 0:
                                if z == 2:
                                    hurtB += beta_stick_att
                            if chooseb == 'B':
                                hurtB -= Def
                                if hucker == 1:
                                    hurtB -= 30
                                if hurtB < 0:
                                    hurtB = 0
                            chance += 1
                            if coat == 1:
                                if  random.randint(1,10) == 5:
                                    hurtB = 0
                                else:
                                    health += 10
                        else:
                            chance += 1
                    if miaomiao == 1:
                        hurtB /= 2
                    if miaomiao == 2:
                        hurtB /=5
                    hurtB = int(hurtB)
                    if hide[0] + hide[1] >= random.randint(1,100):
                        hurtB = 0
                    if hurtB - hurt > beta_break_hurt:
                        beta_att = hurtB
                        beta_hurt = hurt
                        beta_fight = enemy_fight
                    choose = input(f'贝塔的攻击是{enemy_fight}')
                    if S_up == 1:
                        if zero_H > 0:
                            zero_H -= beta_att
                        else:
                            health -= beta_att
                    else:
                        health -= hurtB
                    if random.randint(1,20) == 3 and '战争宝石' in item and att_choose == 1:
                        hurt *= 3
                    if cube_act <= 27 :
                        choose = input('贝塔使用了防御!')
                    if chooseb != 'B':
                        if beta_break != 0:
                            choose = input(f'你对贝塔造成了{hurt}点伤害!')
                            car_B -= hurt
                        else:
                            choose = input(f'你对贝塔造成了{beta_hurt}点伤害!')
                            car_B -= beta_hurt
                    hurt = 0
                    if chooseb == 'B':
                        choose = input('因为你选择了防御,所以伤害不计入')
                    choose = input(f'你被贝塔扣除了{hurtB}点血')
                    dead_interface()
                    hurtB = 0
                    beta_stick_att = 0
                    if respawned == 1:
                        break
                if beta_break == 0:
                    beta_break = 5
            if car_B > 0 and car_A > 0 and AB == 0:
                AB = 4
                input('阿尔法和贝塔一起使用了一发蜘蛛连结拳！')
                x = random.randint(1,4)
                a = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                b = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                c = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                d = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                e = chr(ord('A') + x - 1)
                if miaomiao == 4:
                    b,c,d,e = a
                enemy_fight = a+b+c+d+e
                enemy_fighta = [a,b,c,d,e]
                zero_att = 0
                if '零剑' in weapon:
                    zero_att = random.randint(5,50)
                if '零剑-II' in weapon:
                    zero_att = random.randint(30,70)
                if 'Complex机甲长剑' in weapon and random.randint(1,10) == 3:
                    zero_att = 10
                choose = list(input(f'请选择你对阿尔法(Final)和贝塔(Final)的攻击!(5个一组,由五个大写字母构成)'))
                hurt = 0
                hurtB = 0
                chance = 0
                wrong = 0
                while wrong == 0:
                    wrong = 1
                    if len(choose) != 5:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[0] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[1] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[2] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[3] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[4] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                else:
                    if car_A > 0 or car_B > 0:
                        cube_act = 101
                    while chance < 5:
                        f = choose.pop()
                        g = enemy_fighta.pop()
                        if chooseb != 'B':
                            if (f == 'A' and g == 'B') or (f == 'B' and g == 'C') or (f == 'C' and g == 'D') or (f == 'D' and g == 'A'):
                                hurt += att
                                chance += 1
                                if att_choose == 1:
                                    hurt += 5
                                if '虚空之刃' in weapon and random.randint(1,5) == 2:
                                    hurt += int((car_A+car_B)/5)
                                hurt += item_att
                                hurt += zero_att
                                if hucker == 1:
                                    hurt += 10
                                if miaomiao == 3:
                                    hurt += random.randint(10,50)
                                
                        if (f == 'D' and g == 'C') or (f == 'C' and g == 'B') or (f == 'B' and g == 'A') or (f == 'A' and g == 'D'):
                            hurtB += 20
                            if random.randint(1,5) == 2:
                                hurtB += 10
                            if chooseb == 'B':
                                hurtB -= Def
                                if hucker == 1:
                                    hurtB -= 30
                                if hurtB < 0:
                                    hurtB = 0
                            chance += 1
                            if coat == 1:
                                if  random.randint(1,10) == 5:
                                    hurtB = 0
                                else:
                                    health += 10
                        else:
                            chance += 1
                    if miaomiao == 1:
                        hurtB /= 2
                    if miaomiao == 2:
                        hurtB /=5
                    hurtB = int(hurtB)
                    if hide[0] + hide[1] >= random.randint(1,100):
                        hurtB = 0
                    if S_up == 1:
                        if zero_H > 0:
                            zero_H -= hurtB
                        else:
                            health -= hurtB
                    else:
                        health -= hurtB
                    if random.randint(1,20) == 3 and '战争宝石' in item and att_choose == 1:
                        hurt *= 3
                    choose = input(f'阿尔法(Final)和贝塔(Final)的攻击是{enemy_fight}')
                    if chooseb == 'B':
                        choose = input('因为你选择了防御,所以伤害不计入')
                    else:
                        choose = input(f'你对阿尔法(Final)和贝塔(Final)造成了{hurt}点伤害!')
                        car_A -= int(hurt/2)
                        car_B -= int(hurt/2)
                        hurt = 0
                    choose = input(f'你被阿尔法(Final)和贝塔(Final)扣除了{hurtB}点血')
                    dead_interface()
                    hurtB = 0
                    if respawned == 1:
                        break
            if car_A <= 0 and car_B <= 0 and s_att == 10:
                s_att = 40
                input('“看来，这将会是最后的战斗……”')
            if car_C > 0:
                if s_att == 40:
                    core_fix -= 1
                    core_ball -= 1
                    core_weapon -= 1
                    if core_ball == 0 and core_weapon == 0:
                        core_weapon += 1
                if core_ball == 0:
                    core_ball = random.randint(2,3)
                    x = random.randint(1,4)
                    a = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    b = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    c = chr(ord('A') + x - 1)
                    enemy_fight = a+b+c
                    enemy_fighta = [a,b,c]
                    input('终级核心开始向外界放射能量球！')
                    choose = list(input('回复3个字母接住终级核心的能量球'))
                    wrong = 0
                    chance = 0
                    count = 0
                    while wrong == 0:
                        wrong = 1
                        if len(choose) != 3:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的行动!(3个一组,由3个大写字母构成)'))
                        elif choose[0] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的行动!(3个一组,由3个大写字母构成)'))
                        elif choose[1] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的行动!(3个一组,由3个大写字母构成)'))
                        elif choose[2] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的行动!(3个一组,由3个大写字母构成)'))
                    while chance < 3:
                        f = choose.pop()
                        g = enemy_fighta.pop()
                        if (f == 'A' and g == 'B') or (f == 'B' and g == 'C') or (f == 'C' and g == 'D') or (f == 'D' and g == 'A'):
                            chance += 1
                            count += 1
                        else:
                            chance += 1
                    if count <= 1:
                        hp_m = random.randint(10,15)
                        input(f'你接住了红能量球，你的HP降低了{hp_m}点！，你的魔法值提升了10点！')
                        health -= hp_m
                        magic_point += 10
                        if magic_point > 100:
                            magic_point = 100
                    if count == 2:
                        input('你接住了蓝能量球，什么事情都没有发生')
                    if count == 3:
                        input('你接住了紫能量球，你的HP恢复了50点！你的魔法值提升了5点，能量冗余度降低了5点！')
                        health += 50
                        if health > 300:
                            health = 300
                        magic_point += 5
                        if magic_point > 100:
                            magic_point = 100
                        core -= 5
                x = random.randint(1,4)
                a = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                b = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                c = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                d = chr(ord('A') + x - 1)
                x = random.randint(1,4)
                e = chr(ord('A') + x - 1)
                if miaomiao == 4:
                    b,c,d,e = a
                enemy_fight = a+b+c+d+e
                enemy_fighta = [a,b,c,d,e]
                zero_att = 0
                if '零剑' in weapon:
                    zero_att = random.randint(5,50)
                if '零剑-II' in weapon:
                    zero_att = random.randint(30,70)
                if 'Complex机甲长剑' in weapon and random.randint(1,10) == 3:
                    zero_att = 10
                choose = list(input(f'请选择你对塞恩思的攻击!(5个一组,由五个大写字母构成)'))
                hurt = 0
                hurtB = 0
                chance = 0
                wrong = 0
                while wrong == 0:
                    wrong = 1
                    if len(choose) != 5:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[0] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[1] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[2] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[3] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                    elif choose[4] not in {'A','B','C','D'}:
                        wrong = 0
                        print('输入错误,请依照格式输入!')
                        choose = list(input(f'请选择你的攻击!(5个一组,由五个大写字母构成)'))
                else:
                    cube_act = random.randint(1,100)
                    if car_A > 0 or car_B > 0:
                        cube_act = 101
                    while chance < 5:
                        f = choose.pop()
                        g = enemy_fighta.pop()
                        if chooseb != 'B':
                            if (f == 'A' and g == 'B') or (f == 'B' and g == 'C') or (f == 'C' and g == 'D') or (f == 'D' and g == 'A'):
                                hurt += att
                                chance += 1
                                if att_choose == 1:
                                    hurt += 5
                                if cube_act <= 27:
                                    hurt -= 27
                                    laser(27)
                                else:
                                    laser(0)
                                if '虚空之刃' in weapon and random.randint(1,5) == 2:
                                    hurt += int(car_C/5)
                                hurt += item_att
                                hurt += zero_att
                                if hucker == 1:
                                    hurt += 10
                                if miaomiao == 3:
                                    hurt += random.randint(10,50)
                                
                        if (f == 'D' and g == 'C') or (f == 'C' and g == 'B') or (f == 'B' and g == 'A') or (f == 'A' and g == 'D'):
                            hurtB += s_att
                            if chooseb == 'B':
                                hurtB -= Def
                                if hucker == 1:
                                    hurtB -= 30
                                if hurtB < 0:
                                    hurtB = 0
                            chance += 1
                            if coat == 1:
                                if  random.randint(1,10) == 5:
                                    hurtB = 0
                                else:
                                    health += 10
                        else:
                            chance += 1
                    if miaomiao == 1:
                        hurtB /= 2
                    if miaomiao == 2:
                        hurtB /=5
                    hurtB = int(hurtB)
                    if hide[0] + hide[1] >= random.randint(1,100):
                        hurtB = 0
                    if S_up == 1:
                        if zero_H > 0:
                            zero_H -= hurtB
                        else:
                            health -= hurtB
                    else:
                        health -= hurtB
                    if random.randint(1,20) == 3 and '战争宝石' in item and att_choose == 1:
                        hurt *= 3
                    if chooseb != 'B':
                        if s_att == 40:
                            core -= 3
                            if att_choose == 1:
                                core -= 3
                            if magic_core == 1:
                                core += 1
                    if car_A <= 0 and car_B <= 0:
                        input(f'终级核心正在闪耀着光芒。终级核心的能量冗余度为{core}')
                    choose = input(f'塞恩思的攻击是{enemy_fight}')
                    if chooseb == 'B':
                        choose = input('因为你选择了防御,所以伤害不计入')
                    else:
                        if car_A == 0 and car_B == 0:
                            if cube_act <= 27 :
                                choose = input('塞恩思使用了防御!')
                            if chooseb != 'B':
                                choose = input(f'你对塞恩思造成了{hurt}点伤害!')
                                car_C -= hurt
                                hurt = 0
                                if car_C <= 0:
                                    car_C += 500
                                    input('终级核心的光照耀着赛恩思！')
                                    input('赛恩思血量回复了500点，终级核心的冗余度下降了10点！')
                                    core -= 10
                        else:
                            input('你无法穿透塞恩思的防御！')
                    choose = input(f'你被塞恩思扣除了{hurtB}点血')
                    if core_fix == 0:
                        core_fix = random.randint(3,5)
                        core += 2
                        input('赛恩思操控着终级核心，终级核心的能量冗余度回复了2点！')
                    hurtB = 0
                    dead_interface()
                    if respawned == 1:
                        break
                if s_att == 40 and core_weapon == 0:
                    core_weapon = 4
                    core -= 4
                    input('终级核心消耗了4点冗余度，正在用高射炮向你轰击过来！')
                    choose = list(input('请回复5个字母以躲避'))
                    count = 0
                    x = random.randint(1,4)
                    a = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    b = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    c = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    d = chr(ord('A') + x - 1)
                    x = random.randint(1,4)
                    e = chr(ord('A') + x - 1)
                    enemy_fight = a+b+c+d+e
                    enemy_fighta = [a,b,c,d,e]
                    hurt = 0
                    hurtB = 0
                    chance = 0
                    wrong = 0
                    while wrong == 0:
                        wrong = 1
                        if len(choose) != 5:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的行动!(5个一组,由五个大写字母构成)'))
                        elif choose[0] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的行动!(5个一组,由五个大写字母构成)'))
                        elif choose[1] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的行动!(5个一组,由五个大写字母构成)'))
                        elif choose[2] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的行动!(5个一组,由五个大写字母构成)'))
                        elif choose[3] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的行动!(5个一组,由五个大写字母构成)'))
                        elif choose[4] not in {'A','B','C','D'}:
                            wrong = 0
                            print('输入错误,请依照格式输入!')
                            choose = list(input(f'请选择你的行动!(5个一组,由五个大写字母构成)'))
                    else:
                        while chance < 5:
                        #快悄悄这个地方,我把chance < 5写成了chance <= 5然后查了一天才查到这个bug
                        #悄悄改为瞧瞧,这是个错别字(划)通假字
                        #快看,这里我复制的前面
                            #快看，我还是复制的前面（
                            f = choose.pop()
                            g = enemy_fighta.pop()
                            if f == 'D' and g == 'C' or f == 'C' and g == 'B' or f == 'B' and g == 'A' or f == 'A' and g == 'D':
                                chance += 1
                            else:
                                chance += 1
                                count += 1
                        choose = input(f'高射炮的进攻方式是{enemy_fight}')
                        if count > 3:
                            input('你躲开了高射炮的进攻！')
                            go = 1
                        else:
                            input('进入高射炮击中了，你的HP降低了14点！你下一回合不能动了！')
                            health -= 14
                            core_boom = 1
                            dead_interface()
                            if respawned == 1:
                                break
            att_choose = 0
            item_att = 0
            if S_up == 1:
                if zero_H < 0:
                    zero_H = 0
            hide[1] = 0
            coat = 0
            miaomiao = 0
            if core <= 0:
                choose = input('能量核心的光黯淡下来')
                input('你胜利了！')
                win = 1

        if respawned == 1:
            respawned = 0
            continue
        savepoint = 26
    #做个存档点标记
    if savepoint == 26:
        save_data()
        output('“终于……”')
        output('看着一片狼籍的战场和两个早已停摆的机器人，赛恩思无力地说。')
        output('“你们……还是在我之上啊……”')
        output('赛恩思倒在了地上。')
        output('就在这时候，你看见后面冲上许多机器人，都是你在车上看到的，他们都围在赛恩思身边，似乎有点不知所措。')
        output('小天从后面向你们走来：“谢谢你们打败了赛恩思……我们……都可以回家了。”')
        output('“比去超市进货更令人振奋！”Tetris高兴地说道。')
        output('“嗯……是这样的，我们怎么处置赛恩思呢……”昵称说道。')
        output('“这个嘛……”称为H的显示屏在你们身边亮起，“我们需要断绝赛恩思与SEED的关系，因为罗尔斯早已失联，这样操作起来……”')
        output('“等等，你说罗尔斯失联了？！”倒在地上的赛恩思突然坐起了身，把你们吓了一跳。')
        output('“赛恩思？你居然活着……”H有点为难。“不过，我认为你不能再为SEED工作了。”')
        output('“是……他们不会饶过我……”赛恩思低下头。')
        output('“不过，你为什么一定要为SEED工作呢？”H说，这使赛恩思来了精神。')
        output('“什么？！”')
        output('“SEED的目的，是入侵世界中心的魔法温泉，最后打破秩序，创造只属于他们自己的世界，实际上，是一个独裁的空壳世界。')
        output('你不觉得现在的世界更有意思一点吗？”')
        output('“这……可是我不知道离开SEED，我怎么过。”')
        output('“SEED不是一切，生活的方式非常多，你研究社会学，肯定非常清楚才对，我们去外面聊聊吧。”')
        output('H飞向房间外，赛恩思也跟着它一起走了过去，突然赛恩思向你们回过头来，无力地笑了笑：')
        output('“So、昵称、Zero，谢谢你们……”')
        output('你们似乎有点摸不着头脑，这是小天的一番话把你们打醒了：“嘿！等等！这核心都没能量了，怎么送我们回家呀！”')
        output('So说道：“似乎……本来就不是靠能量核心回家来着……”')
        output('小天愣了愣：“也对……我这就去叫车！再见了、So！再见了！')
        output('Zero！祝你们一路顺风！”')
        output('“还有我呐！”昵称嚷道，不过小天已经跑远了。')
        output('“时间不早了，我们也该离开了。”So说道，“前面是一个通向地下室的电梯，地下室里面有我们需要的渗透机器。”')
        output('你会：A：向前走去,B：与剩下的人聊天,C：看看终级核心,D：去找赛恩思和H')
        go = 0
        while go == 0:
            while choose not in {'A','B','C','D'}:
                output('你会：A：向前走去,B：与剩下的人聊天,C：看看终级核心,D：去找赛恩思和H')
            if choose == 'A':
                go = 1
            elif choose == 'B':
                output('Tetris说：“拜托了……我一直在逛超市呢，结果这车就跑过来了，不过摆脱赛恩思的感觉真好……”')
            elif choose == 'C':
                output('终级核心暗淡无光')
            elif choose == 'D':
                output('你们在露天平台上找到了赛恩思和H')
                output('赛恩思说：“呃……Zero，你跑过来关心我……”')
                output('H替赛恩思说话了：“我给赛恩思推荐了一个社会学作家协会，马上赛恩思就可以完成第一个作品……万事开头难嘛，也许拍电影也挺不错的～”')
                output('你回到房间')
        output('你们向前走去，在终级核心的背面出现了一个黑暗的电梯门。')
        output('你们向前走去，在终级核心的背面出现了一个黑暗的电梯门。')
        output('你们走出电梯。黑暗中一个巨大的，发着蓝光的机器横在你们前方')
        output('你们站在机器前，看着机器的蓝色由柔和转变为凶恶。')
        output('突然间，刺眼的白光再次在你眼前爆发，你失去了知觉。')
        output('你再次睁开眼睛时，你发现你依旧躺在自己的房间。')
        output('你会：A：出门,B：看书')
        while choose not in {'A','B'}:
            output('你会：A：出门,B：看书')
        if choose == 'B':
            output('书架上摆着一本《脑科学研究概论》和一本《社会学》')
        output('你会读哪本？A：《脑科学研究概论》,B：《社会学》')
        while choose not in {'A','B'}:
            output('你会读哪本？A：《脑科学研究概论》,B：《社会学》')
        if choose == 'A':
            output('你翻了几页，书上写道：')
            output('“但，从目前看来，我们还无法获得大脑的量子解析图，只能通过现成的量子计算机将每个人的大脑连结起来，构成所谓的灵魂网络。我们并不知道这样做的潜在隐患，只能希望它不会出什么差错。但纯粹的希望是科学研究所不容许的。”')
        elif choose == 'B':
            output('你翻了几页，书上写道：')
            output('“从更广大群众的角度来说，一项新技术的出现必将带来更加广泛的排斥与挑战。人类好比电感器，总是具有一种维持自身原来状态的惯性。    某些魔法作品中一些人获得超能力，与各种怪兽作战，称霸世界，但假使超能力者真正出现，也只不过会成为科学研究的实验品罢了。”')
        output('你走出房间，夜晚的大厅人非常少。')
        output('这时，你突然发现代数向你走来。他一见到你便说：“我的天！Zero，你去哪了？怎么这么晚才回来？！Sword-10找到了吗？”')
        output('你会回答：A：根本找不到,B：找到了，但也找到了传送机器')
        while choose not in {'A','B'}:
            output('你会回答：A：根本找不到,B：找到了，但也找到了传送机器')
        if choose == 'A':
            output('代数说：“嗯……其实So和昵称已经把事情告诉我了……医务室里的传送机器……我们现在就会派人去那。”')
        elif choose == 'B':
            output('代数说：“哦……传送机器啊，我会派一波人过去的，当然我们在别的地方拿到了Sword-10，点线目前不需要担心辐射病了。”')
        output('你正准备走，代数突然叫住了你')
        output('“嘿，Zero……那啥……我想……你今晚不需要回自己的房间……我想带你去见一下……去见一下……星空的……算了，你今晚在玑沐房里过夜好吗？”')
        output('代数没等你同意，就抓住你的手把你带到一座屋子前面：“这是玑沐的房间，她的房间离星空很近，有什么事情可以很快解决掉。晚安……”')
        output('你走进房间，房间出乎意料地大。你看到一个女孩坐在柔软的大床上，拿着一个笔记本不知道在写什么东西。')
        output('女孩看到了你，站起来大声说：“诶！Zero！说三遍！晚上十点睡觉！晚上十点睡觉！晚上十点睡觉！不要熬夜！现在去洗澡啦！Zero！”')
        output('你感到有些无力。')
        output('你来到旁边的浴室整理着你的衣服，因为之前的冒险弄得有些脏，你打算洗一下。')
        output('正当你把衣服在水池里摆好的时候，你的手突然碰到衣服上一个坚硬的东西，你拿起来一看，是个黑色的小摄像头。')

        output('你会：A：扔掉,B：保存,C：检查')
        while choose not in {'A','B','C'}:
            output('你会：A：扔掉,B：保存,C：检查')
        if choose == 'A':
            output('你把摄像头扔掉了')
        elif choose == 'B':
            output('你把摄像头保存了下来')
        elif choose == 'C':
            output('你仔细检查着摄像头，因为在云村里靠近你的人不多，因此应该是在魔法界域安装上去的')
            output('至于具体的时间，你感觉应该是在你被注入记忆碎片的时候,不过，这么做的用意是什么呢？')
            output('你把摄像头保存了下来')
        output('你处理完摄像头后，你缩进浴室前面的一个大大的浴缸里')
        output('漫长的时间过去了，你浑身都泡软了，这才从浴缸里慢慢地爬出来')
        output('玑沐看到你从浴室里出来，大声地说：“好哦！我进去了！你现在给我睡觉吧！”')
        output('你看着玑沐走进浴室，突然感到有些怪异。')
        output('你会：A：直接睡觉,B：来到大门外面看看')
        while choose not in {'A','B'}:
            output('你会：A：直接睡觉,B：来到大门外面看看')
        if choose == 'B':
            output('你来到门口，突然听见外面有些动静，你便躲在门后偷听。')
            output('门外远远地站着两个人，你看清楚了一个是代数，还有一个穿着军装的你不太认识的人。')
            output('“是这样的，SEED的上层还有其它的人。”')
            output('“所以说，我们还需要更多的兵力？还有更多的魔法界域？”')
            output('“情报是这样的……只不过嘛，渗透机器的事情，好像败露了……”')
            output('“怎么可能？这渗透机器是由邦联军工的最新科技打造的，反侦察效果恐怕没有谁可以媲美它了吧！”')
            output('“我只能说一个猜想，有人在给SEED传递情报。”')
            output('“你是说，我们当中出现了叛徒？！”')
            output('“先不要这么说，但确实有这点嫌疑……”')
            output('代数向远处走去，旁边的人也迅速跟上。')
            output('“看管好Zero。”')
            output('这是你听到的最后一句话。')
        output('你在床上躺好，这张床比你想象中更加柔软。')
        output('玑沐很快从浴室出来：“怎么还没睡？睡觉啦Zero……”')
        output('玑沐说完关上了灯。')
        output('你在黑暗中翻了个身，心里却在想着魔法界域里的事情。')
        output('到底，以后会遇到怎么样的冒险，而神秘的SEED，真面目究竟是什么。')
        output('你真的很想知道。')
        output('【第二章完】')
        
