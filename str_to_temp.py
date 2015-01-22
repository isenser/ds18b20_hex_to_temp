#!/usr/bin/python
# -*- coding: utf-8 -*-

str_in=["fff8",#-0,5
        "ff5e",#-10.125
        "fe6f",#-25,0625
        "fc90"]#-55
def str_to_temp(str_in):
    hex_in=str_in.decode("hex")
    #print len(hex_in)
    if (ord(hex_in[0])&0xf0)==0xf0:
        #print "minus"
        temp_not=~((ord(hex_in[0]))<<8 | ord(hex_in[1]))+1
        temp_int=(temp_not>>4)&0x0ff
        temp_float=(temp_not&0x00F)*0.0625
        print "minus",str(temp_int+temp_float)
    else:
        #print "plus"
        temp_int=(ord(hex_in[0])<<4)|(ord(hex_in[1])>>4)
        print temp_int
        temp_float=(ord(hex_in[1])&0x0f)*0.0625
        print temp_float
        print "plus",str(temp_int+temp_float)
        
for ms in str_in:
    str_to_temp(ms)
