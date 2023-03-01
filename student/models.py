from django.db import models


class University(models.Model):
    name = models.CharField('Nomi', max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Universitet'
        verbose_name_plural = 'Universitetlar'

class Student(models.Model):
    """Talaba"""

    DEGREE = (
        ('Bakalavr', 'Bakalavr'),
        ('Magistr', 'Magistr'),
    )

    full_name = models.CharField('FISH', max_length=150)
    phone_number = models.CharField('Telefon nomer', max_length=20)
    university_id = models.ForeignKey(University, on_delete=models.CASCADE)
    degree = models.CharField('Darajasi', choices=DEGREE, max_length=15)
    contract = models.IntegerField('Kontrakti')
    amont_of_money = models.IntegerField('Ajratilgan pul miqdori', blank=True, null=True, default=0)


    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = 'Talaba'
        verbose_name_plural = 'Talabalar'
