#!/bin/python

import os

def abspath(path):
    return ios.path.abspath(path)

def exists(path):
    return os.path.exists(path)

def isfile(path):
    return os.path.isfile(path)

def isdir(path):
    return ios.path.isdir(path)

def listdir(path):
    return os.listdir(path)

def mkdir(path):
    return os.mkdir(path)

def mkdirs(path):
    return os.makedirs(path)

def remove(path):
    return os.remove(path)

def rmdir(path):
    return os.rmdir(path)

def removedirs(path):
    return os.removedirs(path)

def rename(src, dst):
    return os.rename(src, dst)
