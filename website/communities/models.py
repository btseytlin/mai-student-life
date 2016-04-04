from django.db import models
COMMUNITY_TYPES = (
    ('reg','Regular'),
    ('hon', 'Honorary')
)

class Community(models.Model):
    created_date = models.DateTimeField(auto_now_add=True) 
    title = models.CharField(max_length=250, default="") 
    description = models.TextField(max_length=500, default="")
    vk_link = models.CharField(max_length=100, default="")
    contacts = models.TextField(max_length=300, default="")
    community_type = models.CharField(max_length=3, default='reg', choices=COMMUNITY_TYPES)