Pipedrive-api
=============

A minimalistic Python library for interacting with the Pipedrive.com API (https://developers.Pipedrive.com/v1)
This is written for very specific use, however it should cover all endpoints and methods.

Note: Heavily inspired by https://github.com/jscott1989/python-Pipedrive, however this library depends on python-requests library.

### Usage:

```
from Pipedrive import Pipedrive
pd = Pipedrive(API_TOKEN)
```

### Examples:

#### Get all Persons
```
person = pd.persons.get()
print person.name 
print person.email
```

You can get raw JSON with `person.data`

#### Create a Person and then attach it to a newly created Deal.
```
person = pd.persons.post(data={'name':'John Doe', 
						       'email':'john@example.com'})
person_id = person.id
deal = api.deals.post(data={'person_id':person_id, 
				 	        'title':'Example'})
```

#### Delete a Person
```
pd.persons.delete(id=3426)
```
