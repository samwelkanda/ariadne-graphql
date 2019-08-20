# ariadne-graphql
Ariadne is a Schema-first implementation of how to build graphQL API's in python. This repo demonstrates how to build a graphql api for your project using Ariadne as opposed to graphene.

## Quickstart

The following example creates an API defining `Person` type and single query field `people` returning a list of two persons. It also starts a local dev server with [GraphQL Playground](https://github.com/prisma/graphql-playground) available on the `http://127.0.0.1:8000` address.

Start by installing the dependencies [ariadne](https://ariadnegraphql.org) and [uvicorn](http://www.uvicorn.org/), an ASGI server we will use to serve the API:

```console
pipenv install
```

Finally run the server:

```console
uvicorn example:app
```
