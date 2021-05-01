from rest_framework.exceptions import APIException


class HttpRes(object):
    def __init__(self, user=None, **args):
        self.response = {
            'status': args.get('status', True),
            'error': args.get('error', []),
            'data': args.get('data', []),
            'message': args.get('message', 'Operation was Successful')
        }
