routes = []

def list_gizmos():
	return 'Listing Gizmos'

routes.append(dict(
    rule='/gizmos',
    view_func=list_gizmos))

def add_gizmo():
    return 'Add Gizmo'

routes.append(dict(
    rule='/gizmo',
    view_func=add_gizmo,
    options=dict(methods=['POST'])))

def update_gizmo():
    return 'Update Gizmo'

routes.append(dict(
    rule='/gizmo',
    view_func=update_gizmo,
    options=dict(methods=['PUT'])))

def delete_gizmo():
    return 'Delete Gadget'

routes.append(dict(
    rule='/gadget',
    view_func=delete_gizmo,
    options=dict(methods=['DELETE'])))
