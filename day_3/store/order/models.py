from django.db import models


class Order(models.Model):
    date = models.DateField()
    status = models.CharField(max_length=24, default='abierta')

    def __str__(self):
        return f'No. de orden: {self.id}, fecha: {self.date}'

    def save(self, *args, **kwargs):
        if self.status == 'procesar':
            details = self.orderdetails_set.all()
            error = False
            for detail in details:
                detail.item.stock = detail.item.stock - detail.quantity

                if detail.item.stock < 0:
                    error = True
                    return {"message:": "Not enough stock"}
    
            if not(error):
                for detail in details:
                    detail.item.save()

                self.status = 'cerrada'

        super(Order, self).save(*args, **kwargs)


class Item(models.Model):
    devise = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    stock = models.IntegerField()

    # class Meta:
    #     abstract = True

    def __str__(self):
        return f'{self.devise} brand: {self.brand}, model: {self.model}, stock: {self.stock}'

class Computer(Item):

    def __str__(self):
        return f'Computadora: {self.brand}'


    def save(self, *args, **kwargs):
        self.devise = 'Computer'
        super(Computer, self).save(*args, **kwargs)


class OrderDetails(models.Model):
    quantity = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True)
    orden = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f'{self.orden} - {self.item}'


class InputDevise(Item):
    type = models.CharField(max_length=100)

    # class Meta:
    #     abstract = True

    def __str__(self):
        return self.type


class Mouse(InputDevise):

    def __str__(self):
        return f'Mouse: {self.type}, brand: {self.brand}, stock: {self.stock}'


    def save(self, *args, **kwargs):
        self.devise = 'Mouse'
        super(Mouse, self).save(*args, **kwargs)


class Keyboard(InputDevise):

    def __str__(self):
        return f'Keyboard: {self.type}, brand: {self.brand}, stock: {self.stock}'


    def save(self, *args, **kwargs):
        self.devise = 'Keyboard'
        super(Keyboard, self).save(*args, **kwargs)


class Monitor(Item):
    size = models.CharField(max_length=50)

    def __str__(self):
        return f'Monitor: {self.brand}, {self.size}", stock: {self.stock}'

    def save(self, *args, **kwargs):
        self.devise = 'Monitor'
        super(Monitor, self).save(*args, **kwargs)

