"use strict";




(function ($, data, version) {
    class Queue {
        
        constructor(game) {
            this.arrays = {}
            this.indexes = {}
            Queue.owners = []
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
            var owner = this.owner
        	var queueA = this.arrays[owner], i = this.indexes[owner] || 0, queue = this
            this.processing = true
        	function process() {
                if (queue.processing == false) {
                    return
                }
                if (owner !== queue.owner) {
                    queue.processing = false
                    queue.indexes[owner] = i
                    return queue.process()
                }
        		if (i >= queueA.length) {
                    queue.arrays[owner] = []
                    queue.indexes[owner] = 0
                    queue.processing = false
                    return
                }
                console.log(queueA[i])
        		let result = queueA[i++].call(undefined)
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
            if (Queue.curid === undefined) {
                Queue.curid = 0
            }
            Queue.owners.push(obj)
            obj.id = Queue.curid
            Queue.curid++
        }
        now() {
            return Queue.owners[this.owner]
        }
    }
    class Process {
        
        constructor(func, game) {
            if (!game) throw Error("Missing argument game")
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
    }
    class Battle {
        
        constructor(battleData, game, callback) {
            console.log(this)
            Queue.newid(this)
            game.queue.give(this)
            this.game = game
            this.tutorial = battleData.tutorial
            this.withXk = battleData.withXk
            this.octahedron = battleData.octahedron
            this.cureMagicCost = 30
            this.cureMagicPlus = 40
            this.$element = game.$battle
            this.callback = callback
            this.$element.children().fadeOut() // CRD 战斗中短矛子战隐藏母战斗
            this.$enemy = $("<div/>").appendTo(this.$element)
            var $table = $("<table/>").addClass("ate-info").appendTo(this.$enemy)
            var $tbody = $("<tbody/>").appendTo($table)
            var $tr = $("<tr/>").appendTo($tbody)
            this.won = false
            this.afterWin = battleData.win
            var enemyData = data.enemy[battleData.enemy]

            $("<th/>").html(enemyData.name).appendTo($tr)
            $("<td/>").html("HP").appendTo($tr)
            this.$enemyHealth = $("<span/>").appendTo($("<td/>").appendTo($tr))
            this.$enemyHealthRate = $("<div/>").addClass("ate-info-rate").css({backgroundColor: "red", height: "100%"}).insertAfter(this.$enemyHealth)
            this.enemy = new Enemy(enemyData, this)
            
            this.$self = $("<div/>").appendTo(this.$element)
            var $table1 = $("<table/>").addClass("ate-info").appendTo(this.$self)
            var $tbody1 = $("<tbody/>").appendTo($table1)
            var $tr1 = $("<tr/>").appendTo($tbody1)
            this.$self.animate({marginTop: "6em"})

            $("<th/>").html("Zero").appendTo($tr1)
            $("<td/>").html("魔法值").appendTo($tr1)
            this.$magic = $("<span/>").appendTo($("<td/>").appendTo($tr1))
            this.$magicRate = $("<div/>").addClass("ate-info-rate").css({backgroundColor: "purple", height: "0"}).insertAfter(this.$magic)
            this.magic = 0
            this.rounds = 0

            if (this.enemy.id === 4) {
                this.special = 0
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
            this.$self.animate({marginTop: "0"}, 2000, () => {
                this.$enemy.remove()
                this.$self.remove()
            })
            this.$element.children().fadeIn()
            this.wait(() => {
                this.callback.call(this.game)
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
            if (this.enemy.id === 7 && this.rounds % 10 === 9) { // CRD
                
                this.log("CRD：“什么？！你们居然还能挺得住，看来我要动用增援了！”")
                this.wait(() => {
                    this.log("第一个长矛向你袭来")
                    return this.game.battle(8, this)
                })
                this.wait(() => {
                    this.log("第二个长矛向你袭来")
                    return this.game.battle(8, this)
                })
            }
            this.rounds++
            this.roundEndCallback = []
            if (this.enemy.message) {
                let r = 1 + Math.round(Math.random() * this.enemy.random)
                if (this.enemy.message[r]) {
                    this.log(this.enemy.message[r])
                }
            }
            this.prepareChoose()
        }
        prepareChoose() {
            this.choose(["物品", "防御", "魔法", "跳过"], ch => this.prepare(ch))
        }
        
        prepare(ch) {
            this.defense = false
            this.battleMagic = false
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
            } else {
                switch (ch) {
                    case 0:
                        let found = false
                        for (let index in this.game.items) {
                            let item = this.game.items[index]
                            let itemData = data.items[item]
                            if (itemData.battle === true) {
                                found = true
                                this.game.$items.eq(parseInt(index)).on("click", () => {
                                    this.game.use(this.game.items.indexOf(item), this)
                                    this.game.$items.children().off("click")
                                })
                            }
                        }
                        if (!found) {
                            this.log("你没有可用的物品。")
                            return this.prepareChoose()
                        }
                        this.log("选择一项物品。")
                        break;
                    case 1:
                        this.log("你选择了防御。")
                        this.defense = true
                        this.magic += 40
                        break;
                    case 2:
                        if (this.magic === 0 || (!this.octahedron && this.magic < this.cureMagicCost)) {
                            this.log("你的魔法值不够！")
                            return this.prepareChoose()
                        }
                        this.log("你选择了魔法。")
                        this.wait(500)
                        let magics = [`治疗魔法（${this.cureMagicCost}）`, "战斗魔法（70）", `黑暗魔法（${this.black ? "100" : "？"}）`]
                        if (this.octahedron) { // 如果 几何八面体 enabled
                            magics.push("几何八面体（消耗全部魔法值造成一半伤害）")
                        }
                        var ok = false
                        const chooseMagic = () => 
                        this.game.Process((proc) => {
                            proc.choose(magics, (magic) => {
                                this.game.Process((process) => {
                                    switch (magic) {
                                        case 0:
                                            if (this.magic < this.cureMagicCost) {
                                                process.log("你的魔法值不够！")
                                                process.wait(500)
                                                return
                                            }
                                            process.log(`你选择了治疗魔法，HP恢复${this.cureMagicPlus}`)
                                            this.magic -= this.cureMagicCost
                                            this.game.health += this.cureMagicPlus
                                            break;
                                        case 1:
                                            if (this.magic < 70) {
                                                process.log("你的魔法值不够！")
                                                process.wait(500)
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
                                                process.wait(500)
                                                return
                                            }
                                            break;
                                        case 3:
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
                        break;
                    case 3:
                        this.log("你选择了跳过。")
                }
                this.wait( () => {
                    if (this.won) {
                        return;
                    }
                    const attack = () => {
                        
                        // @ts-ignore
                        let str = $input.val()
                        if (!Battle.check5Capitals(str)) {
                            return;
                        }
                        $attack.remove()
                        this.fight(str)
                    }
                    let $attack = $("<div/>").appendTo(this.$self)
                    let $input = $("<input/>").attr("type", "text").appendTo($attack).on("keypress", e => {if (e.which === 13) attack()})
                    let $button = Game.button().html("攻击！").appendTo($attack).on("click", () => attack())
                })
            }
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
        
        static computeHurtHarm(str, baseThis, baseEnemy, defense, game, self) {
            if (baseThis < 0) {
                baseThis = 0
            }
            if (baseEnemy < 0) {
                baseEnemy = 0
            }
            var same; // 拉低复用性，差评！
            if (self && self.enemy.id === 4) {
                if (self.special === 3) {
                    same = Math.floor(Math.random() * 4)
                    self.special = 0
                } else {
                    self.special++
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
                    hurt += baseEnemy
                    Battle.charWithColor(str.charAt(i), game.$interface, defense ? 0 : 1, true, i * 10 + 30 + "%")
                    Battle.charWithColor(letter, game.$interface, -1, false, i * 10 + 30 + "%")
                } else {
                    Battle.charWithColor(str.charAt(i), game.$interface, defense ? 0 : 1, true, i * 10 + 30 + "%")
                    Battle.charWithColor(letter, game.$interface, -1, true, i * 10 + 30 + "%")
                }
                letters += letter
            }
            return [hurt, letters, harm]
        }
        
        static charWithColor(char, $e, animation, fail, left) {
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
            if (animation === 1) {
                $span.css("top", "70%").animate({top: "50%"}, 3000)
            } else if (animation === 0) {
                $span.css("top", "49%").animate({top: "50%"}, 3000)
            } else if (animation === -1) {
                $span.css("top", "20%").animate({top: "40%"}, 3000)
            }
            if (fail) {
                $span.fadeOut(1000, () => $span.remove())
            } else {
                if (animation === 1) {
                    $span.animate({top: "20%"}, 3000, () => $span.remove())
                } else if (animation === 0) {
                    window.setTimeout(() => $span.remove(), 4000)
                } else if (animation === -1) {
                    $span.animate({top: "70%"}, 3000, () => $span.remove())
                }
            }
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
                let [hurt, letters, harm] = Battle.computeHurtHarm(str,
                    this.defense ? 0 : (this.game.attack - enemyDefence),
                    this.enemy.attack - (this.defense ? this.game.defence : 0),
                    this.defense, this.game)
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
                if (this.battleMagic) {
                    this.game.attack -= 5
                }
            }
            for (let each of this.roundEndCallback) {
                each.call(this.game)
            }
            if (!this.won) {
                this.round()
            }
        }
        get magic() {
            return this._magic
        }
        set magic(val) {
            if (val > 100) {
                val = 100
            }
            this._magic = val
            this.$magic.html(val)
            this.$magicRate.css("height", val + "%")
        }
        roundEnd(fn) {
            this.roundEndCallback.push(fn)
        }
        get black() {
            return this.game.judge(1024)
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
            this.random = enemyData.random
            this.message = enemyData.message
        }
        get health() {
            return this._health
        }
        set health(val) {
            if (val <= 0) {
                this.battle.win()
            }
            this._health = val
            this.battle.$enemyHealth.html(val)
            this.battle.$enemyHealthRate.css("height", val / this.full * 100 + "%")
        }
    }
    class Game {
        constructor() {
            this.$interface = $(".ate-interface")
            this.$settings = Game.button().html("设置").on("click", () => this.settingsMenu()).appendTo(this.$interface)
            var $enter = $("<div/>").addClass("ate-enter").html("Air Ticket Extend<div>Click to start</div>").prependTo(this.$interface).one("click", () => {
                $enter.fadeOut(3000, () => {
                    $enter.remove()
                })
            })
            var $white = $("<div/>").addClass("ate-white").prependTo(this.$interface)
            var $sw0rd = $("<div/>").addClass("ate-sw0rd").prependTo(this.$interface).hide().fadeIn(1000)
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
            var $chapters = $("<div/>").appendTo(this.$interface)
            for (let i = 1; i <= 5; i++) {
                let $chapter = $("<div/>").addClass("ate-chapter").appendTo($chapters)
                if (data[i]) {
                    $chapter.html("Chapter " + i).on("click", () => {
                        this.chapter = i
                        $chapters.fadeOut(() => {
                            $chapters.remove()
                            this.run()
                        })
                    })
                } else {
                    $chapter.addClass("ate-chapter-locked").html("locked")
                }
            }
        }
        run() {
            this.$save = Game.button().html("保存").on("click", () => this.save()).appendTo(this.$interface)
            this.$valsTable = $("<table>").addClass("ate-vals ate-info").appendTo(this.$interface)
            this.$items = $("<div/>").addClass("ate-items").appendTo(this.$interface)
            this.$equipments = $("<div/>").addClass("ate-equipments").appendTo(this.$interface)
            this.$message = $("<div/>").addClass("ate-messages").appendTo(this.$interface)
            this.$battle = $("<div/>").addClass("ate-battle").appendTo(this.$interface)
            this.$buttons = $("<div/>").addClass("ate-choices").appendTo(this.$interface)
            var $tbody3 = $("<tbody/>").appendTo(this.$valsTable)
            var $vals = $("<tr/>").appendTo($tbody3)
            this.$weapon = $("<div/>").html("武器").appendTo(this.$equipments)
            this.$armor = $("<div/>").html("防具").appendTo(this.$equipments)
            $("<td/>")     .html("HP")  .appendTo($vals)
            this.$health  = $("<span/>").appendTo($("<td/>").appendTo($vals))
            $("<td/>")     .html("Att") .appendTo($vals)
            this.$attack  = $("<span/>").appendTo($("<td/>").appendTo($vals))
            $("<td/>")     .html("Def") .appendTo($vals)
            this.$defence = $("<span/>").appendTo($("<td/>").appendTo($vals))
            $("<td/>")     .html("CM币").appendTo($vals)
            this.$cm      = $("<span/>").appendTo($("<td/>").appendTo($vals))

            this.$healthRate = $("<div/>").addClass("ate-info-rate").css({backgroundColor: "green", health: "100%"}).insertAfter(this.$health)
            this.max = 10
            for (let i = 0; i < this.max; i++) {
                $("<div/>").addClass("ate-item").appendTo(this.$items)
            }
            this.queue = new Queue(this)

        	this.attack = 15
            this.defence = 0
            var localStorage = window.localStorage
            if (localStorage.gameData) {
                this.store = JSON.parse(localStorage.gameData)
                this.health = this.store.health
                this.experience = this.store.experience
                this.items = this.store.items
                for (let each of this.items) { // 快快看，Zes在这里把of写成in
                	this._add(each) // 无需parseInt, Game.items是number[]
                }
                this.weapon = this.store.weapon
                this.armor = this.store.armor
                this.cm = this.store.cm
                this.stackables = this.store.stackables || {}
            } else {
                this.store = {}
                this.health = data[this.chapter].maxHealth
                this.cm = 0
                
                this.experience = []
                
                this.items = []
                this.stackables = {}
            }
            this.R = Math.round(Math.random() * 100) + 1
            
            this.history = []
            
            this.exp(this.experience.length ? this.experience.pop() : 0)
        }
        _log(msg) {
            var $msg = $("<span/>").html(msg).css("display", "none"), deferred = $.Deferred()
            $msg.css({
                textAlign: "center"
            })
            this.$message.scrollTop(this.$message[0].scrollHeight)
            this.$message.append($msg).append("<br>")
            $msg.fadeIn(this.settings.speed, () => deferred.resolve())
            this.history.push(msg)
            return deferred.promise()
        }
        
        log(msg) {
            this.wait(() => this._log(msg))
        }
        showItems() {
            var a = []
            $.each(this.items, (_, id) => a.push(data.items[id].name) )
            return a
        }
        putOn(item) {
            if (data.items[item].attack || data.items[item].id === 24) { // 零剑
                this.weapon = item
            } else if (data.items[item].defence) {
                this.armor = item
            } else {
                throw new Error("不可佩戴")
            }
        }
        get attack() {
            return this._attack
        }
        set attack(val) {
            this._attack = val
            if (this.weapon === 24) {
                this.$attack.html("?")
                return
            }
            this.$attack.html(val)
        }
        get defence() {
            return this._defence
        }
        set defence(val) {
            this._defence = val
            this.$defence.html(val)
        }
        get cm() {
            return this._cm
        }
        set cm(val) {
            this._cm = val
            this.$cm.html(val)
        }
        get health() {
            return this._health
        }
        set health(val) {
            if (val > data.maxHealth) {
                val = data.maxHealth
            } else if (val <= 0) {
                this.die()
            }
            this._health = val
            this.$health.html(val)
            this.$healthRate.css("height", val / 240 * 100 + "%")
        }
        get weapon() {
            return this._weapon
        }
        
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
                this.attack += data.items[weapon].attack
            }
            this.$weapon.html(name)
        }
        get armor() {
            return this._armor
        }
        
        set armor(armor) {
            if (!armor) {
                return
            }
            var name = data.items[armor].name, old = this._armor
            this._armor = armor
            if (old) {
                this.defence -= data.items[old].defence
                this._add(old)
                this.items.push(old)
            }
            this._removeItem(armor)
            this.items.splice(this.items.indexOf(armor), 1)
            this.addImage(this.$armor, armor)
            this.defence += data.items[armor].defence
            this.$armor.html(name)
        }
        
        add(item, amount, process) {
            var itemData = data.items[item]
            var amount = amount || 1
            process = process || this
            
            const add = stackable => {
                if (this.items.length === this.max) {
                    var items = this.showItems()
                    items.push("放弃拾取")
                    this.waitProcess(process, p => {
                        p.log("已满，请丢弃一项")
                        p.choose(items, i => {
                            if (i === this.max) {
                                return p.die(this)
                            }
                            this._remove(i)
                            this.items.splice(i, 1)
                            this.items.push(item)
                            if (stackable) {
                                this.stackables[item] += amount
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
                            this.stackables[item] += amount
                        }
                        this._add(item)
                        p.wait(() =>p.die(process))
                    })
                }
            }
            if (itemData.stackable) {
                if (!(item in this.stackables)) {
                    this.stackables[item] = 0
                }
                if (this.stackables[item] === 0) {
                    add(true)
                } else {
                    this.stackables[item] += amount
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
        	$item.append(itemData.name)
        	var $des = $("<span/>").addClass("ate-item-description").appendTo($item)
            var $desDiv = $("<div/>").html(itemData.description).appendTo($des)
            if ("attack" in itemData || "defence" in itemData || item === 24) {
                var $button = Game.button().html("装备").appendTo($desDiv)
                $button.on("click", () => {
                    this.putOn(item)
                })
            }
            Game.button().html("丢弃").appendTo($desDiv).on("click", () => {
                this.remove(this.items.length - 1, this.queue.now())
            })
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
        	var clear = this.$items.children().eq(-1).remove()
            var $items = this.$items.children()
            $items.eq(index).html("").css("backgroundImage", "").appendTo(this.$items) // 因为这里写成$items导致了大问题
            clear.appendTo(this.$items)
        }
        removeItem(item) {
            return this.remove(this.items.indexOf(item))
        }
        _removeItem(item) {
            this._remove(this.items.indexOf(item))
        }
        
        use(index, battle) {
            var item = this.remove(index)
            for (let each of data[item].use) {
            	this.execute(each, battle)
            }
        }
        exp(id) {
        	this.$message.html("")
            this.experience.push(id)
            var story = data[this.chapter].story[id]
            if (!Array.isArray(story)) {
                this.story(story)
            } else {
                this.story(this.judge(story[1]) ? story[0] : story[2])
            }
        }
        story(story) {
            for (let each of story.message) {
                let msg
                if (typeof each === "string") {
                    msg = each
                } else if (Array.isArray(each)) {
                    if (each[2]) {
                        msg = this.judge(each[1]) ? each[0] : each[2]
                    } else {
                        if (this.judge(each[1])) {
                            msg = each[0]
                        } else {
                            continue;
                        }
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
            if (story.choice) {
                let choices = []
                for (let each of story.choice) {
                    if (typeof each === "string") {
                        choices.push(each)
                    } else if (Array.isArray(each)) {
                        if (this.judge(each[1])) {
                            choices.push(each[0])
                        } else {
                            if (each[2]) {
                                choices.push(each[2])
                            }
                        }
                    }
                }
                this.choose(choices, ch => {
                    var to = story.to[ch]
                    if (typeof to === "number") {
                        this.exp(to)
                    } else if (Array.isArray(to)) {
                        this.exp(this.judge(to[1]) ? to[0] : to[2])
                    }
                }, story.fadeChoice)
            } else {
            	let to = story.to
                if (!this.settings.pass) {
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
                    this.wait(() => this.exp(this.judge(to[1]) ? to[0] : to[2]))
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
                	if (tokens[1] == "+") {
                		this[tokens[0]] += amount
                        battle.roundEnd(() => {this[tokens[0]] -= amount})
                	} else if (tokens[1] == "-") {
                		this[tokens[0]] -= amount
                	}
                	break;
                case "harm":
                    battle.enemy.health -= parseInt(tokens[1])
                    break;
                case "dodge":
                    this.dodge(parseInt(tokens[1]))
                    break;
                case "bridge":
                    this.bridge()
                    break;
                case "shop":
                    this.wait(() => this.shop(parseInt(tokens[1])))
                    break;
                case "achieve":
                    this.achieve(tokens[1])
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
                        case "i":
                            return this.items.length === number
                        case "c":
                            return this.cm >= number
                        default:
                            throw new Error(`Illegal condition prefix '${prefix}'.`)
                    }
                }
            }
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
        
        wait(fn) {
            if (typeof fn === "function") {
                this.queue.push(fn, this)
            } else {
                this.queue.push(() => {
                    var deferred = $.Deferred()
                    setTimeout(() => deferred.resolve(), fn)
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
                stackables: this.stackables
        	}
        	localStorage.gameData = JSON.stringify(saveData)
            this.notify("保存成功")
        }
        
        battle(id, owner) {
            this.wait(() => {
                var battle = new Battle(data.battle[id], this, () => this.queue.give(owner))
                battle.run()
            })
        }
        
        dodge(baseEnemy) {
            this.waitProcess(this, p => {
                const dodge = () => {
                    
                    let str = $input.val()
                    if (!Battle.check5Capitals(str)) {
                        return;
                    }
                    $attack.remove()
                    let [hurt, letters, _harm] = Battle.computeHurtHarm(str, 0, baseEnemy, true, this)
                    p.log(`你的攻击是${str}，对方的攻击是${letters}。`)
                    p.log(`你被扣血${hurt}`)
                    this.health -= hurt
                    p.wait(() => p.die(this))
                }
                let $attack = $("<div/>").appendTo(this.$battle)
                let $input = $("<input/>").attr("type", "text").appendTo($attack).on("keypress", e => {if (e.which === 13) dodge()})
                let $button = Game.button().html("攻击！").appendTo($attack).on("click", () => dodge())
            })
        }
        bridge() {
            this.log("选择一座桥以通过")
            const makeBridge = () => this.Process((process) => process.choose(["A", "B", "C"], (ch) => {
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
                        if (this.judge(price[1])) {
                            price = price[0]
                        } else {
                            if (!price[2]) {
                                continue
                            } else {
                                price = price[2]
                            }
                        }
                    }
                    prices[item] = price
                    itemIds.push(item)
                    items.push(data.items[item].name + ` [cost CM币${price}个]`)
                }
                var leaveKey = items.length
                items.push("离开")
                p.choose(items, ch => {
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
        die() {
            this.log("黑暗再次降临。")
            if (this.has(2)) {
                this.log("使用复活爱心吗?")
                this.choose(["是", "否"], (ch) => {
                    if (!ch) {
                        if (this.stackables[2] > 1) {
                            this.stackables[2]--
                        } else if (this.stackables[2] === 1) {
                            this.removeItem(2)
                        }
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
        		get speed() {
        			return settings.speed
        		},
        		set speed(val) {
        			setItem("speed", val)
        		},
                get pass() {
                    return settings.pass
                },
                set pass(val) {
                    setItem("pass", val)
                }
        	}
        }
        settingsMenu() {
            if ($(".ate-settings").length) {
                return
            }
            var $window = $("<div/>").addClass("ate-settings").appendTo(this.$interface)
            var $cover = $("<div/>").addClass("ate-cover").appendTo(this.$interface)
            var $list = $("<ul/>").appendTo($window)
            var $speed = $("<input>").attr("type", "text").val(this.settings.speed).appendTo($("<li/>").html("播放速率倒数").appendTo($list))
            var $pass = Game.button().html(this.settings.pass ? "是" : "否").appendTo($("<li/>").html("无选项自动跳剧情").appendTo($list))
            $pass.on("click", () => {
                $pass.html(this.settings.pass ? "否" : "是")
                this.settings.pass = !this.settings.pass
            })
            Game.button().html("清档").appendTo($window).on("click", () => {
                delete localStorage.gameData
                this.notify("存档已清除！")
            })
            $window.append("<div>历史记录：</div>")
            var $history = $("<ol/>").addClass("ate-history").appendTo($window)
            for (let each of this.history) {
                $("<li/>").html(each).appendTo($history)
            }
            $("<div/>").addClass("ate-settings-done").appendTo($window).on("click", () => {
                if ($speed.val().match(/^\d+$/)) {
                    this.settings.speed = parseInt($speed.val())
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
                get length() {
                    return ach.length
                }
            }
        }
        static button() {
            return $("<div/>").addClass("ate-button")
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

        skip(eid) {
            if (this.queue.processing) {
                throw new Error("Still processing")
            }
            this.$buttons.html("")
            this.exp(eid)
        }

    }


    	window.ateGame = new Game()
        window.ATEGame = Game
        $.extend(Game, {Queue, Battle, Enemy})



    	document.title = "游玩 Air Ticket Extend"
    	$("#firstHeading").html(`--- Air Ticket Extend v ${version} ---`)

})(jQuery, ateData, "2.9.0 Beta")

