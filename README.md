pipedrive-api
=============

A minimalistic Python library for interacting with the pipedrive.com API (https://developers.pipedrive.com/v1)
This is written for very specific use, however it should cover all endpoints and methods.

Note: Heavily inspired by https://github.com/jscott1989/python-pipedrive, however this library depends on python-requests library.

### Usage:

```
from pipedrive import Pipedrive
pd = Pipedrive(API_TOKEN)
```

### Examples:

#### Get all Persons
```
print pd.persons.get()
```

#### Create a Person and then attach it to a newly created Deal.
```
person = pd.persons.post(data={'name':'John Doe', 
						       'email':'john@example.com'})

person_id = person['id']
deal = api.deals.post(data={'person_id':person_id, 
				 	        'title':'Example'})
```

#### Delete a Person
```
pd.persons.delete(id=3426)
```
