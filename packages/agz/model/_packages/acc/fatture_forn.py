# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('fatture_forn',partition_agency_id='agency_id')
        tbl.column('agency_id',size='22', name_long='!![en]agency',batch_assign=True
                    ).relation('agz.agency.id', relation_name='agency_fat_forn', mode='foreignkey', onDelete='setNull')
