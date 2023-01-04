from odoo import models

class PartnerXlsx(models.AbstractModel):
    _name = 'report.car_module.report_car_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, cars_wizard):
        report_name = "Horse power <= " + str(cars_wizard.max_horse_power)
        sheet = workbook.add_worksheet(report_name)
        bold = workbook.add_format({'bold': True})
        headers = ['Name', 'Status', 'Horse Power', 'Door Numbers', 'Driver', 'Parking', 'Feature', 'Total speed']
        row = 0
        col = 0
        for text in headers:
            sheet.write(row, col, text, bold)
            col += 1
        row += 1
        for car in cars_wizard.car_ids:
            fields = [car.name, car.status, car.horse_power, car.door_number, car.driver_id.name, car.parking_id.name,
                      ', '.join(car.feature_ids.mapped('name')), car.total_speed]
            for col in range(len(headers)):
                sheet.write(row, col, fields[col] or '')
            row += 1
        return
