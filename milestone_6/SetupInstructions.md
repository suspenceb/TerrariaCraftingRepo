# Instructions
1. Install and set up an Ubuntu Server (make sure to include Docker).
2. Clone this repository into a folder with appropriate permissions.
    - Change the ownership of the folder to belong to the 'docker' group. For convenience, add your own user to that group.
3. Use the `docker-compose.yml` script in this repo. This will create:
    - A MySQL server using the latest version of MySQL (which, at the time of writing, was 8.3.0)
    - a PHPMyAdmin server
4. Log into the PHPMyAdmin client at `http://<ip-address-of-machine>:8000` in your browser
    1. Complete PHPMyAdmin setup.
    2. Execute the `init_db_code.sql` script to initialize the database schema.
    3. Execute the `create_views.sql` script to create some necessary views.
    4. Use PHPMyAdmin to import all of the `.csv`s in the `DataScraping/` directory.
5. Start up the web server using the Dockerfile in the `Website/` directory.

# TL;DR
```bash
# 1. Install Ubuntu (not shown here)

# 2. Clone our repo and config folder
git clone https://github.com/suspenceb/TerrariaCraftingRepo.git
chgrp -R docker /TerrariaCraftingRepo
sudo usermod -a -G docker $user # Replace `$user` with the name of your user.

# 3. Start up the services
cd TerrariaCraftingRepo/milestone_3/docker-compose.yml
docker compose up -d

# 4. Log into PHPMyAdmin and complete database setup (not shown here)

# 5. Start up the web server
# (in the folder containing the `Dockerfile`)
docker build -t <name-of-image> .
docker run -d -p 8001:8001 <name-of-image>
```

(Services can be turned off with `docker compose down`)
(Information about the current images can be seen with `docker ps`)