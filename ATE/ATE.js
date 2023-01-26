//@ts-check
"use strict";
//import "./types-ate/index.d.ts"




(function ($, /** @type {GameData} */data, version) {
    const LOVECA = 2
    const SW0RD = 24
    const FROZEN_BREAD = 34
    const H_3RD_ANN_CAKE = 44
    const BLOOD_STONE = 48
    const DESTROYER_LASER = 65
    /**
     * 生成一个[start, end]间的随机整数
     * @param {number} start
     * @param {number} end
     */
    function randInt(start, end) {
        return start + Math.floor(Math.random() * (end - start + 1))
    }
    /**
     * @param {string} str
     */
    function intOrScope(str) {
        if (str.startsWith("[") && str.endsWith("]")) {
            let scope = str.slice(1,-1).split(",")
            return randInt(parseInt(scope[0]), parseInt(scope[1]))
        } else {
            return parseInt(str)
        }
    }
    class Input {
        /**
         * 
         * @param {Game} game 
         * @param {string[]} chars 
         * @param {(val: string) => boolean} checkFn 
         * @param {(val: string, input: Input) => void} processFn
         */
        constructor(game, chars, checkFn, processFn) {
            this.$element = game.$input
            this.$input = $("<input/>").attr("type", "text")
                .appendTo(this.$element)
                .on("keypress", (e) => {
                    if (e.which === 13) {
                        const VAL = this.getValue()
                        if (!checkFn(VAL)) {
                            return;
                        }
                        processFn(VAL, this)
                    }
                })
            this.$shoot = Game.button("走你")
                .appendTo(this.$element)
                .on("click", () => {
                    const VAL = this.getValue()
                    if (!checkFn(VAL)) {
                        return;
                    }
                    processFn(VAL, this)
                })
            for (let each of chars) {
                Game.button(each, {margin: "10px", padding: "16px"})
                    .appendTo(this.$element)
                    .on("click", () => this.setValue(this.getValue() + each))
            }
            this.$element.append("<br>")
                this.$clear = Game.button("清除", {cls: "negative"})
                    .appendTo(this.$element)
                    .on("click", () => this.setValue(""))
        }
        /**
         * 
         * @param {string} val 
         * @returns {this|string}
         */
        setValue(val) {
            this.$input.val(val)
            return this
        }
        /**
         * 
         * @returns {string}
         */
        getValue() {
            // @ts-ignore

            return this.$input.val()
        }
        remove(){
            this.$element.html("")
        }
    }
    class TableItem {
        /**
         * @param {string} name
         * @param {string} [color]
         * @param {Table} table
         * @param {number} [full]
         */
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
                    .insertAfter(this.$val)
                if (color.startsWith("linear-gradient")) {
                    this.$rate.css("backgroundImage", color)
                } else {
                    this.$rate.css("backgroundColor", color)
                }
            }
        }
        /**
         * 展示标题和值
         */
        show() {
            this.$valCell.fadeIn()
            this.$title.fadeIn()
        }
        /**
         * 隐藏标题和值
         */
        hide() {
            this.$valCell.hide()
            this.$title.hide()
        }
        /**
         * 设置该项目的值。如果有满值，会设定比率可视化。
         * @param {number} val
         */
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
        /**
         * 
         * @param {string} cls 
         * @param {string} head
         */
        constructor(cls, head) {
            this.$outer = $("<div/>").addClass(cls)
            var $table = $("<table/>").addClass("ate-info").appendTo(this.$outer)
            var $tbody = $("<tbody/>").appendTo($table)
            this.$tr = $("<tr/>").appendTo($tbody)
            this.$th = $("<th/>").html(head).appendTo(this.$tr)
            /** @type {TableItem} */
            this.health = null
            /** @type {TableItem} */
            this.magic = null
            /** @type {TableItem} */
            this.attack = null
            /** @type {TableItem} */
            this.defence = null
            /** @type {TableItem} */
            this.cm = null
            /** @type {TableItem} */
            this.gunHealth = null
            /** @type {TableItem} */
            this.chaos = null
            /** @type {TableItem} */
            this.rules = null
        }
        /**
         * 添加一项
         * @param {"health"|"magic"|"attack"|"defence"|"cm"|"gunHealth"|"chaos"|"rules"} key 表中的键
         * @param {string} name 在页面上显示的内容
         * @param {number} [full] 最大值
         * @param {string} [color] 可视化颜色
         * @param {boolean} [hidden] 是否默认隐藏
         */
        add(key, name, full, color, hidden) {
            var tableItem = new TableItem(name, this, color, full)
            if (hidden) {
                tableItem.hide()
            }
            this[key] = tableItem
            return this
        }
        /**
         * @param {JQuery<HTMLElement>} ele
         */
        appendTo(ele) {
            this.$outer.appendTo(ele)
            return this
        }
        remove() {
            this.$outer.remove()
            return this
        }
    }
    class Settings {
        /**
         * 
         * @param {Game} game 
         */
        constructor(game) {
            this.game = game
            this.values = localStorage.ateSettings ? JSON.parse(localStorage.ateSettings) : {
        		speed: 1500,
                pass: false,
                random: false,
                playwhenhidden: false
        	}
            this.opened = false
            this.hidden = true
            this.$element = $(".ate-settings").hide()
            /** 半透明灰遮罩阻止用户在关闭之前操作游戏 */
            this.$cover = $("<div/>")
                .addClass("ate-cover")
                .appendTo(this.game.$interface)
                .hide()
            this.$tags = $(".ate-settings-tag")
            this.$pages = $(".ate-settings-page")
            this.index = 0
            this.$tags.each((index, tag) => {
                let $tag = $(tag)
                $tag.on("click", () => {
                    if (index === this.index) {
                        return;
                    }
                    this.$tags.eq(this.index).removeClass("ate-settings-tag-show")
                    this.$pages.eq(this.index).removeClass("ate-settings-page-show")
                    this.index = index
                    this.$tags.eq(index).addClass("ate-settings-tag-show")
                    this.$pages.eq(index).addClass("ate-settings-page-show")
                })
            })
            for (let key of ["pass", "random", "playwhenhidden"]) {
                let $btn = $("#ate-settings-" + key)
                let val = this.get(key)
                if (val) {
                    $btn.addClass("ate-button-on")
                }
                $btn.html(val ? "是" : "否").on("click", () => {
                    val = !val
                    this.toggle(key)
                    $btn.html(val ? "是" : "否").toggleClass("ate-button-on")
                })
            }
            $("#ate-settings-clear").on("click", () => {
                delete localStorage.gameData
                this.game.notify("存档已清除！")
            })
            /** 展示区 */
            this.$export = $("#ate-export")
            this.$doneButton = $(".ate-settings-done")
            this.$speed = $("#ate-settings-speed").val(this.get("speed"))
        }
        /**
         * @param {string} key
         */
        get(key) {
            return this.values[key]
        }
        /**
         * @param {string} key
         * @param {any} [val]
         */
        set(key, val) {
            this.values[key] = val
            localStorage.ateSettings = JSON.stringify(this.values)
        }
        /**
         * @param {string} key
         */
        toggle(key) {
            this.set(key, !this.get(key)) // 我是啥b
        }
        open() {
            if (!this.hidden) {
                return
            }
            this.opened = true
            this.hidden = false
            /** base64编码后再展示的数据，避免太容易被用户修改（ */
            var storage = btoa(localStorage.gameData || "")
            this.$export.val(storage)
            this.$doneButton.one("click", () => {
                if (!this.opened) {
                    return
                }
                this.opened = false
                const SPEED_VAL = this.$speed.val()
                if (typeof SPEED_VAL !== "string") {
                    throw new Error("$speed.val() is a str")
                }
                if (SPEED_VAL.match(/^\d+$/)) {
                    this.set("speed", parseInt(SPEED_VAL))
                }
                const IMPORT_VAL = this.$export.val()
                if (typeof IMPORT_VAL !== "string") {
                    throw new Error("$sxport.val() is a str")
                }
                if (IMPORT_VAL !== storage) {
                    try {
                        localStorage.gameData = atob(IMPORT_VAL)
                    } catch (e) {
                        this.game.notify("存档不合法！")
                    }
                }
                // 窗口往左飘走
                this.$element.animate({left: "-100%"}, 3000, () => {
                    this.$element.hide()
                    this.hidden = true
                })
                // 移除遮罩
                this.$cover.hide()
            })
            // 播放过的消息
            if (this.game.history) {
                var $history = $(".ate-history").html("")
                for (let each of this.game.history) {
                    $("<li/>").html(each).appendTo($history)
                }
            }
            this.$cover.show()
            this.$element.css("left", "").show()
        }
    }
    class Queue {
        /**
         * 队列，只在游戏初始化时实例化
         * @param {Game} game 
         */
        constructor(game) {
            /**
             * @type {JQuery.PlainObject<WaitFn[]>}
             */
            this.arrays = {}
            /** 转交以前该进程处理到的位置 */
            this.cachedIndexes = {}
            /** 是否正在处理任务 @type {boolean} */
            this.processing = false
            Queue.newid(game)
            this.give(game)
        }
        /**
         * @param {WaitFn} fn 等待的回调函数。如果返回Promise，将在resolve时执行下个任务。若无返回值，直接执行下个任务。
         * @param {P} cur 加入任务的进程。如果进程已经停运或者没有注册，不会推入。
         */
        push(fn, cur) {
            if (cur.dead || !(this.arrays[cur.id])) {
                return
            }
            this.arrays[cur.id].push(fn)
            if (! this.processing) {
                this.process()
            }
        }
        /**
         * 内部方法，用于启动队列。
         * @private
         * @returns {void}
         */
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
        /**
         * 把队列控制权转交给某进程。队列会转而执行该进程派发的任务。
         * 如果该进程没有注册在队列实例中，会进行注册。
         * @param {P} process 
         */
        give(process) {
            /** @type {number} */
            this.owner = process.id
            if (process.dead) {
                return;
            }
            if (!(this.arrays[process.id])) {
                this.arrays[process.id] = []
            }
            if (!this.processing) {
                this.process()
            }
        }
        /**
         * 将id加给进程，并把进程注册到静态属性。
         * @param {P} obj 
         */
        static newid(obj) {
            Queue.registeredOwners.push(obj)
            obj.id = Queue.curid
            Queue.curid++
        }
        /**
         * 当前控制队列的进程。
         * @returns {P}
         */
        now() {
            return Queue.registeredOwners[this.owner]
        }
    }
    /**
     * @type {P[]}
     */
    Queue.registeredOwners = []
    Queue.curid = 0
    // 不用public static field，兼容性不好（
    class Process {
        /**
         * 
         * @param {(process: Process)=>void} func 
         * @param {Game} game 
         */
        constructor(func, game) {
            if (!game) throw new Error("Missing param game")
            this.id = -1
            Queue.newid(this)
            this.func = func
            this.dead = false
            this.game = game
        }
        /**
         * 执行进程
         */
        go() {
            this.game.queue.give(this)
            this.func(this)
        }
        /**
         * 以该进程签名发出消息。
         * @param {string} msg
         */
        log(msg) {
            this.game.log(msg, this)
        }
        /**
         * 以该进程签名向队列加入回调函数。
         * @param {WaitFn} fn
         */
        wait(fn) {
            this.game.queue.push(fn, this)
        }
        /**
         * 以该进程签名进行选择。
         * @param {any[]} choices
         * @param {(choice: number) => void} callback
         */
        choose(choices, callback) {
            this.wait(() => this.game._choose(choices, callback))
        }
        /**
         * 停止该进程，将队列所有权转交给后继者。
         * @param {CBP} after 要转交的后继者
         */
        die(after) {
            this.dead = true
            delete Queue.registeredOwners[this.id]
            // 使GC正确执行（
            if (after) this.game.queue.give(after)
        }
        /**
         * 将停止的任务以自身签名加入队列。
         * 队列将在本进程之前任务全部完毕后停运该进程。
         * @param {CBP} after 转交后继者
         */
        waitDie(after) {
            this.wait(() => this.die(after))
        }
    }
    class Item {
        /**
         * @param {number} id
         * @param {Game} game
         * @param {number} amount
         * @param {JQuery<HTMLElement>} $element
         */
        constructor(id, game, $element, amount) {
            this.game = game
            var itemData = data.items[id]
            this.id = id
            this.name = itemData.name
            this.description = itemData.description
            this.stackable = itemData.stackable
            this.throwable = itemData.throwable
            if ("battle" in itemData && itemData.battle) {
                this.battle = true
                this.use = itemData.use
                if ("cd" in itemData) {
                    this.cd = itemData.cd
                }
                this.type = Item.BATTLE
            } else if ("attack" in itemData) {
                this.attack = itemData.attack
                if ("magic" in itemData) {
                    this.magic = itemData.magic
                }
                this.type = Item.WEAPON
            } else if ("defence" in itemData) {
                this.defence = itemData.defence
                if ("dodgeRate" in itemData) {
                    this.dodgeRate = itemData.dodgeRate
                }
                this.type = Item.ARMOR
            } else {
                this.type = Item.NORMAL
            }
            this.loadUI($element)
            if (this.stackable) {
                this.amount = amount
            }
        }
        // @ts-ignore
        get amount() {
            return this._amount
        }
        /**
         * @param {number} val
         */
        // @ts-ignore
        set amount(val) {
            if (this.id === BLOOD_STONE) {
                this.game.defence += val - this._amount
            }
            if (val === 0) {
                this.game.removeItem(this)
                return
            }
            this.$descriptionAmount.html(val + "")
            this.$amount.html(val === 1 ? "" : val + "")
            this._amount = val
        }
        /**
         * @param {JQuery<HTMLElement>} $element
         */
        loadUI($element) {
            this.$element = $element
            $element.html("")
            this.game.addImage($element, this)
        	$element.append($("<span/>").addClass("ate-item-name").html(this.name))
        	var $des = $("<span/>").addClass("ate-item-description").appendTo($element)
            var $desDiv = $("<div/>").html(this.description).appendTo($des)
            console.log("test", $element, $des)
            if (this.stackable) {
                this.$amount = $("<span/>")
                    .addClass("ate-item-amount")
                    .appendTo(this.$element)
                this.$descriptionAmount = $("<span/>")
                $desDiv.append("<br>你有")
                    .append(this.$descriptionAmount)
                    .append("个")
            }
            if (this.type == Item.ARMOR && this.game.armor !== this
                || this.type == Item.WEAPON && this.game.weapon !== this) {
                var $button = Game.button("装备").appendTo($desDiv)
                $button.on("click", () => {
                    this.game.equip(this)
                })
            }
            if (this.throwable != false) {
                Game.button("丢弃").appendTo($desDiv).on("click", () => {
                    if (this.game.armor !== this && this.game.weapon !== this) {
                        this.game.removeItem(this)
                    }
                })
            }
        }
    }
    Item.NORMAL = 0
    Item.BATTLE = 1
    Item.WEAPON = 2
    Item.ARMOR = 3
    class Battle {
        /**
         * 
         * @param {BattleData} battleData 
         * @param {Game} game 
         * @param {P} after
         */
        constructor(battleData, game, after) {
            console.log(this)
            this.id = -1
            Queue.newid(this)
            game.queue.give(this)
            this.game = game
            /** 是否处于教程阶段 */
            this.tutorial = battleData.tutorial
            /** 是否有星空伴随 */
            this.withXk = battleData.withXk
            /** 是否可使用几何八面体 */
            this.octahedron = battleData.octahedron
            /** 治疗魔法消耗的MP */
            this.cureMagicCost = this.game.has(14) ? 50 : 30
            /** 治疗魔法增加的HP */
            this.cureMagicPlus = this.game.has(14) ? 80 : 40
            /** div class="ate-battle" */
            this.$element = game.$battle
            /** 决定战斗完成后队列转交给哪个进程 */
            this.after = after
            /** 预定某一回合执行的指令。键为数字值为数组。 */ 
            this.deferredCommands = {}
            /** 是否已经胜利 */
            this.won = false
            /** 胜利后要执行的指令 */
            this.afterWin = battleData.win
            this.$element.children().fadeOut() // CRD 战斗中短矛子战隐藏母战斗
            var enemy = battleData.enemy
            if (Array.isArray(enemy)) {
                this.multiEnemy = true
            } else {
                enemy = [enemy]
            }
            this.aliveEnemyAmount = enemy.length
            this.enemy = []
            for (let each of enemy) {
                let enemyData = data.enemy[each]
                let thisEnemy = new Enemy(enemyData, this)
                this.enemy.push(thisEnemy)
            }
            
            this.zeroTable = new Table("ate-zero-table", "Zero").appendTo(this.$element)
            this.zeroTable.add("magic", "魔法值", 100, "purple")
            this.game.toggleExpand()
            /** 魔法值 */
            this.magic = 0
            /** 当前回合数 - 1 */
            this.rounds = 0;
            this.intenseFight = null;
        }
        /**
         * 使战斗胜利并转交队列给游戏实例。
         * @returns {void}
         */
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
            
            this.game.toggleExpand()
            setTimeout(() => {
                this.zeroTable.remove()
            }, 2000)
            
            this.$element.children().fadeIn()
            this.wait(() => {
                this.game.queue.give(this.after)
                this.dead = true
            })
        }
        /**
         * 以战斗签名发出消息。
         * @param {string} msg
         */
        log(msg) {
            this.game.log(msg, this)
        }
        /**
         * 以战斗签名推入回调函数，或推入等待若干毫秒的回调函数。
         * @param {number|WaitFn} fn
         */
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
        /**
         * 将选择以战斗签名推入
         * @param {string[]} choices 
         * @param {(ch: number) => void} callback 
         */
        choose(choices, callback) {
            this.wait(() => this.game._choose(choices, callback))
        }
        /**
         * 运行战斗
         */
        run() {
            if (this.tutorial) {
            	/**
                 * @type {((game?: Game)=>any)[]}
                 */
            	this.roundEndCallback = []
                this.log("星空说：“让我描述详细一点吧，在魔法系统下，战斗就是我们的【魔法核心】相互接触的过程，每个人都有一个【魔法核心】，只不过大多数人都不会用罢了，我来教你怎么使用。")
                this.log("星空跟你详细说明了使用魔法核心的方法，你试了一下，突然你感觉世界一下就改变了！")
                this.log("星空：现在我们进入了战斗界面！当你听完我的这些话后，就可以加入战斗了。战斗分为准备阶段和对战阶段，在准备阶段时，你可以尝试A【物品】、B【防御】、C【魔法】、D【跳过】，不过你现在没有魔法值，没有物品，选择【防御】吧。")
                this.choose(["防御", "跳过"], ch => this.prepare(ch))
            } else {
                this.round()
            }
        }
        /**
         * 开始一回合
         */
        round() {
            this.log("回合" + (this.rounds + 1))
            /** 是否防御 */
            this.defense = false
            /** 是否启用战斗魔法 */
            this.battleMagic = false
            /** 机械木马是否发动重火力攻击 */
            this.heavyAttack = false
            /** 本回合需要攻击的次数（散弹攻击等设定为2） */
            this.fightTimes = 1
            this.breakHarm = false
            this.frozenBreadUsed = false
            /**
             * 回合结束后执行的回调函数
             * @type {((game?: Game)=>any)[]}
             */
            this.roundEndCallback = []
            if (this.deferredCommands[this.rounds]) {
                for (let command of this.deferredCommands[this.rounds]) {
                    this.game.execute(command, this)
                }
            }
            if (this.game.armor && this.game.armor.id === 23) { // 混乱护盾
                this.game.execute("health + [3,20]")
            }
            for (let enemy of this.enemy) {
                enemy.round()
                if (enemy.message) {
                    let message = enemy.message
                    /** 消息可以是包含随机消息数组的条件表达式或随机消息数组 */
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
            }
            this.wait(() => this.prepareChoose())
        }
        /**
         * 准备阶段以前的四选一
         */
        prepareChoose() {
            this.choose(["物品", "防御", "魔法", "跳过"], ch => this.prepare(ch))
        }
        /**
         * 准备阶段
         * @param {number} ch
         */
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
                    if (this.enemy[0].id === 6 && Math.random() < 0.5) {
                        this.log("四面体向你的背包里发射了一颗能量球，你受到了15点伤害！")
                        this.game.health -= 15
                    }
                    /**
                     * 可用于战斗的道具
                     * @type {number[]}
                     */
                    let battlables = []
                    for (let index in this.game.items) {
                        let item = this.game.items[index]
                        if (item.battle) {
                            battlables.push(parseInt(index))
                        }
                    }
                    if (battlables.length === 0) {
                        this.log("你没有可用的物品。")
                        return this.prepareChoose()
                    }
                    this.log("选择一项物品。")
                    this.game.waitProcess(this, (itemSubProcess) => {
                        for (let index of battlables) {
                            // console.log(index, this.game.$items.eq(parseInt(index)))
                            this.game.$items.children().eq(index).css("boxShadow", "2px 2px 4px 4px #66ccff").on("click", () => {
                                if (this.enemy[0].id === 8 && this.game.items[index].id === H_3RD_ANN_CAKE) {
                                    this.game.achieve(4) // “大材小用”成就
                                    // 真的有人能拿着蛋糕打短矛吗？
                                }
                                this.game.use(index, this, itemSubProcess)
                                this.game.$items.children().css("boxShadow", "").off("click")
                                itemSubProcess.waitDie(this)
                            })
                        }
                    })
                    if (this.enemy[0].id === Enemy.LORCE) {
                        this.rules += randInt(2, 5)
                    }
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
                    if (this.enemy[0].id === 17) {
                        this.magicChooseForLorce()
                        break;
                    }
                    this.magicChoose()
                    break;
                case 3:
                    this.log("你选择了跳过。")
            }
            // 隐藏boss J12132特殊技能
            if (this.enemy[0].id === 14 && !this.defense) { // 大招
                if (this.chaoAttacked == false && (this.chaos >= 85 || this.enemy[0].health <= 1400)) {
                    this.log('混沌持续上升！战斗已经进入白热化！')
                    this.log('现在，你需要独自一人面对考验')
                    this.log('J12132正在释放一次“混沌冲击！”')
                    this.withXk = false
                    this.octahedron = false
                    this.chaoAttacked = true
                    this.fightTimes = 2
                    this.enemy[0].attack += 5
                    this.game.virtually(12133)
                    this.roundEnd(() => {
                        this.enemy[0].attack -= 5
                    })
                } else { // 每回合若不选防御随机触发一个技能
                    switch (Math.floor(Math.random() * 4)) {
                        case 0:
                            this.log("小丑使用了“红心治疗”！")
                            this.game.waitChoose(this, ["进攻", "诅咒"], ch => {
                                if (ch == 0) {
                                    this.chaos += randInt(3,5)
                                    this.enemy[0].health += randInt(10,50)
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
                                    this.enemy[0].attack += 5
                                    this.roundEnd(() => this.enemy[0].attack -= 5)
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
            // 双层wait（
            this.wait(() => this.fightInput())
        }
        /**
         * 选择魔法。
         * 因为嵌套层级太高，故拆分成单独的方法。
         */
        magicChoose() {
            this.log("你选择了魔法。")
            this.wait(200)
            /** 呈现给用户的可用魔法 */
            let magics = [`治疗魔法（${this.cureMagicCost}）`, "战斗魔法（70）", `黑暗魔法（${this.black ? "100" : "？"}）`]
            if (this.octahedron) { // 如果 几何八面体 enabled
                magics.push(`几何八面体（${this.magic}）`)
            }
            this.game.waitChoose(this, magics, (magicType, process, rechoose) => {
                switch (magicType) {
                    case 0:
                        if (this.magic < this.cureMagicCost) {
                            process.log("你的魔法值不够！")
                            return rechoose()
                        }
                        process.log(`你选择了治疗魔法，HP恢复${this.cureMagicPlus}`)
                        this.magic -= this.cureMagicCost
                        this.game.health += this.cureMagicPlus
                        break;
                    case 1:
                        if (this.magic < 70) {
                            process.log("你的魔法值不够！")
                            return rechoose()
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
                                return rechoose()
                            }
                            process.log("水晶被黑暗笼罩住了！黑暗法术增强了！")
                            this.magic = 0
                            this.enemy[0].health = 0
                        } else {
                            process.log("l͓̩̫̘͙͔̯͖̟̤̓͊̑̌́̂̆̚ò̥̪̭̱̰̝̒͂̄͋̿̏͆́̚c͍̲͇͚̖̬͈̪͙̳͌̉́̃k̪̥̱̝̱̑̈́̏̽͗̊̈́͂̀̍e̞͎̩̜̱̩͚̤̊͌̀̀d̠̖̞̝̙̪̟̞̐͛̈̊̀͂̄͌̓̏͌̓ͅ")
                            return rechoose()
                        }
                        break;
                    case 3:
                        if (this.enemy[0].id === 9) {
                            this.game.virtually(200)
                        }
                        let currentMagic = this.magic
                        this.magic = 0
                        this.enemy[0].health -= currentMagic / 2 // 未定，有名说团战打自己，对此我表示不认同（
                        process.log(`你选择了几何八面体，对【${this.enemy[0].name}】造成${currentMagic / 2}点伤害！`)
                        break;
                    default:
                        throw new Error("非法输入")
                }
                return false;
            })
            
        }
        magicChooseForLorce() {
            this.log("你选择了魔法。")
            this.wait(200)
            if (!this.talked) {
                this.log('星空对你说：“罗尔斯的规则法术……好像对我们也有作用！”')
                this.talked = true
            }
            /** 呈现给用户的可用魔法 */
            let magics = ["超级治疗（60）", "规则防御（30）"]
            if (this.octahedron) {
                magics.push(`几何八面体（${this.magic}）`)
            }
            this.game.waitChoose(this, magics, (magicType, process, rechoose) => {
                switch (magicType) {
                    case 0:
                        if (this.magic < 60) {
                            process.log("你的魔法值不够！")
                            return rechoose()
                        }
                        process.log("你试着用尽全力使出治疗法术……你的血量和攻击力增加了！")
                        this.game.health += 80
                        this.game.attack += 5
                        this.battleMagic = true
                        this.magic -= 60
                        break;
                    case 1:
                        if (this.magic < 30) {
                            process.log("你的魔法值不够！")
                            return rechoose()
                        }
                        process.log("你使用了规则防御，罗尔斯的攻击降低了！罗尔斯的防御略微降低了！")
                        this.magic -= 30
                        this.enemy[0].attack -= 10
                        this.roundEnd(() => this.enemy[0].attack += 10)
                        this.enemy[0].defence -= 5
                        this.roundEnd(() => this.enemy[0].defence += 5)
                        break;
                    case 2:
                        let currentMagic = this.magic
                        this.magic = 0
                        this.enemy[0].health -= currentMagic / 2
                        process.log(`你选择了几何八面体，对【罗尔斯】造成${currentMagic / 2}点伤害！`)
                        break;
                    default:
                        throw new Error("非法输入")
                }
                this.rules += randInt(3, 7)
                return false;
            })
        }
        /**
         * 战斗环节输入框生成
         */
        fightInput(enemyIndex = 0) {
            if (enemyIndex >= this.enemy.length) {
                return;
            }
            if (this.enemy[enemyIndex].dead) {
                return this.fightInput(enemyIndex + 1) // 直到找到没死的敌人
            }
            this.wait( () => {
                var input = new Input(this.game, ["A", "B", "C", "D"], Battle.check5Capitals, (str) => {
                    input.remove()
                    this.fight(str, enemyIndex)
                })
                if (this.game.settings.get("random")) {
                    let str = []
                    for (let i = 0; i < 5; i++) {
                        str.push(65 + Math.floor(Math.random() * 4)) 
                    }
                    input.setValue(String.fromCharCode(...str))
                }
            })
        }
        /**
         * 检查字符串是否由5个大写字母组成。
         * @param {string} str 
         * @returns {boolean}
         */
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
        /**
         * 生成敌方攻击方式并计算敌我方伤害
         * 0 - A 1 - B 2 - C 3 - D
         * @param {string} str
         * @param {number} baseThis 己方原始伤害
         * @param {number} baseEnemy 敌方原始伤害
         * @param {boolean} defense 己方是否防御
         * @param {number} defence 己方防御值
         * @param {number} enemyDefence 敌方防御值
         * @param {Game} game 游戏对象（用于索引界面元素）
         * @param {number} [breakRate] 破甲率
         * @param {Battle} [self] 若为dodge则不适用
         * @returns {[number, string, number]} 敌方伤害，敌方攻击方式，我方伤害
         */
        static computeHurtHarm(str, baseThis, baseEnemy, defense, defence, enemyDefence, game, breakRate, self) {
            if (baseEnemy < 0) {
                baseEnemy = 0
            }
            var same; // 拉低复用性，差评！
            if (self && self.enemy[0].id === 4) {
                if (self.rounds % 4 === 3) {
                    same = Math.floor(Math.random() * 4)
                }
            }
            let hurt = 0, harm = 0, letters = ""
            for (let i = 0; i < 5; i++) {
                let charThis = str.charCodeAt(i) - 65, charEnemy = same || Math.floor(Math.random() * 4), letter = String.fromCharCode(charEnemy + 65)
                if (charThis == charEnemy - 1 || charThis == 3 && charEnemy == 0) {
                    let attack = baseThis
                    let weapon = game.weapon
                    let defence = enemyDefence
                    if (!defense && weapon && weapon.magic) {
                        if (self.magic >= game.weapon.magic) {
                            self.magic -= game.weapon.magic
                            if (weapon.id === DESTROYER_LASER) {
                                defence = 0
                            }
                        } else {
                            attack -= game.weapon.attack
                        }
                    }
                    attack -= defence
                    if (attack < 0 || defense) {
                        attack = 0
                    }
                    harm += attack
                    Battle.charWithColor(str.charAt(i), game.$interface, defense ? 0 : 1, false, i * 10 + 30 + "%")
                    Battle.charWithColor(letter, game.$interface, -1, true, i * 10 + 30 + "%")
                } else if (charEnemy == charThis - 1 || charEnemy == 3 && charThis == 0) {
                    // 是否破甲
                    let broken = false;
                    if (breakRate && Math.random() < breakRate) {
                        defence = 0
                        broken = true
                    }
                    if (!defense) {
                        defence = 0
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
        /**
         * 战斗的弹幕动画，带颜色
         * @param {string} char "A"|"B"|"C"|"D"
         * @param {JQuery<HTMLElement>} $e 
         * @param {0|-1|1} animation 0 for defense, 1 for this attack and -1 for enemy's
         * @param {boolean} fail whether the char element fail
         * @param {string} left the left distance to the browser window
         * @param {boolean} [broken] 破甲
         * @returns {JQuery<HTMLSpanElement>}
         */
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
        /**
         * 输入攻击以后的计算等
         * @param {string|number} str 
         */
        fight(str, enemyIndex = 0) {
            let enemy = this.enemy[enemyIndex]
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
                let enemyDefense = Math.random() < enemy.defenseRate
                let weapon = this.game.weapon
                // 敌方防御且“我方武器为毁灭激光枪且魔法值足够”为假，则敌方防御有效，否则为0
                let enemyDefence = enemyDefense ? enemy.defence : 0
                const BREAK_RATES = {
                    13: 0.3,
                    17: 0.6
                }
                // 解构
                let [hurt, letters, harm] = Battle.computeHurtHarm(
                    str, // 攻击方式
                    this.game.attack, // 己方单伤害
                    enemy.attack, // 敌方原始伤害
                    this.defense, // 是否防御
                    enemyDefence,
                    this.game.defence, // 己方防御值
                    this.game,
                    BREAK_RATES[enemy.id] || 0, // 破甲率
                    this
                    )
                if (this.frozenBreadUsed || this.game.dodgeRate && Math.random() <= this.game.dodgeRate) {
                    hurt = 0 // 闪避/冰冻面包直接0伤
                }
                this.log(`你的攻击是${str}，对方的攻击是${letters}`)
                if (enemyDefense) {
                    this.log(`${enemy.name}选择了防御。`)
                }
                this.log(`你受到${hurt}点伤害`)
                this.game.health -= hurt
                this.log(`你造成了${harm}点伤害`)
                enemy.health -= harm
                if (this.withXk) {
                    let xkHarm = enemyDefence < 20 ? 20 - enemyDefence : 0
                    this.log(`星空造成了${xkHarm}点伤害`)
                    enemy.health -= xkHarm
                }
                this.fightTimes--
                if (this.fightTimes > 0) {
                    return this.fightInput() // 散弹攻击打两次
                }
                if (this.multiEnemy && enemyIndex + 1 !== this.enemy.length) {
                    return this.fightInput(enemyIndex + 1)
                }
                if (enemy.fixed && this.heavyAttack && harm > 0) {
                    this.log("你朝炮筒攻打过去，机械木马开始松动了")
                    enemy.gunHealth--
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
        // @ts-ignore
        get rules() {
            return this._rules
        }
        // @ts-ignore
        set rules(val) {
            this._rules = val
            this.enemy[0].table.rules.set(val)
            if (val >= 100) {
                this.log("战斗的规则摇晃着崩塌了")
                this.win()
            }
        }
        /**
         * 加入回合末执行的回调函数。
         * @param {() => void} callback
         */
        roundEnd(callback) {
            this.roundEndCallback.push(callback)
        }
        // @ts-ignore
        get black() {
            return this.game.judge(1024) && this.enemy[0].id === 9
        }
    }
    class Enemy {
        /**
         * @param {EnemyData} enemyData
         * @param {Battle} battle
         */
        constructor(enemyData, battle) {
            /** 敌人编号 */
            this.id = enemyData.id
            this.battle = battle
            this.game = battle.game
            this.table = new Table("ate-enemy-table", enemyData.name).appendTo(this.battle.$element)
            this.table.add("health", "HP", enemyData.health, "red")
            /** 敌人名称 */
            this.name = enemyData.name
            /** 敌人最大血量 */
            this.full = enemyData.health
            /** 敌人当前血量 */
            this.health = enemyData.health
            /** 敌人攻击 */
            this.attack = enemyData.attack
            /** 敌人防御 */
            this.defence = enemyData.defence
            /** 敌人防御率 */
            this.defenseRate = enemyData.defenseRate
            this.message = enemyData.message
            this.dead = false
            

            switch (this.id) {
                case 13: // 机械木马
                    this.table.add("gunHealth", "炮筒", 5, "orange", true)
                    this.gunHealth = 5
                    /**
                     * 是否已经触发过一次【自我修复】
                     */
                    this.fixed = false
                    break;
                case 14:
                    this.table.add("chaos", "混沌", 120, "linear-gradient(red, grey)", true)
                    this.table.chaos.show()
                    this.battle.chaos = 0
                    /** 是否发动过混沌冲击 */
                    this.battle.chaoAttacked = false
                    break;
                case 17: // 罗尔斯
                    this.table.add("rules", "规则度", 100, "linear-gradient(orange, grey)", true)
                    this.battle.rules = 0
                    this.battle.talked = false
                    this.battle.intenseFight = false
                    break;
                default:
                    break;
            }
        }
        // @ts-ignore
        get health() {
            return this._health
        }
        // @ts-ignore
        set health(val) {
            if (this.dead) {
                return
            }
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
                this.table.remove()
                this.battle.aliveEnemyAmount--
                this.dead = true
                if (this.battle.aliveEnemyAmount === 0) {
                    this.battle.win()
                }
            }
        }
        /**
         * @param {number} val
         */
        _setHealth(val) {
            this._health = val
            this.table.health.set(val)
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
            this.table.gunHealth.set(val)
        }
        round() {
            switch (this.id) {
                case Enemy.WHEEL: // 滚轮
                    if (Math.random() < 0.25) {
                        this.battle.log("滚轮扬起的烟尘让你睁不开双眼！你的攻击力降低了！")
                        this.game.attack -= 10
                        this.battle.roundEnd(() => this.game.attack += 10)
                    }
                    break;
                case Enemy.CRD: // CRD
                    if (this.battle.rounds === 9) {
                        
                        this.battle.log("CRD：“什么？！你们居然还能挺得住，看来我要动用增援了！”")
                        this.battle.log("第一个短矛向你袭来")
                        this.game.waitBattle(8, this.battle)
                        this.battle.log("第二个短矛向你袭来")
                        this.game.waitBattle(8, this.battle)
                        this.battle.log("你转过头来，继续对战CRD。")
                        this.battle.wait(() => this.game.$interface.addClass("battling")) // 重新加上，否则手机版不正常
                    }
                    break;
                case Enemy.SHORT_SPEAR: // 短矛
                    if (this.battle.rounds === 6) {
                        this.game.achieve(2)
                    }
                    break;
                case Enemy.DEER_FALSE: // 鹿法师
                case Enemy.DEER_TRUE:
                    if (this.battle.rounds % 5 === 4) {
                        this.battle.log("鹿法师使用了火魔法！ATT暂时提升5点")
                        this.attack += 5
                        this.battle.roundEnd(() => this.attack -= 5)
                    }
                    break;
                case Enemy.MECHANIC_HORSE: // 机械木马
                    if (this.health < 400) {
                        this.battle.log('机械木马的HP降低了！')
                        this.battle.log('机械木马使用了【自我修复】！机械木马的HP回升了70点！')
                        if (this.fixed == false) {
                            this.battle.log('“呃……这样真的能击败它吗？”水晶说道。')
                            this.battle.log('“Zero就不能用点什么手段吗……”一个骷髅抱怨道。')
                            this.battle.log('“呃……对了！我看到这个木马的炮管，在平常的时候好像都是掩着的，说不定这就是它的弱点！Zero，它等下发动炮弹攻击的时候，你向炮管打去，看看会怎么样！”水晶说。')
                            this.table.gunHealth.show()
                            this.fixed = true
                        }
                        this.health += 70
                    }
                    if (this.battle.heavyAttack = this.battle.rounds % 5 === 4) {
                        this.battle.log("机械木马正在准备一发重型火力攻击。")
                        this.attack += 20
                        this.battle.roundEnd(() => this.attack -= 20)
                    } else if (this.battle.rounds % 5 === 0 && this.battle.rounds > 0) {
                        this.battle.log("机械木马正在准备一发散弹攻击！")
                        this.fightTimes = 2
                    }
                    break;
                case Enemy.LORCE: // LORCE
                    if (this.battle.rounds % 4 == 1 && !this.withXk) {
                        this.withXk = true
                        this.octahedron = true
                        this.battle.log("星空恢复了过来。")
                    }
                    let ratio = 0.1
                    if (this.battle.intenseFight == true) {
                        ratio *= 2
                    }
                    if (this.battle.defense) {
                        ratio *= 2
                    }
                    if (this.battle.breakHarm = Math.random() < ratio) {
                        this.battle.log("罗尔斯举起了重剑！罗尔斯的攻击力提高了！")
                        this.attack += 10
                        this.battle.roundEnd(() => this.attack -= 10)
                        this.breakHarm = true
                    }
                    if (Math.random() < ratio) {
                        let poker = randInt(10, 35)
                        this.game.health -= poker
                        this.battle.log(`罗尔斯使用了一发扑克散弹,你受到了${poker}点伤害！`)
                    }
                    if (Math.random() < ratio) {
                        this.battle.log("罗尔斯使用重剑劈晕了星空！")
                        this.withXk = false
                        this.octahedron = false
                    }
                    this.attack += 5
                    this.battle.roundEnd(() => this.attack -= 5)
                    break;
                default:
                    break
            }
        }
    }
    Enemy.WHEEL = 5
    Enemy.CRD = 7
    Enemy.SHORT_SPEAR = 8
    Enemy.DEER_FALSE = 10
    Enemy.DEER_TRUE = 11
    Enemy.MECHANIC_HORSE = 13
    Enemy.LORCE = 17
    class Game {
        constructor() {
            this.id = -1
            this.$interface = $(".ate-interface")
            this.$grid = $("<div/>").addClass("ate-grid").appendTo(this.$interface)
            this.$status = $("<div/>").addClass("ate-status").appendTo(this.$grid)
            this.settings = new Settings(this)
            this.$settings = Game.button("设置").on("click", () => this.settings.open()).appendTo(this.$status)
/* #noapp */
            if (Element.prototype.requestFullscreen) {
                let on = false
                // 使用监听全屏的方式，而不是在点击是切换状态变量on。
                // 这样，如果用户按 ESC 退出也照样能够更新文字。
                $(document).on("fullscreenchange", () => {
                    on = !on
                    this.$fullscreen.html(on ? "退出全屏" : "全屏模式")
                })
                this.$fullscreen = Game.button("退出全屏").on("click", () => {
                    if (!on) {
                        document.documentElement.requestFullscreen({navigationUI: "hide"})
                    } else {
                        document.exitFullscreen()
                    }
                }).appendTo(this.$status)
            }
/* #endnoapp */
            var $enter = $("<div/>").addClass("ate-enter").html("Extend Air Ticket<div>Click to start</div>").prependTo(this.$interface).one("click", () => {
                $enter.fadeOut(1000, () => {
                    $enter.remove()
                })
            })
            var $white = $("<div/>").addClass("ate-white").prependTo(this.$interface)
            var $sw0rd = $("<div/>").addClass("ate-sw0rd").prependTo(this.$interface).hide().fadeIn(1000)
            /**
             * 右上角的Extend Air Ticket v2.x.x Code by Zes M Young
             */
            var $author = $("#author")
            $author.on("click", () => {
                $author.hide()
            })
            setTimeout(() => {
                $white.remove()
                $sw0rd.fadeOut(1000)
            }, 4000)
            $(document).one("click", () => {
                const AUDIO = document.getElementById("music")
                if (AUDIO instanceof HTMLAudioElement) { // 只是为了迎合VSCode（（（
                    $(document).on("visibilitychange", () => {
                        if (document.visibilityState !== "visible") {
                            if (!this.settings.get("playwhenhidden")) {
                                AUDIO.pause()
                            }
                        } else {
                            AUDIO.play()
                        }
                    })
                    AUDIO.play()
                } else {
                    console.warn("未找到<audio>，无法播放。")
                }
                if (Element.prototype.requestFullscreen) {
                    document.documentElement.requestFullscreen({navigationUI: "hide"})
                // @ts-ignore
                } else if (Element.prototype.webkitRequestFullScreen) {
                    // @ts-ignore
                    document.documentElement.webkitRequestFullScreen({navigationUI: "hide"})
                }
            })
            this.itemImages = []
            for (let each of data.items) {
                this.itemImages.push("./images/" + each.id + ".png")
            }

            window.addEventListener("beforeunload", (e) => {
                if (!this.saved) {
                    e.preventDefault()
                    e.returnValue = "" // 现代浏览器不支持自定义挽留消息（来自MDN）
                    return ""
                }
            })
            if (localStorage.gameData) {
                this.storage = JSON.parse(localStorage.gameData)
                /** @type {1|2|3|4|5} */
                this.chapter = this.storage.chapter || 1
            } else {
                this.chapter = 1
            }
            this.chooseChapter()
        }
        /**
         * 选取章节
         */
        chooseChapter() {
            var $chapters = $("<div/>").addClass("ate-chapters").appendTo(this.$status)
            for (let/** @type {1|2|3|4|5} */ i = 1; i <= 5; i++) {
                let $chapter = $("<div/>").addClass("ate-chapter").appendTo($chapters)
                if (data[i] && i == this.chapter) { // 若数据中有该章节
                    $chapter.html("Chapter " + i).on("click", () => {
                        /** @type {1|2|3|4|5} */
                        $chapters.fadeOut(() => {
                            $chapters.remove()
                            this.run()
                        })
                    })
                } else if (data[i] && i < this.chapter) {
                    $chapter.addClass("ate-chapter-passed").html("passed")
                } else { // 若尚无该章节
                    $chapter.addClass("ate-chapter-locked").html("locked")
                }
            }
        }
        /**
         * 运行游戏
         */
        run() {
            /** 保存按钮 */
            this.$save = Game.button("保存").on("click", () => this.save()).appendTo(this.$status)
            this.$shopMagic = Game.button("商店").on("click", () => this.shopMagic()).appendTo(this.$status)
            $(document).on("keypress", e => {e.which === 89 && this.shopMagic()}) // 你TM把我害惨了呜呜呜
            // 加上花括号就不会了（
            this.table = new Table("ate-vals", "状态栏").appendTo(this.$status)
            /** 物品容器（网格div） */
            this.$items = $("<div/>").addClass("ate-items").appendTo(this.$status)
            /** 防具武器（同上） */
            this.$equipments = $("<div/>").addClass("ate-equipments").appendTo(this.$status)
            /** 消息框 */
            this.$message = $("<div/>").addClass("ate-messages").appendTo(this.$grid)
            /** 战斗UI的区域 */
            this.$battle = $("<div/>").addClass("ate-battle").appendTo(this.$grid)
            /** 选择按钮的区域 */
            this.$input = $("<div/>").addClass("ate-input").appendTo(this.$grid)
            this.$buttons = $("<div/>").addClass("ate-choices").appendTo(this.$grid)
            /** 武器 */
            this.$weapon = $("<div/>").addClass("ate-item").appendTo(this.$equipments)
            /** 防具 */
            this.$armor = $("<div/>").addClass("ate-item").appendTo(this.$equipments)
            this.$weapon.append($("<span/>").addClass("ate-item-name").html("武器"))
            this.$armor.append($("<span/>").addClass("ate-item-name").html("防具"))
            this.table.add("health", "HP", data[this.chapter].maxHealth, "green")
            this.table.add("attack", "Att")
            this.table.add("defence", "Def")
            this.table.add("cm", "CM币")

            /** 背包最大容量 */
            this.max = data[this.chapter].maxItems
            for (let i = 0; i < this.max; i++) {
                $("<div/>").addClass("ate-item").appendTo(this.$items)
            }
            this.queue = new Queue(this)
            this.dead = false
        	this.attack = 15
            this.defence = 0
            this.dodgeRate = 0
            var localStorage = window.localStorage
            if (localStorage.gameData) {
                this.storage = JSON.parse(localStorage.gameData)
                this.health = this.storage.health
                /**
                 * @type {Item[]}
                 */
                this.items = []
                this.experience = this.storage.experience
                this.stackables = this.storage.stackables
                /**
                 * @type {number[]}
                 */
                var items = this.storage.items
                /**
                 * 
                 */
                if (this.storage.weapon) {
                    this.weapon = new Item(this.storage.weapon, this, this.$weapon, 1)
                    items.splice(items.indexOf(this.storage.weapon), 1)
                }
                if (this.storage.armor) {
                    this.armor = new Item(this.storage.armor, this, this.$armor, 1)
                    items.splice(items.indexOf(this.storage.armor), 1)
                }
                for (let each of items) { // 快快看，Zes在这里把of写成in （现在不用那个遍历（
                	this.add(each, this.stackables[each]) // 无需parseInt, Game.items是number[]
                }
                this.cm = this.storage.cm
                this.shops = this.storage.shops || []
                this.virtualExperience = this.storage.virtual || []
            } else {
                this.storage = {}
                this.health = data[this.chapter].maxHealth
                this.cm = 0
                /**
                 * 真经历id的数组
                 * @type {Array<number>}
                 */
                this.experience = []
                this.stackables = {}
                /**
                 * 物品id的数组
                 * @type {Array<Item>}
                 */
                this.items = []
                /**
                 * @type {number[]}
                 */
                this.shops = []
                /**
                 * 虚经历id的数组
                 * @type {number[]}
                 */
                this.virtualExperience = []
            }
            /** 
             * 对于数据中所有stackable的物品，如果在存档的stackables中不存在，会自动用0补充
             * 然而存的时候确实也有0。该语句仅用于旧版本数据的更新以及从Re:Air Ticket Extend迁移的数据。
            for (let each of data.items) {
                if (each.stackable && !(each.id in this.stackables)) {
                    this.stackables[each.id] = 0
                }
            }
            */
            /** 彩蛋随机数，相当于ATE1的fun */
            this.R = Math.round(Math.random() * 100) + 1
            /**
             * 所有用Game.prototype.log()播放过的消息
             * @type {string[]}
             */
            this.history = []
            
            this.exp(this.experience.length ? this.experience.pop() : 0)
        }
        /**
         * 推入发送消息到等待队列。
         * @param {string} msg
         * @param {P} process
         */
        log(msg, process = this) {
            process.wait(() => {
                var $msg = $("<span/>").html(msg).css("display", "none")
                var deferred = $.Deferred()
                this.$message.scrollTop(this.$message[0].scrollHeight)
                this.$message.append($msg).append("<br>")
                if (this.settings.get("speed") === 0) { // 应9Y的建议（
                    $msg.show()
                    this.$message.one("click", () => deferred.resolve())
                } else {
                    $msg.fadeIn(this.settings.get("speed"), () => deferred.resolve())
                }
                this.history.push(msg)
                return deferred
            })
        }
        /**
         * 返回由所有物品的名称组成的数组。
         * @param {boolean} nothrowable 若设为true则不会返回无法丢弃的占位卡、监狱钥匙等 
         * @returns {[string[], number[]]}
         */
        showItems(nothrowable) {
            var arr = [], indexes = []
            var items = this.items
            for (let index in items) {
                let each = items[index]
                if (each.throwable !== false || !nothrowable) {
                    arr.push(each.name)
                    indexes.push(parseInt(index))
                }
            }
            return [arr, indexes]
        }
        /**
         * 装备某物品
         * @param {Item} item
         */
        equip(item) {
            this.items.splice(this.items.indexOf(item), 1)
            if (item.type === Item.WEAPON) { // 零剑
                this.weapon = item
            } else if (item.type === Item.ARMOR) {
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
        /**
         * @param {number} val
         */
        // @ts-ignore
        set attack(val) {
            this._attack = val
            if (this.weapon && this.weapon.id === SW0RD) {
                this.table.attack.$val.html("?")
                return
            }
            this.table.attack.set(val)
        }
        // @ts-ignore
        get defence() {
            return this._defence
        }
        /**
         * @param {number} val
         */
        // @ts-ignore
        set defence(val) {
            this._defence = val
            this.table.defence.set(val)
        }
        // @ts-ignore
        get cm() {
            return this._cm
        }
        /**
         * @param {number} val
         */
        // @ts-ignore
        set cm(val) {
            this._cm = val
            this.table.cm.set(val)
        }
        // @ts-ignore
        get health() {
            return this._health
        }
        /**
         * @param {number} val
         */
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
        /**
         * @returns {undefined|Item}
         */
        // @ts-ignore
        get weapon() {
            return this._weapon
        }
        /**
         * @param {Item} weapon
         */
        // @ts-ignore
        set weapon(weapon) {
            if (!weapon || weapon === this.weapon) {
                return
            }
            var old = this.weapon
            this._weapon = weapon
            if (old) {
                if (old.id === SW0RD) {
                    window.clearInterval(this.timer.id)
                    this.attack -= this.timer.lastAdd
                } else {
                    this.attack -= old.attack
                }
                old.$element.insertBefore(this.findBlankItem())
                this.items.push(old)
            } else if (weapon.$element !== this.$weapon) {
                this.$weapon.html("").appendTo(this.$items)
            }
            weapon.$element.prependTo(this.$equipments)
            if (weapon.id === SW0RD) {
                this.timer = {}
                this.timer.lastAdd = 0
                this.timer.id = window.setInterval(() => {
                    this.attack -= this.timer.lastAdd
                    this.timer.lastAdd = randInt(5, 50)
                    this.attack += this.timer.lastAdd
                }, 5000)
            } else {
                // @ts-ignore
                this.attack += weapon.attack
            }
        }
        /**
         * @returns {undefined|Item}
         */
        // @ts-ignore
        get armor() {
            return this._armor
        }
        /**
         * @param {Item} armor
         */
        // @ts-ignore
        set armor(armor) {
            if (!armor || armor === this.armor) {
                return
            }
            var old = this._armor
            this._armor = armor
            if (old) {
                this.defence -= old.defence
                if (old.dodgeRate) {
                    this.dodgeRate -= old.dodgeRate
                }
                old.$element.insertBefore(this.findBlankItem())
                this.items.push(old)
            } else if (armor.$element !== this.$armor) {
                this.$armor.html("").appendTo(this.$items)
            }
            armor.$element.appendTo(this.$equipments)
            this.defence += armor.defence
            if (armor.dodgeRate) {
                this.dodgeRate += armor.dodgeRate
            }

        }
        // #endregion
        /**
         * @param {number} [id]
         */
        findItem(id) {
            if (id === undefined) {
                return undefined
            }
            for (let each of this.items) {
                if (each.id === id) {
                    return each
                }
            }
        }
        /**
         * 以process的签名向队列加入添加某id物品的物品amount个（仅用于可堆叠）的任务
         * @param {number} id
         * @param {number} [amount]
         * @param {P} [process]
         */
        waitGet(id, amount = 1, process = this) {
            /**
             * 仅用于不可堆叠，或原来数量为零的可堆叠。
             * 也就是需要往物品栏添加元素时才使用该函数。
             */
            const add = () => {
                if (this.itemsFull(id)) { // 其实这里判重了，但是不影响
                    this.wait(() => {
                        var [items, indexes] = this.showItems(true) // 必须等到当时实时获取物品数组
                        items.push("放弃拾取")
                        this.Process(p => {
                            p.log("已满，请丢弃一项")
                            p.choose(items, (/** @type {number} */ i) => {
                                if (i === this.max) { // 放弃拾取
                                    return p.die(this)
                                }
                                this.remove(indexes[i])
                                this.add(id, amount)
                                p.die(process)
                            })
                        }).go()
                    })
                } else {
                    var item = this.add(id, amount)
                    this.waitProcess(process, p => {
                        p.log(`已将${item.name}加入您的背包。`)
                        p.waitDie(process)
                    })
                }
            }
            var mayBeItem = this.findItem(id)
            if (mayBeItem && mayBeItem.stackable) {
                mayBeItem.amount += amount
            } else {
                add()
            }
        }
        findBlankItem() {
            var $items = this.$items.children(".ate-item")
            /** @type {JQuery|undefined} */
            var $item
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
            return $item
        }
        /**
         * @param {number} [id]
         */
        itemsFull(id) {
            var stackable
            if (id !== undefined) {
                stackable = data.items[id].stackable
            }
            return this.items.length === this.max && !(stackable && this.has(id))
        }
        /**
         * @param {number} id
         * @param {number} [amount]
         */
        add(id, amount) {
            var item = new Item(id, this, this.findBlankItem(), amount)
            this.items.push(item)
            return item
        }
        /**
         * 判断是否拥有某ID的物品
         * @param {number} id
         */
        has(id) {
        	return !!this.findItem(id)
        }
        /**
         * 移除某位置的物品。
         * @param {number} index
         */
        remove(index) {
            var item = this.items.splice(index, 1)[0]
            item.$element.html("").css("backgroundImage", "").appendTo(this.$items) // 因为这里写成$items导致了大问题
            return item
        }
        /**
         * @param {number} index
         * @param {P} process
         */
        waitRemove(index, process = this) {
            process.wait(() => void this.remove(index))
        }
        /**
         * 
         * @param {Item} item 
         * @returns 
         */
        removeItem(item) {
            return this.remove(this.items.indexOf(item))
        }
        /**
         * @param {Item} item
         * @param {P} process
         */
        waitRemoveItem(item, process = this) {
            process.wait(() => void this.removeItem(item))
        }
        /**
         * 战斗中使用物品。
         * @param {number} index
         * @param {Battle} battle
         * @param {Process} itemSubProcess
         */
        use(index, battle, itemSubProcess) {
            var item = this.items[index]
            if (item.stackable) {
                item.amount -= 1
            } else {
                this.waitRemove(index, battle)
            }
            battle.log(`你使用了${item.name}。`)
            if (item.id === FROZEN_BREAD) {
                battle.frozenBreadUsed = true
            }
            // @ts-ignore
            for (let each of item.use) {
            	this.execute(each, battle, itemSubProcess)
            }
        }
        /**
         * @param {number} id
         */
        exp(id) {
            this.cache()
        	this.$message.html("")
            this.experience.push(id)
            const story = data[this.chapter].story[id]
            if (Array.isArray(story)) {
                this.story(this.judgeArr(story))
            } else {
                this.story(story)
            }
        }
        /**
         * @param {Story} story
         */
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
                this.waitBattle(story.battle, this)
            }
            if ("choice" in story) {
                if ("to" in story) { // 选择一类
                    let length = story.choice.length
                    let choices = []
                    /**
                     * @type {StoryTo[]}
                     */
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
                } else { // 输入框一类，例如J12132的挂历谜题
                    this.wait(() => {
                        this.toggleExpand()
                        let input = new Input(
                            this,
                            [],
                            str => "#pattern" in story.choice ? new RegExp(story.choice["#pattern"]).test(str) : true,
                            str => {
                                if (!("#default" in story.choice)) {
                                    if (str in story.choice) {
                                        const to = story.choice[str]
                                        if (typeof to === "number") {
                                            this.exp(to)
                                        } else if (Array.isArray(to)) {
                                            this.exp(this.judgeArr(to))
                                        }

                                    } else {
                                        return
                                    }
                                } else {
                                    const to = story.choice[str in story.choice ? str : "#default"]
                                    if (typeof to === "number") {
                                        this.exp(to)
                                    } else if (Array.isArray(to)) {
                                        this.exp(this.judgeArr(to))
                                    }
                                }
                                input.remove()
                                this.toggleExpand()
                            }
                        )
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
                } else if (to === true) {
                    this.experience = []
                    this.chapter++
                    this.health = data[this.chapter].maxHealth
                    this.cache()
                    this.save()
                    this.log("请重启游戏！")
                    this.wait(() => location.reload())
                } else {
                    this.log("敬请期待！")
                }
            }
        }
        /**
         * 执行指令
         * @param {string} command 
         * @param {Battle} [battle]
         * @param {Process} [itemSubProcess]
         */
        execute(command, battle, itemSubProcess) {
            /**
             * @type {Array<string>}
             */
            var tokens = command.split(" "), amount
            switch (tokens[0]) {
                case "get":
                	this.waitGet(parseInt(tokens[1]), tokens[2] && parseInt(tokens[2]))
                	break;
                case "remove":
                	this.removeItem(this.findItem(parseInt(tokens[1])))
                	break;
                case "health":
                case "cm":
                    amount = intOrScope(tokens[2])
                	if (tokens[1] == "+") {
                		this[tokens[0]] += amount
                	} else if (tokens[1] == "-") {
                		this[tokens[0]] -= amount
                	}
                	break;
                case "attack":
                case "defence":
                case "dodgeRate":
                    amount = intOrScope(tokens[2])
                    // 第三个令牌，布尔类型，指定指令效果持续至战斗结束
                    // 也就用了黑客三周年蛋糕这一次嘛（（（（
                    let untilEnd = tokens[3] === "true" || tokens[3] === "1"
                    if (battle && untilEnd) {
                        if (tokens[1] == "+") {
                            this[tokens[0]] += amount
                            battle.after.wait(() => this[tokens[0]] -= amount)
                        } else if (tokens[1] == "-") {
                            this[tokens[0]] -= amount
                            battle.after.wait(() => this[tokens[0]] += amount)
                        }
                    } else if (battle) {
                        if (tokens[1] == "+") {
                            this[tokens[0]] += amount
                            battle.roundEnd(() => this[tokens[0]] -= amount)
                        } else if (tokens[1] == "-") {
                            this[tokens[0]] -= amount
                            battle.roundEnd(() => this[tokens[0]] += amount)
                        }
                    } else {
                        if (untilEnd) {
                            console.warn("No battle. Don't use the third argument [untilEnd].")
                        }
                        if (tokens[1] == "+") {
                            this[tokens[0]] += amount
                        } else if (tokens[1] == "-") {
                            this[tokens[0]] -= amount
                        }
                    }
                	break;
                case "harm":
                    if (tokens[2] == "1" && battle.aliveEnemyAmount > 1) {
                        this.Process(process => {
                            process.log("选择一个使用对象。")
                            for (let enemy of battle.enemy) {
                                enemy.table.$outer.on("click", () => {
                                    enemy.health -= parseInt(tokens[1])
                                    $(".ate-enemy-table").off("click")
                                    process.die(itemSubProcess)
                                })
                            }
                        }).go()
                    } else {
                        battle.enemy.forEach(each => !each.dead && (each.health -= parseInt(tokens[1])))
                    }
                    break;
                case "dodge":
                    this.dodge(parseInt(tokens[1]), tokens[2])
                    break;
                case "bridge":
                    this.bridge()
                    break;
                case "floor":
                    this.floor()
                    break;
                case "door":
                    this.door(parseInt(tokens[1]), parseInt(tokens[2]))
                    break;
                case "shop":
                    this.waitShop(parseInt(tokens[1]))
                    break;
                case "achieve":
                    this.achieve(parseInt(tokens[1]))
                    break;
                case "edefence":
                case "eattack":
                    let prop = tokens[0].slice(1)
                    amount = intOrScope(tokens[2])
                	if (tokens[1] == "+") {
                		battle.enemy[prop] += amount
                        battle.roundEnd(() => battle.enemy[prop] -= amount)
                	} else if (tokens[1] == "-") {
                		battle.enemy[prop] -= amount
                        battle.roundEnd(() => battle.enemy[prop] += amount)
                	}
                    break;
                case "experience":
                    this.virtually(parseInt(tokens[1]))
                    break;
                case "defer":
                    let round = battle.rounds + parseInt(tokens[1]) // 第一个令牌表示延迟的回合数
                    battle.deferredCommands[round] = battle.deferredCommands[round] ?? [] // 若无则创建一个
                    battle.deferredCommands[round].push(tokens.slice(2).join(" ")) // 剩余令牌作为指令传入
                    break;
                case "addshop":
                    this.shops.push(parseInt(tokens[1]))
                    break;
                case "sleep":
                    break;
                default:
                    throw new Error("Unknown Command")
            }
        }
        /**
         * 判断一个条件
         * @param {Condition} condition 
         * @returns {boolean}
         */
        judge(condition) {
            if (typeof condition === "number") {
                return this.experience.includes(condition)
            } else if (typeof condition === "string") {
                // 只包含数字的字符串等同于直接输入数字
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
                        case "health":
                        case "h":
                            return this.health === number
                        case "item":
                        case "i":
                            return this.has(number)
                        case "armor":
                        case "a":
                            let armor = this.armor
                            return armor !== undefined && armor.id === number
                        case "weapon":
                        case "w":
                            let weapon = this.weapon
                            return weapon !== undefined && weapon.id === number
                        case "cm":
                        case "c":
                            return this.cm >= number
                        case "virtual":
                        case "v":
                            return this.virtualExperience.includes(number)
                        case "attack":
                        case "att":
                            return this.attack >= number
                        case "defence":
                        case "def":
                            return this.defence >= number
                        default:
                            throw new Error(`Illegal condition prefix '${prefix}'.`)
                    }
                }
            }
        }
        /**
         * 检查是否可能为合法条件字符串。
         * “可能”的合法条件字符串只包含|?&和拉丁字母、阿拉伯数字
         * @param {string|number} condition 
         */
        static isValidCondition(condition) {
            return typeof condition === "number" || /^[a-z0-9&\|!]+$/.test(condition)
        }
        /**
         * 评估一个条件表达式。
         * 如果不是合法条件表达式，直接随机返回其中一项。
         * @param {Expression<any>} arr 
         * @returns {any}
         */
        judgeArr(arr) {
            var l = arr.length
            // 合法条件表达式的第1个位置应该是合法条件字符串
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
        /**
         * 
         * @param {Array<string>} choices 
         * @param {(choice: number)=>void} callback
         * @param {number[]} [fade]
         * @returns {void}
         */
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
        /**
         * 做出选择
         * 在ATE2中不支持key，因为根本没有（
         * @param {Array<string>} choices
         * @param {(choice: number) => void} callback
         * @param {number[]} [fade]
         */
        choose(choices, callback, fade) {
        	this.wait(() => this._choose(choices, callback, fade))
        }
        /**
         * 将一个函数加入等待队列，或将等待若干毫秒的函数加入队列。
         * @param {number|(()=>JQuery.Promise|void)} fnOrWaitMs 
         * @returns {void}
         */
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
        cache() {
            /**
             * 复制一个新数组。
             * 如果有防具或是武器，会将它们推入items数组。
             * 当游戏加载时，this.armor = this.storage.armor这一过程会取出items数组中的防具id。
             * 复制的目的是防止污染当前游戏的items数组。
             */
            var items = []
            var stackables = {}
            for (let each of this.items) {
                items.push(each.id)
                if (each.stackable) {
                    stackables[each.id] = each.amount
                }
            }
            if (this.weapon) {
                items.push(this.weapon.id)
            }
            if (this.armor) {
                items.push(this.armor.id)
            }
            this.storage = {
                health: this.health,
                items: items,
                experience: this.experience,
                weapon: this.weapon ? this.weapon.id : null,
                armor: this.armor ? this.armor.id: null,
                cm: this.cm,
                stackables: stackables,
                virtual: this.virtualExperience,
                chapter: this.chapter
            }
            this.saved = false
        }
        /**
         * 保存游戏数据
         * @returns {void}
         */
        save() {
            this.saved = true
        	localStorage.gameData = JSON.stringify(this.storage)
            this.notify("保存成功")
        }
        /**
         * 以owner为后继者触发战斗
         * @param {number|string} id 
         * @param {P} owner
         */
        waitBattle(id, owner) {
            owner.wait(() => {
                var battle = new Battle(data.battle[id], this, owner)
                battle.run()
            })
        }
        /**
         * 躲避剧情
         * @param {number} baseEnemy
         * @param {string} name
         */
        dodge(baseEnemy, name) {
            this.waitProcess(this, process => {
                this.toggleExpand()
                var input = new Input(
                    this,
                    ["A", "B", "C", "D"],
                    Battle.check5Capitals,
                    str => {
                        input.remove()
                        let [hurt, letters, _harm] = Battle.computeHurtHarm(str, 0, baseEnemy, true, 0, 0, this)
                        process.log(`你的攻击是${str}，${name}的攻击是${letters}。`)
                        process.log(`你被扣血${hurt}`)
                        this.health -= hurt
                        process.wait(() => this.toggleExpand())
                        process.waitDie(this)
                    }
                )
                if (this.settings.get("random")) { // 自动装填
                    let str = [] // 字符串中的字符ASCII码
                    for (let i = 0; i < 5; i++) {
                        str.push(randInt(65, 68)) 
                    }
                    input.setValue(String.fromCharCode(...str)) // 解构
                }
            })
        }
        bridge(floor = false) {
            var length = floor ? 4 : 3
            var type = floor ? "地板" : "桥"
            this.log(`选择一${floor ? '条路线' : '座桥'}以通过`)
            var bridges = []
            for (let i = 0; i < length; i++) {
                bridges.push(String.fromCharCode(65 + i))
            }
            this.waitChoose(this, bridges, (ch, p, rechoose) => {
                var noBridge = Math.floor(Math.random() * 3)
                var formedBridges = Array.from(bridges)
                if (ch === noBridge) {
                    formedBridges.splice(noBridge, 1)
                    p.log(`翻转地板组成了${type + formedBridges.join()}，你没通过${type}！[HP-2]`)
                    this.health -= 2
                    return rechoose()
                } else {
                    p.log(`你通过了${type}！`)
                }
            })
        }
        floor() {
            return this.bridge(true)
        }
        /**
         * @param {number} amount
         * @param {number} least
         */
        door(amount, least) {
            this.waitProcess(this, process => {
                this.toggleExpand()
                var times = 0
                const generate = () => {
                    if (amount == 5 && least == 5 && times % 3 === 0) {
                        return "00000"
                    } else if (amount == 10 && least == 10 && times % 3 === 0) {
                        return Math.random() > 0.5 ? "1111111111" : "0000000000"
                    }
                    let ret = ""
                    for (let i = 0; i < amount; i++) {
                        ret += Math.random() > 0.5 ? "1" : "0"
                    }
                    return ret
                }
                var input = new Input(
                    this,
                    ["0", "1"],
                    str => str.length === amount && !/[^01]/.test(str),
                    str => {
                        let doors = generate()
                        let passed = 0
                        for (let i = 0; i < amount; i++) {
                            if (doors[i] !== str[i]) {
                                passed++
                            }
                        }
                        if (passed >= least) {
                            process.log("你通过了升降门！")
                            process.waitDie(this)
                            input.remove()
                            this.toggleExpand()
                        } else {
                            process.log(`升降门的升降形式是${doors}，你只通过了${passed}道门，请重新来过[HP-5]`)
                            input.setValue("")
                            this.health -= 5
                        }
                        times++
                    })
                process.log(`请输入您的通过方式，由${amount}个二进制字符组成`)
                if (amount != least) {
                    process.log(`至少通过${least}/${amount}道`)
                }
            })
        }
        shopMagic() {
            if (this.queue.owner !== 0) {
                return this.notify("现在不能使用商店魔法");
            }
            var availableShopNames = []
            if (this.shops.length <= 0) { // 我是啥b
                this.log("你没有商店。")
                return
            }
            for (let each of this.shops) {
                let shop = data.shop[each]
                console.log(data.shop, data.shop[each], shop)
                availableShopNames.push(shop.name)
                
            }
            this.Process(p => {
                p.choose(availableShopNames, ch => {
                    this.waitShop(this.shops[ch], p)
                    p.waitDie(this)
                })
            }).go()
        }
        /**
         * 商店
         * @param {number} id
         * @param {P} process
         */
        waitShop(id, process = this) {
            var shopData = data.shop[id]
            var shopPrices = shopData.price
            process.log(`欢迎来到${"name" in shopData ? shopData["name"] : "商店"}！`)
            const shop = () => this.Process((p) => {
                var prices = {}, items = [], itemIds = []
                for (let item in shopPrices) {
                    let price = shopPrices[item]
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
                console.log(prices)
                var leaveKey = items.length
                items.push("离开")
                p.choose(items, (/** @type {number} */ ch) => {
                    if (ch === leaveKey) {
                        return p.die(this)
                    }
                    var bought = parseInt(itemIds[ch])
                    console.log(bought)
                    if (this.itemsFull(bought)) {
                        p.log("背包空间不够，你离开了商店")
                        return p.waitDie(this)
                    }
                    if (prices[bought] > this.cm) {
                        p.log("你的CM币不够！")
                    } else {
                        this.cm -= prices[bought]
                        this.waitGet(bought, 1, p)
                    }
                    p.wait(() => p.die(shop()))
                })
            }).go()
            process.wait(() => shop())
        }
        /**
         * 添加一项虚经历
         * @param {number} id
         */
        virtually(id) {
            this.virtualExperience.push(id)
        }
        die() {
            var process = this.queue.now() // 只能用这种方式，因为赋值是传不了额外参数的
            this.Process((dieProcess) => {
                dieProcess.log("黑暗再次降临。")
                if (this.has(LOVECA)) {
                    dieProcess.log("使用复活爱心吗?")
                    dieProcess.choose(["是", "否"], (ch) => {
                        if (!ch) {
                            this.findItem(LOVECA).amount--
                            this.health = 100
                            dieProcess.log("那么，你将再次驱散黑暗")
                            dieProcess.waitDie(process)
                        } else {
                            dieProcess.log("看来，黑暗将会再度笼罩你")
                            dieProcess.log("You died.")
                            delete localStorage.gameData
                            delete this.queue
                        }
                    })
                } else {
                    dieProcess.log("希望似乎保佑不了你")
                    dieProcess.log("看来，黑暗将会再度笼罩你")
                    dieProcess.log("You died.")
                    delete localStorage.gameData
                    delete this.queue
                }
            }).go()
        }
        /**
         * Simular to {{-}} in wikitext. Prevents float elements from being out of the parent.
         * 与clear模板类似，防止浮动元素漏出容器。
         * @returns 
         */
        static clear() {
            return $("<div/>").css("clear", "both")
        }
        /**
         * 为.ate-item元素添加background-image。
         * @param {JQuery<HTMLElement>} $ele
         * @param {number|Item} item
         */
        addImage($ele, item) {
            if (item instanceof Item) {
                item = item.id
            }
            if (item < this.itemImages.length) {
                $ele.css("backgroundImage", `url(${this.itemImages[item]})`)
            }
        }
        /**
         * 达成某个成就。如果已经达成，则什么也不做。
         * @param {number} id
         */
        achieve(id) {
            if (this.achievements.includes(id)) {
                return
            }
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
            /** @type {number[]} */
            var ach = localStorage.ateAchievements ? JSON.parse(localStorage.ateAchievements) : []
            return {
                /**
                 * @param {number} id
                 */
                push(id) {
                    ach.push(id)
                    localStorage.ateAchievements = JSON.stringify(ach)
                },
                /**
                 * @param {number} id
                 */
                includes(id) {
                    return ach.includes(id)
                },
                // @ts-ignore
                get length() {
                    return ach.length
                }
            }
        }
        /**
         * 以cls为类，返回一个EATUI的按钮。
         * @param {string} text
         * @param {{
         *   cls?: string;
         *   title?: string;
         *   margin?: string;
         *   padding?: string;
         * }} [options]
         * @returns {JQuery}
         */
        static button(text, options) {
            var $button = $("<div/>").addClass("ate-button").html(text)
            if (options) {
                if (options.cls) {
                    $button.addClass("ate-button-" + options.cls)
                }
                if (options.title) {
                    $button.attr("title", options.title)
                }
                if (options.margin) {
                    $button.css("marginLeft", options.margin)
                }
                if (options.padding) {
                    $button.css("paddingLeft", options.padding)
                        .css("paddingRight", options.padding)
                }
            }
            return $button
        }
        /**
         * 发送一条绿色的消息，不展示在消息框中
         * @param {string} msg
         */
        notify(msg) {
            var $msg = $("<div/>").addClass("ate-notification").appendTo(this.$interface).html(msg)
            $msg.fadeIn(1500)
            $msg.fadeOut(3000, () => $msg.remove())
        }
        /**
         * 返回一个进程，game参数自动传入
         * @param {(process:Process)=>void} func 
         * @returns {Process}
         */
        Process(func) {
            return new Process(func, this)
        }
        /**
         * 
         * @param {P} process 
         * @param {(process:Process)=>void} func 
         */
        waitProcess(process, func) {
            process.wait(() => this.Process(func).go())
        }
        /**
         * @typedef {(arg0: number, process?: Process, rechoose?: () => boolean) => (void|boolean)} WaitChooseFn
         * @param {P} process
         * @param {string[]} choices
         * @param {WaitChooseFn} func
         */
        waitChoose(process, choices, func) {
            this.waitProcess(process, (p) => {
                const choosing = () => {
                    p.choose(choices, ch => {
                        let ret = func(ch, p, choosing)
                        if (ret !== true) {
                            p.die(process)
                        }
                    })
                    return true;
                }
                choosing()
            })
        }
        /**
         * @returns {void}
         */
        toggleExpand() {
            let hasClass = this.$interface.hasClass("ate-interface-expanded")
            if (hasClass) {
                this.$interface.removeClass("ate-interface-expanded")
            } else {
                this.$interface.addClass("ate-interface-expanded")
            }
        }
        /**
         * #nolts
         * @param {number} eid
         */
        skip(eid) {
            if (this.queue.processing) {
                throw new Error("Still processing")
            }
            this.$buttons.html("")
            this.exp(eid)
        }
/** #endnolts */
    }
/** #nolts */
        if (new URL(location.href).searchParams.get("pw") != "3473473639574279") {
            return
        }
    	window.ateGame = new Game()
        window.ATEGame = Game
        $.extend(Game, {Queue, Battle, Enemy})
/** #endnolts */
/* #ltsonly #soloonly {
        var game = new Game()
} */
    	document.title = "游玩 Extend Air Ticket"
        $("#version").html(version)
// @ts-ignore
})(jQuery, ateData, "2.14.0/** #nolts */ Beta/** #endnolts */")
