# -*- coding: UTF-8 -*-

from gnr.web.gnrwebpage import BaseComponent
        
class LoginComponent(BaseComponent):
    
    def onAuthenticating_agz(self,avatar,rootenv=None):
        agency_id = self.db.table('agz.staff').readColumns(where='$user_id=:u_id',
                            u_id=avatar.user_id, columns='$agency_id')
        port = self.db.table('agz.agency').readColumns(where='$id=:ag_id',
                            ag_id=agency_id, columns='$port')

        rootenv['current_agency_id'] = agency_id 
        rootenv['current_port'] = port

