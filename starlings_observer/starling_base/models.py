# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
#from starling_base.models import Complex_Traits




class Collection(models.Model):
    date_collected = models.TextField(db_column='DATE_COLLECTED', blank=True, null=True)  # Field name made lowercase.
    arrived_amnh = models.TextField(db_column='Arrived_AMNH', blank=True, null=True)  # Field name made lowercase.
    collector_s_field = models.TextField(db_column='COLLECTOR(S)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    collection_id = models.TextField(db_column='Collection_ID', blank=True, null=False, primary_key=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Collection'

class BasicTraits(models.Model):
    fat = models.TextField(db_column='FAT', blank=True, null=True)  # Field name made lowercase.
    age = models.TextField(db_column='AGE', blank=True, null=True)  # Field name made lowercase.
    sex = models.TextField(db_column='SEX', blank=True, null=True)  # Field name made lowercase.
    basic_traits_id = models.TextField(db_column='Basic_Traits_ID', blank=True, null=False, primary_key=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Basic_Traits'


class ComplexTraits(models.Model):
    weight_g_field = models.DecimalField(db_column='WEIGHT_(g)', blank=True, null=True, max_digits=3, decimal_places=1)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    testes_r = models.TextField(db_column='TESTES_R', blank=True, null=True)  # Field name made lowercase.
    testes_l = models.TextField(db_column='TESTES_L', blank=True, null=True)  # Field name made lowercase.
    ovaries = models.TextField(db_column='OVARIES', blank=True, null=True)  # Field name made lowercase.
    basic_traits_id = models.ForeignKey('Basic_Traits', on_delete=models.CASCADE, blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    complex_traits_id = models.TextField(db_column='Complex_Traits_ID', blank=True, null=False, primary_key=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Complex_Traits'


class Death(models.Model):
    prep = models.TextField(db_column='PREP', blank=True, null=True)  # Field name made lowercase.
    trap = models.TextField(db_column='TRAP', blank=True, null=True)  # Field name made lowercase.
    depredation_method = models.TextField(db_column='DEPREDATION_METHOD', blank=True, null=True)  # Field name made lowercase.
    death_id = models.TextField(db_column='Death_ID', blank=True, null=False, primary_key=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Death'


class Identifiers(models.Model):
    identification = models.TextField(db_column='IDENTIFICATION', blank=True, null=True)  # Field name made lowercase.
    country = models.TextField(db_column='COUNTRY', blank=True, null=True)  # Field name made lowercase.
    identifiers_id = models.TextField(db_column='Identifiers_ID', blank=True, null=False, primary_key=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Identifiers'


class Location(models.Model):
    state = models.TextField(db_column='STATE', blank=True, null=True)  # Field name made lowercase.
    county = models.TextField(db_column='COUNTY', blank=True, null=True)  # Field name made lowercase.
    precise_locality = models.TextField(db_column='PRECISE_LOCALITY', blank=True, null=True)  # Field name made lowercase.
    latitude = models.TextField(db_column='LATITUDE', blank=True, null=True)  # Field name made lowercase.
    longitude = models.TextField(db_column='LONGITUDE', blank=True, null=True)  # Field name made lowercase.
    collection_id = models.ForeignKey(Collection, on_delete=models.CASCADE, blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    identifiers_id = models.ForeignKey(Identifiers, on_delete=models.CASCADE, blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    location_id = models.TextField(db_column='Location_ID', blank=True, null=False, primary_key=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Location'


class PreSkin(models.Model):
    beak_length_mm_pre_skin_field = models.DecimalField(db_column='Beak_length_mm_(Pre-Skin)', blank=True, null=True, max_digits=5, decimal_places=2)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    beak_depth_mm_pre_skin_field = models.DecimalField(db_column='Beak_depth_mm_(Pre-skin)', blank=True, null=True, max_digits=5, decimal_places=2)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    head_length_mm_pre_skin_field = models.DecimalField(db_column='Head_length_mm_(Pre-Skin)', blank=True, null=True, max_digits=5, decimal_places=2)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    wing_length_mm_pre_skin_field = models.DecimalField(db_column='Wing_length_mm_(Pre-Skin)', blank=True, null=True, max_digits=5, decimal_places=2)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    tail_length_mm_pre_skin_field = models.DecimalField(db_column='Tail_length_mm_(Pre-Skin)', blank=True, null=True, max_digits=5, decimal_places=2)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    tarsus_length_mm_pre_skin_field = models.DecimalField(db_column='Tarsus_length_mm_(Pre-Skin)', blank=True, null=True, max_digits=5, decimal_places=2)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    notes_pre_skin_field = models.TextField(db_column='Notes_(Pre-Skin)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    pre_skin_id = models.TextField(db_column='Pre_Skin_ID', blank=True, null=False, primary_key=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Pre_Skin'


class Preparation(models.Model):
    specimen_prep = models.TextField(db_column='SPECIMEN_PREP', blank=True, null=True)  # Field name made lowercase.
    preparator = models.TextField(db_column='PREPARATOR', blank=True, null=True)  # Field name made lowercase.
    death_id = models.ForeignKey(Death, on_delete=models.CASCADE, blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    preparation_id = models.TextField(db_column='Preparation_ID', blank=True, null=False, primary_key=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Preparation'


class Skin(models.Model):
    beak_length_mm_skin_field = models.DecimalField(db_column='Beak_length_mm_(Skin)', blank=True, null=True, max_digits=5, decimal_places=2)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    beak_depth_mm_skin_field = models.DecimalField(db_column='Beak_depth_mm_(Skin)', blank=True, null=True, max_digits=5, decimal_places=2)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    head_length_mm_skin_field = models.DecimalField(db_column='Head_length_mm_(Skin)', blank=True, null=True, max_digits=5, decimal_places=2)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    wing_length_mm_skin_field = models.DecimalField(db_column='Wing_length_mm_(Skin)', blank=True, null=True, max_digits=5, decimal_places=2)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    tail_length_mm_skin_field = models.DecimalField(db_column='Tail_length_mm_(Skin)', blank=True, null=True, max_digits=5, decimal_places=2)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    tarsus_length_mm_skin_field = models.DecimalField(db_column='Tarsus_length_mm_(Skin)', blank=True, null=True, max_digits=5, decimal_places=2)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    notes_skin_field = models.TextField(db_column='Notes_(Skin)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    skin_id = models.TextField(db_column='Skin_ID', blank=True, null=False, primary_key=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Skin'


class BirdInfo(models.Model):
    number = models.TextField(db_column='NUMBER', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    complex_traits_id = models.ForeignKey('Complex_Traits', on_delete=models.CASCADE, blank=True, null=True,)  # Field name made lowercase. This field type is a guess.
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    preparation_id = models.ForeignKey(Preparation, on_delete=models.CASCADE, blank=True, null=True)  # This field type is a guess.
    pre_skin_id = models.ForeignKey('Pre_Skin', on_delete=models.CASCADE, blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    skin_id = models.ForeignKey(Skin, on_delete=models.CASCADE, blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Bird_Info'


