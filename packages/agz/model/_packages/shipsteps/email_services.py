class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('email_services', partition_agency_id='agency_id')
        tbl.column('agency_id',size='22', name_long='agency_id'
                    ).relation('agz.agency.id', relation_name='email_services_sh', mode='foreignkey', onDelete='raise')
