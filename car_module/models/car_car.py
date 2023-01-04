from odoo import fields, models, api

class CarCar(models.Model):
    _name = 'car.car'
    name = fields.Char("Name")
    horse_power = fields.Integer("Horse Power")
    door_number = fields.Integer("Door Numbers")
    driver_id = fields.Many2one('res.partner', string="Driver")
    parking_id = fields.Many2one('parking.parking', string="Parking")
    feature_ids = fields.Many2many('car.feature', string="Feature")
    total_speed = fields.Integer("Total speed", compute="_compute_total_speed")
    status = fields.Selection(string="Status", selection=[('new', 'New'), ('used', 'Used'), ('sold', 'Sold')],
                              default='new')
    car_sequence = fields.Char(string="Sequence")

    @api.depends('horse_power')
    def _compute_total_speed(self):
        for r in self:
            r.total_speed = r.horse_power * 5
        return
