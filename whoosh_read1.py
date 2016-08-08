from whoosh.qparser import MultifieldParser
from whoosh.index import open_dir
import json

results = ""
ix = open_dir("indexdir")
with ix.searcher() as searcher:
    query = MultifieldParser(["title","author","secondauthor"], ix.schema).parse("Dr.")
    results = searcher.search(query, limit=5)
    print len(results)
    result_dict = {}
    for result in results:
        result_dict[result['path']] = [result['title'],result['author'],result['publication']]
        print "/static/imgs/publications/" + result['publication'] + "/" + result['path'].split("/")[-1] + ".jpg"

    print json.dumps(result_dict)
