from django.db import models
 
from sponsor.models import Sponsor
from student.models import Student
    
 
class Donate(models.Model):
    """Ehson"""
    sponsor_id = models.ForeignKey(Sponsor, on_delete=models.CASCADE, verbose_name="Homiy")
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Talaba")
    amont_of_money = models.IntegerField('Ajratilgan pul miqdori')

    def __str__(self):
        return f"Homiy: {self.sponsor_id.full_name}. \n Talaba: {self.student_id.full_name}. \n Ajratilgan pul miqdori: {self.amont_of_money}. "

    class Meta:
        verbose_name = 'Ehson'
        verbose_name_plural = 'Ehsonlar'


class Petition_for_legal_entity(models.Model):
    """Yuridik shaxs uchun ariza"""
    full_name = models.CharField('FISH', max_length=100)
    phone_number = models.CharField('Telefon nomer', max_length=15) 
    amont_of_money = models.IntegerField("Homiylik summasi") 
    organization = models.IntegerField('Kompaiya nomi', blank=True, null=True) 
    created_at = models.DateTimeField('Yaratilgan vaqti', auto_now_add=True)

    def __str__(self):
        return f" Arizachi: {self.full_name}"
    
    class Meta:
        verbose_name = 'Yuridik shaxs uchun ariza'
        verbose_name_plural = 'Jismoniy shaxs uchun arizalar'
    

class Petition_for_physical_entity(models.Model):
    """Jismoniy shaxs uchun ariza"""
    full_name = models.CharField('FISH', max_length=100)
    phone_number = models.CharField('Telefon nomer', max_length=15) 
    amont_of_money = models.IntegerField("Homiylik summasi")  
    created_at = models.DateTimeField('Yaratilgan vaqti', auto_now_add=True)

    def __str__(self):
        return f"Arizachi: {self.full_name}"
        
    class Meta:
        verbose_name = 'Yuridik shaxs uchun ariza'
        verbose_name_plural = 'Yuridik shaxs uchun arizalar'









    