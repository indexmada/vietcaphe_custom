# -*- coding: utf-8 -*-
from odoo import http

# class VietcapheCustom(http.Controller):
#     @http.route('/vietcaphe_custom/vietcaphe_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vietcaphe_custom/vietcaphe_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vietcaphe_custom.listing', {
#             'root': '/vietcaphe_custom/vietcaphe_custom',
#             'objects': http.request.env['vietcaphe_custom.vietcaphe_custom'].search([]),
#         })

#     @http.route('/vietcaphe_custom/vietcaphe_custom/objects/<model("vietcaphe_custom.vietcaphe_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vietcaphe_custom.object', {
#             'object': obj
#         })