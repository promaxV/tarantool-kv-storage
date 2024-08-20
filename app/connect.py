from tarantool import connect

tarantool_connection = None

def init_tarantool_connection(host, port):
    global tarantool_connection
    tarantool_connection = connect(host, port)
    tarantool_connection.eval(r'''
    box.cfg{}
    if not box.space.kv_store then
        local space = box.schema.space.create('kv_store')
        space:format({{name='key', type='string'}, {name='value', type='any'}})
        space:create_index('primary', {type = 'hash', parts = {{'key'}}})
    end
    ''')

def get_tarantool_connection():
    return tarantool_connection

async def write_data(data):
    for key, value in data.items():
        tarantool_connection.insert("kv_store", (key, value))

async def read_data(keys):
    result = {}
    for key in keys:
        res = tarantool_connection.select("kv_store", key)
        if res:
            result[key] = res[0][1]
    return result