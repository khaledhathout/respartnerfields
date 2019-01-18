# -*- coding: utf-8 -*-

from openerp import models, fields, api


# class respartnerfields(models.Model):
#     _name = 'respartnerfields.respartnerfields'

#     name = fields.Char()
# explain what you need

class respartnerfields(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    Tax_available = fields.Char(string="Tax - if available", required=False)


