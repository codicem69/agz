#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):
    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('fornitore_id', name='!![en]Supplier', width='30em')
        r.fieldcell('data')
        r.fieldcell('doc_n')
        r.fieldcell('importo')
        r.fieldcell('descrizione', width='50em')

    def th_options(self):
        return dict(partitioned=True)
