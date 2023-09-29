from SEL4C.models import Gender, Country, User, DiagnosisQuestion, Test, TrainingReagent

"""
print(Gender.objects.all())
print(Country.objects.all())
print(User.objects.all())
"""
print(TrainingReagent.objects.get(identificator = 3).questions)
