#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# Xibo - Digitial Signage - http://www.xibo.org.uk
# Copyright (C) 2009 Alex Harrington
#
# This file is part of Xibo.
#
# Xibo is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version. 
#
# Xibo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Xibo.  If not, see <http://www.gnu.org/licenses/>.
#

from XiboMedia import XiboMedia
from threading import Thread
import urllib

class WebpageMedia(XiboMedia):
    def add(self):
        tmpXML = '<browser id="' + self.mediaNodeName + '" opacity="0" width="' + str(self.width) + '" height="' + str(self.height) + '"/>'
        self.p.enqueue('add',(tmpXML,self.regionNodeName))

    def run(self):
        self.p.enqueue('browserNavigate',(self.mediaNodeName,urllib.unquote(str(self.options['uri'])),self.finishedRendering))
        self.p.enqueue('timer',(int(self.duration) * 1000,self.parent.next))

    def requiredFiles(self):
        return []
	
    def dispose(self):
        self.p.enqueue('del',self.mediaNodeName)
        self.parent.tNext()
    
    def finishedRendering(self):
        self.p.enqueue('browserOptions',(self.mediaNodeName,False,False))
        self.p.enqueue('setOpacity',(self.mediaNodeName,1))
