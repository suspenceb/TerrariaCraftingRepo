-- Some relations have "SERIAL UNIQUE" to make Primary key increment by 1
-- Others don't have "SERIAL UNIQUE" b/c primary key is a composite key made of foreign keys

-- TODO: Add relevant business logic. So checks about the # of items a player can have equipped, etc.
CREATE TABLE Account
(
  UserId SERIAL UNIQUE NOT NULL,
  Username VARCHAR(20) NOT NULL CHECK (LENGTH(Username) < 20),
  PasswordHash VARCHAR NOT NULL,
  PRIMARY KEY (UserId)
);

CREATE TABLE Weapon
(
  WeaponId SERIAL UNIQUE NOT NULL,
  WeaponName VARCHAR NOT NULL,
  WeaponDesc VARCHAR NOT NULL,
  ImageURL VARCHAR NOT NULL,
  ObtainMethod VARCHAR NOT NULL,
  StatAttack VARCHAR NOT NULL,
  PRIMARY KEY (WeaponId)
);

CREATE TABLE Armor
(
  ArmorId SERIAL UNIQUE NOT NULL,
  ArmorName VARCHAR NOT NULL,
  ArmorDesc VARCHAR NOT NULL,
  ImageURL VARCHAR NOT NULL,
  StatDefense INT NOT NULL,
  ObtainMethod VARCHAR NOT NULL,
  ArmorSlot INT NOT NULL,
  StatBonus VARCHAR,
  PRIMARY KEY (ArmorId)
);

CREATE TABLE Accessory
(
  AccessoryId SERIAL UNIQUE NOT NULL,
  AccessoryName VARCHAR NOT NULL,
  AccessoryDesc VARCHAR NOT NULL,
  StatBonus VARCHAR,
  ObtainMethod VARCHAR NOT NULL,
  ImageURL VARCHAR NOT NULL,
  PRIMARY KEY (AccessoryId)
);

CREATE TABLE Advancement
(
  AdvancementId SERIAL UNIQUE NOT NULL,
  Name VARCHAR NOT NULL,
  PRIMARY KEY (AdvancementId)
);

CREATE TABLE UnlocksWeapon
(
  AdvancementId INT NOT NULL,
  WeaponId INT NOT NULL,
  PRIMARY KEY (AdvancementId, WeaponId),
  FOREIGN KEY (AdvancementId) REFERENCES Advancement(AdvancementId),
  FOREIGN KEY (WeaponId) REFERENCES Weapon(WeaponId)
);

CREATE TABLE UnlocksAccessory
(
  AdvancementId INT NOT NULL,
  AccessoryId INT NOT NULL,
  PRIMARY KEY (AdvancementId, AccessoryId),
  FOREIGN KEY (AdvancementId) REFERENCES Advancement(AdvancementId),
  FOREIGN KEY (AccessoryId) REFERENCES Accessory(AccessoryId)
);

CREATE TABLE UnlocksArmor
(
  AdvancementId INT NOT NULL,
  ArmorId INT NOT NULL,
  PRIMARY KEY (AdvancementId, ArmorId),
  FOREIGN KEY (AdvancementId) REFERENCES Advancement(AdvancementId),
  FOREIGN KEY (ArmorId) REFERENCES Armor(ArmorId)
);

CREATE TABLE Character
(
  CharId SERIAL UNIQUE NOT NULL,
  CharName VARCHAR(20) NOT NULL CHECK (LENGTH(CharName) < 20),
  UserId INT NOT NULL,
  WeaponId INT,
  PRIMARY KEY (CharId),
  FOREIGN KEY (UserId) REFERENCES Account(UserId),
  FOREIGN KEY (WeaponId) REFERENCES Weapon(WeaponId)
);

CREATE TABLE Completes
(
  CharId INT NOT NULL,
  AdvancementId INT NOT NULL,
  PRIMARY KEY (CharId, AdvancementId),
  FOREIGN KEY (CharId) REFERENCES Character(CharId),
  FOREIGN KEY (AdvancementId) REFERENCES Advancement(AdvancementId)
);

CREATE TABLE Equips
(
  CharId INT NOT NULL,
  AccessoryId INT NOT NULL,
  PRIMARY KEY (CharId, AccessoryId),
  FOREIGN KEY (CharId) REFERENCES Character(CharId),
  FOREIGN KEY (AccessoryId) REFERENCES Accessory(AccessoryId)
);

CREATE TABLE Wears
(
  CharId INT NOT NULL,
  ArmorId INT NOT NULL,
  PRIMARY KEY (CharId, ArmorId),
  FOREIGN KEY (CharId) REFERENCES Character(CharId),
  FOREIGN KEY (ArmorId) REFERENCES Armor(ArmorId)
);
