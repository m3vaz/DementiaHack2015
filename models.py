from sqlalchemy import Table, Column, Integer, Numeric, String, DateTime
from mente import Base

class Beacon(Base):
	__tablename__ = 'beacons'
	id = Column(Integer, primary_key=True)
	uuid = Column(String(8), unique=True, nullable=False)
	x = Column(Numeric(precision=5, scale=3), nullable=False)
	y = Column(Numeric(precision=5, scale=3), nullable=False)
	
	def __init__(self, uuid=None, x=None, y=None):
		self.uuid = uuid
		self.x = x
		self.y = y
		
	def __repr__(self):
		return '<Beacon ' + self.uuid + '>'
		
	
class Location(Base):
	__tablename__ = 'locations'
	id = Column(Integer, primary_key=True)
	uuid = Column(String(8), nullable=False)
	x = Column(Numeric(precision=5, scale=3), nullable=False)
	y = Column(Numeric(precision=5, scale=3), nullable=False)
	time = Column(DateTime, nullable=False)
	
	def __init__(self, uuid=None, x=None, y=None, time=None):
		self.uuid = uuid
		self.x = x
		self.y = y
		self.time = time
		
	def __repr__(self):
		return '<Location ' + self.uuid + ' at ' + self.time + '>'
	