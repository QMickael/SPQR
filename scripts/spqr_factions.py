#!/usr/bin/python
# -*-coding:utf-8 -*

import sys,pygame
from pygame.locals import *

import spqr_data as SDATA
import spqr_defines as SPQR
import spqr_window as SWINDOW
import spqr_widgets as SWIDGET
import spqr_gui as SGFX
import spqr_events as SEVENT


class CFaction(object):
	def __init__(self, name, leader, logo, regions, \
						generals, capital, colour, playable):
		self.name = name
		self.leader = leader
		self.logo = logo
		self.regions = []
		self.armies = []
		self.capital = capital
		self.colour = colour
		self.playable = True
		self.at_war = []
		self.allies = []
