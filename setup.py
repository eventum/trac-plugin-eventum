# -*- coding: utf-8 -*-
from setuptools import setup

setup(
	name='TracEventumLink',
	version='0.2',
	author='Elan Ruusamäe',
	author_email='glen@pld-linux.org',
	description='Automatically create links for Eventum issue ID-s.',
	url='http://eventum.mysql.org/',
	license='BSD-like',
	packages=['trac.eventum'],
	entry_points = {'trac.plugins': ['trac.eventum = trac.eventum']}
)
