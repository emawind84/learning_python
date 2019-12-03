Python 3.4.2 (default, Oct 19 2014, 13:31:11) 
[GCC 4.9.1] on linux
Type "copyright", "credits" or "license()" for more information.
>>> import hvac
>>> client = hvac.Client()
>>> client.is_authenticated()
False
>>> client.is_initialized
<bound method Client.is_initialized of <hvac.v1.Client object at 0x74b86990>>
>>> client.is_initialized()
True
>>> client.token = '8fce8b0b-b36c-3d71-4b86-2c5d2b0af61a'
>>> client.is_authenticated()
True
>>> client.write('secret/foo', baz='bar')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    client.write('secret/foo', baz='bar')
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/v1/__init__.py", line 189, in write
    response = self._adapter.post('/v1/{0}'.format(path), json=kwargs, wrap_ttl=wrap_ttl)
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/adapters.py", line 103, in post
    return self.request('post', url, **kwargs)
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/adapters.py", line 233, in request
    utils.raise_for_error(response.status_code, text, errors=errors)
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/utils.py", line 35, in raise_for_error
    raise exceptions.InvalidPath(message, errors=errors)
hvac.exceptions.InvalidPath: {"request_id":"c042d655-4479-063a-b372-6d4e5de2ff74","lease_id":"","renewable":false,"lease_duration":0,"data":null,"wrap_info":null,"warnings":["Invalid path for a versioned K/V secrets engine. See the API docs for the appropriate API endpoints to use. If using the Vault CLI, use 'vault kv put' for this operation."],"auth":null}
>>> client.write('secret/foo', baz='bar', lease='1h')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    client.write('secret/foo', baz='bar', lease='1h')
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/v1/__init__.py", line 189, in write
    response = self._adapter.post('/v1/{0}'.format(path), json=kwargs, wrap_ttl=wrap_ttl)
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/adapters.py", line 103, in post
    return self.request('post', url, **kwargs)
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/adapters.py", line 233, in request
    utils.raise_for_error(response.status_code, text, errors=errors)
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/utils.py", line 35, in raise_for_error
    raise exceptions.InvalidPath(message, errors=errors)
hvac.exceptions.InvalidPath: {"request_id":"6a1dfcc0-c4b4-45e8-87c1-171395b01def","lease_id":"","renewable":false,"lease_duration":0,"data":null,"wrap_info":null,"warnings":["Invalid path for a versioned K/V secrets engine. See the API docs for the appropriate API endpoints to use. If using the Vault CLI, use 'vault kv put' for this operation."],"auth":null}
>>> client.write('secret/foo', baz='asd')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    client.write('secret/foo', baz='asd')
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/v1/__init__.py", line 189, in write
    response = self._adapter.post('/v1/{0}'.format(path), json=kwargs, wrap_ttl=wrap_ttl)
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/adapters.py", line 103, in post
    return self.request('post', url, **kwargs)
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/adapters.py", line 233, in request
    utils.raise_for_error(response.status_code, text, errors=errors)
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/utils.py", line 35, in raise_for_error
    raise exceptions.InvalidPath(message, errors=errors)
hvac.exceptions.InvalidPath: {"request_id":"88be5424-bfb5-5792-2cac-582f4baf691a","lease_id":"","renewable":false,"lease_duration":0,"data":null,"wrap_info":null,"warnings":["Invalid path for a versioned K/V secrets engine. See the API docs for the appropriate API endpoints to use. If using the Vault CLI, use 'vault kv put' for this operation."],"auth":null}
>>> client.is_initialized()
True
>>> client.is_sealed()
False
>>> client.list('secret')
>>> client.list()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    client.list()
TypeError: list() missing 1 required positional argument: 'path'
>>> client.seal()
>>> client.unseal()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    client.unseal()
TypeError: unseal() missing 1 required positional argument: 'key'
>>> client.unseal('1gu8WGf16WZMXwwYLtc8afDaVX9szlb0p20u4BqlxOo=')
{'n': 1, 'sealed': False, 'version': '0.11.1', 'type': 'shamir', 'nonce': '', 'cluster_name': 'vault-cluster-949c3b15', 't': 1, 'cluster_id': '1225d916-7a0c-bb82-03a8-8c9427342350', 'progress': 0}
>>> client.write('secret/asd', pippo='ciccio')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    client.write('secret/asd', pippo='ciccio')
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/v1/__init__.py", line 189, in write
    response = self._adapter.post('/v1/{0}'.format(path), json=kwargs, wrap_ttl=wrap_ttl)
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/adapters.py", line 103, in post
    return self.request('post', url, **kwargs)
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/adapters.py", line 233, in request
    utils.raise_for_error(response.status_code, text, errors=errors)
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/utils.py", line 35, in raise_for_error
    raise exceptions.InvalidPath(message, errors=errors)
hvac.exceptions.InvalidPath: {"request_id":"18c7a51b-74a1-6a78-717f-1031e58e736f","lease_id":"","renewable":false,"lease_duration":0,"data":null,"wrap_info":null,"warnings":["Invalid path for a versioned K/V secrets engine. See the API docs for the appropriate API endpoints to use. If using the Vault CLI, use 'vault kv put' for this operation."],"auth":null}
>>> client.write('asd', pippo='ciccio')
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    client.write('asd', pippo='ciccio')
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/v1/__init__.py", line 189, in write
    response = self._adapter.post('/v1/{0}'.format(path), json=kwargs, wrap_ttl=wrap_ttl)
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/adapters.py", line 103, in post
    return self.request('post', url, **kwargs)
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/adapters.py", line 233, in request
    utils.raise_for_error(response.status_code, text, errors=errors)
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/utils.py", line 35, in raise_for_error
    raise exceptions.InvalidPath(message, errors=errors)
hvac.exceptions.InvalidPath: no handler for route 'asd'
>>> client.is_initialized()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    client.is_initialized()
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/v1/__init__.py", line 226, in is_initialized
    return self._adapter.get('/v1/sys/init').json()['initialized']
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/adapters.py", line 90, in get
    return self.request('get', url, **kwargs)
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/adapters.py", line 233, in request
    utils.raise_for_error(response.status_code, text, errors=errors)
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/utils.py", line 39, in raise_for_error
    raise exceptions.InternalServerError(message, errors=errors)
hvac.exceptions.InternalServerError: failed to check for initialization: open vault/core: not a directory
>>> client.is_initialized()
False
>>> client.list_secret_backends()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    client.list_secret_backends()
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/v1/__init__.py", line 556, in list_secret_backends
    return self._adapter.get('/v1/sys/mounts').json()
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/adapters.py", line 90, in get
    return self.request('get', url, **kwargs)
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/adapters.py", line 233, in request
    utils.raise_for_error(response.status_code, text, errors=errors)
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/utils.py", line 43, in raise_for_error
    raise exceptions.VaultDown(message, errors=errors)
hvac.exceptions.VaultDown: Vault is sealed
>>> client.initialize()
{'root_token': '6e3de8f4-26d9-baa1-e5c7-2051ca9d0e41', 'keys': ['29728ae93f4419e86a75ea0e0b5d7963f2e1a2062eecdf6c44a081c6963336ebce', '707b08c23f1f6170bd995f58f8e8e36682fe3019260150c351c577cb72317f2885', '45d1eb9881d6e954978e45b316b61a474b19fa1d7a58889713ae0d186bea68ad29', '04c4355c9553197c446fc72a63e03d95f8abed86be25a3c659dfc3b960bc9d3b6d', '5568ecc077afb6c736d384788fd6bbd78096c1122304ea103d4d404fb1cff618f9'], 'keys_base64': ['KXKK6T9EGehqdeoOC115Y/LhogYu7N9sRKCBxpYzNuvO', 'cHsIwj8fYXC9mV9Y+OjjZoL+MBkmAVDDUcV3y3IxfyiF', 'RdHrmIHW6VSXjkWzFrYaR0sZ+h16WIiXE64NGGvqaK0p', 'BMQ1XJVTGXxEb8cqY+A9lfir7Ya+JaPGWd/DuWC8nTtt', 'VWjswHevtsc204R4j9a714CWwRIjBOoQPU1AT7HP9hj5']}
>>> client.initialize()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    client.initialize()
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/v1/__init__.py", line 251, in initialize
    return self._adapter.put('/v1/sys/init', json=params).json()
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/adapters.py", line 116, in put
    return self.request('put', url, **kwargs)
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/adapters.py", line 233, in request
    utils.raise_for_error(response.status_code, text, errors=errors)
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/utils.py", line 29, in raise_for_error
    raise exceptions.InvalidRequest(message, errors=errors)
hvac.exceptions.InvalidRequest: Vault is already initialized
>>> client.key_status()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    client.key_status()
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/v1/__init__.py", line 380, in key_status
    return self._adapter.get('/v1/sys/key-status').json()
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/adapters.py", line 90, in get
    return self.request('get', url, **kwargs)
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/adapters.py", line 233, in request
    utils.raise_for_error(response.status_code, text, errors=errors)
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/utils.py", line 43, in raise_for_error
    raise exceptions.VaultDown(message, errors=errors)
hvac.exceptions.VaultDown: Vault is sealed
>>> keys = ['29728ae93f4419e86a75ea0e0b5d7963f2e1a2062eecdf6c44a081c6963336ebce', '707b08c23f1f6170bd995f58f8e8e36682fe3019260150c351c577cb72317f2885', '45d1eb9881d6e954978e45b316b61a474b19fa1d7a58889713ae0d186bea68ad29', '04c4355c9553197c446fc72a63e03d95f8abed86be25a3c659dfc3b960bc9d3b6d', '5568ecc077afb6c736d384788fd6bbd78096c1122304ea103d4d404fb1cff618f9']
>>> client.unseal(keys)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    client.unseal(keys)
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/v1/__init__.py", line 301, in unseal
    return self._adapter.put('/v1/sys/unseal', json=params).json()
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/adapters.py", line 116, in put
    return self.request('put', url, **kwargs)
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/adapters.py", line 233, in request
    utils.raise_for_error(response.status_code, text, errors=errors)
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/utils.py", line 29, in raise_for_error
    raise exceptions.InvalidRequest(message, errors=errors)
hvac.exceptions.InvalidRequest: failed to parse JSON input: json: cannot unmarshal array into Go struct field UnsealRequest.Key of type string
>>> client.unseal_multi
<bound method Client.unseal_multi of <hvac.v1.Client object at 0x74b86990>>
>>> client.unseal_multi(keys)
{'n': 5, 'sealed': False, 'version': '0.11.1', 'type': 'shamir', 'nonce': '', 'cluster_name': 'vault-cluster-141fc98a', 't': 3, 'cluster_id': '9d321506-5f9b-aa2f-67ca-2618bce4c038', 'progress': 0}
>>> client.is_
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    client.is_
AttributeError: 'Client' object has no attribute 'is_'
>>> client.is_authenticated()
False
>>> client.token = '6e3de8f4-26d9-baa1-e5c7-2051ca9d0e41'
>>> client.is_authenticated()
True
>>> client.write('secret/asd', asd='qweqwe')
>>> client.read('secret/asd')
{'data': {'asd': 'qweqwe'}, 'auth': None, 'renewable': False, 'lease_id': '', 'wrap_info': None, 'request_id': '3667ea35-7734-3604-4992-c97b842232dc', 'warnings': None, 'lease_duration': 2764800}
>>> client.logout()
>>> client.read('secret/asd')
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    client.read('secret/asd')
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/v1/__init__.py", line 157, in read
    return self._adapter.get('/v1/{0}'.format(path), wrap_ttl=wrap_ttl).json()
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/adapters.py", line 90, in get
    return self.request('get', url, **kwargs)
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/adapters.py", line 233, in request
    utils.raise_for_error(response.status_code, text, errors=errors)
  File "/media/usb2/learning_log/env/lib/python3.4/site-packages/hvac/utils.py", line 29, in raise_for_error
    raise exceptions.InvalidRequest(message, errors=errors)
hvac.exceptions.InvalidRequest: missing client token
>>> client.token = '6e3de8f4-26d9-baa1-e5c7-2051ca9d0e41'
>>> client.read('secret/asd')
{'data': {'asd': 'qweqwe'}, 'auth': None, 'renewable': False, 'lease_id': '', 'wrap_info': None, 'request_id': '7aa43837-13af-2e2a-2c96-92dad16bbf4c', 'warnings': None, 'lease_duration': 2764800}
>>> data = client.read('secret/asd')
>>> data
{'data': {'asd': 'qweqwe'}, 'auth': None, 'renewable': False, 'lease_id': '', 'wrap_info': None, 'request_id': '0d83c492-6441-c897-3d3f-8bc0b1b6bb73', 'warnings': None, 'lease_duration': 2764800}
>>> data.data
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    data.data
AttributeError: 'dict' object has no attribute 'data'
>>> print(data.data)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print(data.data)
AttributeError: 'dict' object has no attribute 'data'
>>> data
{'data': {'asd': 'qweqwe'}, 'auth': None, 'renewable': False, 'lease_id': '', 'wrap_info': None, 'request_id': '0d83c492-6441-c897-3d3f-8bc0b1b6bb73', 'warnings': None, 'lease_duration': 2764800}
>>> data.auth
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    data.auth
AttributeError: 'dict' object has no attribute 'auth'
>>> data['data']
{'asd': 'qweqwe'}
>>> 
