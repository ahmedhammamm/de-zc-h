import re

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    data.columns = data.columns.str.replace(r'([a-z0-9])([A-Z])', r'\1_\2').str.lower() 

    cond_1 = data['passenger_count'] > 0
    cond_2 = data['trip_distance'] > 0

    return data[cond_1 & cond_2]


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are passenger_count that equal to zero'
    assert output['trip_distance'].isin([0]).sum() == 0, 'There are trip_distance that equal to zero'
    assert 'vendor_id' in output.columns