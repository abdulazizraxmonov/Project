from django.db import models

class Day(models.Model):
    date = models.DateField(unique=True)

    def __str__(self):
        return self.date.strftime('%A, %d %B %Y')

class Speaker(models.Model):
    CATEGORY_CHOICES = [
        ('Organizing Committee', 'Organizing Committee'),
        ('Scientific Committee', 'Scientific Committee'),
        ('Keynote Speaker', 'Keynote Speaker'),
    ]

    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='speakers/', blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    affiliation = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Mahshulot(models.Model):
    name = models.CharField(max_length=100)
    date = models.TimeField()

    def __str__(self):
        return self.name

class Session(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    day = models.ForeignKey(Day, on_delete=models.CASCADE, related_name='sessions')
    speakers = models.ManyToManyField(Speaker, related_name='sessions')
    start_time = models.TimeField()
    end_time = models.TimeField()
    mahshulot_id = models.ManyToManyField(Mahshulot, related_name='sessions')

    def __str__(self):
        return self.title


class Section(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Submission(models.Model):
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100)
    author_email = models.EmailField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Fee(models.Model):
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f"{self.category} - ${self.amount}"



class Author_information(models.Model):
    frist_name_your = models.CharField(max_length=255)
    last_name_your = models.CharField(max_length=255)
    email_your = models.EmailField()
    phone_your = models.CharField(max_length=13)
    affiliation_your = models.CharField(max_length=150)
    country_your = models.CharField(max_length=255)

    frist_name_autor = models.CharField(max_length=255)
    last_name_autor = models.CharField(max_length=255)
    email_autor = models.EmailField()
    phone_autor = models.CharField(max_length=13)
    affiliation_autor = models.CharField(max_length=150)
    country_autor = models.CharField(max_length=255)

    title_paper = models.CharField(max_length=255)
    section_paper = models.CharField(max_length=255)
    keyword_paper = models.IntegerField()
    file_paper = models.FileField()

    def __str__(self):
        return self.frist_name_your




class Sponsor(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='sponsors/logos/')
    website = models.URLField()

    def __str__(self):
        return self.name

class ConferenceInfo(models.Model):
    address = models.TextField()
    contact_email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.address