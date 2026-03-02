from database.dbfile import db
# """
# Session management core module.
# """
# pass

# db.define_table('users',
#     Field('user_id', 'integer'),  # Your unique ID
#     Field('name'),
#     Field('phone'),
#     Field('balance', 'float', default=0.0)
# )
user_id = db.users.insert(
    name="john",
    phone="hahsed_password",
    balance=300    
)
db.commit()