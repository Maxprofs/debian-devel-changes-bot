# -*- coding: utf-8 -*-
#
#   Debian Changes Bot
#   Copyright (C) 2008 Chris Lamb <chris@chris-lamb.co.uk>
#   Copyright (C) 2015 Sebastian Ramacher <sramacher@debian.org>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

from .accepted_upload import AcceptedUploadParser
from .bug_closed import BugClosedParser
from .bug_submitted import BugSubmittedParser
from .security_announce import SecurityAnnounceParser


def get_message(email, **kwargs):
    order = (
        AcceptedUploadParser,
        BugClosedParser,
        BugSubmittedParser,
        SecurityAnnounceParser,
    )
    headers, body = email

    for parser in order:
        msg = parser.parse(headers, body, **kwargs)
        if msg:
            return msg
