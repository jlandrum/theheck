import pytest


@pytest.fixture
def builtins_open(mocker):
    return mocker.patch('six.moves.builtins.open')


@pytest.fixture
def isfile(mocker):
    return mocker.patch('os.path.isfile', return_value=True)


@pytest.fixture
@pytest.mark.usefixtures('isfile')
def history_lines(mocker):
    def aux(lines):
        mock = mocker.patch('io.open')
        mock.return_value.__enter__ \
            .return_value.readlines.return_value = lines

    return aux


@pytest.fixture
def config_exists(mocker):
    path_mock = mocker.patch('theheck.shells.generic.Path')
    return path_mock.return_value \
        .expanduser.return_value \
        .exists
