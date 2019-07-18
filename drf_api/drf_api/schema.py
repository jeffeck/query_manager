import graphene 

from querymanager.schema import Query as programmer_query 


class Query(programmer_query):
    pass 

schema = graphene.Schema(query=Query)


