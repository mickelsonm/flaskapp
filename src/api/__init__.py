from flask import Blueprint

mod = Blueprint('api', __name__)

@mod.route('/')
def home():
    return 'API home'

from gadgets import routes as gadgets_routes
from gizmos import routes as gizmos_routes

routes = (
    gadgets_routes +
    gizmos_routes)

for r in routes:
    mod.add_url_rule(
        r['rule'],
        endpoint=r.get('endpoint', None),
        view_func=r['view_func'],
        **r.get('options',{}))
