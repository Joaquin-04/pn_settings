from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class PurchaseRequisition(models.Model):
    _inherit = 'purchase.requisition'

    service_delivery_date = fields.Date(string="Fecha de Inicio de Servicio")
    service_completion_date = fields.Date(string="Fecha de Finalización de Servicio")
    show_service_dates = fields.Boolean(compute="_compute_show_service_dates", store=True)

    @api.depends('type_id')
    def _compute_show_service_dates(self):
        for record in self:
            _logger.warning(f"{record.type_id} & {record.type_id.id in [2, 4]}")
            record.show_service_dates = record.type_id.id not in [2, 4]

    @api.onchange('type_id')
    def _onchange_type_id(self):
        """Onchange para actualizar show_service_dates dinámicamente."""
        _logger.warning(f"{self.type_id} & {self.type_id.id in [2, 4]}")
        self.show_service_dates = self.type_id.id not in [2, 4]
        _logger.warning(f"{self.show_service_dates}")
