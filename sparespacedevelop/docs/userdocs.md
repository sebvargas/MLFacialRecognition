**get all users**: 
returns array of all users
```
.get('localhost:3001/users')
```

**create new user**: 
returns user when successful
```
.post('localhost:3001/users', {
	fullname: 'Devin Roche',
	password: 'fart',
	contact: {
		email: 'foo@email.com',
		phone: '123-456-7890',
	},
	userType: 'host'
})
```

**get a single user**
returns user when successful
```
.get('localhost:3001/user/:id')
```

**edit a user**
when successful, returns json {message: 'user updated', user}
```
.put('localhost:3001/user/:id', {
	any field you want to edit goes here
})
```
**delete a user**
when successful, returns json {user}
```
.put('localhost:3001/user/:id', {
	any field you want to edit goes here
})
```

**login**: 
when successful, sends user
```
.post('localhost:3001/login', {
    "username":"fart",
    "password": "password"
})
```

**clear collection**
only use this when testing!!!
```
.delete('localhost:3001/deleteUsers')
```