from item import Item, Rarity
# ================  Оружие  ===================

# ================== МЕЧИ ==================

SWORDS = [
    Item(
        item_id="sword_rapira",
        name="Рапира",
        description="Лёгкий и быстрый клинок, идеален для точных ударов.",
        icon_path="icons/weapons/swords/rapira.png",
        rarity=Rarity.UNCOMMON,
    ), Item(
        item_id="sword_sablia",
        name="Сабля",
        description="Изогнутый клинок, эффективен в рубящих атаках.",
        icon_path="icons/weapons/swords/sablia.png",
        rarity=Rarity.COMMON,
    ), Item(
        item_id="sword_hope_of_kingdom",
        name="Надежда королевства",
        description="Легендарный меч, символ воли королевства и его защитников.",
        icon_path="icons/weapons/swords/hope_of_kingdom.png",
        rarity=Rarity.LEGENDARY,
    )
]
# ================== ТОПОРЫ ==================

AXES = [
    Item(
        item_id="axe_one_handed",
        name="Одноручный топор",
        description="Простой боевой топор, удобный в одной руке.",
        icon_path="icons/weapons/axes/one_handed_axe.png",
        rarity=Rarity.COMMON,
    ), Item(
        item_id="axe_two_handed",
        name="Двуручный топор",
        description="Тяжёлый топор, наносящий сокрушительные удары.",
        icon_path="icons/weapons/axes/two_handed_axe.png",
        rarity=Rarity.RARE,
    ), Item(
        item_id="axe_bonebreaker",
        name="Костолом",
        description="Мощный топор, разбивающий кости и доспехи одним ударом.",
        icon_path="icons/weapons/axes/bonebreaker.png",
        rarity=Rarity.EPIC,
    )
]
# ================== КОСЫ ==================

SCYTHES = [
    Item(
        item_id="scythe_basic",
        name="Коса",
        description="Острая коса, переоборудованная из рабочего инструмента в оружие.",
        icon_path="icons/weapons/scythes/scythe_basic.png",
        rarity=Rarity.UNCOMMON,
    ),
    Item(
        item_id="scythe_reaper",
        name="Жнец",
        description="Боевой клинок-коса, внушающий ужас своим видом.",
        icon_path="icons/weapons/scythes/reaper.png",
        rarity=Rarity.EPIC,
    ),
    Item(
        item_id="scythe_soul_harvester",
        name="Собиратель душ",
        description="Древняя коса, о которой говорят, что она пленяет души поверженных врагов.",
        icon_path="icons/weapons/scythes/soul_harvester.png",
        rarity=Rarity.LEGENDARY,
    )
]

#====================== Зелья ==========================

#===================== Здоровье ========================

HEALTH_potion = [
    Item(
        item_id="small_health_potion",
        name="Маленькое зелье здоровья",
        description="Маленькое зелье, восстанавливающее до 10 ед. здоровья.",
        icon_path="icons/potions/health_potion_small.png",
        rarity=Rarity.COMMON,
    ),
    Item(
        item_id="medium_health_potion",
        name="Среднее зелье здоровья",
        description="Зелье среднего размера, восстанавливающее до 25 ед. здоровья.",
        icon_path="icons/potions/health_potion_medium.png",
        rarity=Rarity.UNCOMMON,
    ),
    Item(
        item_id="big_health_potion",
        name="Большое зелье здоровья",
        description="Крупное зелье, восстанавливающее до 50 ед. здоровья.",
        icon_path="icons/potions/health_potion_big.png",
        rarity=Rarity.RARE,
    ),
]
# Зелья скорости
SPEED_potion = [
    Item(
        item_id="small_speed_potion",
        name="Маленькое зелье скорости",
        description="Ненадолго немного увеличивает скорость передвижения.",
        icon_path="icons/potions/speed_potion_small.png",
        rarity=Rarity.UNCOMMON,
    ),
    Item(
        item_id="medium_speed_potion",
        name="Среднее зелье скорости",
        description="Умеренно повышает скорость передвижения на средний промежуток времени.",
        icon_path="icons/potions/speed_potion_medium.png",
        rarity=Rarity.EPIC,
    ),
    Item(
        item_id="big_speed_potion",
        name="Большое зелье скорости",
        description="Сильно увеличивает скорость передвижения на продолжительное время.",
        icon_path="icons/potions/speed_potion_big.png",
        rarity=Rarity.LEGENDARY,
    ),
]
# Зелья восстановления выносливости
STAMINA_potion = [
    Item(
        item_id="small_stamina_potion",
        name="Маленькое зелье выносливости",
        description="Немного восстанавливает запас выносливости.",
        icon_path="icons/potions/stamina_potion_small.png",
        rarity=Rarity.UNCOMMON,
    ),
    Item(
        item_id="medium_stamina_potion",
        name="Среднее зелье выносливости",
        description="Восстанавливает заметную часть выносливости.",
        icon_path="icons/potions/stamina_potion_medium.png",
        rarity=Rarity.RARE,
    ),
    Item(
        item_id="big_stamina_potion",
        name="Большое зелье выносливости",
        description="Существенно восполняет запас выносливости.",
        icon_path="icons/potions/stamina_potion_big.png",
        rarity=Rarity.EPIC,
    ),
]
for potion in HEALTH_potion + SPEED_potion + STAMINA_potion:
    potion.is_stackable = True
    potion.max_stack_size = 10