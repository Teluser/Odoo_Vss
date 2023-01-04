# -*- coding: utf-8 -*-
from odoo import http

# class CarModule(http.Controller):
#     @http.route('/car_module/car_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/car_module/car_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('car_module.listing', {
#             'root': '/car_module/car_module',
#             'objects': http.request.env['car_module.car_module'].search([]),
#         })

#     @http.route('/car_module/car_module/objects/<model("car_module.car_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('car_module.object', {
#             'object': obj
#         })