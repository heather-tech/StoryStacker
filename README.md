# StoryStacker

StoryStacker is a user-friendly command-line interface (CLI) application that allows Book Club leaders to efficiently manage authors and books.   


## Installation
To install and run StoryStacker, ensure that you have Python 3 and pip installed on your system.

1. Clone this repository to your local machine and navigate to its directory.
2. Run `pipenv install` to install all the necessary package dependencies.
3. Run `pipenv shell` to enter the virtual environment.
4. Navigate to the `lib/db` directory and run `python seed.py` to populate the database with mock data.
5. Return to the `lib` directory by running `cd ..`.
6. Run `python cli.py` to start using StoryStacker.

## Using CLI 

Welcome To StoryStacker (Main Menu)
1. Manage Authors 
2. Manage Books 
3. Exit

Author Management (Main Menu Option 1)
1. Create Author
2. Delete Author
3. List Authors
4. Go Back

Book Management (Main Menu Option 2)
1. Create Book
2. Delete Book
3. List Books
4. Go Back



## Visual
[Visual of CLI and Database](https://imgur.com/a/RBSG6Mu)

## Resources

- [SQLite](https://sqlite.org/index.html)
- [SQLALchemy](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/)
- [Faker](https://faker.readthedocs.io/en/master/)
