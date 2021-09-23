"""
A menu - you need to add the database and fill in the functions.
"""

from peewee import *


def create_tables():
    with database:
        database.create_tables([Player])


db = SqliteDatabase('records.sqlite')


class Player(Model):
    name = CharField()
    country = CharField()
    catches = IntegerField()

    # link model to the database
    class Meta:
        database = db

    def __str__(self):
        # auto increment id
        return f'{self.id}: {self.name} from {self.country} caught {self.catches}'


"connect to database and create table"
db.connect()


def main():
    menu_text = """
    1. Display all records
    2. Add new record
    3. Edit existing record
    4. Delete record
    5. Quit
    """

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            add_new_record()
        elif choice == '3':
            edit_existing_record()
        elif choice == '4':
            delete_record()
        elif choice == '5':
            break
        else:
            print('Not a valid selection, please try again')


def display_all_records():
    """ display all records """
    all_players = Player.select()
    for player in all_players:
        print(player)


def add_new_record():
    """ add new record """
    player_name = input('what is your name: ')
    player_country = input('Name of country: ')
    player_catches = int(input('How many chainsaw did you catch: '))
    new_play = Player.create(name=player_name, country=player_country,
                             catches=player_catches)
    try:
        new_play.save()
        print(f'record added{new_play}')
    except PeeweeException:
        print('Error, player exists')


def edit_existing_record():
    print('todo edit existing record. What if user wants to edit record that does not exist?')
    player_name = input('Enter the name of the catcher')
    player_catches = int(input('Enter how number of catches'))
    rows_modified = Player.update(catches=player_catches).where(
        Player.name == player_name).execute()
    if rows_modified == 0:
        return None
    else:
        rows_modified.save()
        print(rows_modified)


def delete_record():
    """ delete an existing record from the db."""
    delete_row = input('please enter the name you wish to delete')
    record_delete = Player.delete().where(Player.name == delete_row).execute()
    if not record_delete:
        raise PeeweeException(
            'Error!, can\'t delete a book that does not exist')


def search_record():
    search = input('Enter the name of the record holder')
    get_player = Player.get_or_none(Player.name == search)
    print(get_player)


if __name__ == '__main__':
    main()
