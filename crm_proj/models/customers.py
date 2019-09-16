# -*- coding: utf-8 -*-


from odoo import api, fields, models


class Customers(models.Model):
    _inherit='res.partner'

    trn = fields.Char(string="Tax Registration Number")
    customer_group = fields.Many2one(comodel_name="res.partner", string="Customer Group", required=True)
    customer_source = fields.Many2one(comodel_name="res.partner", string="Customer Source", required=True)
    customer_id = fields.Integer(string="Customer ID", readonly=True,related='id')
    business_name = fields.Char(string="Business Name",required=True)

