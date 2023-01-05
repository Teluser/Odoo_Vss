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
    car_sequence = fields.Char(string="Sequence", readonly=True, required=True, copy=False, default='New')
    image = fields.Binary(string="Car Image")
    car_price = fields.Float(string="Price")
    parking_price = fields.Float(related="parking_id.parking_price")
    total_price = fields.Float("Total Price", compute="_compute_total_price", store=True)

    @api.depends('car_price', 'parking_price')
    def _compute_total_price(self):
        for r in self:
            r.total_price = r.car_price + r.parking_price
        return

    @api.model
    def create(self, vals):
        if vals.get('car_sequence', 'New') == 'New':
            vals['car_sequence'] = self.env['ir.sequence'].next_by_code('car.car.sequence') or 'New'
        return super(CarCar, self).create(vals)

    @api.depends('horse_power')
    def _compute_total_speed(self):
        for r in self:
            r.total_speed = r.horse_power * 5
        return
