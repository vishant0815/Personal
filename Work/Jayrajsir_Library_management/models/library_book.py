from odoo import models, fields
from server.odoo import api

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string="Title", required=True)
    author = fields.Char(string="Author")
    isbn = fields.Char(string="ISBN")
    publication_date = fields.Date(string="Publication Date")
    category_id = fields.Many2one('library.book.category', string="Category")  # Keep Many2one
    category_selection = fields.Selection(
        selection=lambda self: self._get_category_selection(),
        string="Category (Selection)",
        compute="_compute_category_selection",
        store=True
    )
    tags_ids = fields.Many2many('library.book.tags', string="Tags", related="category_id.tag_ids", readonly=True)
    state = fields.Selection([('available', 'Available'), ('borrowed', 'Borrowed')], string="Availability", default='available')
    description = fields.Text(string="Book Summary")
    library_id = fields.Many2one('library.library', string="Library")

    @staticmethod
    def _get_category_selection(self):
        """Fetch dynamic category list for the selection field."""
        categories = self.env['library.book.category'].search([])
        return [(str(cat.id), cat.name) for cat in categories]

    @api.depends('category_id')
    def _compute_category_selection(self):
        """Update selection field when Many2one changes."""
        for record in self:
            record.category_selection = str(record.category_id.id) if record.category_id else False
