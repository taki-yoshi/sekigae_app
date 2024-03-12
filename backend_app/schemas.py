from pydantic import BaseModel

class Request(BaseModel):
    students:list[dict[str,list[str]]]
    seats_sum: int
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "students": [
                        {
                        "A": [
                            "1","2","3"
                        ],
                        "B": [
                            "2","1","3"
                        ],
                        "C": [
                            "1","2","3"
                        ]
                        }
                    ],
                    "seats_sum": 3
                }
            ]
        }
    }

class Response(BaseModel):
    changed_seats:dict[str,list[str]]