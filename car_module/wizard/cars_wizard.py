from odoo import models, fields

class CarsWizard(models.TransientModel):
    _name = 'cars.wizard'

    max_horse_power = fields.Integer()
    car_ids = fields.Many2many('car.car')

    def get_car_report(self):
        self.car_ids = self.env['car.car'].search([('horse_power', '<=', self.max_horse_power)])
        action = self.env.ref('car_module.report_car_xlsx').read()[0]
        return action
