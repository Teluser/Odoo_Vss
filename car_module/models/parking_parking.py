from odoo import fields, models, api

class ParkingParking(models.Model):
    _name = 'parking.parking'
    name = fields.Char("Name")
    car_ids = fields.One2many('car.car', 'parking_id')
