from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.testclient import TestClient
import pytest
import starlette
import starlette_logger
import structlog

structlog.configure()

class TestMiddleware:

    @pytest.fixture
    def testapp(self):
        app = Starlette()
        app.add_route("/health", lambda *args: JSONResponse({}))
        yield app

    @pytest.fixture
    def testclient(self, testapp: Starlette):
        yield TestClient(testapp)

    def test_init_idware(self, testapp: Starlette, testclient: TestClient):
        testapp.add_middleware(starlette_logger.RequestIdMiddleware)
        testclient.get("/health")

    def test_init_logware(self, testapp: Starlette, testclient: TestClient):
        testapp.add_middleware(starlette_logger.RequestLoggerMiddleware)
        testclient.get("/health")


