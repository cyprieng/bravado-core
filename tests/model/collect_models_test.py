import pytest

from bravado_core.model import collect_models, MODEL_MARKER
from bravado_core.spec import Spec


@pytest.fixture
def pet_model_spec():
    return {
        MODEL_MARKER: 'Pet',
        'type': 'object',
        'properties': {
            'name': {
                'type': 'string'
            }
        }
    }


def test_simple(minimal_swagger_dict, pet_model_spec):
    minimal_swagger_dict['definitions']['Pet'] = pet_model_spec
    swagger_spec = Spec(minimal_swagger_dict)
    models = {}
    collect_models(
        minimal_swagger_dict['definitions']['Pet'],
        MODEL_MARKER,
        ['definitions', 'Pet', 'x-model'],
        models=models,
        swagger_spec=swagger_spec)
    assert 'Pet' in models
