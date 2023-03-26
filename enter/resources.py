from import_export import resources
from.models import *

class MemberResource(resources.ModelResource):
    class Meta:
        model = Post

class Signin(resources.ModelResource):
    class Meta:
        model = MyfutureForm