from sqlalchemy import Table, Column, Integer, Numeric, String, DateTime
from mente import Base
from datetime import datetime as dt
import json

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
		from decimal import Decimal
		if isinstance(o, Decimal):
			return float(o)
		if isinstance(o, dt):
			return str(o)
		return super(DecimalEncoder, self).default(o)

class Beacon(Base):
	__tablename__ = 'beacons'
	id = Column(Integer, primary_key=True)
	uuid = Column(String(8), unique=True, nullable=False)
	x = Column(Numeric(precision=5, scale=3), nullable=False)
	y = Column(Numeric(precision=5, scale=3), nullable=False)

	def to_json(self):
		temp = {'uuid':self.uuid, 'x':self.x, 'y':self.y}
		return json.dumps(temp, cls=DecimalEncoder)
	
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
	
	def to_json(self):
		temp = {'uuid':self.uuid, 'x':self.x, 'y':self.y, 'time':self.time}
		return json.dumps(temp, cls=DecimalEncoder)
	
	def __init__(self, uuid=None, x=None, y=None, time=None):
		self.uuid = uuid
		self.x = x
		self.y = y
		self.time = time
		
	def __repr__(self):
		return '<Location ' + self.uuid + ' at ' + str(self.time) + '>'
	