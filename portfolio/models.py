from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200,verbose_name="Título")
    description =models.TextField(verbose_name="Descripción"    )
    image = models.ImageField(verbose_name="Imagen", upload_to="projects/")
    url = models.URLField(verbose_name="URL del proyecto", blank=True, null=True)
    github = models.URLField(verbose_name="URL del repositorio en GitHub", blank=True, null=True)
    created =models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated =models.DateTimeField(auto_now=True,verbose_name="Fecha de actualización")
    
    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ["-created"]
    
    def __str__(self):
        return self.title
# Create your models here.
