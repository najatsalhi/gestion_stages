from odoo import models, fields

class ConventionStage(models.Model):
    _name = 'gestion_stage.convention_stage'
    _description = "Convention de Stage"

    demande_stage_id = fields.Many2one('gestion_stage.demande_stage', string="Demande de Stage", required=True)
    fichier_convention = fields.Binary(string="Convention Signée")
    valide_encadrant = fields.Boolean(string="Validé par l'encadrant")
    valide_admin = fields.Boolean(string="Validé par l'administration")
