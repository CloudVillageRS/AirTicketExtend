
type Condition = string | number
type Expression<T> = [T, Condition]
type Expression<T> = [T, Condition, T]
type Expression<T> = [T, Condition, T, Condition]
type Expression<T> = [T, Condition, T, Condition, T]
type EnemyData = {
    name: string;
    attack: number;
    health: number;
    defence: number;
    defenseRate: number;
    random: number;
    id: number;
    message: Object<number, string>
};
type ItemData = {
    name: string;
    description: string;
    battle?: boolean;
    id: number;
    stackable?: boolean;
    attack?: number;
    defence?: number;
    use?: string[];
    throwable?: boolean
}
type StoryTo = number | Expression<number>
type StoryToes = StoryTo[]
type Choice = string | Expression<string>
type Story = {
    message: Array<string|Expression<string>>;
    battle: string | number;
    choice: Choice[];
    to: StoryTo|StoryToes;
    fadeChoice: number[];
}
type Achievement = {
    name: string;
    description: string;
    id: number
}
type Chapter = {
    maxHealth: number;
    story: (Story|Expression<Story>)[];
}
type GameData = {
    items: ItemData[];
    battle: Object<number|string, {
        enemy: number;
        win?: string[];
        withXk?: boolean;
    }>;
    enemy: EnemyData[];
    achievement: Achievement;
    shop: Object<
        number,
        Object<number, number|Expression<number>>
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