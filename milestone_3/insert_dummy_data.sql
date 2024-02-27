-- Accessories
INSERT INTO "main"."Accessory"
("AccessoryId", "AccessoryName", "AccessoryDesc", "StatBonus", "ObtainMethod", "ImageURL")
VALUES (1, 'Band of Regeneration', 'Slowly regenerates life', 'Regenerate 1 health/second', 'LOOT::Gold Chests in Underground and Cavern and in Living Mahogany Trees in the Underground Jungle.', 'https://terraria.wiki.gg/images/0/0f/Band_of_Regeneration.png');

INSERT INTO "main"."Accessory"
("AccessoryId", "AccessoryName", "AccessoryDesc", "StatBonus", "ObtainMethod", "ImageURL")
VALUES (2, 'Discount Card', 'Shops prices lowered by 20%', 'Shops prices lowered by 20%', 'EVENT:: Pirate Invasion', 'https://terraria.wiki.gg/images/e/ef/Discount_Card.png');

INSERT INTO "main"."Accessory"
("AccessoryId", "AccessoryName", "AccessoryDesc", "StatBonus", "ObtainMethod", "ImageURL")
VALUES (3, 'Yoyo Bag', 'Gives the user master yoyo skills', 'Allows the holder to use two yoyos, similar to the Yoyo Glove along with two Counterweights and also increases the yoyo''s range', 'CRAFTING:: 1x - White String, 1x - Yoyo Gove, 1x - Counterweight', 'https://terraria.wiki.gg/images/8/8d/Yoyo_Bag.png');

-- Armor
INSERT INTO "main"."Armor"
("ArmorId", "ArmorName", "ArmorDesc", "ImageURL", "StatDefense", "ObtainMethod", "ArmorSlot", "StatBonus")
VALUES (1, 'Meteor Helmet', 'DESCRIPTION', 'https://terraria.wiki.gg/images/3/36/Meteor_Helmet.png', 5, 'Crafting:: 10 Meteorite Bars', 3, '9% increased magic damage');

INSERT INTO "main"."Armor"
("ArmorId", "ArmorName", "ArmorDesc", "ImageURL", "StatDefense", "ObtainMethod", "ArmorSlot", "StatBonus")
VALUES (2, 'Meteor Suit', 'DESCRIPTION', 'https://terraria.wiki.gg/images/b/be/Meteor_Suit.png', 6, 'Crafting:: 20 Meteorite Bars', 2, '9% increased magic damage');

INSERT INTO "main"."Armor"
("ArmorId", "ArmorName", "ArmorDesc", "ImageURL", "StatDefense", "ObtainMethod", "ArmorSlot", "StatBonus")
VALUES (3, 'Meteor Leggings', 'DESCRIPTION', 'https://terraria.wiki.gg/images/e/e5/Meteor_Leggings.png', 5, 'Crafting:: 15 Meteorite Bars', 1, '9% increased magic damage');

INSERT INTO "main"."Armor"
("ArmorId", "ArmorName", "ArmorDesc", "ImageURL", "StatDefense", "ObtainMethod", "ArmorSlot", "StatBonus")
VALUES (4, 'Ninja Hood', 'DESCRIPTION', 'https://terraria.wiki.gg/images/c/c4/Ninja_Hood.png', 2, 'BOSS::33.33% chance King Slime', 3, '3% increased critical strike chance');

INSERT INTO "main"."Armor"
("ArmorId", "ArmorName", "ArmorDesc", "ImageURL", "StatDefense", "ObtainMethod", "ArmorSlot", "StatBonus")
VALUES (5, 'Ninja Shirt', 'DESCRIPTION', 'https://terraria.wiki.gg/images/f/f9/Ninja_Shirt.png', 4, 'BOSS::33.33% chance King Slime', 2, '3% increased critical strike chance');

INSERT INTO "main"."Armor"
("ArmorId", "ArmorName", "ArmorDesc", "ImageURL", "StatDefense", "ObtainMethod", "ArmorSlot", "StatBonus")
VALUES (6, 'Ninja Pants', 'DESCRIPTION', 'https://terraria.wiki.gg/images/a/ad/Ninja_Pants.png', 3, 'BOSS::33.33% chance King Slime', 1, '3% increased critical strike chance');

-- Weapons
INSERT INTO "main"."Weapon"
("WeaponId", "WeaponName", "WeaponDesc", "ImageURL", "ObtainMethod", "StatDamage", "StatKnockback", "StatCritChance", "StatUseTime")
VALUES (1, 'Copper Broadsword', '', 'https://terraria.wiki.gg/images/c/cb/Copper_Broadsword.png', 'Crafting:: 6 Copper Bars', '9 Damage', '5.5 Knockback', '4%', '21');

INSERT INTO "main"."Weapon"
("WeaponId", "WeaponName", "WeaponDesc", "ImageURL", "ObtainMethod", "StatDamage", "StatKnockback", "StatCritChance", "StatUseTime")
VALUES (2, 'Meowmere', 'DESCRIPTION', 'https://terraria.wiki.gg/images/6/63/Meowmere.png', 'BOSS:: 22.2% chance Moon Lord', '200', '6.5', '4%', '14');

INSERT INTO "main"."Weapon"
("WeaponId", "WeaponName", "WeaponDesc", "ImageURL", "ObtainMethod", "StatDamage", "StatKnockback", "StatCritChance", "StatUseTime")
VALUES (3, 'Molten Hamaxe', 'DESCRIPTION', 'https://terraria.wiki.gg/images/d/d8/Molten_Hamaxe.png', 'Crafting:: 15 Hellstone bars', '20', '7', '4%', '14');

INSERT INTO "main"."Weapon"
("WeaponId", "WeaponName", "WeaponDesc", "ImageURL", "ObtainMethod", "StatDamage", "StatKnockback", "StatCritChance", "StatUseTime")
VALUES (4, 'Nettle Burst', 'Ignores 10 points of enemy Defense', 'https://terraria.wiki.gg/images/9/98/Nettle_Burst.png', 'BOSS: Plantera', '35', '1', '4%', '25');

-- Advancements
INSERT INTO "main"."Advancement"
("AdvancementId", "Name")
VALUES (1, 'Enter Hardmode');

INSERT INTO "main"."Advancement"
("AdvancementId", "Name")
VALUES (2, 'Defeat Moon Lord');

INSERT INTO "main"."Advancement"
("AdvancementId", "Name")
VALUES (3, 'Defeat Plantera');

INSERT INTO "main"."Advancement"
("AdvancementId", "Name")
VALUES (4, 'Defeat the Eater of Worlds/Brain of Cthulhu');

-- UnlocksAccessory
INSERT INTO "main"."UnlocksAccessory"
("AdvancementId", "AccessoryId")
VALUES (1, 2);

-- UnlocksArmor
INSERT INTO "main"."UnlocksArmor"
("AdvancementId", "ArmorId")
VALUES (4, 1);

INSERT INTO "main"."UnlocksArmor"
("AdvancementId", "ArmorId")
VALUES (4, 2);

INSERT INTO "main"."UnlocksArmor"
("AdvancementId", "ArmorId")
VALUES (4, 3);

-- UnlocksWeapon
INSERT INTO "main"."UnlocksWeapon"
("AdvancementId", "WeaponId")
VALUES (1, 2);

INSERT INTO "main"."UnlocksWeapon"
("AdvancementId", "WeaponId")
VALUES (2, 2);

INSERT INTO "main"."UnlocksWeapon"
("AdvancementId", "WeaponId")
VALUES (1, 4);

INSERT INTO "main"."UnlocksWeapon"
("AdvancementId", "WeaponId")
VALUES (3, 4);

-- Account
INSERT INTO "main"."Account"
("UserId", "Username", "PasswordHash")
VALUES (1, 'Albert', 'friedChicken');

INSERT INTO "main"."Account"
("UserId", "Username", "PasswordHash")
VALUES (2, 'Jay', 'securityToken');

-- Character
INSERT INTO "main"."Character"
("CharId", "CharName", "UserId", "WeaponId")
VALUES (1, 'MonsterHunter', 1, 2); -- Belongs to Albert, has Meowmere

INSERT INTO "main"."Character"
("CharId", "CharName", "UserId", "WeaponId")
VALUES (2, 'Dave', 1, 3); -- Belongs to Albert, has Molten Hamaxe

INSERT INTO "main"."Character"
("CharId", "CharName", "UserId")
VALUES (3, 'BOI', 2); -- Belongs to Jay, has no weapon

-- Completes
INSERT INTO "main"."Completes"
("CharId", "AdvancementId")
VALUES (1, 1); -- MonsterHunter has entered hardmode

INSERT INTO "main"."Completes"
("CharId", "AdvancementId")
VALUES (1, 2); -- MonsterHUnter has defeated Moon Lord

INSERT INTO "main"."Completes"
("CharId", "AdvancementId")
VALUES (2, 4); -- Dave has defeated Eater of Worlds

-- Equips
INSERT INTO "main"."Equips"
("CharId", "AccessoryId")
VALUES (1, 2); -- MonsterHunter has a Discout Card

INSERT INTO "main"."Equips"
("CharId", "AccessoryId")
VALUES (1, 1); -- MonsterHunter has a Band of Regeneration

INSERT INTO "main"."Equips"
("CharId", "AccessoryId")
VALUES (3, 3); -- BOI has a yo-yo bag

-- Wears
-- Give MonsterHunter full set of Ninja Armor
INSERT INTO "main"."Wears"
("CharId", "ArmorId")
VALUES (1, 4);

INSERT INTO "main"."Wears"
("CharId", "ArmorId")
VALUES (1, 5);

INSERT INTO "main"."Wears"
("CharId", "ArmorId")
VALUES (1, 6);

-- Give Dave a full set of Meteor Armor
INSERT INTO "main"."Wears"
("CharId", "ArmorId")
VALUES (2, 1);

INSERT INTO "main"."Wears"
("CharId", "ArmorId")
VALUES (2, 2);

INSERT INTO "main"."Wears"
("CharId", "ArmorId")
VALUES (2, 3);