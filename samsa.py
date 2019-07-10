from bottle import Bottle, request, response, route
import subprocess, random, io, string

app = Bottle()

@app.error(404)
def error404(error):
    return "This is samsa. Try /swagger"

@app.route('/convert/v2tov3', method='POST')
@app.route('/v2tov3', method='POST')
def convert_v2_to_v3():

    try:
        syntax = request.query['format']
    except:
        syntax = "json"

    r = str(random.randint(1000,9999))
    f = "/tmp/" + r + ".api"
    with io.open(f, 'wb') as outfile:
        outfile.write(request.body.read())
    outfile.close()

    converted = "/tmp/" + r + ".api_out"
    output = subprocess.check_output(['api-spec-converter', '-s', syntax, '--from=swagger_2', '--to=openapi_3', f])

    if syntax == "json":
        response.headers['Content-Type'] = 'application/json; charset=UTF-8'
    else:
        response.headers['Content-Type'] = 'text/yaml; charset=UTF-8'

    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS, HEAD'

    return output

@app.route('/convert/v3tov2', method='POST')
@app.route('/v3tov2', method='POST')
def convert_v3_to_v2():

    try:
        syntax = request.query['format']
    except:
        syntax = "json"

    r = str(random.randint(1000,9999))
    f = "/tmp/" + r + ".api"
    with io.open(f, 'wb') as outfile:
        outfile.write(request.body.read())
    outfile.close()

    converted = "/tmp/" + r + ".api_out"
    output = subprocess.check_output(['api-spec-converter', '-s', syntax, '--from=openapi_3', '--to=swagger_2', f])

    if syntax == "json":
        response.headers['Content-Type'] = 'application/json; charset=UTF-8'
    else:
        response.headers['Content-Type'] = 'text/yaml; charset=UTF-8'

    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS, HEAD'

    return output

@app.get('/convert/swagger')
@app.get('/swagger')
@app.get('/swagger.json')
@app.get('/convert/swagger.json')
def swagger():

    swagger = '''{
    "swagger": "2.0",
    "info": {
        "version": "1.0",
        "title": "samsa",
        "description": "Convert between OpenAPI v2 and v3 formats (YAML/JSON)"
    },
    "basePath": "/convert",
    "paths": {
        "/v3tov2": {
            "post": {
                "operationId": "POST_v3tov2",
                "summary": "OpenAPI 3.0 to Swagger",
                "parameters": [
                    {
                        "name": "format",
                        "in": "query",
                        "type": "string",
                        "enum": [
                            "json",
                            "yaml"
                        ]
                    }
                ],
                "responses": {
                    "200": {
                        "description": ""
                    },
                    "400": {
                        "description": ""
                    }
                }
            }
        },
        "/v2tov3": {
            "post": {
                "operationId": "v2tov3",
                "summary": "Swagger to OpenAPI 3.0",
                "parameters": [
                    {
                        "name": "format",
                        "in": "query",
                        "type": "string",
                        "enum": [
                            "json",
                            "yaml"
                        ]
                    }
                ],
                "responses": {
                    "200": {
                        "description": ""
                    },
                    "400": {
                        "description": ""
                    }
                }
            }
        }
    },
    "definitions": {}
}'''
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS, HEAD'
    response.headers['Content-Type'] = 'application/json; charset=UTF-8'
    return swagger
