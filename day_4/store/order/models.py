from django.db import models


class Component(models.Model):
    component = (
        ('Keyboard', 'Keyboard'),
        ('Mouse', 'Mouse'),
        ('Display', 'Display'),
        ('Speaker', 'Speaker'),
        ('Motherboard', 'Motherboard'),
        ('Processor', 'Processor')
    )
    type = models.CharField(choices=component, max_length=50)

    class Meta:
        abstract = True

    
    def __str__(self):
        return self.type


class ImputDevice(Component):
    brand = models.CharField(max_length=50)

    def __str__(self):
        return self.brand


class Keyboard(ImputDevice):
    quantity = models.IntegerField()
    cost = models.FloatField()
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.description} {self.brand}, stock: {self.quantity}'


class Mouse(ImputDevice):
    type = 'Mouse'
    quantity = models.IntegerField()
    cost = models.FloatField()
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.description} {self.brand}, stock: {self.quantity}'


class OutputDevice(Component):
    brand = models.CharField(max_length=50)

    def __str__(self):
        return self.brand

class Display(OutputDevice):
    quantity = models.IntegerField()
    cost = models.FloatField()
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.description} {self.brand}, stock: {self.quantity}'


class Speaker(OutputDevice):
    quantity = models.IntegerField()
    cost = models.FloatField()
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.description} {self.brand}, stock: {self.quantity}'


class InternalDevice(Component):
    brand = models.CharField(max_length=100)

    def __str__(self):
        return self.brand


class Motherboard(InternalDevice):
    quantity = models.IntegerField()
    cost = models.FloatField()
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.description} {self.brand}, stock: {self.quantity}'


class Processor(InternalDevice):
    quantity = models.IntegerField()
    cost = models.FloatField()
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.description} {self.brand}, stock: {self.quantity}'


class Computer(models.Model):
    name = models.CharField(max_length=100)
    display = models.ForeignKey(Display, on_delete=models.CASCADE)
    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)
    mouse = models.ForeignKey(Mouse, on_delete=models.CASCADE)
    keyboard = models.ForeignKey(Keyboard, on_delete=models.CASCADE)
    motherboard = models.ForeignKey(Motherboard, on_delete=models.CASCADE)
    processor = models.ForeignKey(Processor, on_delete=models.CASCADE)

    quantity = models.IntegerField(default=1)
    total_cost = models.FloatField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}, stock: {self.quantity}, price: {self.total_cost}'


    def decrement(self):
        keyboard = Keyboard.objects.filter(id=self.keyboard.id)[0]
        mouse = Mouse.objects.filter(id=self.mouse.id)[0]
        display = Display.objects.filter(id=self.display.id)[0]
        speaker = Speaker.objects.filter(id=self.speaker.id)[0]
        motherboard = Motherboard.objects.filter(id=self.motherboard.id)[0]
        processor = Processor.objects.filter(id=self.processor.id)[0]

        if keyboard.quantity >= self.quantity and mouse.quantity >= self.quantity and display.quantity >= self.quantity and speaker.quantity >= self.quantity and motherboard.quantity >= self.quantity and processor.quantity >= self.quantity:
            keyboard.quantity = self.keyboard.quantity - self.quantity
            mouse.quantity = self.mouse.quantity - self.quantity
            display.quantity = self.display.quantity- self.quantity
            speaker.quantity = self.speaker.quantity - self.quantity
            motherboard.quantity = self.motherboard.quantity - self.quantity
            processor.quantity = self.processor.quantity - self.quantity

            keyboard.save()
            mouse.save()
            display.save()
            speaker.save()
            motherboard.save()
            processor.save()

            self.total_cost = keyboard.cost + mouse.cost + display.cost + speaker.cost + motherboard.cost  + processor.cost

            return True
        
        self.total_cost = 0
        return False

    def save(self, *args, **kwargs):
        if self.decrement():
            super(Computer, self).save(*args, **kwargs)
            return True

        return False


class Order(models.Model):
    total_cost = models.FloatField(null=True, blank=True)
    code = models.CharField(max_length=25, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order No. {self.id}'


class OrderDetails(models.Model):
    quantity = models.IntegerField(default=1)
    total = models.FloatField(blank=True, null=True)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE, blank=True)
    orden = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f'{self.orden} - {self.computer}'


    def decrement(self):
        if self.computer.quantity >= self.quantity:
            self.computer.quantity = self.computer.quantity - self.quantity
            self.computer.save()

            # print('*' * 50)
            # print(self.computer)
            self.total = self.computer.total_cost * self.quantity
            # print('OrderDetail total: {}, computer cost: {}, quantity: {}'.format(self.total,  self.computer.total_cost, self.quantity))
            self.orden.total_cost = self.orden.total_cost + self.total if self.orden.total_cost else self.total
            self.orden.save()
            # print('Order total Cost: {}'.format(self.orden.total_cost))
            # print('*' * 50)

            return True
        
        return False

    def save(self, *args, **kwargs):
        if self.decrement():
            super(OrderDetails, self).save(*args, **kwargs)
            return True

        return False