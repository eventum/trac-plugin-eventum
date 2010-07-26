# -*- coding: utf-8 -*-
#
# Copyright (C) 2008 Elan Ruusamäe <glen@pld-linux.org>
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution. The terms
# are also available at http://trac.edgewall.com/license.html.
#
# Author: Elan Ruusamäe <glen@pld-linux.org>

from trac.core import implements, Component
from trac.wiki import IWikiSyntaxProvider
import trac

if [int(x) for x in trac.__version__.split('.')] >= [0, 11]:
	# trac 0.11
	from genshi.builder import tag
else:
	# trac 0.10
	from trac.util.html import html
	tag = html

class TracEventumLink(Component):
	implements(IWikiSyntaxProvider)

    issue_regexp = r"\b(?i:issue):?\s+?#?(?P<id>\d+)\b"

	# IWikiSyntaxProvider methods
	def get_wiki_syntax(self):
		eventum_url = self.env.config.get('eventum', 'url')

		def issue(formatter, match, fullmatch):
			return tag.a(tag.span(match, class_="icon"), class_="ext-link", href = eventum_url % int(fullmatch.group('id')))

		if eventum_url:
			yield (self.issue_regexp, issue)
		else:
			self.log.warn('url not set in configuration. Eventum links disabled')

	def get_link_resolvers(self):
		return []
