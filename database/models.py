from dataclasses import dataclass
from pydal import Field
from .dbfile import db

db.define_table('users',
    Field('user_id', 'integer'),  # Your unique ID
    Field('name' , 'str'),
    Field('phone'),
    Field('balance', 'float', default=0.0)
)

# 2. Transactions (all money movements)
db.define_table('transactions',
    Field('user_id', "reference users"),  # Link to users
    Field('type'),                 # 'airtime', 'data', 'call', 'message'
    Field('amount', 'float'),
    Field('status'),               # 'success', 'failed'
    Field('timestamp', 'datetime')
)

# 3. Airtime purchases
db.define_table('airtime',
    Field('user_id', 'integer'),
    Field('phone_number'),
    Field('amount', 'float'),
    Field('network'),              # MTN, Glo, etc
    Field('timestamp', 'datetime')
)

# 4. Data purchases
db.define_table('data',
    Field('user_id', 'integer'),
    Field('phone_number'),
    Field('plan' , 'str'),                 # '1GB', '2GB'
    Field('amount', 'float'),
    Field('network' , 'str'),
    Field('timestamp', 'datetime')
)

# 5. Calls/Messages log
db.define_table('logs',
    Field('user_id', 'integer'),
    Field('receiver'),
    Field('cost', 'float'),
    Field('timestamp', 'datetime')
)
db.transactions.user_id.index = True
db.airtime.user_id.index = True
db.data.user_id.index = True
db.logs.user_id.index = True
db.commit()




@dataclass()
class DatabaseClass:
    def __init__(self):
        self.__user_id 
    def set_user_id(self , user_id):
        self.__user_id = user_id
    def insert_users(self , name , phone):
       user_data = db.users.insert(
            name=name,
            phone=phone,
            balance=0
        )
       db.commit()
       self.set_user_id(user_data)
    def insert_transaction (self , transaction_type, amount, status , transact_time):
        db.transactions.insert( user_id = self.__user_id , type = transaction_type , amount = amount , status = status , timestamp = transact_time );
        db.commit()
    def data_purchase(self , phone_number , plan : str , amount : float , network : str , transact_time) :
        db.data.insert(user_id = self.__user_id , phone_number= phone_number , plan = plan , amount = amount , network = network , timestamp=transact_time )
        db.commit()
    def airtime_purchase(self , phone_number : str , amount : float , network : str  , transact_time):
        db.airtime.insert( user_id = self.__user_id , phone_number = phone_number , amount  = amount, network = network, timestamp = transact_time)
        db.commit()
    def logs_insert(self , message : str , reciever , cost , transact_time) :
        db.logs.insert(user_id = self.__user_id , message = message ,  reciever = reciever , msg_cost = cost , timestamp = transact_time )
        db.commit()
    def update_balance(self, amount: float, operation: str):
        user = db.users(self.__user_id)

        if not user:
            raise Exception("User not found")

        if operation == "credit":
            new_balance = user.balance + amount
        elif operation == "debit":
            if user.balance < amount:
                raise Exception("Insufficient balance")
            new_balance = user.balance - amount
        else:
            raise Exception("Invalid operation")

        user.update_record(balance=new_balance)
        db.commit()