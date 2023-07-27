from .models import Orders, Comments
from django.forms import ModelForm, TextInput, Textarea

class OrdersForm(ModelForm):
 class Meta:

     model = Orders
     fields = ["email", "telephone", "name", "organization", "full_text"]

     widgets = {
      "email": TextInput(attrs={
      "class": "form-control", "placeholder": "Ваш email"}),

      "telephone": TextInput(attrs={
      "class": "form-control", "placeholder": "Ваш телефон (можно указать несколько)"}),

      "name": TextInput(attrs={
      "class": "form-control", "placeholder": "ФИО"}),

      "organization": TextInput(attrs={
      "class": "form-control", "placeholder": "Организация ( поле для юридических лиц)"}),

      "full_text": Textarea(attrs={
      "class": "form-control", "placeholder": "Описание заказа, требуемая услуга, указание маршрута груза \n"
      "Например: Ставрополь - Невинномысск, необходимо перевезти мебель, \n"
      "имеются особые хрупкие детали, общим весом около 50 кг"}),
     }


class CommentsForm(ModelForm):
    class Meta:

      model = Comments
      fields = ["email", "name", "full_text"]

      widgets = {
       "email": TextInput(attrs={
       "class": "form-control", "placeholder": "Ваш email"}),

       "name": TextInput(attrs={
       "class": "form-control", "placeholder": "Имя/Фамилия"}),

       "full_text": Textarea(attrs={
       "class": "form-control", "placeholder": "Напишите свой отзыв о работе нашей компании"}),
      }
