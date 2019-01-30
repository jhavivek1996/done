from rolepermissions.roles import AbstractUserRole

class Library(AbstractUserRole):
    available_permissions = {
        'create_library_record': True,
        'edit_library_file': True,
        'add_books':True,
        'remove_books':True,
        ''
    }

