from django.db import models


class Anime(models.Model):
    name = models.CharField(max_length=106)
    description = models.TextField()
    image = models.ImageField(upload_to='anime_images')
    date = models.CharField(max_length=50)
    chapters = models.IntegerField()
    status = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    def delete(self, using=None, keep_parents=False):
        """ Función para eliminar las imagens que vayamos agragando """
        self.image.storage.delete(self.image.name)
        super().delete()
