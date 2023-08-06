"""
Fuel and Electricity

This model calculates fuel and electricity data from the number of hours each machine is operated for using.
"""
from hestia_earth.schema import InputStatsDefinition, TermTermType
from hestia_earth.utils.model import filter_list_term_type
from hestia_earth.utils.tools import flatten, list_sum, non_empty_list

from hestia_earth.models.log import debugValues, logRequirements, logShouldRun
from hestia_earth.models.utils.term import get_lookup_value
from hestia_earth.models.utils.input import _new_input
from . import MODEL

REQUIREMENTS = {
    "Cycle": {
        "completeness.electricityFuel": "False",
        "practices": [{
            "@type": "Practice",
            "term.termType": "operation",
            "value": "> 0"
        }]
    }
}
LOOKUPS = {
    "operation": "fuelUse"
}
RETURNS = {
    "Input": [{
        "term.termType": "fuel",
        "value": "",
        "statsDefinition": "modelled",
        "operation": ""
    }]
}
MODEL_KEY = 'fuelElectricity'


def _input(term_id: str, value: float, operation: dict):
    input = _new_input(term_id, MODEL)
    input['value'] = [value]
    input['statsDefinition'] = InputStatsDefinition.MODELLED.value
    input['operation'] = operation
    return input


def _run_operation(cycle: dict):
    def exec(operation: dict):
        input = operation.get('input', {})
        input_term = input.get('term', {})
        input_term_id = input_term.get('@id')
        coefficient = input.get('value')
        value = list_sum(operation.get('value', []))

        debugValues(cycle, model=MODEL, term=input_term_id,
                    operation=operation.get('@id'),
                    value=value,
                    coefficient=coefficient)
        logShouldRun(cycle, MODEL, input_term_id, True, model_key=MODEL_KEY, operation=operation.get('@id'))

        return _input(input_term.get('@id'), coefficient * value, operation.get('term', {}))
    return exec


def _should_run_operation(cycle: dict):
    def exec(practice: dict):
        term = practice.get('term', {})
        term_id = term.get('@id')
        value = list_sum(practice.get('value', []))
        has_value = value > 0

        coeffs = get_lookup_value(term, LOOKUPS['operation'], model=MODEL, model_key=MODEL_KEY)
        values = non_empty_list(coeffs.split(';')) if coeffs else []
        inputs = [{'term': {'@id': c.split(':')[0]}, 'value': float(c.split(':')[1])} for c in values]
        has_lookup_value = len(inputs) > 0

        logRequirements(cycle, model=MODEL, term=term_id, model_key=MODEL_KEY,
                        has_value=has_value,
                        has_lookup_value=has_lookup_value)

        should_run = all([has_value, has_lookup_value])
        logShouldRun(cycle, MODEL, term_id, should_run, model_key=MODEL_KEY)
        return [{
            **practice,
            'input': input
        } for input in inputs] if should_run else []
    return exec


def _should_run(cycle: dict):
    is_incomplete = not cycle.get('completeness', {}).get('electricityFuel', False)
    operations = filter_list_term_type(cycle.get('practices', []), TermTermType.OPERATION)
    operations = flatten(map(_should_run_operation(cycle), operations))
    has_operations = len(operations) > 0

    logRequirements(cycle, model=MODEL, model_key=MODEL_KEY,
                    is_incomplete=is_incomplete,
                    has_operations=has_operations,
                    operations=';'.join(non_empty_list(map(lambda v: v.get('term', {}).get('@id'), operations))))

    should_run = all([is_incomplete, has_operations])
    logShouldRun(cycle, MODEL, None, should_run, model_key=MODEL_KEY)
    return should_run, operations


def run(cycle: dict):
    should_run, operations = _should_run(cycle)
    return list(map(_run_operation(cycle), operations)) if should_run else []
