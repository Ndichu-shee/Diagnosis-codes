from django.test import TestCase
from records.models import DiagnosisCodes

class DiagnosisCodesTestCase(TestCase):
     
    def setUp(self):

        DiagnosisCodes.objects.create(
            icd_code='ICD_10 2015',
            category_code='AOO',
            code_id='3',
            addition_code='AOO3',
            summary='Cholera due to Vibrio cholerae 01, biovar cholerae',
            description='Cholera due to Vibrio cholerae 01, biovar cholerae',
            category_title='Cholera',
        )
    def test_diagnosis_codes(self):
        diagnosiscodes = DiagnosisCodes.objects.get(id=1)
        icd_code = f'{diagnosiscodes. icd_code}'
        category_code = f'{diagnosiscodes.category_code}'
        code_id = f'{diagnosiscodes.code_id}'
        addition_code = f'{diagnosiscodes.addition_code}'
        summary = f'{diagnosiscodes.summary}'
        description = f'{diagnosiscodes.description}'
        category_title =f'{diagnosiscodes.category_title}'

        self.assertEqual(icd_code,'ICD_10 2015')
        self.assertEqual(category_code,'AOO')
        self.assertEqual( code_id,'3')
        self.assertEqual(addition_code,'AOO3')
        self.assertEqual(summary,'Cholera due to Vibrio cholerae 01, biovar cholerae')
        self.assertEqual(description,'Cholera due to Vibrio cholerae 01, biovar cholerae')
        self.assertEqual(category_title,'Cholera')
        result = DiagnosisCodes.objects.all()
        self.assertEqual(len(result),1)