-- Accessories
INSERT INTO Accessory
(AccessoryId, AccessoryName, StatBonus, ImageURL)
VALUES (1, 'Band of Regeneration', 'Regenerate 1 health/second', 'https://terraria.wiki.gg/images/0/0f/Band_of_Regeneration.png');

INSERT INTO Accessory
(AccessoryId, AccessoryName, StatBonus, ImageURL)
VALUES (2, 'Discount Card', 'Shops prices lowered by 20%', 'https://terraria.wiki.gg/images/e/ef/Discount_Card.png');

INSERT INTO Accessory
(AccessoryId, AccessoryName, StatBonus, ImageURL)
VALUES (3, 'Yoyo Bag', 'Allows the holder to use two yoyos, similar to the Yoyo Glove along with two Counterweights and also increases the yoyo''s range', 'https://terraria.wiki.gg/images/8/8d/Yoyo_Bag.png');

-- Armor
INSERT INTO Armor
(ArmorId, ArmorName, ImageURL, StatDefense, StatBonus, ArmorSlot)
VALUES (1, 'Meteor Helmet', 'https://terraria.wiki.gg/images/3/36/Meteor_Helmet.png', 5, '9% increased magic damage', 3);

INSERT INTO Armor
(ArmorId, ArmorName, ImageURL, StatDefense, StatBonus, ArmorSlot)
VALUES (2, 'Meteor Suit', 'https://terraria.wiki.gg/images/b/be/Meteor_Suit.png', 6, '9% increased magic damage', 2);

INSERT INTO Armor
(ArmorId, ArmorName, ImageURL, StatDefense, StatBonus, ArmorSlot)
VALUES (3, 'Meteor Leggings', 'https://terraria.wiki.gg/images/e/e5/Meteor_Leggings.png', 5, '9% increased magic damage', 1);

INSERT INTO Armor
(ArmorId, ArmorName, ImageURL, StatDefense, StatBonus, ArmorSlot)
VALUES (4, 'Ninja Hood', 'https://terraria.wiki.gg/images/c/c4/Ninja_Hood.png', 2, '3% increased critical strike chance', 3);

INSERT INTO Armor
(ArmorId, ArmorName, ImageURL, StatDefense, StatBonus, ArmorSlot)
VALUES (5, 'Ninja Shirt', 'https://terraria.wiki.gg/images/f/f9/Ninja_Shirt.png', 4, '3% increased critical strike chance', 2);

INSERT INTO Armor
(ArmorId, ArmorName, ImageURL, StatDefense, StatBonus, ArmorSlot)
VALUES (6, 'Ninja Pants', 'https://terraria.wiki.gg/images/a/ad/Ninja_Pants.png', 3, '3% increased critical strike chance', 1);

-- Weapons
INSERT INTO Weapon
(WeaponId, WeaponName, ImageURL, StatDamage, DamageType, StatKnockback, StatCritChance, StatUseTime)
VALUES (1, 'Copper Broadsword', 'https://terraria.wiki.gg/images/c/cb/Copper_Broadsword.png', '9 Damage', 'melee', '5.5 Knockback', '4%', '21');

INSERT INTO Weapon
(WeaponId, WeaponName, ImageURL, StatDamage, DamageType, StatKnockback, StatCritChance, StatUseTime)
VALUES (2, 'Meowmere', 'https://terraria.wiki.gg/images/6/63/Meowmere.png', '200', 'melee', '6.5', '4%', '14');

INSERT INTO Weapon
(WeaponId, WeaponName, ImageURL, StatDamage, DamageType, StatKnockback, StatCritChance, StatUseTime)
VALUES (3, 'Molten Hamaxe', 'https://terraria.wiki.gg/images/d/d8/Molten_Hamaxe.png', '20', 'melee', '7', '4%', '14');

INSERT INTO Weapon
(WeaponId, WeaponName, ImageURL, StatDamage, DamageType, StatKnockback, StatCritChance, StatUseTime)
VALUES (4, 'Nettle Burst', 'https://terraria.wiki.gg/images/9/98/Nettle_Burst.png', '35', 'magic', '1', '4%', '25');

-- Advancements
INSERT INTO Advancement
(AdvancementId, Name)
VALUES (1, 'Enter Hardmode');

INSERT INTO Advancement
(AdvancementId, Name)
VALUES (2, 'Defeat Moon Lord');

INSERT INTO Advancement
(AdvancementId, Name)
VALUES (3, 'Defeat Plantera');

INSERT INTO Advancement
(AdvancementId, Name)
VALUES (4, 'Defeat the Eater of Worlds/Brain of Cthulhu');

-- UnlocksAccessory
INSERT INTO UnlocksAccessory
(AdvancementId, AccessoryId)
VALUES (1, 2);

-- UnlocksArmor
INSERT INTO UnlocksArmor
(AdvancementId, ArmorId)
VALUES (4, 1);

INSERT INTO UnlocksArmor
(AdvancementId, ArmorId)
VALUES (4, 2);

INSERT INTO UnlocksArmor
(AdvancementId, ArmorId)
VALUES (4, 3);

-- UnlocksWeapon
INSERT INTO UnlocksWeapon
(AdvancementId, WeaponId)
VALUES (1, 2);

INSERT INTO UnlocksWeapon
(AdvancementId, WeaponId)
VALUES (2, 2);

INSERT INTO UnlocksWeapon
(AdvancementId, WeaponId)
VALUES (1, 4);

INSERT INTO UnlocksWeapon
(AdvancementId, WeaponId)
VALUES (3, 4);

-- Account
INSERT INTO Account
(UserId, Username, PasswordHash)
VALUES (1, 'Albert', 'friedChicken');

INSERT INTO Account
(UserId, Username, PasswordHash)
VALUES (2, 'Jay', 'securityToken');

-- TerrariaCharacter
INSERT INTO TerrariaCharacter
(CharId, CharName, UserId, WeaponId)
VALUES (1, 'MonsterHunter', 1, 2); -- Belongs to Albert, has Meowmere

INSERT INTO TerrariaCharacter
(CharId, CharName, UserId, WeaponId)
VALUES (2, 'Dave', 1, 3); -- Belongs to Albert, has Molten Hamaxe

INSERT INTO TerrariaCharacter
(CharId, CharName, UserId)
VALUES (3, 'BOI', 2); -- Belongs to Jay, has no weapon

-- Completes
INSERT INTO Completes
(CharId, AdvancementId)
VALUES (1, 1); -- MonsterHunter has entered hardmode

INSERT INTO Completes
(CharId, AdvancementId)
VALUES (1, 2); -- MonsterHUnter has defeated Moon Lord

INSERT INTO Completes
(CharId, AdvancementId)
VALUES (2, 4); -- Dave has defeated Eater of Worlds

-- Equips
INSERT INTO Equips
(CharId, AccessoryId)
VALUES (1, 2); -- MonsterHunter has a Discout Card

INSERT INTO Equips
(CharId, AccessoryId)
VALUES (1, 1); -- MonsterHunter has a Band of Regeneration

INSERT INTO Equips
(CharId, AccessoryId)
VALUES (3, 3); -- BOI has a yo-yo bag

-- Wears
-- Give MonsterHunter full set of Ninja Armor
INSERT INTO Wears
(CharId, ArmorId)
VALUES (1, 4);

INSERT INTO Wears
(CharId, ArmorId)
VALUES (1, 5);

INSERT INTO Wears
(CharId, ArmorId)
VALUES (1, 6);

-- Give Dave a full set of Meteor Armor
INSERT INTO Wears
(CharId, ArmorId)
VALUES (2, 1);

INSERT INTO Wears
(CharId, ArmorId)
VALUES (2, 2);

INSERT INTO Wears
(CharId, ArmorId)
VALUES (2, 3);