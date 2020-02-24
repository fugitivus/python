#!/usr/bin/python3
# coding: utf-8

import os

def cls():
	#for windows console use cls
	os.system('clear')
	return 0

shell_normal   	= '\33[0m'
fg_normal   	= '\33[0m'
bg_normal   	= '\33[0m'
shell_bold     	= '\33[1m'
shell_italic	= '\33[3m'
shell_blink		= '\33[5m'

fg_dblack  		= '\33[30m'
fg_dred    		= '\33[31m'
fg_dgreen  		= '\33[32m'
fg_dyellow 		= '\33[33m'
fg_dblue   		= '\33[34m'
fg_dviolet 		= '\33[35m'
fg_dorange		= '\33[36m'
fg_dwhite		= '\33[37m'

bg_dblack		= '\33[40m'
bg_dred			= '\33[41m'
bg_dgreen		= '\33[42m'
bg_dyellow		= '\33[43m'
bg_dblue		= '\33[44m'
bg_dviolet		= '\33[45m'
bg_dorange		= '\33[46m'
bg_dwhite		= '\33[47m'

fg_white		= '\33[90m'
fg_red			= '\33[91m'
fg_green		= '\33[92m'
fg_yellow		= '\33[93m'
fg_blue			= '\33[94m'
fg_violet		= '\33[95m'
fg_orange		= '\33[96m'
fg_white		= '\33[97m'

bg_white		= '\33[100m'
bg_red			= '\33[101m'
bg_green		= '\33[102m'
bg_yellow		= '\33[103m'
bg_blue			= '\33[104m'
bg_violet		= '\33[105m'
bg_orange		= '\33[106m'
bg_white		= '\33[107m'

version = '0.1'
