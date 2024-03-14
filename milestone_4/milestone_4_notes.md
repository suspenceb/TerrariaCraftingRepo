# API endpoints needed

API: Login
    HTTP GET /login/
    Sends: username, password
    Receives: Session Token.

API: Register
    HTTP GET /register/
    Sends: username, password
    Receives: OK.

API: Home Screen
    HTTP GET /home/{filterId1, filterId2, filterId3, ...}
    Sends: filters, which select from our view (and session token)
    Receives: A filtered results of available items
    Ideas for views:
    - We thought about 1 'baseline' view, which includes Union of weapon, armor, and accessories that have _no_ advancements required.
    - We thought about 3 'fragment' views that hold just the summary data from the weapon, armor, and accessories tables.

API: My Character
    HTTP GET /character/{characterId}
    - Sends: characterId, Session
    - Receives: character name, armor, accessories, stats
    - SQL View: TODO - this would be ideal for an SQL VIEW.

API: Account :: Add Character
    HTTP PUT /character/addCharacter/{characterName}

API: Account :: Password Reset

API: GetItem
    HTTP GET /item/{itemType}/{itemId}

API: Modify the Character's data
    Idea 1: PUT request that has the entire character. their name, what items equipped
    Idea 2: PUT request that has a separate API endpoint per table. So to un-equip an item, PUT character/{itemType}/{ItemId}

