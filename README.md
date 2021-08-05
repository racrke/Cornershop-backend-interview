
## Menu creation with dishes

POST /api/menu

```json
{
    "dishes":[
        {"name":"Pizza"},
        {"name":"Pollo"}
    ]
}
```

Response:
```json
{
    "result": "success"
}
```
## See Menu contents

GET /api/menu/:uuid

Response Example

```json
[
    {
        "model": "norasystem.dish",
        "pk": 1,
        "fields": {
            "name": "Pizza",
            "menu": "3d3c69a3-a5ab-496b-a9b2-2bde79a8f956"
        }
    },
    {
        "model": "norasystem.dish",
        "pk": 2,
        "fields": {
            "name": "Pollo",
            "menu": "3d3c69a3-a5ab-496b-a9b2-2bde79a8f956"
        }
    }
]
```
## Employee creation

POST /api/employee

```json
{
    "full_name" : "Maria Juana",
    "slack_id" : "DHBEJCK",
    "phone_number" : 811005083
}
```
## See current buyers with dishes and specifications

GET /api/report:uuid Response example

```json
[
    {
        "request__employee__full_name": "Maria Juana",
        "dish__menu__uuid": "3d3c69a3-a5ab-496b-a9b2-2bde79a8f956",
        "dish__name": "Pollo",
        "notes": "normal"
    },
    ...
]
```
## Request a dish

POST /api/request
```json
{
    "dish_id": 2,
    "notes": "normal",
    "phone_number": 811005083
}
```

Postman Link https://www.getpostman.com/collections/dd40b401da16626d798d
