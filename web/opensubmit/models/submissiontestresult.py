from django.db import models

class SubmissionTestResult(models.Model):
    '''
        An executor test result for a given submission file.
    '''

    VALIDITY_TEST = 'v'
    FULL_TEST = 'f'
    JOB_TYPES = (
        (VALIDITY_TEST, 'Validation test'),
        (FULL_TEST, 'Full test')
    )
    submission_file = models.ForeignKey('SubmissionFile', models.CASCADE, related_name="test_results")
    machine = models.ForeignKey('TestMachine', models.CASCADE, related_name="test_results")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    result = models.TextField(null=True, blank=True)
    result_tutor = models.TextField(null=True, blank=True)
    kind = models.CharField(max_length=2, choices=JOB_TYPES)
    perf_data = models.TextField(null=True, blank=True)

    class Meta:
        app_label = 'opensubmit'
