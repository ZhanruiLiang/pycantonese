..  _data:

Corpus Data
===========

The CHAT Transcription Format
-----------------------------

PyCantonese adopts the CHAT format (as used in the CHILDES database for
language acquisition research) as the standard corpus format.
The choice is motivated by the fact that CHAT is widely used, well-documented,
and rich for linguistic annotations.

All built-in corpus datasets of PyCantonese are in the CHAT format.
Underlyingly, PyCantonese uses the Python library
`PyLangAcq <https://pylangacq.org/>`_ to parse CHAT data files.
For the bare minimum of the CHAT format that PyCantonese assumes,
see `here <https://pylangacq.org/read.html#chat-format>`_.


Accessing Built-in Data
-----------------------

Currently, PyCantonese comes with one built-in Cantonese corpus, the
150,000-word `Hong
Kong Cantonese Corpus <http://compling.hss.ntu.edu.sg/hkcancor/>`_ (HKCanCor)
by Kang Kwong Luke, via :func:`~pycantonese.hkcancor`:

.. code-block:: python

    >>> import pycantonese as pc
    >>> corpus = pc.hkcancor()

..  NOTE::

    HKCanCor is released under a CC BY license.
    If this corpus is used, the following should be cited:

    K. K. Luke and May L.Y. Wong (2015) The Hong Kong Cantonese Corpus:
    Design and Uses. *Journal of Chinese Linguistics* (to appear).

On the CHAT format of HKCanCor incorporated in PyCantonese,
please consult this
`readme <https://github.com/jacksonllee/pycantonese/blob/master/pycantonese/data/hkcancor/README.md>`_.

Accessing Custom Data
---------------------

If you have a Cantonese corpus in the CHAT format in your local drive and would
like to use PyCantonese to handle it, the function :func:`~pycantonese.read_chat`
is available for this purpose:

.. code-block:: python

    >>> import pycantonese as pc
    >>> corpus = pc.read_chat('path/to/files/*.cha')

If your CHAT data files have the extension name ``.cha`` and are all in
a single directory, then filename pattern matching with ``*`` can be used to
match all CHAT files in the specified directory.

:func:`~pycantonese.read_chat` has the optional parameter ``encoding`` which defaults to
``utf8`` for UTF-8 and can be overridden for another encoding if necessary.

If you are aware of other Cantonese corpora that could be incorporated into
PyCantonese for open access,
or if you are the owner of a Cantonese corpus and
would like to make it accessible
through PyCantonese, please contact `Jackson Lee <https://jacksonllee.com>`_.
