from django.db import models


class TreeMenuCategory(models.Model):
    class Meta:
        verbose_name = 'Menu category'
        verbose_name_plural = 'Menu categories'

    name = models.CharField('Name', max_length=50, blank=True, null=False)
    verbose_name = models.CharField('Verbose name', max_length=50, blank=True, null=False)

    def __str__(self):
        return self.verbose_name


class TreeMenu(models.Model):
    class Meta:
        verbose_name = 'Menu item'
        verbose_name_plural = 'Menu items'

    name = models.CharField('Name', max_length=50, blank=True, null=False)
    category = models.ForeignKey(TreeMenuCategory, verbose_name='Category', on_delete=models.CASCADE, blank=False,
                                 null=False)
    path = models.CharField('Link', max_length=100, blank=True, null=False)
    parent = models.ForeignKey('self', verbose_name='Parent element', on_delete=models.SET_DEFAULT, null=True,
                               blank=True, default=0)

    def __str__(self):
        return self.name
