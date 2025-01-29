from odoo import models, fields 
class DemandeStage(models.Model):
    _name = 'gestion_stage.demande_stage'
    _description = 'Demande de Stage'

    etudiant_id = fields.Many2one(
        'gestion_stage.etudiant', string='Étudiant', required=True
    )
    date_demande = fields.Date(string='Date de la Demande', default=fields.Date.today)
    statut = fields.Selection(
        [('en_attente', 'En attente'), ('validee', 'Validée'), ('rejetee', 'Rejetée')],
        string='Statut',
        default='en_attente'
    )
    remarques = fields.Text(string='Remarques')
