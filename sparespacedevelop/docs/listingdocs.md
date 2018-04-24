**get all listings**: 
returns an array of all listings
```
.get('localhost:3001/listings')
```

**post a new listing**: 
this wil return the listing when successful.
```
.post('localhost:3001/listings', {
    _host: logged in users id,
    title: 'My super sexy space!!',
    duration: '10 Weeks',
    description: 'this space is the best! you want this!',
    images[
        "image 1",
        "image 2",
        "image 3",
        "image 4"
    ]
})
```

**populate hostid with host info for view specific listing**: 
```
.get('localhost:3001/listing/:listing_id')
```

**clear collection**
only use this when testing!!!
```
.delete('localhost:3001/deleteListings')
```