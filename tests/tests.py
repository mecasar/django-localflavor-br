from __future__ import unicode_literals

from django.contrib.localflavor.br.forms import (BRZipCodeField,
    BRCNPJField, BRCPFField, BRPhoneNumberField, BRStateSelect,
    BRStateChoiceField)

from django.test import SimpleTestCase


class BRLocalFlavorTests(SimpleTestCase):
    def test_BRZipCodeField(self):
        error_format = ['Enter a zip code in the format XXXXX-XXX.']
        valid = {
            '12345-123': '12345-123',
        }
        invalid = {
            '12345_123': error_format,
            '1234-123': error_format,
            'abcde-abc': error_format,
            '12345-': error_format,
            '-123': error_format,
        }
        self.assertFieldOutput(BRZipCodeField, valid, invalid)

    def test_BRCNPJField(self):
        error_format = ['Invalid CNPJ number.']
        error_numbersonly = ['This field requires only numbers.']
        valid = {
            '64.132.916/0001-88': '64.132.916/0001-88',
            '64-132-916/0001-88': '64-132-916/0001-88',
            '64132916/0001-88': '64132916/0001-88',
        }
        invalid = {
            '12-345-678/9012-10': error_format,
            '12.345.678/9012-10': error_format,
            '12345678/9012-10': error_format,
            '64.132.916/0001-XX': error_numbersonly,
        }
        self.assertFieldOutput(BRCNPJField, valid, invalid)

    def test_BRCPFField(self):
        error_format = ['Invalid CPF number.']
        error_numbersonly = ['This field requires only numbers.']
        error_atmost_chars = ['Ensure this value has at most 14 characters (it has 15).']
        error_atleast_chars = ['Ensure this value has at least 11 characters (it has 10).']
        error_atmost = ['This field requires at most 11 digits or 14 characters.']
        valid = {
            '663.256.017-26': '663.256.017-26',
            '66325601726': '66325601726',
            '375.788.573-20': '375.788.573-20',
            '84828509895': '84828509895',
        }
        invalid = {
            '489.294.654-54': error_format,
            '295.669.575-98': error_format,
            '539.315.127-22': error_format,
            '375.788.573-XX': error_numbersonly,
            '375.788.573-000': error_atmost_chars,
            '123.456.78': error_atleast_chars,
            '123456789555': error_atmost,
        }
        self.assertFieldOutput(BRCPFField, valid, invalid)

    def test_BRPhoneNumberField(self):
        # TODO: this doesn't test for any invalid inputs.
        error_format = [u'Phone numbers must be in XX-XXXX-XXXX format.']
        valid = {
            '41-3562-3464': '41-3562-3464',
            '4135623464': '41-3562-3464',
            '41 3562-3464': '41-3562-3464',
            '41 3562 3464': '41-3562-3464',
            '(41) 3562 3464': '41-3562-3464',
            '41.3562.3464': '41-3562-3464',
            '41.3562-3464': '41-3562-3464',
            ' (41) 3562.3464': '41-3562-3464',
            '11-53562-3464': '11-53562-3464',
            '11535623464': '11-53562-3464',
            '11 53562-3464': '11-53562-3464',
            '11 53562 3464': '11-53562-3464',
            '(11) 53562 3464': '11-53562-3464',
            '11.53562.3464': '11-53562-3464',
            '11.53562-3464': '11-53562-3464',
            ' (11) 53562.3464': '11-53562-3464',
        }
        invalid = {
            '415623464': error_format,
            '1-5362-3464': error_format,
            '1 5362-3464': error_format,
            '(1) 5362 3464': error_format,
            '1.3562.3464' : error_format,
            '1.3562-3464': error_format,
            '41562346456': error_format,
            '1-5362-346456': error_format,
            '1 5362-346456': error_format,
            '(1) 5362 346456': error_format,
            '1.356256.3464' : error_format,
            '1.356256-3464': error_format,
        }
        self.assertFieldOutput(BRPhoneNumberField, valid, invalid)

    def test_BRStateSelect(self):
        f = BRStateSelect()
        out = '''<select name="states">
<option value="AC">Acre</option>
<option value="AL">Alagoas</option>
<option value="AP">Amap\xe1</option>
<option value="AM">Amazonas</option>
<option value="BA">Bahia</option>
<option value="CE">Cear\xe1</option>
<option value="DF">Distrito Federal</option>
<option value="ES">Esp\xedrito Santo</option>
<option value="GO">Goi\xe1s</option>
<option value="MA">Maranh\xe3o</option>
<option value="MT">Mato Grosso</option>
<option value="MS">Mato Grosso do Sul</option>
<option value="MG">Minas Gerais</option>
<option value="PA">Par\xe1</option>
<option value="PB">Para\xedba</option>
<option value="PR" selected="selected">Paran\xe1</option>
<option value="PE">Pernambuco</option>
<option value="PI">Piau\xed</option>
<option value="RJ">Rio de Janeiro</option>
<option value="RN">Rio Grande do Norte</option>
<option value="RS">Rio Grande do Sul</option>
<option value="RO">Rond\xf4nia</option>
<option value="RR">Roraima</option>
<option value="SC">Santa Catarina</option>
<option value="SP">S\xe3o Paulo</option>
<option value="SE">Sergipe</option>
<option value="TO">Tocantins</option>
</select>'''
        self.assertHTMLEqual(f.render('states', 'PR'), out)

    def test_BRStateChoiceField(self):
        error_invalid = ['Select a valid brazilian state. That state is not one of the available states.']
        valid = {
            'AC': 'AC',
            'AL': 'AL',
            'AP': 'AP',
            'AM': 'AM',
            'BA': 'BA',
            'CE': 'CE',
            'DF': 'DF',
            'ES': 'ES',
            'GO': 'GO',
            'MA': 'MA',
            'MT': 'MT',
            'MS': 'MS',
            'MG': 'MG',
            'PA': 'PA',
            'PB': 'PB',
            'PR': 'PR',
            'PE': 'PE',
            'PI': 'PI',
            'RJ': 'RJ',
            'RN': 'RN',
            'RS': 'RS',
            'RO': 'RO',
            'RR': 'RR',
            'SC': 'SC',
            'SP': 'SP',
            'SE': 'SE',
            'TO': 'TO',
        }
        invalid = {
            'pr': error_invalid,
        }
        self.assertFieldOutput(BRStateChoiceField, valid, invalid)
