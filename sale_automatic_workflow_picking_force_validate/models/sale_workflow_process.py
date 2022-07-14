# copyright 2022 Sodexis
# license OPL-1 (see license file for full copyright and licensing details).

from odoo import models, fields


class SaleWorkflowProcess(models.Model):
    _inherit = "sale.workflow.process"

    force_qty = fields.Boolean(
        string="Force Qtys",
    )
