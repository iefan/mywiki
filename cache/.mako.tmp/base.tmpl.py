# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1373936473.442
_enable_loop = True
_template_filename = u'themes\\blogtxt\\templates/base.tmpl'
_template_uri = u'base.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'extra_head', u'belowtitle']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        lang = context.get('lang', UNDEFINED)
        def extra_head():
            return render_extra_head(context.locals_(__M_locals))
        permalink = context.get('permalink', UNDEFINED)
        license = context.get('license', UNDEFINED)
        title = context.get('title', UNDEFINED)
        def belowtitle():
            return render_belowtitle(context.locals_(__M_locals))
        search_form = context.get('search_form', UNDEFINED)
        sidebar_links = context.get('sidebar_links', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        content_footer = context.get('content_footer', UNDEFINED)
        len = context.get('len', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        analytics = context.get('analytics', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        blog_url = context.get('blog_url', UNDEFINED)
        rel_link = context.get('rel_link', UNDEFINED)
        def content():
            return render_content(context.locals_(__M_locals))
        blog_title = context.get('blog_title', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'<!DOCTYPE html>\n<html lang="')
        # SOURCE LINE 3
        __M_writer(unicode(lang))
        __M_writer(u'">\n<head>\n    <meta charset="utf-8">\n    <title>')
        # SOURCE LINE 6
        __M_writer(unicode(title))
        __M_writer(u'</title>\n    <!-- Le styles -->\n    <link rel="stylesheet" type="text/css" media="screen,projection" href="')
        # SOURCE LINE 8
        __M_writer(unicode(rel_link(permalink, "/assets/css/style.css")))
        __M_writer(u'" title="blog.txt" />\n    <link rel="stylesheet" type="text/css" media="screen,projection" href="')
        # SOURCE LINE 9
        __M_writer(unicode(rel_link(permalink, "/assets/css/2c-r.css")))
        __M_writer(u'" title="blog.txt" />\n    <link rel="stylesheet" type="text/css" media="print" href="')
        # SOURCE LINE 10
        __M_writer(unicode(rel_link(permalink, "/assets/css/print.css")))
        __M_writer(u'" title="blog.txt" />\n    <!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->\n    <!--[if lt IE 9]>\n      <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>\n    <![endif]-->\n')
        # SOURCE LINE 15
        if rss_link:
            # SOURCE LINE 16
            __M_writer(u'        ')
            __M_writer(unicode(rss_link))
            __M_writer(u'\n')
            # SOURCE LINE 17
        else:
            # SOURCE LINE 18
            for language in translations:
                # SOURCE LINE 19
                __M_writer(u'            <link rel="alternate" type="application/rss+xml" title="RSS (')
                __M_writer(unicode(language))
                __M_writer(u')" href="')
                __M_writer(unicode(_link("rss", None, lang)))
                __M_writer(u'">\n')
        # SOURCE LINE 22
        __M_writer(u'    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        # SOURCE LINE 23
        __M_writer(u'\n</head>\n<body>\n    <script type="text/javascript">\n        var addthis_config = { \'ui_language\': \'')
        # SOURCE LINE 27
        __M_writer(unicode(lang))
        __M_writer(u'\' };\n    </script>\n<body>\n<div id="wrapper">\n    <div id="container">\n        <div id="content">\n            <div id="header">\n                <h1 id="blog-title">\n                    <a href="')
        # SOURCE LINE 35
        __M_writer(unicode(blog_url))
        __M_writer(u'" title="')
        __M_writer(unicode(blog_title))
        __M_writer(u'">')
        __M_writer(unicode(blog_title))
        __M_writer(u'</a>\n                </h1>\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'belowtitle'):
            context['self'].belowtitle(**pageargs)
        

        # SOURCE LINE 48
        __M_writer(u'\n            </div>\n        <div class="hfeed">\n            <!--Body content-->\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 52
        __M_writer(u'\n            <!--End of body content-->\n        </div><!-- .hfeed -->\n    </div><!-- #content -->\n</div><!-- #container -->\n\n<div id="primary" class="sidebar">\n    <ul>\n')
        # SOURCE LINE 60
        for url, text in sidebar_links[lang]:
            # SOURCE LINE 61
            __M_writer(u'            <li><h3><a href="')
            __M_writer(unicode(rel_link(permalink, url)))
            __M_writer(u'">')
            __M_writer(unicode(text))
            __M_writer(u'</a></h3>\n')
        # SOURCE LINE 63
        __M_writer(u'        <li>')
        __M_writer(unicode(license))
        __M_writer(u'\n        <!-- social buttons -->\n        <!-- <li> -->\n        <!--     <div class="addthis_toolbox addthis_default_style" style="margin-bottom: 12px;"> -->\n        <!--     <a class="addthis_button_preferred_1"></a> -->\n        <!--     <a class="addthis_button_preferred_2"></a> -->\n        <!--     <a class="addthis_button_preferred_3"></a> -->\n        <!--     <a class="addthis_button_preferred_4"></a> -->\n        <!--     <a class="addthis_button_compact"></a> -->\n        <!--     <a class="addthis_counter addthis_bubble_style"></a> -->\n        <!--     </div> -->\n        <!--     <script type="text/javascript" src="http://s7.addthis.com/js/250/addthis_widget.js#pubid=ra-4f7088a56bb93798"></script> -->\n        <!-- <\\!-- End of social buttons -\\-> -->\n        <li>')
        # SOURCE LINE 76
        __M_writer(unicode(search_form))
        __M_writer(u'\n    </ul>\n</div><!-- #primary .sidebar -->\n\n<div id="footer">\n     <!-- <span class="vcard"><a class="url fn n" href="http://scottwallick.com/" title="scottwallick.com" rel="follow designer"><span class="given-name">Scott</span><span class="additional-name"> Allan</span><span class="family-name"> Wallick</span></a></span></span> -->\n    <small>')
        # SOURCE LINE 82
        __M_writer(unicode(content_footer))
        __M_writer(u'</small><p>\n</div><!-- #footer -->\n\n</div><!-- #wrapper -->\n    ')
        # SOURCE LINE 86
        __M_writer(unicode(analytics))
        __M_writer(u'\n</body><!-- end transmission -->\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_belowtitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        def belowtitle():
            return render_belowtitle(context)
        messages = context.get('messages', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 37
        __M_writer(u'\n')
        # SOURCE LINE 38
        if len(translations) > 1:
            # SOURCE LINE 39
            __M_writer(u'                <small>\n                    ')
            # SOURCE LINE 40
            __M_writer(unicode((messages[lang][u"Also available in: "])))
            __M_writer(u'\n')
            # SOURCE LINE 41
            for langname in translations.keys():
                # SOURCE LINE 42
                if langname != lang:
                    # SOURCE LINE 43
                    __M_writer(u'                            <a href="')
                    __M_writer(unicode(_link("index", None, langname)))
                    __M_writer(u'">')
                    __M_writer(unicode(messages[langname]["LANGUAGE"]))
                    __M_writer(u'</a>\n')
            # SOURCE LINE 46
            __M_writer(u'                </small>\n')
        # SOURCE LINE 48
        __M_writer(u'                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


