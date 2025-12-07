from pyramid.response import Response
from pyramid.view import view_config
import json

from sqlalchemy.exc import DBAPIError
from sqlalchemy import asc

from .. import models


@view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
def my_view(request):
    try:
        query = request.dbsession.query(models.MyModel)
        one = query.filter(models.MyModel.name == 'one').first()
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'one': one, 'project': 'pertemuan6'}


# API ENDPOINTS
@view_config(route_name='api_models', renderer='json', request_method='GET')
def api_get_models(request):
    """GET - Dapatkan semua matakuliah"""
    try:
        models_list = request.dbsession.query(models.MyModel).all()
        data = [{'id': m.id, 'name': m.name, 'value': m.value} for m in models_list]
        return {'success': True, 'message': f'Data ditemukan: {len(data)}', 'data': data}
    except Exception as e:
        return {'success': False, 'message': str(e), 'data': None}


@view_config(route_name='api_models', renderer='json', request_method='POST')
def api_create_model(request):
    """POST - Tambah matakuliah baru"""
    try:
        data = request.json_body
        if 'name' not in data or 'value' not in data:
            return {'success': False, 'message': 'Field name dan value wajib diisi'}, 400
        
        new_model = models.MyModel(name=data['name'], value=data['value'])
        request.dbsession.add(new_model)
        request.dbsession.flush()
        
        return {'success': True, 'message': 'Data berhasil ditambahkan', 
                'data': {'id': new_model.id, 'name': new_model.name, 'value': new_model.value}}, 201
    except Exception as e:
        request.dbsession.rollback()
        return {'success': False, 'message': str(e)}, 400


@view_config(route_name='api_model_detail', renderer='json', request_method='GET')
def api_get_model(request):
    """GET - Dapatkan detail matakuliah"""
    try:
        model_id = request.matchdict['id']
        model = request.dbsession.query(models.MyModel).filter(models.MyModel.id == model_id).first()
        
        if not model:
            return {'success': False, 'message': f'Data ID {model_id} tidak ditemukan'}, 404
        
        return {'success': True, 'message': 'Data ditemukan', 
                'data': {'id': model.id, 'name': model.name, 'value': model.value}}
    except Exception as e:
        return {'success': False, 'message': str(e)}, 400


@view_config(route_name='api_model_detail', renderer='json', request_method='PUT')
def api_update_model(request):
    """PUT - Update matakuliah"""
    try:
        model_id = request.matchdict['id']
        data = request.json_body
        model = request.dbsession.query(models.MyModel).filter(models.MyModel.id == model_id).first()
        
        if not model:
            return {'success': False, 'message': f'Data ID {model_id} tidak ditemukan'}, 404
        
        if 'name' in data:
            model.name = data['name']
        if 'value' in data:
            model.value = data['value']
        
        request.dbsession.flush()
        return {'success': True, 'message': 'Data berhasil diupdate', 
                'data': {'id': model.id, 'name': model.name, 'value': model.value}}
    except Exception as e:
        request.dbsession.rollback()
        return {'success': False, 'message': str(e)}, 400


@view_config(route_name='api_model_detail', renderer='json', request_method='DELETE')
def api_delete_model(request):
    """DELETE - Hapus matakuliah"""
    try:
        model_id = request.matchdict['id']
        model = request.dbsession.query(models.MyModel).filter(models.MyModel.id == model_id).first()
        
        if not model:
            return {'success': False, 'message': f'Data ID {model_id} tidak ditemukan'}, 404
        
        request.dbsession.delete(model)
        request.dbsession.flush()
        return {'success': True, 'message': f'Data ID {model_id} berhasil dihapus'}
    except Exception as e:
        request.dbsession.rollback()
        return {'success': False, 'message': str(e)}, 400


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.txt for description and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

