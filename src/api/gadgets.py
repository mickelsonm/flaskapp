routes = []

def list_gadgets():
	return 'Listing Gadgets'

routes.append(dict(
    rule='/gadgets',
    view_func=list_gadgets))

def add_gadget():
    return 'Add Gadget'

routes.append(dict(
    rule='/gadget',
    view_func=add_gadget,
    options=dict(methods=['POST'])))

def update_gadget():
    return 'Update Gadget'

routes.append(dict(
    rule='/gadget',
    view_func=add_gadget,
    options=dict(methods=['PUT'])))

def delete_gadget():
    return 'Delete Gadget'

routes.append(dict(
    rule='/gadget',
    view_func=delete_gadget,
    options=dict(methods=['DELETE'])))
