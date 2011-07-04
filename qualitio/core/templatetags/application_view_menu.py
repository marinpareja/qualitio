from django import template
from django.template import RequestContext

register = template.Library()

@register.tag
def application_view_menu(parser, token):
    obj, view = token.split_contents()[1:]
    return ApplicationViewMenuNode(parser.compile_filter(obj), parser.compile_filter(view))


class ApplicationViewMenuNode(template.Node):
    # TODO: this could be probably better resolved by using some registartion form for views,
    # to determine which view currently open
    # TODO: move this to core
    def __init__(self, obj, view):
        self.obj = obj
        self.view = view

    def render(self, context):
        materialized_obj = self.obj.resolve(context)
        materialized_view = self.view.resolve(context)
        return template.loader.render_to_string("%s/_%s_menu.html"
                                                % (materialized_obj._meta.app_label,
                                                   materialized_obj._meta.module_name),
                                                {"obj" : materialized_obj,
                                                 "view" : materialized_view},
                                                context_instance=RequestContext(context['request']))
