class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('fileforemail',partition_agency_id='agency_id')
        self.sysFields(tbl)
        tbl.column('agency_id',size='22', name_long='!![en]agency'
                    ).relation('agz.agency.id', relation_name='agency_fileforemail', mode='foreignkey', onDelete='setNull')
        tbl.column('notestandard', name_short='!![en]Default notes')

    def defaultValues(self):
        return dict(agency_id=self.db.currentEnv.get('current_agency_id'))
