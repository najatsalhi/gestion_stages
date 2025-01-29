from odoo import models, fields 
class Etudiant(models.Model):
    _name = 'gestion_stage.etudiant'
    _description = 'Étudiant'

    name = fields.Char(string='Nom et Prénom', required=True)
    email = fields.Char(string='Email', required=True)
    filiere = fields.Char(string='Filière', required=True)
    annee = fields.Selection(
        [('1', '1ère Année'), ('2', '2ème Année'), ('3', '3ème Année')],
        string='Année Académique',
        required=True
    )
    demande_ids = fields.One2many(
        'gestion_stage.demande_stage', 'etudiant_id', string='Demandes de Stage'
    )
