# restedorm

I needed a way to map a rest-api in a project I'm working on, I like the orm way and wanted to give it a try

## Usage

The way to use restedorm is just as straight forward as defining a model:

    from restedorm.abstract_base import RestObject
    from restedorm.decorators import Endpoint
    
    @Endpoint('users')
    class User(RestObject):
        id = int()
        name = str()
        bio = str()
        twitter = str()
        linkedin = str()
        state = str()
        last_login = datetime
        skype = str()
        email = str()
        website_url = str()
        date_joined = datetime

And then start querying it (bare in mind that the api needs to be able to handle filter and so on for this to work):

    user = User.objects.get(id=1)
    users = User.objects.filter()