-- Statements 0-7 exist to create view #7, which is a table of all the items that have been equipped
-- This table helps us to create the 'My Character' view, since we can query it by the player's ID
--      to get a list of all the items that the player has.


-- The VIEWs that JOIN the tables of existing items with the tables of what's actually equipped
-- 0
CREATE VIEW Wields AS
SELECT CharId, WeaponId FROM TerrariaCharacter

-- 1
CREATE VIEW accessories_equipped AS
SELECT Equips.CharId, Accessory.AccessoryId, AccessoryName, AccessoryDesc, StatBonus, ObtainMethod, ImageURL
FROM Accessory
JOIN Equips ON Accessory.AccessoryId = Equips.AccessoryId;

-- 2
CREATE VIEW weapons_equipped AS
SELECT Wields.CharId, Weapon.WeaponId, WeaponName, WeaponDesc, ImageURL, ObtainMethod, StatDamage, StatKnockback, StatCritChance, StatUseTime
FROM Weapon
JOIN Wields ON Weapon.WeaponId = Wields.WeaponId;

-- 3
CREATE VIEW armors_equipped AS
SELECT Wears.CharId, Armor.ArmorId, ArmorName, ArmorDesc, ImageURL, StatDefense, ObtainMethod, ArmorSlot, StatBonus
FROM Armor
JOIN Wears ON Armor.ArmorId = Wears.ArmorId;

-- The VIEWs that Rename everything to be Union Compatible
-- 4
CREATE VIEW weapons_equipped_unionable AS
    SELECT CharId,
        WeaponId AS ItemId,
        'Weapon' AS ItemType,
        WeaponName AS ItemName,
        WeaponDesc AS ItemDesc,
        ImageURL,
        ObtainMethod,
        StatDamage,
        StatKnockback,
        StatCritChance,
        StatUseTime,
        NULL AS StatBonus,
        NULL AS StatDefense
    FROM weapons_equipped;

-- 5
CREATE VIEW accessories_equipped_unionable AS
    SELECT CharId,
        AccessoryId AS ItemId,
        'Accessory' AS ItemType,
        AccessoryName AS ItemName,
        AccessoryDesc AS ItemDesc,
        ImageURL,
        ObtainMethod,
        NULL AS StatDamage,
        NULL AS StatKnockback,
        NULL AS StatCritChance,
        NULL AS StatUseTime,
        StatBonus,
        NULL AS StatDefense
    FROM accessories_equipped;

-- 6
CREATE VIEW armors_equipped_unionable AS
    SELECT CharId,
        ArmorId AS ItemId,
        'Armor' AS ItemType,
        ArmorName AS ItemName,
        ArmorDesc AS ItemDesc,
        ImageURL,
        ObtainMethod,
        NULL AS StatDamage,
        NULL AS StatKnockback,
        NULL AS StatCritChance,
        NULL AS StatUseTime,
        NULL AS StatBonus,
        StatDefense
    FROM armors_equipped;


-- The VIEW that UNIONs all the items into a single table

-- 7
CREATE VIEW items_equipped AS
    SELECT * FROM weapons_equipped_unionable
    UNION ALL
    SELECT * FROM accessories_equipped_unionable
    UNION ALL
    SELECT * FROM armors_equipped_unionable;

-- The API query that will get the items equipped to a particular character.

-- 8
-- SELECT * FROM items_equipped WHERE items_equipped.CharId = {selected_character_ID_from_API}