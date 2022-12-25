

type Condition = string | number
type Expression<T> = [T, Condition]
type Expression<T> = [T, Condition, T]
type Expression<T> = [T, Condition, T, Condition]
type Expression<T> = [T, Condition, T, Condition, T]
interface EnemyData {
    name: string;
    attack: number;
    health: number;
    defence: number;
    defenseRate: number;
    /** @deprecated */
    random: number;
    id: number;
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
    throwable?: boolean
}

interface WeaponItem {
    name: string;
    description: string;
    id: number;
    stackable?: boolean;
    attack: number;
    throwable?: boolean
}

interface ArmorItem {
    name: string;
    description: string;
    id: number;
    stackable?: boolean;
    defence: number;
    throwable?: boolean
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
}
interface Achievement {
    name: string;
    description: string;
    id: number
}
interface Chapter {
    maxHealth: number;
    story: (Story|Expression<Story>)[];
}
interface GameData {
    items: ItemData[];
    battle: Object<number|string, {
        enemy: number;
        win?: string[];
        withXk?: boolean;
    }>;
    enemy: EnemyData[];
    achievement: Achievement;
    shop: JQuery.PlainObject<
        JQuery.PlainObject<number|Expression<number>>
    >;
    1: Chapter;
    2: Chapter;
    3: Chapter;
    4: Chapter;
    5: Chapter;
}

interface P {
    id: number;
    wait(fn: () => JQuery.Promise | void): void;
    dead: boolean;
}
type CBP = P | void
type WaitFn = () => (JQuery.Promise|void);

