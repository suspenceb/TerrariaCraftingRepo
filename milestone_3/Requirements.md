IT&C 350-001: Database Principles + Applictn

Milestone 3: Update Schema and ERD Diagrams, start Git repo, and Build Database with dummy data
Due: Mar 2, 2024 at 11:59pm
	
Details	Rationale

The purpose of this part of the project is to set up your initial database. We will use PostgreSQL Server, a popular open-source database server that is flexible enough that it should meet the needs of a wide variety of projects. You will also be required to set up a GitHub project as a team and use it to collaborate throughout the semester on the project.
Related Course Learning Outcomes

-	Use conceptual and data models to design and implement distributed database access applications applying current languages, system technologies, and tools.
- Integrate, deploy, and demonstrate operational applications on database system infrastructure. Includes use of DDL, DML, programming interfaces, and UI implementation. [first part of this outcome]
- Learn to collaborate on a project using a content repository.


Procedures

-  XX Download and install the most recent version of MySQL Server on the local machine of at least one group member.
-  XX Export the SQL schema queries that will build the database structure from the https://erdplus.com/ (Links to an external site.) website related to your existing design.
-   XX  Make sure primary keys in your entities use SERIAL as column types so that they're auto-generated and auto-incremented. (This doesn't apply to entities that have primary composite keys)
-   XX  Make sure primary keys are composite for many-to-many relationships. 
-	Make any updates you need to enforce your business rules using CHECKs, foreign key constraints, etc.
-	XX Populate the data with dummy data, so you can test queries and visualize the dataset.
-	XX  Create an account on GitHub if you don't have one. Create a new repository and have all team members join it and make a change to demonstrate that they can contribute.

  
Migrations:


X- Create at least one INSERT script (e.g., to populate the database with dummy data) and one DELETE script (e.g., to depopulate the same data). These are called data migrations.
-	In the future, each change you make will be done via ALTER and ROLLBACK submissions. Later in the semester when you realize you have to modify the database structure, create ALTER scripts (e.g., to add columns) and a corresponding ROLLBACK script. Make sure you name them starting with numbers so you can keep track of the order. These are called schema migrations.
X-	Document the information about connecting to GitHub in your Final Report Template.
X-	Save the initial schema SQL files that build your database to the GitHub repo. This will serve as a backup. Make sure you do not share any confidential information, such as authentication information, publicly on GitHub.
-	Document information about all of the software you have used and how to connect to your database, run the schema script, etc.
- Please add the instructor and TAs to your github account if it is private. 
 
Demo files for INSERT scripts and table creation can be found at https://github.com/OrangeySnicket/350DemoFiles
 
Submit your Project Documentation, updated with new diagrams and SQL code, for points.
