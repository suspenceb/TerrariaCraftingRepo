DELETE FROM Wears
WHERE CharId IN (1, 2);

DELETE FROM Equips
WHERE CharId IN (1, 3);

DELETE FROM Completes
WHERE CharId IN (1, 2);

DELETE FROM TerrariaCharacter
WHERE CharId IN (1, 2, 3);

DELETE FROM Account
WHERE UserId IN (1, 2);

DELETE FROM UnlocksWeapon
WHERE AdvancementId IN (1, 2, 3);

DELETE FROM UnlocksArmor
WHERE AdvancementId IN (4) AND ArmorId IN (1, 2, 3);

DELETE FROM UnlocksAccessory
WHERE AdvancementId IN (1) AND AccessoryId IN (2);

DELETE FROM Advancement
WHERE AdvancementId IN (1, 2, 3, 4);

DELETE FROM Accessory
WHERE AccessoryId IN (1, 2, 3);

DELETE FROM Armor
WHERE ArmorId IN (1, 2, 3, 4, 5, 6);

DELETE FROM Weapon
WHERE WeaponId IN (1, 2, 3, 4);

