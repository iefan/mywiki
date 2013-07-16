# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1373936473.527
_enable_loop = True
_template_filename = u'themes\\blogtxt\\templates/gallery.tmpl'
_template_uri = u'gallery.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'extra_head', u'sourcelink']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def extra_head():
            return render_extra_head(context.locals_(__M_locals))
        permalink = context.get('permalink', UNDEFINED)
        text = context.get('text', UNDEFINED)
        def content():
            return render_content(context.locals_(__M_locals))
        images = context.get('images', UNDEFINED)
        def sourcelink():
            return render_sourcelink(context.locals_(__M_locals))
        rel_link = context.get('rel_link', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        # SOURCE LINE 8
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        # SOURCE LINE 9
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 30
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        text = context.get('text', UNDEFINED)
        images = context.get('images', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 11
        __M_writer(u'\n    <p>\n')
        # SOURCE LINE 13
        if text:
            # SOURCE LINE 14
            __M_writer(u'        ')
            __M_writer(unicode(text))
            __M_writer(u'\n')
        # SOURCE LINE 16
        __M_writer(u'    </p>\n    <ul class="thumbnails">\n')
        # SOURCE LINE 18
        for image in images:
            # SOURCE LINE 19
            __M_writer(u'            <li><a href="')
            __M_writer(unicode(image[0]))
            __M_writer(u'" class="thumbnail"><img src="')
            __M_writer(unicode(image[1]))
            __M_writer(u'" /></a></li>\n')
        # SOURCE LINE 21
        __M_writer(u"    </ul>\n    <script>\n        jQuery('a.thumbnail').colorbox({\n            rel:'gal',\n            maxWidth:'80%',\n            maxHeight:'80%',\n            scalePhotos: true\n        });\n    </script>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        rel_link = context.get('rel_link', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        permalink = context.get('permalink', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n    <link rel="stylesheet" href="')
        # SOURCE LINE 5
        __M_writer(unicode(rel_link(permalink, "/assets/css/colorbox.css")))
        __M_writer(u'"/>\n    <script src="')
        # SOURCE LINE 6
        __M_writer(unicode(rel_link(permalink, "/assets/js/jquery-1.7.2.min.js")))
        __M_writer(u'"></script>\n    <script src="')
        # SOURCE LINE 7
        __M_writer(unicode(rel_link(permalink, "/assets/js/jquery.colorbox-min.js")))
        __M_writer(u'"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


