from ariadne import ObjectType, QueryType, gql, make_executable_schema
from ariadne.asgi import GraphQL
# Wrapping string in gql function provides validation and better error traceback
type_defs = gql("""
    type Query {
        people: [Person!]!

    }

    type Person {
        firstname: String
        lastname: String
        age: Int
        fullname: String
    }
""")

# Map resolver functions to Query fields using QueryType
query = QueryType()

# Resolvers are simple python functions

@query.field("people")
def resolve_people(*_):
    return [
        {"firstname":"Samwel", "lastname":"Kanda", "age":"28"},
        {"firstname":"Sam", "lastname":"Wanekeya", "age":"23"}

    ]

# Map resolver functions to custom type fields using ObjectType
person = ObjectType("Person")

@person.field("fullname")
def resolve_fullname(person, *_):
    return "%s %s" % (person["firstname"], person["lastname"])

# Create executable GraphQL schema
schema = make_executable_schema(type_defs, [query, person])

# Create an ASGI app using the schema, running in debug mode
app = GraphQL(schema, debug=True)
