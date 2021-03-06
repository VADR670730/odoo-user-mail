# -*- coding: utf-8 -*-
##############################################################################
#
#
#
##############################################################################


{
    'name': 'User mail client',
    'version': '1.3',
    'category': 'other',
    'summary': 'Administation of mail for users on client side',
    'description': """
    Client side configuration of mail accounts
    
    use this in /etc/odoo/openerp-server.conf:
# mail_server
passwd_server = localhost
passwd_dbname = mail_server
passwd_user = admin
passwd_passwd = admin
# for smtp-configuration
smtp_host = localhost
smtp_port = 8069
smtp_encryption = yes
smtp_user = admin
smtp_pass = admin
# for imap-configuration
imap_host = localhost
imap_port = 8069

    self.sock_common = xmlrpclib.ServerProxy('%s/xmlrpc/common' % self.passwd_server)
  File "/usr/lib/python2.7/xmlrpclib.py", line 1573, in __init__
    raise IOError, "unsupported XML-RPC protocol"
IOError: unsupported XML-RPC protocol
    
    
    """,
    'author': 'Vertel AB',
    'license': 'AGPL-3',
    'website': 'http://www.vertel.se',
    'depends': ['user_password_tmp','fetchmail', 'user_mail_common'],
    'data': ['res_users_view.xml','res_users_data.xml','res_users_report.xml'],
    'installable': True,
    'application': True,
    #'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
