from flask_injector import request

from services.FibService import FibService
from services.HealthService import HealthService
from repository.MyDatabase import DatabaseBase, MSSqlDatabase


def configure(binder):
    binder.bind(DatabaseBase, to=MSSqlDatabase, scope=request)
    binder.bind(FibService, to=FibService, scope=request)
    binder.bind(HealthService, to=HealthService, scope=request)
