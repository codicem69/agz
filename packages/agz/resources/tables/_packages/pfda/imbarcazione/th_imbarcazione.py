#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        #r.fieldcell('tipo')
        r.fieldcell('tip_imbarcazione_code')
        r.fieldcell('nome',width='20em')
        r.fieldcell('flag', width='20em')
        r.fieldcell('loa')
        r.fieldcell('gt')
        r.fieldcell('nt')
        r.fieldcell('imo', name='IMO')

    def th_order(self):
        return 'nome'

    def th_query(self):
        return dict(column='nome', op='contains', val='')

class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer()
        self.datiImbarcazione(bc.roundedGroupFrame(title='Dati Imbarcazione',region='top',datapath='.record',height='185px', splitter=True))
        tc = bc.tabContainer(region = 'center',margin='2px')
        self.proformaImbarcazione(tc.contentPane(title='Proforma'))
        #pane = form.record
        #fb = pane.formbuilder(cols=2, border_spacing='4px')
        #fb.field('tip_imbarcazione_code' )
        #fb.field('nome' )
        #fb.field('flag',columns='$nome,$code',auxColumns='$nome', limit=20 )
        #fb.field('loa',validate_regex=" ^[0-9,]*$",validate_regex_error='Insert only numbers and comma', placeholder='eg: 10 or 10,50' )
        #fb.field('gt',validate_regex=" ^[0-9,]*$",validate_regex_error='Insert only numbers and comma', placeholder='eg:1200 or 1200,00' )
        #fb.field('nt' ,validate_regex=" ^[0-9,]*$",validate_regex_error='Insert only numbers and comma', placeholder='eg:650 or 650,00')

    def datiImbarcazione(self,pane):
        fb = pane.div(margin_left='50px',margin_right='80px').formbuilder(cols=1, border_spacing='4px',colswidth='auto',fld_width='100%')
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('tip_imbarcazione_code' )
        fb.field('nome' )
        fb.field('flag',columns='$nome,$code',auxColumns='$nome', limit=20 )
        fb.field('imo',validate_onAccept='FIRE #FORM.imo' )
        #fb.field('loa',validate_regex=" ^[0-9,]*$",validate_regex_error='Insert only numbers and comma', placeholder='eg: 10 or 10,50' )
        fb.field('loa', placeholder='eg: 10 or 10,50',validate_onAccept='FIRE #FORM.loa' )
        fb.field('gt',validate_regex=" ^[0-9,]*$",validate_regex_error='Insert only numbers and comma', placeholder='eg:1200 or 1200,00' )
        fb.field('nt' ,validate_regex=" ^[0-9,]*$",validate_regex_error='Insert only numbers and comma', placeholder='eg:650 or 650,00')
        fb.dataRpc('', self.ricercaImo, imo='=.imo',_fired='^#FORM.imo', _onResult="""if(result!=null) {alert(result);}""")
        fb.dataRpc('', self.loa, loa='=.loa',_fired='^#FORM.loa', _onResult="""if(result!=null) {SET .loa = result;}""")

    def proformaImbarcazione(self,pane):
        pane.dialogTableHandler(relation='@proforma_imb',
                                viewResource='ViewProforma')

    @public_method
    def loa(self,loa):
        if loa:
            if loa.find('.')>=0:
                loa=loa.replace('.',',')
                return loa

    @public_method
    def ricercaImo(self,imo):
        tbl_imbarcazioni = self.db.table('pfda.imbarcazione')
        imo_nave = tbl_imbarcazioni.readColumns(columns="""$imo AS imo_nave""", where='$imo=:imo', imo=imo)
        if imo_nave is not None:
            result = 'Already existing IMO. Please check before Save'
            return result

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
