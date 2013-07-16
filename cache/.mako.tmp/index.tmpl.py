# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1373936473.499
_enable_loop = True
_template_filename = u'themes\\blogtxt\\templates/index.tmpl'
_template_uri = u'index.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content']


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
        lang = context.get('lang', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        def content():
            return render_content(context.locals_(__M_locals))
        disqus_forum = context.get('disqus_forum', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 49
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        def content():
            return render_content(context)
        disqus_forum = context.get('disqus_forum', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        for post in posts:
            # SOURCE LINE 5
            __M_writer(u'        <div class="post">\n            <h2><a href="')
            # SOURCE LINE 6
            __M_writer(unicode(post.permalink(lang)))
            __M_writer(u'">')
            __M_writer(unicode(post.title(lang)))
            __M_writer(u'</a></h2>\n            <div class="entry-content">\n                ')
            # SOURCE LINE 8
            __M_writer(unicode(post.text(lang,index_teasers)))
            __M_writer(u'\n            </div>\n            <div class="entry-meta">\n                <span class="meta-sep">|</span>\n                <span class="entry-date">')
            # SOURCE LINE 12
            __M_writer(unicode(messages[lang]["Posted"]))
            __M_writer(u': ')
            __M_writer(unicode(post.date))
            __M_writer(u'</span>\n                <span class="meta-sep">|</span>\n')
            # SOURCE LINE 14
            if disqus_forum:
                # SOURCE LINE 15
                __M_writer(u'                    <a href="')
                __M_writer(unicode(post.permalink(absolute=True)))
                __M_writer(u'#disqus_thread">Comments</a>\n')
            # SOURCE LINE 17
            __M_writer(u'            </div>\n        </div>\n')
        # SOURCE LINE 20
        __M_writer(u'    <div id="nav-below" class="navigation">\n')
        # SOURCE LINE 21
        if prevlink:
            # SOURCE LINE 22
            __M_writer(u'            <div class="nav-previous">\n                <a href="')
            # SOURCE LINE 23
            __M_writer(unicode(prevlink))
            __M_writer(u'">&larr; Newer posts</a>\n            </div>\n')
        # SOURCE LINE 26
        if nextlink:
            # SOURCE LINE 27
            __M_writer(u'            <div class="nav-next">\n                <a href="')
            # SOURCE LINE 28
            __M_writer(unicode(nextlink))
            __M_writer(u'">Older posts &rarr;</a>\n            </div>\n')
        # SOURCE LINE 31
        __M_writer(u'    </div>\n\n    <!-- %if disqus_forum: -->\n    <!--     <script type="text/javascript"> -->\n    <!--     //<![CDATA[ -->\n    <!--     (function() { -->\n    <!--         var links = document.getElementsByTagName(\'a\'); -->\n    <!--         var query = \'?\'; -->\n    <!--         for(var i = 0; i < links.length; i++) { -->\n    <!--         if(links[i].href.indexOf(\'#disqus_thread\') >= 0) { -->\n    <!--             query += \'url\' + i + \'=\' + encodeURIComponent(links[i].href) + \'&\'; -->\n    <!--         } -->\n    <!--         } -->\n    <!--         document.write(\'<script charset="utf-8" type="text/javascript" src="http://disqus.com/forums/lateralopinion/get_num_replies.js\' + query + \'"></\' + \'script>\'); -->\n    <!--     })(); -->\n    <!--     //]]> -->\n    <!--     </script> -->\n    <!-- %endif -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


