# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.protocols.wrappers import (
    HTTPStatus, abort, redirect, with_pool, with_transaction)
from trytond.wsgi import app


@app.route('/s/<base64:database_name>$<shortened>')
@with_pool
@with_transaction(readonly=False)
def shortened(request, pool, shortened):
    ShortenedURL = pool.get('web.shortened_url')

    try:
        shortened_url = ShortenedURL.get(shortened)
    except IndexError:
        abort(HTTPStatus.NOT_FOUND)

    return redirect(shortened_url.access(), code=301)
