**Methodology**

First define the MicroService: This will store books.
We can add books and remove books. We can also view a single resource or entire lot.

Then define the endpoints and what requests will be used over those endpoints.



**Endpoints**

- Colllection -> /books : this will return the entire collection of added books
        -- Accept GET request to view all books
        -- Accept POST request to add a new book (new resource) to collection

- Individual resource -> /getBook/<identifier> return the specific book given the id
        -- Accept GET request for single book
        -- Accept DELETE request to remove resource

