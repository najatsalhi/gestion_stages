from odoo import models, fields

class ConventionStage(models.Model):
    _name = 'gestion_stage.convention_stage'
    _description = 'Convention de Stage'

    demande_id = fields.Many2one(
        'gestion_stage.demande_stage', string='Demande Associée', required=True
    )
    entreprise = fields.Char(string='Entreprise', required=True)
    date_signature = fields.Date(string='Date de Signature')
    fichier_pdf = fields.Binary(string='Convention PDF')
