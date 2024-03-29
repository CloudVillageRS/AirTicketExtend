//@ts-check
"use strict";
//import "./types-ate/index.d.ts"







(function ($, data, version) {
    
    function randInt(start, end) {
        return start + Math.floor(Math.random() *(end - start + 1))
    }
    class TableItem {
        
        constructor(name, table, color, full) {
            this.name = name
            this.full = full
            this.$title = $("<td/>")
                .html(name)
                .appendTo(table.$tr)
            this.$valCell = $("<td/>").appendTo(table.$tr)
            this.$val = $("<span/>").appendTo(this.$valCell)
            if (color && full) {
                this.$rate = $("<div/>")
                    .addClass("ate-info-rate")
                    .css("backgroundColor", color)
                    .insertAfter(this.$val)
            }
        }
        
        show() {
            this.$valCell.fadeIn()
            this.$title.fadeIn()
        }
        
        hide() {
            this.$valCell.hide()
            this.$title.hide()
        }
        
        set(val) {
            if (this.val && this.val != val) {
                let delta = val - this.val
                let $rise = $("<span/>").html((delta > 0 ? "+" : "") + delta + "")
                $rise.appendTo(this.$valCell)
                    .addClass("ate-val-rise")
                    .css("color", delta < 0 ? "red" : "green")
                    .animate({
                        opacity: 0,
                        top: "-3em"
                    }, 2000, () => {
                        $rise.remove()
                    })
            }
            this.val = val
            this.$val.html(val + "")
            if (this.full) {
                this.$rate.css("height", val / this.full * 100 + "%")
            }
        }
    }
    class Table {
        
        constructor(cls, head) {
            this.$outer = $("<div/>").addClass(cls)
            var $table = $("<table/>").addClass("ate-info").appendTo(this.$outer)
            var $tbody = $("<tbody/>").appendTo($table)
            this.$tr = $("<tr/>").appendTo($tbody)
            this.$th = $("<th/>").html(head).appendTo(this.$tr)
            
            this.health = null
            
            this.magic = null
            
            this.attack = null
            
            this.defence = null
            
            this.cm = null
            
            this.gunHealth = null
            
            this.chaos = null
            
            this.rules = null
        }
        
        add(key, name, full, color, hidden) {
            var tableItem = new TableItem(name, this, color, full)
            if (hidden) {
                tableItem.hide()
            }
            this[key] = tableItem
            return this
        }
        
        appendTo(ele) {
            this.$outer.appendTo(ele)
            return this
        }
        remove() {
            this.$outer.remove()
            return this
        }
    }
    class Queue {
        
        constructor(game) {
            
            this.arrays = {}
            
            this.cachedIndexes = {}
            
            this.processing = false
            Queue.newid(game)
            this.give(game)
        }
        
        push(fn, cur) {
            if (cur.dead || !(this.arrays[cur.id])) {
                return
            }
            this.arrays[cur.id].push(fn)
            if (! this.processing) {
                this.process()
            }
        }
        
        process() {
            if (this.processing) {
                return;
            }
            var originalOwner = this.owner
        	var queueArray = this.arrays[originalOwner]
            var processingIndex = this.cachedIndexes[originalOwner] || 0
            this.processing = true
        	const process = () => {
                if (this.processing == false) {
                    return
                }
                if (originalOwner !== this.owner) {
                    this.processing = false
                    this.cachedIndexes[originalOwner] = processingIndex
                    return this.process()
                }
        		if (processingIndex >= queueArray.length) {
                    this.arrays[originalOwner] = []
                    this.cachedIndexes[originalOwner] = 0
                    this.processing = false
                    return
                }
                console.log(queueArray[processingIndex], originalOwner)
        		let result = queueArray[processingIndex++].call(undefined)
        		if (result && result.done) {
        			result.done(process)
        		} else {
        			process()
        		}
        	}
        	process()
        }
        
        give(process) {
            
            this.owner = process.id
            if (!(this.arrays[process.id])) {
                this.arrays[process.id] = []
            }
            if (!this.processing) {
                this.process()
            }
        }
        
        static newid(obj) {
            Queue.registeredOwners.push(obj)
            obj.id = Queue.curid
            Queue.curid++
        }
        
        now() {
            return Queue.registeredOwners[this.owner]
        }
    }
    
    Queue.registeredOwners = []
    Queue.curid = 0
    class Process {
        
        constructor(func, game) {
            if (!game) throw new Error("Missing param game")
            this.id = -1
            Queue.newid(this)
            this.func = func
            this.dead = false
            this.game = game
        }
        
        go() {
            this.game.queue.give(this)
            this.func(this)
        }
        
        log(msg) {
            this.wait(() => this.game._log(msg))
        }
        
        wait(fn) {
            this.game.queue.push(fn, this)
        }
        
        choose(choices, callback) {
            this.wait(() => this.game._choose(choices, callback))
        }
        
        die(after) {
            this.dead = true
            if (after) this.game.queue.give(after)
        }
        
        waitDie(after) {
            this.wait(() => this.die(after))
        }
    }
    class Battle {
        
        constructor(battleData, game, after) {
            console.log(this)
            this.id = -1
            Queue.newid(this)
            game.queue.give(this)
            this.game = game
            
            this.tutorial = battleData.tutorial
            
            this.withXk = battleData.withXk
            
            this.octahedron = battleData.octahedron
            
            this.cureMagicCost = this.game.has(14) ? 50 : 30
            
            this.cureMagicPlus = this.game.has(14) ? 80 : 40
            
            this.$element = game.$battle
            
            this.after = after
            this.$element.children().fadeOut() // CRD 战斗中短矛子战隐藏母战斗
            var enemyData = data.enemy[battleData.enemy]
            
            this.won = false
            
            this.afterWin = battleData.win
            this.enemyTable = new Table("ate-enemy-table", enemyData.name).appendTo(this.$element)

            this.enemyTable.add("health", "HP", enemyData.health, "red")
            this.enemyTable.add("gunHealth", "炮筒", 5, "orange", true)
            this.enemyTable.add("chaos", "混沌", 120, "linear-gradient(red, grey)", true)
            this.enemy = new Enemy(enemyData, this)
            
            this.zeroTable = new Table("ate-zero-table", "Zero").appendTo(this.$element)
            this.zeroTable.add("magic", "魔法值", 100, "purple")
            this.game.$interface.addClass("battling")
            
            this.magic = 0
            
            this.rounds = 0
            if (this.enemy.id === 14) {
                this.enemyTable.chaos.show()
                this.chaos = 0
                
                this.chaoAttacked = false
            }
        }
        
        win() {
            if (this.won) {
                return;
            }
            this.won = true
            this.log("您获胜了！")
            if (this.afterWin) {
                for (let command of this.afterWin) {
                    this.game.execute(command)
                }
            }
            
            this.game.$interface.removeClass("battling")
            setTimeout(() => {
                this.enemyTable.remove()
                this.zeroTable.remove()
            }, 2000)
            
            this.$element.children().fadeIn()
            this.wait(() => {
                this.game.queue.give(this.after)
                this.dead = true
            })
        }
        
        log(msg) {
            this.wait(() => this.game._log(msg))
        }
        
        wait(fn) {
            if (typeof fn === "function") {
                this.game.queue.push(fn, this)
            } else {
                this.game.queue.push(() => {
                    var deferred = $.Deferred()
                    setTimeout(() => deferred.resolve(), fn)
                    return deferred
                }, this)
            }
        }
        
        choose(choices, callback) {
            this.wait(() => this.game._choose(choices, callback))
        }
        
        run() {
            if (this.tutorial) {
            	
            	this.roundEndCallback = []
                this.log("星空说：“让我描述详细一点吧，在魔法系统下，战斗就是我们的【魔法核心】相互接触的过程，每个人都有一个【魔法核心】，只不过大多数人都不会用罢了，我来教你怎么使用。")
                this.log("星空跟你详细说明了使用魔法核心的方法，你试了一下，突然你感觉世界一下就改变了！")
                this.log("星空：现在我们进入了战斗界面！当你听完我的这些话后，就可以加入战斗了。战斗分为准备阶段和对战阶段，在准备阶段时，你可以尝试A【物品】、B【防御】、C【魔法】、D【跳过】，不过你现在没有魔法值，没有物品，选择【防御】吧。")
                this.choose(["防御", "跳过"], ch => this.prepare(ch))
            } else {
                this.round()
            }
        }
        
        round() {
            this.log("回合" + (this.rounds + 1))
            
            this.defense = false
            
            this.battleMagic = false
            
            this.heavyAttack = false
            
            this.fightTimes = 1
            
            this.roundEndCallback = []
            if (this.game.armor === 23) { // 混乱护盾
                this.game.execute("health + [3,20]")
            }
            switch (this.enemy.id) {
                case 7: // CRD
                    if (this.rounds === 9) {
                        
                        this.log("CRD：“什么？！你们居然还能挺得住，看来我要动用增援了！”")
                        this.wait(() => {
                            this.log("第一个短矛向你袭来")
                            return this.game.battle(8, this)
                        })
                        this.wait(() => {
                            this.log("第二个短矛向你袭来")
                            return this.game.battle(8, this)
                        })
                    }
                    break;
                case 8: // 长矛
                    if (this.rounds === 6) {
                        this.game.achieve(2)
                    }
                    break;
                case 10: // 鹿法师
                case 11:
                    if (this.rounds % 5 === 4) {
                        this.log("鹿法师使用了火魔法！ATT暂时提升5点")
                        this.enemy.attack += 5
                        this.roundEnd(() => this.enemy.attack -= 5)
                    }
                    break;
                case 13: // 机械木马
                    if (this.enemy.health < 400) {
                        this.log('机械木马的HP降低了！')
                        this.log('机械木马使用了【自我修复】！机械木马的HP回升了70点！')
                        if (this.enemy.fixed == false) {
                            this.log('“呃……这样真的能击败它吗？”水晶说道。')
                            this.log('“Zero就不能用点什么手段吗……”一个骷髅抱怨道。')
                            this.log('“呃……对了！我看到这个木马的炮管，在平常的时候好像都是掩着的，说不定这就是它的弱点！Zero，它等下发动炮弹攻击的时候，你向炮管打去，看看会怎么样！”水晶说。')
                            // @ts-ignore
                            this.enemyTable.gunHealth.show()
                            this.enemy.fixed = true
                        }
                        this.enemy.health += 70
                    }
                    if (this.heavyAttack = this.rounds % 5 === 4) {
                        this.log("机械木马正在准备一发重型火力攻击。")
                        this.enemy.attack += 20
                        this.roundEnd(() => this.enemy.attack -= 20)
                    } else if (this.rounds % 5 === 0 && this.rounds > 0) {
                        this.log("机械木马正在准备一发散弹攻击！")
                        this.fightTimes = 2
                    }
                    break;
                default:
                    break
            }
            if (this.enemy.message) {
                let message = this.enemy.message
                
                if (typeof message[0] !== "string") {
                    message = this.game.judgeArr(message)
                }
                let r = Math.floor(Math.random() * (message.length + 1))
                if (r < message.length) {
                    let messageArray = message[r].split(";")
                    for (let each of messageArray) {
                        if (each.startsWith("/")) {
                            this.game.execute(each.slice(1), this)
                        } else {
                            this.log(each)
                        }
                    }
                }
            }
            this.prepareChoose()
        }
        
        prepareChoose() {
            this.choose(["物品", "防御", "魔法", "跳过"], ch => this.prepare(ch))
        }
        
        prepare(ch) {
            if (this.tutorial) {
                if (ch === 0) {
                    this.defense = true
                    this.log("星空：很好，让我们试一下战斗吧！")
                    this.log("星空：现在是进入【战斗】的时间了！")
                    this.log("敌人会利用A、B、C、D四种方式攻击你，每回合攻击五次，其中，D克A克B克C克D，这个木马接下来会使用AAAAA攻击，回复DDDDD来阻止它吧！因为我们点击了防御，我们无法对敌人造成伤害，但攻击可以增加魔法值！")
                    this.choose(["DDDDD", "你在教我做事？"], ch => this.fight(ch))
                } else if (ch === 1) {
                    this.log("星空：你……不选防御吗？那也挺好。")
                    this.log("星空：总之，现在是进入【战斗】的时间了！")
                    this.log("敌人会利用A、B、C、D四种方式攻击你，每回合攻击五次，其中，D克A克B克C克D，这个木马接下来会使用AAAAA攻击，回复DDDDD来阻止它吧！")
                    this.choose(["DDDDD", "你在教我做事？"], ch => this.fight(ch))
                } else {
                    throw new Error("Invalid Input.")
                }
                return
            }
            switch (ch) {
                case 0:
                    
                    let battlables = []
                    for (let index in this.game.items) {
                        let item = this.game.items[index]
                        let itemData = data.items[item]
                        if ("battle" in itemData && itemData.battle === true) {
                            battlables.push(parseInt(index))
                        }
                    }
                    if (battlables.length === 0) {
                        this.log("你没有可用的物品。")
                        return this.prepareChoose()
                    }
                    this.log("选择一项物品。")
                    this.game.waitProcess(this, (p) => {
                        for (let index of battlables) {
                            // console.log(index, this.game.$items.eq(parseInt(index)))
                            this.game.$items.children().eq(index).css("boxShadow", "2px 2px 4px 4px #66ccff").on("click", () => {
                                this.game.use(index, this)
                                this.game.$items.children().css("boxShadow", "").off("click")
                                p.waitDie(this)
                            })
                        }
                    })
                    break;
                case 1:
                    this.log("你选择了防御。")
                    this.defense = true
                    this.magic += 40
                    break;
                case 2:
                    // 魔法值为零，或没有几何八面体且魔法值小于治疗魔法消耗
                    if (this.magic === 0 || (!this.octahedron && this.magic < this.cureMagicCost)) {
                        this.log("你的魔法值不够！")
                        return this.prepareChoose()
                    }
                    this.magicChoose()
                    break;
                case 3:
                    this.log("你选择了跳过。")
            }
            // 隐藏boss J12132特殊技能
            if (this.enemy.id === 14 && !this.defense) { // 大招
                if (this.chaoAttacked == false && (this.chaos >= 85 || this.enemy.health <= 1400)) {
                    this.log('混沌持续上升！战斗已经进入白热化！')
                    this.log('现在，你需要独自一人面对考验')
                    this.log('J12132正在释放一次“混沌冲击！”')
                    this.withXk = false
                    this.octahedron = false
                    this.chaoAttacked = true
                    this.fightTimes = 2
                    this.enemy.attack += 5
                    this.game.virtually(12133)
                    this.roundEnd(() => {
                        this.enemy.attack -= 5
                    })
                } else { // 每回合若不选防御随机触发一个技能
                    switch (Math.floor(Math.random() * 4)) {
                        case 0:
                            this.log("小丑使用了“红心治疗”！")
                            this.game.waitChoose(this, ["进攻", "诅咒"], ch => {
                                if (ch == 0) {
                                    this.chaos += randInt(3,5)
                                    this.enemy.health += randInt(10,50)
                                } else {
                                    this.log('你诅咒小丑的治疗法术，小丑的法术失效了！')
                                    this.chaos += 1
                                }
                            })
                            break
                        case 1: // 草花？不是梅花吗（
                            this.log('小丑使用了“草花守护”！')
                            this.game.waitChoose(this, ["进攻", "打散"], ch => {
                                if (ch == 0) {
                                    this.chaos += randInt(3,4)
                                    let attack = this.game.attack
                                    this.game.attack = 0
                                    this.roundEnd(() => this.game.attack = attack)
                                } else {
                                    this.log('你用力向草花打去')
                                    this.chaos += 2
                                }
                            })
                            break
                        case 2:
                            this.log('小丑使用了“方块箭矢”！')
                            this.game.waitChoose(this, ["进攻", "格挡"], ch => {
                                if (ch == 0) {
                                    this.chaos += 2
                                    this.game.health -= randInt(5,35)
                                } else {
                                    this.log('你尽可能地格挡箭矢的进攻')
                                    this.chaos += randInt(1,5)
                                    this.game.attack -= 10
                                    this.roundEnd(() => this.game.attack += 10)
                                }
                            })
                            break
                        case 3:
                            this.log('小丑使用了“黑桃炸弹”！')
                            this.game.waitChoose(this, ["进攻", "闪躲"], ch => {
                                if (ch == 0) {
                                    this.chaos += randInt(2,3)
                                    this.enemy.attack += 5
                                    this.roundEnd(() => this.enemy.attack -= 5)
                                } else {
                                    this.log('你拼命闪躲着炸弹，你的防御增加了！同时攻击减少了')
                                    this.chaos += randInt(3,5)
                                    this.game.defence += 10
                                    this.game.attack -= 10
                                    this.roundEnd(() => this.game.defence -= 10)
                                    this.roundEnd(() => this.game.attack += 10)
                                }
                            })
                            break
                    }
                }
            }
            //
            this.fightInput()
        }
        
        fightInput() {
            this.wait( () => {
                const attack = () => {
                    
                    // @ts-ignore
                    let str = $input.val()
                    if (!Battle.check5Capitals(str)) {
                        return;
                    }
                    $attack.remove()
                    this.fight(str)
                }
                let $attack = $("<div/>").appendTo(this.zeroTable.$outer)
                let $input = $("<input/>")
                    .attr("type", "text")
                    .appendTo($attack)
                    .on("keypress", e => {
                        if (e.which === 13) {
                            attack()
                        }
                    })
                if (this.game.settings.get("random")) {
                    let str = []
                    for (let i = 0; i < 5; i++) {
                        str.push(65 + Math.floor(Math.random() * 4)) 
                    }
                    $input.val(String.fromCharCode(...str))
                }
                Game.button()
                    .html("攻击！")
                    .appendTo($attack)
                    .on("click", () => attack())
            })
        }
        
        magicChoose() {
            this.log("你选择了魔法。")
            this.wait(500)
            
            let magics = [`治疗魔法（${this.cureMagicCost}）`, "战斗魔法（70）", `黑暗魔法（${this.black ? "100" : "？"}）`]
            if (this.octahedron) { // 如果 几何八面体 enabled
                magics.push("几何八面体（消耗全部魔法值造成一半伤害）")
            }
            var ok = false
            const chooseMagic = () => 
            this.game.Process((proc) => {
                proc.choose(magics, ( magic) => {
                    this.game.Process((process) => {
                        switch (magic) {
                            case 0:
                                if (this.magic < this.cureMagicCost) {
                                    process.log("你的魔法值不够！")
                                    return
                                }
                                process.log(`你选择了治疗魔法，HP恢复${this.cureMagicPlus}`)
                                this.magic -= this.cureMagicCost
                                this.game.health += this.cureMagicPlus
                                break;
                            case 1:
                                if (this.magic < 70) {
                                    process.log("你的魔法值不够！")
                                    return
                                }
                                process.log(`你选择了战斗魔法，Att提高5，持续一回合。`)
                                this.battleMagic = true
                                this.magic -= 70
                                this.game.attack += 5
                                break;
                            case 2:
                                if (this.black) {
                                    if (this.magic < 100) {
                                        process.log("你的魔法值不够！")
                                        return
                                    }
                                    process.log("水晶被黑暗笼罩住了！黑暗法术增强了！")
                                    this.magic = 0
                                    this.enemy.health = 0
                                } else {
                                    process.log("l͓̩̫̘͙͔̯͖̟̤̓͊̑̌́̂̆̚ò̥̪̭̱̰̝̒͂̄͋̿̏͆́̚c͍̲͇͚̖̬͈̪͙̳͌̉́̃k̪̥̱̝̱̑̈́̏̽͗̊̈́͂̀̍e̞͎̩̜̱̩͚̤̊͌̀̀d̠̖̞̝̙̪̟̞̐͛̈̊̀͂̄͌̓̏͌̓ͅ")
                                    return
                                }
                                break;
                            case 3:
                                if (this.enemy.id === 9) {
                                    this.game.virtually(200)
                                }
                                let currentMagic = this.magic
                                this.magic = 0
                                this.enemy.health -= currentMagic / 2
                                process.log(`你选择了几何八面体，对【${this.enemy.name}】造成${currentMagic / 2}点伤害！`)
                                break;
                            default:
                                throw new Error("非法输入")
                            
                        }
                        process.die(proc)
                        ok = true
                    }).go()
                    proc.die(ok ? this : chooseMagic())
                })
            }).go()
            
            this.wait(() => chooseMagic())
        }
        
        static check5Capitals(str) {
            if (str.length !== 5) {
                return false
            }
            for (let i = 0; i < 5; i++) {
                if (!(65 <= str.charCodeAt(i) && str.charCodeAt(i) <= 68)) {
                    return false
                }
            }
            return true
        }
        
        static computeHurtHarm(str, baseThis, baseEnemy, defense, defence, game, breakRate, self) {
            if (baseThis < 0) {
                baseThis = 0
            }
            if (baseEnemy < 0) {
                baseEnemy = 0
            }
            var same; // 拉低复用性，差评！
            if (self && self.enemy.id === 4) {
                if (self.rounds % 4 === 3) {
                    same = Math.floor(Math.random() * 4)
                }
            }
            let hurt = 0, harm = 0, letters = ""
            for (let i = 0; i < 5; i++) {
                let charThis = str.charCodeAt(i) - 65, charEnemy = same || Math.floor(Math.random() * 4), letter = String.fromCharCode(charEnemy + 65)
                if (charThis == charEnemy - 1 || charThis == 3 && charEnemy == 0) {
                    harm += baseThis
                    Battle.charWithColor(str.charAt(i), game.$interface, defense ? 0 : 1, false, i * 10 + 30 + "%")
                    Battle.charWithColor(letter, game.$interface, -1, true, i * 10 + 30 + "%")
                } else if (charEnemy == charThis - 1 || charEnemy == 3 && charThis == 0) {
                    // 是否破甲
                    let broken = false;
                    if (breakRate && Math.random() < breakRate) {
                        defence = 0
                        broken = true
                    }
                    if (defence < baseEnemy) {
                        hurt += baseEnemy - defence
                    }
                    console.log(i, broken, defense)
                    Battle.charWithColor(str.charAt(i), game.$interface, defense ? 0 : 1, true, i * 10 + 30 + "%", defense && broken)
                    Battle.charWithColor(letter, game.$interface, -1, false, i * 10 + 30 + "%")
                } else {
                    Battle.charWithColor(str.charAt(i), game.$interface, defense ? 0 : 1, true, i * 10 + 30 + "%")
                    Battle.charWithColor(letter, game.$interface, -1, true, i * 10 + 30 + "%")
                }
                letters += letter
            }
            return [hurt, letters, harm]
        }
        
        static charWithColor(char, $e, animation, fail, left, broken) {
            var colors = {
                A: "red",
                B: "green",
                C: "brown",
                D: "aqua"
            }
            var $span = $("<span/>").html(char).css("color", colors[char]).appendTo($e)
            $span.css({
                fontSize: "3em",
                position: "fixed",
                display: "block",
                left: left,
                fontWeight: "bold"
            })
            let type;
            if (animation === 1) {
                type = "self-"
            } else if (animation === 0) {
                type = "self-defense-"
            } else if (animation === -1) {
                type = "enemy-"
            }
            if (broken) {
                type += "broken"
            } else if (fail) {
                type += "failed"
            } else {
                type += "success"
            }
            $span.css("animation", `ate-char-${type} 4s linear`)
            $span.css("--char-color", colors[char])
            window.setTimeout(() => $span.remove(), 3800)
            return $span
        }
        
        fight(str) {
            if (this.tutorial && typeof str === "number") {
                if (str === 0) {
                    this.magic += 40
                    this.log("星空：太棒了，现在我们有足够的魔法值来使用魔法了，试一下【魔法】吧，它会给你带来增益效果！剩下的你就自己摸索吧")
                } else {
                    this.log("星空：呃……你没有听我的，看来你是想自己对战了，那我就不打扰你了！我先给你个治疗法术吧！")
                    this.game.execute("health + 240")
                }
                this.tutorial = false // 退出教程
            } else if (typeof str === "string") {
                let enemyDefense = Math.random() < this.enemy.defenseRate
                let enemyDefence = enemyDefense ? this.enemy.defence : 0
                let [hurt, letters, harm] = Battle.computeHurtHarm(
                    str, // 攻击方式
                    this.defense ? 0 : (this.game.attack - enemyDefence), // 己方单伤害
                    this.enemy.attack, // 敌方原始伤害
                    this.defense, // 是否防御
                    this.game.defence, // 己方防御值
                    this.game,
                    this.enemy.id === 13 && this.heavyAttack ? 0.3 : 0, // 破甲率
                    this
                    )
                this.log(`你的攻击是${str}，对方的攻击是${letters}`)
                if (enemyDefense) {
                    this.log(`${this.enemy.name}选择了防御。`)
                }
                this.log(`你受到${hurt}点伤害`)
                this.game.health -= hurt
                this.log(`你造成了${harm}点伤害`)
                this.enemy.health -= harm
                if (this.withXk) {
                    let xkHarm = enemyDefence < 20 ? 20 - enemyDefence : 0
                    this.log(`星空造成了${xkHarm}点伤害`)
                    this.enemy.health -= xkHarm
                }
                this.fightTimes--
                if (this.fightTimes > 0) {
                    return this.fightInput() // 散弹攻击打两次
                }
                if (this.enemy.fixed && this.heavyAttack && harm > 0) {
                    this.log("你朝炮筒攻打过去，机械木马开始松动了")
                    this.enemy.gunHealth--
                }
                if (this.battleMagic) {
                    this.game.attack -= 5
                }
            }
            for (let each of this.roundEndCallback) {
                each.call(this.game)
            }
            if (!this.won) {
                this.rounds++
                this.round()
            }
        }
        // @ts-ignore
        get magic() {
            return this._magic
        }
        // @ts-ignore
        set magic(val) {
            if (val > 100) {
                val = 100
            }
            this._magic = val
            this.zeroTable.magic.set(val)
        }
        // @ts-ignore
        get chaos() {
            return this._chaos
        }
        // @ts-ignore
        set chaos(val) {
            this._chaos = val
            // @ts-ignore
            this.enemyTable.chaos.set(val)
            if (this.chaos >= 100) {
                this.log('混沌盘旋着毁灭了战场，你胜利了。')
                this.game.virtually(12132)
                this.win()
            }
        }
        
        roundEnd(callback) {
            this.roundEndCallback.push(callback)
        }
        // @ts-ignore
        get black() {
            return this.game.judge(1024) && this.enemy.id === 9
        }
    }
    class Enemy {
        
        constructor(enemyData, battle) {
            
            this.id = enemyData.id
            this.battle = battle
            this.game = battle.game
            
            this.name = enemyData.name
            
            this.full = enemyData.health
            
            this.health = enemyData.health
            
            this.attack = enemyData.attack
            
            this.defence = enemyData.defence
            
            this.defenseRate = enemyData.defenseRate
            this.message = enemyData.message
            if (this.id === 13) { // 机械木马
                this.gunHealth = 5
                
                this.fixed = false
            }
        }
        // @ts-ignore
        get health() {
            return this._health
        }
        // @ts-ignore
        set health(val) {
            this._setHealth(val)
            if (this.id === 13) {
                if (val <= 0) {
                    this.battle.log("木马的血条似乎空了……但不要以为【自我修复】的力量就这点！")
                    this.game.achieve(3)
                    this._setHealth(this._health + 200)
                }
                return
            } else if (this.id === 14) {
                if (val <= 0) { // J12132暴力结局
                    this.battle.win()
                }
            }
            if (val <= 0) {
                this.battle.win()
            }
        }
        
        _setHealth(val) {
            this._health = val
            // @ts-ignore
            this.battle.enemyTable.health.set(val)
        }
        // @ts-ignore
        get gunHealth() {
            return this._gunHealth
        }
        // @ts-ignore
        set gunHealth(val) {
            if (val <= 0) {
                this.battle.log("机械木马剧烈地抖动！你胜利了！")
                this.battle.win()
            }
            this._gunHealth = val
            this.battle.enemyTable.gunHealth.set(val)
        }
    }
    class Game {
        constructor() {
            this.id = -1
            this.$interface = $(".ate-interface")
            this.$settings = Game.button().html("设置").on("click", () => this.settingsMenu()).appendTo(this.$interface)
            var $enter = $("<div/>").addClass("ate-enter").html("Extend Air Ticket<div>Click to start</div>").prependTo(this.$interface).one("click", () => {
                $enter.fadeOut(1000, () => {
                    $enter.remove()
                })
            })
            var $white = $("<div/>").addClass("ate-white").prependTo(this.$interface)
            var $sw0rd = $("<div/>").addClass("ate-sw0rd").prependTo(this.$interface).hide().fadeIn(1000)

            $sw0rd.on("click", () => {
                location.href = "https://wiki.cvserver.top"
            })

            var $author = $("#author")
            $author.on("click", () => {
                $author.hide()
            })
            setTimeout(() => {
                $white.remove()
                $sw0rd.fadeOut(1000)
            }, 4000)

            $(document).one("click", () => document.getElementById("music").play())
            this.itemImages = []
            for (let each of data.items) {
                this.itemImages.push("./images/" + each.id + ".png")
            }

            this.chooseChapter()
        }
        
        chooseChapter() {
            var $chapters = $("<div/>").addClass("ate-chapters").appendTo(this.$interface)
            for (let i = 1; i <= 5; i++) {
                let $chapter = $("<div/>").addClass("ate-chapter").appendTo($chapters)
                if (data[i]) { // 若数据中有该章节
                    $chapter.html("Chapter " + i).on("click", () => {
                        
                        this.chapter = i
                        $chapters.fadeOut(() => {
                            $chapters.remove()
                            this.run()
                        })
                    })
                } else { // 若尚无该章节
                    $chapter.addClass("ate-chapter-locked").html("locked")
                }
            }
        }
        
        run() {
            this.$save = Game.button().html("保存").on("click", () => this.save()).appendTo(this.$interface)
            this.table = new Table("ate-vals", "状态栏").appendTo(this.$interface)
            this.$items = $("<div/>").addClass("ate-items").appendTo(this.$interface)
            this.$equipments = $("<div/>").addClass("ate-equipments").appendTo(this.$interface)
            this.$message = $("<div/>").addClass("ate-messages").appendTo(this.$interface)
            this.$battle = $("<div/>").addClass("ate-battle").appendTo(this.$interface)
            this.$buttons = $("<div/>").addClass("ate-choices").appendTo(this.$interface)
            this.$weapon = $("<div/>").appendTo(this.$equipments)
            this.$armor = $("<div/>").appendTo(this.$equipments)
            this.$armor.append($("<span/>").addClass("ate-item-name").html("防具"))
            this.$weapon.append($("<span/>").addClass("ate-item-name").html("武器"))
            this.table.add("health", "HP", data[this.chapter].maxHealth, "green")
            this.table.add("attack", "Att")
            this.table.add("defence", "Def")
            this.table.add("cm", "CM币")

            
            this.max = 10
            for (let i = 0; i < this.max; i++) {
                $("<div/>").addClass("ate-item").appendTo(this.$items)
            }
            this.queue = new Queue(this)
            this.dead = false
        	this.attack = 15
            this.defence = 0
            var localStorage = window.localStorage
            if (localStorage.gameData) {
                this.store = JSON.parse(localStorage.gameData)
                this.health = this.store.health
                this.experience = this.store.experience
                this.items = this.store.items
                this.stackables = this.store.stackables
                for (let each of this.items) { // 快快看，Zes在这里把of写成in
                	this._add(each) // 无需parseInt, Game.items是number[]
                }
                this.weapon = this.store.weapon
                this.armor = this.store.armor
                this.cm = this.store.cm
                this.virtualExperience = this.store.virtual || []
            } else {
                this.store = {}
                this.health = data[this.chapter].maxHealth
                this.cm = 0
                
                this.experience = []
                this.stackables = {}
                
                this.items = []
                
                this.virtualExperience = []
            }
            
            for (let each of data.items) {
                if (each.stackable && !(each.id in this.stackables)) {
                    this.stackables[each.id] = 0
                }
            }
            
            this.R = Math.round(Math.random() * 100) + 1
            
            this.history = []
            
            this.exp(this.experience.length ? this.experience.pop() : 0)
        }
        
        _log(msg) {
            var $msg = $("<span/>").html(msg).css("display", "none")
            var deferred = $.Deferred()
            this.$message.scrollTop(this.$message[0].scrollHeight)
            this.$message.append($msg).append("<br>")
            $msg.fadeIn(this.settings.get("speed"), () => deferred.resolve())
            this.history.push(msg)
            return deferred
        }
        
        log(msg) {
            this.wait(() => this._log(msg))
        }
        
        showItems(nothrowable) {
            var a = []
            for (let each of this.items) {
                let itemData = data.items[each]
                if (itemData.throwable !== false || !nothrowable) {
                    a.push(itemData.name)
                }
            }
            return a
        }
        
        putOn(item) {
            var itemData = data.items[item]
            if ("attack" in itemData && itemData.attack || itemData.id === 24) { // 零剑
                this.weapon = item
            } else if ("defence" in itemData && itemData.defence) {
                this.armor = item
            } else {
                throw new Error("不可佩戴")
            }
        }
        // #region
        // @ts-ignore
        get attack() {
            return this._attack
        }
        
        // @ts-ignore
        set attack(val) {
            this._attack = val
            if (this.weapon === 24) {
                this.table.attack.$val.html("?")
                return
            }
            this.table.attack.set(val)
        }
        // @ts-ignore
        get defence() {
            return this._defence
        }
        
        // @ts-ignore
        set defence(val) {
            this._defence = val
            this.table.defence.set(val)
        }
        // @ts-ignore
        get cm() {
            return this._cm
        }
        
        // @ts-ignore
        set cm(val) {
            this._cm = val
            this.table.cm.set(val)
        }
        // @ts-ignore
        get health() {
            return this._health
        }
        
        // @ts-ignore
        set health(val) {
            if (val > data[this.chapter].maxHealth) {
                val = data[this.chapter].maxHealth
            } else if (val <= 0) {
                this.die()
            }
            this._health = val
            this.table.health.set(val)
        }
        // @ts-ignore
        get weapon() {
            return this._weapon
        }
        
        // @ts-ignore
        set weapon(weapon) {
            if (!weapon) {
                return
            }
            var name = data.items[weapon].name, old = this.weapon
            this._weapon = weapon
            if (old) {
                if (old === 24) {
                    window.clearInterval(this.timer.id)
                    this.attack -= this.timer.lastAdd
                } else {
                    // @ts-ignore
                    this.attack -= data.items[old].attack
                }
                this._add(old)
                this.items.push(old)
            }
            this._removeItem(weapon)
            this.items.splice(this.items.indexOf(weapon), 1)
            this.addImage(this.$weapon, weapon)
            if (weapon === 24) {
                this.timer = {}
                this.timer.lastAdd = 0
                this.timer.id = window.setInterval(() => {
                    this.attack -= this.timer.lastAdd
                    this.timer.lastAdd = 5 + Math.floor(Math.random() * 46)
                    this.attack += this.timer.lastAdd
                }, 5000)
            } else {
                // @ts-ignore
                this.attack += data.items[weapon].attack
            }
            // @ts-ignore
            this.$weapon.html($("<span/>").addClass("ate-item-name").html(name))
        }
        // @ts-ignore
        get armor() {
            return this._armor
        }
        
        // @ts-ignore
        set armor(armor) {
            if (!armor) {
                return
            }
            var name = data.items[armor].name, old = this._armor
            this._armor = armor
            if (old) {
                // @ts-ignore
                this.defence -= data.items[old].defence
                this._add(old)
                this.items.push(old)
            }
            this._removeItem(armor)
            this.items.splice(this.items.indexOf(armor), 1)
            this.addImage(this.$armor, armor)
            // @ts-ignore
            this.defence += data.items[armor].defence
            // @ts-ignore
            this.$armor.html($("<span/>").addClass("ate-item-name").html(name))
        }
        // #endregion
        
        add(item, amount, process) {
            var itemData = data.items[item]
            var amount = amount || 1
            process = process || this
            

            
            const add = stackable => {
                if (this.items.length === this.max && !(stackable && this.has(item))) {
                    var items = this.showItems(true)
                    items.push("放弃拾取")
                    this.waitProcess(process, p => {
                        p.log("已满，请丢弃一项")
                        p.choose(items, ( i) => {
                            if (i === this.max) { // 放弃拾取
                                return p.die(this)
                            }
                            this._remove(i)
                            this.items.splice(i, 1)
                            this.items.push(item)
                            if (stackable) {
                                this.setStackableAmount(item, this.stackables[item] + amount)
                            }
                            this._add(item)
                            p.die(process)
                        })
                    })
                } else {
                    this.waitProcess(process, p => {
                        p.log(`已将${itemData.name}加入您的背包。`)
                        this.items.push(item)
                        if (stackable) {
                            this.setStackableAmount(item, this.stackables[item] + amount)
                        }
                        this._add(item)
                        p.waitDie(process)
                    })
                }
            }
            if (itemData.stackable) {
                if (this.stackables[item] === 0) {
                    add(true)
                } else {
                    this.setStackableAmount(item, this.stackables[item] + amount)
                }
            } else {
                add(false)
            }
        }
        
        _add(item) {
            var itemData = data.items[item]
        	var $items = this.$items.children(".ate-item"), 
                $item
        	$items.each((_, ele) => {
        		var $ele = $(ele)
        		if ($ele.html() == "") {
        			$item = $ele
        			return false
        		}
        	})
            if (!$item) {
                throw new Error("没有找到空位")
            }
            this.addImage($item, item)
        	$item.append($("<span/>").addClass("ate-item-name").html(itemData.name))
        	var $des = $("<span/>").addClass("ate-item-description").appendTo($item)
            var $desDiv = $("<div/>").html(itemData.description).appendTo($des)
            if (itemData.stackable) {
                $desDiv.append(`<br>你有<span class="ate-item-amount">${this.stackables[item]}</span>个`)
            }
            if ("attack" in itemData || "defence" in itemData || item === 24) {
                var $button = Game.button().html("装备").appendTo($desDiv)
                $button.on("click", () => {
                    this.putOn(item)
                })
            }
            var pos = this.items.length - 1
            Game.button().html("丢弃").appendTo($desDiv).on("click", () => {
                if (itemData.stackable) {
                    this.removeItem(item, this.queue.now())
                } else {
                    this.remove(pos, this.queue.now())
                }
            })
        }
        
        setStackableAmount(item, amount) {
            if (this.stackables[item] !== 0 && amount !== 0) {
                this.$items.children().eq(this.items.indexOf(item)).find(".ate-item-amount").html("" + amount)
                
            }
            this.stackables[item] = amount
            if (amount === 0) {
                this.items.splice(this.items.indexOf(item), 1)
                this._removeItem(item)
            }
        }
        
        has(item) {
        	return this.items.includes(item)
        }
        
        remove(index, process) {
            process = process || this
            process.wait( () => this._remove(index) )
            return this.items.splice(index, 1)[0]
        }
        
        _remove(index) {
            var $items = this.$items.children()
            $items.eq(index).html("").css("backgroundImage", "").appendTo(this.$items) // 因为这里写成$items导致了大问题
        }
        
        removeItem(item, process) {
            if (data.items[item].stackable) {
                return this.setStackableAmount(item, 0)
            }
            return this.remove(this.items.indexOf(item), process)
        }
        
        _removeItem(item) {
            this._remove(this.items.indexOf(item))
        }
        
        use(index, battle) {
            var item = this.remove(index, battle)
            var itemData = data.items[item]
            battle.log(itemData.name)
            // @ts-ignore
            for (let each of itemData.use) {
            	this.execute(each, battle)
            }
        }
        
        exp(id) {
        	this.$message.html("")
            this.experience.push(id)
            const story = data[this.chapter].story[id]
            if (Array.isArray(story)) {
                this.story(this.judgeArr(story))
            } else {
                this.story(story)
            }
        }
        
        story(story) {
            for (let each of story.message) {
                let msg
                if (typeof each === "string") {
                    msg = each
                } else if (Array.isArray(each)) {
                    msg = this.judgeArr(each)
                    if (!msg) {
                        continue
                    }
                }
                if (msg.startsWith("/")) {
                    this.execute(msg.slice(1))
                } else if (msg.endsWith("/")) {
                    this.log(msg.slice(0, -1))
                } else {
                    this.log(msg)
                }
                    
            }
            if ("battle" in story) {
                this.battle(story.battle, this)
            }
            if ("choice" in story) {
                if ("to" in story) {
                    let length = story.choice.length
                    let choices = []
                    
                    let toes = []
                    for (let i = 0; i < length; i++) {
                        let eachChoice = story.choice[i]
                        let eachTo = story.to[i]
                        if (typeof eachChoice === "string") {
                            choices.push(eachChoice)
                            toes.push(eachTo)
                        } else if (Array.isArray(eachChoice)) {
                            let choice = this.judgeArr(eachChoice)
                            if (choice) {
                                choices.push(choice)
                                toes.push(eachTo)
                            }
                        }
                    }
                    this.choose(choices, ch => {
                        const to = toes[ch]
                        if (typeof to === "number") {
                            this.exp(to)
                        } else if (Array.isArray(to)) {
                            this.exp(this.judgeArr(to))
                        }
                    }, story.fadeChoice)
                } else {
                    this.wait(() => {
                        let $input = $("<input/>")
                            .attr("type", "text")
                            .appendTo(this.$message)
                            .on("keypress", e => {
                                if (e.which === 13) {
                                    
                                    // @ts-ignore
                                    const VAL = $input.val()
                                    if (!("#default" in story.choice)) {
                                        if (VAL in story.choice) {
                                            const to = story.choice[VAL]
                                            if (typeof to === "number") {
                                                this.exp(to)
                                            } else if (Array.isArray(to)) {
                                                this.exp(this.judgeArr(to))
                                            }
                                        } else {
                                            return
                                        }
                                    } else {
                                        const to = story.choice[VAL in story.choice ? VAL : "#default"]
                                        if (typeof to === "number") {
                                            this.exp(to)
                                        } else if (Array.isArray(to)) {
                                            this.exp(this.judgeArr(to))
                                        }
                                    }
                                    $input.remove()
                                }
                            })
                    })
                }
            } else {
            	const to = story.to
                if (!this.settings.get("pass")) {
                    this.wait(() => {
                        var deferred = $.Deferred()
                        this.$message.append($("<span/>").html("点按以继续").css("font-size", "50%"))
                        this.$message.one("click", () => deferred.resolve())
                        return deferred
                    })
                }
                if (typeof to === "number") {
                    this.wait(() => this.exp(to))
                } else if (Array.isArray(to)) {
                    this.wait(() => this.exp(this.judgeArr(to)))
                } else {
                    this.log("敬请期待！")
                }
            }
        }
        
        execute(command, battle) {
            
            var tokens = command.split(" "), amount
            switch (tokens[0]) {
                case "get":
                	this.add(parseInt(tokens[1]), tokens[2] && parseInt(tokens[2]))
                	break;
                case "remove":
                	this.remove(this.items.indexOf(parseInt(tokens[1])))
                	break;
                case "health":
                case "cm":
                    if (tokens[2].startsWith("[") && tokens[2].endsWith("]")) {
                        let scope = tokens[2].slice(1,-1).split(",")
                        amount = parseInt(scope[0]) + Math.floor(Math.random() * (parseInt(scope[1]) - parseInt(scope[0]) + 1))
                    } else {
                        amount = parseInt(tokens[2])
                    }
                	if (tokens[1] == "+") {
                		this[tokens[0]] += amount
                	} else if (tokens[1] == "-") {
                		this[tokens[0]] -= amount
                	}
                	break;
                case "attack":
                case "defence":
                    if (tokens[2].startsWith("[") && tokens[2].endsWith("]")) {
                        let scope = tokens[2].slice(1,-1).split(",")
                        amount = parseInt(scope[0]) + Math.floor(Math.random() * (parseInt(scope[1]) - parseInt(scope[0]) + 1))
                    } else {
                        amount = parseInt(tokens[2])
                    }
                    if (battle) {
                        if (tokens[1] == "+") {
                            this[tokens[0]] += amount
                            battle.roundEnd(() => {this[tokens[0]] -= amount})
                        } else if (tokens[1] == "-") {
                            this[tokens[0]] -= amount
                            battle.roundEnd(() => {this[tokens[0]] += amount})
                        }
                    } else {
                        if (tokens[1] == "+") {
                            this[tokens[0]] += amount
                        } else if (tokens[1] == "-") {
                            this[tokens[0]] -= amount
                        }
                    }
                	break;
                case "harm":
                    battle.enemy.health -= parseInt(tokens[1])
                    break;
                case "dodge":
                    this.dodge(parseInt(tokens[1]), tokens[2])
                    break;
                case "bridge":
                    this.bridge()
                    break;
                case "shop":
                    this.wait(() => this.shop(parseInt(tokens[1])))
                    break;
                case "achieve":
                    this.achieve(parseInt(tokens[1]))
                    break;
                case "edefence":
                case "eattack":
                    let prop = tokens[0].slice(1)
                    if (tokens[2].startsWith("[") && tokens[2].endsWith("]")) {
                        let scope = tokens[2].slice(1,-1).split(",")
                        amount = parseInt(scope[0]) + Math.floor(Math.random() * (parseInt(scope[1]) - parseInt(scope[0]) + 1))
                    } else {
                        amount = parseInt(tokens[2])
                    }
                	if (tokens[1] == "+") {
                		battle.enemy[prop] += amount
                        battle.roundEnd(() => {battle.enemy[prop] -= amount})
                	} else if (tokens[1] == "-") {
                		battle.enemy[prop] -= amount
                        battle.roundEnd(() => {battle.enemy[prop] += amount})
                	}
                    break;
                case "experience":
                    this.virtually(parseInt(tokens[1]))
                    break;
                case "sleep":
                    break;
                default:
                    throw new Error("Unknown Command")
            }
        }
        
        judge(condition) {
            
            if (typeof condition === "number") {
                return this.experience.includes(condition)
            } else if (typeof condition === "string") {
                if (/^[0-9]+$/.test(condition)) {
                    return this.experience.includes(parseInt(condition))
                }
                // 递归警告
                let match
                if (match = /^([\w\!\&\|]+?)\|([\w\!\&\|]+)$/.exec(condition)) {
                    return this.judge(match[1]) || this.judge(match[2])
                }
                if (match = /^([\w\!\&\|]+?)&([\w\!\&\|]+)$/.exec(condition)) {
                    return this.judge(match[1]) && this.judge(match[2])
                }
                if (condition.startsWith("!")) {
                    return !this.judge(condition.slice(1))
                }
                if (match = /^([a-z]+)(\d+)$/.exec(condition)) {
                    let prefix = match[1]
                    let number = parseInt(match[2])
                    switch (prefix) {
                        case "r":
                            return this.R === number
                        case "h":
                            return this.health === number
                        case "i":
                            return this.has(number)
                        case "a":
                            return this.armor === number
                        case "w":
                            return this.weapon === number
                        case "c":
                            return this.cm >= number
                        case "v":
                            return this.virtualExperience.includes(number)
                        default:
                            throw new Error(`Illegal condition prefix '${prefix}'.`)
                    }
                }
            }
        }
        
        static isValidCondition(condition) {
            return typeof condition === "number" || /^[richawv0-9&\|!]+$/.test(condition)
        }
        
        judgeArr(arr) {
            var l = arr.length
            if (!Game.isValidCondition(arr[1])) {
                return arr[randInt(0, l - 1)]
            }
            var res;
            for (let i = 0; i < l; i++) {
                if (i === l - 1) {
                    res = arr[i]
                    break
                }
                if (this.judge(arr[i + 1])) {
                    res = arr[i]
                    break
                }
                i++
            }
            return res
        }
        
        _choose(choices, callback, fade) {
            $(".ate-choices > *").hide()
            var $choices = $("<div/>").appendTo(this.$buttons)
            for (let index in choices) { // index 为字符串，别弄错了
                let $btn = $("<div/>").addClass("ate-choice").html(choices[index]).appendTo($choices);
                $btn.on("click", () => {
                    setTimeout(() => $choices.remove());
                    $(".ate-choices > *").show()
                    callback.call(choices, parseInt(index))
                })
                if (fade && fade.includes(parseInt(index))) { // 瞧，我又弄错了 2022/11/17
                    $btn.css("opacity", "0.05")
                }
            }
            $choices.append(Game.clear())
        }
        
        choose(choices, callback, fade) {
        	this.wait(() => this._choose(choices, callback, fade))
        }
        
        wait(fnOrWaitMs) {
            if (typeof fnOrWaitMs === "function") {
                this.queue.push(fnOrWaitMs, this)
            } else {
                this.queue.push(() => {
                    var deferred = $.Deferred()
                    setTimeout(() => deferred.resolve(), fnOrWaitMs)
                    return deferred
                }, this)
            }
        }
        save() {
            if (this.queue.owner !== 0) {
                return void this.notify("战斗无法保存")
            }
            var items = $.merge([], this.items)
            if (this.weapon) {
                items.push(this.weapon)
            }
            if (this.armor) {
                items.push(this.armor)
            }
        	var saveData = {
        		health: this.health,
        		items: items,
        		experience: this.experience,
                weapon: this.weapon,
                armor: this.armor,
                cm: this.cm,
                stackables: this.stackables,
                virtual: this.virtualExperience
        	}
        	localStorage.gameData = JSON.stringify(saveData)
            this.notify("保存成功")
        }
        
        battle(id, owner) {
            owner.wait(() => {
                var battle = new Battle(data.battle[id], this, owner)
                battle.run()
            })
        }
        
        dodge(baseEnemy, name) {
            this.waitProcess(this, p => {
                this.$interface.addClass("battling")
                const dodge = () => {
                    let str = $input.val()
                    if (typeof str !== "string") {
                        throw new Error("Str should be string")
                    }
                    if (!Battle.check5Capitals(str)) {
                        return;
                    }
                    $attack.remove()
                    let [hurt, letters, _harm] = Battle.computeHurtHarm(str, 0, baseEnemy, true, 0, this)
                    p.log(`你的攻击是${str}，${name}的攻击是${letters}。`)
                    p.log(`你被扣血${hurt}`)
                    this.health -= hurt
                    p.wait(() => void this.$interface.removeClass("battling"))
                    p.wait(() => p.die(this))
                }
                let $attack = $("<div/>").appendTo(this.$battle)
                let $input = $("<input/>").attr("type", "text").appendTo($attack).on("keypress", e => {if (e.which === 13) dodge()})
                if (this.settings.get("random")) {
                    let str = []
                    for (let i = 0; i < 5; i++) {
                        str.push(65 + Math.floor(Math.random() * 4)) 
                    }
                    $input.val(String.fromCharCode(...str))
                }
                // @ts-ignore
                let $button = Game.button().html("攻击！").appendTo($attack).on("click", () => dodge())
            })
        }
        bridge() {
            this.log("选择一座桥以通过")
            const makeBridge = () => this.Process((process) => process.choose(["A", "B", "C"], ( ch) => {
                var noBridge = Math.floor(Math.random() * 3)
                var bridges = ["A", "B", "C"]
                if (ch === noBridge) {
                    bridges.splice(noBridge, 1)
                    process.log(`翻转地板组成了桥${bridges.join()}，你没通过桥！`)
                    process.die(makeBridge())
                } else {
                    process.log("你通过了桥！")
                    process.die(this)
                }
            })).go()
            this.wait(() => makeBridge())
        }
        
        shop(id) {
            var shopData = data.shop[id]
            const shop = () => this.Process((p) => {
                var prices = {}, items = [], itemIds = []
                for (let item in shopData) {
                    let price = shopData[item]
                    if (Array.isArray(price)) {
                        price = this.judgeArr(price)
                        if (!price) {
                            continue
                        }
                    }
                    prices[item] = price
                    itemIds.push(item)
                    items.push(data.items[item].name + ` [cost CM币${price}个]`)
                }
                var leaveKey = items.length
                items.push("离开")
                p.choose(items, ( ch) => {
                    if (ch === leaveKey) {
                        return p.die(this)
                    }
                    if (this.items.length === this.max) {
                        p.log("背包空间不够，你离开了商店")
                        return p.die()
                    }
                    var bought = parseInt(itemIds[ch])
                    if (prices[bought] > this.cm) {
                        p.log("你的CM币不够！")
                    } else {
                        this.cm -= prices[bought]
                        this.add(bought, 1, p)
                    }
                    p.wait(() => p.die(shop()))
                })
            }).go()
            this.wait(() => shop())
        }
        
        virtually(id) {
            this.virtualExperience.push(id)
        }
        die() {
            this.log("黑暗再次降临。")
            if (this.has(2)) {
                this.log("使用复活爱心吗?")
                this.choose(["是", "否"], (ch) => {
                    if (!ch) {
                        this.setStackableAmount(2, this.stackables[2] - 1)
                        this.health = 100
                        this.log("那么，你将再次驱散黑暗")
                    } else {
                        this.log("看来，黑暗将会再度笼罩你")
                        this.log("You died.")
                        delete localStorage.gameData
                    }
                })
            } else {
                this.log("但是，希望似乎保佑不了你")
                this.log("看来，黑暗将会再度笼罩你")
                this.log("You died.")
                delete localStorage.gameData
                delete this.queue
            }
        }
        // @ts-ignore
        get settings() {
        	var settings
        	var defaultSettings = {
        		speed: 1500,
                pass: false
        	}
        	function getSettings() {
        		settings = localStorage.ateSettings ? JSON.parse(localStorage.ateSettings) : defaultSettings
        	}
        	
        	function setItem(item, val) {
        		settings[item] = val
        		localStorage.ateSettings = JSON.stringify(settings)
        		getSettings()
        	}
        	getSettings()
            
        	return {
        		
        		get(prop) {
                    return settings[prop]
                },
                
                set(prop, val) {
                    setItem(prop, val)
                },
                
                toggle(prop) {
                    setItem(prop, !settings[prop])
                }
        	}
        }
        settingsMenu() {
            if ($(".ate-settings").length > 0) { 
                // 阻止生成多个设置窗口
                return
            }
            var $window = $("<div/>")
                .addClass("ate-settings")
                .appendTo(this.$interface)
            // 半透明灰遮罩阻止用户在关闭之前操作游戏
            var $cover = $("<div/>")
                .addClass("ate-cover")
                .appendTo(this.$interface) 
            var $list = $("<ul/>").appendTo($window)


            var $speed = $("<input>")
                .attr("type", "text")
                .val(this.settings.get("speed"))
                .appendTo($("<li/>").html("消息播放时间/ms").appendTo($list))
            
            var pass = this.settings.get("pass")
            var $pass = Game.button(pass && "on")
                .html(pass ? "是" : "否")
                .appendTo($("<li/>").html("无选项自动跳剧情").appendTo($list))
            $pass.on("click", () => {
                $pass.html(this.settings.get("pass") ? "否" : "是")
                this.settings.toggle("pass")
                $pass.toggleClass("ate-button-on")
            })

            var random = this.settings.get("random")
            var $random = Game.button(random && "on")
                .html(random ? "是" : "否")
                .appendTo($("<li/>").html("战斗攻击自动填入").appendTo($list))
            $random.on("click", () => {
                $random.html(this.settings.get("random") ? "否" : "是")
                this.settings.toggle("random")
                $random.toggleClass("ate-button-on")
            })

            if (this.history) {
                Game.button("negative").html("清档").appendTo($window).on("click", () => {
                    delete localStorage.gameData
                    this.notify("存档已清除！")
                })
                $window.append("<div>历史记录：</div>")
                var $history = $("<ol/>").addClass("ate-history").appendTo($window)
                for (let each of this.history) {
                    $("<li/>").html(each).appendTo($history)
                }
            }
            var store = btoa(localStorage.gameData || "")
            var $export = $("<textarea/>")
                .val(store)
                .appendTo($window)
            $("<div/>").addClass("ate-settings-done").appendTo($window).on("click", () => {
                const SPEED_VAL = $speed.val()
                if (typeof SPEED_VAL !== "string") {
                    throw new Error("$speed.val() is a str")
                }
                if (SPEED_VAL.match(/^\d+$/)) {
                    this.settings.set("speed", parseInt(SPEED_VAL))
                }
                const IMPORT_VAL = $export.val()
                if (typeof IMPORT_VAL !== "string") {
                    throw new Error("$speed.val() is a str")
                }
                if (IMPORT_VAL !== store) {
                    localStorage.gameData = atob(IMPORT_VAL)
                }
                $window.animate({left: "-100%"}, 3000, () => $window.remove())
                $cover.remove()
            })
        }
        
        static clear() {
            return $("<div/>").css("clear", "both")
        }
        
        addImage($ele, id) {
            if (id < this.itemImages.length) {
                $ele.css("backgroundImage", `url(${this.itemImages[id]})`)
            }
        }
        
        achieve(id) {
            if (this.achievements.includes(id)) return
            var achievement = data.achievement[id]
            var $achivement = $("<div/>").addClass("ate-achievement")
            this.$interface.append($achivement)
            $("<div/>").addClass("ate-achievement-title").html("成就：" + achievement.name).appendTo($achivement)
            $("<span/>").addClass("ate-achievement-content").html(achievement.description).appendTo($achivement)
            $achivement.animate({opacity: 1.0, left: 0}, 2000)
            setTimeout(() => $achivement.fadeOut(3000), 12000)
            this.achievements.push(id)
        }
        // @ts-ignore
        get achievements() {
            
            var ach = localStorage.ateAchievements ? JSON.parse(localStorage.ateAchievements) : []
            return {
                
                push(id) {
                    ach.push(id)
                    localStorage.ateAchievements = JSON.stringify(ach)
                },
                
                includes(id) {
                    return ach.includes(id)
                },
                // @ts-ignore
                get length() {
                    return ach.length
                }
            }
        }
        
        static button(cls) {
            var $button = $("<div/>").addClass("ate-button")
            return $button.addClass("ate-button-" + cls)
        }
        
        notify(msg) {
            var $msg = $("<div/>").addClass("ate-notification").appendTo(this.$interface).html(msg)
            $msg.fadeIn(1500)
            $msg.fadeOut(3000, () => $msg.remove())
        }
        
        Process(func) {
            return new Process(func, this)
        }
        
        waitProcess(process, func) {
            process.wait(() => this.Process(func).go())
        }
        
        waitChoose(process, choices, func) {
            this.waitProcess(process, (p) => {
                p.choose(choices, ch => {
                    func(ch, process, func)
                    p.die(process)
                })
            })
        }
        
        skip(eid) {
            if (this.queue.processing) {
                throw new Error("Still processing")
            }
            this.$buttons.html("")
            this.exp(eid)
        }

    }


        if (new URL(location.href).searchParams.get("pw") != "3473473639574279") {
            return
        }
    	window.ateGame = new Game()
        window.ATEGame = Game
        $.extend(Game, {Queue, Battle, Enemy})


    	document.title = "游玩 Extend Air Ticket"
    	$("#firstHeading").html(`--- Extend Air Ticket v ${version} ---`)
        $("#version").html(version)

})(jQuery, ateData, "2.12.1.32 Beta")

