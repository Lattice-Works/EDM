def make_key_edm(edm):
    '''
    Function to turn the edm from a list of objects into a dictionary
    with the id as key.
    '''
    outedm = {}
    for key in ['associationTypes', 'entityTypes', 'propertyTypes']:
        outedm[key] = {get_id(x, key): x for x in edm[key]}
    outedm['schemas'] = {concat_fqn(x['fqn']):x for x in edm['schemas']}
    return outedm

def get_id(x, key):
    '''
    Helper function to get the id from an object.  Mainly because in
    associationtypes, the id is in the entitytype.
    '''
    if key == 'associationTypes':
        return x['entityType']['id']
    else:
        return x['id']

def concat_fqn(fqn):
    '''
    Helper function to go from fqn ({"namespace": x, "name": y}) to
    it's string version "x.y"
    '''
    return "{namespace}.{name}".format(
        namespace=fqn['namespace'],
        name=fqn['name']
        )
