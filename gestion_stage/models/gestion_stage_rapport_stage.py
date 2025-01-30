from odoo import models, fields



class GestionStageRapportStage(models.Model):
    _name = 'gestion.stage.rapport.stage'
    _description = 'Rapport de Stage'
    
    # ...existing code...
    
    def generate_report(self):
        # Logic to generate the report
        report_data = {
            'title': self.name,
            'student': self.student_id.name,
            'company': self.company_id.name,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'content': self.content,
        }
        return report_data
    
    def print_report(self):
        report_data = self.generate_report()
        # Logic to print the report
        print(f"Title: {report_data['title']}")
        print(f"Student: {report_data['student']}")
        print(f"Company: {report_data['company']}")
        print(f"Start Date: {report_data['start_date']}")
        print(f"End Date: {report_data['end_date']}")
        print(f"Content: {report_data['content']}")
    
    def save_report(self, file_path):
        report_data = self.generate_report()
        # Logic to save the report to a file
        with open(file_path, 'w') as file:
            file.write(f"Title: {report_data['title']}\n")
            file.write(f"Student: {report_data['student']}\n")
            file.write(f"Company: {report_data['company']}\n")
            file.write(f"Start Date: {report_data['start_date']}\n")
            file.write(f"End Date: {report_data['end_date']}\n")
            file.write(f"Content: {report_data['content']}\n")
    
    def email_report(self, email_address):
        report_data = self.generate_report()
        # Logic to email the report
        email_body = (
            f"Title: {report_data['title']}\n"
            f"Student: {report_data['student']}\n"
            f"Company: {report_data['company']}\n"
            f"Start Date: {report_data['start_date']}\n"
            f"End Date: {report_data['end_date']}\n"
            f"Content: {report_data['content']}\n"
        )
        # Assuming a send_email function is available
        send_email(email_address, "Stage Report", email_body)
    
    # ...existing code...
