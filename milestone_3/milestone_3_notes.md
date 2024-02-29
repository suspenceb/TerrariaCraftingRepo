
## MySQL server setup
There's a setup script called `sudo mysql_secure_installation` that does some pre-setup.

- [ ] Set up database with a user account.

sudo mysqld_safe --skip-grant-tables &

https://phoenixnap.com/kb/mysql-secure-installation


- [ ] TODO: Document that for ArmorSlot, 1 = Pants 2 = Shirt 3 = Helmet. Consider converting it into an ENUM instead.

## Dummy Data

### Weapons

Copper Broadsword
DESCRIPTION
https://terraria.wiki.gg/images/c/cb/Copper_Broadsword.png
Crafting:: 6 Copper Bars
9 Damage
5.5 Knockback
4% critical chance
21 Use time

Meowmere (hardmode post-Moon Lord)
DESCRIPTION
https://terraria.wiki.gg/images/6/63/Meowmere.png
BOSS:: 22.2% chance Moon Lord
200 damage
6.5 knockback
4% critical chance
14 use time

Molten Hamaxe
DESCRIPTION
https://terraria.wiki.gg/images/d/d8/Molten_Hamaxe.png
Crafting:: 15 Hellstone bars
20 damage
7 knockback
4% critical chance
14 use time

Nettle Burst (Hardmode, post-Plantera)
Ignores 10 points of enemy Defense
https://terraria.wiki.gg/images/9/98/Nettle_Burst.png
BOSS:: Plantera
35 damage
1 knockback
4% critical chance
25 use time

### Armor
Meteor Helmet  (post Eater of Worlds/Brain of Cthulhu defeat)
DESCRIPTION
https://terraria.wiki.gg/images/3/36/Meteor_Helmet.png
5 Defense
Crafting:: 10 Meteorite Bars
Helmet
9% increased magic damage

Meteor Suit
DESCRIPTION
https://terraria.wiki.gg/images/b/be/Meteor_Suit.png
6 Defense
Crafting:: 20 Meteorite Bars
Shirt
9% increased magic damage

Meteor Leggings
DESCRIPTION
https://terraria.wiki.gg/images/e/e5/Meteor_Leggings.png
5 Defense
Crafting:: 15 Meteorite Bars
Pants
9% increased magic damage

Ninja Hood
DESCRIPTION
https://terraria.wiki.gg/images/c/c4/Ninja_Hood.png
2 Defense
BOSS::33.33% chance King Slime
Helmet
3% increased critical strike chance

Ninja Shirt
DESCRIPTION
https://terraria.wiki.gg/images/f/f9/Ninja_Shirt.png
4 Defense
BOSS::33.33% chance King Slime
Shirt
3% increased critical strike chance

Ninja Pants
DESCRIPTION
https://terraria.wiki.gg/images/a/ad/Ninja_Pants.png
3 Defense
BOSS::33.33% chance King Slime
Pants
3% increased critical strike chance

### Accessories

Band of Regeneration
Slowly regenerates life
Regenerate 1 health/second
LOOT::Gold Chests in Underground and Cavern and in Living Mahogany Trees in the Underground Jungle.
https://terraria.wiki.gg/images/0/0f/Band_of_Regeneration.png

Discount Card (hardmode item)
Shops prices lowered by 20%
Shops prices lowered by 20%
EVENT:: Pirate Invasion
https://terraria.wiki.gg/images/e/ef/Discount_Card.png

Yoyo Bag
Gives the user master yoyo skills
Allows the holder to use two yoyos, similar to the Yoyo Glove along with two Counterweights and also increases the yoyo's range
CRAFTING:: 1x - White String, 1x - Yoyo Gove, 1x - Counterweight
https://terraria.wiki.gg/images/8/8d/Yoyo_Bag.png

### Advancements
Enter Hardmode
Defeat Moon Lord
Defeat Plantera
Defeat the Eater of Worlds/Brain of Cthulhu

## Server Connection Instructions
_Information about all of the software you have used and how to connect to your database, run the schema script_
1. Connect to the IT&C VPN
2. Open a command prompt and SSH into the server with:
    ```bash
    ssh username@<ip-address>
    ```
3. Navigate to our Docker folder in `/docker`.


## Server Config details


```bash
# Add everyone to the `docker` group and change group control of that folder.
sudo usermod -a -G docker ethan
sudo usermod -a -G docker suspenceb
sudo usermod -a -G docker sam
sudo usermod -a -G docker mgregg99
sudo usermod -a -G docker student
chgrp -R docker /docker
```
