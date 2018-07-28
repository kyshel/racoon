#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import argparse
from func import *

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('-t','--table',default='targets')
parser.add_argument('-s','--select',action='store_true')

group = parser.add_mutually_exclusive_group()
group.add_argument('-i','--insert',help='insert new entry ')
group.add_argument('-u','--update',)
group.add_argument('-d','--delete',help='delete entry by id')
group.add_argument('-r','--remove',help='remove entry by name')

args = parser.parse_args()
# print(args)

if args.table is 'targets':
	if args.insert is not None:
		resp_add_target(args.insert)
	if args.update is not None:
		pass
	if args.delete is not None:
		resp_rm_target_byid(args.delete)
	if args.remove is not None:
		resp_rm_target_byname(args.remove)
	if args.select is True:
		resp_get_targets()

	else:
		print('Please choose an operation! ')	


