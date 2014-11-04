#!/usr/local/bin/python2.7
# encoding: utf-8
'''
fileutil -- shortdesc

fileutil is a description

It defines classes_and_methods

@author:     user_name

@copyright:  2014 organization_name. All rights reserved.

@license:    license

@contact:    user_email
@deffield    updated: Updated
'''
import os
import commands

def get_cfg_content(file_path):
    content = None
    file_object = open(file_path, 'r')
    try:
        content = file_object.read()
    finally:
        file_object.close()
    return content

def is_cfg_key_exist(file_path, key):
    exist = False
    file_object = open(file_path, 'r')
    try:
        lines = file_object.readlines()
        for line in lines:
            kv = line.split('=')
            if kv[0] == key:
                exist = True
                break
    finally:
        file_object.close()
    return exist

def get_cfg_key_value(file_path, key):
    value = None
    file_object = open(file_path, 'r')
    try:
        lines = file_object.readlines()
        for line in lines:
            print line
            kv = line.split('=')
            if kv[0] == key:
                value = kv[1]
                break
    finally:
        file_object.close()
    return value.strip('\n')

def update_cfg_key_value(file_path, key, value):
    is_update = False
    file_object = open(file_path, 'r+')
    try:
        lines = file_object.readlines()
        print lines
        for i in range(len(lines)):
            kv = lines[i].split('=')
            if kv[0] == key:
                lines[i] = kv[0] + '=' + value + '\n'
                is_update = True
                break
        file_object.seek(0)
        for line in lines:
            if line == '\n':
                continue
            file_object.write(line)
    finally:
        file_object.close()
    return is_update

def add_cfg_key_value(file_path, key, value):
    is_add = False
    file_object = open(file_path, 'a')
    try:
        file_object.write(key + '=' + value)
        file_object.write('\n')
        is_add = True
    finally:
        file_object.close()
    return is_add

def delete_cfg_key_value(file_path, key):
    is_delete = False

  

if __name__=="__main__":
    add_cfg_key_value('cfg', 't1', '1')
    add_cfg_key_value('cfg', 't2', '2')
    add_cfg_key_value('cfg', 't3', '3')
    add_cfg_key_value('cfg', 't4', '4')
    
#       print get_cfg_key_value('cfg', 't1') == 'b'
#       print is_cfg_key_exist('cfg', 't1')
#       print is_cfg_key_exist('cfg', 't')
#     update_cfg_key_value('cfg', 't1', 'b')
#     update_cfg_key_value('cfg', 't2', 'c')
#     update_cfg_key_value('cfg', 't3', 'd')
#     update_cfg_key_value('cfg', 't4', 'e')

