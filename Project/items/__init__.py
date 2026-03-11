from .map_item import MapItem
from .inventory import Inventory
from .item import Item
from .rarity import Rarity
from .weapon import Weapon
from .armor import Armor
from .consumable import Consumable


SWORDS = [
    Weapon(
        item_id="sword_rapira",
        name="Рапира",
        description="Лёгкий и быстрый клинок, идеален для точных ударов.",
        icon_path="icons/weapons/swords/rapira.png",
        rarity=Rarity.UNCOMMON,
        base_damage=12,
        attack_speed=1.3,
        critical_chance=0.15,
        critical_multiplier=2.0,
        scaling_stats={"dexterity": 0.3}
    ),
    Weapon(
        item_id="sword_sablia",
        name="Сабля",
        description="Изогнутый клинок, эффективен в рубящих атаках.",
        icon_path="icons/weapons/swords/sablia.png",
        rarity=Rarity.COMMON,
        base_damage=15,
        attack_speed=1.0,
        critical_chance=0.05,
        critical_multiplier=1.5,
        scaling_stats={"strength": 0.2}
    ),
    Weapon(
        item_id="sword_hope_of_kingdom",
        name="Надежда королевства",
        description="Легендарный меч, символ воли королевства и его защитников.",
        icon_path="icons/weapons/swords/hope_of_kingdom.png",
        rarity=Rarity.LEGENDARY,
        base_damage=25,
        attack_speed=1.2,
        critical_chance=0.2,
        critical_multiplier=2.5,
        scaling_stats={"strength": 0.3, "dexterity": 0.2, "charisma": 0.1}
    )
]
# ================== ТОПОРЫ ==================

AXES = [
    Weapon(
        item_id="axe_one_handed",
        name="Одноручный топор",
        description="Простой боевой топор, удобный в одной руке.",
        icon_path="icons/weapons/axes/one_handed_axe.png",
        rarity=Rarity.COMMON,
        base_damage=18,
        attack_speed=0.8,
        critical_chance=0.05,
        critical_multiplier=1.8,
        scaling_stats={"strength": 0.3}
    ),
    Weapon(
        item_id="axe_two_handed",
        name="Двуручный топор",
        description="Тяжёлый топор, наносящий сокрушительные удары.",
        icon_path="icons/weapons/axes/two_handed_axe.png",
        rarity=Rarity.RARE,
        base_damage=25,
        attack_speed=0.6,
        critical_chance=0.08,
        critical_multiplier=2.0,
        scaling_stats={"strength": 0.4}
    ),
    Weapon(
        item_id="axe_bonebreaker",
        name="Костолом",
        description="Мощный топор, разбивающий кости и доспехи одним ударом.",
        icon_path="icons/weapons/axes/bonebreaker.png",
        rarity=Rarity.EPIC,
        base_damage=35,
        attack_speed=0.7,
        critical_chance=0.12,
        critical_multiplier=2.2,
        scaling_stats={"strength": 0.5}
    )
]

# ================== КОСЫ ==================

SCYTHES = [
    Weapon(
        item_id="scythe_basic",
        name="Коса",
        description="Острая коса, переоборудованная из рабочего инструмента в оружие.",
        icon_path="icons/weapons/scythes/scythe_basic.png",
        rarity=Rarity.UNCOMMON,
        base_damage=20,
        attack_speed=0.9,
        critical_chance=0.10,
        critical_multiplier=2.0,
        scaling_stats={"dexterity": 0.2}
    ),
    Weapon(
        item_id="scythe_reaper",
        name="Жнец",
        description="Боевой клинок-коса, внушающий ужас своим видом.",
        icon_path="icons/weapons/scythes/reaper.png",
        rarity=Rarity.EPIC,
        base_damage=30,
        attack_speed=1.0,
        critical_chance=0.15,
        critical_multiplier=2.3,
        scaling_stats={"dexterity": 0.3, "intelligence": 0.2}
    ),
    Weapon(
        item_id="scythe_soul_harvester",
        name="Собиратель душ",
        description="Древняя коса, о которой говорят, что она пленяет души поверженных врагов.",
        icon_path="icons/weapons/scythes/soul_harvester.png",
        rarity=Rarity.LEGENDARY,
        base_damage=40,
        attack_speed=1.1,
        critical_chance=0.25,
        critical_multiplier=2.5,
        scaling_stats={"dexterity": 0.4, "intelligence": 0.3, "spirit": 0.2}
    )
]

#====================== Броня ==========================
ARMOR_SET = [
    Armor(
        item_id="armor_iron_helmet",
        name="Железный шлем",
        description="Простой железный шлем, обеспечивающий базовую защиту головы.",
        icon_path="",
        rarity=Rarity.COMMON,
        armor_type="helmet",
        defense=8,
    ),
    Armor(
        item_id="armor_iron_chest",
        name="Железная кираса",
        description="Тяжёлая железная кираса, надёжно защищающая торс.",
        icon_path="",
        rarity=Rarity.COMMON,
        armor_type="chest",
        defense=15,
    ),
    Armor(
        item_id="armor_iron_gloves",
        name="Железные перчатки",
        description="Железные перчатки, защищающие кисти рук.",
        icon_path="",
        rarity=Rarity.COMMON,
        armor_type="gloves",
        defense=5,
    ),
    Armor(
        item_id="armor_iron_boots",
        name="Железные сапоги",
        description="Тяжёлые железные сапоги для защиты ног.",
        icon_path="",
        rarity=Rarity.COMMON,
        armor_type="boots",
        defense=6,
        speed_bonus=-0.5  # Легкая потеря скорости из-за веса
    ),
    Armor(
        item_id="armor_dragon_scale",
        name="Доспех из драконьей чешуи",
        description="Легендарный доспех, созданный из чешуи древнего дракона.",
        icon_path="icons/armor/dragon_scale.png",
        rarity=Rarity.LEGENDARY,
        armor_type="chest",
        defense=30,
        health_bonus=50,
        speed_bonus=1.0
    ),
]
#====================== Зелья ==========================

#===================== Здоровье ========================

HEALTH_POTIONS = [
    Consumable(
        item_id="small_health_potion",
        name="Маленькое зелье здоровья",
        description="Маленькое зелье, восстанавливающее до 10 ед. здоровья.",
        icon_path="icons/potions/health_potion_small.png",
        rarity=Rarity.COMMON,
        effect_type="health",
        effect_value=10
    ),
    Consumable(
        item_id="medium_health_potion",
        name="Среднее зелье здоровья",
        description="Зелье среднего размера, восстанавливающее до 25 ед. здоровья.",
        icon_path="icons/potions/health_potion_medium.png",
        rarity=Rarity.UNCOMMON,
        effect_type="health",
        effect_value=25
    ),
    Consumable(
        item_id="big_health_potion",
        name="Большое зелье здоровья",
        description="Крупное зелье, восстанавливающее до 50 ед. здоровья.",
        icon_path="icons/potions/health_potion_big.png",
        rarity=Rarity.RARE,
        effect_type="health",
        effect_value=50
    ),
]
#===================== Скорость ========================
SPEED_POTIONS = [
    Consumable(
        item_id="small_speed_potion",
        name="Маленькое зелье скорости",
        description="Ненадолго немного увеличивает скорость передвижения.",
        icon_path="icons/potions/speed_potion_small.png",
        rarity=Rarity.UNCOMMON,
        effect_type="speed",
        effect_value=2,
        duration=30.0
    ),
    Consumable(
        item_id="medium_speed_potion",
        name="Среднее зелье скорости",
        description="Умеренно повышает скорость передвижения на средний промежуток времени.",
        icon_path="icons/potions/speed_potion_medium.png",
        rarity=Rarity.EPIC,
        effect_type="speed",
        effect_value=4,
        duration=45.0
    ),
    Consumable(
        item_id="big_speed_potion",
        name="Большое зелье скорости",
        description="Сильно увеличивает скорость передвижения на продолжительное время.",
        icon_path="icons/potions/speed_potion_big.png",
        rarity=Rarity.LEGENDARY,
        effect_type="speed",
        effect_value=6,
        duration=60.0
    ),
]
#===================== Выносливость ========================
STAMINA_POTIONS = [
    Consumable(
        item_id="small_stamina_potion",
        name="Маленькое зелье выносливости",
        description="Немного восстанавливает запас выносливости.",
        icon_path="icons/potions/stamina_potion_small.png",
        rarity=Rarity.UNCOMMON,
        effect_type="stamina",
        effect_value=15
    ),
    Consumable(
        item_id="medium_stamina_potion",
        name="Среднее зелье выносливости",
        description="Восстанавливает заметную часть выносливости.",
        icon_path="icons/potions/stamina_potion_medium.png",
        rarity=Rarity.RARE,
        effect_type="stamina",
        effect_value=30
    ),
    Consumable(
        item_id="big_stamina_potion",
        name="Большое зелье выносливости",
        description="Существенно восполняет запас выносливости.",
        icon_path="icons/potions/stamina_potion_big.png",
        rarity=Rarity.EPIC,
        effect_type="stamina",
        effect_value=50
    ),
]
