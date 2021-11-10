from django.db import models

class Noticia(models.Model):

    titulo=models.CharField(max_length=100)
    resumen=models.CharField(max_length=1000)
    palabras_clave=models.CharField(max_length=500)
    autor=models.ForeignKey("Periodista",on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Noticia")
        verbose_name_plural = ("Noticias")

    def __str__(self):
        return self.titulo


        return reverse("Noticia_detail", kwargs={"pk": self.pk})

class Periodista(models.Model):

    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    dni=models.CharField(max_length=8)
    celular=models.CharField(max_length=9)
    direccion=models.CharField(max_length=500)
    correo=models.EmailField(max_length=70)

    class Meta:
        verbose_name = ("Periodista")
        verbose_name_plural = ("Periodistas")

    def __str__(self):
        return self.nombre

