from odoo import models, fields

class Employee(models.Model):
    _inherit = 'hr.employee'
    pincode = fields.Char("Pincode")
    password = fields.Char("Password")