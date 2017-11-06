"""
Simple WSGI, which returns GET and POST parameters.
"""
from pprint import pformat
from cgi import parse_qsl

def get_post(environ, start_response):
    output = ['<!DOCTYPE html>\n']
    output.append('<html lang="en">\n')
    output.append('    <head>\n')
    output.append('        <meta charset="utf-8" />\n')
    output.append('        <title>DZ - 2. N 3.</title>\n')
    output.append('    </head>\n')
    output.append('    <body>\n')
    output.append('        <h3>Hello, World!</h3>\n')
    output.append('        <div>\n')
    output.append('            <h5>Post:</h5>\n')
    output.append('            <form method="post">\n')
    output.append('                <input type="text" name = "post">\n')
    output.append('                <input type="submit" value="Send">\n')
    output.append('            </form>\n')
    output.append('        </div>\n')
    output.append('        <div>\n')
    method = parse_qsl(environ['QUERY_STRING'])
    if environ['REQUEST_METHOD'] == 'POST':
        output.append('            <h5>Post Parameters:</h5>\n')
        output.append('            <ul>\n')
        output.append('                <li>')
        result = pformat(environ['wsgi.input'].read())
        result = result[1 : (len(result) - 1)]
        result = result.replace('=', ' = ')
        output.append(result)
        output.append('</li>\n')
        output.append('            </ul>\n')

    if environ['REQUEST_METHOD'] == 'GET':
        if environ['QUERY_STRING'] != '':
            output.append('            <h5>Get Parameters:</h5>\n')
            output.append('            <ul>\n')
            for result in method:
                output.append('             <li>')
                output.append(' = '.join(result))
                output.append('</li>\n')
            output.append('            </ul>\n')
    output.append('        </div>\n')
    output.append('    </body>\n')
    output.append('</html>')
    output_len = sum(len(line) for line in output)
    start_response('200 OK', [('Content-type', 'text/html'),
                              ('Content-Length', str(output_len))])
    return output

