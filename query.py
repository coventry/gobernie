import json, xapian
from .config import dbpath, fields

def search(query, numresults=10):
    # XXX There  should be a way  to do this without  going through an
    # intermediate string, and without adding prefixes.
    qstring = ['%s:"%s"' % (field, value) for field, value in query.items()]
    querystring = ' AND '.join(qstring)
    db = xapian.Database(dbpath)
    queryparser = xapian.QueryParser()
    for field, abbrev in fields.items():
        queryparser.add_prefix(field, abbrev)
    print querystring
    query = queryparser.parse_query(querystring, queryparser.FLAG_BOOLEAN)
    enquire = xapian.Enquire(db)
    enquire.set_query(query)
    return [json.loads(r.document.get_data())
            for r in enquire.get_mset(0, numresults)]

