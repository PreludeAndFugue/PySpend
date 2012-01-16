#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# standard lib imports
from __future__ import division
import json
import os
import os.path
# third party imports
import wx
# pyspend imports
import db
import gui

CONFIG = 'config.json'
OPEN = 0
SAVE = 1

def run():
    spend = PySpend(redirect=False)
    spend.MainLoop()

class PySpend(wx.App):
    def OnInit(self):
        self.config = self._read_config()
        
        self.frame = PySpendController(config=self.config, parent=None)
        self.frame.Show()
        self.SetTopWindow(self.frame)

        return True
        
    def OnExit(self):
        self._write_config()
        
    def _read_config(self):
        '''Read the config file.'''
        config = json.load(open(self._config_path(), 'r'))
        return config
        
    def _write_config(self):
        '''Write changes to the config file on exit.'''
        with open(self._config_path(), 'w') as f:
            json.dump(self.config, f, indent=4)
            
    def _config_path(self):
        path = os.path.dirname(__file__)
        return os.path.join(path, CONFIG)

class PySpendController(gui.PySpendGUI):
    def __init__(self, config, *args, **kwargs):
        super(PySpendController, self).__init__(*args, **kwargs)
        
        # check database
        self.config = config
        self.db_path = config['DB']
        self.check_db()
        self.db = db.connect(self.db_path)
        
        self._bind_events()

        # initialise some widgets
        self.config_cat_list()
        self.refresh_cat_list()
        self.refresh_category()
        self.config_item_list()
        self.refresh_item_list()

    def _bind_events(self):
        self.date_picker.Bind(wx.EVT_DATE_CHANGED, self.pick_date)
        self.date_spin.Bind(wx.EVT_SPIN_UP, self.date_next)
        self.date_spin.Bind(wx.EVT_SPIN_DOWN, self.date_prev)
        self.add_item.Bind(wx.EVT_BUTTON, self.new_item)
        self.add_cat.Bind(wx.EVT_BUTTON, self.new_cat)
        self.cost.Bind(wx.EVT_KILL_FOCUS, self.validate_cost)
        self.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.delete_popup)
        self.menu_delete.Bind(wx.EVT_MENU, self.delete_item)

    ############################################################################
    # open and save database files
    
    def check_db(self):
        '''Check that the db path is an sqlite file.'''
        if not os.path.exists(self.db_path):
            msg = 'No database file. Please open an existing file, or create a new one.'
            caption = 'No Database'
            choices = ['Open', 'Create']
            dlg = wx.SingleChoiceDialog(self, msg, caption, choices)
            if dlg.ShowModal() == wx.ID_OK:
                action = dlg.GetStringSelection()
                if action == 'Open':
                    self.db_path = self.open_db()
                else:
                    self.db_path = self.save_db()
                self.config['DB'] = self.db_path
    
    def open_db(self):
        '''Open a database file.'''
        return self._file_dialog(OPEN)
        
    def save_db(self):
        '''Save a database file to a new location or create a new file when
        the file doesn't exist.'''
        return self._file_dialog(SAVE)
        
    def _file_dialog(self, type_):
        if type_ == OPEN:
            style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
            msg = "Open a database"
        else:
            style = wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT
            msg = "Save or create a database"
        wildcard = "Database Files (*.sqlite)|*.sqlite"
        dlg = wx.FileDialog(self, message=msg, wildcard=wildcard, style=style)
        if dlg.ShowModal() == wx.ID_OK:
            print 'ok'
            return dlg.GetPath()
        else:
            print 'cancel'
        dlg.Destroy()
        

    ############################################################################
    # event handlers

    def pick_date(self, event):
        self.refresh_item_list()

    def date_next(self, event):
        self.day_inc(1)

    def date_prev(self, event):
        self.day_inc(-1)

    def day_inc(self, inc):
        day = self.date_picker.GetValue()
        new_day = day + wx.DateSpan(0, 0, 0, inc)
        self.date_picker.SetValue(new_day)
        self.refresh_item_list()

    def new_item(self, event):
        cat = self.category.GetValue()
        item = self.name.GetValue().strip()
        if not item or not cat:
            return
        amount = int(self.cost.GetValue())
        if amount == 0:
            return

        cat_id = self.db.get_catid(cat)
        date = self.date_picker.GetValue().FormatISODate()
        #print(cat_id, cat, item, amount, date)

        self.db.new_item(cat_id, item, amount, date)

        self.refresh_item_list()

        # set the focus back to the item text box
        self.name.SetFocus()
        self.name.SetSelection(-1, -1)
        
    def delete_popup(self, event):
        '''Show the delete pop-up menu on right click on a list control.'''
        self.delete_list = event.GetEventObject()
        selected_item = self.delete_list.GetFirstSelected()
        item_id = self.delete_list.GetItem(selected_item, 0).GetText()
        self.delete_item_id = int(item_id)
        self.PopupMenu(self.menu_delete)
        
    def delete_item(self, event):
        if self.delete_list is self.cat_list:
            # try to delete category
            if not self.db.category_used(self.delete_item_id):
                self.db.delete_category(self.delete_item_id)
                self.refresh_cat_list()
                self.refresh_category()
        else:
            # delete outgoings item
            self.db.delete_item(self.delete_item_id)
            self.refresh_item_list()

    def validate_cost(self, event):
        '''Cost should be an integer.'''
        try:
            int(self.cost.GetValue())
        except ValueError:
            self.cost.SetBackgroundColour('pink')
            self.cost.SetValue('')
            self.cost.SetFocus()
            self.cost.Refresh()
        else:
            bg_colour = wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW)
            self.cost.SetBackgroundColour(bg_colour)
            self.cost.Refresh()

    def new_cat(self, event):
        category = self.cat_text.GetValue().strip()
        if not category:
            # blank cat name
            return
        if self.db.category_exists(category):
            print('category already exists')
        else:
            self.db.new_category(category)
            self.refresh_cat_list()
            self.refresh_category()

    ############################################################################
    # category tab

    def config_cat_list(self):
        '''Initial configuration'''
        self.cat_list.InsertColumn(0, 'cat_id', width=0)
        self.cat_list.InsertColumn(1, 'Category', width=450)

    def refresh_cat_list(self):
        '''Refresh the cat list whenever change is made to categories.'''
        self.cat_list.DeleteAllItems()
        for row in self.db.categories():
            self.cat_list.Append(row)

    ############################################################################
    # item tab

    def config_item_list(self):
        '''Initial configuration of item list.'''
        l = wx.LIST_FORMAT_LEFT
        r = wx.LIST_FORMAT_RIGHT
        columns = [('itemid', 0, l), ('Category', 130, l), ('Item', 340, l),
                   (u'Cost (£)', 70, r)]
        for i, (col, width, format) in enumerate(columns):
            self.item_list.InsertColumn(i, col, format=format, width=width)

    def refresh_item_list(self):
        date_iso = self.date_picker.GetValue().FormatISODate()
        self.item_list.DeleteAllItems()
        total_cost = 0
        fmt = u'£{:0.2f}'.format
        for row in self.db.day_items(date_iso):
            row = list(row)
            cost = row[-1]
            total_cost += cost
            cost /= 100
            row[-1] = fmt(cost)
            self.item_list.Append(row)
        # update total in footer
        self.total_cost.SetLabel(fmt(total_cost/100))

    def refresh_category(self):
        '''The category combo box needs refreshing.'''
        cats = [c for _, c in self.db.categories()]
        self.category.Clear()
        self.category.AppendItems(cats)