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

	issue_regexp = r"\bissue(?::|\s+#?)(?P<id>\d+)\b"
	eventum_url = "https://eventum.dev.delfi.ee/view.php?id=%d"

	# IWikiSyntaxProvider methods
	def get_wiki_syntax(self):
		def issue(formatter, match, fullmatch):
			return tag.a(match, class_="ext-link", href = self.eventum_url % int(fullmatch.group('id')))
		yield (self.issue_regexp, issue)

	def get_link_resolvers(self):
		return []
