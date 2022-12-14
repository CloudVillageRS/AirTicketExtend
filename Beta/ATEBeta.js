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
            this.$element.children().fadeOut() // CRD ????????????????????????????????????
            var enemyData = data.enemy[battleData.enemy]
            
            this.won = false
            
            this.afterWin = battleData.win
            this.enemyTable = new Table("ate-enemy-table", enemyData.name).appendTo(this.$element)

            this.enemyTable.add("health", "HP", enemyData.health, "red")
            this.enemyTable.add("gunHealth", "??????", 5, "orange", true)
            this.enemyTable.add("chaos", "??????", 120, "linear-gradient(red, grey)", true)
            this.enemy = new Enemy(enemyData, this)
            
            this.zeroTable = new Table("ate-zero-table", "Zero").appendTo(this.$element)
            this.zeroTable.add("magic", "?????????", 100, "purple")
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
            this.log("???????????????")
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
                this.log("????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????")
                this.log("?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????")
                this.log("???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????A???????????????B???????????????C???????????????D???????????????????????????????????????????????????????????????????????????????????????")
                this.choose(["??????", "??????"], ch => this.prepare(ch))
            } else {
                this.round()
            }
        }
        
        round() {
            this.log("??????" + (this.rounds + 1))
            
            this.defense = false
            
            this.battleMagic = false
            
            this.heavyAttack = false
            
            this.fightTimes = 1
            
            this.roundEndCallback = []
            if (this.game.armor === 23) { // ????????????
                this.game.execute("health + [3,20]")
            }
            switch (this.enemy.id) {
                case 7: // CRD
                    if (this.rounds === 9) {
                        
                        this.log("CRD?????????????????????????????????????????????????????????????????????????????????")
                        this.wait(() => {
                            this.log("???????????????????????????")
                            return this.game.battle(8, this)
                        })
                        this.wait(() => {
                            this.log("???????????????????????????")
                            return this.game.battle(8, this)
                        })
                    }
                    break;
                case 8: // ??????
                    if (this.rounds === 6) {
                        this.game.achieve(2)
                    }
                    break;
                case 10: // ?????????
                case 11:
                    if (this.rounds % 5 === 4) {
                        this.log("??????????????????????????????ATT????????????5???")
                        this.enemy.attack += 5
                        this.roundEnd(() => this.enemy.attack -= 5)
                    }
                    break;
                case 13: // ????????????
                    if (this.enemy.health < 400) {
                        this.log('???????????????HP????????????')
                        this.log('?????????????????????????????????????????????????????????HP?????????70??????')
                        if (this.enemy.fixed == false) {
                            this.log('????????????????????????????????????????????????????????????')
                            this.log('???Zero???????????????????????????????????????????????????????????????')
                            this.log('?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????Zero???????????????????????????????????????????????????????????????????????????????????????????????????')
                            // @ts-ignore
                            this.enemyTable.gunHealth.show()
                            this.enemy.fixed = true
                        }
                        this.enemy.health += 70
                    }
                    if (this.heavyAttack = this.rounds % 5 === 4) {
                        this.log("???????????????????????????????????????????????????")
                        this.enemy.attack += 20
                        this.roundEnd(() => this.enemy.attack -= 20)
                    } else if (this.rounds % 5 === 0 && this.rounds > 0) {
                        this.log("?????????????????????????????????????????????")
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
            this.choose(["??????", "??????", "??????", "??????"], ch => this.prepare(ch))
        }
        
        prepare(ch) {
            if (this.tutorial) {
                if (ch === 0) {
                    this.defense = true
                    this.log("????????????????????????????????????????????????")
                    this.log("???????????????????????????????????????????????????")
                    this.log("???????????????A???B???C???D?????????????????????????????????????????????????????????D???A???B???C???D?????????????????????????????????AAAAA???????????????DDDDD?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????")
                    this.choose(["DDDDD", "?????????????????????"], ch => this.fight(ch))
                } else if (ch === 1) {
                    this.log("???????????????????????????????????????????????????")
                    this.log("????????????????????????????????????????????????????????????")
                    this.log("???????????????A???B???C???D?????????????????????????????????????????????????????????D???A???B???C???D?????????????????????????????????AAAAA???????????????DDDDD??????????????????")
                    this.choose(["DDDDD", "?????????????????????"], ch => this.fight(ch))
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
                        this.log("???????????????????????????")
                        return this.prepareChoose()
                    }
                    this.log("?????????????????????")
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
                    this.log("?????????????????????")
                    this.defense = true
                    this.magic += 40
                    break;
                case 2:
                    // ??????????????????????????????????????????????????????????????????????????????
                    if (this.magic === 0 || (!this.octahedron && this.magic < this.cureMagicCost)) {
                        this.log("????????????????????????")
                        return this.prepareChoose()
                    }
                    this.magicChoose()
                    break;
                case 3:
                    this.log("?????????????????????")
            }
            // ??????boss J12132????????????
            if (this.enemy.id === 14 && !this.defense) { // ??????
                if (this.chaoAttacked == false && (this.chaos >= 85 || this.enemy.health <= 1400)) {
                    this.log('???????????????????????????????????????????????????')
                    this.log('??????????????????????????????????????????')
                    this.log('J12132???????????????????????????????????????')
                    this.withXk = false
                    this.octahedron = false
                    this.chaoAttacked = true
                    this.fightTimes = 2
                    this.enemy.attack += 5
                    this.game.virtually(12133)
                    this.roundEnd(() => {
                        this.enemy.attack -= 5
                    })
                } else { // ????????????????????????????????????????????????
                    switch (Math.floor(Math.random() * 4)) {
                        case 0:
                            this.log("????????????????????????????????????")
                            this.game.waitChoose(this, ["??????", "??????"], ch => {
                                if (ch == 0) {
                                    this.chaos += randInt(3,5)
                                    this.enemy.health += randInt(10,50)
                                } else {
                                    this.log('????????????????????????????????????????????????????????????')
                                    this.chaos += 1
                                }
                            })
                            break
                        case 1: // ???????????????????????????
                            this.log('????????????????????????????????????')
                            this.game.waitChoose(this, ["??????", "??????"], ch => {
                                if (ch == 0) {
                                    this.chaos += randInt(3,4)
                                    let attack = this.game.attack
                                    this.game.attack = 0
                                    this.roundEnd(() => this.game.attack = attack)
                                } else {
                                    this.log('????????????????????????')
                                    this.chaos += 2
                                }
                            })
                            break
                        case 2:
                            this.log('????????????????????????????????????')
                            this.game.waitChoose(this, ["??????", "??????"], ch => {
                                if (ch == 0) {
                                    this.chaos += 2
                                    this.game.health -= randInt(5,35)
                                } else {
                                    this.log('????????????????????????????????????')
                                    this.chaos += randInt(1,5)
                                    this.game.attack -= 10
                                    this.roundEnd(() => this.game.attack += 10)
                                }
                            })
                            break
                        case 3:
                            this.log('????????????????????????????????????')
                            this.game.waitChoose(this, ["??????", "??????"], ch => {
                                if (ch == 0) {
                                    this.chaos += randInt(2,3)
                                    this.enemy.attack += 5
                                    this.roundEnd(() => this.enemy.attack -= 5)
                                } else {
                                    this.log('????????????????????????????????????????????????????????????????????????')
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
                    .html("?????????")
                    .appendTo($attack)
                    .on("click", () => attack())
            })
        }
        
        magicChoose() {
            this.log("?????????????????????")
            this.wait(500)
            
            let magics = [`???????????????${this.cureMagicCost}???`, "???????????????70???", `???????????????${this.black ? "100" : "???"}???`]
            if (this.octahedron) { // ?????? ??????????????? enabled
                magics.push("????????????????????????????????????????????????????????????")
            }
            var ok = false
            const chooseMagic = () => 
            this.game.Process((proc) => {
                proc.choose(magics, ( magic) => {
                    this.game.Process((process) => {
                        switch (magic) {
                            case 0:
                                if (this.magic < this.cureMagicCost) {
                                    process.log("????????????????????????")
                                    return
                                }
                                process.log(`???????????????????????????HP??????${this.cureMagicPlus}`)
                                this.magic -= this.cureMagicCost
                                this.game.health += this.cureMagicPlus
                                break;
                            case 1:
                                if (this.magic < 70) {
                                    process.log("????????????????????????")
                                    return
                                }
                                process.log(`???????????????????????????Att??????5?????????????????????`)
                                this.battleMagic = true
                                this.magic -= 70
                                this.game.attack += 5
                                break;
                            case 2:
                                if (this.black) {
                                    if (this.magic < 100) {
                                        process.log("????????????????????????")
                                        return
                                    }
                                    process.log("??????????????????????????????????????????????????????")
                                    this.magic = 0
                                    this.enemy.health = 0
                                } else {
                                    process.log("l????????????????????????????????????????????????????????????????????c????????????????????????????k??????????????????????????????????e????????????????????????d??????????????????????????????????????????")
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
                                process.log(`????????????????????????????????????${this.enemy.name}?????????${currentMagic / 2}????????????`)
                                break;
                            default:
                                throw new Error("????????????")
                            
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
            var same; // ???????????????????????????
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
                    // ????????????
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
                    this.log("?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????")
                } else {
                    this.log("????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????")
                    this.game.execute("health + 240")
                }
                this.tutorial = false // ????????????
            } else if (typeof str === "string") {
                let enemyDefense = Math.random() < this.enemy.defenseRate
                let enemyDefence = enemyDefense ? this.enemy.defence : 0
                let [hurt, letters, harm] = Battle.computeHurtHarm(
                    str, // ????????????
                    this.defense ? 0 : (this.game.attack - enemyDefence), // ???????????????
                    this.enemy.attack, // ??????????????????
                    this.defense, // ????????????
                    this.game.defence, // ???????????????
                    this.game,
                    this.enemy.id === 13 && this.heavyAttack ? 0.3 : 0, // ?????????
                    this
                    )
                this.log(`???????????????${str}?????????????????????${letters}`)
                if (enemyDefense) {
                    this.log(`${this.enemy.name}??????????????????`)
                }
                this.log(`?????????${hurt}?????????`)
                this.game.health -= hurt
                this.log(`????????????${harm}?????????`)
                this.enemy.health -= harm
                if (this.withXk) {
                    let xkHarm = enemyDefence < 20 ? 20 - enemyDefence : 0
                    this.log(`???????????????${xkHarm}?????????`)
                    this.enemy.health -= xkHarm
                }
                this.fightTimes--
                if (this.fightTimes > 0) {
                    return this.fightInput() // ?????????????????????
                }
                if (this.enemy.fixed && this.heavyAttack && harm > 0) {
                    this.log("??????????????????????????????????????????????????????")
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
                this.log('????????????????????????????????????????????????')
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
            if (this.id === 13) { // ????????????
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
                    this.battle.log("???????????????????????????????????????????????????????????????????????????????????????")
                    this.game.achieve(3)
                    this._setHealth(this._health + 200)
                }
                return
            } else if (this.id === 14) {
                if (val <= 0) { // J12132????????????
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
                this.battle.log("?????????????????????????????????????????????")
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
            this.$settings = Game.button().html("??????").on("click", () => this.settingsMenu()).appendTo(this.$interface)
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
                if (data[i]) { // ????????????????????????
                    $chapter.html("Chapter " + i).on("click", () => {
                        
                        this.chapter = i
                        $chapters.fadeOut(() => {
                            $chapters.remove()
                            this.run()
                        })
                    })
                } else { // ??????????????????
                    $chapter.addClass("ate-chapter-locked").html("locked")
                }
            }
        }
        
        run() {
            this.$save = Game.button().html("??????").on("click", () => this.save()).appendTo(this.$interface)
            this.table = new Table("ate-vals", "?????????").appendTo(this.$interface)
            this.$items = $("<div/>").addClass("ate-items").appendTo(this.$interface)
            this.$equipments = $("<div/>").addClass("ate-equipments").appendTo(this.$interface)
            this.$message = $("<div/>").addClass("ate-messages").appendTo(this.$interface)
            this.$battle = $("<div/>").addClass("ate-battle").appendTo(this.$interface)
            this.$buttons = $("<div/>").addClass("ate-choices").appendTo(this.$interface)
            this.$weapon = $("<div/>").appendTo(this.$equipments)
            this.$armor = $("<div/>").appendTo(this.$equipments)
            this.$armor.append($("<span/>").addClass("ate-item-name").html("??????"))
            this.$weapon.append($("<span/>").addClass("ate-item-name").html("??????"))
            this.table.add("health", "HP", data[this.chapter].maxHealth, "green")
            this.table.add("attack", "Att")
            this.table.add("defence", "Def")
            this.table.add("cm", "CM???")

            
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
                for (let each of this.items) { // ????????????Zes????????????of??????in
                	this._add(each) // ??????parseInt, Game.items???number[]
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
            if ("attack" in itemData && itemData.attack || itemData.id === 24) { // ??????
                this.weapon = item
            } else if ("defence" in itemData && itemData.defence) {
                this.armor = item
            } else {
                throw new Error("????????????")
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
                    items.push("????????????")
                    this.waitProcess(process, p => {
                        p.log("????????????????????????")
                        p.choose(items, ( i) => {
                            if (i === this.max) { // ????????????
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
                        p.log(`??????${itemData.name}?????????????????????`)
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
                throw new Error("??????????????????")
            }
            this.addImage($item, item)
        	$item.append($("<span/>").addClass("ate-item-name").html(itemData.name))
        	var $des = $("<span/>").addClass("ate-item-description").appendTo($item)
            var $desDiv = $("<div/>").html(itemData.description).appendTo($des)
            if (itemData.stackable) {
                $desDiv.append(`<br>??????<span class="ate-item-amount">${this.stackables[item]}</span>???`)
            }
            if ("attack" in itemData || "defence" in itemData || item === 24) {
                var $button = Game.button().html("??????").appendTo($desDiv)
                $button.on("click", () => {
                    this.putOn(item)
                })
            }
            var pos = this.items.length - 1
            Game.button().html("??????").appendTo($desDiv).on("click", () => {
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
            $items.eq(index).html("").css("backgroundImage", "").appendTo(this.$items) // ??????????????????$items??????????????????
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
                        this.$message.append($("<span/>").html("???????????????").css("font-size", "50%"))
                        this.$message.one("click", () => deferred.resolve())
                        return deferred
                    })
                }
                if (typeof to === "number") {
                    this.wait(() => this.exp(to))
                } else if (Array.isArray(to)) {
                    this.wait(() => this.exp(this.judgeArr(to)))
                } else {
                    this.log("???????????????")
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
                // ????????????
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
            for (let index in choices) { // index ???????????????????????????
                let $btn = $("<div/>").addClass("ate-choice").html(choices[index]).appendTo($choices);
                $btn.on("click", () => {
                    setTimeout(() => $choices.remove());
                    $(".ate-choices > *").show()
                    callback.call(choices, parseInt(index))
                })
                if (fade && fade.includes(parseInt(index))) { // ????????????????????? 2022/11/17
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
                return void this.notify("??????????????????")
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
            this.notify("????????????")
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
                    p.log(`???????????????${str}???${name}????????????${letters}???`)
                    p.log(`????????????${hurt}`)
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
                let $button = Game.button().html("?????????").appendTo($attack).on("click", () => dodge())
            })
        }
        bridge() {
            this.log("????????????????????????")
            const makeBridge = () => this.Process((process) => process.choose(["A", "B", "C"], ( ch) => {
                var noBridge = Math.floor(Math.random() * 3)
                var bridges = ["A", "B", "C"]
                if (ch === noBridge) {
                    bridges.splice(noBridge, 1)
                    process.log(`????????????????????????${bridges.join()}?????????????????????`)
                    process.die(makeBridge())
                } else {
                    process.log("??????????????????")
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
                    items.push(data.items[item].name + ` [cost CM???${price}???]`)
                }
                var leaveKey = items.length
                items.push("??????")
                p.choose(items, ( ch) => {
                    if (ch === leaveKey) {
                        return p.die(this)
                    }
                    if (this.items.length === this.max) {
                        p.log("???????????????????????????????????????")
                        return p.die()
                    }
                    var bought = parseInt(itemIds[ch])
                    if (prices[bought] > this.cm) {
                        p.log("??????CM????????????")
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
            this.log("?????????????????????")
            if (this.has(2)) {
                this.log("??????????????????????")
                this.choose(["???", "???"], (ch) => {
                    if (!ch) {
                        this.setStackableAmount(2, this.stackables[2] - 1)
                        this.health = 100
                        this.log("?????????????????????????????????")
                    } else {
                        this.log("????????????????????????????????????")
                        this.log("You died.")
                        delete localStorage.gameData
                    }
                })
            } else {
                this.log("????????????????????????????????????")
                this.log("????????????????????????????????????")
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
                // ??????????????????????????????
                return
            }
            var $window = $("<div/>")
                .addClass("ate-settings")
                .appendTo(this.$interface)
            // ?????????????????????????????????????????????????????????
            var $cover = $("<div/>")
                .addClass("ate-cover")
                .appendTo(this.$interface) 
            var $list = $("<ul/>").appendTo($window)


            var $speed = $("<input>")
                .attr("type", "text")
                .val(this.settings.get("speed"))
                .appendTo($("<li/>").html("??????????????????/ms").appendTo($list))
            
            var pass = this.settings.get("pass")
            var $pass = Game.button(pass && "on")
                .html(pass ? "???" : "???")
                .appendTo($("<li/>").html("????????????????????????").appendTo($list))
            $pass.on("click", () => {
                $pass.html(this.settings.get("pass") ? "???" : "???")
                this.settings.toggle("pass")
                $pass.toggleClass("ate-button-on")
            })

            var random = this.settings.get("random")
            var $random = Game.button(random && "on")
                .html(random ? "???" : "???")
                .appendTo($("<li/>").html("????????????????????????").appendTo($list))
            $random.on("click", () => {
                $random.html(this.settings.get("random") ? "???" : "???")
                this.settings.toggle("random")
                $random.toggleClass("ate-button-on")
            })

            if (this.history) {
                Game.button("negative").html("??????").appendTo($window).on("click", () => {
                    delete localStorage.gameData
                    this.notify("??????????????????")
                })
                $window.append("<div>???????????????</div>")
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
            $("<div/>").addClass("ate-achievement-title").html("?????????" + achievement.name).appendTo($achivement)
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


    	document.title = "?????? Extend Air Ticket"
    	$("#firstHeading").html(`--- Extend Air Ticket v ${version} ---`)
        $("#version").html(version)

})(jQuery, ateData, "2.12.1.32 Beta")

