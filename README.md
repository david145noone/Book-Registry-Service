# Book Registry Service

## Technologies Implemented

![Python](https://img.shields.io/badge/Python-3.6-blue)

## Usage

All responses will have the form

```json
{
        "data": "Mixed type holding the content of the response",
        "message": "Description of what happened during the request"
}
```

Subsequent response definitions will only detail the expected value of `data`

### List all devices

**Definition**

`GET /books`

**Response**

- `200 OK` on success

```json
[
        {
                "identifier": "database ID",
                "title": "This is some book",
                "author": "I. Wrote. Somebook",
                "pageCount": 200,
                "ISBN": 9783161484100
        },
        {
                "..."
        }
]
```


### Register a new book

**Definition**

- `POST /devices`

**Arguements**

- `"title": string` the title of the book
- `"author": string` the author of the book
- `"pageCount": int` the number of pages the book has
- `"ISBN": int` the ISBN of the book

If a book with the same title exists already, that book is overwritten and the new book is stored.

**Response**

- `201 Created` on success

```json
{
        "identifier": "database ID",
        "title": "This is some book",
        "author": "I. Wrote. Somebook",
        "pageCount": 200,
        "ISBN": 9783161484100
}
```

### Lookup book details

**Definition**

- `GET /book/<title>`

**Response**

- `404 Not found` if the book does not exist
- `200 OK` on success

```json
{
        "identifier": "database ID",
        "title": "This is some book",
        "author": "I. Wrote. Somebook",
        "pageCount": 200,
        "ISBN": 9783161484100
}
```

### Delete a device

**Definition** 

- `DELETE /book/<title>`

**Response**

- `404 Not found` if the book does not exist
- `204 No content` on success


