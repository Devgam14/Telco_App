from pydal import DAL

db = DAL("sqlite://nhs_db" , folder=r"telco_app\database\dbs")
if db:
    print("Connected")