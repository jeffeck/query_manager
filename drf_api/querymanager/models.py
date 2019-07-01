from django.db import models

class Programmer(models.Model): 
    """
    Model for programmers / authors of queries
    """
    def __str__(self):
        return str(self.programmer_id) + ": " + self.name

    programmer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


class Query(models.Model): 
    """
    Model for SQL Queries
    """
    class Meta:
        verbose_name_plural = "Queries"

    def __str__(self):
        return str(self.query_id) + ": " + self.name

    query_id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100)
    query = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Programmer, null=True, on_delete=models.PROTECT)

    updated_at = models.DateTimeField(auto_now=True)
    


