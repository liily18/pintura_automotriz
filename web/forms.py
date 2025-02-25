from django import forms

class ContactoForm(forms.Form):
    nombre_completo = forms.CharField(
        label="Nombre Completo", 
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre completo'})
    )
    correo = forms.EmailField(
        label="Correo Electrónico", 
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'tuemail@ejemplo.com'})
    )
    direccion = forms.CharField(
        label="Dirección", 
        max_length=200, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu dirección'})
    )
    asunto = forms.ChoiceField(
        label="Asunto",
        choices=[
            ('cotizacion', 'Cotización'),
            ('duda', 'Duda'),
            ('sugerencia', 'Sugerencia'),
            ('reclamo', 'Reclamo')
        ],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    comentario = forms.CharField(
        label="Comentario", 
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Escribe tu mensaje aquí...'})
    )
