from django.dispatch import receiver
from django.db.models.signals import post_save

from main.models import Donate 


@receiver(post_save, sender=Donate)
def add_amount(sender, instance, created, **kwargs):
    if created:
        sponsor = instance.sponsor_id
        sponsor.amont_of_money -= instance.amont_of_money
        sponsor.spent_money += instance.amont_of_money
        sponsor.save()

        student = instance.student
        student.student_id += instance.amont_of_money
        student.save()
 