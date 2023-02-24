# encoding: utf-8
class Menu(object):
    def config(self,root,**kwargs):
         agz = root.branch(u"agz", tags="")
         agz.thpage(u"!![en]Agencies", table="agz.agency", tags="")
         agz.thpage(u"!![en]Staff", table="agz.staff", tags="")
         glbl = root.packageBranch("Glbl", pkg='glbl', tags="")
