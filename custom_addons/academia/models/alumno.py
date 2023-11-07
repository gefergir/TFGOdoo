from odoo import api, models, fields
class Alumno(models.Model):
    _name = 'alumno'
    _description = 'Alumno de clase'

    name = fields.Char(string="nombre")
    description = fields.Char(string="descripcion")