from django.db import models


class Imovel(models.Model):
    codigo_imovel = models.IntegerField(primary_key=True)
    limite_hospedes = models.IntegerField()
    quantidade_banheiros = models.IntegerField()
    aceita_animais = models.BooleanField()
    valor_limpeza = models.DecimalField(max_digits=8, decimal_places=2)
    data_ativacao = models.DateField()
    data_criacao = models.DateTimeField(auto_now_add=True, null=True)
    data_atualizacao = models.DateTimeField(auto_now=True, null=True)


class Anuncio(models.Model):
    codigo_imovel = models.IntegerField()
    plataforma = models.CharField(max_length=20)
    taxa_plataforma = models.DecimalField(max_digits=5, decimal_places=2)
    data_criacao = models.DateTimeField(auto_now_add=True, null=True)
    data_atualizacao = models.DateTimeField(auto_now=True, null=True)
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)


class Reserva(models.Model):
    codigo_reserva = models.CharField(max_length=10)
    id_anuncio = models.IntegerField()
    data_checkin = models.DateField()
    data_checkout = models.DateField()
    preco_total = models.DecimalField(max_digits=8, decimal_places=2)
    comentario = models.TextField(blank=True, null=True)
    numero_hospedes = models.IntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True, null=True)
    data_atualizacao = models.DateTimeField(auto_now=True, null=True)
    anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE)
