from starlette.applications import Starlette
import pytest
import starlette
import starlette_logger

class TestRequestIdMiddleware:

    @pytest.fixture
    def testapp(self):
        app = Starlette()
        yield app

    def test_init(self, testapp):
        testapp.add_middleware(starlette_logger.RequestIdMiddleware)

