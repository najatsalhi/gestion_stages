from odoo import models, fields, api

class DemandeStage(models.Model):
    _name = 'gestion_stage.demande_stage'
    _description = 'Demande de Stage'

    etudiant_id = fields.Many2one('gestion_stage.etudiant', string='Étudiant', required=True)
    entreprise_nom = fields.Char(string='Nom de l\'Entreprise', required=True)
    entreprise_adresse = fields.Char(string='Adresse de l\'Entreprise')
    responsable = fields.Char(string='Responsable')
    date_debut = fields.Date(string='Date de Début')
    date_fin = fields.Date(string='Date de Fin')
    statut = fields.Selection([('draft', 'Brouillon'), ('confirmed', 'Confirmé'), ('done', 'Terminé')], string='Statut', default='draft')

    historique_statut = fields.Text(string="Historique des Statuts", readonly=True)

    @api.onchange('statut')
    def _onchange_statut(self):
        if self.statut:
            self.historique_statut = f"{self.historique_statut}\nStatut changé en {dict(self._fields['statut'].selection).get(self.statut)}"

    def action_submit(self):
        self.write({'statut': 'en_attente'})