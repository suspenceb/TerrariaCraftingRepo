-- THIS IS PSEUDO-SQL. Haven't checked syntax yet, just getting the gist.
SELECT WeaponId, WeaponName, WeaponDesc, ImageURL, ObtainMethod AS "id", "name", "description", "imageURL", "ObtainMethod"
FROM Weapon
WHERE -- Weapon is currently equipped to the character
UNION -- Probably UNION_ALL actually
SELECT AccessoryId, AccessoryName, AccessoryDesc, ImageURL, ObtainMethod AS "id", "name", "description", "imageURL", "ObtainMethod"
FROM Accessory
where -- Accessory is currently equipped to the character

-- The VIEWs that JOIN the tables of available items with the tables of what's actually equipped
-- 0
CREATE VIEW Wields AS
SELECT CharId, WeaponId FROM Character

-- 1
CREATE VIEW accessories_are_equipped AS
SELECT * FROM Accessory, Equips
WHERE Accessory.AccessoryId = Equips.AccessoryId;

-- 2
CREATE VIEW weapons_are_equipped
SELECT * FROM Weapon, Wields
WHERE Weapon.WeaponId = Wields.WeaponId;

-- 3
CREATE VIEW armors_are_equipped
SELECT * FROM Armor, Wears
WHERE Armor.ArmorId = Wears.ArmorId;

-- The VIEWs that Rename everything to be Union Compatible
-- 4

-- 5

-- 6

-- The VIEW that UNIONs all the items into a single table

-- 7

-- The API query that will get the items equipped to a particular character.

-- 8