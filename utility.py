# coding=utf-8
# 

import os, configparser
import logging
logger = logging.getLogger(__name__)



def getCurrentDirectory():
	"""
	Get the absolute path to the directory where this module is in.

	This piece of code comes from:

	http://stackoverflow.com/questions/3430372/how-to-get-full-path-of-current-files-directory-in-python
	"""
	return os.path.dirname(os.path.abspath(__file__))



def _load_config(file='rtt.config'):
	"""
	Read the config file, convert it to a config object. The config file is 
	supposed to be located in the same directory as the py files, and the
	default name is "config".

	Caution: uncaught exceptions will happen if the config files are missing
	or named incorrectly.
	"""
	cfg = configparser.ConfigParser()
	cfg.read(os.path.join(getCurrentDirectory(), file))
	return cfg



# initialized only once when this module is first imported by others
if not 'config' in globals():
	config = _load_config()
