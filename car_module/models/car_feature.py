from odoo import fields, models, api

class CarFeature(models.Model):
    _name = 'car.feature'
    name = fields.Char("Name")
