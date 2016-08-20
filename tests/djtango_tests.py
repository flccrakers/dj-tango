#!/usr/bin/python3
# -*- coding:Utf-8 -*-

from nose.tools import *
import djtango

def setup():
    print ("SETUP!")

def teardown():
    print ("TEAR DOWN!")

def test_basic():
    print ("I RAN!")