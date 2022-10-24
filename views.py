from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from builder import build_query
from models import BatchRequestParams

main_bp = Blueprint('main', __name__)


@main_bp.route('/perform_query', methods=['POST'])
def perform_query():
    """
    Perform a query against the database.
    """
    try:
        params = BatchRequestParams().load(request.json)
    except ValidationError as error:
        return error.messages, 400

    result = None
    for query in params['queries']:
        build_query(
            cmd=query['cmd'],
            param=query['value'],
            data=result,
        )

    return jsonify(result)
