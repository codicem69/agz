# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('opening_gate', partition_agency_id='agency_id')
        tbl.column('agency_id',size='22',name_long='!![en]Agency').relation('agz.agency.id',relation_name='agency_sh_gate', mode='foreignkey', onDelete='raise')
        tbl.column('port',size='22',name_short='!![en]Port').relation('unlocode.place.id',relation_name='port_gate', mode='foreignkey', onDelete='raise')

    def defaultValues(self):
        return dict(agency_id=self.db.currentEnv.get('current_agency_id'),port=self.db.currentEnv.get('current_port'))

        
