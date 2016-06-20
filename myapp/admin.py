from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from myapp.models import TestModel

class ResourceTestModel_1(resources.ModelResource):
    class Meta:
        model = TestModel

    def before_import(self, *args, **kwargs):
        self._meta.model.objects.all().delete()

    def get_or_init_instance(self, instance_loader, row):
        return (self.init_instance(row), True)

class ResourceTestModel_2(resources.ModelResource):
    class Meta:
        model = TestModel
        bulk_replace = True

@admin.register(TestModel)
class AdminTestModel(ImportExportModelAdmin):
    resource_class = ResourceTestModel_2
    list_display = ('id', 'f1', 'f2', 'f3', 'f4',)

