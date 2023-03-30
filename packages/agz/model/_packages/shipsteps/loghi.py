from gnr.core.gnrdecorator import metadata

class Table(object):
    def config_db(self,pkg):
        
        tbl=pkg.table('loghi', partition_agency_id='agency_id')
        tbl.column('agency_id',size='22',name_long='!![en]Agency').relation('agz.agency.id',relation_name='agency_sh_logo', mode='foreignkey', onDelete='raise')

    def defaultValues(self):
        return dict(agency_id=self.db.currentEnv.get('current_agency_id'))
