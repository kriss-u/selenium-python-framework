def assert_in(search_term, results):
    for item in results:
        assert search_term in item.text
