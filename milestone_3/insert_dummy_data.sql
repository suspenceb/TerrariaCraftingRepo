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