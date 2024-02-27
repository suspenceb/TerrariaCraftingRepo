DELETE FROM "main"."Wears"
WHERE "CharId" IN (1, 2);

DELETE FROM "main"."Equips"
WHERE "CharId" IN (1, 3);

DELETE FROM "main"."Completes"
WHERE "CharId" IN (1, 2);

DELETE FROM "main"."Character"
WHERE "CharId" IN (1, 2, 3);

DELETE FROM "main"."Account"
WHERE "UserId" IN (1, 2);

DELETE FROM "main"."UnlocksWeapon"
WHERE "AdvancementId" IN (1, 2, 3);

DELETE FROM "main"."UnlocksArmor"
WHERE "AdvancementId" IN (4) AND "ArmorId" IN (1, 2, 3);

DELETE FROM "main"."UnlocksAccessory"
WHERE "AdvancementId" IN (1) AND "AccessoryId" IN (2);

DELETE FROM "main"."Advancement"
WHERE "AdvancementId" IN (1, 2, 3, 4);

DELETE FROM "main"."Accessory"
WHERE "AccessoryId" IN (1, 2, 3);

DELETE FROM "main"."Armor"
WHERE "ArmorId" IN (1, 2, 3, 4, 5, 6);

DELETE FROM "main"."Weapon"
WHERE "WeaponId" IN (1, 2, 3, 4);

