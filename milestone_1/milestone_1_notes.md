## What needs to get done
Describe the purpose and requirements of the project, by:
- Create a Project definition statement (<30 words)
- Identify stakeholders
    - Ask them what they want from this system
- Create High Level requirements, including:
    - Functionality
    - Non-functional, system-design stuff: (don't need to hit every one of these)
        - Security
        - Portability
        - Maintainability
        - Reliability
        - Performance
        - Availability
        - Flexibility
        - Usabilty (e.g. responsive design on mobile and desktop?)
        - Scalability (e.g. 3000 concurrent users)
- Create a lo-fi prototype (of major front-end interface pages)

(Each of these things will be broken into their own section, below)

## Project Definition Statement
_<30 words summarizing goal of system_

**Attempt 1**
Create an equipment preparation system for Terraria players that enables users to discover and create the best combination of equipment for their current in-game situation.

## Stakeholder interviews
Who are Stake holders?
- Terarria players
- And our creation team
Who is going to be maintaining the site
- We are, the creators and maintainers of the site
Data we would like to see
- Crafting trees
- View items
- Items have conditions, such as where you can get them and what section of the game you need to be.

Interview with Mr. Sam
Q: Why do you like Terraria?
A: Lots of bosses and lot of fun equipment. Kill things with yo-yo's
Q: What is the hardest thing about Terraria?
A: Acquiring stuff and getting ready for fights. Need to understand how to get ready.
Q: What would you envision an app of this type could do for you?
A: It could help me understand my options at where I am in the game.
Q: Limitations of current systems?
A: Terraria wiki exists, but you have to browse the wiki. Stats arent shown in a concise form
Q: What features do you want to see?
A: Understand boss difficulties, and crafting trees.
## Functionality Requirements

Home Page Functionality
- Users can see a list of all items available for them to acquire and use under the condition that they have logged in and created a character profile.
- The list of available items changes based on the information provided by users about their Terraria Character.
- Users can view individual items with statistics about each item.
- Users can select an item to add to their list of equipped items.

Character Page Functionality
- Users can record what bosses their character has defeated so far.
- Users can record whether they have entered hardmode or not.
- Users can record what biomes/regions they have discovered in their world so far.
- Users can see the current character statistics with the items they have equipped.

User page Funcionality
- Users can create and select characters
- Users can change their password

## Non-functionality Requirements
Security
- Website protects against XSS
- Website inputs will protect against SQL injections
- Fail2ban (wish list)
Availability
- 95% uptime
Usability
- Mobile/Desktop (wishlist)
- Darkmode

## Lo-fi prototype
