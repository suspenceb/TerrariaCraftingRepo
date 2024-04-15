# Installing the Terraria Repository

### Prerequisites

Before installing the Terraria repository, ensure you are using a computer with git and docker installed.

### Cloning the Repository

1. Navigate to the directory where you would like to store resources for the repository
2. Clone the repository with `git clone https://github.com/suspenceb/TerrariaCraftingRepo.git`
3. Navigate into the created `TerrariaCraftingRepo` folder, then navigate to the `Website` folder. All future commands will be run from this context.

### Setting Variables

1. Rename `example.env` to `.env`.
2. Open `.env` with a text editor.
3. Change the `DB_PASSWORD` value to a secure alphanumeric string. Remember this value, you will need it later.
4. Change the `SECRET` value to a secure alphanumeric string.
5. Save `.env` and open `docker-compose.yml`
6. Set `MYSQL_ROOT_PASSWORD` to be equal to the password set in step 3.
7. (Optional) Change the first number on the port line if you want the server to run on a port other than 80
8. Save `docker-compose.yml`

### Starting the Server

1. Run `docker compose up` to start the server.
2. Navigate to the IP of your server to access the repo.
