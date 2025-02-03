from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Etudiant(models.Model):
    _name = 'gestion_stage.etudiant'
    _description = "Étudiant"

    nom = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string="Prénom", required=True)    
    email = fields.Char(string='Email')
    phone  = fields.Integer(string='Téléphone')
    filiere = fields.Selection([
        ('mgsi', 'Génie management et gouvernance des systèmes d\'information'),
        ('informatique', 'Informatique'),
        ('electrique', 'Génie Électrique'),
        ('civil', 'Génie Civil'),
        ('industriel', 'Génie Industriel'),
    ], string="Filière", required=True)
    niveau = fields.Selection([
        ('1A', '1ère Année'),
        ('2A', '2ème Année'),
        ('3A', '3ème Année'),
    ], string="Niveau", required=True)
    
    @api.constrains('email')
    def _check_email(self):
        for record in self:
            if not record.email or '@' not in record.email:
                raise ValidationError("L'adresse email doit être valide.")
