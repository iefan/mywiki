# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1377247349.934139
_enable_loop = True
_template_filename = u'themes/blogtxt/templates/post.tmpl'
_template_uri = u'post.tmpl'
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
        permalink = context.get('permalink', UNDEFINED)
        title = context.get('title', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        len = context.get('len', UNDEFINED)
        def content():
            return render_content(context.locals_(__M_locals))
        link = context.get('link', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        disqus_forum = context.get('disqus_forum', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 46
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        title = context.get('title', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        len = context.get('len', UNDEFINED)
        def content():
            return render_content(context)
        link = context.get('link', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        disqus_forum = context.get('disqus_forum', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n    <div id="post-')
        # SOURCE LINE 4
        __M_writer(unicode(post.pagenames[lang]))
        __M_writer(u'" class="post">\n      <h2  class="post_title" align="center"><a href=\'')
        # SOURCE LINE 5
        __M_writer(unicode(permalink))
        __M_writer(u"'>")
        __M_writer(unicode(title))
        __M_writer(u'</a></h2>\n      <br/>\n        <div class="archive-meta" align="center">\n          <span class="meta-sep">|</span>\n')
        # SOURCE LINE 9
        if link:
            # SOURCE LINE 10
            __M_writer(u"                    <p><a href='")
            __M_writer(unicode(link))
            __M_writer(u"'>")
            __M_writer(unicode(messages[lang]["Original site"]))
            __M_writer(u'</a></p>\n                    <span class="meta-sep">|</span>\n')
        # SOURCE LINE 13
        __M_writer(u'            ')
        __M_writer(unicode(messages[lang]["Posted"]))
        __M_writer(u': ')
        __M_writer(unicode(post.date))
        __M_writer(u'<span class="meta-sep">|</span>\n            <!-- <span class="meta-sep">|</span> -->\n')
        # SOURCE LINE 15
        if len(translations) > 1:
            # SOURCE LINE 16
            for langname in translations.keys():
                # SOURCE LINE 17
                if langname != lang:
                    # SOURCE LINE 18
                    __M_writer(u'                        <a href="')
                    __M_writer(unicode(post.permalink(langname)))
                    __M_writer(u'">')
                    __M_writer(unicode(messages[langname][u"Read in english"]))
                    __M_writer(u'</a>\n                        <span class="meta-sep">|</span>\n')
        # SOURCE LINE 23
        __M_writer(u'            <a href="')
        __M_writer(unicode(post.pagenames[lang]+".txt"))
        __M_writer(u'">reSt</a>\n            <span class="meta-sep">|</span>\n')
        # SOURCE LINE 25
        for tag in post.tags:
            # SOURCE LINE 26
            __M_writer(u'                    <a href="')
            __M_writer(unicode(_link("tag", tag, lang)))
            __M_writer(u'"><span class="badge badge-info">')
            __M_writer(unicode(tag))
            __M_writer(u'</span></a>\n')
        # SOURCE LINE 28
        __M_writer(u'            <span class="entry-tags">\n            </span>\n        </div>\n        <div class="entry-content" >\n            ')
        # SOURCE LINE 32
        __M_writer(unicode(post.text(lang)))
        __M_writer(u'\n        </div>\n    </div>\n    <!-- %if disqus_forum: -->\n    <!--     <\\!-- Disqus comments !-\\-> -->\n    <!--     <script type="text/javascript"> -->\n    <!--         var disqus_url = \'')
        # SOURCE LINE 38
        __M_writer(unicode(post.permalink(absolute=True)))
        __M_writer(u'\'; -->\n    <!--         var disqus_developer = 1; -->\n    <!--     </script> -->\n    <!--     <div id="disqus_thread"></div> -->\n    <!--     <script type="text/javascript" src="http://disqus.com/forums/')
        # SOURCE LINE 42
        __M_writer(unicode(disqus_forum))
        __M_writer(u'/embed.js"></script> -->\n    <!--     <noscript><a href="http://disqus.com/forums/')
        # SOURCE LINE 43
        __M_writer(unicode(disqus_forum))
        __M_writer(u'/?url=ref">View the discussion thread.</a></noscript><a href="http://disqus.com" class="dsq-brlink">blog comments powered by <span class="logo-disqus">Disqus</span></a> -->\n    <!--     <\\!-- End of Disqus comments !-\\-> -->\n    <!-- %endif -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


