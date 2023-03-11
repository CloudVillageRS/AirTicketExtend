

type Condition = string | number
type Expression<T> = [T, Condition] | [T, Condition, T] |  [T, Condition, T, Condition] | [T, Condition, T, Condition, T]
interface EnemyData {
    /** 名称 */
    name: string;
    /** 攻击力 */
    attack: number;
    /** 血量 */
    health: number;
    /** 防御力 */
    defence: number;
    /** 防御率 */
    defenseRate: number;
    /** @deprecated */
    random: number;
    /** ID */
    id: number;
    /** 消息 */
    message?: Array;
};

interface NormalItem {
    name: string;
    description: string;
    id: number;
    stackable?: boolean;
    throwable?: boolean

}
interface BattleItem {
    name: string;
    description: string;
    battle: boolean;
    id: number;
    stackable?: boolean;
    use: string[];
    throwable?: boolean;
    cd?: number
}

interface WeaponItem {
    name: string;
    description: string;
    id: number;
    stackable?: boolean;
    attack: number;
    throwable?: boolean;
    magic?: number
}

interface ArmorItem {
    name: string;
    description: string;
    id: number;
    stackable?: boolean;
    defence: number;
    throwable?: boolean;
    dodgeRate?: number
}

type ItemData = NormalItem | BattleItem | WeaponItem | ArmorItem
type StoryTo = number | Expression<number>
type StoryToes = StoryTo[]
type Choice = string | Expression<string>
type Story =  {
    message: Array<string|Expression<string>>;
    choice: Choice[];
    to: StoryToes;
    fadeChoice: number[];
} | {
    message: Array<string|Expression<string>>;
    battle: string | number;
    to: StoryTo;
} | {
    message: Array<string|Expression<string>>;
    choice: {
        [key: string]: StoryTo,
        "#pattern": string
    }
}
interface Achievement {
    name: string;
    description: string;
    id: number
}
interface Chapter {
    maxHealth: number;
    maxItems: number;
    story: (Story|Expression<Story>)[];
}
interface GameData {
    items: ItemData[];
    battle: JQuery.PlainObject<BattleData>;
    enemy: EnemyData[];
    achievement: Achievement;
    shop: JQuery.PlainObject<
        {
            price: JQuery.PlainObject<number|Expression<number>>;
            if?: Condition;
            name?: string
        }
    >;
    1: Chapter;
    2: Chapter;
    3: Chapter;
    4: Chapter;
    5: Chapter;
}

interface BattleData {
    enemy: number | number[];
    win?: string[];
    withXk?: boolean;
    withNc?: boolean;
    withSo?: boolean;
    tutorial?: boolean;
    octahedron?: boolean
}

interface ProcessLike {
    wait(fn: () => JQuery.Promise | void): void;
    dead: boolean;
    log(msg: string): void;
}
type CBP = ProcessLike | void
type Task = () => any;
