import logging

import azure.functions as func
import os
import sys
from sys import path

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir_path)

from get_scores import get_scores

def main(req: func.HttpRequest) -> func.HttpResponse:
    #sheet_id = req.params.get('sheet_id')
    res=get_scores()
    return func.HttpResponse(body=res,mimetype='text/html')
