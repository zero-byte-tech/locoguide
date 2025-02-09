from django.db import models
from uuid import uuid4


# BaseModel class
class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Country geo code model
class Country(BaseModel):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.name

# Division Model
class Division(BaseModel):
    en_name = models.CharField(max_length=100)
    bn_name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.en_name} - {self.bn_name}"
    

# District Model
class District(BaseModel):
    en_name = models.CharField(max_length=100)
    bn_name = models.CharField(max_length=100)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.en_name} - {self.bn_name}"

# Upazila Model
class Upazila(BaseModel):
    en_name = models.CharField(max_length=100)
    bn_name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.en_name} - {self.bn_name}"
    
# Union Model
class Union(BaseModel):
    en_name = models.CharField(max_length=100)
    bn_name = models.CharField(max_length=100)
    upazila = models.ForeignKey(Upazila, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.en_name} - {self.bn_name}"

# Ward Model
class Ward(BaseModel):
    en_name = models.CharField(max_length=100)
    bn_name = models.CharField(max_length=100)
    union = models.ForeignKey(Union, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.en_name} - {self.bn_name}"

# Village Model
class Village(BaseModel):
    en_name = models.CharField(max_length=100)
    bn_name = models.CharField(max_length=100)
    ward = models.ManyToManyField(Ward, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.en_name} - {self.bn_name}"

# Post Office Model
class PostOffice(BaseModel):
    en_name = models.CharField(max_length=100)
    bn_name = models.CharField(max_length=100)
    village = models.ForeignKey(Village, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.en_name} - {self.bn_name}"

# Police Station Model
class PoliceStation(BaseModel):
    en_name = models.CharField(max_length=100)
    bn_name = models.CharField(max_length=100)
    upazila = models.ForeignKey(Upazila, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.en_name} - {self.bn_name}"


# Location Type Model
class LocationType(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name