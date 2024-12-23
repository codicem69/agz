# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('carta', pkey='id', name_long='!![it]Carta', name_plural='!![it]Carte',caption_field='descr_carta', partition_agency_id='agency_id')

        tbl.column('agency_id',size='22',name_long='!![en]Agency',batch_assign=True).relation(
                                    'agz.agency.id',relation_name='agency_carta', mode='foreignkey', onDelete='raise')
