
# API Documentation

To test the API, you can use the following cURL commands. You can also use Postman or any other API testing tool.

------------------------------------------------------------------------------------------

#### Create a user

<details>
 <summary><code>POST</code> <code><b>/</b></code><code>api</code><code>(Create a person and store in a database)</code></summary>

##### Parameters

> | name      |  type     | data type               | description                                                           |
> |-----------|-----------|-------------------------|-----------------------------------------------------------------------|
> | name      |  required | json(string)  |name of user  |

##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `application/json`        | `{"name":<name stored>,"id":"user_id"}`     |
> | `400`         | `application/json`         | `{"msg":"name already in use"}`    |
> |`500` | `application/json` | `{"msg":"failed to create user"}` |

##### Example cURL

> ```javascript
>  curl -X POST -H "Content-Type: application/json" --data @post.json "http://localhost:8000/api"
> ```
>
>```python
>import requests
>import json
>
>url = "http://localhost:8000/api"
>payload = {
>  "name": "test"
>}
>headers = {
>  'Content-Type': 'application/json'
>}
>
>response = requests.request("POST", url, headers=headers, data = json.dumps(payload))
>
>print(response.text.encode('utf8'))

</details>

------------------------------------------------------------------------------------------

#### Get all users

<details>
 <summary><code>GET</code> <code><b>/</b></code><code>api</code><code>(Get all persons from a database)</code></summary>

##### Parameters

> | name      |  type     | data type               | description                                                           |
> |-----------|-----------|-------------------------|-----------------------------------------------------------------------|
> | none      |  required | none  |none |

##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `application/json`        | `list({"name":<name stored>,"id":"user_id"})`     |
> | `404`         | `application/json`         | `{"msg":"no users found"}`    |
> |`500` | `application/json` | `{"msg":"failed to get users"}` |

##### Example cURL

> ```javascript
>  curl -X GET -H "Content-Type: application/json" "http://localhost:8000/api"
> ```

>```python
>import requests
>import json
>
>url = "http://localhost:8000/api"
>payload = {}
>headers = {
>  'Content-Type': 'application/json'
>}
>
>response = requests.request("GET", url, headers=headers, data = payload)
>
>print(response.text.encode('utf8'))
>```

</details>

------------------------------------------------------------------------------------------

#### Get a user

<details>
 <summary><code>GET</code> <code><b>/</b></code><code>api/{idOrName}</code><code>(Get a person from a database)</code></summary>

##### Parameters

> | name      |  type     | data type               | description                                                           |
> |-----------|-----------|-------------------------|-----------------------------------------------------------------------|
> | IdOrName      |  required | url(param)  |name or id of user |
>

##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `201`         | `application/json`        | `{"name":<name stored>,"id":"user_id"}`     |
> | `400`         | `application/json`                | `{"msg":"id or name is required"}`                            |
> | `404`         | `application/json`         | `{"msg":"user not found"}`    |
 
##### Example cURL

> ```javascript
>  curl -X GET -H "Content-Type: application/json" "http://localhost:8000/api/{idorname}"
> ```

>```python
>import requests
>import json
>
>url = "http://localhost:8000/api/{idorname}"
>payload = {}
>headers = {
>  'Content-Type': 'application/json'
>}
>
>response = requests.request("GET", url, headers=headers, data = payload)
>
>print(response.text.encode('utf8'))
>```

</details>

------------------------------------------------------------------------------------------

#### Update a user

<details>
 <summary><code>PUT</code> <code><b>/</b></code><code>api/{idOrName}</code><code>(Update a person in a database)</code></summary>

##### Parameters

> | name      |  type     | data type               | description                                                           |
> |-----------|-----------|-------------------------|-----------------------------------------------------------------------|
> | IdOrName      |  required | url(param)  |name or id of user |
> | name      |  required | json(string)  |name of user  |

##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `400`         | `application/json`         | `{"msg":"name already in use"}`    |
> | `404`         | `application/json`         | `{"msg":"user not found"}`    |
> |`500` | `application/json` | `{"msg":"failed to update user"}` |

##### Example cURL

> ```javascript
>  curl -X PUT -H "Content-Type: application/json" --data @put.json "http://localhost:8000/api/{idorname}"
> ```

>```python
>import requests
>import json
>
>url = "http://localhost:8000/api/{idorname}"
>payload = {}
>headers = {
>  'Content-Type': 'application/json'
>}
>
>response = requests.request("PUT", url, headers=headers, data = payload)
>
>print(response.text.encode('utf8'))
>```

</details>

------------------------------------------------------------------------------------------

#### Delete a user

<details>
 <summary><code>DELETE</code> <code><b>/</b></code><code>api/{idOrName}</code><code>(Delete a person from a database)</code></summary>

##### Parameters

> | name      |  type     | data type               | description                                                           |
> |-----------|-----------|-------------------------|-----------------------------------------------------------------------|
> | IdOrName      |  required | url(param)  |name or id of user |

##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `204`         | `application/json`        | `{"msg":"user deleted"}`     |
> | `404`         | `application/json`         | `{"msg":"user not found"}`    |
> |`500` | `application/json` | `{"msg":"failed to delete user"}` |

##### Example cURL

> ```javascript
>  curl -X DELETE -H "Content-Type: application/json" "http://localhost:8000/api/{idorname}"
> ```
>```python
>import requests
>import json
>
>url = "http://localhost:8000/api/{idorname}"
>payload = {}
>headers = {
>  'Content-Type': 'application/json'
>}
>
>response = requests.request("DELETE", url, headers=headers, data = payload)
>
>print(response.text.encode('utf8'))
>```

</details>

------------------------------------------------------------------------------------------
