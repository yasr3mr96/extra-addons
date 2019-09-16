# -*- coding: utf-8 -*-
from odoo import http

# class CrmProject(http.Controller):
#     @http.route('/crm_project/crm_project/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crm_project/crm_project/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('crm_project.listing', {
#             'root': '/crm_project/crm_project',
#             'objects': http.request.env['crm_project.crm_project'].search([]),
#         })

#     @http.route('/crm_project/crm_project/objects/<model("crm_project.crm_project"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crm_project.object', {
#             'object': obj
#         })