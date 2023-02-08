
LoginSchema = {
    'username': {'type': 'string', 'nullable': False, 'required': True, 'empty': False},
    'password': {'type': 'string', 'nullable': False, 'required': True, 'empty': False}
}

UpdateSchema = {
    'firstname': {'type': 'string', 'nullable': False, 'empty': False},
    'lastname': {'type': 'string', 'nullable': False, 'empty': False},
    'birthdate': {'type': 'string', 'nullable': False, 'empty': False},
    'email': {'type': 'string', 'nullable': False, 'empty': False}
}
