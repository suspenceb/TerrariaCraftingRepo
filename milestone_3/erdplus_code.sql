-- Comments are made with hyphens
CREATE TABLE Account
(
  UserId INT NOT NULL,
  Username VARCHAR NOT NULL,
  PasswordHash VARCHAR NOT NULL,
  PRIMARY KEY (UserId)
);

CREATE TABLE Weapon
(
  WeaponId INT NOT NULL,
  WeaponName VARCHAR NOT NULL,
  WeaponDesc VARCHAR NOT NULL,
  ImageURL VARCHAR NOT NULL,
  ObtainMethod VARCHAR NOT NULL,
  StatAttack VARCHAR NOT NULL,
  PRIMARY KEY (WeaponId)
);

CREATE TABLE Armor
(
  ArmorId INT NOT NULL,
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
  AccessoryId INT NOT NULL,
  AccessoryName VARCHAR NOT NULL,
  AccessoryDesc VARCHAR NOT NULL,
  StatBonus VARCHAR,
  ObtainMethod VARCHAR NOT NULL,
  ImageURL VARCHAR NOT NULL,
  PRIMARY KEY (AccessoryId)
);

CREATE TABLE Advancement
(
  AdvancementId INT NOT NULL,
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
  CharId INT NOT NULL,
  CharName VARCHAR NOT NULL,
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
