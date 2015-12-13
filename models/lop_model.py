# -*- coding: utf-8 -*-
from openerp import models, fields, api, osv, _

class Lop(models.Model):
    _name = 'lop.model'
    _description = 'Lop'
    
    name = fields.Char(string='Ten Lop', required=True)
    danhsach_ids = fields.One2many('danhsachketnapdoan.model', 'lop_id', string='Danh Sach Sinh Vien can Ket Nap Doan')
    
    @api.one
    def lay_dachsach(self):
        sql='''
            SELECT DISTINCT id, hoten, ngaysinh, sdt, email, giotinh
            FROM sinhvien_model
            WHERE lop_id = '%s'
                AND doanvien = %s
        '''%(self.id, False)
        self.env.cr.execute(sql)
#       Lấy dự liệu trả về kiểu: Dictionary
        res = {}
        for line in self.env.cr.dictfetchall(): 
            res={'sinhvien_id': line['id'] or '',
                 'hoten': line['hoten'] or '',
                 'ngaysinh': line['ngaysinh'] or '',
                 'sdt': line['sdt'] or '',
                 'email': line['email'] or '',
                 'giotinh': line['giotinh'] or '',
                 'sdt': line['sdt'] or '',
                 'lop_id': self.id or ''}
#             Tạo danh sách
            danhsach_obj = self.env['danhsachketnapdoan.model']
            danhsach_obj.create(res)
    @api.one
    def ketnap(self):
        sql='''
            UPDATE sinhvien_model 
            SET doanvien = TRUE 
            WHERE id in (SELECT sinhvien_id FROM danhsachketnapdoan_model WHERE lop_id = %s)
        '''%(self.id)
        self.env.cr.execute(sql)
        