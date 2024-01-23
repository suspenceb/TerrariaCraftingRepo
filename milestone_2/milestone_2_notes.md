## What needs to get done

### Create an ER Diagram

- Generate a list of all fields to support your requirements. Separate into **core data fields** and **derived data fields**. Show list to stakeholders to verify that you have captured all the data they need.
- Identify the key entities (which will become tables) and associated attributes (which will become fields). Entities should typically have a single focal subject that may be a noun (e.g., Users, Classes, Places, Objects) or a verb (e.g., Purchases, Transactions, Events). Attributes should typically be assigned to just one entity, though foreign keys may be used in a secondary table (e.g., a userid in a Purchases table). Make sure you don’t have unnecessary duplication of fields. Make sure the field names are meaningful and consistently applied throughout.
- Identify a primary key for each table, as well as candidate keys. Also label foreign keys when appropriate.
- Identify the types of relationships between the entities (e.g., tables), and their attributes. And give them names. Identify their cardinality. Identify if they are binary, unary, etc.
- Create an Entity Relational Model using [ERD Plus](https://erdplus.com/) Make sure you create a user account so that your progress isn’t lost. You will be updating this in the future. This will capture the entities, associated attributes, and their relationships to other entities. Make sure you include all the details for each field and entity (e.g., check the appropriate boxes to indicate if a field is unique, multivalued, optional, composite, derived, etc.; and if each entity is regular, associative, or weak).
- Add the ER diagram to the Final Report write-up.

### Create a Relational Schema Diagram

- Start by converting your ER diagram into a Relational Schema diagram using [ERD Plus](https://erdplus.com/). This will give you a starting point, and may help you realize problems with your original ER diagram that you'll want to address before re-converting it again. If you categorized all of your keys, relationship types, etc. properly, then this conversion should get you very close to what you'll need.
- Look at the editor and make sure you change the "data type" for each field to be an appropriate one. This is important to get right, since this tool will automatically generate the SQL queries that will be used to build your database. Notice you can also reorder the fields in a table.
- Add the Relational Schema diagram to the Final Report write-up.

### Create Business Rules

**Prompt**

- Consider what constraints you should place on users or your database fields. What data or actions should be allowed or denied? Under what circumstances? Go through each low-fidelity mockup screen, as well as each field in each table and each relationship to make sure you consider all key constraints. These will become business rules. Consider the following types of constraints:
  - Who can perform which actions?
  - Degree of Participation (is there a min or max number of relationships that must exist?)
  - Is there a default value? If so, what?
  - What limitations should there be for certain data fields? (Length requirements?)
  - What values should never occur? (e.g., negative numbers, creating an event before the current time, etc.)
- Add the Business Rules to the Final Report write-up. (Ensure these are clear and specific, see project description)
- Update your ER diagram and relational schema diagram to reflect any of the rules that can be reflected in them, but were not previously (e.g., required versus optional values; degree of participation…). Not all of your rules can be enforced in the database schema itself; some will be through validation code that you will write or stored procedures that are triggered. This will be done later. Update your Field Name descriptions from your prior assignment to reflect any field-level business rules that were not included originally (e.g., in the Data Type, Key? Optional? Restrictions, and Notes columns).
- Submit the updated FinalReportTemplate.docx, including all sections from the prior assignment after updating them to reflect any changes you have made. It is meant to be a living document that is iteratively improved throughout the semester.

**Response:**

- Users can create as many characters as they wish
- New characters have no items assigned to them
- Characters can equip, at maximum, 1 weapon, 3 armor pieces (head, chestplate, boots), and 6 equipments.
- Users can have 0 or 1 characters selected for viewing relevant items
- The list of items cannot be changed from the front end and will be managed directly in the database by site administrators when needed.
- Usernames can only contain letters and numbers (no special chars)
- Attempts to equip more items than is permitted will not replace prior equipped items (operation will produce an error instead)
- If the user has 0 characters selected, they are unable to equip any items.
- Users can have 0 or more advancements selected when filtering data output
