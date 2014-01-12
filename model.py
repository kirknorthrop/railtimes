# coding: utf-8
from sqlalchemy import Column, Float, Integer, String, Time, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Agency(Base):
	__tablename__ = u'agency'

	agency_id = Column(String(255), primary_key=True, index=True)
	agency_name = Column(String(255))
	agency_url = Column(String(255))
	agency_timezone = Column(String(255))
	agency_lang = Column(String(255))
	agency_phone = Column(String(255))


class Calendar(Base):
	__tablename__ = u'calendar'

	service_id = Column(Integer(), primary_key=True, index=True)
	monday = Column(Boolean())
	tuesday = Column(Boolean())
	wednesday = Column(Boolean())
	thursday = Column(Boolean())
	friday = Column(Boolean())
	saturday = Column(Boolean())
	sunday = Column(Boolean())
	start_date = Column(Integer())
	end_date = Column(Integer())


class Link(Base):
	__tablename__ = u'links'

	id = Column(Integer(), primary_key=True, index=True)
	mode = Column(String(255), primary_key=True, index=True)
	from_stop_id = Column(String(255))
	to_stop_id = Column(String(255))
	link_secs = Column(Integer())
	start_time = Column(Time())
	end_time = Column(Time())
	priority = Column(Integer())
	start_date = Column(Integer())
	end_date = Column(Integer())
	monday = Column(Integer())
	tuesday = Column(Integer())
	wednesday = Column(Integer())
	thursday = Column(Integer())
	friday = Column(Integer())
	saturday = Column(Integer())
	sunday = Column(Integer())


class Route(Base):
	__tablename__ = u'routes'

	route_id = Column(Integer(), primary_key=True, index=True)
	agency_id = Column(String, ForeignKey('agency.agency_id'))
	agency = relationship('Agency')
	route_short_name = Column(String(255))
	route_long_name = Column(String(255))
	route_type = Column(Integer())


class StopTime(Base):
	__tablename__ = u'stop_times'

	id = Column(Integer(), primary_key=True, index=True)
	trip_id = Column(Integer, ForeignKey('trips.trip_id'))
	trip = relationship('Trip')
	arrival_time = Column(Time())
	departure_time = Column(Time())
	stop_id = Column(String, ForeignKey('stops.stop_id'))
	stop = relationship('Stop')
	stop_sequence = Column(Integer())
	pickup_type = Column(Integer())
	drop_off_type = Column(Integer())
	scheduled_arrival = Column(Time())
	scheduled_departure = Column(Time())
	platform = Column(Integer())
	line = Column(String(255))
	path = Column(String(255))
	activity = Column(String(255))
	engineering_allowance = Column(String(255))
	pathing_allowance = Column(String(255))
	performance_allowance = Column(String(255))


class Stop(Base):
	__tablename__ = u'stops'

	stop_id = Column(String(255), primary_key=True, index=True)
	stop_code = Column(String(255))
	stop_name = Column(String(255))
	stop_lat = Column(Float(asdecimal=True))
	stop_lon = Column(Float(asdecimal=True))
	stop_url = Column(String(255))
	location_type = Column(Integer())
	parent_station = Column(String(255))
	wheelchair_boarding = Column(Integer())
	cate_type = Column(Integer())
	tiploc = Column(String(255))


class Transfer(Base):
	__tablename__ = u'transfers'

	id = Column(Integer(), primary_key=True, index=True)
	from_stop_id = Column(String(255))
	to_stop_id = Column(String(255))
	transfer_type = Column(Integer())
	min_transfer_time = Column(Integer())


class Trip(Base):
	__tablename__ = u'trips'

	route_id = Column(Integer, ForeignKey('routes.route_id'))
	route = relationship('Route')
	service_id = Column(Integer, ForeignKey('calendar.service_id'))
	service = relationship('Calendar')
	trip_id = Column(Integer(), primary_key=True, index=True)
