#!/usr/bin/env python  
#-*- coding: utf-8 -*-
import socket
import urllib.request
import urllib.error
import os
import shutil
import configparser
import platform


if __name__ == "__main__":
	val = os.system(
		'/bin/cat /home/tmp/GlobalSettings/Files/service.start >/etc/local.d/service.start')



