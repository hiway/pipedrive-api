pipedrive-api
=============

A minimalistic Python library for interacting with the pipedrive.com API

This is written for very specific use, however it should cover all endpoints and methods.

### Usage:

```
from pipedrive import Pipedrive
pd = Pipedrive(API_TOKEN)
```

### Examples:

#### Get all Persons
```
print pd.persons()
```

#### Create a Person and then attach it to a newly created Deal.
```
person = pd.persons(method='post', 
					data={'name':'John Doe', 
						  'email':'john@example.com'})

person_id = person['data']['id']
deal = api.deals(method='post', 
				 data={'person_id':person_id, 
				 'title':'Example'})
```

#### Delete a Person
```
pd.persons(method='delete', id=3426)
```
