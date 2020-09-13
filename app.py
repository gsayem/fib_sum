from timeit import default_timer as timer

from flask import Flask, jsonify
from flask_caching import Cache
from flask_injector import FlaskInjector
from injector import inject

from di.dependencies import configure
from services.FibService import FibService
from services.HealthService import HealthService
from utility.app_constant import CACHE_KEY_PREFIX_FIBONACCI_SUM_SERIES, CACHE_TYPE_KEY, CACHE_TYPE_VALUE

app = Flask(__name__)
cached = Cache(config={CACHE_TYPE_KEY: CACHE_TYPE_VALUE})
cached.init_app(app)


# End point /fib/number
@inject
@app.route('/fib/<number>')
def fib_combination_series(service: FibService, number):
    if number.isdigit() and int(number) > 0:
        combination_series = cached.get(CACHE_KEY_PREFIX_FIBONACCI_SUM_SERIES + number)
        if combination_series is None:
            print("Data not found in cache.")
            combination_series = service.get_combination_sum(int(number))
            cached.set(CACHE_KEY_PREFIX_FIBONACCI_SUM_SERIES + number, combination_series)
        else:
            print("Data found in cache.")
    else:
        return jsonify("Only positive value and more than 0 allow"), 500

    jsonify_com = jsonify(combination_series)
    service.save_data(int(number), str(jsonify_com.json))
    return jsonify_com, 200


# End point /db/number
# It return from DB based on number if exist
@inject
@app.route('/db/<number>')
def get_fib_combination_series_by_val(service: FibService, number):
    if number.isdigit() and int(number) > 0:
        combination_series = service.get_data_by_fib(int(number))
        return jsonify(combination_series), 200
    else:
        return jsonify("Only positive value and more than 0 allow"), 500


# End point /db
# All data return from DB if exist
@inject
@app.route('/db')
def get_fib_combination_series_all(service: FibService):
    combination_series = service.get_all_data()
    return jsonify(combination_series), 200

# System health
@inject
@app.route('/health')
def get_system_health(service: HealthService):
    return jsonify(service.get_system_health()), 200


# benchmark with some data
@inject
@app.route('/benchmark')
def benchmarking(service: FibService):
    result = []
    start = timer()
    service.get_combination_sum(10)
    end = timer()
    output1 = "Total time (sec) for 10 Fib : " + str(end - start)
    result.append(output1)

    start = timer()
    service.get_combination_sum(15)
    end = timer()
    output1 = "Total time (sec) for 15 Fib : " + str(end - start)
    result.append(output1)

    start = timer()
    service.get_combination_sum(20)
    end = timer()
    output1 = "Total time (sec) for 20 Fib : " + str(end - start)
    result.append(output1)

    start = timer()
    service.get_combination_sum(30)
    end = timer()
    output1 = "Total time (sec) for 30 Fib : " + str(end - start)
    result.append(output1)

    start = timer()
    service.get_combination_sum(40)
    end = timer()
    output1 = "Total time (sec) for 40 Fib : " + str(end - start)
    result.append(output1)

    start = timer()
    service.get_combination_sum(50)
    end = timer()
    output1 = "Total time (sec) for 50 Fib : " + str(end - start)
    result.append(output1)

    start = timer()
    service.get_combination_sum(60)
    end = timer()
    output1 = "Total time (sec) for 60 Fib : " + str(end - start)
    result.append(output1)

    start = timer()
    service.get_combination_sum(70)
    end = timer()
    output1 = "Total time (sec) for 70 Fib : " + str(end - start)
    result.append(output1)

    start = timer()
    service.get_combination_sum(80)
    end = timer()
    output1 = "Total time (sec) for 80 Fib : " + str(end - start)
    result.append(output1)

    start = timer()
    service.get_combination_sum(90)
    end = timer()
    output1 = "Total time (sec) for 90 Fib : " + str(end - start)
    result.append(output1)

    start = timer()
    service.get_combination_sum(100)
    end = timer()
    output1 = "Total time (sec) for 100 Fib : " + str(end - start)
    result.append(output1)

    return jsonify(result), 200


# Setup Flask Injector
FlaskInjector(app=app, modules=[configure])
