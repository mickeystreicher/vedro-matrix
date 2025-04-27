from unittest.mock import Mock

from vedro import catched
from vedro_fn import given, scenario, then, when

from vedro_matrix import ParamsMatrix, params_matrix


@scenario()
def create_params_matrix():
    with given:
        matrix = None

    with when:
        matrix = params_matrix(["chrome", "firefox"])

    with then:
        assert isinstance(matrix, ParamsMatrix)


@scenario()
def try_to_create_params_matrix_with_no_args():
    with when, catched(Exception) as exc_info:
        params_matrix()

    with then:
        assert exc_info.type is ValueError


@scenario()
def generate_combinations_of_three_params():
    with given:
        mock = Mock()
        matrix = params_matrix(["x1", "x2"], ["y1", "y2"], ["z1", "z2"])

    with when:
        res = matrix(mock)

    with then:
        assert res == mock
        assert mock.mock_calls == []
        assert getattr(mock, "__vedro__params__") == [
            (("x2", "y2", "z2"), {}, ()),
            (("x2", "y2", "z1"), {}, ()),
            (("x2", "y1", "z2"), {}, ()),
            (("x2", "y1", "z1"), {}, ()),
            (("x1", "y2", "z2"), {}, ()),
            (("x1", "y2", "z1"), {}, ()),
            (("x1", "y1", "z2"), {}, ()),
            (("x1", "y1", "z1"), {}, ()),
        ]


@scenario()
def generate_combinations_with_keyword_args():
    with given:
        mock = Mock()
        matrix = params_matrix(x=["x1", "x2"], y=["y1", "y2"])

    with when:
        res = matrix(mock)

    with then:
        assert res == mock
        assert mock.mock_calls == []
        assert getattr(mock, "__vedro__params__") == [
            (("x2", "y2"), {}, ()),
            (("x2", "y1"), {}, ()),
            (("x1", "y2"), {}, ()),
            (("x1", "y1"), {}, ()),
        ]


@scenario()
def generate_combinations_with_mixed_args():
    with given:
        mock = Mock()
        matrix = params_matrix(["x1", "x2"], y=["y1", "y2"])

    with when:
        res = matrix(mock)

    with then:
        assert res == mock
        assert mock.mock_calls == []
        assert getattr(mock, "__vedro__params__") == [
            (("x2", "y2"), {}, ()),
            (("x2", "y1"), {}, ()),
            (("x1", "y2"), {}, ()),
            (("x1", "y1"), {}, ()),
        ]
