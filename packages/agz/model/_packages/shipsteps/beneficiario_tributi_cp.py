class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('beneficiario_tributi_cp',partition_agency_id='agency_id')
        tbl.column('agency_id',size='22',name_long='!![en]Agency').relation('agz.agency.id',relation_name='agency_sh_tributi', mode='foreignkey', onDelete='raise')
