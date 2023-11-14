# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
	_inherit = "product.template"

	seuil = fields.Float("Seuil")
	valeur = fields.Float(string="Valeur", compute="compute_valeur")

	def show_stock_minimum(self):
		resultat = self.search([('type', '=', 'product')]).filtered(lambda x: x.qty_available <= x.seuil)
		tree = self.env.ref('vietcaphe_custom.product_template_stock_minimum_tree')
		return {
			'type': 'ir.actions.act_window',
			'name': 'Alerte stock Minimum',
			'view_mode': 'tree',
			'res_model': 'product.template', 
			'view_id': tree.id,
			'domain': [('id', 'in', resultat.ids)],
			}

	def compute_valeur(self):
		for record in self:
			record.valeur = record.qty_available * record.standard_price