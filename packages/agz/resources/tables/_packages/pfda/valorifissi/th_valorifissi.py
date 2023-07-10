#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent


class LookupView(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('agency_id', edit=True, hasDownArrow=True)
        r.fieldcell('garbageval', edit=True)
        r.fieldcell('retaingarbval', edit=True)
        r.fieldcell('ispsval', edit=True)
        r.fieldcell('miscval', edit=True)
        r.fieldcell('bulkval', edit=True)
        r.fieldcell('notemiscval', edit=True)

    def th_order(self):
        return 'garbageval'

    def th_query(self):
        return dict(column='id', op='contains', val='')

