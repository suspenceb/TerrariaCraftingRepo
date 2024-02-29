-- Some relations have "SERIAL UNIQUE" to make Primary key increment by 1
-- Others don't have "SERIAL UNIQUE" b/c primary key is a composite key made of foreign keys
CREATE TABLE Account
(
  UserId SERIAL UNIQUE NOT NULL,
  Username VARCHAR(20) NOT NULL CHECK (LENGTH(Username) < 20),
  PasswordHash VARCHAR(96) NOT NULL,
  PRIMARY KEY (UserId)
);

CREATE TABLE Weapon
(
  WeaponId SERIAL UNIQUE NOT NULL,
  WeaponName VARCHAR(64) NOT NULL,
  WeaponDesc VARCHAR(64) NOT NULL,
  ImageURL VARCHAR(128) NOT NULL,
  ObtainMethod VARCHAR(256) NOT NULL,
  StatDamage VARCHAR(8),
  StatKnockback VARCHAR(8) ,
  StatCritChance VARCHAR(8),
  StatUseTime VARCHAR(8),
  PRIMARY KEY (WeaponId)
);

CREATE TABLE Armor
(
  ArmorId SERIAL UNIQUE NOT NULL,
  ArmorName VARCHAR(64) NOT NULL,
  ArmorDesc VARCHAR(64) NOT NULL,
  ImageURL VARCHAR(128) NOT NULL,
  StatDefense INT NOT NULL,
  ObtainMethod VARCHAR(256) NOT NULL,
  ArmorSlot INT NOT NULL,
  StatBonus VARCHAR(128),
  PRIMARY KEY (ArmorId)
);

CREATE TABLE Accessory
(
  AccessoryId SERIAL UNIQUE NOT NULL,
  AccessoryName VARCHAR(64) NOT NULL,
  AccessoryDesc VARCHAR(64) NOT NULL,
  StatBonus VARCHAR(256),
  ObtainMethod VARCHAR(256) NOT NULL,
  ImageURL VARCHAR(128) NOT NULL,
  PRIMARY KEY (AccessoryId)
);

CREATE TABLE Advancement
(
  AdvancementId SERIAL UNIQUE NOT NULL,
  Name VARCHAR(64) NOT NULL,
  PRIMARY KEY (AdvancementId)
);

CREATE TABLE UnlocksWeapon
(
  AdvancementId BIGINT UNSIGNED NOT NULL,
  WeaponId BIGINT UNSIGNED NOT NULL,
  PRIMARY KEY (AdvancementId, WeaponId),
  FOREIGN KEY (AdvancementId) REFERENCES Advancement(AdvancementId),
  FOREIGN KEY (WeaponId) REFERENCES Weapon(WeaponId)
);

CREATE TABLE UnlocksAccessory
(
  AdvancementId BIGINT UNSIGNED NOT NULL,
  AccessoryId BIGINT UNSIGNED NOT NULL,
  PRIMARY KEY (AdvancementId, AccessoryId),
  FOREIGN KEY (AdvancementId) REFERENCES Advancement(AdvancementId),
  FOREIGN KEY (AccessoryId) REFERENCES Accessory(AccessoryId)
);

CREATE TABLE UnlocksArmor
(
  AdvancementId BIGINT UNSIGNED NOT NULL,
  ArmorId BIGINT UNSIGNED NOT NULL,
  PRIMARY KEY (AdvancementId, ArmorId),
  FOREIGN KEY (AdvancementId) REFERENCES Advancement(AdvancementId),
  FOREIGN KEY (ArmorId) REFERENCES Armor(ArmorId)
);

CREATE TABLE TerrariaCharacter
(
  CharId SERIAL UNIQUE NOT NULL,
  CharName VARCHAR(20) NOT NULL CHECK (LENGTH(CharName) < 20),
  UserId BIGINT UNSIGNED NOT NULL,
  WeaponId BIGINT UNSIGNED,
  PRIMARY KEY (CharId),
  FOREIGN KEY (UserId) REFERENCES Account(UserId),
  FOREIGN KEY (WeaponId) REFERENCES Weapon(WeaponId)
);

CREATE TABLE Completes
(
  CharId BIGINT UNSIGNED NOT NULL,
  AdvancementId BIGINT UNSIGNED NOT NULL,
  PRIMARY KEY (CharId, AdvancementId),
  FOREIGN KEY (CharId) REFERENCES TerrariaCharacter(CharId),
  FOREIGN KEY (AdvancementId) REFERENCES Advancement(AdvancementId)
);

CREATE TABLE Equips
(
  CharId BIGINT UNSIGNED NOT NULL,
  AccessoryId BIGINT UNSIGNED NOT NULL,
  PRIMARY KEY (CharId, AccessoryId),
  FOREIGN KEY (CharId) REFERENCES TerrariaCharacter(CharId),
  FOREIGN KEY (AccessoryId) REFERENCES Accessory(AccessoryId)
);

CREATE TABLE Wears
(
  CharId BIGINT UNSIGNED NOT NULL,
  ArmorId BIGINT UNSIGNED NOT NULL,
  PRIMARY KEY (CharId, ArmorId),
  FOREIGN KEY (CharId) REFERENCES TerrariaCharacter(CharId),
  FOREIGN KEY (ArmorId) REFERENCES Armor(ArmorId)
);
