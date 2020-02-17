from django.db import models
from django_countries.fields import CountryField
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):

    """Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True


class RoomType(AbstractItem):

    """RoomType Model Definition"""

    class Meta:
        verbose_name = "Room Type"

    def __str__(self):
        return self.name

    pass


class Amenity(AbstractItem):

    """Amenity Model Definition"""

    class Meta:
        verbose_name = "Amenities"

    def __str__(self):
        return self.name


class Facility(AbstractItem):

    """Facility Model Definition"""

    class Meta:
        verbose_name = "Facilities"

    def __str__(self):
        return self.name


class HouseRule(AbstractItem):

    """HouseRule Model Definition"""

    def __str__(self):
        return self.name


class Photo(core_models.TimeStampedModel):

    """Photo Model Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedModel):

    """Room Model Definition"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room_type = models.ForeignKey("RoomType", on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField("Amenity")
    facilities = models.ManyToManyField("Facility")
    house_rules = models.ManyToManyField("HouseRule")

    def __str__(self):
        return self.name

