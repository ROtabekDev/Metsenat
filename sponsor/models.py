from django.db import models


class Sponsor(models.Model):
    """Homiy"""

    SPONSOR_TYPE = (
        ('JSH', 'Jismoniy shaxs'),
        ('YSH', 'Yuridik shaxs')
    )

    STATUS = (
        ('NEW', 'Yangi'),
        ('Moderation', 'Moderatsiyada'),
        ('Approved', 'Tasdiqlangan'),
        ('Canceled', 'Bekor qilingan'),
    )

    PAYMENT_TYPE = (
        ('Uzcard', 'Uzcard'),
        ('Humo', 'Humo'),
    )

    full_name = models.CharField('FISH', max_length=100)
    phone_number = models.CharField('Telefon nomer', max_length=15)
    sponsor_type = models.CharField('Homiy turi', choices=SPONSOR_TYPE, max_length=15)
    amont_of_money = models.IntegerField("Homiylik summasi")
    spent_money = models.IntegerField('Sarflangan pul miqdori',  blank=True, null=True )
    payment_type = models.CharField('To`lov turi', choices=PAYMENT_TYPE, max_length=15)
    organization = models.CharField('Kompaiya nomi', max_length=100, blank=True, null=True)
    status = models.CharField('Holati', max_length=20, choices=STATUS, default='NEW')
    created_at = models.DateTimeField('Yaratilgan vaqti', auto_now_add=True)

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = 'Homiy'
        verbose_name_plural = 'Homiylar'
    

