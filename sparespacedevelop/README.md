# :house: sparespace services :house:

This is the backend repository for [sparespace](https://github.com/devinroche/sparespace). sparespace is a senior project developed by a group of gonzaga students.  

## prerequisites
make sure you have the things installed below.

- [node](https://nodejs.org/en/)

you can also use homebrew!
```brew install node```

## running Stuffs

run me first!
```
npm install
```

### application
```
npm start
```

### test
```
npm run test
```

### linter
```
npm run lint
```

### lint fixer 
fixes *some* linter errors
```
npm run lint-fix
```

## api
[users api](/docs/userdocs.md)
[listings api](/docs/listingdocs.md)

## cool stuff we use
- [travis-ci](https://travis-ci.org/)
- [mocha](https://mochajs.org/)
- [eslint](https://eslint.org/)
- [chai](http://chaijs.com/)
- [nodemailer](https://nodemailer.com/about/)
- [mongoose](http://mongoosejs.com/)

## env
things we have in our .env file include
- db url
- sparespace team email
- email password
- google maps api key