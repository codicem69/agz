class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('cliente', partition_agency_id='agency_id')

        tbl.column('agency_id',size='22', name_long='!![en]agency', plugToForm=dict(hasDownArrow=True),batch_assign=True
                    ).relation('agz.agency.id', relation_name='agency_cliente', mode='foreignkey', onDelete='setNull')
