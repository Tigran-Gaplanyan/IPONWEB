#
import json
import os
import csv

FILENAME = "error_messages.csv"
WRONG_ERROR_CODE = "The code of error message is wrong."


#
def get_error_message(code, param=None):
    with open(os.path.join(os.path.dirname(__file__), FILENAME), "r", encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["CODE"] == code:
                if param:
                    text = "{} : {}".format(row["MESSAGE"], param)
                else:
                    text = row["MESSAGE"]
                return json.dumps(
                    {
                        "status": "error",
                        "error": {
                            "code": row["CODE"],
                            "text": text,
                        },
                    }
                )

    return WRONG_ERROR_CODE
