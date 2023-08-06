from ..util.result_utils import error_handler,two_ret_error_handler
from rest_api_client.lib import (
    RestAPI,
    Endpoint,
    HTTPMethod,
    MissingMethodName,
    BearerHeaderToken,
)

class VoteDelegationTemplateService(object):
    def __init__(self):
        None

    def set_api_client(self, server_url, client):
        self._api = RestAPI(api_url=server_url+"/vote/template" ,driver=client)
        endpoints = [
            Endpoint(name="address",path="/get_address",method=HTTPMethod.POST),
            Endpoint(name="getResults",path="/get_results",method=HTTPMethod.POST),
            Endpoint(name="canPay",path="/can_pay",method=HTTPMethod.POST),
            Endpoint(name="getPayees",path="/get_payees",method=HTTPMethod.POST),
            Endpoint(name="getRatioByPayee",path="/get_ratioByPayee",method=HTTPMethod.POST),
            Endpoint(name="init",path="/estimate_init_forReceipt",method=HTTPMethod.POST),
            Endpoint(name="transfer",path="/estimate_transfer_forReceipt",method=HTTPMethod.POST),
            Endpoint(name="delegate",path="/estimate_delegate_forReceipt",method=HTTPMethod.POST),
            Endpoint(name="vote",path="/prepare_vote_forVote",method=HTTPMethod.POST),
            Endpoint(name="start",path="/prepare_start_forState",method=HTTPMethod.POST),
            Endpoint(name="end",path="/prepare_end_forState",method=HTTPMethod.POST),
            Endpoint(name="tryForReceipt",path="/try_forReceipt",method=HTTPMethod.POST),
            Endpoint(name="tryForVote",path="/try_forVote",method=HTTPMethod.POST),
            Endpoint(name="tryForState",path="/try_forState",method=HTTPMethod.POST),
        ]
        self._api.register_endpoints(endpoints)

    @error_handler
    def address(self, service_name):
        res = self._api.call_endpoint("address",data=
            {
                'name': service_name
            })
        return res['data']

    @error_handler
    def get_results(self, service_name, _instanceId, _hash):
        res = self._api.call_endpoint("getResults",data=
            {
                'name': service_name,
                'instanceId': _instanceId
            })
        return res['data']

    @error_handler
    def can_pay(self, service_name, _instanceId, _payerAddress):
        res = self._api.call_endpoint("canPay",data=
            {
                'name': service_name,
                'instanceId': _instanceId,
                'payerAddress': _payerAddress
            })
        return res['data']

    @error_handler
    def get_payees(self, service_name, _instanceId):
        res = self._api.call_endpoint("getPayees",data=
            {
                'name': service_name, 
                'instanceId': _instanceId
            })
        return res['data']

    @error_handler
    def get_ratio_by_payee(self, service_name, _instanceId, _payee):
        res = self._api.call_endpoint("getRatioByPayee",data=
            {
                'name': service_name,
                'instanceId': _instanceId, 
                'payee': _payee
            })
        return res['data']

    @two_ret_error_handler
    def init(self, service_name, pub, sign_func,  _instanceId,_voters,_proposals):
        res = self._api.call_endpoint("init",data=
            {
                'name': service_name, 
                'instanceId': _instanceId, 
                'voters': _voters, 
                'proposals': _proposals, 
                'sender': pub
            })
        tx = res['data']['transaction']

        raw = sign_func(pub, tx)
        result = self._api.call_endpoint("tryForReceipt",data={'name': service_name, 'tx': raw})
        return result['data']['code'],result['data']['receipt']

    @error_handler
    def start(self, service_name, pub, sign_func,  _instanceId):
        res = self._api.call_endpoint("start",data=
            {
                'name': service_name, 
                'instanceId': _instanceId, 
                'sender': pub
            })
        tx = res['data']['transaction']

        raw = sign_func(pub, tx)
        result = self._api.call_endpoint("tryForState",data={'name': service_name, 'tx': raw})
        res = result['data']['res']
        return res


    @error_handler
    def end(self, service_name, pub, sign_func,  _instanceId):
        res = self._api.call_endpoint("end",data=
            {
                'name': service_name, 
                'instanceId': _instanceId, 
                'sender': pub
            })
        tx = res['data']['transaction']

        raw = sign_func(pub, tx)
        result = self._api.call_endpoint("tryForState",data={'name': service_name, 'tx': raw})
        res = result['data']['res']
        return res

    @error_handler
    def delegation(self, service_name, pub, sign_func,  _instanceId,_to):
        res = self._api.call_endpoint("transfer",data=
            {
                'name': service_name, 
                'instanceId': _instanceId, 
                'to': _to,
                'sender': pub
            })
        tx = res['data']['transaction']

        raw = sign_func(pub, tx)
        result = self._api.call_endpoint("tryForReceipt",data={'name': service_name, 'tx': raw})
        return result['data']['code'],result['data']['receipt']

    @error_handler
    def transfer(self, service_name, pub, sign_func,  _instanceId,_to):
        res = self._api.call_endpoint("transfer",data=
            {
                'name': service_name, 
                'instanceId': _instanceId, 
                'to': _to,
                'sender': pub
            })
        tx = res['data']['transaction']

        raw = sign_func(pub, tx)
        result = self._api.call_endpoint("tryForReceipt",data={'name': service_name, 'tx': raw})
        return result['data']['code'],result['data']['receipt']


    @error_handler
    def vote(self, service_name, pub, sign_func,  _instanceId,_proposal):
        res = self._api.call_endpoint("vote",data=
            {
                'name': service_name, 
                'instanceId': _instanceId, 
                'proposal': _proposal,
                'sender': pub
            })
        tx = res['data']['transaction']

        raw = sign_func(pub, tx)
        result = self._api.call_endpoint("tryForVote",data={'name': service_name, 'tx': raw})
        res = result['data']['res']
        return res

