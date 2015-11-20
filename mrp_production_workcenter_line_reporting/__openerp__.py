# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2010-2015 Elico Corp (<http://www.elico-corp.com>)
#    Authors: Siyuan Gu
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{'name': 'Mrp productoin workcenter line reporting',
 'version': '0.1',
 'category': '',
 'depends': ['mrp_operations'],
 'author': 'Elico Corp',
 'license': 'AGPL-3',
 'website': 'https://www.elico-corp.com',
 'description': """
Mrp productoin workcenter line reporting
============================================================================
This model allows to record the finished and scraped quantity
for per work order.

Usage
-----
A new button is added in the page "work order" under "Manufacturing Orders".

This button is linked to a wizard which allows user
adds the finished and scrapted quanities and date.

A new page "Finished and Scraped reporting" is added in the "Work Orders".

Contributors
------------

* Siyuan Gu: gu.siyuan@elico-corp.com
""",
 'images': [],
 'demo': [],
 'data': ['security/ir.model.access.csv',
          'wizard/wizard_mrp_workcenter_line_reporting.xml',
          'views/mrp_production_workcenter_line.xml',
          'views/mrp_operations_view.xml',
          'views/mrp_scrapted_reason.xml'],
 'test': [],
 'installable': True,
 'application': False}
