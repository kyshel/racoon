#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from time import localtime, strftime
from sqlalchemy.sql import select
import logging

logging.basicConfig(
	level=logging.DEBUG,
	format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
	datefmt='%m-%d %H:%M:%S',
	handlers=[
	logging.FileHandler("{0}/{1}.log".format('.', 'db')),
	#logging.StreamHandler()
    ]
	)


logging.info('> db.py start < ')

engine = create_engine('mysql://root:123@localhost/racoon')

metadata = MetaData()
targets=Table('targets',metadata,
	Column('id',Integer,primary_key=True),
	Column('time',String(20)),
	Column('target',String(128),unique=True), # too short, comprise
	)

metadata.create_all(engine, checkfirst=True)

conn = engine.connect()
cur_time = strftime("%Y-%m-%d %H:%M:%S", localtime())

def logger(info):
	logging.info(info)

def get_target_byid(id):
	result = conn.execute(
		select([targets]).where(targets.c.id == id)
		)
	return result.fetchone()

def get_target_byname(name):
	result = conn.execute(
		select([targets]).where(targets.c.target == name)
		)
	return result.fetchone()

def get_targets():
	try:
		result = conn.execute(select([targets]))
	except Exception as e:
		logging.debug(e)
		return -1
	else:
		return result

def add_target(target_new):
	try:
		r_i_target=conn.execute(targets.insert(),
			time=cur_time, 
			target=target_new,
			)
	except Exception as e:
		logging.debug(e)
		return -1
	else:
		pk=r_i_target.inserted_primary_key
		return pk[0]

def rm_target_byid(id):
	try:
		r_d_target=conn.execute(
			targets.delete().where(targets.c.id == id)
			)
	except Exception as e:
		logging.debug(e)
		return -1
	else:
		return r_d_target.rowcount

def rm_target_byname(name):
	try:
		r_d_target=conn.execute(
			targets.delete().where(targets.c.target == name)
			)
	except Exception as e:
		logging.debug(e)
		return -1
	else:
		return r_d_target.rowcount

logging.info('> db.py end < ')




