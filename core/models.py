
from stdimage.models import StdImageField
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# models de cadastro de usuario
class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O e-mail é Obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        # extra_fields.setdefault()
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True')

        return self._create_user(email, password, **extra_fields)


class CustomUsuario(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    fone = models.CharField('Telefone', max_length=15)
    is_staff = models.BooleanField('Membro da equipe', default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'fone']

    def __str__(self):
        return self.email

    objects = UsuarioManager()


# models de cadastrar informações
'''class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True'''


class Link(models.Model):
    ICONE_CHOICES = (
        ('bi bi-instagram', 'Instagram'),
        ('bi bi-facebook', 'Facebook'),
        ('bi bi-twitter', 'Twitter'),
        ('bi bi-youtube', 'Youtube'),
        ('bi bi-whatsapp', 'Whatsapp')
    )
    nome = models.CharField('Nome', max_length=100)
    nickname = models.CharField('Nickname', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    link = models.CharField('Link', max_length=150)
    icone = models.CharField('Icone', max_length=17, choices=ICONE_CHOICES)
    imagem = StdImageField('Imagem', upload_to='link', variations={'thumb': (250, 250)})

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'

    def __str__(self):
        return self.nome
