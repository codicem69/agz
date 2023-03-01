# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('fatture_forn', partition_agency_id='agency_id')
        tbl.column('agency_id',size='22', name_long='!![en]agency', plugToForm=True
                    ).relation('agz.agency.id', relation_name='agency_fatforn', mode='foreignkey', onDelete='setNull')

    def defaultValues(self):
        return dict(agency_id=self.db.currentEnv.get('current_agency_id'))
