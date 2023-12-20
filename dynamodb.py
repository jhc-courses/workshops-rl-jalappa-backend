from config import TABLE_NAME

import json
import boto3
from boto3.dynamodb.conditions import Key


boto3.setup_default_session(region_name="ap-south-1")

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(TABLE_NAME)


def add_all_courses():
    with open("courses.json") as fh:
        courses = json.loads(fh.read())

        for course in courses:
            try:
                item = {
                    "pk": "COURSES",
                    "sk": f"COURSE#{course['id']}",
                    **course,
                }

                table.put_item(
                    Item=item, ConditionExpression="attribute_not_exists(id)"
                )
            except:
                continue


def get_all_courses_info():
    response = table.query(
        KeyConditionExpression=Key("pk").eq("COURSES"),
    )
    return response["Items"]


def add_user_rating(course_id, user_rating):
    print("api call")
    key = {
        "pk": "COURSES",
        "sk": f"COURSE#{course_id}",
    }

    response = table.get_item(Key=key)
    record = response["Item"] if "Item" in response else None

    if record:
        record[f"{user_rating}s"] += 1

        likes = record["likes"]
        dislikes = record["dislikes"]
        total_rating = likes * 5 / (likes + dislikes)

        record["total_rating"] = round(total_rating, 1)

        table.put_item(Item=record)

        return {
            "message": "OK",
        }

    else:
        return {
            "message": "Error",
        }
