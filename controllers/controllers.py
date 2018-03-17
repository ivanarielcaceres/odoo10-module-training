# -*- coding: utf-8 -*-
from odoo import http

# class TestIvan(http.Controller):
#     @http.route('/test_ivan/test_ivan/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_ivan/test_ivan/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_ivan.listing', {
#             'root': '/test_ivan/test_ivan',
#             'objects': http.request.env['test_ivan.test_ivan'].search([]),
#         })

#     @http.route('/test_ivan/test_ivan/objects/<model("test_ivan.test_ivan"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_ivan.object', {
#             'object': obj
#         })