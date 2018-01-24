

def wsgi_app(environ, start_response):

    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain'),
    ]

    start_response(status, headers)

    query_string = environ.get('QUERY_STRING')
    # print(query_string)

    return (query_string.replace('&', '\n').encode(),)

