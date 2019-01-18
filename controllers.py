# -*- coding: utf-8 -*-
from openerp import http

# class Respartnerfields(http.Controller):
#     @http.route('/respartnerfields/respartnerfields/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/respartnerfields/respartnerfields/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('respartnerfields.listing', {
#             'root': '/respartnerfields/respartnerfields',
#             'objects': http.request.env['respartnerfields.respartnerfields'].search([]),
#         })

#     @http.route('/respartnerfields/respartnerfields/objects/<model("respartnerfields.respartnerfields"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('respartnerfields.object', {
#             'object': obj
#         })