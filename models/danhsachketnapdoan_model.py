# -*- coding: utf-8 -*-
from openerp import models, fields

class DanhSachKetNapDoan(models.Model):
    _name = 'danhsachketnapdoan.model'
    _description = 'Danh Sach Sinh Vien can Ket Nap Doan'
    
    hoten = fields.Char(string='Ho ten', required=True)
    ngaysinh = fields.Date(string='Ngay Sinh')
    sdt = fields.Char(string='So DT')
    email = fields.Char(string='eMail')
    giotinh = fields.Boolean(string='Gioi Tinh')
    doanvien = fields.Boolean(string='La Doan Vien')
    
    sinhvien_id = fields.Many2one('sinhvien.model', string="Sinh Vien ID")
    lop_id = fields.Many2one('lop.model', string="Lop ID")