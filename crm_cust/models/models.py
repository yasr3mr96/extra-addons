# -*- coding: utf-8 -*-

from odoo import models, fields, api

class crm_cust(models.Model):
    _inherit = 'crm.lead'

    order_type = fields.Many2one(comodel_name="crm_cust.order_type", string="Order Type", required=True)
    sale_status = fields.Many2one(comodel_name="crm_cust.sale_status", string="Sale Status", required=True)



class OrderType(models.Model):
    _name="crm_cust.order_type"
    name = fields.Char(string="Name", required=True)

class SaleStatus(models.Model):
    _name="crm_cust.sale_status"
    name = fields.Char(string="Name", required=True)