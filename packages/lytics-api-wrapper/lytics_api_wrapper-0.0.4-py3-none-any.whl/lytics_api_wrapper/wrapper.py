import requests
import json
from datetime import datetime

class ly:
    def __init__(self, key, aid, env="prod"):
        self.key = key
        if env == "prod":
            self.API = "https://api.lytics.io/"
        elif env == "local":
            self.API = "http://localhost:5353/"
        else:
            self.API = "https://stagingapik8s.lytics.io/"

        r = requests.get(self.API+"api/account/{}".format(aid), params={"key": key})

        if r.status_code != 200:
            raise Exception(
                "failed to create ly object with status code: {}".format(r.text))

        data = json.loads(r.text)
        self.aid = data["data"]["aid"]
        self.name = data["data"]["name"]
        self.account_id = data["data"]["id"]

    def add_params(self, p):
        p['key'] = self.key
        p['account_id'] = self.account_id
        return p

    def __str__(self):
        return "{} (AID {})".format(self.name, self.aid)

    def get(self, path, params={}, headers={}):
        
        return requests.get(self.API+path, params=self.add_params(params), headers=headers)

    def post(self, path, stuff={}, params={}, headers={}):
        params['key'] = self.key
        return requests.post(self.API+path, params=self.add_params(params), data=stuff, headers=headers)

    def delete(self, path, params={}, headers={}):
        params['key'] = self.key
        return requests.delete(self.API+path, params=self.add_params(params), headers=headers)

    def put(self, path, stuff={}, params={}, headers={}):
        params['key'] = self.key
        return requests.put(self.API+path, params=self.add_params(params), headers=headers)

    def scan(self, filter, limit=1000000000, gen=0):
        docs = []
        self.scan_helper(filter, "", docs, 0, limit, gen)
        return docs

    def size(self, filter):
        r = self.post("api/segment/scan", stuff=filter)
        jr = json.loads(r.text)
        return jr['total']

    def scan_helper(self, filter, next, docs, count, cap, gen):
        params = {"limit": 100}
        if len(next) > 0:
            params['next'] = next

        if gen != 0:
            params['generation'] = gen

        r = self.post("api/segment/scan", stuff=filter, params=params)
        jr = json.loads(r.text)
        total = jr['total']
        for e in jr['data']:
            docs.append(e)

        if len(jr['_next']) > 0 and count*100 < min(total, cap):
            self.scan_helper(filter, jr['_next'], docs, count+1, cap, gen)

    def delete_content(self, filter_string):
        config = {
            "workflow_id": "e40a0ad5d0a845ca8549a7d23ede9eed",
            "config": {
                "filter_ql": filter_string,
                "skip_emitting_sentinel": True,
                "gdpr_delete": True,
                "skip_content_filters": True
            }
        }

        r = self.post("api/work", json.dumps(config))
        print(r.text)

    def evaluate_segment(self, filter_string):
        config = {
            "workflow_id": "e40a0ad5d0a845ca8549a7d23ede9eed",
            "config": {
                "filter_ql": filter_string,
                "skip_emitting_sentinel": True,
                "segment_scanner_version": "v2",
            }
        }

        r = self.post("api/work", json.dumps(config))
        print(r.text)

    def rescore_content(self, filter):
        now = datetime.utcnow().isoformat()[:-7]+'Z'

        config = {
            "workflow_id": "23be8d80749b106513e83547e2c8bff1",
            "verbose_logging": True,
            "config": {
                "collection_id": filter,
                "skip_sitemaps": True,
                "enrich_epoch": {
                    "meta": now,
                    "google_nlp": now
                },
                "rescore": True,
            }
        }
        r = self.post("api/work", json.dumps(config))
        j = json.loads(r.text)
        print(j['data']['id'])

    def enrich_content(self, filter, enrichers=["meta", "google_nlp", "diffbot_meta"]):
        now = datetime.utcnow().isoformat()[:-7]+'Z'

        config = {
            "workflow_id": "23be8d80749b106513e83547e2c8bff1",
            "verbose_logging": True,
            "config": {
                "collection_id": filter,
                "skip_sitemaps": True,
                "enrich_epoch": {}
            }
        }

        for e in enrichers:
            config["config"]["enrich_epoch"][e] = now

        print(config)

        #r = self.post("api/work", json.dumps(config))
        #j = json.loads(r.text)
        # print(j['data']['id'])
