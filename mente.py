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
	
def insert_sample_data():
	from math import sin, cos, pi
	from models import Location
	from datetime import datetime, timedelta
	from decimal import Decimal
	findx = lambda t: Decimal(sin(t) + 2.5).quantize(Decimal('1.000'))
	findy = lambda t: Decimal(cos(t) + 2.5).quantize(Decimal('1.000'))
	t = [x*pi/8 for x in range(0,20)];
	starttime = datetime.now();
	interval = timedelta(seconds=5)
	times = [starttime+interval*x for x in range(0,20)]
	
	locations = []
	for i in range(0,20):
		val = t[i]
		this_time = times[i]
		loc = Location(uuid='0x0000', x=findx(val), y=findy(val), time = this_time)
		locations.append(loc)
		
	get_session().add_all(locations)
	get_session().commit()
	
	
	
def get_session():
	return session;

def get_connection():
	con = engine.connect()
	return con