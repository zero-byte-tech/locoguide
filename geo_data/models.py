from django.db import models
from uuid import uuid4
<<<<<<< HEAD
from locoguide.baseModel import BaseModel

# BaseModel class

=======
from locoguide.basemodel import BaseModel
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
>>>>>>> 3a9effa062fd83652cbd8c3efdc1bdb373383faf

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

# Pauroshova Model
class Pauroshova(BaseModel):
    en_name = models.CharField(max_length=100)
    bn_name = models.CharField(max_length=100)
    upazila = models.ForeignKey(Upazila, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.en_name} - {self.bn_name}"
    
# Union Model
class Union(BaseModel):
    en_name = models.CharField(max_length=100)
    bn_name = models.CharField(max_length=100)
    upazila = models.ForeignKey(Upazila, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.en_name} - {self.bn_name}"


# Postal Code Model
class PostalCode(BaseModel):
    code = models.CharField(max_length=10)
    union = models.ForeignKey(Union, on_delete=models.CASCADE)

    def __str__(self):
        return self.code

# Ward Model
class Ward(BaseModel):
    en_name = models.CharField(max_length=100)
    bn_name = models.CharField(max_length=100)
    union = models.ForeignKey(Union, on_delete=models.CASCADE, null=True, blank=True)
    pauroshova = models.ForeignKey(Pauroshova, on_delete=models.CASCADE, null=True, blank=True)

    
    
    def clean(self):
        """
        Validate that exactly one of union or pauroshova is selected
        """
        if self.union and self.pauroshova:
            raise ValidationError("Cannot select both Union and Pauroshova. Please choose only one.")
        
        if not self.union and not self.pauroshova:
            raise ValidationError("Must select either Union or Pauroshova.")

        super().clean()
    def save(self, *args, **kwargs):
        """
        Override save method to ensure validation is called
        """
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.en_name} - {self.bn_name}"
    
# Village Model
class Village(BaseModel):
    en_name = models.CharField(max_length=100)
    bn_name = models.CharField(max_length=100)
<<<<<<< HEAD
    ward = models.ManyToManyField(Ward)
=======
    ward = models.ManyToManyField(Ward )
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

>>>>>>> 3a9effa062fd83652cbd8c3efdc1bdb373383faf

    def __str__(self):
        return f"{self.en_name} - {self.bn_name}"
    
# Area Model
class Area(BaseModel):
    en_name = models.CharField(max_length=100)
    bn_name = models.CharField(max_length=100)
    village = models.ForeignKey(Village, on_delete=models.CASCADE , null=True,blank=True)
    Ward = models.ForeignKey(Ward, on_delete=models.CASCADE, null=True,blank=True)

    def __str__(self):
        return f"{self.en_name} - {self.bn_name}"
    
    def clean(self):
        """
        Validate that at least one location (village or ward) is provided
        """
        if not self.village and not self.ward:
            raise ValidationError(_("Either village or ward (or both) must be provided"))

        # If both are provided, validate their relationship
        if self.village and self.ward:
            if self.village.ward != self.ward:
                raise ValidationError(_("Village must belong to the selected ward"))

        super().clean()

    def save(self, *args, **kwargs):
        """
        Override save method to ensure validation is called
        """
        self.clean()
        super().save(*args, **kwargs)

# Address Model
class Address(BaseModel):
    en_name = models.CharField(max_length=100)
    bn_name = models.CharField(max_length=100)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True, blank=True)
    postal_code = models.ForeignKey(PostalCode, on_delete=models.CASCADE, null=True, blank=True)

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