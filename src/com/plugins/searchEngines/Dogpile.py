"""
    This file is part of EmailHarvester
    Copyright (C) 2016 @maldevel
    https://github.com/maldevel/EmailHarvester
    
    EmailHarvester - A tool to retrieve Domain email addresses from Search Engines.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
    For more see the file 'LICENSE' for copying permission.
"""

from com.core.SearchEngine import SearchEngine


class Dogpile(SearchEngine):
    def __init__(self, site=None):
        url_dict = {}
        if site is None:
            url_dict = {
                "Dogpile": {"url": 'http://www.dogpile.com/search/web?qsi={counter}&q="%40{word}"',
                            "init": 1,
                            "step": 10}
            }
        super().__init__(url_dict)

