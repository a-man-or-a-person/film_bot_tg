from DB.orm import create_tables, insert_workers, admin_insert_film

create_tables()
insert_workers()
admin_insert_film(**{'name': 'Django', 'source_film': 'https://git'})