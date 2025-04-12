from django.db import models
from django.core.validators import MinLengthValidator


class PlantType(models.Model):
    '''
    Stored a plant type name for statistical analysis
    
    (Plant's latin name or any descriptive name)
    Examples: Dendrobium Nobile, Cactus with small yellow flower
    '''
    name = models.CharField(
        max_length=128,
        validators=[ 
            MinLengthValidator(4, "Name should contain more, than 4 characters."),
        ]
        )
    
    def __str__(self):
        return self.name
    
class Location(models.Model):
    """
    Represents a location, where plants can be.
    """
    name = models.CharField(
        max_length=128,
        validators=[ 
            MinLengthValidator(4, "Name should contain more, than 4 characters."),
        ]
        )

    def __str__(self):
        return self.name
    
class Plant(models.Model):
    '''
    Stores an instance of a plant in the plant database
    '''
    name = models.CharField(max_length=64)
    plant_type = models.ForeignKey(PlantType, on_delete=models.CASCADE)
    # location = models.ForeignKey(Location, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    

class PlantEvent(models.Model):
    '''
    Stores an event in the plant's timeline.
    TODO: handle differently events with a duration (like flowering)
    '''
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=1000)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} (UNDEFINED)"
    
class DurationPlantEvent(PlantEvent):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
            return f"{self.title} ({self.start_date} - {self.end_date})"
    
class StaticPlantEvent(PlantEvent):
    date = models.DateTimeField()

    def __str__(self):
            return f"{self.title} ({self.date})"