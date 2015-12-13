# -*- coding: utf-8 -*-
from openerp import models, fields

class SinhVien(models.Model):
    _name = 'sinhvien.model'
    _description = 'Sinh Vien'
    
    hoten = fields.Char(string='Ho ten', required=True)
    ngaysinh = fields.Date(string='Ngay Sinh')
    sdt = fields.Char(string='So DT')
    email = fields.Char(string='eMail')
    giotinh = fields.Boolean(string='Gioi Tinh')
    doanvien = fields.Boolean(string='La Doan Vien')
    
    lop_id = fields.Many2one('lop.model', string="Lop")