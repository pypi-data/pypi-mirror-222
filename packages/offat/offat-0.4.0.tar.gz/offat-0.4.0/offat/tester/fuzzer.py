import random
import string

def generate_phone_number():
    '''Generate Random 10 digit phone number starting with 72'''
    return '72'+''.join(random.choice(string.digits) for _ in range(8))

def generate_random_chars(length):
    """Generate a random string of given length containing characters only."""
    characters = string.ascii_letters
    return ''.join(random.choice(characters) for _ in range(length))


def generate_random_char_digits(length):
    """Generate a random string of given length containing characters and digits only."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def generate_random_string(length):
    """Generate a random string of given length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


def fill_schema_params(params:dict[dict], param_in:str=None,is_required:bool=None):
    schema_params = []
    for var_name,var_data in params.items():
        var_type = var_data.get('type')

        match var_type:
            case 'string':
                if 'email' in var_name:
                    var_value = generate_random_char_digits(6) + '@example.com'
                elif 'password' in var_name:
                    var_value = generate_random_string(15)
                elif 'phone' in var_name:
                    var_value = generate_phone_number()
                else:
                    var_value = generate_random_string(10)
            
            case 'integer':
                var_value = random.randint(0,1000)
            
            case _:
                var_value = generate_random_string(10)

        var_data['value'] = var_value
        var_data['name'] = var_name
         
        if is_required:
            var_data['required'] = is_required

        if param_in:
            var_data['in'] = param_in

        schema_params.append(var_data)

    return schema_params


def fill_params(params:list[dict]):
    schema_params = []
    for index in range(len(params)):
        param_type = params[index].get('type')
        param_is_required = params[index].get('required')
        param_in = params[index].get('in')

        match param_type:
            case 'string':
                param_value = generate_random_chars(10)

            case 'integer':
                param_value = random.randint(0,1000)
            
            # TODO: handle file type
            
            case _: # default case
                param_value = generate_random_string(10)
        
        if params[index].get('schema'):
            schema_obj = params[index].get('schema',{}).get('properties',{})
            filled_schema_params = fill_schema_params(schema_obj, param_in, param_is_required)

            schema_params.append(filled_schema_params)
        else:
            params[index]['value'] = param_value

    # delete schema params
    for param in params:
        if param.get('schema'):
            params.remove(param)

    for schema_param in schema_params:
        params += schema_param

    return params