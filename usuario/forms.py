from django import forms


class LoginForm(forms.Form):
    nome_de_login = forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Ex.: Beyoncé"}
        ),
    )
    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Digite sua senha"}
        ),
    )


class CadastroForm(forms.Form):
    nome_de_cadastro = forms.CharField(
        label="Nome de Cadastro",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Ex.: Beyoncé"}
        ),
    )
    email = forms.EmailField(
        label="E-mail",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: joao.silva@exemplo.com",
            }
        ),
    )
    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Digite sua senha"}
        ),
    )
    confirmacao_de_senha = forms.CharField(
        label="Confirmação de Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Digite sua senha novamente"}
        ),
    )

    def clean_nome_de_cadastro(self):
        nome = self.cleaned_data.get("nome_de_cadastro")

        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError(
                    "Não é possível inserir espaços no campo Nome de Cadastro."
                )
            else:
                return nome

    def clean_confirmacao_de_senha(self):
        senha = self.cleaned_data.get("senha")
        confirmacao_de_senha = self.cleaned_data.get("confirmacao_de_senha")

        if senha and confirmacao_de_senha:
            if senha != confirmacao_de_senha:
                raise forms.ValidationError("Senhas não são iguais")
            else:
                return confirmacao_de_senha
