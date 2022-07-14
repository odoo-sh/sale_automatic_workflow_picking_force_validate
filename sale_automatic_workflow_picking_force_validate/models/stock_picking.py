# copyright 2022 Sodexis
# license OPL-1 (see license file for full copyright and licensing details).

from odoo import models
from odoo.exceptions import UserError
# from odoo.tools import float_compare


class StockPicking(models.Model):
    _inherit = "stock.picking"

    def validate_picking(self):
        """Force Quantities and validate the pickings."""
        force_qty_pickings = self.filtered(lambda p: p.state not in ['done', 'cancel'] and p.workflow_process_id.force_qty)
        remaining = self - force_qty_pickings
        for picking in force_qty_pickings:
            picking.action_assign()
            if picking.move_line_ids:
                remaining |= picking
                continue
            move_lines_to_create = []
            for move in picking.move_lines.filtered(lambda m: not m.move_line_ids):
                line_vals = move._prepare_move_line_vals()
                line_vals.update({
                    'qty_done': move.product_id.uom_id._compute_quantity(move.product_uom_qty, move.product_uom, rounding_method='HALF-UP')
                })
                move_lines_to_create.append(line_vals)
            self.env['stock.move.line'].create(move_lines_to_create)
            picking.with_context(skip_overprocessed_check=True).button_validate()
        return super(StockPicking, remaining).validate_picking()
