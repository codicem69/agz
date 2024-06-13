#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method
from gnr.core.gnrnumber import decimalRound
from gnr.core.gnrbag import Bag
from gnr.web.gnrbaseclasses import TableTemplateToHtml
from datetime import datetime
from gnr.core.gnrlang import GnrException

class ViewProforma(BaseComponent):

    def th_options(self):
        return dict(partitioned=True)

class Form(BaseComponent):

    def th_bottom_custom(self, bottom):

            bar = bottom.slotBar('*,stampa_proforma,5,crea_email,*,10')
            bar.stampa_proforma.button('Stampa Proforma', iconClass='print',
                                        action="""genro.publish("table_script_run",{table:"pfda.proforma",
                                                                                   res_type:'print',
                                                                                   resource:'stampa_proforma',
                                                                                   pkey: pkey})""",
                                                                                   pkey='=#FORM.pkey')

            bar.crea_email.button('Crea email proforma', iconClass='print',
                                        action="""genro.publish("table_script_run",{table:"pfda.proforma",
                                                                                   res_type:'print',
                                                                                   resource:'email_proforma',
                                                                                   pkey: pkey})""",
                                                                                   pkey='=#FORM.pkey')

            email_account_id = self.db.application.getPreference('mail.account_id',pkg='pfda')
            email_template_id = self.db.application.getPreference('tpl.template_id',pkg='pfda')
            # qua verifichiamo di aver settato nelle preferenze del proforma l'account email e il template da utilizzare
            # nel caso  saremo avvisati da un msg alert
            if (email_account_id and email_template_id) == None:
                #raise GnrException('purtroppo manca questa cosa ')
                bar.data('.messaggio_speciale', "Verifica di aver inserito nelle preferenze globali \n l'account email e il template da utilizzare per l'invio dell'email")
                bar.dataController('alert(msg)', msg='=.messaggio_speciale', _if='msg', _onStart=True)
    
