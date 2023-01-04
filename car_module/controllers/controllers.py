from odoo import http
from odoo.http import request

class CarModule(http.Controller):
    @http.route('/car_module/cars/', auth='public')
    def get_three_cars_with_biggest_horse_power(self, **kw):
        car_ids = request.env['car.car'].search([])
        car_horse_power = car_ids.mapped('horse_power')
        car_horse_power.sort()
        max_horse_power = car_horse_power[-3:]
        car_max_horse_power_ids = request.env['car.car'].search([('horse_power', 'in', max_horse_power)])
        return request.render("car_module.car_web_template", {'car_ids': car_max_horse_power_ids})

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