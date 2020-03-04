import json
from typing import Optional

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ParseError

from paint.apps.batch.types import V1BatchParameters
from paint.util.api import get_query_param
from paint.util.solver.solver import solver

### API v1 ##############################################

class BatchV1(APIView):
    """Implements v1 of the batch API
    
    This exists for backwards-compatibility
    """

    def get(self, request: Request) -> Response:
        """Generate a response using the solver lib"""
        input_raw: Optional[str] = get_query_param(request, 'input')
        if not input_raw:
            raise ParseError(f"Query parameter 'input' is missing")
        batch_parameters: V1BatchParameters = json.loads(input_raw)

        batch_result: str = solver(batch_parameters)

        return Response(batch_result)
        
