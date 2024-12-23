# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('proprietario', pkey='id', name_long='!![it]Proprietario Carta', name_plural='!![it]Proprietari Carte',caption_field='full_descr', partition_agency_id='agency_id')

        tbl.column('agency_id',size='22',name_long='!![en]Agency',batch_assign=True).relation(
                                    'agz.agency.id',relation_name='agency_proprietario', mode='foreignkey', onDelete='raise')
