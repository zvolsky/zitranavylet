# -*- coding: utf-8 -*-

if 'mojeknihovna.eu' in request.env.http_host.lower():
    pass #redirect(URL('codex2020', 'default', 'index'))
elif 'sluzbicka.eu' in request.env.http_host.lower():
    pass #redirect(URL('sluzbicka', 'default', 'index'))
