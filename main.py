#!/usr/bin/python

import pyaudio
import sys,random,time,argparse
import numpy as np
import aubio
import pygame
import Queue
from threading import Thread

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", required=False, type=int, help="Audio Input Device")
parser.add_argument("-f", "--fullscreen",action="store_true", help="Run in Full screen Mode")
args = parser.parse_args()

if not args.input:
	print("No input device specified. Printing list of input devvices now: ")
p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
	print("Device number (%i) : %s" %(i, p.get_device_info_by_index(i).get('name')))
print("Run this program with '-i 1' or '--input 1', or the number  of the input you'd like to use.")
exit()



















