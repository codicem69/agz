class Table(object):
    def config_db(self,pkg):

        tbl=pkg.table('arrival', partition_agency_id='agency_id')

        tbl.column('agency_id',size='22',name_long='!![en]Agency',batch_assign=True).relation(
                                    'agz.agency.id',relation_name='agency_email', mode='foreignkey', onDelete='raise')
