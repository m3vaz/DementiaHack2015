from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
uri = r"db2+ibm_db://user09971:WDKGhAo60wFY@75.126.155.153:50000/SQLDB"
engine = create_engine(uri, convert_unicode=True)
session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = session.query_property()

def init_db():
	
	# run to create all models
	from models import Beacon, Location
	Base.metadata.create_all(bind=engine)
	Beacon.query.delete()
	Location.query.delete()
	
	b1 = Beacon(uuid = '0x0001', x = 0, y = 0)
	b2 = Beacon(uuid = '0x0002', x = 0, y = 5)
	b3 = Beacon(uuid = '0x0003', x = 5, y = 0)
	
	get_session().add_all([b1,b2,b3])
	get_session().commit()
	
def get_session():
	return session;

def get_connection():
	con = engine.connect()
	return con