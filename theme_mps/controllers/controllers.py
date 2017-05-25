# -*- coding: utf-8 -*-
from odoo import http

# class Mps(http.Controller):
#     @http.route('/mps/mps/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mps/mps/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mps.listing', {
#             'root': '/mps/mps',
#             'objects': http.request.env['mps.mps'].search([]),
#         })

#     @http.route('/mps/mps/objects/<model("mps.mps"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mps.object', {
#             'object': obj
#         })