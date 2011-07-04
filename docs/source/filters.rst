Filters
-------

Reusable django application that makes posible
to create very flexible Model generic filters.

.. note::
   This documentation site assumes that you're
   familiar with django.

The basic idea is to create Form instance for each field
of model's fields and make possible to join them to sets
and then join those sets to groups:

::

  field_name     :    field_value-to-filter AND
  field_name     :    field_value-to-filter AND
  field_name     :    field_value-to-filter

  - OR -

  field_name     :    field_value-to-filter AND
  field_name     :    field_value-to-filter AND
  field_name     :    field_value-to-filter

  - etc ... -

All filter values in one set are join with AND operator
all sets values are join with OR operator.


How does it work
================

1) Mechanism is based on django.forms. Each model's field is translated
   to FieldFilterForm subclass (with a pretty name) eg. if you have Person
   model:

.. code-block:: python

   class Person(models.Model):
       name = models.CharField(max_length=512)


filter form that will be generated for ``name`` field would be:


.. code-block:: python

   class PersonNameFieldFilterForm(FieldFilterForm):
       q = forms.CharField(required=False)


2) Application introduces special control forms. Forms params are processed
   in filter.views.filter view. If control field occur it changes number of
   field filters, removes forms control params and redirects to same page
   withuot control params.


Convention
==========

Each Form representing the field shoud have:
  - ``construct_Q`` method which returns django's Q object
  - ``field_name`` instance variable with the field name
  - ``field_name_label`` instance variable with label for field filter
  - ALL FieldFilterForm fields MUSN'T be required.

<<<<<<< HEAD
   There are special forms in field filters called control forms
   designed to add field filters, field groups, and removing them.
=======

Mapping between django ORM fields and field filter forms is defined in
``qualitio.filter.fieldfilters`` module.
>>>>>>> 94a9d75a0c18031600570d235c61347c090ea27c


Usage
=====

Suppose we have example ``people`` application with following model:

.. code-block:: python

   # people/models.py
   class Person(models.Model):
       first_name = models.CharField(max_length=512)
       last_name = models.CharField(max_length=512)


We can define filter for the above model:


.. code-block:: python

   # people/filters.py
   from people.models import Person
   from qualitio import filter as filterapp

   class PeopleFilter(filterapp.ModelFilter):
       class Meta:
           model = Person
	   # options:
	   # fields = (<field names>)
	   # exclude = (<field names to exclude>)


and construct view for it:


.. code-block:: python

   # people/views.py
   from people.filters import PeopleFilter

   def people_filter(request):
       filter = PeopleFilter(request.GET)

       has_control_params, params = filter.build_from_params()
       if has_control_params:
           return HttpResponseRedirect('%s?%s' % (request.path, params.urlencode()))

       return render_to_response('people/filter.html', {
           'queryset': filter.qs,
	   'filter': filter,
       })


Custom filters
==============

Filter works fully dynamic however it can be customized.

Let's customize out previous example. We'll make custom
field filter for ``first_name`` field.


.. code-block:: python

   # people/filters.py
   from django import forms
   from django.db.models import Q

   from people.models import Person
   from qualitio import filter as filterapp

   class FirstNameFieldFilter(filterapp.FieldFilterForm):

       # It's really important to MAKE FIELDS NOT REQUIRED
       startswith = forms.CharField(required=False)
       endswith = forms.CharField(required=False)

       # ``field_name`` variable will be prepared for you by
       # ``FieldFilter.create_form_class`` method so DON'T write it
       # field_name = 'first_name'

       # You can add label here or as an option in ``FieldFilter`` declaration
       # below in ``Filter`` class definition
       field_name_label = 'First name filter'

       def construct_Q(self):
       	   startswith = self.cleaned_data.get('startswith')
       	   endswith = self.cleaned_data.get('endswith')
	   return Q('%s__startswith' % self.field_name : startswith,
	            '%s__endswith' % self.field_name : endswith)

   class PeopleFilter(filterapp.ModelFilter):
       class Meta:
           model = Person

       # qustom ``first_name`` field filter with overriden label
       first_name = filters.FieldFilter(FirstNameFieldFilter, label="Field name blah blah")


Filter app in Qualitio
======================

Filter app provides generic way for filtering in Qualitio. Each of main applications
(require, store, execute) can provide it's own customization for filtering.

Example filter customization can be found in ``qualitio/require/filter.py`` file.



Actions
=======

Actions are an operations that can be run on filtered (and selected)
items in filter views.


* where the actions came from?

   filter view search for actions in '<model-application-name>.actions' module
   and it pick up every class that is derived from 'qualitio.filter.actions.Action'

   So to make sure you're actions will be founded put them in
   '<your-application>.actions' module.


* how to write an action?

   Eg. for existing require application


.. code-block:: python

   # qualitio.require.actions
   from django import forms

   from qualitio.require import models
   from qualitio.filter import actions

   class ChangeParentForm(actions.ActionForm):
       parent = forms.ModelChoiceField(queryset=models.Requirement.objects.all())

   class ChangeParent(actions.Action):
       model = models.Requirement
       label = 'Change parent'
       form_class = ChangeParentForm

       def run_action(self, querydict, queryset, form=None):
           for obj in queryset.all():
               obj.parent = form.cleaned_data.get('parent')
               obj.modified_time = datetime.datetime.now()
               obj.save()
	   return self.success(message='Action done!')


'form' param is used only if you attach form to your action.
Form is validated before 'run_actions' runs in 'execute' method.
