from src.pre_built.counter import count_ocurrences


def test_counter():
    PYTHON_STRING = "python"
    PYTHON_OCURRENCES = 1639
    python_counter = count_ocurrences("data/jobs.csv", PYTHON_STRING)
    assert python_counter == PYTHON_OCURRENCES

    JS_STRING = "javascript"
    JS_OCURRENCES = 122
    js_counter = count_ocurrences("data/jobs.csv", JS_STRING)
    assert js_counter == JS_OCURRENCES
