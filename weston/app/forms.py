from django import forms




class UserLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'id': 'loginEmail',
                'type': 'email',
                'class': 'form-control mt-1 mb-2',
                'placeholder': 'Ingrese su Correo Electrónico'
            }
        )
    )
 
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'id': 'loginPassword',
            'type': 'password',
            'class': 'form-control mt-1 mb-3',
            'placeholder': 'Ingrese su Contraseña'
        })
    )


class UserSignUpForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'id': 'loginEmail',
                'type': 'email',
                'class': 'form-control mt-1 mb-2',
                'placeholder': 'Ingresar Correo Electrónico'
            }
        )
    )
    nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'id': 'nombre',
                'type': 'text',
                'class': 'form-control mt-1 mb-2',
                'placeholder': 'Ingrese Nombre'
            }
        ))
    telefono = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'id': 'telefono',
                'type': 'number',
                'class': 'form-control mt-1 mb-2',
                'placeholder': 'Ingrese Número de Teléfono'
            }
        ))

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id': 'clave1',
                'type': 'password',
                'class': 'form-control mt-1 mb-2',
                'placeholder': 'Ingrese Contraseña'
            }
        ))

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id': 'clave2',
                'type': 'password',
                'class': 'form-control mt-1 mb-3',
                'placeholder': 'Repetir Contraseña'
            }
        ))

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Las Contraseñas no coinciden')
        return cd['password2']
