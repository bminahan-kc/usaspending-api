from usaspending_api.search.elasticsearch.filters.naics import NaicsCodes
from usaspending_api.common.exceptions import InvalidParameterException
from pytest import raises


def test_primative_naics_filter():
    assert NaicsCodes._query_string(require=["11"], exclude=[]) == "((11*))"


def test_primative_negative_naics_filter():
    assert NaicsCodes._query_string(require=[], exclude=["11"]) == "((NOT 11*))"


def test_positive_leaf_naics_filter():
    assert NaicsCodes._query_string(require=["112233"], exclude=[]) == "((112233))"


def test_negative_leaf_naics_filter():
    assert NaicsCodes._query_string(require=[], exclude=["112233"]) == "((NOT 112233))"


def test_two_positive_sibling_naics():
    assert NaicsCodes._query_string(require=["11", "22"], exclude=[]) == "((11*)) OR ((22*))"


def test_two_negative_sibling_naics():
    assert NaicsCodes._query_string(require=[], exclude=["11", "22"]) == "((NOT 11*)) AND ((NOT 22*))"


def test_simple_positive_hierarchy():
    assert NaicsCodes._query_string(require=["11", "1111"], exclude=[]) == "((11*) AND (((1111*))))"


def test_simple_negative_hierarchy():
    assert NaicsCodes._query_string(require=[], exclude=["11", "1111"]) == "((NOT 11*) OR (((NOT 1111*))))"


def test_positive_to_negative_cross_hierarchy():
    assert NaicsCodes._query_string(require=["11"], exclude=["1111"]) == "((11*) AND (((NOT 1111*))))"


def test_negative_to_positive_cross_hierarchy():
    assert NaicsCodes._query_string(require=["1111"], exclude=["11"]) == "((NOT 11*) OR (((1111*))))"


def test_positive_uncle_naics():
    assert NaicsCodes._query_string(require=["11", "2211"], exclude=[]) == "((11*)) OR ((2211*))"


def test_negative_uncle_naics():
    assert NaicsCodes._query_string(require=[], exclude=["11", "2211"]) == "((NOT 11*)) AND ((NOT 2211*))"


def test_competing_naics():
    assert NaicsCodes._query_string(require=["11"], exclude=["11"]) == "((11*)) AND ((NOT 11*))"


def test_duplicate_positive_naics():
    assert NaicsCodes._query_string(require=["11", "11"], exclude=[]) == "((11*)) OR ((11*))"


def test_duplicate_negative_naics():
    assert NaicsCodes._query_string(require=[], exclude=["11", "11"]) == "((NOT 11*)) AND ((NOT 11*))"


def test_three_layer_naics():
    assert (
        NaicsCodes._query_string(require=["11", "112233"], exclude=["1122"])
        == "((11*) AND (((NOT 1122*) OR (((112233))))))"
    )


def test_large_positive_list():
    large_list = _large_naics_list("")
    assert NaicsCodes._query_string(require=large_list, exclude=[]) == " OR ".join(
        [NaicsCodes._query_string(require=[f"{i}"], exclude=[]) for i in range(10, 100, 5)]
    )


def test_large_negative_list():
    large_list = _large_naics_list("")
    assert NaicsCodes._query_string(require=[], exclude=large_list) == " AND ".join(
        [NaicsCodes._query_string(require=[], exclude=[f"{i}"]) for i in range(10, 100, 5)]
    )


def test_bad_require_naics():
    with raises(InvalidParameterException):
        NaicsCodes.generate_elasticsearch_query({"require": ["111"]}, None)


def test_bad_exclude_naics():
    with raises(InvalidParameterException):
        NaicsCodes.generate_elasticsearch_query({"exclude": ["111"]}, None)


def _large_naics_list(prefix):
    return [f"{prefix}{i}" for i in range(10, 100, 5)]
