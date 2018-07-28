#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import db

def resp_get_targets():
	for row in db.get_targets():
		print(row)
	return

def resp_add_target(target_to_add):
	added_id=db.add_target(target_to_add)
	if added_id == -1:
		print('Error! Maybe duplicated:')
		print(db.get_target_byname(target_to_add))
	else:
		print('OK!')
		print(db.get_target_byid(added_id))
	return

def resp_rm_target_byid(id):
	row=db.get_target_byid(id)
	rows=db.rm_target_byid(id)
	if rows == -1:
		print('Error! See log.txt for details.')
	else:
		print('OK! '+str(rows)+' row removed!')
		print(row)
	return


def resp_rm_target_byname(name):
	row=db.get_target_byname(name)
	rows=db.rm_target_byname(name)
	if rows == -1:
		print('Error! See log.txt for details.')
	else:
		print('OK! '+str(rows)+' row removed!')
		print(row)
	return


