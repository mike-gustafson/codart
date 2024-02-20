from django import forms
from .models import Dart, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

LANGUAGE_CHOICES = [
    ('', 'Click to Select Language'),
    ('c', 'C'),
    ('java', 'Java'),
    ('python', 'Python'),
    ('csharp', 'C#'),
    ('cpp', 'C++'),
    ('javascript', 'JavaScript'),
    ('php', 'PHP'),
    ('ruby', 'Ruby'),
    ('swift', 'Swift'),
    ('go', 'Go'),
    ('typescript', 'TypeScript'),
    ('kotlin', 'Kotlin'),
    ('rust', 'Rust'),
    ('scala', 'Scala'),
    ('perl', 'Perl'),
    ('dart', 'Dart'),
    ('lua', 'Lua'),
    ('haskell', 'Haskell'),
    ('r', 'R'),
    ('sql', 'SQL'),
    ('html', 'HTML'),
    ('css', 'CSS'),
    ('bash', 'Bash/Shell'),
    ('matlab', 'MATLAB'),
    ('groovy', 'Groovy'),
    ('powershell', 'PowerShell'),
    ('julia', 'Julia'),
    ('elixir', 'Elixir'),
    ('fortran', 'Fortran'),
    ('assembly', 'Assembly'),
    ('pascal', 'Pascal'),
    ('scheme', 'Scheme'),
    ('objective-c', 'Objective-C'),
    ('vba', 'VBA'),
    ('swift', 'Swift'),
    ('ruby', 'Ruby'),
    ('fsharp', 'F#'),
    ('clojure', 'Clojure'),
    ('erlang', 'Erlang'),
    ('visual-basic', 'Visual Basic'),
    ('sas', 'SAS'),
    ('cobol', 'COBOL'),
    ('apl', 'APL'),
    ('ada', 'Ada'),
    ('ocaml', 'OCaml'),
    ('abap', 'ABAP'),
    ('scratch', 'Scratch'),
    ('prolog', 'Prolog'),
    ('lisp', 'Lisp'),
    ('labview', 'LabVIEW'),
    ('d', 'D'),
    ('awk', 'AWK'),
    ('smalltalk', 'Smalltalk'),
    ('plsql', 'PL/SQL'),
    ('forth', 'Forth'),
    ('actionscript', 'ActionScript'),
    ('vhdl', 'VHDL'),
    ('elm', 'Elm'),
    ('tcl', 'TCL'),
    ('logo', 'Logo'),
    ('foxpro', 'FoxPro'),
    ('factor', 'Factor'),
    ('hack', 'Hack'),
    ('nim', 'Nim'),
    ('crystal', 'Crystal'),
    ('verilog', 'Verilog'),
    ('coffeescript', 'CoffeeScript'),
    ('xquery', 'XQuery'),
    ('coldfusion', 'ColdFusion'),
    ('haxe', 'Haxe'),
    ('webassembly', 'WebAssembly'),
    ('racket', 'Racket'),
    ('common-lisp', 'Common Lisp'),
    ('lua', 'Lua'),
    ('vala', 'Vala'),
    ('solidity', 'Solidity'),
    ('io', 'Io'),
    ('reason', 'Reason'),
    ('mojolicious', 'Mojolicious'),
    ('livecode', 'LiveCode'),
    ('mercury', 'Mercury'),
    ('ballerina', 'Ballerina'),
    ('idris', 'Idris'),
    ('pike', 'Pike'),
    ('sed', 'Sed'),
    ('rebol', 'REBOL'),
    ('pure-data', 'Pure Data'),
    ('autoit', 'AutoIt'),
    ('mumps', 'MUMPS'),
    ('chapel', 'Chapel'),
    ('cuneiform', 'Cuneiform'),
    ('cil', 'CIL'),
    ('clips', 'CLIPS'),
    ('cobra', 'Cobra'),
    ('algol', 'ALGOL'),
    ('nimrod', 'Nimrod'),
    ('oak', 'Oak'),
    ('oberon', 'Oberon'),
    ('modula-2', 'Modula-2'),
    ('j', 'J'),
]

class DartForm(forms.ModelForm):
    code_language = forms.ChoiceField(choices=LANGUAGE_CHOICES, widget=forms.Select(attrs={'class': 'form-control border-primary', 'style': 'width: fit-content'}))
    
    class Meta:
        model = Dart
        exclude = ("user", "likes", "dislikes")
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Title',
                    'class': 'form-control border-primary'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                    'class': 'form-control border-primary',
                    'rows': 3
                }
            ),
            'code_block': forms.Textarea(
                attrs={
                    'placeholder': 'Enter your code here',
                    'class': 'form-control border-primary'
                }
            ),
            
        }


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="", 
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email Address'
            }
        ),
    )
    first_name = forms.CharField(
        label="", 
        max_length=100, 
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'First Name'
            }
        ),
    )
    last_name = forms.CharField(
        label="", 
        max_length=100, 
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Last Name'
            }
        ),
    )

    username = forms.CharField(
        label="", 
        max_length=100, 
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }
        ),
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<span class="form-text text-muted"><small>Your password can\'t be too similar to your other personal information.<br>Your password must contain at least 8 characters.<br>Your password can\'t be a commonly used password.<br>Your password can\'t be entirely numeric.</small></span>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')  # Adjust as needed

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_image',)