import os, json, sys
import tornado.web

path = json.loads(open(os.path.join(sys.prefix, "etc", "jupyter", "jupyter-data-directory.json")).read())["path"].format(prefix=sys.prefix)

def url_path_join(*pieces):
    """
    Duplicated from Jupyter Server
    """
    initial = pieces[0].startswith('/')
    final = pieces[-1].endswith('/')
    stripped = [s.strip('/') for s in pieces]
    result = '/'.join(s for s in stripped if s)
    if initial: result = '/' + result
    if final: result = result + '/'
    if result == '//': result = '/'
    return result

def _load_jupyter_server_extension(nb_server_app):
    """
    Called when the extension is loaded.

    Args:
        nb_server_app (NotebookWebApplication): handle to the Notebook webserver instance.
    """
    web_app = nb_server_app.web_app
    host_pattern = '.*$'
    route_pattern = url_path_join(web_app.settings['base_url'], r'/data/(.*)')
    web_app.add_handlers(host_pattern, [(route_pattern,
                                        tornado.web.StaticFileHandler,
                                        {'path': path}
                                        )]
                        )

# for backward compatibility with classic jupyter notebook
load_jupyter_server_extension = _load_jupyter_server_extension

