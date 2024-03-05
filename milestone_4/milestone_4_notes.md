# API endpoints needed

API: Login
Sends: username, password
Receives: OK.

API: Register
Sends: username, password
Receives: OK.

API: Home Screen
Sends: filters, which select from our view _TODO_
Receives: A filtered results of available items
Ideas for views:
- We thought about 1 'baseline' view, which includes Union of weapon, armor, and accessories that have _no_ advancements required.
- We thought about 3 'fragment' views that hold just the summary data from the weapon, armor, and accessories tables.

API: My Character
- Sends: user, selected character
- Receives: character name, armor, accessories, stats
- SQL View: TODO - this would be ideal for an SQL VIEW.



