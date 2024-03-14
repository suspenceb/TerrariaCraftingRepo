-- The VIEWs that JOIN the tables of available items with the tables of what's actually equipped
-- 0
CREATE VIEW Wields AS
SELECT CharId, WeaponId FROM Character

-- 1
CREATE VIEW accessories_equipped AS
SELECT * FROM Accessory, Equips
WHERE Accessory.AccessoryId = Equips.AccessoryId;

-- 2
CREATE VIEW weapons_equipped
SELECT * FROM Weapon, Wields
WHERE Weapon.WeaponId = Wields.WeaponId;

-- 3
CREATE VIEW armors_equipped
SELECT * FROM Armor, Wears
WHERE Armor.ArmorId = Wears.ArmorId;

-- The VIEWs that Rename everything to be Union Compatible
-- 4
CREATE VIEW weapons_equipped_unionable
    SELECT WeaponId AS ItemId,
        'Weapon' AS ItemType,
        WeaponName AS ItemName,
        WeaponDesc AS ItemDesc,
        ImageURL,
        ObtainMethod,
        StatAttack,
        NULL AS StatBonus
        NULL AS StatDefense
    FROM weapons_are_equipped;

-- 5
CREATE VIEW accessories_equipped_unionable
    SELECT AccessoryId AS ItemId,
        'Accessory' AS ItemType,
        AccessoryName AS ItemName,
        AccessoryDesc AS ItemDesc,
        ImageURL,
        ObtainMethod,
        NULL AS StatAttack,
        StatBonus,
        NULL AS StatDefense
    FROM Accessory;

-- 6
CREATE VIEW armors_equipped_unionable
    SELECT ArmorId AS ItemId,
        'Armor' AS ItemType,
        ArmorName AS ItemName,
        ArmorDesc AS ItemDesc,
        ImageURL,
        ObtainMethod,
        NULL AS StatAttack,
        NULL AS StatBonus,
        StatDefense
    FROM Armor;


-- The VIEW that UNIONs all the items into a single table

-- 7

-- The API query that will get the items equipped to a particular character.

-- 8