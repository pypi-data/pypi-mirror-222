[![PyPI version](https://img.shields.io/pypi/v/SqlalchemyMixin.svg)](https://pypi.python.org/pypi/SqlalchemyMixin)
# SQLAlchemy Mixin

A pack of framework-agnostic, easy-to-integrate for SQLAlchemy ORM.

Heavily inspired by [Django ORM](https://docs.djangoproject.com/en/1.10/topics/db/queries/)
and [Eloquent ORM](https://laravel.com/docs/5.4/eloquent)

easy integration to your existing project like [FastApi](https://fastapi.tiangolo.com):
```python
from sqlalchemy_mixins import BaseMixin

class User(Base, BaseMixin):
     pass
```

## Table of Contents

1. [Installation](#installation)
1. [Quick Start](#quick-start)
    1. [Framework-agnostic](#framework-agnostic)
    1. [Usage with Flask-SQLAlchemy](#usage-with-flask-sqlalchemy)
1. [Features](#features)
    1. [Active Record](#active-record)
        1. [CRUD](#crud)
        1. [Querying](#querying)
    1. [Eager Load](#eager-load)
    1. [Django-like queries](#django-like-queries)
        1. [Filter and sort by relations](#filter-and-sort-by-relations)
        1. [Automatic eager load relations](#automatic-eager-load-relations)
    1. [All-in-one: smart_query](#all-in-one-smart_query)
    1. [Beauty \_\_repr\_\_](#beauty-__repr__)
    1. [DateMixin](#timestamps)

## Installation

Use pip
```
pip install SqlalchemyMixin
```

## Quick Start

### Framework-agnostic
Here's a quick demo of what our mixins can do.

```python
bob = User.create(name='Bob')
post1 = Post.create(body='Post 1', user=bob, rating=3)
post2 = Post.create(body='long-long-long-long-long body', rating=2,
                    user=User.create(name='Bill'),
                    comments=[Comment.create(body='cool!', user=bob)])

# filter using operators like 'in' and 'contains' and relations like 'user'
# will output this beauty: <Post #1 body:'Post1' user:'Bill'>
print(Post.where(rating__in=[2, 3, 4], user___name__like='%Bi%').all())
# joinedload post and user
print(Comment.with_joined('user', 'post', 'post.comments').first())
# subqueryload posts and their comments
print(User.with_subquery('posts', 'posts.comments').first())
# sort by rating DESC, user name ASC
print(Post.sort('-rating', 'user___name').all())
# created_at, updated_at timestamps added automatically
print("Created Bob at ", bob.created_at)   
# serialize to dict, with relationships
```



### Usage with Flask-SQLAlchemy

```python
import sqlalchemy as sa
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_mixins import BaseMixin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
db = SQLAlchemy(app)

######### Models ######### 
class BaseModel(db.Model, BaseMixin):
    __abstract__ = True
    pass


class User(BaseModel):
    name = sa.Column(sa.String)

######## Initialize ########
BaseModel.set_session(db.session)

######## Create test entity ########
db.create_all()
user = User.create(name='bob')
print(user)
```

# *** Autocommit ***
This library relies on SQLAlchemy's `autocommit` flag. It needs to be set to True when initializing the session i.e:
```python
session = scoped_session(sessionmaker(bind=engine, autocommit=True))
BaseModel.set_session(session)
```
or with `Flask-SQLAlchemy`
```python
db = SQLAlchemy(app, session_options={'autocommit': True})
```

# Features

Main features are
 * [Active Record](#active-record)
 * [Eager Load](#eager-load)
 * [Django-like queries](#django-like-queries)
 * [Beauty \_\_repr\_\_](#beauty-__repr__)
 * [Timestamps](#timestamps)

## Active Record
provided by [`ActiveRecordMixin`](sqlalchemy_mixins/active_record.py)

SQLAlchemy's [Data Mapper](https://en.wikipedia.org/wiki/Data_mapper_pattern)
pattern is cool, but
[Active Record](https://en.wikipedia.org/wiki/Active_record_pattern)
pattern is easiest and more [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself).

Well, we implemented it on top of Data Mapper!
All we need is to just inject [session](http://docs.sqlalchemy.org/en/latest/orm/session.html) into ORM class while bootstrapping our app:

```python
BaseModel.set_session(session)
# now we have access to BaseOrmModel.session property
```

### CRUD
We all love SQLAlchemy, but doing [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)
is a bit tricky there.

For example, creating an object needs 3 lines of code:
```python
bob = User(name='Bobby', age=1)
session.add(bob)
session.flush()
```

Well, having access to session from model, we can just write
```python
bob = User.create(name='Bobby', age=1)
```
that's how it's done in [Django ORM](https://docs.djangoproject.com/en/1.10/ref/models/querysets/#create)
and [Peewee](http://docs.peewee-orm.com/en/latest/peewee/querying.html#creating-a-new-record)

update and delete methods are provided as well
```python
bob.update(name='Bob', age=21)
bob.delete()
```

And, as in [Django](https://docs.djangoproject.com/en/1.10/topics/db/queries/#retrieving-a-single-object-with-get)
and [Eloquent](https://laravel.com/docs/5.4/eloquent#retrieving-single-models),
we can quickly retrieve object by id
```python
User.get(1) # instead of session.query(User).get(1)
```

and fail if such id doesn't exist
```python
User.get_or_abort(123987) # will raise sqlalchemy_mixins.ModelNotFoundError
```


### Querying
As in [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.1/queries/#querying-records),
[Peewee](http://docs.peewee-orm.com/en/latest/peewee/api.html#Model.select)
and [Django ORM](https://docs.djangoproject.com/en/1.10/topics/db/queries/#retrieving-objects),
you can quickly query some class
```python
User.query # instead of session.query(User)
```

Also we can quickly retrieve first or all objects:
```python
User.first() # instead of session.query(User).first()
User.all() # instead of session.query(User).all()
```

## Eager load
provided by [`EagerLoadMixin`](sqlalchemy_mixins/eager_load.py)

### Nested eager load
If you use SQLAlchemy's [eager loading](http://docs.sqlalchemy.org/en/latest/orm/tutorial.html#eager-loading),
you may find it not very convenient, especially when we want, say,
load user, all his posts and comments to every his post in the same query.

Well, now you can easily set what ORM relations you want to eager load
```python
User.with_({
    'posts': {
        'comments': {
            'user': JOINED
        }
    }
}).all()
```

or we can write class properties instead of strings:
```python
User.with_({
    User.posts: {
        Post.comments: {
            Comment.user: JOINED
        }
    }
}).all()
```

### Subquery load
Sometimes we want to load relations in separate query, i.e. do [subqueryload](http://docs.sqlalchemy.org/en/latest/orm/loading_relationships.html#sqlalchemy.orm.subqueryload).
For example, we load posts on page like [this](http://www.qopy.me/3V4Tsu_GTpCMJySzvVH1QQ),
and for each post we want to have user and all comments (and comment authors).

To speed up query, we load comments in separate query, but, in this separate query, join user
```python
from sqlalchemy_mixins import JOINED, SUBQUERY
Post.with_({
    'user': JOINED, # joinedload user
    'comments': (SUBQUERY, {  # load comments in separate query
        'user': JOINED  # but, in this separate query, join user
    })
}).all()
```

Here, posts will be loaded on first query, and comments with users - in second one.
See [SQLAlchemy docs](http://docs.sqlalchemy.org/en/latest/orm/loading_relationships.html)
for explaining relationship loading techniques.

### Quick eager load
For simple cases, when you want to just 
[joinedload](http://docs.sqlalchemy.org/en/latest/orm/loading_relationships.html#sqlalchemy.orm.joinedload)
or [subqueryload](http://docs.sqlalchemy.org/en/latest/orm/loading_relationships.html#sqlalchemy.orm.subqueryload) 
a few relations, we have easier syntax for you:

```python
Comment.with_joined('user', 'post', 'post.comments').first()
User.with_subquery('posts', 'posts.comments').all()
```

> Note that you can split relations with dot like `post.comments`
> due to [this SQLAlchemy feature](http://docs.sqlalchemy.org/en/latest/orm/loading_relationships.html#sqlalchemy.orm.subqueryload_all)


## Filter and sort by relations
provided by [`SmartQueryMixin`](sqlalchemy_mixins/smart_query.py)

### Django-like queries
We implement Django-like
[field lookups](https://docs.djangoproject.com/en/1.10/topics/db/queries/#field-lookups)
and
[automatic relation joins](https://docs.djangoproject.com/en/1.10/topics/db/queries/#lookups-that-span-relationships).

It means you can **filter and sort dynamically by attributes defined in strings!**

So, having defined `Post` model with `Post.user` relationship to `User` model,
you can write
```python
Post.where(rating__gt=2, user___name__like='%Bi%').all() # post rating > 2 and post user name like ...
Post.sort('-rating', 'user___name').all() # sort by rating DESC, user name ASC
```
(`___` splits relation and attribute, `__` splits attribute and operator)

> If you need more flexibility, you can use low-level `filter_expr` method `session.query(Post).filter(*Post.filter_expr(rating__gt=2, body='text'))`, [see example](examples/smartquery.py#L232).
>
> It's like [`filter_by` in SQLALchemy](http://docs.sqlalchemy.org/en/latest/orm/query.html#sqlalchemy.orm.query.Query.filter_by), but also allows magic operators like `rating__gt`.
>
> Note: `filter_expr` method is very low-level and does NOT do magic Django-like joins. Use [`smart_query`](#all-in-one-smart_query) for that.

> **All relations used in filtering/sorting should be _explicitly set_, not just being a backref**
>
> In our example, `Post.user` relationship should be defined in `Post` class even if `User.posts` is defined too.
>
> So, you can't type
> ```python
> class User(BaseModel):
>     # ...
>     user = sa.orm.relationship('User', backref='posts')
> ```
> and skip defining `Post.user` relationship. You must define it anyway:
>
> ```python
> class Post(BaseModel):
>     # ...
>     user = sa.orm.relationship('User') # define it anyway
> ```

For DRY-ifying your code and incapsulating business logic, you can use
SQLAlchemy's [hybrid attributes](http://docs.sqlalchemy.org/en/latest/orm/extensions/hybrid.html)
and [hybrid_methods](http://docs.sqlalchemy.org/en/latest/orm/extensions/hybrid.html?highlight=hybrid_method#sqlalchemy.ext.hybrid.hybrid_method).
Using them in our filtering/sorting is straightforward (see examples and tests).

### Automatic eager load relations
Well, as [`SmartQueryMixin`](sqlalchemy_mixins/smart_query.py) does auto-joins for filtering/sorting,
there's a sense to tell sqlalchemy that we already joined that relation.

So that relations are automatically set to be joinedload if they were used for filtering/sorting.


So, if we write
```python
comments = Comment.where(post___public=True, post___user___name__like='Bi%').all()
```
then no additional query will be executed if we will access used relations
```python
comments[0].post
comments[0].post.user
```

### All-in-one: smart_query
#### Filter, sort and eager load in one smartest method.
provided by [`SmartQueryMixin`](sqlalchemy_mixins/smart_query.py)

In real world, we want to filter, sort and also eager load some relations at once.
Well, if we use the same, say, `User.posts` relation in filtering and sorting,
it **should not be joined twice**.

That's why we combined filter, sort and eager load in one smartest method:
```python
Comment.smart_query(
    filters={
        'post___public': True,
        'user__isnull': False
    },
    sort_attrs=['user___name', '-created_at'],
    schema={
        'post': {
            'user': JOINED
        }
    }).all()
```



As developers, we need to debug things with convenience.
When we play in REPL, we can see this

```
>>> session.query(Post).all()
[<myapp.models.Post object at 0x04287A50>, <myapp.models.Post object at 0x04287A90>]
```

Well, using our mixin, we can have more readable output with post IDs:

```
>>> session.query(Post).all()
[<Post #11>, <Post #12>]
```

Even more, in `Post` model, we can define what else (except id) we want to see:

```python
class User(BaseModel):
    __repr_attrs__ = ['name']
    # ...


class Post(BaseModel):
    __repr_attrs__ = ['user', 'body'] # body is just column, user is relationship
    # ...

```

Now we have
```
>>> session.query(Post).all()
[<Post #11 user:<User #1 'Bill'> body:'post 11'>,
 <Post #12 user:<User #2 'Bob'> body:'post 12'>]

```

And you can customize max `__repr__` length:
```
class Post(BaseModel):
    # ...
    __repr_max_length__ = 25
    # ...
    
>>> long_post
<Post #2 body:'Post 2 long-long body' user:<User #1 'Bob'>>   
```



## DateMixin
provided by [`DateMixin`](sqlalchemy_mixins/date_mixin.py)

You can view the created and updated timestamps.

```python
bob = User(name="Bob")
session.add(bob)
session.flush()

print("Created Bob:    ", bob.created_at)
# Created Bob:     2019-03-04 03:53:53.606765

print("Pre-update Bob: ", bob.updated_at)
# Pre-update Bob:  2019-03-04 03:53:53.606769

time.sleep(2)

bob.name = "Robert"
session.commit()

print("Updated Bob:    ", bob.updated_at)
# Updated Bob:     2019-03-04 03:53:58.613044
```