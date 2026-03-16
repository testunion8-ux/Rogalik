from item import Item, Rarity
# ================  Оружие  ===================

# ================== МЕЧИ ==================

SWORDS = [
    Item(
        item_id="sword_rapira",
        name="Рапира",
        description="Лёгкий и быстрый клинок, идеален для точных ударов.",
        rarity=Rarity.UNCOMMON,
    ), Item(
        item_id="sword_sablia",
        name="Сабля",
        description="Изогнутый клинок, эффективен в рубящих атаках.",
        rarity=Rarity.COMMON,
    ), Item(
        item_id="sword_hope_of_kingdom",
        name="Надежда королевства",
        description="Легендарный меч, символ воли королевства и его защитников.",
        rarity=Rarity.LEGENDARY,
    )
]
# ================== ТОПОРЫ ==================

AXES = [
    Item(
        item_id="axe_one_handed",
        name="Одноручный топор",
        description="Простой боевой топор, удобный в одной руке.",
        rarity=Rarity.COMMON,
    ), Item(
        item_id="axe_two_handed",
        name="Двуручный топор",
        description="Тяжёлый топор, наносящий сокрушительные удары.",
        rarity=Rarity.RARE,
    ), Item(
        item_id="axe_bonebreaker",
        name="Костолом",
        description="Мощный топор, разбивающий кости и доспехи одним ударом.",
        rarity=Rarity.EPIC,
    )
]
# ================== КОСЫ ==================

SCYTHES = [
    Item(
        item_id="scythe_basic",
        name="Коса",
        description="Острая коса, переоборудованная из рабочего инструмента в оружие.",
        rarity=Rarity.UNCOMMON,
    ),
    Item(
        item_id="scythe_reaper",
        name="Жнец",
        description="Боевой клинок-коса, внушающий ужас своим видом.",
        rarity=Rarity.EPIC,
    ),
    Item(
        item_id="scythe_soul_harvester",
        name="Собиратель душ",
        description="Древняя коса, о которой говорят, что она пленяет души поверженных врагов.",
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
        rarity=Rarity.COMMON,
    ),
    Item(
        item_id="medium_health_potion",
        name="Среднее зелье здоровья",
        description="Зелье среднего размера, восстанавливающее до 25 ед. здоровья.",
        rarity=Rarity.UNCOMMON,
    ),
    Item(
        item_id="big_health_potion",
        name="Большое зелье здоровья",
        description="Крупное зелье, восстанавливающее до 50 ед. здоровья.",
        rarity=Rarity.RARE,
    ),
]
# Зелья скорости
SPEED_potion = [
    Item(
        item_id="small_speed_potion",
        name="Маленькое зелье скорости",
        description="Ненадолго немного увеличивает скорость передвижения.",
        rarity=Rarity.UNCOMMON,
    ),
    Item(
        item_id="medium_speed_potion",
        name="Среднее зелье скорости",
        description="Умеренно повышает скорость передвижения на средний промежуток времени.",
        rarity=Rarity.EPIC,
    ),
    Item(
        item_id="big_speed_potion",
        name="Большое зелье скорости",
        description="Сильно увеличивает скорость передвижения на продолжительное время.",
        rarity=Rarity.LEGENDARY,
    ),
]
# Зелья восстановления выносливости
STAMINA_potion = [
    Item(
        item_id="small_stamina_potion",
        name="Маленькое зелье выносливости",
        description="Немного восстанавливает запас выносливости.",
        rarity=Rarity.UNCOMMON,
    ),
    Item(
        item_id="medium_stamina_potion",
        name="Среднее зелье выносливости",
        description="Восстанавливает заметную часть выносливости.",
        rarity=Rarity.RARE,
    ),
    Item(
        item_id="big_stamina_potion",
        name="Большое зелье выносливости",
        description="Существенно восполняет запас выносливости.",
        rarity=Rarity.EPIC,
    ),
]
