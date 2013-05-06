# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################

from subprocess import Popen, PIPE

# This command will be invoked 
sbCommand = 'shellinaboxd -t -s /:srikant:srikant:/:'

# rows will contain all the records of complaints by all users
rows = db(db.complaint).select() 

@auth.requires_login()
def index():
    """
    srikant: This index page is default for all clients/users, once a user
    apply for technician, he will be redirected to different page(techie)
    """
    # complaint is declared in db.py 
    form = SQLFORM(db.complaint)
    if form.process().accepted:
        response.flash = 'record inserted'
        
    # allows users to redirect to techie page if they belong to 'techie' group
    if auth.has_membership(role='techie'):
        redirect(URL('techie'))  
                                                                                                                              
    # Returns 'rows', 'form' and 'message' to views/default/index.html
    return dict(message=T('Hello %(first_name)s' % auth.user),
                form=form,
                rows=rows,
               )


@auth.requires_membership('techie')
def techie(): 
    return dict(message=T('Hello %(first_name)s' % auth.user),
                rows=rows,
               )


#def access():
    


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
